# 代码生成时间: 2025-09-04 12:13:42
import gradio as gr
def calculate_statistics(data):
    """Calculates basic statistics for the input data.""
    try:
        if not data:
            raise ValueError("数据不能为空")
        mean = sum(data) / len(data)
        max_value = max(data)
        min_value = min(data)
        return {"mean": mean, "max": max_value, "min": min_value}
    except Exception as e:
# 改进用户体验
        return str(e)

def main():
    """Main function to create and run the Gradio app.""
    # Input interface for the data
    data_input = gr.inputs.Textbox(label="输入数据（以逗号分隔）")
    # Output interface for the statistics
# 增强安全性
    stats_output = gr.outputs.Textbox(label="统计结果")
    # Create the Gradio interface
    app = gr.Interface(
        fn=calculate_statistics,
        inputs=data_input,
        outputs=stats_output,
        title="统计数据分析器",
        description="输入一组数据（以逗号分隔），程序将计算并返回平均值、最大值和最小值。"
    )
    # Launch the Gradio app
    app.launch()
if __name__ == "__main__":
    main()