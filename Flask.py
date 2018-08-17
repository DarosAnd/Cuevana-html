from flask import Flask, render_template
app = Flask(__name__, static_url_path="/static")

@app.route("/Inicio")
def hello():
    return render_template("Home.html")

@app.route("/Registro")
def registrar():
    return render_template("REGISTRAR.html")

if __name__ == "__main__":
    app.run(debug=True)