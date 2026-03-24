# CircleCI Quick Reference

## 🚀 Quick Setup Commands

### 1. Generate Required Keys
```bash
# Django Secret Keys
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# SSH Deployment Key
ssh-keygen -t rsa -b 4096 -f circleci-deploy-key -N ""

# Database Password (32 characters)
openssl rand -base64 32
```

### 2. Required Context Variables

#### **testing** Context:
- `DJANGO_SECRET_KEY`
- `DB_NAME=test_db.sqlite3`

#### **development** Context:
- `DJANGO_SECRET_KEY`
- `DB_NAME=tasksphere_dev`
- `DB_USER=dev_db_user`
- `DB_PASSWORD=dev_db_password`
- `DB_HOST=dev-db-host.com`
- `DB_PORT=5432`
- `ALLOWED_HOSTS=dev.yourdomain.com`
- `CORS_ALLOWED_ORIGINS=https://dev.yourdomain.com`

#### **production** Context:
- `DJANGO_SECRET_KEY`
- `DB_NAME=tasksphere_prod`
- `DB_USER=prod_db_user`
- `DB_PASSWORD=prod_db_password`
- `DB_HOST=prod-db-host.com`
- `DB_PORT=5432`
- `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`
- `CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com`
- `DEPLOY_HOST=your-server.com`
- `DEPLOY_USER=deploy`
- `DEPLOY_KEY=[SSH private key]
- `DEPLOY_PATH=/var/www/tasksphere`

### 3. Workflow Triggers
- **All branches** → `test` + `security` jobs
- **develop branch** → `deploy-staging` job
- **main branch** → `deploy-production` job

### 4. Environment File Creation
CircleCI automatically creates `.env` files from context variables during pipeline runs.

## 🔧 Configuration Files

- `.circleci/config.yml` - Main CircleCI configuration
- `CIRCLECI_SETUP.md` - Detailed setup guide
- `requirements.txt` - Python dependencies (includes requests)

## 🎯 Key Features

- ✅ **Context-based secrets management**
- ✅ **Environment separation** (test/dev/prod)
- ✅ **Automated testing and security scanning**
- ✅ **Branch-based deployments**
- ✅ **SSH key management for deployments**
- ✅ **Health checks and verifications**
