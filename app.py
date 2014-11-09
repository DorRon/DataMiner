from flask import Flask, redirect, render_template, request, make_response, abort

app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == "__main__":
    app.debug=True
    app.run()