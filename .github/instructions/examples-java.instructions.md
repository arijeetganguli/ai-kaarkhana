---
applyTo: "examples/java/**/*.java"
---

# Java examples

- Packages are `io.kaarkhana.examples.sNN` with matching test packages. Java 17, JUnit 5 and Mockito only; do not add dependencies.
- Keep the initial (defective) implementation and the improved one side by side; do not fix the initial one. Tests that document an initial defect are named `initialDefect...`.
- Tests assert exact values and exception types. No `assertThrows(Exception.class, ...)`.
- Run `cd examples/java && mvn test` after any change. Do not commit `target/`.
