# GitHub Actions Secrets Quick Reference

## Essential Commands

### Add Secrets via CLI
```bash
# Application secrets
gh secret set DJANGO_SECRET_KEY --body "$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
gh secret set DB_NAME --body "tasksphere_prod"
gh secret set DB_USER --body "tasksphere_user"
gh secret set DB_PASSWORD --body "$(openssl rand -base64 32)"
gh secret set DB_HOST --body "your-db-host.com"
gh secret set DB_PORT --body "5432"

# API configuration
gh secret set ALLOWED_HOSTS --body "yourdomain.com,www.yourdomain.com"
gh secret set CORS_ALLOWED_ORIGINS --body "https://yourdomain.com,https://www.yourdomain.com"

# Deployment secrets
gh secret set DEPLOY_HOST --body "your-server.com"
gh secret set DEPLOY_USER --body "deploy"
gh secret set DEPLOY_KEY --body "$(cat ~/.ssh/deploy_key)"
gh secret set DEPLOY_PATH --body "/var/www/tasksphere"
```

### List Secrets
```bash
gh secret list
```

### Remove Secrets
```bash
gh secret delete DJANGO_SECRET_KEY
```

## Required Secrets Checklist

- [ ] `DJANGO_SECRET_KEY` - Django secret key
- [ ] `DB_NAME` - Database name
- [ ] `DB_USER` - Database username
- [ ] `DB_PASSWORD` - Database password
- [ ] `DB_HOST` - Database host
- [ ] `DB_PORT` - Database port
- [ ] `ALLOWED_HOSTS` - Allowed domains
- [ ] `CORS_ALLOWED_ORIGINS` - CORS origins
- [ ] `DEPLOY_HOST` - Server hostname
- [ ] `DEPLOY_USER` - SSH username
- [ ] `DEPLOY_KEY` - SSH private key
- [ ] `DEPLOY_PATH` - Deployment path

## Security Tips

1. **Never commit secrets to repository**
2. **Use different secrets for each environment**
3. **Rotate secrets regularly**
4. **Monitor access logs**
5. **Use GitHub environments for production**
