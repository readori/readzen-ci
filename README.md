# ReadZen CI

Public CI/CD pipeline for [ReadZen].

Uses public repo CI minutes to build, test, and deploy from the private `readori/readzen` repository.

## Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| **Android Build** | Manual / Dispatch | Builds debug APK + runs lint |
| **Backend Tests** | Manual / Dispatch | Python tests with Postgres + Redis |
| **Cloudflare Deploy** | Manual / Dispatch | Deploys Workers backend |
| **Cloudflare Setup** | Manual (provision/init-schema/status) | Creates D1 + KV resources |
| **Release Build** | Manual | Release APK + TypeScript check |

## Required Secrets

| Secret | Description |
|--------|-------------|
| `READZEN_PAT` | **Required** — GitHub PAT with `repo` scope for `readori/readzen` |
| `CLOUDFLARE_API_TOKEN` | Cloudflare API Token |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare Account ID |
| `MAPS_API_KEY` | Google Maps API key (optional, for Android builds) |

## Setup

1. Create a **fine-grained GitHub PAT** at https://github.com/settings/tokens?type=beta
   - Resource: `readori/readzen`
   - Permissions: `Contents: Read`
2. Add as `READZEN_PAT` secret in this repo's Settings → Secrets
3. Add Cloudflare secrets
4. Run **Cloudflare Infrastructure Setup** → `provision`
5. Update `wrangler.toml` with the D1/KV IDs
6. Run **Cloudflare Infrastructure Setup** → `init-schema`
7. Run **Cloudflare Deploy**
