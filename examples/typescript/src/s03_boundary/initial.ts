/**
 * S3 initial implementation: senior discount eligibility. Requirement: aged 65 or older.
 *
 * PROBLEM: `>` excludes exactly 65. Tests with typical ages (30, 70) pass, so the
 * off-by-one survives until a 65 year old customer complains.
 */
export function isSenior(age: number): boolean {
  return age > 65;
}
