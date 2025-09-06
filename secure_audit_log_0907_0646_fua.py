# 代码生成时间: 2025-09-07 06:46:40
import gradio as gr
def log_event(event_type, event_detail):
    """
    Logs an event to the audit log.

    Parameters:
    - event_type (str): The type of event being logged.
    - event_detail (str): The details of the event.
    """
    try:
        # Open the log file and append the event.
        with open("audit_log.txt", "a") as log_file:
            log_file.write(f"{event_type}: {event_detail}
")
    except IOError as e:
        print(f"Error writing to log file: {e}")

def main():
    """
    The main function of the program, sets up the Gradio interface.
    """
    with gr.Blocks() as demo:
        # Define the interface elements.
        input_event_type = gr.Textbox(label="Event Type")
        input_event_detail = gr.Textbox(label="Event Detail")
        submit_button = gr.Button("Log Event")
        output_text = gr.Textbox(label="Log Status")
        
        # Define the function to be called when the button is pressed.
        def log_event_interface(event_type, event_detail):
            log_event(event_type, event_detail)
            return "Event logged successfully."
        
        # Link the interface elements to the function.
        submit_button.click(log_event_interface, inputs=[input_event_type, input_event_detail], outputs=output_text)
        
    # Launch the interface.
    demo.launch()

if __name__ == "__main__":
    main()