package io.kaarkhana.examples.s03;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class SeniorDiscountTest {

    @ParameterizedTest
    @CsvSource({"0,false", "64,false", "65,true", "66,true", "100,true"})
    void eligibilityBelowAtAndAboveTheBoundary(int age, boolean expected) {
        assertEquals(expected, SeniorDiscount.isSenior(age));
    }

    @Test
    void negativeAgeIsRejected() {
        var ex = assertThrows(IllegalArgumentException.class, () -> SeniorDiscount.isSenior(-1));
        assertEquals("age must not be negative, got -1", ex.getMessage());
    }

    // --- Documented defect of the initial implementation (characterisation) ---

    @Test
    void initialDefectExcludesExactly65() {
        assertFalse(SeniorDiscountInitial.isSenior(65)); // requirement says 65 is eligible
    }
}
