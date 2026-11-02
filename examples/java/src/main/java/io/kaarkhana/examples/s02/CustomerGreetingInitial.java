package io.kaarkhana.examples.s02;

/**
 * S2 initial implementation: greeting for a customer looked up by id.
 *
 * <p>PROBLEM: the repository returns null for an unknown id, and the customer name may be
 * null for an incomplete profile. Both end in a NullPointerException on the same line, with
 * no indication of which id or which rule was violated.
 */
public class CustomerGreetingInitial {

    public record Customer(String name) {}

    public interface LegacyCustomerRepository {
        Customer findById(String id); // returns null when not found
    }

    private final LegacyCustomerRepository repository;

    public CustomerGreetingInitial(LegacyCustomerRepository repository) {
        this.repository = repository;
    }

    public String greetingFor(String id) {
        return "Hello, " + repository.findById(id).name().trim();
    }
}
