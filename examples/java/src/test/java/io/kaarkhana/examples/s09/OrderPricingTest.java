package io.kaarkhana.examples.s09;

import static org.junit.jupiter.api.Assertions.assertEquals;

import io.kaarkhana.examples.s09.OrderPricing.Item;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class OrderPricingTest {
    private static final List<String> TIERS = Arrays.asList("GOLD", "SILVER", "BASIC", null, "UNKNOWN");
    private static final List<String> PROMOS = Arrays.asList(null, "WELCOME", "OTHER");
    private static final List<List<Item>> CARTS = List.of(
            List.of(),
            List.of(new Item(100, 1)),
            List.of(new Item(1999, 1)),
            List.of(new Item(2000, 1)),
            List.of(new Item(500, 4)),
            List.of(new Item(100, 9)),
            List.of(new Item(100, 10)),
            List.of(new Item(333, 3), new Item(101, 7)),
            List.of(new Item(10_000, 12)),
            List.of(new Item(1, 1)));

    @Test
    void refactoringPreservesBehaviourOverTheWholeGrid() {
        int compared = 0;
        for (String tier : TIERS) {
            for (String promo : PROMOS) {
                for (List<Item> cart : CARTS) {
                    assertEquals(
                            OrderPricingInitial.price(cart, tier, promo),
                            OrderPricing.price(cart, tier, promo),
                            "tier=" + tier + " promo=" + promo + " cart=" + cart);
                    compared++;
                }
            }
        }
        assertEquals(150, compared);
    }

    // Characterisation tests: written first, run against the initial code, then kept.
    @ParameterizedTest
    @CsvSource({
        "1000,2,GOLD,,1800",
        "1000,2,SILVER,,1900",
        "1000,2,BASIC,,2000",
        "100,10,BASIC,,970",
        "100,10,GOLD,,855",
        "1000,2,BASIC,WELCOME,1500",
        "900,2,BASIC,WELCOME,1800",
        "1000,2,GOLD,WELCOME,1300",
    })
    void characterisationOfCurrentBehaviour(long price, int qty, String tier, String promo, long expected) {
        List<Item> cart = List.of(new Item(price, qty));
        assertEquals(expected, OrderPricingInitial.price(cart, tier, promo));
        assertEquals(expected, OrderPricing.price(cart, tier, promo));
    }

    @Test
    void emptyCartWithPromoNeverGoesNegative() {
        assertEquals(0, OrderPricing.price(List.of(), "GOLD", "WELCOME"));
    }

    @Test
    void quirkUnknownTierIsTreatedAsNoTier() {
        List<Item> cart = List.of(new Item(1000, 2));
        assertEquals(OrderPricing.price(cart, "BASIC", null), OrderPricing.price(cart, "PLATINUM", null));
    }
}
