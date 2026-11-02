import { describe, expect, it } from "vitest";
import * as improved from "../src/s09_refactoring/improved";
import * as initial from "../src/s09_refactoring/initial";
import type { Item } from "../src/s09_refactoring/initial";

const TIERS = ["GOLD", "SILVER", "BASIC", null, "UNKNOWN"];
const PROMOS = [null, "WELCOME", "OTHER"];
const CARTS: Item[][] = [
  [],
  [[100, 1]],
  [[1999, 1]],
  [[2000, 1]],
  [[500, 4]],
  [[100, 9]],
  [[100, 10]],
  [
    [333, 3],
    [101, 7],
  ],
  [[10_000, 12]],
  [[1, 1]],
];

describe("S9 refactoring", () => {
  it("preserves behaviour over the whole grid", () => {
    let compared = 0;
    for (const tier of TIERS) {
      for (const promo of PROMOS) {
        for (const cart of CARTS) {
          expect(improved.priceOrder(cart, tier, promo), `tier=${tier} promo=${promo}`).toBe(
            initial.priceOrder(cart, tier, promo),
          );
          compared++;
        }
      }
    }
    expect(compared).toBe(150);
  });

  // Characterisation tests: written first, run against the initial code, then kept.
  it.each([
    [[[1000, 2]], "GOLD", null, 1800],
    [[[1000, 2]], "SILVER", null, 1900],
    [[[1000, 2]], "BASIC", null, 2000],
    [[[100, 10]], "BASIC", null, 970],
    [[[100, 10]], "GOLD", null, 855],
    [[[1000, 2]], "BASIC", "WELCOME", 1500],
    [[[900, 2]], "BASIC", "WELCOME", 1800],
    [[[1000, 2]], "GOLD", "WELCOME", 1300],
    [[], "GOLD", "WELCOME", 0],
  ] as Array<[Item[], string, string | null, number]>)("characterisation %j %s %s -> %i", (cart, tier, promo, expected) => {
    expect(initial.priceOrder(cart, tier, promo)).toBe(expected);
    expect(improved.priceOrder(cart, tier, promo)).toBe(expected);
  });

  it("quirk: an unknown tier is treated as no tier", () => {
    const cart: Item[] = [[1000, 2]];
    expect(improved.priceOrder(cart, "PLATINUM")).toBe(improved.priceOrder(cart, "BASIC"));
  });
});
