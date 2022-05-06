from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from .user import User

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Username"})
    email = StringField(validators=[InputRequired(), Length(max=30)],
        render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one."
            )


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


class ChatForm(FlaskForm):
    message = StringField(validators=[InputRequired()],
        render_kw={"placeholder": "Message..."})
    # TODO, change "Send" to a "greater than" symbol
    submit = SubmitField("Send")

    # TODO, might want to check the function below later!
    def validate_message(self, message):
        if message.data == "":
            raise ValidationError(
                "Message is empty! Please enter a message."
            )

    # https://www.geeksforgeeks.org/flask-form-submission-without-page-reload/
