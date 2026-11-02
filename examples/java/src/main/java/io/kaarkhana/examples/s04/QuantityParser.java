package io.kaarkhana.examples.s04;

/**
 * S4 improved implementation. Requirement: a quantity is a whole number of at least 1.
 *
 * <p>Invalid input raises a specific exception that names the input and keeps the original
 * exception as its cause.
 */
public final class QuantityParser {
    private QuantityParser() {}

    public static int parse(String text) {
        if (text == null) {
            throw new InvalidQuantityException("quantity must not be null");
        }
        int value;
        try {
            value = Integer.parseInt(text.trim());
        } catch (NumberFormatException e) {
            throw new InvalidQuantityException("not a whole number: '" + text + "'", e);
        }
        if (value < 1) {
            throw new InvalidQuantityException("quantity must be at least 1, got " + value);
        }
        return value;
    }
}
