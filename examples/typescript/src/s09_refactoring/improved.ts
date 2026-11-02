/**
 * S9 refactored implementation: same behaviour, one rule per function.
 *
 * Steps, each verified by the characterisation tests: extract subtotal and quantity; replace
 * nested ifs by `tierPercent` and `bulkPercent`; extract `percentOff`; extract `applyPromo`.
 * One quirk is deliberately preserved: an unknown tier is treated as "no tier" instead of
 * being rejected. That is a decision for the business owner, not a refactoring.
 */
import type { Item } from "./initial";

const TIER_PERCENT: ReadonlyMap<string, number> = new Map([
  ["GOLD", 10],
  ["SILVER", 5],
]);
const BULK_THRESHOLD = 10;
const PREMIUM_BULK_PERCENT = 5;
const STANDARD_BULK_PERCENT = 3;
const PROMO_CODE = "WELCOME";
const PROMO_MINIMUM_SUBTOTAL = 2000;
const PROMO_OFF = 500;

function tierPercent(tier: string | null): number {
  return (tier !== null && TIER_PERCENT.get(tier)) || 0;
}

function bulkPercent(tier: string | null, quantity: number): number {
  if (quantity < BULK_THRESHOLD) {
    return 0;
  }
  return tier !== null && TIER_PERCENT.has(tier) ? PREMIUM_BULK_PERCENT : STANDARD_BULK_PERCENT;
}

function percentOff(amount: number, percent: number): number {
  return amount - Math.floor((amount * percent) / 100);
}

function applyPromo(total: number, subtotal: number, promoCode: string | null): number {
  if (promoCode === PROMO_CODE && subtotal >= PROMO_MINIMUM_SUBTOTAL) {
    return Math.max(total - PROMO_OFF, 0);
  }
  return total;
}

export function priceOrder(items: Item[], tier: string | null, promoCode: string | null = null): number {
  const subtotal = items.reduce((sum, [price, qty]) => sum + price * qty, 0);
  const quantity = items.reduce((sum, [, qty]) => sum + qty, 0);
  let total = percentOff(subtotal, tierPercent(tier));
  total = percentOff(total, bulkPercent(tier, quantity));
  return applyPromo(total, subtotal, promoCode);
}
