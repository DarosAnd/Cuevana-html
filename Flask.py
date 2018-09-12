from usuario import Usuario
from flask import *
from titulo import *
from likes  import *
import hashlib
app = Flask(__name__, static_url_path="/static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/Home")
def inicio():
    if 'userid' in session:
        return redirect("/InSession")
    return render_template("Home.html", listaPeliculas=Pelicula.getPeliculas())

@app.route("/InSession", methods=['GET', 'POST'])
def logeado():
    if 'userid' not in session:
        return redirect("/SignIn")
    return render_template("InSession.html", Usuario=Usuario.getUsuario(session["userid"]), listaPeliculas=Pelicula.getPeliculas())

@app.route("/pelicula", methods=['GET', 'POST'])
def pelicula():
    if 'userid' not in session:
        return redirect("/SignIn")

    miPelicula = Pelicula.getPelicula(int(request.args.get("id")))


    return render_template("pelicula.html", Usuario=Usuario.getUsuario(session["userid"]), pelicula=miPelicula, likes=Like.getLikesPelicula(miPelicula.idTitulo))

@app.route("/SignUp", methods = ['GET', 'POST'])
def tomarDatos():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("inputName")
        unUsuario.apellidoUsuario = request.form.get("inputLastname")
        unUsuario.mail = request.form.get("inputEmail")
        unUsuario.contrasenia = request.form.get("inputPassword")
        x = hashlib.sha256(unUsuario.contrasenia)
        unUsuario.contrasenia = x.hexdigest()
        unUsuario.nickName = request.form.get("inputNickname")
        session['userid'] = unUsuario.idUsuario

        for item in Usuario().getUsuarios():
            if item.mail == unUsuario.mail or item.nickName == unUsuario.nickName:
                return render_template("SignUp.html")

        unUsuario.registrarUsuario()

        return render_template("Home.html")
    return render_template("SignUp.html")

@app.route("/SignIn", methods = ['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
            for item in Usuario.getUsuarios():
                x = hashlib.sha256(request.form.get('inputPassword'))

                if item.nickName == request.form.get('inputNickname') and item.contrasenia == x.hexdigest():
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