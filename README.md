# Learn Python 3

Welcome to the Learn Python 3 project! Here, you will find references, setup guides, how to run, and how to compile Python code. This guide is based on Python version 3.13.1.

## Python References
- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial on W3Schools](https://www.w3schools.com/python/)
- [Python for Beginners](https://www.pythonforbeginners.com/)

## How to Set Up Python Environment
1. **Install Python**: Download and install Python 3.13.1 from [python.org](https://www.python.org/downloads/).
2. **Set Up a Virtual Environment**:
   - Open a terminal or command prompt.
   - Run the following command to create a virtual environment:
     ```
     python -m venv myenv
     ```
   - Activate the virtual environment:
     - On Windows: `myenv\Scripts\activate`
     - On macOS/Linux: `source myenv/bin/activate`

## How to Run Python Code
1. Ensure the virtual environment is active.
2. Run the Python script with the command:
   ```
   python filename.py
   ```
   **Example**: To run a script named `app.py`, use:
   ```
   python filename.py
   ```
   **Example on macOS**: Open the terminal and run:
   ```
   python3 filename.py
   ```

## How to Compile Python Code
Python is an interpreted language, so explicit compilation is not required like in other languages. However, you can compile Python code to bytecode using the `compileall` module:
1. Open a terminal or command prompt.
2. Run the following command to compile Python files in a directory:
   ```
   python -m compileall directory_name
   ```
   **Example**: To compile all Python files in a folder named `src`, use:
   ```
   python -m compileall src
   ```
   This will generate `.pyc` files in the `__pycache__` directory.

Happy learning and experimenting with Python 3.13.1!
