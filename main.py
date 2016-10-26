from flask import Flask, render_template, request, jsonify, make_response
app = Flask(__name__)


@app.route("/")
def hello():
    # return render_template('chat.html')
    return make_response(render_template('chat.html'),200)


if __name__ == "__main__":
    app.run(debug=True)