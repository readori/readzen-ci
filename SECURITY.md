# Security Policy

## ⚠️ This Repository

This is a **CI/CD pipeline repository** for the ReadZen project. It contains workflow definitions that access sensitive secrets.

## Security Measures

### Workflow Triggers
- ✅ `workflow_dispatch` (manual only) — requires repository write access
- ✅ `repository_dispatch` — requires PAT with repo scope
- ❌ `push` triggers — **disabled** on build/deploy workflows
- ❌ `pull_request` / `pull_request_target` — **never used** on sensitive workflows
- ℹ️ `push` trigger on `security-audit.yml` only (read-only, no secrets)

### Secret Protection
- All secrets stored in GitHub Encrypted Secrets
- Secrets passed via `env:` variables (not direct `${{ }}` interpolation in `run:`)
- GitHub context values (`actor`, `ref`, `sha`) passed via `env:` to prevent injection
- Infrastructure IDs masked in logs via `::add-mask::`
- Artifact retention set to **1 day** (minimizes exposure window)
- `persist-credentials: false` on **all** checkout steps
- Wrangler output filtered to exclude sensitive patterns

### Access Control
- CODEOWNERS requires @readori approval for all changes
- Workflow caller verification (main branch only)
- Concurrency controls on **all** workflows prevent parallel secret access
- Job timeout limits on **all** jobs prevent runaway processes
- Security audit scans entire push range (not just last commit)

### What Forks CANNOT Do
- ❌ Execute build/deploy workflows (no push/PR triggers)
- ❌ Access secrets (GitHub prevents this for forks)
- ❌ Modify protected workflows without owner review
- ❌ Read workflow run logs (require authentication)

## Secret Rotation Schedule

| Secret | Rotation | Last Rotated |
|--------|----------|--------------|
| `READZEN_PAT` | Every 90 days | 2026-04-20 |
| `CLOUDFLARE_API_TOKEN` | Every 90 days | 2026-04-20 |
| `JWT_SECRET` | Every 180 days | 2026-04-20 |
| `SECRET_KEY` | Every 180 days | 2026-04-20 |

## Reporting Vulnerabilities

Report security issues privately to the repository owner.
