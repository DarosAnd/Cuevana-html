from usuario import Usuario
from BD import DB
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static")

@app.route("/Inicio")
def inicio():
    return render_template("Home.html")

@app.route("/Registro")
def registrar():
    return render_template("Registrar.html")

@app.route("/Registro", methods = ['GET', 'POST'])
def tomarDatos():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("inputName")
        unUsuario.apellidoUsuario = request.form.get("inputLastname")
        unUsuario.mail = request.form.get("inputEmail")
        unUsuario.contrasenia = request.form.get("inputPassword")
        unUsuario.nickName = request.form.get("inputNickname")

        unUsuario.registrarUsuario()


@app.route("/Entrar")
def entrar():
    return render_template("Entrar.html")

DB().setconnection('localhost','root','alumno','mydb')


if __name__ == "__main__":
    app.run(debug=True)

    #if request.method == 'POST':
     #   result = request.form
      #  return render_template("result.html", result=result)