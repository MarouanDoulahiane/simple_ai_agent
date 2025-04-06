import json
import operator

def basic_calculator(input_str):
    """
    Perform a numeric operation on two numbers based on the input string or dictionary.

    Parameters:
    imput_str (str or dict): Either a JSON string representing a dictionary with keys 'num1', 'num2', and 'operation',
                            or a dictionary directly. Example: '{"num1": 5, "num2": 3, "operation": "add"}'

    Returns:
    str: The formatted result of the operation.

    Raises:
    Exception: If an error occurs during the operation (e.g., divistion by zero),
    ValueError: If an unsupported operation is requested or input is invalid.
    """
    try:
        # Handle both dictionary and string inputs
        if isinstance(input_str, dict):
            input_dict = input_str
        else:
            # Clean and parse the input string
            input_str_clean = input_str.replace("'", "\"")
            input_str_clean = input_str_clean.strip().strip("\"")
            input_dict = json.loads(input_str_clean)

        # Valdiate required fields
        if not all(key in input_dict for key in ["num1", "num2", "operation"]):
            return "Error: input must contain 'num1', num2', 'operation'"

        num1 = float(input_dict['num1']) # Convert to float to handle decimal numbers
        num2 = float(input_dict['num2'])
        operation = input_dict['operation'].lower() # Make case-insesitive
    except (json.JSONDecodeError, KeyError) as e:
        return "Invalid input format. Please provide valid numbers and operation."
    except ValueError as e:
        return "Error: Please provide valid numerical values."


    # Define the supported operations with error handling
    operations = {
        'add': operator.add,
        'plus': operator.add,  # Alternative word for add
        'subtract': operator.sub,
        'minus': operator.sub,  # Alternative word for subtract
        'multiply': operator.mul,
        'times': operator.mul,  # Alternative word for multiply
        'divide': operator.truediv,
        'floor_divide': operator.floordiv,
        'modulus': operator.mod,
        'power': operator.pow,
        'lt': operator.lt,
        'le': operator.le,
        'eq': operator.eq,
        'ne': operator.ne,
        'ge': operator.ge,
        'gt': operator.gt
    }

    # Check if the operation is supported
    if operation not in operations:
        return f"Unsupported operation: '{operation}'. Supported operations are: {', '.join(operations.keys())}"

    try:
        # Special handling for division by zero
        if (operation in ['divide', 'floor_divide', 'modulus']) and num2 == 0:
            return "Error: Division by zero is not allowed"

        # Perform the operation
        result = operations[operation](num1, num2)
        
        # Format result based on type
        if isinstance(result, bool):
            result_str = "True" if result else "False"
        elif isinstance(result, float):
            # Handle floating point precision
            result_str = f"{result:.6f}".rstrip('0').rstrip('.')
        else:
            result_str = str(result)


        return f"The answer is: {result_str}"
    except Exception as e:
        return f"Error during calculation: {str(e)}"
