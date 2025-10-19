import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pizza Order Form")
root.geometry("600x700") 

tk.Label(root, text="Pizza Order Form", font=("Arial", 20, "bold")).pack(pady=50, anchor="center") 
tk.Label(root, text="Select Pizza Size:", font=("Arial", 18, "bold")).pack(anchor="w", padx=40, pady=10) 

# Variables to store selections
size_small = tk.IntVar()
size_medium = tk.IntVar()
size_large = tk.IntVar()

tk.Checkbutton(root, text="Small", anchor="w", font=("Arial", 14), variable=size_small).pack(fill="x", padx=40, pady=5) 
tk.Checkbutton(root, text="Medium", anchor="w", font=("Arial", 14), variable=size_medium).pack(fill="x", padx=40, pady=5) 
tk.Checkbutton(root, text="Large", anchor="w", font=("Arial", 14), variable=size_large).pack(fill="x", padx=40, pady=5) 

tk.Label(root, text="Select Toppings:", font=("Arial", 18, "bold")).pack(anchor="w", padx=40, pady=10) 

# Variables for toppings
topping_cheese = tk.IntVar()
topping_pepperoni = tk.IntVar()
topping_mushrooms = tk.IntVar()

tk.Checkbutton(root, text="Cheese", anchor="w", font=("Arial", 14), variable=topping_cheese).pack(fill="x", padx=40, pady=5) 
tk.Checkbutton(root, text="Pepperoni", anchor="w", font=("Arial", 14), variable=topping_pepperoni).pack(fill="x", padx=40, pady=5) 
tk.Checkbutton(root, text="Mushrooms", anchor="w", font=("Arial", 14), variable=topping_mushrooms).pack(fill="x", padx=40, pady=5) 

# Function to handle the order
def place_order():
    sizes = []
    toppings = []

    if size_small.get():
        sizes.append("Small")
    if size_medium.get():
        sizes.append("Medium")
    if size_large.get():
        sizes.append("Large")

    if topping_cheese.get():
        toppings.append("Cheese")
    if topping_pepperoni.get():
        toppings.append("Pepperoni")
    if topping_mushrooms.get():
        toppings.append("Mushrooms")

    if not sizes and not toppings:
        messagebox.showinfo("Order", "No items selected!")
        return

    order_summary = "Pizza Size: " + ", ".join(sizes) + "\nToppings: " + ", ".join(toppings)
    messagebox.showinfo("Order Placed", order_summary)

tk.Button(root, text="Place Order", bg="green", fg="white", font=("Arial", 16, "bold"), command=place_order).pack(pady=30, anchor="center") 
root.mainloop()