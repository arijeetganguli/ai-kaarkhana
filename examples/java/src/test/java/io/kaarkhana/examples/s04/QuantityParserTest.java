package io.kaarkhana.examples.s04;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

class QuantityParserTest {

    @ParameterizedTest
    @CsvSource({"1,1", "' 12 ',12", "007,7"})
    void validQuantities(String text, int expected) {
        assertEquals(expected, QuantityParser.parse(text));
    }

    @ParameterizedTest
    @ValueSource(strings = {"abc", "", "1.5", "0", "-5"})
    void invalidTextRaisesASpecificException(String text) {
        assertThrows(InvalidQuantityException.class, () -> QuantityParser.parse(text));
    }

    @Test
    void nullIsRejected() {
        var ex = assertThrows(InvalidQuantityException.class, () -> QuantityParser.parse(null));
        assertEquals("quantity must not be null", ex.getMessage());
    }

    @Test
    void originalExceptionIsPreservedAsTheCause() {
        var ex = assertThrows(InvalidQuantityException.class, () -> QuantityParser.parse("abc"));
        assertInstanceOf(NumberFormatException.class, ex.getCause());
        assertEquals("not a whole number: 'abc'", ex.getMessage());
    }

    // --- Documented defects of the initial implementation (characterisation) ---

    @Test
    void initialDefectInventsZeroForGarbageAndNull() {
        assertEquals(0, QuantityParserInitial.parse("abc"));
        assertEquals(0, QuantityParserInitial.parse(null));
    }

    @Test
    void initialDefectAcceptsNegativeQuantities() {
        assertEquals(-5, QuantityParserInitial.parse("-5"));
    }
}
