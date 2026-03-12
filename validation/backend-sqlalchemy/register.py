from flask import Flask, redirect, render_template, request, session, url_for
from form import RegisterForm
from model.user import db, User


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"

# app.config["SQLALCHEMY_DATABASE_URI"] = (
#     "postgresql://postgres:Nopassword%4003@localhost/test"
# )
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database tables created.")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        mobile = form.mobile.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, mobile=mobile, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return render_template(
            "login.html", message="Registration successful! Please login!"
        )

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password_user = request.form["password"]
        user = User.query.filter_by(username=username).first()

        # password_from_db = user.password
        # if password_from_db == password_user:
        #     return "login successful"

        if user and user.check_password(password_user):
            session["user_id"] = user.id
            return redirect(url_for("dashboard_1"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard_1():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", user=user.username)
    # return render_template("dashboard.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
