package io.kaarkhana.examples.s03;

/** S3 improved implementation: named inclusive boundary and rejection of invalid ages. */
public final class SeniorDiscount {
    public static final int SENIOR_AGE = 65;

    private SeniorDiscount() {}

    public static boolean isSenior(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("age must not be negative, got " + age);
        }
        return age >= SENIOR_AGE;
    }
}
