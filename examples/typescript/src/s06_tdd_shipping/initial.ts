/**
 * S6 initial implementation: what a one-shot generated answer often looks like.
 *
 * Requirement (see examples/end_to_end/README.md): domestic (DE) orders ship for 4.99 EUR,
 * free from 100.00 EUR. International orders ship for a flat 14.99 EUR and are never free.
 * The order total must be positive and the country a two letter code.
 *
 * PROBLEMS: ignores the country; `>` instead of `>=` so exactly 100.00 pays shipping;
 * floating point money; no validation.
 */
export function shippingFee(total: number, _country: string): number {
  if (total > 100) {
    return 0;
  } else {
    return 4.99;
  }
}
