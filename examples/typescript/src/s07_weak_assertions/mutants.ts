import { CAP, GRACE_DAYS, RATE } from "./lateFee";

/**
 * Hand-written mutants of `lateFeeCents`: the original with exactly one small change, the
 * kind a mutation testing tool (Stryker) generates automatically.
 *
 * Not included on purpose: `daysLate <= 3` -> `daysLate < 3` changes the result only for 3
 * days, where both branches return 0. It is an equivalent mutant: no test can kill it.
 */
export const MUTANTS: Record<string, (daysLate: number) => number> = {
  m1_grace_boundary_shifted: (d) => (d <= GRACE_DAYS + 1 ? 0 : Math.min((d - GRACE_DAYS) * RATE, CAP)),
  m2_off_by_one_day: (d) => (d <= GRACE_DAYS ? 0 : Math.min((d - GRACE_DAYS + 1) * RATE, CAP)),
  m3_rate_changed: (d) => (d <= GRACE_DAYS ? 0 : Math.min((d - GRACE_DAYS) * (RATE + 1), CAP)),
  m4_cap_changed: (d) => (d <= GRACE_DAYS ? 0 : Math.min((d - GRACE_DAYS) * RATE, CAP + 1)),
  m5_cap_removed: (d) => (d <= GRACE_DAYS ? 0 : (d - GRACE_DAYS) * RATE),
};
