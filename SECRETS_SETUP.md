# GitHub Actions Secrets Setup Guide

This document explains how to configure GitHub Actions secrets for secure CI/CD pipeline deployment.

## Required Secrets

### Application Secrets
- `DJANGO_SECRET_KEY` - Django secret key for production
- `DB_NAME` - Production database name
- `DB_USER` - Database username  
- `DB_PASSWORD` - Database password
- `DB_HOST` - Database host (e.g., AWS RDS endpoint)
- `DB_PORT` - Database port (default: 5432)

### API Configuration
- `ALLOWED_HOSTS` - Comma-separated list of allowed domains
- `CORS_ALLOWED_ORIGINS` - Comma-separated list of allowed CORS origins

### Deployment Secrets
- `DEPLOY_HOST` - Production server hostname
- `DEPLOY_USER` - SSH username for deployment
- `DEPLOY_KEY` - SSH private key for server access
- `DEPLOY_PATH` - Application path on production server

### Optional External Services
- `REDIS_URL` - Redis connection URL
- `EMAIL_HOST` - SMTP server hostname
- `EMAIL_PORT` - SMTP server port
- `EMAIL_HOST_USER` - SMTP username
- `EMAIL_HOST_PASSWORD` - SMTP password

## How to Add Secrets

### Method 1: GitHub Web Interface
1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Enter name and value
5. Click **Add secret**

### Method 2: GitHub CLI
```bash
gh secret set DJANGO_SECRET_KEY --body "your-secret-key-here"
gh secret set DB_PASSWORD --body "your-db-password"
```

### Method 3: Using .env file (for bulk setup)
```bash
# Create secrets from .env file
while IFS='=' read -r key value; do
  if [[ $key != \#* ]] && [[ -n $key ]]; then
    gh secret set "$key" --body "$value"
  fi
done < .env.production
```

## Security Best Practices

### 1. Generate Strong Secrets
```bash
# Django Secret Key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Database Password (32 characters)
openssl rand -base64 32

# SSH Key (without passphrase)
ssh-keygen -t rsa -b 4096 -f deploy_key -N ""
```

### 2. Environment-Specific Secrets
- Use different secrets for development, staging, and production
- Prefix secrets with environment: `PROD_DB_PASSWORD`, `STAGING_DB_PASSWORD`

### 3. Rotate Secrets Regularly
- Database passwords: Every 90 days
- Django secret key: When compromised or annually
- SSH keys: When compromised or annually

### 4. Access Control
- Only give repository maintainers access to production secrets
- Use GitHub environments for additional protection
- Enable approval requirements for production deployments

## Environment Configuration

### Development
Use `.env` file (gitignored):
```bash
cp .env.example .env
# Edit .env with local values
```

### Production
CI/CD automatically creates `.env` from secrets during pipeline run.

### Staging
Create separate workflow file `.github/workflows/staging.yml` with staging-specific secrets.

## Testing Secrets Locally

### Using dotenv
```bash
pip install python-dotenv
# Create .env.local with test values
python -c "from dotenv import load_dotenv; load_dotenv('.env.local'); print('Secrets loaded')"
```

### Using direnv
```bash
# .envrc
export DJANGO_SECRET_KEY="test-key-for-development"
export DB_PASSWORD="test-password"
```

## Troubleshooting

### Common Issues
1. **Secret not found**: Check spelling and ensure secret is added to correct repository
2. **Permission denied**: Verify GitHub Actions has permission to access secrets
3. **Invalid format**: Ensure secrets don't contain special characters that need escaping

### Debugging
```yaml
# In workflow file, for debugging only (remove before committing!)
- name: Debug secrets
  run: |
    echo "DB_NAME is ${{ secrets.DB_NAME }}"
    echo "ALLOWED_HOSTS is ${{ secrets.ALLOWED_HOSTS }}"
  if: github.ref == 'refs/heads/debug'  # Only on debug branch
```

## Security Monitoring

### GitHub Audit Log
Monitor who accessed secrets:
1. Go to **Settings** → **Audit log**
2. Filter by "Secrets" events
3. Review access patterns

### Automated Alerts
Set up alerts for:
- Secret modifications
- Failed deployments
- Unusual access patterns

## Compliance

### GDPR Considerations
- Document what personal data is stored
- Ensure secrets are encrypted at rest
- Implement data retention policies

### SOC 2 Compliance
- Maintain audit trails
- Implement access controls
- Regular security assessments

## Emergency Procedures

### If Secrets are Compromised
1. Immediately rotate all compromised secrets
2. Review access logs for unauthorized usage
3. Update all services with new secrets
4. Investigate root cause
5. Document incident and response

### Rollback Plan
1. Keep previous version of secrets secure
2. Test rollback procedures regularly
3. Have communication plan ready for stakeholders
