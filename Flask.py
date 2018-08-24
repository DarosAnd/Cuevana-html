from BD import DB
from usuario import Usuario
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static")

@app.route("/Inicio")
def inicio():
    return render_template("Home.html")

@app.route("/InicioLogeado", methods = ['GET', 'POST'])
def logeado():
    return render_template("InicioLogeado.html")

@app.route("/Registro", methods = ['GET', 'POST'])
def tomarDatos():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("inputName")
        unUsuario.apellidoUsuario = request.form.get("inputLastname")
        unUsuario.mail = request.form.get("inputEmail")
        unUsuario.contrasenia = request.form.get("inputPassword")
        unUsuario.nickName = request.form.get("inputNickname")

        for item in Usuario().getUsuarios():
            if item.mail == unUsuario.mail or item.nickName == unUsuario.nickName:

                #Ya existe el mail ingresado
                return render_template("Registrar.html")

        unUsuario.registrarUsuario()

        return render_template("InicioLogeado.html")
    return render_template("Registrar.html")

@app.route("/Entrar", methods = ['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        for item in Usuario().getUsuarios():
            if item.mail == request.form.get("inputEmail") and item.contrasenia == request.form.get("inputPassword"):
                return render_template("InicioLogeado.html")
    return render_template("Entrar.html")

DB().setconnection('localhost','root','alumno','mydb')

if __name__ == "__main__":
    app.run(debug=True)

    #if request.method == 'POST':
     #   result = request.form
      #  return render_template("result.html", result=result)