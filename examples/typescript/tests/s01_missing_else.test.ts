import { describe, expect, it } from "vitest";
import * as improved from "../src/s01_missing_else/improved";
import * as initial from "../src/s01_missing_else/initial";

describe("S1 improved", () => {
  it.each([
    ["BASIC", 0],
    ["SILVER", 0.05],
    ["GOLD", 0.1],
  ] as const)("tier %s has rate %s", (tier, rate) => {
    expect(improved.discountRate(improved.parseTier(tier))).toBe(rate);
  });

  it.each(["PLATINUM", "gold", "", " GOLD", null, undefined, 7])("rejects %j", (bad) => {
    expect(() => improved.parseTier(bad)).toThrow(improved.UnknownTierError);
    expect(() => improved.parseTier(bad)).toThrow(/unknown loyalty tier/);
  });

  it("applies the tier rate to the price", () => {
    expect(improved.priceAfterDiscount(10_000, "GOLD")).toBe(9_000);
    expect(improved.priceAfterDiscount(10_000, "SILVER")).toBe(9_500);
    expect(improved.priceAfterDiscount(10_000, "BASIC")).toBe(10_000);
  });

  it("never lets an unknown tier reach price arithmetic", () => {
    expect(() => improved.priceAfterDiscount(10_000, "PLATINUM")).toThrow(improved.UnknownTierError);
  });
});

describe("S1 documented defects of the initial implementation (characterisation)", () => {
  it("returns undefined for an unknown tier", () => {
    expect(initial.discountRate("PLATINUM")).toBeUndefined();
  });

  it("produces NaN far from the cause instead of failing", () => {
    expect(initial.priceAfterDiscount(10_000, "PLATINUM")).toBeNaN();
  });
});
