# Triton ML Tracker

A reproducible machine learning project environment focused on clean project structure, dependency management, and scalable ML development.

## Requirements

* Python 3.14.x
* Git

## Project Structure

Tritontracker/

* data/

  * raw/
  * processed/

* notebooks/
* configs/
* scripts/
* src/
* tests/
* .gitignore
* README.md
* pyproject.toml

## Setup

### 1\. Clone the repository

git clone https://github.com/Sakthi-5/triton-ML-tracker.git
cd triton-ML-tracker

### 2\. Create the virtual environment

python -m venv .venv

### 3\. Activate the virtual environment

Windows PowerShell:

.venv\\Scripts\\Activate.ps1

### 4\. Verify the environment

python --version

The project requires Python 3.14.x.

## One-command setup

Windows PowerShell:

.\scripts\setup.ps1

This creates the virtual environment and verifies that Python 3.14.x is being used.

After setup, activate the environment:

.venv\Scripts\Activate.ps1

## Development Status

This repository currently contains the environment and project foundation only.

ML application and pipeline logic will be added in later stages.

## License

This project is for learning and development purposes.

