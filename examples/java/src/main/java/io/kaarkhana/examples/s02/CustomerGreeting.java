package io.kaarkhana.examples.s02;

import java.util.Objects;

/**
 * S2 improved implementation.
 *
 * <p>Requirement used in this example (stated, not invented by the code): an unknown customer
 * is an error; a customer with a missing or blank name is greeted as "Hello, customer". The
 * default exists because the requirement says so. Without that sentence the correct move is to
 * ask, not to choose a default.
 */
public class CustomerGreeting {
    private final CustomerRepository repository;

    public CustomerGreeting(CustomerRepository repository) {
        this.repository = Objects.requireNonNull(repository, "repository");
    }

    public String greetingFor(String id) {
        Objects.requireNonNull(id, "id");
        Customer customer = repository.findById(id).orElseThrow(() -> new CustomerNotFoundException(id));
        String name = customer.name() == null ? "" : customer.name().trim();
        return name.isEmpty() ? "Hello, customer" : "Hello, " + name;
    }
}
