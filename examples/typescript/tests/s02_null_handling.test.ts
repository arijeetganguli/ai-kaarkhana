import { describe, expect, it } from "vitest";
import * as improved from "../src/s02_null_handling/improved";
import * as initial from "../src/s02_null_handling/initial";

describe("S2 improved", () => {
  it("greets by trimmed name", () => {
    expect(improved.greeting({ name: "  Asha " })).toBe("Hello, Asha");
  });

  it.each([null, undefined, "", "   "])("uses the specified default for name %j", (name) => {
    expect(improved.greeting({ name })).toBe("Hello, customer");
  });

  it.each([null, undefined])("rejects a missing customer (%j) explicitly", (customer) => {
    expect(() => improved.greeting(customer)).toThrow("customer is required");
  });
});

describe("S2 documented defects of the initial implementation (characterisation)", () => {
  it("throws a TypeError for a missing customer", () => {
    expect(() => initial.greeting(undefined)).toThrow(TypeError);
  });

  it("throws a TypeError for a missing name", () => {
    expect(() => initial.greeting({ name: null })).toThrow(TypeError);
  });
});
