# Task Manager 
A REST API for managing projects and tasks with JWT authentication.
Built with Django and Django REST Framework.
## Stack
- Python / Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Deployed on Railway

## Features
- JWT token based authentication (register, login, logout)
- Create and manage projects
- Create and manage tasks within projects
- Delegate tasks to other users
- Filter tasks by status and project
- Pagination support
- Custom permissions (only owner can edit/delete)

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/users/register/ | Register new user |
| POST | /api/users/login/ | Login and get JWT token |
| POST | /api/users/logout/ | Logout and blacklist token |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/projects/ | List all projects |
| POST | /api/projects/ | Create project |
| GET | /api/projects/<id>/ | Get single project |
| PUT | /api/projects/<id>/ | Update project |
| DELETE | /api/projects/<id>/ | Delete project |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks/ | List all tasks |
| POST | /api/tasks/ | Create task |
| GET | /api/tasks/<id>/ | Get single task |
| PUT | /api/tasks/<id>/ | Update task |
| DELETE | /api/tasks/<id>/ | Delete task |

### Filtering
| Filter | Example | Description |
|--------|---------|-------------|
| status | /api/tasks/?status=todo | Filter by status |
| project | /api/tasks/?project=1 | Filter by project |
| both | /api/tasks/?status=todo&project=1 | Filter by both |

## How to Run Locally
```bash
# Clone the repository
git clone your_github_url
cd taskmanager

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
SECRET_KEY=your_secret_key
DB_NAME=taskmanager
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```
## Live URL
https://projectmanger01.up.railway.app/api/