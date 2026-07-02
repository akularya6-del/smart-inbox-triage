.PHONY: dev dev-backend dev-frontend build test test-frontend lint migrate docker-up docker-down

dev:
	@echo "Starting backend and frontend..."
	$(MAKE) -j2 dev-backend dev-frontend

dev-backend:
	cd backend && uvicorn app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

build:
	cd frontend && npm run build

test:
	cd backend && pytest

test-frontend:
	cd frontend && npm test

lint:
	cd backend && flake8 app tests
	cd frontend && npm run lint

migrate:
	cd backend && alembic upgrade head

docker-up:
	docker compose up --build

docker-down:
	docker compose down
