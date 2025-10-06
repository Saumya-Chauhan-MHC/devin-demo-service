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

Together, these files provide realistic but simple "issues" for Devin to analyze, just enough for meaningful scoping and PR creation.

---

## How It’s Used in the CLI Demo

This repo is the `DEFAULT_REPO` target for the **Devin Issues CLI**.
You’ll see it referenced in our demo's `.env` as:

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

## End-to-End Demo Reference

This repository pairs directly with the **[Devin Issues CLI Demo](https://www.loom.com/share/83ca12c2be174387a53ad76f60e5d7b3?sid=b20a888e-99e7-4311-8ad1-2d2efad2f20a)**,
which shows the full workflow from **issue listing → scoping → confidence → PR creation**.

If you’re viewing this repo in isolation, check out the CLI demo video or follow these commands:

| Step           | Command                                                                    | Description                                                         |
| -------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| List issues | `devin-cli issues list --repo Saumya-Chauhan-MHC/devin-demo-service`       | Lists open GitHub issues                                            |
| Scope issue | `devin-cli issues scope -n 1 --repo Saumya-Chauhan-MHC/devin-demo-service` | Starts a Devin session to analyze the issue                         |
| Confidence  | *(auto)*                                                                   | Devin prints the full scoping plan and native confidence (🟢 🟡 🔴) |
| Create PR    | Press `y` when prompted                                                    | Devin creates a branch and opens a PR through its GitHub App        |

Example CLI output:

```
Devin’s scoping
Current: /health returns 500 due to NoneType in probe
Requested: Handle probe=None safely
Tests: probe=None, probe={'status':'fail'}
Confidence: High 🟢 — straightforward fix

✅ PR Created
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
