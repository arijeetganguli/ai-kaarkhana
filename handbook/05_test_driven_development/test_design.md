# Test design

> A test suite is a product with users: the next developer, the assistant, and you at 2 a.m. during an incident. Design it for them.

Part of [Chapter 5: Test Driven Development](README.md).

The snippets on this page are short and illustrative: they show the shape of a technique in each language. The runnable, verified versions live in [`examples/`](../../examples/README.md) and are linked where they exist.

## 1. Structure of a test

**Arrange, Act, Assert** (or Given, When, Then). One act per test. Blank lines between the three parts make failures easy to read.

```python
def test_expired_coupon_is_rejected():
    coupon = a_coupon(expires_on=date(2026, 1, 31))       # arrange
    result = apply_coupon(coupon, today=date(2026, 2, 1)) # act
    assert result.rejected_because == "EXPIRED"           # assert
```

Naming: describe the behaviour, not the method. `rejects_an_expired_coupon` beats `testApplyCoupon2`.

## 2. Fixtures and test data

Tests need data. Three approaches, from weakest to strongest:

| Approach | Problem or strength |
| --- | --- |
| Copy and paste literals into each test | Noise hides what matters; one schema change breaks fifty tests |
| Shared mutable fixture used by every test | Hidden coupling; tests pass or fail depending on order |
| **Fresh fixture per test plus a test data builder** | Each test states only what is relevant to it |

### Test data builder

A builder gives sensible, **valid** defaults and lets each test override only the fields that matter. (There is a prompt for designing one: [Test data builder design](../../prompts/testing/test-data-builder-design.md).)

**Python**

```python
from dataclasses import dataclass, replace
from datetime import date

@dataclass(frozen=True)
class Coupon:
    code: str = "SPRING10"
    percent_off: int = 10
    expires_on: date = date(2099, 12, 31)

def a_coupon(**overrides) -> Coupon:
    return replace(Coupon(), **overrides)

expired = a_coupon(expires_on=date(2020, 1, 1))
```

**Java**

```java
record Coupon(String code, int percentOff, LocalDate expiresOn) {
    static Coupon aCoupon() {
        return new Coupon("SPRING10", 10, LocalDate.of(2099, 12, 31));
    }
    Coupon withExpiresOn(LocalDate d) { return new Coupon(code, percentOff, d); }
}

Coupon expired = Coupon.aCoupon().withExpiresOn(LocalDate.of(2020, 1, 1));
```

**TypeScript**

```typescript
interface Coupon { code: string; percentOff: number; expiresOn: string }

const aCoupon = (overrides: Partial<Coupon> = {}): Coupon => ({
  code: "SPRING10",
  percentOff: 10,
  expiresOn: "2099-12-31",
  ...overrides,
});

const expired = aCoupon({ expiresOn: "2020-01-01" });
```

### Fixtures in the frameworks

| Need | pytest | JUnit 5 | Vitest / Jest |
| --- | --- | --- | --- |
| Fresh state per test | `@pytest.fixture` | `@BeforeEach` | `beforeEach` |
| Cleanup | `yield` in the fixture | `@AfterEach` | `afterEach` |
| Temporary files | `tmp_path` | `@TempDir` | `fs.mkdtempSync` in a hook |
| Shared, expensive and read-only | `scope="module"` | `@BeforeAll` | `beforeAll` |

An in-memory database fixture with a clean schema per test is used in [`test_s08_integration.py`](../../examples/python/tests/test_s08_integration.py).

### Rules for test data

- **Valid by default.** Builders produce data that satisfies domain rules; invalid data is an explicit override.
- **No production data.** Copying real customer records into fixtures is a privacy and security failure. See [Chapter 9](../09_security_engineering/README.md).
- **Control time and randomness.** Inject a clock or seed; never read `now()` inside the code under test without a seam.
- **Make intent visible.** `a_coupon(expires_on=yesterday)` explains the test; a literal date does not.

## 3. Parameterised tests

When the same behaviour is checked against many inputs, a parameterised test replaces copy and paste and makes the **table of cases** visible. This fits the scenario matrix naturally.

**Python**

```python
import pytest

@pytest.mark.parametrize(
    ("days_late", "expected_cents"),
    [(0, 0), (3, 0), (4, 50), (43, 2_000), (44, 2_000)],
)
def test_late_fee(days_late, expected_cents):
    assert late_fee_cents(days_late) == expected_cents
```

**Java**

```java
@ParameterizedTest(name = "{0} days late costs {1} cents")
@CsvSource({"0,0", "3,0", "4,50", "43,2000", "44,2000"})
void lateFee(long daysLate, long expectedCents) {
    assertEquals(expectedCents, LateFee.feeCents(daysLate));
}
```

**TypeScript**

```typescript
it.each([
  [0, 0], [3, 0], [4, 50], [43, 2_000], [44, 2_000],
])("%i days late costs %i cents", (daysLate, expected) => {
  expect(lateFeeCents(daysLate)).toBe(expected);
});
```

Keep case names meaningful. A failing row should tell you *which scenario* broke.

## 4. Boundary tests

Most defects live at the edges of ranges. For each boundary `B`, test the value *below*, *at* and *above* it. See [Boundary testing](../../prompts/testing/boundary-testing.md) and [scenario S3](../../examples/scenarios.md#s3-incorrect-boundary-condition).

| Rule | Values to test |
| --- | --- |
| Free shipping at 100.00 or more | 99.99, 100.00, 100.01 |
| Grace period of 3 days | 0, 3, 4 |
| Cap of 2000 cents | the input that *just* reaches the cap, one below, one above |
| Length between 3 and 20 | 2, 3, 4, 19, 20, 21 |
| A collection | empty, one element, many |

Boundaries also include **types and encodings**: integer overflow, negative numbers, zero, empty string, whitespace only, very long input, Unicode, time zone and daylight saving transitions, and the leap day.

## 5. Negative tests

A negative test asserts that bad input or a failing dependency produces the **specified** failure, and that nothing else happens. See [Negative testing](../../prompts/testing/negative-testing.md) and [scenario S4](../../examples/scenarios.md#s4-inadequate-exception-handling).

Assert three things:

1. The **type or code** of the failure.
2. The **message or detail**, without leaking secrets.
3. The **absence of side effects**: nothing saved, nothing sent, state unchanged.

**Python**

```python
def test_negative_quantity_is_rejected_and_nothing_is_saved(repo):
    with pytest.raises(ValueError, match="quantity must be positive"):
        place_order(repo, sku="A1", quantity=-1)
    assert repo.count() == 0
```

**Java**

```java
@Test
void negativeQuantityIsRejectedAndNothingIsSaved() {
    var ex = assertThrows(IllegalArgumentException.class,
            () -> service.placeOrder("A1", -1));
    assertTrue(ex.getMessage().contains("quantity must be positive"));
    assertEquals(0, repo.count());
}
```

**TypeScript**

```typescript
it("rejects a negative quantity and saves nothing", async () => {
  await expect(placeOrder(repo, "A1", -1)).rejects.toThrow("quantity must be positive");
  expect(repo.count()).toBe(0);
});
```

Do not write `assertThrows(Exception.class, ...)` or `pytest.raises(Exception)`: they pass when *anything* goes wrong, including a typo.

## 6. Mocking and stubbing

Test doubles replace collaborators so tests are fast and deterministic.

| Double | Purpose | Example |
| --- | --- | --- |
| **Stub** | Returns canned answers | A rate service that always returns 1.1 |
| **Fake** | A simple working implementation | An in-memory repository |
| **Mock** | Records calls so the test can verify them | An email sender; assert one message sent |
| **Spy** | Wraps the real object and records calls | Rarely needed |

### Guidance

- **Prefer fakes and stubs over mocks** for anything that has state. Verify *outcomes* more than *interactions*.
- **Mock at the boundary you own** (an interface your code defines), not third-party types.
- **Do not mock the thing you are testing**, nor simple value objects.
- **Verify an interaction when the interaction is the behaviour** (an email is sent exactly once), not for every internal call.
- **A mock can only tell you the code calls what you told it to expect.** It cannot tell you the real dependency agrees. That is why integration tests exist.

**Python** (`unittest.mock`)

```python
from unittest.mock import Mock

def test_receipt_is_emailed_once_after_payment():
    mailer = Mock()
    gateway = Mock()
    gateway.charge.return_value = "OK"

    checkout(gateway, mailer, amount_cents=1_000, email="a@example.com")

    mailer.send_receipt.assert_called_once_with("a@example.com", 1_000)
```

**Java** (Mockito)

```java
@Test
void receiptIsEmailedOnceAfterPayment() {
    var gateway = mock(PaymentGateway.class);
    var mailer = mock(Mailer.class);
    when(gateway.charge(1_000)).thenReturn("OK");

    new Checkout(gateway, mailer).pay(1_000, "a@example.com");

    verify(mailer, times(1)).sendReceipt("a@example.com", 1_000);
}
```

**TypeScript** (Vitest)

```typescript
it("emails the receipt once after payment", async () => {
  const gateway = { charge: vi.fn().mockResolvedValue("OK") };
  const mailer = { sendReceipt: vi.fn() };

  await checkout(gateway, mailer, 1_000, "a@example.com");

  expect(mailer.sendReceipt).toHaveBeenCalledTimes(1);
  expect(mailer.sendReceipt).toHaveBeenCalledWith("a@example.com", 1_000);
});
```

Runnable negative tests with specific error types and messages are in scenario S4 ([Python](../../examples/python/tests/test_s04_exception_handling.py), [TypeScript](../../examples/typescript/tests/s04_exception_handling.test.ts)). Runnable tests that contrast a mocked collaborator with a real one are in scenario S8 ([Python](../../examples/python/tests/test_s08_integration.py), [TypeScript](../../examples/typescript/tests/s08_integration.test.ts)).

### The over-mocking trap

[Scenario S8](../../examples/scenarios.md#s8-missing-integration-tests-and-inadequate-unit-tests) contains a mocked repository test that passes while the real SQL maps columns in the wrong order. A suite made only of such tests is green and worthless at the boundary.

## 7. Regression tests

A **regression test** captures a defect once so it cannot return silently. The process:

1. Reproduce the bug as a failing test, at the lowest level that shows it.
2. Fix.
3. Keep the test, named after the behaviour, with a link to the defect ID.
4. Look for *siblings*: the same mistake elsewhere ([Regression Analyst](../../skills/regression-analyst/SKILL.md), [Regression test generation](../../prompts/testing/regression-test-generation.md)).

## 8. Integration tests

Integration tests exercise your code with a **real** boundary. They are slower, so choose carefully what to cover.

| Boundary | What to test | Typical approach |
| --- | --- | --- |
| Database | Queries, mappings, constraints, transactions, rollback, migrations | Real database in a container, or an embedded one where it behaves the same; fresh schema per test |
| HTTP client | Status handling (2xx, 4xx, 5xx), timeouts, malformed bodies, retries | A local stub server |
| HTTP server | Routing, validation, serialisation, auth, error format | The framework's test client |
| Messaging | Serialisation, retries, idempotent consumption, dead letters | Test containers or in-memory broker |
| File system | Missing files, permissions, partial writes | Temporary directory |

Rules:

- **Each test owns its data** and cleans up.
- **No sleeping.** Wait on a condition with a timeout, not a fixed delay.
- **Test the failure paths**: the dependency is down, slow or lying.
- **Keep them deterministic.** Order independence, no shared global state.
- **State the fidelity limit.** An in-memory SQLite is not PostgreSQL. If behaviour differs (SQL dialect, locking, isolation), use the real engine.

The three languages are demonstrated in [scenario S8](../../examples/scenarios.md#s8-missing-integration-tests-and-inadequate-unit-tests) (an in-memory database in Python, a local HTTP server in Java and TypeScript), and the [Missing integration test lab](../../examples/broken_code_lab/08_missing_integration_test/CHALLENGE.md) lets you practise it. Use [Integration test generation](../../prompts/testing/integration-test-generation.md) and the [Integration Test Engineer](../../skills/integration-test-engineer/SKILL.md).

## 9. Contract tests

When two services communicate, tests of each in isolation can both be green while the combination fails. A **contract test** pins the shape and semantics both sides rely on (fields, types, status codes, error format, optionality). See [Contract testing](../../prompts/testing/contract-testing.md) and the [API Contract Reviewer](../../skills/api-contract-reviewer/SKILL.md).

## 10. Flaky tests

A flaky test is a test that sometimes fails without a code change. It is a defect in the suite and erodes trust in every red. Typical causes: time, randomness, shared state, ordering, real network, concurrency, resource limits. Quarantine visibly, then fix. Do not simply retry. Use [Flaky test diagnosis](../../prompts/testing/flaky-test-diagnosis.md).

## 11. Test design checklist

- [ ] Each test has one reason to fail and a behaviour name.
- [ ] Expected values are literals traceable to a requirement.
- [ ] Boundaries have below, at and above cases.
- [ ] Failure paths assert the specific failure and no side effects.
- [ ] Doubles are used at boundaries I own; at least one integration test exists per real boundary.
- [ ] Data comes from builders and is valid by default; no production data.
- [ ] No dependency on order, clock, randomness or network without control.
- [ ] I have broken the code on purpose and a test failed.

## Practice

- Replace a copy and paste test class in your own project with a builder and a parameterised test.
- Find a test that uses `Exception.class` or `pytest.raises(Exception)` and make it specific.
- Pick one mocked repository test. Write the integration test that would catch a wrong query.

## Related

**Skills:** [Unit Test Engineer](../../skills/unit-test-engineer/SKILL.md), [Integration Test Engineer](../../skills/integration-test-engineer/SKILL.md), [Edge Case Hunter](../../skills/edge-case-hunter/SKILL.md), [Regression Analyst](../../skills/regression-analyst/SKILL.md)

**Prompts:** [Unit test generation](../../prompts/testing/unit-test-generation.md), [Boundary testing](../../prompts/testing/boundary-testing.md), [Negative testing](../../prompts/testing/negative-testing.md), [Integration test generation](../../prompts/testing/integration-test-generation.md), [Test data builder design](../../prompts/testing/test-data-builder-design.md)

**Workflows:** [Write unit and integration tests](../../workflows/07_unit_and_integration_testing.md)

**Further reading** (external): [Mockito documentation](https://site.mockito.org), [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [Vitest mocking](https://vitest.dev/guide/mocking).

Previous: [TDD with AI](tdd_with_ai.md) · Next: [Property based and mutation testing](property_based_and_mutation_testing.md)
