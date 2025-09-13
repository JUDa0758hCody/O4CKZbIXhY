# 代码生成时间: 2025-09-13 23:54:06
import gr
import random
import string

"""
Test data generator using the Gradio framework.
This program generates random test data for testing purposes.

Usage:
    Run the program to start the Gradio interface.
    The interface will provide a text input for the number of test data entries.
    After entering the number and clicking 'Generate', the generated test data will be displayed.
"""

# Function to generate a random string of a given length
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Function to generate test data
def generate_test_data(num_entries):
    """
    Generate test data.

    Args:
        num_entries (int): Number of test data entries to generate.

    Returns:
        list: A list of test data entries.

    Raises:
        ValueError: If the number of entries is not a positive integer.
    """
    if not isinstance(num_entries, int) or num_entries <= 0:
        raise ValueError("Number of entries must be a positive integer.")
    
    test_data = []
    for _ in range(num_entries):
        # Generate random string of length 10
        random_string = generate_random_string(10)
        # Generate a random integer between 1 and 100
        random_number = random.randint(1, 100)
        # Append the generated data to the list
        test_data.append({"string": random_string, "number": random_number})
    
    return test_data

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_test_data,
    inputs=[gr.inputs.Number(label="Number of entries")],
    outputs=[gr.outputs.JSON(label="Generated test data")],
    title="Test Data Generator",
    description="Generate random test data using Gradio."
)

# Run the Gradio interface
iface.launch()