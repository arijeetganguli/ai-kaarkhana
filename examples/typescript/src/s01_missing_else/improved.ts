/**
 * S1 improved implementation.
 *
 * Why not "just add an else": `else return 0` would turn a misspelt tier into "no
 * discount" and hide the data problem. Tiers are a closed union; parsing rejects
 * anything else at the boundary, and the exhaustive `switch` makes the compiler
 * flag every place that must change when a tier is added.
 */
export type Tier = "BASIC" | "SILVER" | "GOLD";

export class UnknownTierError extends Error {
  constructor(value: unknown) {
    super(`unknown loyalty tier: ${JSON.stringify(value)}`);
    this.name = "UnknownTierError";
  }
}

export function parseTier(value: unknown): Tier {
  if (value === "BASIC" || value === "SILVER" || value === "GOLD") {
    return value;
  }
  throw new UnknownTierError(value);
}

export function discountRate(tier: Tier): number {
  switch (tier) {
    case "BASIC":
      return 0;
    case "SILVER":
      return 0.05;
    case "GOLD":
      return 0.1;
    default: {
      const unreachable: never = tier;
      throw new UnknownTierError(unreachable);
    }
  }
}

export function priceAfterDiscount(priceCents: number, tier: unknown): number {
  return priceCents - Math.round(priceCents * discountRate(parseTier(tier)));
}
