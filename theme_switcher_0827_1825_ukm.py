# 代码生成时间: 2025-08-27 18:25:09
import gradio as gr
def switch_theme(theme):
    """
    Function to switch the theme based on the user's input.
    Args:
    - theme (str): The theme to switch to.
    Returns:
    - str: A message indicating the theme has been switched successfully.
    """
    try:
        if theme not in ['light', 'dark']:
            raise ValueError("Invalid theme. Please choose 'light' or 'dark'.")
        return f"Theme switched to {theme} successfully."
    except Exception as e:
        return str(e)

# Define the Gradio interface
iface = gr.Interface(
    fn=switch_theme,
    inputs=gr.Textbox(label="Enter theme (light/dark)"),
    outputs="text",
    title="Theme Switcher",
    description="A simple theme switcher application."
)

# Run the Gradio interface
iface.launch()