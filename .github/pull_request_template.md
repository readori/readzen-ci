## ⚠️ Security Notice

This is a CI/CD pipeline repository. All changes are security-sensitive.

### Checklist
- [ ] No secrets or tokens hardcoded in files
- [ ] Workflow permissions use least-privilege principle
- [ ] No `pull_request_target` triggers added
- [ ] All secrets accessed via `${{ secrets.* }}` only
- [ ] Artifact retention set to minimum needed
- [ ] Changes reviewed by @readori
