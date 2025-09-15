# 代码生成时间: 2025-09-15 10:26:54
import gradio as gr
def add_item(item_name, quantity):
    # Check if item already exists
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    return inventory


def remove_item(item_name, quantity):
    # Check if item exists and has enough quantity
    if item_name in inventory and inventory[item_name] >= quantity:
        inventory[item_name] -= quantity
        if inventory[item_name] == 0:
            del inventory[item_name]
    else:
        raise ValueError("Item does not exist or insufficient quantity")
    return inventory


def get_inventory():
    return inventory

# Initialize inventory as an empty dictionary
inventory = {}

# Gradio interface
iface = gr.Interface(
    fn=get_inventory,
    inputs=[],
    outputs="json",
    title="Inventory Management System",
    description="Manage your inventory with this simple system",
)

iface.add_component(
    gr.Textbox(label="Item Name"),
    type="input",
    param="item_name",
)

iface.add_component(
    gr.Slider(minimum=0, maximum=100, label="Quantity"),
    type="input",
    param="quantity",
)

iface.add_component(
    gr.Button(label="Add Item"),
    type="input",
    elem_id="add_item",
)

iface.add_component(
    gr.Button(label="Remove Item"),
    type="input",
    elem_id="remove_item",
)

iface.add_component(
    gr.JSON(label="Inventory"),
    type="output",
    elem_id="inventory_output",
)

iface.add_route(
    fn=add_item,
    inputs=["item_name", "quantity", "add_item"],
    outputs="inventory_output",
)

iface.add_route(
    fn=remove_item,
    inputs=["item_name", "quantity", "remove_item"],
    outputs="inventory_output",
)

if __name__ == "__main__":
    iface.launch()