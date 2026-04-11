from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import json
from datetime import datetime
from products import products

app = Flask(__name__)
app.secret_key = "parfum-secret"
ORDER_DIR = "data/orders"

os.makedirs(ORDER_DIR, exist_ok=True)

def get_product_by_id(pid):
    return next((p for p in products if str(p["id"]) == str(pid)), None)

@app.route("/")
def index():
    cart = session.get("cart", {})
    return render_template("index.html", products=products, cart_count=sum(cart.values()))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    cart_items = []
    total_price = 0

    for pid, qty in cart.items():
        prod = get_product_by_id(pid)
        if prod:
            total = prod["price"] * qty
            total_price += total
            cart_items.append({
                "id": pid,
                "name": prod["name"],
                "price": prod["price"],
                "quantity": qty,
                "total": total
            })

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total_price=total_price,
        cart_count=sum(cart.values()),
        products=products
    )

@app.route("/cart/add-item")
def add_to_cart():
    pid = request.args.get("id")
    if not pid or not get_product_by_id(pid):
        return redirect(url_for("index"))
    cart = session.get("cart", {})
    cart[pid] = cart.get(pid, 0) + 1
    session["cart"] = cart
    return redirect(url_for("index"))

@app.route("/cart/remove-item")
def remove_from_cart():
    pid = request.args.get("id")
    cart = session.get("cart", {})
    if pid in cart:
        del cart[pid]
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", {})
    if not cart:
        flash("Coșul este gol.")
        return redirect(url_for("index"))

    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        payment_method = request.form.get("payment_method")

        order = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "address": address,
            "payment_method": payment_method,
            "items": [],
            "total": 0
        }

        for pid, qty in cart.items():
            prod = get_product_by_id(pid)
            if prod:
                total = prod["price"] * qty
                order["items"].append({
                    "id": pid,
                    "name": prod["name"],
                    "price": prod["price"],
                    "quantity": qty,
                    "total": total
                })
                order["total"] += total

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{ORDER_DIR}/order-{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(order, f, indent=4)

        print(f"[COMANDA NOUĂ] => {order}")

        session.pop("cart", None)
        flash("Comanda a fost trimisă cu succes!")
        return redirect(url_for("index"))

    cart_items = []
    total_price = 0
    for pid, qty in cart.items():
        prod = get_product_by_id(pid)
        if prod:
            total = prod["price"] * qty
            total_price += total
            cart_items.append({
                "id": pid,
                "name": prod["name"],
                "price": prod["price"],
                "quantity": qty, 
                "total": total
            })

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total_price=total_price,
        cart_count=sum(cart.values()),
        products=products
    )

@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        cart_count=sum(session.get("cart", {}).values()),
        products=products
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)