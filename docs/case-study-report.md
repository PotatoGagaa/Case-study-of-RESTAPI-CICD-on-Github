# Case Study Report: REST API CI/CD on GitHub

## 1. Executive Summary
This case study demonstrates how to validate a Python REST API automatically with GitHub Actions,
use GitHub Secrets without exposing their values, and test failure handling in a controlled workflow.

## 2. Objectives
- Build a small REST API using FastAPI.
- Create repeatable automated API tests with Pytest.
- Run tests automatically on GitHub push and pull-request events.
- Demonstrate secure injection and missing-secret handling.
- Record evidence for both successful and failed workflow runs.

## 3. Scope
**Included:** API endpoints, request validation, authentication checks, automated tests, GitHub Actions CI,
a manual Secret demonstration, and least-privilege workflow permissions.

**Not included in the baseline:** production deployment, database persistence, real user identity management,
or production credentials.

## 4. Architecture
Developer workstation → GitHub repository → GitHub Actions runner → dependency installation → Pytest.
A separate manually triggered workflow validates whether `DEMO_API_TOKEN` is available without printing it.

## 5. Technology Stack
- Python 3.12
- FastAPI
- Pytest and FastAPI TestClient
- GitHub repository and GitHub Actions
- GitHub Actions repository Secret for the isolated demonstration

## 6. Implementation
Describe the API endpoints, test coverage, workflow triggers, permissions, and Secret configuration.
Include a repository URL and commit identifier.

## 7. Test Plan and Evidence

| ID | Scenario | Expected result | Actual result / evidence |
|---|---|---|---|
| T01 | Health endpoint | HTTP 200 | Fill in after execution |
| T02 | Protected endpoint without token | HTTP 401 | Fill in after execution |
| T03 | Create and retrieve task | HTTP 201 then HTTP 200 | Fill in after execution |
| T04 | Empty title | HTTP 422 | Fill in after execution |
| T05 | Missing task | HTTP 404 | Fill in after execution |
| T06 | All tests run in GitHub Actions | Workflow passes | Add run URL / screenshot |
| T07 | Deliberately broken assertion | Workflow fails | Add run URL / screenshot |
| S01 | Demo Secret configured | Workflow passes without printing value | Add run URL / screenshot |
| S02 | Demo Secret missing | Workflow fails with a safe message | Add run URL / screenshot |

Do not claim a test passed until you have run it and captured the evidence.

## 8. Security Analysis
Discuss least-privilege permissions, secret storage, environment separation, log hygiene, untrusted pull-request
risks, dependency pinning, and branch protection. Explain that GitHub log masking is not a complete security boundary.

## 9. Results
Summarize actual pass/fail counts, relevant workflow runs, observed failures, and remediation.

## 10. Limitations
The API uses in-memory storage and a demo-only hard-coded test token. The baseline provides CI and a Secret
demonstration, not continuous deployment. These choices are intentional to keep the learning scope small.

## 11. Recommendations
For a production-ready pipeline, add stronger authentication, persistent storage, dependency/security scanning,
protected branches, environment approvals, immutable action references, and controlled deployment.

## 12. Conclusion
State what the experiment demonstrated, what evidence supports the conclusion, and which improvements remain.
