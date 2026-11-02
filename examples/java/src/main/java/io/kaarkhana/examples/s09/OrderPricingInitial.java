package io.kaarkhana.examples.s09;

import java.util.List;

/**
 * S9 initial implementation: order pricing with nested conditionals.
 *
 * <p>Behaviour (as implemented; confirmed by characterisation tests): tier discount GOLD 10
 * percent, SILVER 5 percent, anything else 0; bulk discount at 10 or more units (5 percent for
 * GOLD and SILVER, 3 percent otherwise) applied after the tier discount; promo WELCOME takes 500
 * cents off when the undiscounted subtotal is at least 2000, never below zero.
 *
 * <p>PROBLEM: four levels of nesting mix three rules. Adding a rule means re-reading all of it.
 */
public final class OrderPricingInitial {
    private OrderPricingInitial() {}

    public static long price(List<OrderPricing.Item> items, String tier, String promoCode) {
        long subtotal = 0;
        long quantity = 0;
        for (OrderPricing.Item item : items) {
            subtotal += item.unitPriceCents() * item.quantity();
            quantity += item.quantity();
        }

        long total = subtotal;
        if ("GOLD".equals(tier)) {
            total = total - total * 10 / 100;
        } else {
            if ("SILVER".equals(tier)) {
                total = total - total * 5 / 100;
            }
        }

        if (quantity >= 10) {
            if ("GOLD".equals(tier) || "SILVER".equals(tier)) {
                total = total - total * 5 / 100;
            } else {
                total = total - total * 3 / 100;
            }
        }

        if ("WELCOME".equals(promoCode)) {
            if (subtotal >= 2000) {
                total = total - 500;
                if (total < 0) {
                    total = 0;
                }
            }
        }
        return total;
    }
}
