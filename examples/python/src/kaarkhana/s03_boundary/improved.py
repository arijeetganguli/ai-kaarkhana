"""S3 improved implementation.

The boundary is explicit (a named constant) and inclusive, and invalid ages are
rejected instead of being classified as "not senior".
"""

SENIOR_AGE = 65


def is_senior(age):
    if isinstance(age, bool) or not isinstance(age, int):
        raise ValueError(f"age must be a whole number, got {age!r}")
    if age < 0:
        raise ValueError(f"age must not be negative, got {age}")
    return age >= SENIOR_AGE
