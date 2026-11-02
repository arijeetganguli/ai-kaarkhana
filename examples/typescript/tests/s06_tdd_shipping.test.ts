import { describe, expect, it } from "vitest";
import { shippingFeeCents as fee } from "../src/s06_tdd_shipping/improved";
import * as initial from "../src/s06_tdd_shipping/initial";

describe("S6 improved (built test first)", () => {
  // SC-01 .. SC-03: domestic fee and the free shipping boundary
  it("charges the standard fee below the threshold", () => expect(fee(9_999, "DE")).toBe(499));
  it("ships free at exactly the threshold", () => expect(fee(10_000, "DE")).toBe(0));
  it("ships free above the threshold", () => expect(fee(10_001, "DE")).toBe(0));

  // SC-04 .. SC-05: international orders are never free
  it("charges international orders a flat fee", () => expect(fee(5_000, "FR")).toBe(1_499));
  it("never ships international orders free", () => expect(fee(1_000_000, "US")).toBe(1_499));

  // SC-06 .. SC-07: smallest valid order and invalid totals
  it("accepts the smallest valid total", () => expect(fee(1, "DE")).toBe(499));
  it.each([0, -1, -10_000])("rejects non-positive total %i", (bad) => {
    expect(() => fee(bad, "DE")).toThrow("positive");
  });
  it.each([100.5, "100", null, undefined])("rejects non-integer total %j", (bad) => {
    expect(() => fee(bad, "DE")).toThrow("integer");
  });

  // SC-08: invalid country codes
  it.each(["", "D", "DEU", "de", "D1", null, 49])("rejects country %j", (bad) => {
    expect(() => fee(5_000, bad)).toThrow("country");
  });
});

describe("S6 documented defects of the initial implementation (characterisation)", () => {
  it("charges shipping at exactly the threshold", () => {
    expect(initial.shippingFee(100, "DE")).toBe(4.99); // should be free
  });
  it("ignores the country", () => {
    expect(initial.shippingFee(5, "US")).toBe(4.99); // should be 14.99
  });
  it("accepts negative totals", () => {
    expect(initial.shippingFee(-50, "DE")).toBe(4.99);
  });
});
