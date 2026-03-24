# CircleCI Contexts Setup Guide

This guide explains how to configure CircleCI contexts for secure environment variable management in your CI/CD pipeline.

## 🎯 What Are CircleCI Contexts?

CircleCI contexts are collections of environment variables that can be shared across projects and workflows. They provide:
- **Secure storage** for sensitive data
- **Reusable configurations** across multiple projects
- **Access control** through organization-level permissions
- **Environment separation** (dev, staging, production)

## 📋 Required Contexts

### 1. **testing** Context
Used for test runs and security scans.

**Environment Variables:**
```bash
DJANGO_SECRET_KEY=your-test-secret-key
DB_NAME=test_db.sqlite3
```

### 2. **development** Context  
Used for staging deployments.

**Environment Variables:**
```bash
DJANGO_SECRET_KEY=your-dev-secret-key
DB_NAME=tasksphere_dev
DB_USER=dev_db_user
DB_PASSWORD=dev_db_password
DB_HOST=dev-db-host.com
DB_PORT=5432
ALLOWED_HOSTS=dev.yourdomain.com
CORS_ALLOWED_ORIGINS=https://dev.yourdomain.com
```

### 3. **production** Context
Used for production deployments.

**Environment Variables:**
```bash
DJANGO_SECRET_KEY=your-prod-secret-key
DB_NAME=tasksphere_prod
DB_USER=prod_db_user
DB_PASSWORD=prod_db_password
DB_HOST=prod-db-host.com
DB_PORT=5432
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
DEPLOY_HOST=your-server.com
DEPLOY_USER=deploy
DEPLOY_KEY=-----BEGIN RSA PRIVATE KEY-----
[Your private key content]
-----END RSA PRIVATE KEY-----
DEPLOY_PATH=/var/www/tasksphere
```

## 🔧 Setting Up Contexts

### Step 1: Create Contexts in CircleCI

1. **Log in to CircleCI** (https://circleci.com)
2. **Go to Organization Settings**
3. **Select "Contexts" from the left menu**
4. **Click "Create Context"** for each context:

#### Create "testing" Context:
- **Name:** `testing`
- **Description:** `Testing environment variables`

#### Create "development" Context:
- **Name:** `development`  
- **Description:** `Development environment variables`

#### Create "production" Context:
- **Name:** `production`
- **Description:** `Production environment variables`

### Step 2: Add Environment Variables

For each context, add the required environment variables:

#### In "testing" Context:
1. Click "Add Environment Variable"
2. **Variable Name:** `DJANGO_SECRET_KEY`
3. **Value:** Generate with: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
4. Click "Add Variable"

5. **Variable Name:** `DB_NAME`
6. **Value:** `test_db.sqlite3`
7. Click "Add Variable"

#### In "development" Context:
Add all development variables following the same process.

#### In "production" Context:
Add all production variables, including the deployment SSH key.

### Step 3: Set Up SSH Key for Production

1. **Generate SSH Key:**
```bash
ssh-keygen -t rsa -b 4096 -f circleci-deploy-key -N ""
```

2. **Add Public Key to Server:**
```bash
ssh-copy-id -i circleci-deploy-key.pub user@your-server.com
```

3. **Add Private Key to CircleCI:**
   - In "production" context
   - Variable Name: `DEPLOY_KEY`
   - Value: Content of `circleci-deploy-key` (private key)
   - Include the entire key including `-----BEGIN` and `-----END` lines

## 🔐 Security Best Practices

### 1. **Access Control**
- Only give necessary team members access to production context
- Use different contexts for different environments
- Regularly review context permissions

### 2. **Key Management**
- Generate unique keys for each environment
- Rotate secrets regularly (every 90 days)
- Use strong passwords and keys

### 3. **Audit Trail**
- Monitor context usage in CircleCI
- Review access logs regularly
- Set up alerts for context modifications

## 🚀 Workflow Triggers

### Branch-Based Deployment:
- **`develop` branch** → Triggers `deploy-staging` job
- **`main` branch** → Triggers `deploy-production` job
- **All branches** → Run `test` and `security` jobs

### Manual Deployment:
You can also trigger deployments manually from the CircleCI dashboard.

## 📊 Environment Variable Reference

| Variable | Testing | Development | Production | Description |
|----------|---------|-------------|------------|-------------|
| `DJANGO_SECRET_KEY` | ✅ | ✅ | ✅ | Django secret key |
| `DB_NAME` | ✅ | ✅ | ✅ | Database name |
| `DB_USER` | ❌ | ✅ | ✅ | Database username |
| `DB_PASSWORD` | ❌ | ✅ | ✅ | Database password |
| `DB_HOST` | ❌ | ✅ | ✅ | Database host |
| `DB_PORT` | ❌ | ✅ | ✅ | Database port |
| `ALLOWED_HOSTS` | ❌ | ✅ | ✅ | Allowed domains |
| `CORS_ALLOWED_ORIGINS` | ❌ | ✅ | ✅ | CORS origins |
| `DEPLOY_HOST` | ❌ | ❌ | ✅ | Deployment server |
| `DEPLOY_USER` | ❌ | ❌ | ✅ | SSH username |
| `DEPLOY_KEY` | ❌ | ❌ | ✅ | SSH private key |
| `DEPLOY_PATH` | ❌ | ❌ | ✅ | Deployment path |

## 🛠️ Testing Your Setup

### 1. **Test Context Access:**
```bash
# Push to develop branch
git push origin develop

# Check CircleCI dashboard for successful deployment
```

### 2. **Test Production Deployment:**
```bash
# Push to main branch
git push origin main

# Monitor production deployment
```

### 3. **Verify Environment Variables:**
Check job logs to ensure environment variables are properly loaded:
```bash
# Look for these lines in CircleCI logs
echo "SECRET_KEY is set: ${DJANGO_SECRET_KEY:0:20}..."
echo "DB_NAME: ${DB_NAME}"
```

## 🔍 Troubleshooting

### Common Issues:

1. **Context Not Found:**
   - Ensure context names match exactly in config.yml
   - Check context spelling and case sensitivity

2. **Environment Variable Missing:**
   - Verify variable names match between context and config
   - Check for typos in variable names

3. **Permission Denied:**
   - Ensure project has access to the context
   - Check organization-level permissions

4. **SSH Key Issues:**
   - Verify SSH key format in CircleCI
   - Check server SSH configuration
   - Test SSH connection manually

### Debug Commands:
Add these to your CircleCI jobs for debugging:
```yaml
- run:
    name: Debug environment variables
    command: |
      echo "Available environment variables:"
      env | grep -E "(DB_|DEPLOY_|DJANGO_)" | sort
```

## 📚 Additional Resources

- [CircleCI Contexts Documentation](https://circleci.com/docs/2.0/contexts/)
- [CircleCI Environment Variables](https://circleci.com/docs/2.0/env-vars/)
- [CircleCI Security Best Practices](https://circleci.com/docs/2.0/best-practices/#security)

## 🎉 Summary

CircleCI contexts provide a secure, scalable way to manage environment variables across your CI/CD pipeline. By separating environments into different contexts, you ensure:

- ✅ **Security** - Sensitive data is encrypted and access-controlled
- ✅ **Flexibility** - Different configurations for different environments  
- ✅ **Maintainability** - Centralized management of environment variables
- ✅ **Scalability** - Easy to add new projects and environments
