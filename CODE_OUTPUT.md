**This file consists of the entire unaltered output for reference.**

Here is the fully functioning code with all the necessary components, including filepaths and structure. You should be able to run the application effortlessly by following the instructions provided.

---

### **Project Structure**
```
project/
├── calculator/
│   ├── __init__.py
│   ├── core.py
│   └── cli.py
├── tests/
│   └── test_core.py
├── setup.py
├── requirements.txt
├── README.md
└── main.py
```

---

### **Step 1: Implement the Core Logic (`calculator/core.py`)**
```python
# calculator/core.py

def add_numbers(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b
```

---

### **Step 2: Implement the CLI (`calculator/cli.py`)**
```python
# calculator/cli.py
import argparse
from .core import add_numbers

def main():
    parser = argparse.ArgumentParser(description="Simple calculator to add two numbers.")
    parser.add_argument('num1', type=float, help="First number")
    parser.add_argument('num2', type=float, help="Second number")
    args = parser.parse_args()

    try:
        result = add_numbers(args.num1, args.num2)
        print(f"The sum of {args.num1} and {args.num2} is {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

---

### **Step 3: Write Unit Tests (`tests/test_core.py`)**
```python
# tests/test_core.py
import pytest
from calculator.core import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(2.5, 3.5) == 6.0

if __name__ == "__main__":
    pytest.main()
```

---

### **Step 4: Create `requirements.txt`**
```txt
pytest
```

---

### **Step 5: Create `setup.py`**
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'add_numbers=calculator.cli:main',
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
)
```

---

### **Step 6: Write `README.md`**
```markdown
# Simple Calculator

A Python command-line program to add two numbers.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install the package:
   ```bash
   python setup.py install
   ```

## Usage

```bash
add_numbers <num1> <num2>
```

## Running Tests

To run the tests, use the following command:

```bash
pytest tests/
```

## Example

```bash
add_numbers 2 3
```
```

---

### **Step 7: Create `main.py`**
```python
# main.py
from calculator.cli import main

if __name__ == "__main__":
    main()
```

---

### **Step 8: Run Tests**
Run the following command to execute the tests:
```bash
pytest tests/
```

---

### **Step 9: Deploy and Use**
1. Install the package:
   ```bash
   python setup.py install
   ```
2. Use the CLI:
   ```bash
   add_numbers <num1> <num2>
   ```

---

### **Example Usage**
```bash
$ add_numbers 2 3
The sum of 2.0 and 3.0 is 5.0
```

---

This fully functioning code includes all necessary components, and you should be able to run the application effortlessly by following the instructions provided. Let me know if you need further assistance! 🚀