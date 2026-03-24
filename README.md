# Task Management 

A Django REST API for task management demonstrating full CRUD operations, authentication, and secure CI/CD pipeline using GitHub Actions secrets.

## Features

- ✅ User authentication and authorization
- ✅ Task CRUD operations with title and description
- ✅ Task status management (to_do, in_progress, completed, outdated)
- ✅ Secure CI/CD pipeline with GitHub Actions secrets
- ✅ Automated testing and security scanning
- ✅ Production deployment automation

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TaskSphere-backend
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your local settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `POST /api/logout/` - User logout

### Tasks
- `GET /api/tasks/` - List user's tasks
- `POST /api/tasks/` - Create new task
- `GET /api/tasks/{id}/` - Get specific task
- `PUT /api/tasks/{id}/` - Update task
- `PATCH /api/tasks/{id}/` - Partial update task
- `DELETE /api/tasks/{id}/` - Delete task

### Task Statuses
- `to_do` - Initial state
- `in_progress` - Currently working on
- `completed` - Finished
- `outdated` - No longer relevant

## CI/CD Pipeline

### Workflow Triggers
- **Push to main/develop**: Runs full test suite and deploys to production (main only)
- **Pull requests**: Runs tests and security checks
- **Manual**: Can trigger test workflow manually

### Security Features
- ✅ GitHub Actions secrets integration
- ✅ Automated security scanning (Safety, Bandit)
- ✅ Dependency vulnerability checks
- ✅ Code quality checks
- ✅ Environment-specific configurations

### Required GitHub Secrets

See [SECRETS_SETUP.md](SECRETS_SETUP.md) for detailed setup instructions.

**Essential secrets:**
- `DJANGO_SECRET_KEY` - Django secret key
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` - Database credentials
- `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS` - API configuration
- `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY` - Deployment credentials

### Quick Setup Commands

```bash
# Install GitHub CLI (if not installed)
# macOS: brew install gh
# Ubuntu: sudo apt install gh
# Windows: winget install GitHub.cli

# Set essential secrets
gh secret set DJANGO_SECRET_KEY --body "$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
gh secret set DB_NAME --body "tasksphere_prod"
gh secret set DB_USER --body "tasksphere_user"
gh secret set DB_PASSWORD --body "$(openssl rand -base64 32)"
```

## Testing

### Run Tests Locally
```bash
python manage.py test
```

### Run Security Checks
```bash
pip install safety bandit
safety check
bandit -r .
```

### Test CI/CD Locally
```bash
# Install act (GitHub Actions runner)
# macOS: brew install act
# Ubuntu: sudo apt install act
act -j test-secrets
```

## Project Structure

```
TaskSphere-backend/
├── .github/workflows/          # CI/CD pipelines
│   ├── ci-cd.yml            # Main pipeline
│   └── test-secrets.yml     # Secrets testing
├── api/                      # Django app
│   ├── migrations/           # Database migrations
│   ├── models.py            # Task model
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   └── urls.py             # API URLs
├── tasksphere/              # Django project settings
├── .env.example            # Environment template
├── .env.production.template # Production config template
├── requirements.txt         # Python dependencies
├── SECRETS_SETUP.md        # Detailed secrets guide
├── SECRETS_QUICKSTART.md   # Quick reference
└── README.md              # This file
```

## Security Best Practices

1. **Never commit secrets to repository**
2. **Use different secrets for each environment**
3. **Rotate secrets regularly**
4. **Monitor access logs**
5. **Keep dependencies updated**

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Check [SECRETS_SETUP.md](SECRETS_SETUP.md) for CI/CD issues
- Review GitHub Actions logs for pipeline problems
- Create an issue for bugs or feature requests