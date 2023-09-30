MANAGE_PY := ./lenta/manage.py

run:
	@echo "Running the application..."
	$(MANAGE_PY) runserver

migrate:
	@echo "Running migrations..."
	$(MANAGE_PY) makemigrations
	$(MANAGE_PY) migrate

createsuperuser:
	@echo "Creating superuser..."
	$(MANAGE_PY) createsuperuser

test:
	@echo "Running tests..."
	$(MANAGE_PY) test

clear:
	@echo "Clearing cache..."
	rm -rf .ruff_cache

lint:
	@echo "Running linter..."
	black .
	ruff check .
