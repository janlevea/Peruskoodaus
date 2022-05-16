@echo off
REM python -m unittest %*
pytest --cov --cov-report=term-missing %*
