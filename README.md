# Speed Measurement for Python Functions

## Description

This project is designed to measure the execution time of various functions in Python. It allows you to compare the performance of functions that perform similar tasks, which is particularly useful for code optimization. By providing a straightforward way to assess execution times, developers can make informed decisions about performance improvements, especially considering that Python can be slower compared to other programming languages.

## Installation

To work with this project, you only need to have Python version `3.x` installed. Clone or download the repository to your computer:

```bash
git clone https://github.com/OlyoshaOlyosha/PythonFunctionSpeedTest.git
```

## Usage

1. **Changing Parameters**:  You can modify the function arguments directly in the code. You can input any number of arguments, and they will be applied to all functions simultaneously. Alternatively, you can define the arguments within the functions themselves if you prefer.

    ```python
    n = 10000000
    ```

2. **Adding Functions**: To add a new function for measurement, simply define it in the code and include it in the `functions` list. For example:

    ```python
    def func3(n):
        # Your code here
        return result

    functions = [func1, func2, func3]  # Add your function here
    ```

3. **Running Measurements**: Run the script to automatically measure the execution time of all functions in the `functions` list:

    ```bash
    python function_speed_test.py
    ```

4. **Viewing Results**: After the script finishes executing, you will see the execution time for each function, along with their results.

## License

This project is licensed under the MIT License. You are free to use and modify it as you wish.
