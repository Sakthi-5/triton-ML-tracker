# Check system Python version
$pythonVersion = python --version
Write-Host "Using $pythonVersion"

# Create the virtual environment if it does not already exist
if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

# Verify the Python version inside the virtual environment
$venvPython = & ".\.venv\Scripts\python.exe" --version
Write-Host "Virtual environment Python: $venvPython"

Write-Host "Virtual environment is ready."