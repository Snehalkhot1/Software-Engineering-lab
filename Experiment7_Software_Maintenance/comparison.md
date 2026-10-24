
# Comparison of Software Maintenance and Evolution Techniques

## Aim
To compare different software maintenance and evolution
techniques using a Student Management System.

## Comparison Table

| Parameter | Corrective | Adaptive | Perfective | Preventive |
|---|---|---|---|---|
| Main purpose | Fix existing faults | Adapt to environmental changes | Improve features or performance | Reduce future maintenance problems |
| Main trigger | Reported defect | Changed platform, environment, or requirements | User needs or improvement opportunities | Technical debt or maintainability concerns |
| Example | Fix invalid marks handling | Add persistent file storage for the chosen environment | Improve student search | Refactor functions and add tests |
| Main benefit | Improves correctness | Maintains compatibility | Improves usefulness | Improves maintainability |
| Limitation | Often reactive | May require compatibility changes | Can increase scope | Benefits may not be immediately visible |
| Verification | Defect and regression tests | Environment and compatibility tests | Feature and performance tests | Regression tests and code review |

## Additional Evolution Techniques

### Refactoring
Improves the internal structure of code without intentionally
changing its external behavior.

### Regression Testing
Re-runs existing tests after changes to detect unintended
effects on previously working functionality.

### Version Control
Git records changes and helps developers compare versions,
review modifications, and restore earlier code when necessary.

## Observations
1. Corrective maintenance focuses on fixing faults.
2. Adaptive maintenance responds to environmental changes.
3. Perfective maintenance improves existing software.
4. Preventive maintenance reduces future maintenance effort.
5. Refactoring, testing, and version control support safe evolution.

## Result
The maintenance techniques were compared through a Student
Management System. Automated tests help verify that changes
do not break important existing features.
