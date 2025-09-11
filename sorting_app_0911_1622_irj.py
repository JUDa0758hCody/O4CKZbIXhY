# 代码生成时间: 2025-09-11 16:22:47
import gradio as gr
def merge_sort(arr):
# TODO: 优化性能
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
# 优化算法效率
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
# 改进用户体验
                j += 1
            k += 1
# 增强安全性
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
# TODO: 优化性能
            k += 1
    return arr
def get_sorted_list(input_list):
    """Sorts the list using merge sort algorithm.
    
    Args:
        input_list (list): A list of integers to be sorted.
# 添加错误处理
    
    Returns:
        list: A sorted list of integers.
    """
# 增强安全性
    if not input_list:
        return []
    try:
        sorted_list = merge_sort(input_list)
# 扩展功能模块
        return sorted_list
    except Exception as e:
        return str(e)
iface = gr.Interface(
    fn=get_sorted_list, 
    inputs=gr.Textbox(label="Enter numbers separated by space"), 
    outputs="text")
iface.launch()