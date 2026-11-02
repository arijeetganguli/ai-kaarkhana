import { describe, expect, it } from "vitest";
import * as improved from "../src/s05_boolean_logic/improved";
import * as initial from "../src/s05_boolean_logic/initial";

const OWNER = 1;
const OTHER = 2;

// Decision table: every combination of admin, owner and locked.
const table: Array<[boolean, boolean, boolean, boolean]> = [
  // admin, owner, locked, expected
  [false, false, false, false],
  [false, true, false, true],
  [true, false, false, true],
  [true, true, false, true],
  [false, false, true, false],
  [false, true, true, false],
  [true, false, true, false],
  [true, true, true, false],
];

describe("S5 improved", () => {
  it.each(table)("admin=%s owner=%s locked=%s -> %s", (isAdmin, isOwner, locked, expected) => {
    const user = { id: isOwner ? OWNER : OTHER, isAdmin };
    expect(improved.canEdit(user, { ownerId: OWNER, locked })).toBe(expected);
  });
});

describe("S5 documented defect of the initial implementation (characterisation)", () => {
  it("lets an admin edit a locked document", () => {
    expect(initial.canEdit({ id: OTHER, isAdmin: true }, { ownerId: OWNER, locked: true })).toBe(true);
  });
});
