# Devin Demo Service

### A scaffold microservice for demonstrating the **Devin Issues CLI**

This repository is a lightweight **demo project** used to showcase how the
**[Devin Issues CLI](https://github.com/your-username/devin-cli)** connects with GitHub Issues and Devin to:

* Automatically **scope issues** with detailed plans and confidence levels
* Generate **branches, commits, and PRs** via Devin’s GitHub App integration
* Provide end-to-end visibility from “bug filed” → “PR opened”

---

## Project Overview

The service simulates a basic **FastAPI-like** backend with three key components:

| File                    | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `app/main.py`           | Minimal healthcheck route (`/health`) that occasionally fails (used for testing bug fixes). |
| `app/metrics.py`        | Placeholder Prometheus metrics endpoint stub.                                               |
| `app/logging_config.py` | Simple JSON logger setup used to demonstrate enhancements like `request_id` propagation.    |

Together, these files provide realistic but simple "issues" for Devin to analyze — just enough for meaningful scoping and PR creation.

---

## How It’s Used in the CLI Demo

This repo is the `DEFAULT_REPO` target for the **Devin Issues CLI**.
You’ll see it referenced in `.env` as:

```bash
DEFAULT_REPO=Saumya-Chauhan-MHC/devin-demo-service
```

When you run:

```bash
devin-cli issues list --repo Saumya-Chauhan-MHC/devin-demo-service
```

You’ll see a few pre-populated open issues, like:

```
#1  Bug: /health intermittently returns 500 (staging)
#2  Feature: Add Prometheus /metrics endpoint
#3  Enhancement: Structured JSON logs + request_id propagation
```

These mimic a real-world engineering backlog — perfect for demonstrating Devin’s scoping and PR automation.

---

## 🔍 Example Workflow

| Step           | Command                                                                    | What Happens                                                          |
| -------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| List issues | `devin-cli issues list --repo Saumya-Chauhan-MHC/devin-demo-service`       | Lists all open issues from GitHub                                     |
| Scope issue | `devin-cli issues scope -n 1 --repo Saumya-Chauhan-MHC/devin-demo-service` | Starts a Devin session to analyze the issue                           |
| Confidence  | *(auto)*                                                                   | Devin prints a scoping plan and native confidence (🟢 🟡 🔴)          |
| Create PR    | Press `y` when prompted                                                    | Devin creates a branch and opens a PR in this repo via its GitHub App |

Example CLI output:

```
Devin’s scoping
Current: /health returns 500 due to NoneType in probe
Requested: Handle probe=None safely
Tests: probe=None, probe={'status':'fail'}
Confidence: High 🟢 — straightforward fix

PR Created
https://github.com/Saumya-Chauhan-MHC/devin-demo-service/pull/9
```

---

## Repo Setup (for Testing Locally)

1. Clone this repo:

   ```bash
   git clone https://github.com/Saumya-Chauhan-MHC/devin-demo-service.git
   cd devin-demo-service
   ```

2. (Optional) Create a simple virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies (if any future ones are added):

   ```bash
   pip install -r requirements.txt
   ```

4. Run sample file:

   ```bash
   python app/main.py
   ```

---


## License

MIT License © 2025 Saumya Chauhan
Use this repository freely for demos, educational purposes, or local Devin CLI testing.

---

Would you like me to include a **“Quick Reset” section** too (e.g., for deleting branches/PRs after a demo so it’s clean before the next run)? That’s often helpful for presentations.
