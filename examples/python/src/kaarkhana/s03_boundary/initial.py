"""S3 initial implementation: senior discount eligibility.

Requirement: customers aged 65 or older are eligible.

PROBLEM
    `>` excludes exactly 65. Tests with "typical" ages (30, 70) pass, so the
    off-by-one survives until a 65 year old customer complains.
"""


def is_senior(age):
    return age > 65
