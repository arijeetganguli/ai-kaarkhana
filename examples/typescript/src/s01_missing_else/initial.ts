/**
 * S1 initial implementation: discount rate by loyalty tier.
 *
 * PROBLEM: the if/else-if chain has no final branch. An unknown tier ("PLATINUM",
 * "gold", undefined) falls off the end and the function returns undefined. The
 * failure surfaces later as NaN in price arithmetic, which is never reported.
 * (The type system cannot help here because the input arrives as a plain string.)
 */
export function discountRate(tier: string): number | undefined {
  if (tier === "GOLD") {
    return 0.1;
  } else if (tier === "SILVER") {
    return 0.05;
  } else if (tier === "BASIC") {
    return 0;
  }
  return undefined;
}

export function priceAfterDiscount(priceCents: number, tier: string): number {
  return priceCents - Math.round(priceCents * (discountRate(tier) as number));
}
