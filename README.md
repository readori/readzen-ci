# ReadZen CI/CD Build Pipeline

Public repository for Android APK compilation & backend testing.  
Avoids GitHub Actions private repository CI minutes limitations.

## Workflows

| Workflow | Trigger | Purpose |
|----------|---------|--------|
| `android-build.yml` | Push to main, PR | Build debug/release APK |
| `backend-test.yml` | Push to main, PR | Run Python tests + lint |
| `release.yml` | Tag `v*` | Build release APK + upload artifacts |

## Usage

1. Push/sync source code from private `readzen` repo
2. CI workflows run automatically
3. APK artifacts available under Actions → Artifacts

## Manual Build

```bash
# Android
cd android && ./gradlew assembleDebug

# Backend tests
cd backend && pip install -r requirements.txt && python -m pytest tests/ -v
```

## Source Repository

Main development: [readori/readzen](https://github.com/readori/readzen) (private)
