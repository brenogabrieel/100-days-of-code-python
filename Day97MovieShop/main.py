from cs50 import SQL
from flask_session import Session
from flask import Flask, render_template, redirect, request, session
from datetime import datetime

app = Flask(__name__)

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///data.db")



@app.route("/")
def index():
    try:
        movies = db.execute("SELECT * FROM movies ORDER BY name ASC")
    except RuntimeError:
        movies = db.execute("SELECT * FROM movies")

    moviesLen = len(movies)
    shoppingCart = []
    shopLen = 0
    totItems, total, display = 0, 0, 0

    if 'user' in session:
        shoppingCart = db.execute(
            "SELECT name, image, SUM(qty) as qty, SUM(subTotal) as subTotal, price, id FROM cart GROUP BY name"
        )
        shopLen = len(shoppingCart)
        for item in shoppingCart:
            total += item.get("subTotal", 0)
            totItems += item.get("qty", 0)

    return render_template("index.html", shoppingCart=shoppingCart, movies=movies, shopLen=shopLen, moviesLen=moviesLen,
                           total=total, totItems=totItems, display=display, session=session)



@app.route("/buy/")
def buy():
    qty = request.args.get('quantity')
    if qty is None or not qty.isdigit():
        return redirect("/")

    qty = int(qty)

    if 'user' in session:
        id = request.args.get('id')
        if id is None or not id.isdigit():
            return redirect("/")

        id = int(id)
        goods = db.execute("SELECT * FROM movies WHERE id = :id", id=id)

        if not goods:
            return redirect("/")

        price = goods[0]["onSalePrice"] if goods[0]["onSale"] == 1 else goods[0]["price"]
        name = goods[0]["name"]
        image = goods[0]["image"]
        subTotal = qty * price

        db.execute(
            "INSERT OR REPLACE INTO cart (id, qty, name, image, price, subTotal) VALUES (:id, :qty, :name, :image, :price, :subTotal)",
            id=id, qty=qty, name=name, image=image, price=price, subTotal=subTotal
        )

        shoppingCart = db.execute(
            "SELECT name, image, SUM(qty) as qty, SUM(subTotal) as subTotal, price, id FROM cart GROUP BY name"
        )
        shopLen = len(shoppingCart)
        totItems, total, display = 0, 0, 0

        for item in shoppingCart:
            total += item.get("subTotal", 0)
            totItems += item.get("qty", 0)

        try:
            movies = db.execute("SELECT * FROM movies ORDER BY name ASC")
        except RuntimeError:
            movies = db.execute("SELECT * FROM movies")

        moviesLen = len(movies)

        return render_template("index.html", shoppingCart=shoppingCart, movies=movies, shopLen=shopLen,
                               moviesLen=moviesLen, total=total, totItems=totItems, display=display, session=session)

    return redirect("/")


@app.route("/update/")
def update():
    qty = request.args.get('quantity')
    if qty is None or not qty.isdigit():
        return redirect("/")

    qty = int(qty)

    if 'user' in session:
        id = request.args.get('id')
        if id is None or not id.isdigit():
            return redirect("/")

        id = int(id)
        db.execute("DELETE FROM cart WHERE id = :id", id=id)
        goods = db.execute("SELECT * FROM movies WHERE id = :id", id=id)

        if not goods:
            return redirect("/")

        price = goods[0]["onSalePrice"] if goods[0]["onSale"] == 1 else goods[0]["price"]
        name = goods[0]["name"]
        image = goods[0]["image"]
        subTotal = qty * price

        db.execute(
            "INSERT INTO cart (id, qty, name, image, price, subTotal) VALUES (:id, :qty, :name, :image, :price, :subTotal)",
            id=id, qty=qty, name=name, image=image, price=price, subTotal=subTotal
        )

        shoppingCart = db.execute(
            "SELECT name, image, SUM(qty) as qty, SUM(subTotal) as subTotal, price, id FROM cart GROUP BY name"
        )
        shopLen = len(shoppingCart)
        totItems, total, display = 0, 0, 0

        for item in shoppingCart:
            total += item.get("subTotal", 0)
            totItems += item.get("qty", 0)

        return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                               display=display, session=session)

    return redirect("/")


@app.route("/checkout/")
def checkout():
    if 'user' in session:
        order = db.execute("SELECT * from cart")

        for item in order:
            db.execute(
                "INSERT INTO purchases (uid, id, name, image, quantity) VALUES(:uid, :id, :name, :image, :quantity)",
                uid=session["uid"], id=item["id"], name=item["name"], image=item["image"], quantity=item["qty"]
            )

        db.execute("DELETE from cart")

    return redirect("/")


@app.route("/remove/", methods=["GET"])
def remove():
    out = request.args.get("id")

    if out is None or not out.isdigit():
        return redirect("/cart/")

    out = int(out)
    db.execute("DELETE from cart WHERE id=:id", id=out)
    totItems, total, display = 0, 0, 0

    shoppingCart = db.execute(
        "SELECT name, image, SUM(qty) as qty, SUM(subTotal) as subTotal, price, id FROM cart GROUP BY name"
    )
    shopLen = len(shoppingCart)

    for item in shoppingCart:
        total += item.get("subTotal", 0)
        totItems += item.get("qty", 0)

    display = 1

    return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                           display=display, session=session)


@app.route("/login/", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/new/", methods=["GET"])
def new():
    return render_template("new.html")


@app.route("/logged/", methods=["POST"])
def logged():
    user = request.form["username"].lower()
    pwd = request.form["password"]

    if user == "" or pwd == "":
        return render_template("login.html")

    query = "SELECT * FROM users WHERE username = :user AND password = :pwd"
    rows = db.execute(query, user=user, pwd=pwd)

    if len(rows) == 1:
        session['user'] = user
        session['time'] = datetime.now()
        session['uid'] = rows[0]["id"]
        return redirect("/")

    return render_template("login.html", msg="Wrong username or password.")


@app.route("/history/")
def history():
    shoppingCart = []
    shopLen = len(shoppingCart)
    totItems, total, display = 0, 0, 0

    if 'user' in session:
        mymovies = db.execute("SELECT * FROM purchases WHERE uid=:uid", uid=session["uid"])
        mymoviesLen = len(mymovies)

        return render_template("history.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total,
                               totItems=totItems, display=display, session=session, mymovies=mymovies,
                               mymoviesLen=mymoviesLen)

    return redirect("/login/")


@app.route("/logout/")
def logout():
    if 'user' in session:
        db.execute("DELETE from cart")
        session.clear()

    return redirect("/")


@app.route("/register/", methods=["POST"])
def registration():
    username = request.form["username"]
    password = request.form["password"]
    confirm = request.form["confirm"]
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]

    if password != confirm:
        return render_template("new.html", msg="Passwords do not match!")

    rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

    if len(rows) > 0:
        return render_template("new.html", msg="Username already exists!")

    db.execute(
        "INSERT INTO users (username, password, fname, lname, email) VALUES (:username, :password, :fname, :lname, :email)",
        username=username, password=password, fname=fname, lname=lname, email=email
    )

    return render_template("login.html")


@app.route("/cart/")
def cart():
    if 'user' in session:
        totItems, total, display = 0, 0, 0
        shoppingCart = db.execute(
            "SELECT name, image, SUM(qty) as qty, SUM(subTotal) as subTotal, price, id FROM cart GROUP BY name"
        )
        shopLen = len(shoppingCart)

        for item in shoppingCart:
            total += item.get("subTotal", 0)
            totItems += item.get("qty", 0)

        return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                               display=display, session=session)

    return redirect("/login/")


if __name__ == "__main__":
    app.run(debug=True)
