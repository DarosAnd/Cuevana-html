from BD import DB
from usuario import Usuario
from flask import *
app = Flask(__name__, static_url_path="/static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/Inicio")
def inicio():
    if 'userid' in session:
        return redirect("/InicioLogeado")
    return render_template("Home.html")


@app.route("/InicioLogeado", methods=['GET', 'POST'])
def logeado():
    print("ACA " + session["userid"])
    return render_template("InicioLogeado.html", Usuario=Usuario.getUsuario(session["userid"]))

@app.route("/Registro", methods = ['GET', 'POST'])
def tomarDatos():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("inputName")
        unUsuario.apellidoUsuario = request.form.get("inputLastname")
        unUsuario.mail = request.form.get("inputEmail")
        unUsuario.contrasenia = request.form.get("inputPassword")
        unUsuario.nickName = request.form.get("inputNickname")
        session['userid'] = unUsuario.idUsuario

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
            for item in Usuario.getUsuarios():
                if item.nickName == request.form['inputNickname'] and item.contrasenia == request.form['inputPassword']:
                    print("Seteanding " + request.form['inputNickname'])
                    print("Seteanding " + Usuario.devolverIdUsuarioPorNickName(request.form['inputNickname']))
                    session['userid'] = Usuario.devolverIdUsuarioPorNickName(request.form['inputNickname'])

                    return render_template("InicioLogeado.html")

    return render_template("Entrar.html")

@app.route('/logout')
def salir():
   session.pop('username', None)
   return render_template('Home.html')

DB().setconnection('localhost','root','alumno','mydb')

if __name__ == "__main__":
    app.run(debug=True)

    #if request.method == 'POST':
     #   result = request.form
      #  return render_template("result.html", result=result)