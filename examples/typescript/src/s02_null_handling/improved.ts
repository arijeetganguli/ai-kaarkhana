/**
 * S2 improved implementation.
 *
 * Requirement used in this example (stated, not invented by the code): a greeting needs a
 * customer; a customer with a missing or blank name is greeted as "Hello, customer".
 * The default exists because the requirement says so. Without that sentence the correct
 * move is to ask, not to choose a default.
 */
export interface Customer {
  name?: string | null;
}

export function greeting(customer: Customer | null | undefined): string {
  if (customer == null) {
    throw new Error("customer is required");
  }
  const name = (customer.name ?? "").trim();
  return name === "" ? "Hello, customer" : `Hello, ${name}`;
}
