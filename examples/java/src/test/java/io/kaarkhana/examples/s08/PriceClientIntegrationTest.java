package io.kaarkhana.examples.s08;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpTimeoutException;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

/** Unit test with a mock (passes either way) and integration tests against a real local server. */
@Tag("integration")
class PriceClientIntegrationTest {
    private static HttpServer server;
    private static URI baseUri;
    private static final HttpClient HTTP = HttpClient.newHttpClient();

    @BeforeAll
    static void startServer() throws IOException {
        server = HttpServer.create(new InetSocketAddress(InetAddress.getLoopbackAddress(), 0), 0);
        server.createContext("/prices/ok", ex -> respond(ex, 200, "1250"));
        server.createContext("/prices/missing", ex -> respond(ex, 404, "not found"));
        server.createContext("/prices/boom", ex -> respond(ex, 500, "internal error"));
        server.createContext("/prices/garbage", ex -> respond(ex, 200, "twelve fifty"));
        server.createContext("/prices/slow", ex -> {
            try {
                Thread.sleep(1_500);
                respond(ex, 200, "1250");
            } catch (InterruptedException | IOException ignored) {
                // the client gave up before we answered
            }
        });
        server.start();
        baseUri = URI.create("http://127.0.0.1:" + server.getAddress().getPort());
    }

    @AfterAll
    static void stopServer() {
        server.stop(0);
    }

    private static void respond(HttpExchange exchange, int status, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(status, bytes.length);
        try (var out = exchange.getResponseBody()) {
            out.write(bytes);
        }
    }

    private PriceClient client() {
        return new PriceClient(HTTP, baseUri, Duration.ofSeconds(2));
    }

    private PriceClient impatientClient() {
        return new PriceClient(HTTP, baseUri, Duration.ofMillis(300));
    }

    // --- Why the mocked unit test is not enough ---------------------------------------------

    @Test
    @SuppressWarnings("unchecked")
    void unitTestWithMockedHttpClientPassesForTheInitialImplementation() throws Exception {
        HttpClient mockClient = mock(HttpClient.class);
        HttpResponse<String> response = mock(HttpResponse.class);
        when(response.body()).thenReturn("1250");
        when(mockClient.send(any(HttpRequest.class), any(HttpResponse.BodyHandler.class))).thenReturn(response);

        var initial = new PriceClientInitial(mockClient, URI.create("http://unused.invalid"));

        assertEquals(1250, initial.fetchPriceCents("ok"));
    }

    @Test
    void initialDefectNotFoundSurfacesAsNumberFormatException() {
        var initial = new PriceClientInitial(HTTP, baseUri);
        assertThrows(NumberFormatException.class, () -> initial.fetchPriceCents("missing"));
    }

    @Test
    void initialDefectServerErrorSurfacesAsNumberFormatException() {
        var initial = new PriceClientInitial(HTTP, baseUri);
        assertThrows(NumberFormatException.class, () -> initial.fetchPriceCents("boom"));
    }

    // --- Integration tests of the improved client ---------------------------------------------

    @Test
    void returnsThePriceFromARealResponse() {
        assertEquals(1250, client().fetchPriceCents("ok"));
    }

    @Test
    void notFoundBecomesPriceNotFound() {
        var ex = assertThrows(PriceNotFoundException.class, () -> client().fetchPriceCents("missing"));
        assertEquals("no price for sku: missing", ex.getMessage());
    }

    @Test
    void serverErrorBecomesPriceServiceException() {
        var ex = assertThrows(PriceServiceException.class, () -> client().fetchPriceCents("boom"));
        assertEquals("pricing service answered HTTP 500", ex.getMessage());
    }

    @Test
    void malformedBodyBecomesPriceServiceExceptionWithCause() {
        var ex = assertThrows(PriceServiceException.class, () -> client().fetchPriceCents("garbage"));
        assertInstanceOf(NumberFormatException.class, ex.getCause());
        assertTrue(ex.getMessage().contains("twelve fifty"));
    }

    @Test
    void slowResponseTimesOutWithinTheConfiguredLimit() {
        long start = System.nanoTime();
        var ex = assertThrows(PriceServiceException.class, () -> impatientClient().fetchPriceCents("slow"));
        long elapsedMs = Duration.ofNanos(System.nanoTime() - start).toMillis();
        assertInstanceOf(HttpTimeoutException.class, ex.getCause());
        assertTrue(elapsedMs < 1_200, "should give up long before the server answers, took " + elapsedMs + " ms");
    }

    @Test
    void unreachableServiceBecomesPriceServiceException() {
        var unreachable = new PriceClient(HTTP, URI.create("http://127.0.0.1:1"), Duration.ofMillis(300));
        assertThrows(PriceServiceException.class, () -> unreachable.fetchPriceCents("ok"));
    }
}
