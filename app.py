from flask import Flask, render_template, request
import scrap

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/preview", methods=['POST', 'GET'])
def preview():
    obj = request.form.to_dict()
    url = obj["url"]

    result = scrap.scrap_web(url)

    return render_template("preview.html", result=result)


if __name__ == '__main__':
    app.run()
