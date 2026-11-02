/**
 * S4 initial implementation: parse an order quantity from user input.
 *
 * PROBLEM: `catch { return 0 }` swallows every failure and invents a value. "abc" and
 * null become 0, the cause is lost, and "-5" is accepted because nothing checks the
 * range. `parseInt("12abc")` also silently returns 12.
 */
export function parseQuantity(text: string | null): number {
  try {
    const value = parseInt(text as string, 10);
    return Number.isNaN(value) ? 0 : value;
  } catch {
    return 0;
  }
}
