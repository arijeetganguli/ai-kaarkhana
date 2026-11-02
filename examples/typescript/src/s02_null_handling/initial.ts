/**
 * S2 initial implementation: greeting for a customer.
 *
 * PROBLEM: `customer` may be undefined (lookup miss) and `name` may be null
 * (incomplete profile). Both throw a TypeError with no hint of which rule was
 * violated. Non-null assertions (`!`) silence the compiler, not the problem.
 */
export interface LegacyCustomer {
  name: string | null;
}

export function greeting(customer: LegacyCustomer | undefined): string {
  return "Hello, " + customer!.name!.trim();
}
