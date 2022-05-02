#'''WSGI entry'''
# allows gunicorn to run
import flask_app
handler = flask_app.create_app()


if __name__ == '__main__':
    # Entry point when run via Python interpreter.
    # print("== Running in debug mode ==")
    flask_app.create_app().run(debug=True)
