package io.kaarkhana.examples.s08;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpTimeoutException;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.Objects;

/**
 * S8 improved implementation: explicit timeout, status handling and domain errors. The
 * behaviour is proven against a real local HTTP server in {@code PriceClientIntegrationTest}.
 */
public class PriceClient {
    private final HttpClient client;
    private final URI baseUri;
    private final Duration timeout;

    public PriceClient(HttpClient client, URI baseUri, Duration timeout) {
        this.client = Objects.requireNonNull(client);
        this.baseUri = Objects.requireNonNull(baseUri);
        this.timeout = Objects.requireNonNull(timeout);
    }

    public long fetchPriceCents(String sku) {
        Objects.requireNonNull(sku, "sku");
        String path = "/prices/" + URLEncoder.encode(sku, StandardCharsets.UTF_8);
        HttpRequest request = HttpRequest.newBuilder(baseUri.resolve(path)).timeout(timeout).GET().build();
        HttpResponse<String> response;
        try {
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (HttpTimeoutException e) {
            throw new PriceServiceException("pricing service timed out after " + timeout.toMillis() + " ms", e);
        } catch (IOException e) {
            throw new PriceServiceException("pricing service unreachable", e);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new PriceServiceException("interrupted while calling pricing service", e);
        }

        int status = response.statusCode();
        if (status == 404) {
            throw new PriceNotFoundException(sku);
        }
        if (status != 200) {
            throw new PriceServiceException("pricing service answered HTTP " + status);
        }
        try {
            return Long.parseLong(response.body().trim());
        } catch (NumberFormatException e) {
            throw new PriceServiceException("malformed price in response: '" + response.body() + "'", e);
        }
    }
}
