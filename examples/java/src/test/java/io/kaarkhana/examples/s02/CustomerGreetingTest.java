package io.kaarkhana.examples.s02;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.NullAndEmptySource;
import org.junit.jupiter.params.provider.ValueSource;

class CustomerGreetingTest {
    private CustomerRepository repository;
    private CustomerGreeting greeting;

    @BeforeEach
    void setUp() {
        repository = mock(CustomerRepository.class);
        greeting = new CustomerGreeting(repository);
    }

    @Test
    void greetsByTrimmedName() {
        when(repository.findById("42")).thenReturn(Optional.of(new Customer("  Asha ")));
        assertEquals("Hello, Asha", greeting.greetingFor("42"));
    }

    @ParameterizedTest
    @NullAndEmptySource
    @ValueSource(strings = {"   "})
    void missingOrBlankNameUsesTheSpecifiedDefault(String name) {
        when(repository.findById("42")).thenReturn(Optional.of(new Customer(name)));
        assertEquals("Hello, customer", greeting.greetingFor("42"));
    }

    @Test
    void unknownCustomerIsRejectedWithTheIdInTheMessage() {
        when(repository.findById("404")).thenReturn(Optional.empty());
        var ex = assertThrows(CustomerNotFoundException.class, () -> greeting.greetingFor("404"));
        assertEquals("customer not found: 404", ex.getMessage());
        verify(repository).findById("404");
    }

    @Test
    void nullIdIsRejectedBeforeTheRepositoryIsCalled() {
        assertThrows(NullPointerException.class, () -> greeting.greetingFor(null));
        org.mockito.Mockito.verifyNoInteractions(repository);
    }

    // --- Documented defects of the initial implementation (characterisation) ---

    @Test
    void initialDefectUnknownCustomerCausesNullPointerException() {
        var legacy = new CustomerGreetingInitial(id -> null);
        assertThrows(NullPointerException.class, () -> legacy.greetingFor("404"));
    }

    @Test
    void initialDefectMissingNameCausesNullPointerException() {
        var legacy = new CustomerGreetingInitial(id -> new CustomerGreetingInitial.Customer(null));
        assertThrows(NullPointerException.class, () -> legacy.greetingFor("42"));
    }
}
