# 代码生成时间: 2025-09-22 15:06:47
import gradio as gr
def add_item_to_cart(item, quantity):
    # 确保添加的物品和数量有效
    if item not in cart.get(item, 0):
        cart[item] = quantity
    else:
        cart[item] += quantity
    return cart

def remove_item_from_cart(item):
    # 确保移除的物品在购物车中
    if item in cart:
        del cart[item]
    else:
        raise ValueError(f"Item '{item}' not found in the cart.")
    return cart

def update_item_quantity(item, quantity):
    # 确保更新的物品在购物车中，并且数量有效
    if item in cart:
        if quantity <= 0:
            del cart[item]
        else:
            cart[item] = quantity
    else:
        raise ValueError(f"Item '{item}' not found in the cart.")
    return cart

def clear_cart():
    # 清空购物车
    cart.clear()
    return cart

def get_cart_contents():
    # 返回购物车中所有物品及其数量
    return cart

# 初始化购物车
cart = {}

# Gradio接口定义
iface = gr.Interface(
    fn=get_cart_contents,
    inputs=[],
    outputs="text",
    examples=[],
    title="Shopping Cart App",
    description="A simple shopping cart application."
)

iface.add_component(
    name="Add item", 
    description="Add an item to the cart", 
    fn=add_item_to_cart, 
    inputs=[gr.Textbox("Item"), gr.Slider(0, 100, default=1, label="Quantity")], 
    outputs="text"
)
iface.add_component(
    name="Remove item", 
    description="Remove an item from the cart", \ 
    fn=remove_item_from_cart, \ 
    inputs=gr.Textbox("Item"), \ 
    outputs="text"
)
iface.add_component(
    name="Update item quantity", \ 
    description="Update the quantity of an item in the cart", \ 
    fn=update_item_quantity, \ 
    inputs=[gr.Textbox("Item"), gr.Slider(0, 100, default=1, label="Quantity")], \ 
    outputs="text"
)
iface.add_component(
    name="Clear cart", \ 
    description="Clear the entire cart", \ 
    fn=clear_cart, \ 
    inputs=[], \ 
    outputs="text"
)

# 启动Gradio界面
iface.launch()