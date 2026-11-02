package io.kaarkhana.examples.s07;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.LongUnaryOperator;
import org.junit.jupiter.api.Test;

/** S7: both suites execute every line; only one of them is any good. */
class LateFeeMutationTest {

    /** The weak suite: executes every line, asserts almost nothing. */
    private static final Consumer<LongUnaryOperator> WEAK = fn -> {
        assertTrue(fn.applyAsLong(10) > 0);
        assertTrue(fn.applyAsLong(0) >= 0);
        assertTrue(fn.applyAsLong(1000) > 0);
    };

    /** The strong suite: exact values on both sides of every rule. */
    private static final Consumer<LongUnaryOperator> STRONG = fn -> {
        assertEquals(0, fn.applyAsLong(0));
        assertEquals(0, fn.applyAsLong(3)); // last grace day
        assertEquals(50, fn.applyAsLong(4)); // first charged day
        assertEquals(350, fn.applyAsLong(10)); // 7 days * 50
        assertEquals(2_000, fn.applyAsLong(43)); // exactly reaches the cap
        assertEquals(2_000, fn.applyAsLong(44)); // would be 2050 without the cap
        assertEquals(2_000, fn.applyAsLong(1000));
    };

    private static List<String> survivors(Consumer<LongUnaryOperator> suite) {
        List<String> alive = new ArrayList<>();
        LateFee.MUTANTS.forEach((name, mutant) -> {
            try {
                suite.accept(mutant);
                alive.add(name);
            } catch (AssertionError killed) {
                // the suite noticed the change: mutant killed
            }
        });
        return alive;
    }

    @Test
    void bothSuitesPassOnTheOriginalCode() {
        WEAK.accept(LateFee::feeCents);
        STRONG.accept(LateFee::feeCents);
    }

    @Test
    void weakSuiteLetsEveryMutantSurvive() {
        assertEquals(new ArrayList<>(LateFee.MUTANTS.keySet()), survivors(WEAK));
    }

    @Test
    void strongSuiteKillsEveryMutant() {
        assertEquals(List.of(), survivors(STRONG));
    }
}
