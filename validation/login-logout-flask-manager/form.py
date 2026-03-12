from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    mobile = StringField(
        "Mobile",
        validators=[
            DataRequired(message="Mobile number is required"),
            Length(min=10, max=15),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Please enter a valid email address"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(message="Password is required"), Length(min=6)],
    )
    submit = SubmitField("Register")
