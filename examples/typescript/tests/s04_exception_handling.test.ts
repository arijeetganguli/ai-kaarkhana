import { describe, expect, it } from "vitest";
import * as improved from "../src/s04_exception_handling/improved";
import * as initial from "../src/s04_exception_handling/initial";

describe("S4 improved", () => {
  it.each([
    ["1", 1],
    [" 12 ", 12],
    ["007", 7],
  ])("parses %j as %i", (text, expected) => {
    expect(improved.parseQuantity(text)).toBe(expected);
  });

  it.each(["abc", "", "1.5", "12abc", "0", "-5"])("rejects %j", (text) => {
    expect(() => improved.parseQuantity(text)).toThrow(improved.InvalidQuantityError);
  });

  it("rejects non-text input with a clear message", () => {
    expect(() => improved.parseQuantity(null)).toThrow("quantity must be text");
  });

  it("names the offending input in the message", () => {
    expect(() => improved.parseQuantity("abc")).toThrow('not a whole number: "abc"');
  });
});

describe("S4 documented defects of the initial implementation (characterisation)", () => {
  it("invents zero for garbage and null", () => {
    expect(initial.parseQuantity("abc")).toBe(0);
    expect(initial.parseQuantity(null)).toBe(0);
  });

  it("accepts negative quantities and trailing garbage", () => {
    expect(initial.parseQuantity("-5")).toBe(-5);
    expect(initial.parseQuantity("12abc")).toBe(12);
  });
});
