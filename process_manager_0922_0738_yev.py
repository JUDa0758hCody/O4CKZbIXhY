# 代码生成时间: 2025-09-22 07:38:34
import psutil
from gradio import Interface, components as gc

"""
Process Manager using Python and Gradio framework
This application allows users to manage system processes,
including listing and killing processes.
"""

class ProcessManager:
    def __init__(self):
        # Initialize the process manager
        pass

    def list_processes(self):
        try:
            # Get a list of all running processes
            processes = [p.info for p in psutil.process_iter(['pid', 'name', 'status', 'create_time'])]
            return processes
        except Exception as e:
            # Handle any exception that occurs while listing processes
            return f"Error: {str(e)}"

    def kill_process(self, pid):
        try:
            # Kill a process by its PID
            process = psutil.Process(pid)
            process.terminate()
            return f"Process {pid} terminated successfully"
        except Exception as e:
            # Handle any exception that occurs while killing a process
            return f"Error: {str(e)}"

# Create a Gradio interface for the process manager
def run_process_manager():
    process_manager = ProcessManager()

    # Text box to display the list of processes
    process_list = gc.Textbox(label="List of Processes")

    # Text box to display the result of killing a process
    kill_result = gc.Textbox(label="Kill Process Result")

    # Button to list all processes
    list_button = gc.Button(value="List Processes")
    def on_list_click():
        process_list_text = str(process_manager.list_processes())
        process_list.update(process_list_text)

    # Button to kill a process
    kill_button = gc.Button(value="Kill Process")
    process_id = gc.Textbox(label="Enter Process ID")
    def on_kill_click():
        try:
            pid = int(process_id.value)
            result = process_manager.kill_process(pid)
            kill_result.update(result)
        except ValueError:
            kill_result.update("Invalid process ID. Please enter a valid integer.")
        except Exception as e:
            kill_result.update(f"Error: {str(e)}")

    # Create a Gradio interface with the buttons and text boxes
    iface = Interface(
        fn=on_list_click,
        inputs=list_button,
        outputs=process_list,
        title="Process Manager - List Processes",
    )
    iface2 = Interface(
        fn=on_kill_click,
        inputs=[process_id, kill_button],
        outputs=kill_result,
        title="Process Manager - Kill Process",
    )

    return iface, iface2

# Run the Gradio interface
if __name__ == '__main__':
    run_process_manager()