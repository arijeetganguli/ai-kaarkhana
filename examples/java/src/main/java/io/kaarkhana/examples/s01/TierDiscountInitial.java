package io.kaarkhana.examples.s01;

/**
 * S1 initial implementation: discount rate by loyalty tier.
 *
 * <p>PROBLEM: the if/else-if chain has no final branch, so an unknown tier leaves
 * {@code rate} as null. The caller unboxes it in {@link #priceAfterDiscount} and gets a
 * NullPointerException with no hint about which tier was invalid.
 */
public final class TierDiscountInitial {
    private TierDiscountInitial() {}

    public static Double discountRate(String tier) {
        Double rate = null;
        if ("GOLD".equals(tier)) {
            rate = 0.10;
        } else if ("SILVER".equals(tier)) {
            rate = 0.05;
        } else if ("BASIC".equals(tier)) {
            rate = 0.0;
        }
        return rate;
    }

    public static long priceAfterDiscount(long priceCents, String tier) {
        return priceCents - Math.round(priceCents * discountRate(tier));
    }
}
