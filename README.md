# PortfolioAI

<div align="center">
  <p>
    <a href="#">
      <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
    </a>
    <a href="https://github.com/psf/black">
      <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
    </a>
  </p>
  
  <h1>PortfolioAI</h1>
  <p>A modern, AI-powered portfolio generator that helps users create professional portfolios, resumes, and cover letters with ease.</p>
  
  <p>
    <a href="#features">Features</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#getting-started">Getting Started</a> •
    <a href="#deployment">Deployment</a> •
    <a href="#api-documentation">API Docs</a> •
    <a href="#contributing">Contributing</a>
  </p>
</div>

## 🌟 Features

- **AI-Powered Portfolio Generation**: Generate professional portfolios using advanced AI
- **Resume Builder**: Create, optimize, and customize your resume
- **Cover Letter Generator**: Generate personalized cover letters tailored to job descriptions
- **User Authentication**: Secure user accounts with JWT-based authentication
- **Responsive UI**: Modern and intuitive user interface built with Streamlit
- **Docker Support**: Containerized for easy deployment and scaling
- **Production-Ready**: Built with security, performance, and scalability in mind

## 🏗️ Architecture

PortfolioAI follows a microservices architecture with the following components:

### Backend (FastAPI)
- RESTful API service
- JWT Authentication
- PostgreSQL database
- Redis for caching and rate limiting
- Asynchronous request handling
- Background task processing

### Frontend (Streamlit)
- Interactive web interface
- Responsive design
- Real-time previews
- Theme support (light/dark mode)

### Infrastructure
- Docker containerization
- Docker Compose for local development
- Production-ready configuration
- Monitoring and logging

## 🚀 Getting Started

### Prerequisites

- Docker 20.10+ and Docker Compose 1.29+
- Python 3.9+ (for local development)
- Git

### Quick Start with Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PortfolioAI
   ```

2. **Set up environment variables**
   ```bash
   # Copy example environment files
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   
   # Update the environment variables as needed
   # (See Configuration section below for details)
   ```

3. **Build and start the services**
   ```bash
   docker-compose up -d --build
   ```

4. **Access the application**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000
   - pgAdmin (if enabled): http://localhost:5050

### Local Development Setup

1. **Set up Python virtual environment**
   ```bash
   # Backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # Frontend
   cd ../frontend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Start the backend server**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Start the frontend development server**
   ```bash
   cd frontend
   streamlit run app.py
   ```

## ⚙️ Configuration

### Backend Configuration

Create a `.env` file in the `backend` directory with the following variables:

```env
# Application
ENVIRONMENT=development
DEBUG=True

# Server
HOST=0.0.0.0
PORT=8000

# Database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-password
POSTGRES_DB=portfoliodb
POSTGRES_SERVER=db
POSTGRES_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=your-secure-redis-password
REDIS_DB=0

# JWT Authentication
SECRET_KEY=your-secure-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080  # 7 days

# File Uploads
MAX_UPLOAD_SIZE=10485760  # 10MB
```

### Frontend Configuration

Create a `.env` file in the `frontend` directory with the following variables:

```env
# Application
ENVIRONMENT=development
DEBUG=True

# Server
HOST=0.0.0.0
PORT=8501

# API
API_URL=http://localhost:8000

# Authentication
AUTH_ENABLED=True
SESSION_SECRET_KEY=your-secure-session-key
```

## 🚀 Deployment

### Docker Compose (Production)

1. **Update environment variables**
   - Set `ENVIRONMENT=production` in both backend and frontend `.env` files
   - Update all sensitive credentials
   - Configure proper CORS settings

2. **Build and start the production stack**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
   ```

3. **Verify the services**
   ```bash
   docker-compose ps
   ```

### Kubernetes (Advanced)

For production deployments, you can use the provided Kubernetes manifests in the `deploy/kubernetes` directory.

## 📚 API Documentation

Once the backend is running, you can access the following documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🛠️ Development

### Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **Mypy** for type checking

Run the following commands before committing:

```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8

# Type checking
mypy .
```

### Testing

Run tests using pytest:

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
pytest
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [Streamlit](https://streamlit.io/) - For building interactive web apps
- [PostgreSQL](https://www.postgresql.org/) - Powerful open-source database
- [Redis](https://redis.io/) - In-memory data structure store

---

<div align="center">
  <p>Made with ❤️ by the PortfolioAI Team</p>
</div>
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy example environment files
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   
   # Update the variables in both .env files with your configuration
   ```

5. **Run the application**
   - Start the backend:
     ```bash
     cd backend
     python run.py
     ```
   - In a new terminal, start the frontend:
     ```bash
     cd frontend
     streamlit run app.py
     ```
   - The application should now be running at `http://localhost:8501`

## 📚 Documentation

- [Backend API Documentation](/backend/README.md)
- [Frontend Documentation](/frontend/README.md)
- [Deployment Guide](/docs/DEPLOYMENT.md)

## 🛠 Built With

- **Frontend**: Streamlit (Python web framework)
- **Backend**: FastAPI (Python API framework)
- **Database**: Supabase
- **AI**: Groq (llama-3.3-70b-versatile)
- **Authentication**: JWT (JSON Web Tokens)
- **Templating**: Jinja2
- **Document Processing**: python-docx, PyPDF2

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project.
