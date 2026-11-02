package io.kaarkhana.examples.s08;

/** The pricing service has no price for the requested SKU (HTTP 404). */
public class PriceNotFoundException extends RuntimeException {
    public PriceNotFoundException(String sku) {
        super("no price for sku: " + sku);
    }
}
