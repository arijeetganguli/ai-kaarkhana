package io.kaarkhana.examples.s02;

import java.util.Optional;

/** Absence is part of the type: callers cannot forget to handle it. */
public interface CustomerRepository {
    Optional<Customer> findById(String id);
}
