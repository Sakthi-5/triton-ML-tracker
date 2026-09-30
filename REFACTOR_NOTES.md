\# Refactoring Notes



\## Day 8 — Clean Code \& SOLID



\### Single Responsibility Principle (SRP)



Refactored the Pipeline so that step execution and step-specific

processing are separated from the main pipeline orchestration.



\- `Pipeline` manages pipeline flow.

\- `\_run\_step()` manages execution and error handling for an individual step.

\- Individual `Step` classes contain their own processing logic.



\### Open/Closed Principle (OCP)



The Pipeline is open for extension but closed for modification.



A new preprocessing step can be added by creating a new `Step`

implementation without modifying the existing `Pipeline`.



Example:

\- Added `RemoveDigitsStep`

\- Existing `Pipeline` code was not changed.



\### Dependency Inversion



`Pipeline` works with the `Step` abstraction instead of depending

on specific preprocessing implementations.



```text

Pipeline → Step abstraction

&nbsp;             ↑

&nbsp;      Concrete Steps

