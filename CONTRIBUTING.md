# 🤝 Contributing to Densify AI

Thank you for your interest in contributing to Densify AI! This document provides guidelines and instructions for contributing.

## Getting Started

### 1. Fork the Repository
Click the "Fork" button on GitHub to create your own copy.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/Densify-AI.git
cd Densify-AI
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
```

### 4. Set Up Development Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## Development Workflow

### Before Making Changes
1. Pull latest changes: `git pull origin main`
2. Create a new branch
3. Make sure tests pass: `pytest tests/ -v`

### Making Changes
1. Follow PEP 8 style guide
2. Add docstrings to functions
3. Write/update tests for new features
4. Keep commits atomic and meaningful

### Code Style
```python
# Good: Clear and documented
def detect_people(frame):
    """
    Detect people in a frame using YOLOv8
    
    Args:
        frame: Input video frame
        
    Returns:
        tuple: (count, boxes_list)
    """
    # Implementation
    pass

# Avoid: Unclear variable names
def fn(f):
    # Implementation
    pass
```

---

## Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test
```bash
pytest tests/test_detector.py -v
```

### Create New Tests
```python
# tests/test_new_feature.py
import pytest
from src.utils.new_module import new_function

def test_new_function():
    result = new_function(input_data)
    assert result == expected_output
```

---

## Committing Changes

### Commit Message Format
```
type: brief description

Detailed description of changes
- Change 1
- Change 2

Fixes #issue_number (if applicable)
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build, dependencies

### Example
```bash
git commit -m "feat: add heatmap visualization

- Implement heatmap generation
- Add visualization to dashboard
- Update requirements with required packages

Fixes #42"
```

---

## Creating a Pull Request

1. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Go to GitHub and click "Compare & pull request"

3. Fill in the PR template:
   - Describe changes clearly
   - Link related issues
   - Add screenshots if UI changes
   - List breaking changes if any

4. Wait for review and CI/CD checks

---

## PR Checklist

- [ ] Code follows PEP 8
- [ ] Tests pass: `pytest tests/ -v`
- [ ] New tests added for new features
- [ ] Docstrings added/updated
- [ ] No print statements (use logging)
- [ ] Imports sorted and cleaned
- [ ] Requirements.txt updated if dependencies added
- [ ] README/docs updated if needed

---

## Code Guidelines

### Import Order
```python
# Standard library
import os
import sys

# Third-party
import numpy as np
from flask import Flask

# Local
from src.config import DEBUG
from src.utils.detector import detect_people
```

### Naming Conventions
- Classes: `PascalCase` - `class PeopleDetector`
- Functions: `snake_case` - `def detect_people`
- Constants: `UPPER_SNAKE_CASE` - `MODEL_PATH`
- Private: prefix with `_` - `def _helper_function`

### Documentation
```python
def complex_function(param1, param2):
    """
    Brief description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Type: Description of return value
        
    Raises:
        ValueError: When something is wrong
        
    Examples:
        >>> result = complex_function(1, 2)
        >>> result
        3
    """
    pass
```

---

## Reporting Issues

### Bug Report Template
```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: macOS/Linux/Windows
- Python version: 3.10
- Dependencies: from `pip list`

## Screenshots
If applicable, add screenshots
```

### Feature Request Template
```markdown
## Feature Description
What feature are you requesting?

## Use Case
Why do you need this feature?

## Possible Solution
How would you implement it?

## Alternatives
Other solutions considered
```

---

## Review Process

- Maintainers will review your PR
- Changes may be requested
- Once approved, your PR will be merged
- Your contribution will be credited!

---

## Setting Up IDE

### VS Code
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "autopep8",
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "ms-python.python"
    }
}
```

### PyCharm
1. Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Select "Existing Environment" → venv/bin/python

---

## Contact

- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Email: For security issues

---

**Thank you for contributing! 🎉**
