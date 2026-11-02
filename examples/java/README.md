# Java examples (JUnit 5 and Mockito)

Nine scenarios from the [scenario catalogue](../scenarios.md). Each has an `...Initial` class (defective) and the improved class, plus a JUnit 5 test. Mockito is used in S2 (mocked repository) and S8 (mocked HTTP client, to show why mocks are not enough).

## Requirements

- JDK 17 or newer
- Maven 3.9 or newer (dependencies: JUnit Jupiter 5.11.4, Mockito 5.14.2, resolved from Maven Central)

## Run

```bash
cd examples/java
mvn test
```

Expected: `BUILD SUCCESS`, all tests green (88 at the time of writing). S8 includes a local HTTP server on an ephemeral loopback port and takes about a second.

Run one scenario: `mvn test -Dtest=ShippingFeeTest`.

## Layout

| Path | Purpose |
| --- | --- |
| `src/main/java/io/kaarkhana/examples/sNN/` | `...Initial` (defective, Javadoc names the problem) and the improved class. |
| `src/test/java/io/kaarkhana/examples/sNN/` | Tests of the improved code plus `initialDefect...` characterisation tests. |

| Scenario | Package | Main classes |
| --- | --- | --- |
| S1 missing else | `s01` | `TierDiscountInitial`, `Tier` |
| S2 null handling | `s02` | `CustomerGreetingInitial`, `CustomerGreeting` |
| S3 boundary | `s03` | `SeniorDiscountInitial`, `SeniorDiscount` |
| S4 exception handling | `s04` | `QuantityParserInitial`, `QuantityParser` |
| S5 boolean logic | `s05` | `DocumentAccessInitial`, `DocumentAccess` |
| S6 TDD shipping fee | `s06` | `ShippingFeeInitial`, `ShippingFee` |
| S7 weak assertions and mutants | `s07` | `LateFee` (with `MUTANTS`), `LateFeeMutationTest` |
| S8 integration (HTTP) | `s08` | `PriceClientInitial`, `PriceClient` |
| S9 refactoring | `s09` | `OrderPricingInitial`, `OrderPricing` |

## Try mutation testing for real

[PIT](https://pitest.org) integrates with Maven through the `pitest-maven` plugin and the `pitest-junit5-plugin`. Add them to the `pom.xml` following the PIT documentation for the versions you choose (not pinned here to avoid shipping unverified versions), then run `mvn test-compile org.pitest:pitest-maven:mutationCoverage`.

Back to [examples](../README.md).
