package io.kaarkhana.examples.s04;

/**
 * S4 initial implementation: parse an order quantity from user input.
 *
 * <p>PROBLEM: {@code catch (Exception e) { return 0; }} swallows every failure and invents a
 * value. "abc" and null become quantity 0, the cause is lost, and "-5" is accepted because
 * nothing checks the range.
 */
public final class QuantityParserInitial {
    private QuantityParserInitial() {}

    public static int parse(String text) {
        try {
            return Integer.parseInt(text.trim());
        } catch (Exception e) {
            return 0;
        }
    }
}
