# PortfolioAI Backend

FastAPI backend for the PortfolioAI application, providing AI-powered portfolio generation and management services.

## 🚀 Features

- **RESTful API**: Built with FastAPI for high performance
- **AI Integration**: Connect with AI models for content generation
- **Database**: MongoDB for data persistence
- **Authentication**: JWT-based user authentication
- **CORS**: Configured for frontend communication

## 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PortfolioAI/backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the backend directory with:
   ```
   MONGODB_URL=your_mongodb_connection_string
   JWT_SECRET_KEY=your_jwt_secret_key
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧪 Testing

To run tests:
```bash
pytest
```

## 🐳 Docker

Build and run with Docker:
```bash
docker build -t portfolioai-backend .
docker run -p 8000:8000 portfolioai-backend
```

## 📝 License

MIT License - see the [LICENSE](LICENSE) file for details.
