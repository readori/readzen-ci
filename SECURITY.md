# Security Policy

## ⚠️ This Repository

This is a **CI/CD pipeline repository** for the ReadZen project. It contains workflow definitions that access sensitive secrets (API tokens, PATs, deployment keys).

## Security Measures

### Workflow Triggers
- ✅ `workflow_dispatch` (manual only) — requires repository write access
- ✅ `repository_dispatch` — requires PAT with repo scope
- ❌ `push` triggers — **disabled** to prevent fork exploitation
- ❌ `pull_request` / `pull_request_target` — **never used** (prevents fork secret access)

### Secret Protection
- All secrets stored in GitHub Encrypted Secrets
- Secrets passed via `env:` variables (not direct `${{ }}` interpolation in `run:`)
- Infrastructure IDs masked in logs via `::add-mask::`
- Artifact retention set to **1 day** (minimizes exposure window)
- `persist-credentials: false` on all checkout steps

### Access Control
- CODEOWNERS requires @readori approval for all changes
- Workflow caller verification (main branch only)
- Concurrency controls prevent parallel secret access
- Job timeout limits prevent runaway processes

### What Forks CANNOT Do
- ❌ Execute workflows (no push/PR triggers)
- ❌ Access secrets (GitHub prevents this for forks)
- ❌ Modify protected workflows without owner review
- ❌ Read workflow run logs (require authentication)

## Reporting Vulnerabilities

If you discover a security vulnerability, please report it privately to the repository owner.

## Secret Rotation

Secrets should be rotated regularly:
- `READZEN_PAT` — every 90 days
- `CLOUDFLARE_API_TOKEN` — every 90 days  
- `JWT_SECRET` / `SECRET_KEY` — every 180 days
