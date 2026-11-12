.PHONY: setup setup-backend setup-frontend run run-backend run-frontend test lint clean

# ============================================
# Full Setup
# ============================================
setup: setup-backend setup-frontend
	@echo "✅ Setup complete!"

setup-backend:
	cd backend && python -m venv venv && venv\Scripts\pip install -r requirements.txt
	cd backend && venv\Scripts\alembic upgrade head

setup-frontend:
	cd frontend && npm install

# ============================================
# Run Development Servers
# ============================================
run-backend:
	cd backend && venv\Scripts\uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-frontend:
	cd frontend && npm run dev

# ============================================
# Testing
# ============================================
test:
	cd backend && venv\Scripts\pytest tests/ -v

test-coverage:
	cd backend && venv\Scripts\pytest tests/ -v --cov=app --cov-report=html

# ============================================
# Linting
# ============================================
lint:
	cd backend && venv\Scripts\ruff check app/
	cd frontend && npm run lint

lint-fix:
	cd backend && venv\Scripts\ruff check app/ --fix
	cd frontend && npm run lint -- --fix

# ============================================
# Database
# ============================================
db-migrate:
	cd backend && venv\Scripts\alembic upgrade head

db-reset:
	cd backend && del fake_news.db 2>NUL & venv\Scripts\alembic upgrade head

# ============================================
# Docker
# ============================================
docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

# ============================================
# Clean
# ============================================
clean:
	cd backend && rmdir /s /q venv 2>NUL & rmdir /s /q __pycache__ 2>NUL & del fake_news.db 2>NUL
	cd frontend && rmdir /s /q node_modules 2>NUL & rmdir /s /q dist 2>NUL
	@echo "🧹 Cleaned!"
