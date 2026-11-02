/** S3 improved implementation: named inclusive boundary, invalid ages rejected. */
export const SENIOR_AGE = 65;

export function isSenior(age: unknown): boolean {
  if (typeof age !== "number" || !Number.isInteger(age)) {
    throw new RangeError(`age must be a whole number, got ${JSON.stringify(age)}`);
  }
  if (age < 0) {
    throw new RangeError(`age must not be negative, got ${age}`);
  }
  return age >= SENIOR_AGE;
}
