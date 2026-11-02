package io.kaarkhana.examples.s02;

public class CustomerNotFoundException extends RuntimeException {
    public CustomerNotFoundException(String id) {
        super("customer not found: " + id);
    }
}
