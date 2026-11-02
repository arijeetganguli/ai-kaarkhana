package io.kaarkhana.examples.s08;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

/**
 * S8 initial implementation: fetch a price in cents from a pricing service.
 *
 * <p>PROBLEMS: no request timeout; the status code is never checked, so the body of a 404 or a
 * 500 is parsed as if it were a price; failures surface as NumberFormatException instead of a
 * domain error. A unit test that mocks {@link HttpClient} cannot see any of this.
 */
public class PriceClientInitial {
    private final HttpClient client;
    private final URI baseUri;

    public PriceClientInitial(HttpClient client, URI baseUri) {
        this.client = client;
        this.baseUri = baseUri;
    }

    public long fetchPriceCents(String sku) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder(baseUri.resolve("/prices/" + sku)).GET().build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        return Long.parseLong(response.body().trim());
    }
}
