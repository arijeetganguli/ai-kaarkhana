package io.kaarkhana.examples.s09;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * S9 refactored implementation: same behaviour, one rule per method.
 *
 * <p>Steps, each verified by the characterisation tests: extract subtotal and quantity; replace
 * nested ifs by {@code tierPercent} and {@code bulkPercent}; extract {@code percentOff}; extract
 * {@code applyPromo}. One quirk is deliberately preserved: an unknown tier is treated as "no
 * tier" instead of being rejected. That is a decision for the business owner, not a refactoring.
 */
public final class OrderPricing {
    public record Item(long unitPriceCents, int quantity) {}

    // HashMap, not Map.of: Map.of(...).getOrDefault(null, ...) throws NullPointerException,
    // and the initial implementation accepts a null tier (treated as "no tier").
    private static final Map<String, Integer> TIER_PERCENT = tiers();
    private static final int BULK_THRESHOLD = 10;
    private static final int PREMIUM_BULK_PERCENT = 5;
    private static final int STANDARD_BULK_PERCENT = 3;
    private static final String PROMO_CODE = "WELCOME";
    private static final long PROMO_MINIMUM_SUBTOTAL = 2000;
    private static final long PROMO_OFF = 500;

    private static Map<String, Integer> tiers() {
        Map<String, Integer> map = new HashMap<>();
        map.put("GOLD", 10);
        map.put("SILVER", 5);
        return Collections.unmodifiableMap(map);
    }

    private OrderPricing() {}

    public static long price(List<Item> items, String tier, String promoCode) {
        long subtotal = items.stream().mapToLong(i -> i.unitPriceCents() * i.quantity()).sum();
        long quantity = items.stream().mapToLong(Item::quantity).sum();
        long total = percentOff(subtotal, tierPercent(tier));
        total = percentOff(total, bulkPercent(tier, quantity));
        return applyPromo(total, subtotal, promoCode);
    }

    private static int tierPercent(String tier) {
        return TIER_PERCENT.getOrDefault(tier, 0);
    }

    private static int bulkPercent(String tier, long quantity) {
        if (quantity < BULK_THRESHOLD) {
            return 0;
        }
        return TIER_PERCENT.containsKey(tier) ? PREMIUM_BULK_PERCENT : STANDARD_BULK_PERCENT;
    }

    private static long percentOff(long amount, int percent) {
        return amount - amount * percent / 100;
    }

    private static long applyPromo(long total, long subtotal, String promoCode) {
        if (PROMO_CODE.equals(promoCode) && subtotal >= PROMO_MINIMUM_SUBTOTAL) {
            return Math.max(total - PROMO_OFF, 0);
        }
        return total;
    }
}
