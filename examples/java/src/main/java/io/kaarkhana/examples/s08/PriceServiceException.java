package io.kaarkhana.examples.s08;

/** The pricing service failed, timed out or answered with something we cannot use. */
public class PriceServiceException extends RuntimeException {
    public PriceServiceException(String message) {
        super(message);
    }

    public PriceServiceException(String message, Throwable cause) {
        super(message, cause);
    }
}
