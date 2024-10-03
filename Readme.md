# Django Project Quickstart Template

This template provides a streamlined setup for quickly starting Django projects with best practices for virtual environments, dependency management, and pre-commit hooks.

## Setup

1. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```

2. **Install dependencies**:
   - Install development dependencies:
     ```sh
     pip install -r requirements-dev.txt
     ```
   - Install production dependencies:
     ```sh
     pip install -r requirements.txt
     ```
3. **Install precommit**:
   - Install precommit to handle checks before commit
     ```sh
     pre-commit.ext install
     ```

## Dependency Management

We use [pip-tools](https://pypi.org/project/pip-tools/) to handle dependencies efficiently:

1. Add your production dependencies to `requirements.in`:

   - Example: `Django==5.1.1`

2. Compile the `requirements.txt` file:

   ```bash
   pip-compile requirements.in
   ```

3. Install the compiled dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Development dependencies (such as `pip-tools`, linters, and formatters) are listed in `requirements-dev.txt`.

## Summary of Pre-commit Checks

Run pre-commit checks using:

```bash
pre-commit run -a
```

This will check for:

1. **Trailing whitespace**: Removes unnecessary spaces.
2. **End-of-file fixer**: Ensures all files end with a newline.
3. **Check large files**: Warns if large files are added.
4. **isort**: Ensures imports are properly sorted.
5. **Black**: Automatically formats Python code to PEP8 standards.
6. **Flake8**: Lints the Python code for errors.
7. **Bandit**: Checks for common security issues.
8. **Django check**: Validates Django project configurations with `python manage.py check`.

## Things not included in this Django Quickstart

1. Authentication
2. Frontend styling
3. File storage

## License

This template is provided under the MIT License.
