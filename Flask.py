from BD import DB
from usuario import Usuario
from flask import *
import hashlib
app = Flask(__name__, static_url_path="/static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/Home")
def inicio():
    if 'userid' in session:
        return redirect("/InSession")
    return render_template("Home.html")


@app.route("/InSession", methods=['GET', 'POST'])
def logeado():
    if 'userid' not in session:
        return redirect("/Home")
    return render_template("InSession.html", Usuario=Usuario.getUsuario(session["userid"]))

@app.route("/SignUp", methods = ['GET', 'POST'])
def tomarDatos():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("inputName")
        unUsuario.apellidoUsuario = request.form.get("inputLastname")
        unUsuario.mail = request.form.get("inputEmail")
        unUsuario.contrasenia = request.form.get("inputPassword")
        unUsuario.contrasenia = hashlib.sha256(unUsuario.contrasenia.hexdigest())
        print(unUsuario.contrasenia)
        unUsuario.nickName = request.form.get("inputNickname")
        session['userid'] = unUsuario.idUsuario

        for item in Usuario().getUsuarios():
            if item.mail == unUsuario.mail or item.nickName == unUsuario.nickName:

                #Ya existe el mail ingresado
                return render_template("SignUp.html")

        unUsuario.registrarUsuario()

        return render_template("Home.html")
    return render_template("SignUp.html")

@app.route("/SignIn", methods = ['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
            for item in Usuario.getUsuarios():

                if item.nickName == request.form.get('inputNickname') and item.contrasenia == request.form.get('inputPassword'):
                    session['userid'] = Usuario.devolverIdUsuarioPorNickName(request.form.get('inputNickname'))
                    return redirect("/InSession")

    return render_template("SignIn.html")

@app.route('/LogOut')
def logout():
    session.pop('userid', None)
    return redirect('/Home')

DB().setconnection('localhost','root','alumno','mydb')

if __name__ == "__main__":
    app.run(debug=True)