package io.kaarkhana.examples.s06;

import java.util.regex.Pattern;

/** S6 improved implementation, produced by the TDD cycles in examples/end_to_end. Money is long cents. */
public final class ShippingFee {
    public static final String DOMESTIC_COUNTRY = "DE";
    public static final long DOMESTIC_FEE_CENTS = 499;
    public static final long FREE_SHIPPING_THRESHOLD_CENTS = 10_000;
    public static final long INTERNATIONAL_FEE_CENTS = 1_499;

    private static final Pattern COUNTRY = Pattern.compile("[A-Z]{2}");

    private ShippingFee() {}

    public static long feeCents(long totalCents, String country) {
        if (totalCents < 1) {
            throw new IllegalArgumentException("totalCents must be positive, got " + totalCents);
        }
        if (country == null || !COUNTRY.matcher(country).matches()) {
            throw new IllegalArgumentException("country must be a two letter upper case code, got " + country);
        }
        if (!DOMESTIC_COUNTRY.equals(country)) {
            return INTERNATIONAL_FEE_CENTS;
        }
        return totalCents >= FREE_SHIPPING_THRESHOLD_CENTS ? 0 : DOMESTIC_FEE_CENTS;
    }
}
