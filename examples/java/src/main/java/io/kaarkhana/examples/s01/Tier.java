package io.kaarkhana.examples.s01;

/**
 * S1 improved implementation: the set of tiers is a type.
 *
 * <p>Why not "just add an else": {@code else return 0.0} would turn a misspelt tier into "no
 * discount" and hide the data problem. Parsing rejects anything outside the three tiers defined
 * by the requirement, and the {@code switch} over the enum has no default so the compiler
 * forces a decision whenever a tier is added.
 */
public enum Tier {
    BASIC,
    SILVER,
    GOLD;

    public static Tier parse(String text) {
        if (text != null) {
            for (Tier tier : values()) {
                if (tier.name().equals(text)) {
                    return tier;
                }
            }
        }
        throw new UnknownTierException("unknown loyalty tier: " + (text == null ? "null" : "'" + text + "'"));
    }

    public double discountRate() {
        return switch (this) {
            case BASIC -> 0.0;
            case SILVER -> 0.05;
            case GOLD -> 0.10;
        };
    }

    public long priceAfterDiscount(long priceCents) {
        return priceCents - Math.round(priceCents * discountRate());
    }

    public static class UnknownTierException extends IllegalArgumentException {
        public UnknownTierException(String message) {
            super(message);
        }
    }
}
