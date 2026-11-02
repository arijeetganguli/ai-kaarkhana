/**
 * S7 code under test: late fee for a returned item.
 *
 * Requirement: the first 3 days late are a grace period (no fee); from day 4 the fee is 50
 * cents per day beyond the grace period; the fee never exceeds 2000 cents.
 */
export const GRACE_DAYS = 3;
export const RATE = 50;
export const CAP = 2_000;

export function lateFeeCents(daysLate: number): number {
  if (daysLate <= GRACE_DAYS) {
    return 0;
  }
  return Math.min((daysLate - GRACE_DAYS) * RATE, CAP);
}
