# 代码生成时间: 2025-08-27 05:24:52
import gradio as gr
def bubble_sort(arr):
    """
    Bubble sort algorithm implementation.
# 增强安全性
    It repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
    
    Args:
    arr (list): The list of numbers to be sorted.
    
    Returns:
    list: The sorted list of numbers.
# NOTE: 重要实现细节
    """
# 优化算法效率
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def quick_sort(arr):
    """
    Quick sort algorithm implementation.
    It selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    
    Args:
# NOTE: 重要实现细节
    arr (list): The list of numbers to be sorted.
# TODO: 优化性能
    
    Returns:
    list: The sorted list of numbers.
    """
# NOTE: 重要实现细节
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
# TODO: 优化性能
        return quick_sort(less) + [pivot] + quick_sort(greater)
def merge_sort(arr):
    """
# 扩展功能模块
    Merge sort algorithm implementation.
    It divides the list into halves, calls itself for the two halves, and then merges the sorted halves.
    
    Args:
    arr (list): The list of numbers to be sorted.
# TODO: 优化性能
    
    Returns:
    list: The sorted list of numbers.
# 扩展功能模块
    """
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
# 扩展功能模块
        left = merge_sort(arr[:mid])
# 扩展功能模块
        right = merge_sort(arr[mid:])
        return merge(left, right)
# 改进用户体验
def merge(left, right):
    """
    Merge function for merge sort.
# 增强安全性
    It takes two sorted arrays and merges them into a single sorted array.
    
    Args:
    left (list): The first sorted array.
    right (list): The second sorted array.
# 改进用户体验
    
    Returns:
    list: The merged sorted array.
    """
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
# 优化算法效率
        else:
            result.append(right.pop(0))
    result.extend(left or right)
# 优化算法效率
    return result
def main(arr, algorithm):
    """
    Main function to select and apply the sorting algorithm.
    
    Args:
    arr (list): The list of numbers to be sorted.
# 添加错误处理
    algorithm (str): The name of the sorting algorithm to apply.
    
    Returns:
    list: The sorted list of numbers.
    """
    if not arr:
        return []
    elif algorithm == 'bubble_sort':
        return bubble_sort(arr)
    elif algorithm == 'quick_sort':
        return quick_sort(arr)
    elif algorithm == 'merge_sort':
        return merge_sort(arr)
# FIXME: 处理边界情况
    else:
        raise ValueError('Invalid algorithm selected')

def run():
    """
    Function to define the Gradio interface.
    """
# 改进用户体验
    demo = gr.Interface(
        fn=main,
        inputs=[gr.inputs.List(), gr.inputs.Dropdown(['bubble_sort', 'quick_sort', 'merge_sort'])],
# NOTE: 重要实现细节
        outputs=gr.outputs.List(),
        title='Sorting Algorithm App',
        description='Select a sorting algorithm to sort the list of numbers.'
    )
    demo.launch()
if __name__ == '__main__':
    run()