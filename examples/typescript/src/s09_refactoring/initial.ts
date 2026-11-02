/**
 * S9 initial implementation: order pricing with nested conditionals.
 *
 * Behaviour (as implemented; confirmed by characterisation tests): tier discount GOLD 10
 * percent, SILVER 5 percent, anything else 0; bulk discount at 10 or more units (5 percent
 * for GOLD and SILVER, 3 percent otherwise) applied after the tier discount; promo WELCOME
 * takes 500 cents off when the undiscounted subtotal is at least 2000, never below zero.
 *
 * PROBLEM: four levels of nesting mix three rules. Adding a rule means re-reading all of it.
 */
export type Item = [unitPriceCents: number, quantity: number];

export function priceOrder(items: Item[], tier: string | null, promoCode: string | null = null): number {
  let subtotal = 0;
  let quantity = 0;
  for (const [price, qty] of items) {
    subtotal += price * qty;
    quantity += qty;
  }

  let total = subtotal;
  if (tier === "GOLD") {
    total = total - Math.floor((total * 10) / 100);
  } else {
    if (tier === "SILVER") {
      total = total - Math.floor((total * 5) / 100);
    }
  }

  if (quantity >= 10) {
    if (tier === "GOLD" || tier === "SILVER") {
      total = total - Math.floor((total * 5) / 100);
    } else {
      total = total - Math.floor((total * 3) / 100);
    }
  }

  if (promoCode === "WELCOME") {
    if (subtotal >= 2000) {
      total = total - 500;
      if (total < 0) {
        total = 0;
      }
    }
  }
  return total;
}
