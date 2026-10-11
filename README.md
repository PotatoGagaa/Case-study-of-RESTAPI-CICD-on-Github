# REST API CI/CD Security Case Study

A learning project demonstrating a Python FastAPI REST API, Pytest API tests,
GitHub Actions CI, and safe use of GitHub Actions Secrets.

## Features

- `GET /health`: health check
- `GET /tasks`: list tasks (requires `X-API-Token`)
- `POST /tasks`: create a task (requires `X-API-Token`)
- `GET /tasks/{task_id}`: retrieve a task (requires `X-API-Token`)
- `DELETE /tasks/{task_id}`: delete a task (requires `X-API-Token`)
- `.github/workflows/ci.yml`: automated tests on push and pull requests
- `.github/workflows/secret-demo.yml`: manual Secret injection demonstration

> This is a learning example. It uses in-memory storage and a hard-coded,
> non-production test token. Do not use this authentication implementation
> or token in production.

## Run locally

Python 3.12 is recommended.

```bash
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install and test:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -v
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to try the API.

For protected endpoints, add header `X-API-Token: demo-test-token`.

## Configure GitHub Actions

1. Create a GitHub repository, for example `rest-api-cicd-case-study`.
2. Push this project's files to the repository.
3. Open the **Actions** tab and inspect the `REST API CI` workflow.
4. Push a code change and confirm the workflow runs automatically.

## Demonstrate GitHub Secrets

1. In the repository, open **Settings → Secrets and variables → Actions**.
2. Choose **New repository secret**.
3. Name it `DEMO_API_TOKEN`; use a throwaway, non-production demo value.
4. Open **Actions → GitHub Secret Demo → Run workflow**.
5. Confirm the workflow reports that the secret is present without displaying its value.
6. For a negative test, temporarily remove or rename the demo secret and rerun the workflow. It should fail with a missing-secret message. Restore the secret afterwards if you still need the demo.

Never print secrets, commit them to source control, or use production credentials in this exercise. GitHub log masking is a defense-in-depth feature, not a guarantee against every form of accidental disclosure.

## Suggested case-study experiments

- Baseline: all tests pass.
- Regression: intentionally change an expected status code in a test and observe CI fail.
- Recovery: revert the test change and observe CI pass.
- Secret present: manual Secret workflow passes without revealing the value.
- Secret missing: manual Secret workflow fails safely.
- Security review: inspect workflow permissions and verify no real credential is in Git history.

## Limitations and next steps

- Task storage is in memory and resets when the process restarts.
- The API token is a demo constant used only to illustrate endpoint authorization.
- CI is implemented; a deployment stage is not included in this baseline.
- For a production-like extension, use environment-specific credentials, branch protection,
  dependency/security scanning, a real secret manager or OIDC where applicable, and a
  controlled test-environment deployment.
