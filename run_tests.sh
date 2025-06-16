#!/bin/bash

# Create reports directory if it doesn't exist
mkdir -p reports

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment activated: $(pwd)/.venv"
        echo "Installing/updating requirements..."
        pip install -r requirements.txt
        echo "Installing package in development mode..."
        pip install -e .
        echo "Installing Playwright browsers..."
        playwright install
    else
        echo "❌ Failed to activate virtual environment"
        exit 1
    fi
else
    echo "❌ Virtual environment not found. Please create it first:"
    echo "python -m venv .venv"
    exit 1
fi

# Run tests with both Playwright and coverage reports
echo "Running tests and generating reports..."
pytest --html=reports/playwright-report.html --self-contained-html --cov=backend --cov-report=html:reports/htmlcov

# Check if tests passed
if [ $? -eq 0 ]; then
    echo "✅ Tests completed successfully!"
    
    # Run LLM evaluation
    echo "Running LLM evaluation..."
    python metrics/run_evaluation.py
    
    # Print report locations
    echo "📊 Reports generated in the 'reports' directory:"
    echo "   - Playwright report: reports/playwright-report.html"
    echo "   - Coverage report: reports/htmlcov/index.html"
    echo "   - LLM evaluation report: reports/llm_evaluation_report.html"
    
    # Open reports in browser based on OS
    echo "Opening reports in browser..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open reports/playwright-report.html
        open reports/htmlcov/index.html
        open reports/llm_evaluation_report.html
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open reports/playwright-report.html
        xdg-open reports/htmlcov/index.html
        xdg-open reports/llm_evaluation_report.html
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        # Windows
        start reports/playwright-report.html
        start reports/htmlcov/index.html
        start reports/llm_evaluation_report.html
    fi
else
    echo "❌ Tests failed!"
    exit 1
fi 