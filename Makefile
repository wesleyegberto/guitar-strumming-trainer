# Makefile for Rhythm Master (macOS)

APP_NAME = Rhythm Master
PYTHON = python3
VENV = venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV)/bin/pip
REQ_FILE = requirements.txt

.PHONY: all
all: build

# 1. Ensure Tkinter support on macOS (Homebrew), create venv, and install dependencies
.PHONY: setup
setup:
	@echo "Checking Tkinter support on macOS..."
	@if command -v brew >/dev/null 2>&1; then \
		brew list python-tk@3.14 >/dev/null 2>&1 || brew install python-tk@3.14; \
	fi
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Upgrading pip and installing dependencies from $(REQ_FILE)..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r $(REQ_FILE)
	@echo "Setup complete!"

# 2. Run the app directly via Python for quick testing
.PHONY: run
run:
	@echo "Starting $(APP_NAME) in development mode..."
	$(VENV_PYTHON) main.py

# 3. Build the native macOS .app bundle
.PHONY: build
build: setup clean-build
	@echo "Building macOS bundle (.app)..."
	$(VENV_PYTHON) setup.py py2app
	@echo "Build complete! App located at: dist/$(APP_NAME).app"

# 4. Install the application into macOS /Applications
.PHONY: install
install: build
	@echo "Copying '$(APP_NAME).app' to /Applications..."
	rm -rf "/Applications/$(APP_NAME).app"
	cp -R "dist/$(APP_NAME).app" "/Applications/"
	@echo "Installed successfully!"

# 5. Clean build artifacts only
.PHONY: clean-build
clean-build:
	@echo "Cleaning build and dist directories..."
	rm -rf build dist

# 6. Full cleanup
.PHONY: clean
clean: clean-build
	@echo "Removing virtual environment and temporary files..."
	rm -rf $(VENV) __pycache__ *.pyc
	@echo "Cleanup complete!"