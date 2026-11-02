import { describe, expect, it } from "vitest";
import * as improved from "../src/s03_boundary/improved";
import * as initial from "../src/s03_boundary/initial";

describe("S3 improved", () => {
  it.each([
    [0, false],
    [64, false],
    [65, true],
    [66, true],
    [100, true],
  ])("age %i -> %s", (age, expected) => {
    expect(improved.isSenior(age)).toBe(expected);
  });

  it.each([-1, 65.5, Number.NaN, "65", null, undefined])("rejects %j", (bad) => {
    expect(() => improved.isSenior(bad)).toThrow(RangeError);
  });
});

describe("S3 documented defect of the initial implementation (characterisation)", () => {
  it("excludes exactly 65", () => {
    expect(initial.isSenior(65)).toBe(false); // requirement says 65 is eligible
    expect(initial.isSenior(66)).toBe(true);
  });
});
