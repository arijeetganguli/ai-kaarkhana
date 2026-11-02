package io.kaarkhana.examples.s07;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.function.LongUnaryOperator;

/**
 * S7 code under test: late fee for a returned item.
 *
 * <p>Requirement: the first 3 days late are a grace period (no fee); from day 4 the fee is 50
 * cents per day beyond the grace period; the fee never exceeds 2000 cents.
 *
 * <p>{@link #MUTANTS} are hand-written mutants: the original with exactly one small change, the
 * kind a mutation testing tool such as PIT generates automatically.
 *
 * <p>Not included on purpose: changing {@code daysLate <= 3} to {@code daysLate < 3} changes the
 * result only for 3 days, where both branches return 0. It is an equivalent mutant: no test can
 * kill it.
 */
public final class LateFee {
    static final long GRACE_DAYS = 3;
    static final long RATE = 50;
    static final long CAP = 2_000;

    private LateFee() {}

    public static long feeCents(long daysLate) {
        if (daysLate <= GRACE_DAYS) {
            return 0;
        }
        return Math.min((daysLate - GRACE_DAYS) * RATE, CAP);
    }

    public static final Map<String, LongUnaryOperator> MUTANTS = new LinkedHashMap<>();

    static {
        MUTANTS.put("m1_grace_boundary_shifted", d -> d <= GRACE_DAYS + 1 ? 0 : Math.min((d - GRACE_DAYS) * RATE, CAP));
        MUTANTS.put("m2_off_by_one_day", d -> d <= GRACE_DAYS ? 0 : Math.min((d - GRACE_DAYS + 1) * RATE, CAP));
        MUTANTS.put("m3_rate_changed", d -> d <= GRACE_DAYS ? 0 : Math.min((d - GRACE_DAYS) * (RATE + 1), CAP));
        MUTANTS.put("m4_cap_changed", d -> d <= GRACE_DAYS ? 0 : Math.min((d - GRACE_DAYS) * RATE, CAP + 1));
        MUTANTS.put("m5_cap_removed", d -> d <= GRACE_DAYS ? 0 : (d - GRACE_DAYS) * RATE);
    }
}
