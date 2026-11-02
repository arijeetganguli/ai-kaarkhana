/**
 * S6 improved implementation, produced by the TDD cycles in examples/end_to_end.
 * Money is integer cents; the country is validated at the boundary.
 */
export const DOMESTIC_COUNTRY = "DE";
export const DOMESTIC_FEE_CENTS = 499;
export const FREE_SHIPPING_THRESHOLD_CENTS = 10_000;
export const INTERNATIONAL_FEE_CENTS = 1_499;

export function shippingFeeCents(totalCents: unknown, country: unknown): number {
  if (typeof totalCents !== "number" || !Number.isInteger(totalCents)) {
    throw new RangeError(`totalCents must be an integer, got ${JSON.stringify(totalCents)}`);
  }
  if (totalCents < 1) {
    throw new RangeError(`totalCents must be positive, got ${totalCents}`);
  }
  if (typeof country !== "string" || !/^[A-Z]{2}$/.test(country)) {
    throw new RangeError(`country must be a two letter upper case code, got ${JSON.stringify(country)}`);
  }
  if (country !== DOMESTIC_COUNTRY) {
    return INTERNATIONAL_FEE_CENTS;
  }
  return totalCents >= FREE_SHIPPING_THRESHOLD_CENTS ? 0 : DOMESTIC_FEE_CENTS;
}
