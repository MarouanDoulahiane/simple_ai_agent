def reverse_string(input_string):
    """
    Reverse the given string.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        return "Error: Input must be a string"
    
    # Reverse the string using slicing
    reversed_string = input_string[::-1]
    
    # Format the output
    result = f"The reversed string is: {reversed_string}"
    
    return result
