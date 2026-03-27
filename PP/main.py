from tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700")
        self.root.title("QulaMart")
        self.root.config(bg="#f0f0f0")

        self.cart = []  
        self.total_price = 0  

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        self.login_frame = Frame(self.root, bg="#EDDED7", width=1350, height=700)
        self.login_frame.pack()

        Label(
            self.login_frame, text="Sign in", font=("Arial", 30), bg="#EDDED7", fg="#261206"
        ).place(x=700, y=20)

        self.username_entry = Entry(
            self.login_frame, width=34, font=("Arial", 15), border=0, bg="#EDDED7", fg="#261206"
        )
        self.username_entry.place(x=700, y=120)
        self.username_entry.insert(0, "Username")

        self.password_entry = Entry(
            self.login_frame, width=34, font=("Arial", 15), border=0, bg="#EDDED7", fg="#261206"
        )
        self.password_entry.place(x=700, y=170)
        self.password_entry.insert(0, "Password")

        Button(
            self.login_frame,
            text="Login",
            font=("Arial", 15),
            bg="green",
            fg="white",
            command=self.open_menu_screen,
        ).place(x=700, y=300, width=100)


        Button(
            self.login_frame,
            text="cat",
            font=("Arial", 15),
            bg="green",
            fg="white",
            command=self.open_cat,
        ).place(x=700, y=500, width=100)


    def open_cat(self):
        self.clear_screen()
        self.login_frame = Frame(self.root, bg="#EDDED7", width=1350, height=700)
        self.login_frame.pack()
        img = Image.open("image/cat.png")
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
    
        
        

    def open_menu_screen(self):
        self.clear_screen()

        self.menu_frame = Frame(self.root, bg="#f0f0f0", width=1350, height=700)
        self.menu_frame.pack(fill="both", expand=True)
        

        Label(
            self.menu_frame,
            text="QulaMart",
            font=("times new roman", 40, "bold"),
            compound=LEFT,
            bg="green",
            fg="#063970",
            padx=20,
            anchor="w"
        ).place(x=0, y=0, relwidth=1, height=70)

        Button(
            self.menu_frame,
            text="Logout",
            font=("times new roman", 15, "bold"),
            bg="green",
            cursor="hand2",
            command=self.create_login_screen,
        ).place(x=1100, y=10, width=150, height=30)


        Button(
            self.menu_frame,
            text="Electronics",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=lambda: self.open_category_screen("Electronics", [
                {"name": "TV", "price": 1000, "image": "image/tv.png"},
                {"name": "laptop", "price": 750, "image": "image/lap.png"},
                {"name": "Iphone", "price": 740, "image": "image/iphone.png"},
                {"name": "vacuum cleaners", "price": 200, "image": "image/OIP.png"},
                {"name": "air fryer", "price": 75, "image": "image/air.png"},
                {"name": "Laptop", "price": 1500, "image": "image/lap.png"}
        
            ]),
        ).place(x=10, y=70, width=200, height=50)


        Button(
            self.menu_frame,
            text="Frozen food",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=lambda: self.open_category_screen("Frozen food", [
                {"name": "molo", "price": 2.49, "image": "image/molo.png"},
                {"name": "Beans", "price": 1.99, "image": "image/bean.png"},
                {"name": "Chiken", "price": 3.99, "image": "image/ch.png"},
                {"name": "Meat ", "price": 10.99, "image": "image/me.png"},
                {"name": "okra", "price": 1.99, "image": "image/okra.png"},
                {"name": "Chiken Burger", "price": 4.99, "image": "image/ch.png"},
                {"name": "Meat Burger", "price": 5.99, "image": "image/bb.png"},
                {"name": "Fish", "price": 8.99, "image": "image/fish.png"},
                {"name": "potato", "price": 3.00, "image": "image/pot.png"}
        
            ]),
        ).place(x=10, y=120, width=200, height=50)


        Button(
            self.menu_frame,
            text="Fruit",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=lambda: self.open_category_screen("Fruit ", [
                {"name": "Grapes", "price": 0.99, "image": "image/grap.png"},
                {"name": "appel", "price": 0.99, "image": "image/app.png"},
                {"name": "Green appel", "price": 3.99, "image": "image/greenap.png"},
                {"name": "Berries", "price": 10.99, "image": "image/ber.png"},
                {"name": "Mango", "price": 1.99, "image": "image/man.png"},
                {"name": "Banana", "price": 2.99, "image": "image/ban.png"},
                {"name": "Orange", "price": 2.99, "image": "image/or.png"},
                {"name": "Cherry", "price": 1.49, "image": "image/che.png"},
                {"name": "Pineapple", "price": 3.99, "image": "image/pin.png"},
                {"name": "Strawberry", "price": 2.49, "image": "image/str.png"},
                {"name": "Avocado", "price": 3.00, "image": "image/avo.png"}
        
            ]),
        ).place(x=10, y=170, width=200, height=50)

        Button(
            self.menu_frame,
            text="Vegetable",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=lambda: self.open_category_screen("Vegetable", [
                {"name": "Tomato ", "price": 0.49, "image": "image/to.png"},
                {"name": "Corn", "price": 1.99, "image": "image/corn.png"},
                {"name": "Green Bell Pepper", "price": 1.99, "image": "image/greenpep.png"},
                {"name": "Bell Pepper ", "price": 3.99, "image": "image/BBP.png"},
                {"name": "Chili Peppers", "price": 1.99, "image": "image/cp.png"},
                {"name": "Potato", "price": 2.99, "image": "image/pota.png"},
                {"name": "Onion", "price": 0.99, "image": "image/on.png"},
                {"name": "Cucumber", "price": 0.49, "image": "image/cu.png"}
            ]),
        ).place(x=10, y=220, width=200, height=50)

        Button(
            self.menu_frame,
            text="Canned Food",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=lambda: self.open_category_screen("Canned Food", [
                {"name": "SweetCorn", "price": 1.49, "image": "image/sc.png"},
                {"name": "Canned Beans", "price": 0.75, "image": "image/BBS.png"},
                {"name": "Hummus", "price": 0.75, "image": "image/hum.png"},
                {"name": "Hummus ", "price": 0.75, "image": "image/humm.png"},
                {"name": "Tuna Can", "price": 0.5, "image": "image/tun.png"},
                {"name": "Red beans", "price": 0.75, "image": "image/lls.png"},
                {"name": "Onion", "price": 0.99, "image": "image/on.png"},
                {"name": "Olive", "price": 0.49, "image": "image/ol.png"}
            ]),
        ).place(x=10, y=270, width=200, height=50)


        Button(
            self.menu_frame,
            text="Bakery",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=lambda: self.open_category_screen("B", [
                {"name": "Frence Brad", "price": 1.00, "image": "image/fb.png"},
                {"name": "Arabic Bread white", "price": 0.5, "image": "image/ab.png"},
                {"name": "Arabic Bread black", "price": 0.5, "image": "image/abb.png"},
                {"name": "toast bread ", "price": 0.75, "image": "image/tb.png"},
                {"name": "cupcakes", "price": 0.5, "image": "image/cc.png"},
                {"name": "Cookies", "price": 0.35, "image": "image/acc.png"},
                {"name": "pizza", "price": 3.00, "image": "image/pi.png"},
                {"name": "Croissant", "price": 0.49, "image": "image/ccb.png"}
            ]),
        ).place(x=10, y=320, width=200, height=50)


        Button(
            self.menu_frame,
            text="Cart",
            font=("Arial", 20),
            bg="#ffffff",
            fg="#000000",
            command=self.open_cart_screen,
        ).place(x=10, y=370, width=200, height=50)

    def open_category_screen(self, category, items):
        self.clear_screen()

        frame = Frame(self.root, bg="#f0f0f0", width=1250, height=700)
        frame.pack(fill="both", expand=True)

        Label(
            frame,
            text=f"{category} - Subcategories",
            font=("Arial", 30, "bold"),
            bg="green",
            fg="white",
        ).pack(side=TOP, fill=X)

        Button(
            frame,
            text="Back to Menu",
            font=("Arial", 15),
            bg="green",
            fg="white",
            command=self.open_menu_screen,
        ).place(x=20, y=20, width=150, height=40)

        for i, item in enumerate(items):
            self.create_box(
                parent=frame,
                x=(i % 4) * 300 + 50,
                y=(i // 4) * 250 + 100,
                width=250,
                height=200,
                image_path=item["image"],
                label_text=item["name"],
                button_text="View Item",
                command=lambda item=item: self.open_item_viewer(item),
            )

    def create_box(self, parent, x, y, width, height, image_path, label_text, button_text, command):
        frame = Frame(parent, bd=2, relief=RIDGE, bg="white")
        frame.place(x=x, y=y, width=width, height=height)       
        img = Image.open(image_path).resize((240, 140), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lbl = Label(frame, image=img, bg="white")
        lbl.image = img
        lbl.pack(side=TOP, fill=BOTH, expand=True)
      

        Button(
            frame,
            text=button_text,
            font=("Arial", 12),
            bg="green",
            fg="white",
            command=command,
        ).pack(side=BOTTOM, fill=X)

    def open_item_viewer(self, item):
        self.clear_screen()

        frame = Frame(self.root, bg="#f0f0f0", width=1250, height=700)
        frame.pack(fill="both", expand=True)

        Label(
            frame,
            text=f"{item['name']} - ${item['price']}",
            font=("Arial", 30, "bold"),
            bg="green",
            fg="white",
        ).pack(side=TOP, fill=X)

        counter = IntVar(value=0)

        def increment_counter():
            counter.set(counter.get() + 1)

        def decrement_counter():
            if counter.get() > 0:
                counter.set(counter.get() - 1)

        Button(frame, text="-", font=("Arial", 20), command=decrement_counter).pack(side=LEFT, padx=10)
        Label(frame, textvariable=counter, font=("Arial", 20)).pack(side=LEFT)
        Button(frame, text="+", font=("Arial", 20), command=increment_counter).pack(side=LEFT, padx=10)

        Button(
            frame,
            text="Add to Cart",
            font=("Arial", 15),
            bg="green",
            fg="white",
            command=lambda: self.add_to_cart(item, counter.get()),
        ).pack(side=TOP, pady=20)

        Button(
            frame,
            text="Back to Categories",
            font=("Arial", 15),
            bg="green",
            fg="white",
            command=self.open_menu_screen,
        ).pack(side=TOP, pady=20)

    def add_to_cart(self, item, quantity):
        """Adds an item to the cart."""
        if quantity > 0:
            self.cart.append({"name": item["name"], "quantity": quantity, "price": item["price"] * quantity})
            self.total_price += item["price"] * quantity

    def open_cart_screen(self):
        self.clear_screen()

        frame = Frame(self.root, bg="#f0f0f0", width=1250, height=700)
        frame.pack(fill="both", expand=True)

        Label(
            frame,
            text="Cart - Summary",
            font=("Arial", 30, "bold"),
            bg="green",
            fg="white",
        ).pack(side=TOP, fill=X)

        if not self.cart:
            Label(
                frame,
                text="Your cart is empty.",
                font=("Arial", 15),
                bg="#f0f0f0",
                fg="black",
            ).pack(side=TOP, pady=10)
        else:
            for item in self.cart:
                Label(
                    frame,
                    text=f"{item['name']} x{item['quantity']} = ${item['price']}",
                    font=("Arial", 15),
                    bg="#f0f0f0",
                    fg="black",
                ).pack(anchor="w", padx=20, pady=10)

            Label(
                frame,
                text=f"Total Price: ${self.total_price}",
                font=("Arial", 20, "bold"),
                bg="#f0f0f0",
                fg="black",
            ).pack(side=BOTTOM, pady=20)

     

        Button(
            frame,
            text="Back to Menu",
            font=("Arial", 15),
            bg="green",
            fg="white",
            command=self.open_menu_screen,
        ).pack(side=TOP, pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
