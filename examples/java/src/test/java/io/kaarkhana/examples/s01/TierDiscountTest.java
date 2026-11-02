package io.kaarkhana.examples.s01;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.NullSource;
import org.junit.jupiter.params.provider.ValueSource;

class TierDiscountTest {

    @ParameterizedTest
    @CsvSource({"BASIC,0.0", "SILVER,0.05", "GOLD,0.10"})
    void knownTiersHaveTheirDocumentedRate(String tier, double rate) {
        assertEquals(rate, Tier.parse(tier).discountRate());
    }

    @ParameterizedTest
    @ValueSource(strings = {"PLATINUM", "gold", "", " GOLD"})
    void unknownTierIsRejectedWithTheValueInTheMessage(String bad) {
        var ex = assertThrows(Tier.UnknownTierException.class, () -> Tier.parse(bad));
        assertEquals("unknown loyalty tier: '" + bad + "'", ex.getMessage());
    }

    @ParameterizedTest
    @NullSource
    void nullTierIsRejected(String bad) {
        assertThrows(Tier.UnknownTierException.class, () -> Tier.parse(bad));
    }

    @Test
    void priceAfterDiscountAppliesTheTierRate() {
        assertEquals(9_000, Tier.GOLD.priceAfterDiscount(10_000));
        assertEquals(9_500, Tier.SILVER.priceAfterDiscount(10_000));
        assertEquals(10_000, Tier.BASIC.priceAfterDiscount(10_000));
    }

    // --- Documented defects of the initial implementation (characterisation) ---

    @Test
    void initialDefectReturnsNullForUnknownTier() {
        assertNull(TierDiscountInitial.discountRate("PLATINUM"));
    }

    @Test
    void initialDefectFailsFarFromTheCauseWithANullPointerException() {
        assertThrows(NullPointerException.class, () -> TierDiscountInitial.priceAfterDiscount(10_000, "PLATINUM"));
    }
}
