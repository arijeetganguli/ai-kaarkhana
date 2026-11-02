package io.kaarkhana.examples.s03;

/**
 * S3 initial implementation: senior discount eligibility. Requirement: aged 65 or older.
 *
 * <p>PROBLEM: {@code >} excludes exactly 65. Tests with typical ages (30, 70) pass, so the
 * off-by-one survives until a 65 year old customer complains.
 */
public final class SeniorDiscountInitial {
    private SeniorDiscountInitial() {}

    public static boolean isSenior(int age) {
        return age > 65;
    }
}
