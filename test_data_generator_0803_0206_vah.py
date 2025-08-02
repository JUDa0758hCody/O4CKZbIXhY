# 代码生成时间: 2025-08-03 02:06:33
import gr
import random

"""
Test Data Generator using Gradio framework.
This program generates random test data for user testing.
"""

def generate_test_data():
    """
    Generate random test data.
    """
    # Generate random integers for age and ID
    age = random.randint(18, 100)
    user_id = random.randint(100000, 999999)
    
    # Generate random strings for first and last names
    first_names = ["John", "Jane", "Bob", "Alice"]
    last_names = ["Doe", "Smith", "Johnson", "Williams"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    # Return the generated test data as a dictionary
    return {
        "age": age,
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name
    }


def main():
    """
    Main function to create a Gradio interface for test data generation.
    """
    # Create a Gradio interface
    demo = gr.Interface(
        fn=generate_test_data,
        inputs=[],
        outputs="json",
        live=True
    )
    
    # Start the Gradio interface
    demo.launch()

if __name__ == "__main__":
    main()