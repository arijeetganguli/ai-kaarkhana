/**
 * S4 improved implementation. Requirement: a quantity is a whole number of at least 1.
 *
 * Invalid input raises a specific error that names the input. The whole string must be a
 * whole number (`Number` is strict where `parseInt` is not).
 */
export class InvalidQuantityError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "InvalidQuantityError";
  }
}

export function parseQuantity(text: unknown): number {
  if (typeof text !== "string") {
    throw new InvalidQuantityError(`quantity must be text, got ${typeof text}`);
  }
  const trimmed = text.trim();
  const value = Number(trimmed);
  if (trimmed === "" || !Number.isInteger(value)) {
    throw new InvalidQuantityError(`not a whole number: ${JSON.stringify(text)}`);
  }
  if (value < 1) {
    throw new InvalidQuantityError(`quantity must be at least 1, got ${value}`);
  }
  return value;
}
