package io.kaarkhana.examples.s06;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.NullSource;
import org.junit.jupiter.params.provider.ValueSource;

class ShippingFeeTest {

    // SC-01 .. SC-03: domestic fee and the free shipping boundary
    @ParameterizedTest(name = "DE order of {0} cents pays {1}")
    @CsvSource({"1,499", "9999,499", "10000,0", "10001,0"})
    void domesticFeeAroundTheFreeShippingThreshold(long total, long expected) {
        assertEquals(expected, ShippingFee.feeCents(total, "DE"));
    }

    // SC-04 .. SC-05: international orders are never free
    @ParameterizedTest
    @CsvSource({"FR,5000", "US,1000000"})
    void internationalOrdersPayTheFlatFeeEvenFarAboveTheThreshold(String country, long total) {
        assertEquals(1_499, ShippingFee.feeCents(total, country));
    }

    // SC-07: invalid totals
    @ParameterizedTest
    @ValueSource(longs = {0, -1, -10_000})
    void nonPositiveTotalsAreRejected(long bad) {
        var ex = assertThrows(IllegalArgumentException.class, () -> ShippingFee.feeCents(bad, "DE"));
        assertEquals("totalCents must be positive, got " + bad, ex.getMessage());
    }

    // SC-08: invalid country codes
    @ParameterizedTest
    @ValueSource(strings = {"", "D", "DEU", "de", "D1"})
    void invalidCountryCodesAreRejected(String bad) {
        assertThrows(IllegalArgumentException.class, () -> ShippingFee.feeCents(5_000, bad));
    }

    @ParameterizedTest
    @NullSource
    void nullCountryIsRejected(String bad) {
        assertThrows(IllegalArgumentException.class, () -> ShippingFee.feeCents(5_000, bad));
    }

    // --- Documented defects of the initial implementation (characterisation) ---

    @Test
    void initialDefectChargesShippingAtExactlyTheThreshold() {
        assertEquals(4.99, ShippingFeeInitial.fee(100, "DE")); // should be free
    }

    @Test
    void initialDefectIgnoresCountry() {
        assertEquals(4.99, ShippingFeeInitial.fee(5, "US")); // should be 14.99
    }

    @Test
    void initialDefectAcceptsNegativeTotals() {
        assertEquals(4.99, ShippingFeeInitial.fee(-50, "DE"));
    }
}
