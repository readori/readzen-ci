# ReadZen CI

Public CI/CD pipeline for [ReadZen].

Uses public repo CI minutes to build, test, and deploy from the private `readori/readzen` repository.

## Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| **Android Build** | Manual / Dispatch | Builds debug APK + runs lint |
| **Backend Tests** | Manual / Dispatch | Python tests with Postgres + Redis |
| **Deploy Backend** | Manual (`TRIGGER_DEPLOY`) | Full Cloudflare Worker deploy + D1 migrations |
| **Python Backend Deploy** | Manual | Deploy FastAPI backend via SSH + Docker Compose |
| **Cloudflare Setup** | Manual | Creates D1 + KV resources, init schema |
| **Release Build** | Manual | Release APK + TypeScript check |
| **Admin Bootstrap** | Manual | Bootstrap admin user / update payment secrets |
| **Security Audit** | Scheduled / Manual | Dependency vulnerability scan |

## Required Secrets

### Core
| Secret | Description |
|--------|-------------|
| `READZEN_PAT` | GitHub PAT with `repo:read` scope for `readori/readzen` |

### Cloudflare Worker Backend
| Secret | Description |
|--------|-------------|
| `CLOUDFLARE_API_TOKEN` | Cloudflare API Token (Workers, D1, KV) |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare Account ID |
| `ADMIN_API_KEY` | Admin API key for the Worker's admin endpoints |
| `STRIPE_SECRET_KEY` | Stripe secret key (optional) |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signing secret (optional) |
| `PAYPAL_CLIENT_ID` | PayPal client ID (optional) |
| `PAYPAL_CLIENT_SECRET` | PayPal client secret (optional) |

### Python FastAPI Backend (Docker / SSH)
| Secret | Description |
|--------|-------------|
| `BACKEND_SSH_HOST` | Hostname or IP of the production server |
| `BACKEND_SSH_USER` | SSH username (e.g. `deploy`) |
| `BACKEND_SSH_KEY` | SSH private key (ED25519 or RSA) |
| `BACKEND_DATABASE_URL` | PostgreSQL asyncpg URL |
| `BACKEND_REDIS_URL` | Redis URL |
| `BACKEND_SECRET_KEY` | FastAPI `SECRET_KEY` |
| `BACKEND_JWT_SECRET` | JWT signing secret |

### Android Build
| Secret | Description |
|--------|-------------|
| `MAPS_API_KEY` | Google Maps API key (optional) |
| `CI_KEYSTORE_BASE64` | Base64-encoded `.keystore` (optional — repo has committed keystore) |
| `CI_KEYSTORE_PASSWORD` | Keystore password (only needed with `CI_KEYSTORE_BASE64`) |

## Setup Guide

### First-time Cloudflare deployment
1. Add `READZEN_PAT`, `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `ADMIN_API_KEY` secrets
2. Run **Deploy Backend** → `full-setup-and-deploy`
3. Run **Admin Bootstrap** → `bootstrap-admin`

### First-time Python backend deployment
1. Add all `BACKEND_*` secrets
2. Ensure server has Docker + Docker Compose
3. Run **Python Backend Deploy** → `full-deploy`

### Subsequent deployments
- **Cloudflare Worker**: Push `TRIGGER_DEPLOY` file or run **Deploy Backend** → `deploy`
- **Python Backend**: Run **Python Backend Deploy** → `deploy`
- **DB migrations**: Run **Python Backend Deploy** → `migrate-db`
