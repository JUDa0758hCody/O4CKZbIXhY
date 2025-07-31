# 代码生成时间: 2025-07-31 19:44:31
import gradio as gr
def generate_random_number(min_value, max_value):    """Generate a random number between min_value and max_value.

    Args:
        min_value (int): The minimum value of the random number.
        max_value (int): The maximum value of the random number.

    Returns:
        int: A random integer between min_value and max_value."""    if min_value > max_value:        raise ValueError("min_value cannot be greater than max_value")    from random import randint    return randint(min_value, max_value)

# Create a Gradio interface for the random number generator
iface = gr.Interface(
    fn=generate_random_number,
    inputs=[
        gr.Slider(minimum=1, maximum=100, step=1, label="Minimum Value"),
        gr.Slider(minimum=1, maximum=100, step=1, label="Maximum Value")
    ],
    outputs="number",
    title="Random Number Generator",
    description="Generate a random number between two specified values."
)

# Run the Gradio interface
iface.launch()