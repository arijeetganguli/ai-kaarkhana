import { describe, expect, it } from "vitest";
import { lateFeeCents } from "../src/s07_weak_assertions/lateFee";
import { MUTANTS } from "../src/s07_weak_assertions/mutants";

type Fn = (daysLate: number) => number;

// The weak suite: executes every line, asserts almost nothing.
function weakSuite(fn: Fn): void {
  expect(fn(10)).toBeGreaterThan(0);
  expect(fn(0)).toBeGreaterThanOrEqual(0);
  expect(fn(1000)).toBeGreaterThan(0);
}

// The strong suite: exact values on both sides of every rule.
function strongSuite(fn: Fn): void {
  expect(fn(0)).toBe(0);
  expect(fn(3)).toBe(0); // last grace day
  expect(fn(4)).toBe(50); // first charged day
  expect(fn(10)).toBe(350); // 7 days * 50
  expect(fn(43)).toBe(2_000); // exactly reaches the cap
  expect(fn(44)).toBe(2_000); // would be 2050 without the cap
  expect(fn(1000)).toBe(2_000);
}

function survivors(suite: (fn: Fn) => void): string[] {
  return Object.entries(MUTANTS)
    .filter(([, mutant]) => {
      try {
        suite(mutant);
        return true; // nothing failed: the mutant survived
      } catch {
        return false; // the suite noticed: mutant killed
      }
    })
    .map(([name]) => name);
}

describe("S7 weak assertions", () => {
  it("both suites pass on the original code", () => {
    weakSuite(lateFeeCents);
    strongSuite(lateFeeCents);
  });

  it("the weak suite lets every mutant survive", () => {
    expect(survivors(weakSuite)).toEqual(Object.keys(MUTANTS));
  });

  it("the strong suite kills every mutant", () => {
    expect(survivors(strongSuite)).toEqual([]);
  });
});
