# 代码生成时间: 2025-08-25 11:20:26
import gradio as gr

# 购物车类
class ShoppingCart:
    def __init__(self):
        # 初始化购物车为空字典
        self.items = {}

    # 添加商品到购物车
    def add_item(self, item_name, quantity):
        # 检查商品是否存在于购物车中
        if item_name in self.items:
            self.items[item_name] += quantity  # 如果存在，增加数量
        else:
            self.items[item_name] = quantity  # 如果不存在，添加商品和数量

    # 从购物车删除商品
    def remove_item(self, item_name):
        # 检查商品是否存在于购物车中
        if item_name in self.items:
            del self.items[item_name]  # 如果存在，删除商品
        else:
            raise ValueError("Item not found in the shopping cart.")  # 如果不存在，抛出异常

    # 显示购物车内容
    def display_cart(self):
        return self.items

# 购物车实例
cart = ShoppingCart()

# Gradio接口函数
def add_to_cart(item_name, quantity):
    """添加商品到购物车

    参数:
    item_name (str): 商品名称
    quantity (int): 商品数量
    """
    cart.add_item(item_name, quantity)
    return cart.display_cart()

def remove_from_cart(item_name):
    """从购物车删除商品

    参数:
    item_name (str): 商品名称
    """
    try:
        cart.remove_item(item_name)
        return cart.display_cart()
    except ValueError as e:
        return str(e)

# Gradio接口设置
iface = gr.Interface(
    fn=add_to_cart, 
    inputs=["text", "number"],
    outputs="json",
    examples=[["apple", 3], ["banana", 2]],
    live=True,
    title="Shopping Cart Application"
)
iface.remove_from_cart = gr.Interface(
    fn=remove_from_cart, 
    inputs="text",
    outputs="json",
    examples=["apple"],
    live=True
)

# 运行Gradio应用
iface.launch()