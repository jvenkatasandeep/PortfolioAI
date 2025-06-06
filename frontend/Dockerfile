# ===================================
# Build Stage
# ===================================
FROM python:3.9-slim as builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY frontend/requirements.txt .
RUN pip install --user -r requirements.txt

# ===================================
# Runtime Stage
# ===================================
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_RUN_ON_SAVE=false \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    STREAMLIT_SERVER_MAX_UPLOAD_SIZE=2000 \
    STREAMLIT_SERVER_FILE_WATCHER_TYPE=none

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd --create-home appuser

# Set working directory
WORKDIR /app

# Create necessary directories
RUN mkdir -p /app/.streamlit /app/static /app/tmp

# Copy Python dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code and config
COPY frontend/ .
COPY --chown=appuser:appuser frontend/streamlit_config.toml /app/.streamlit/config.toml

# Set ownership and permissions
RUN chown -R appuser:appuser /app \
    && chmod -R 755 /app \
    && chmod -R 777 /app/tmp

# Switch to non-root user
USER appuser

# Add user's local bin to PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/healthz || exit 1

# Expose the port the app runs on
EXPOSE 8501

# Set the working directory
WORKDIR /app

# Command to run the application with production settings
ENTRYPOINT ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["app.py"]
