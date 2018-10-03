from usuario import Usuario
from flask import *
from titulo import Pelicula
from likes  import *
from comentarios import *
import hashlib
app = Flask(__name__, static_url_path="/static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return redirect("/Home")

@app.route("/Home")
def inicio():
    if 'userid' in session:
        return redirect("/InSession")
    return render_template("Home.html", listaPeliculas=Pelicula.getPeliculas())

@app.route("/SignUp", methods = ['GET', 'POST'])
def tomarDatos():
    if request.method == 'POST':
        unUsuario = Usuario()
        unUsuario.nombreUsuario = request.form.get("inputName")
        unUsuario.apellidoUsuario = request.form.get("inputLastname")
        unUsuario.mail = request.form.get("inputEmail")
        unUsuario.contrasenia = request.form.get("inputPassword")
        x = hashlib.sha256(unUsuario.contrasenia.encode('utf8'))
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
                x = hashlib.sha256(request.form.get('inputPassword').encode('utf8'))

                if item.nickName == request.form.get('inputNickname') and item.contrasenia == x.hexdigest():
                    session['userid'] = Usuario.devolverIdUsuarioPorNickName(request.form.get('inputNickname'))
                    return redirect("/InSessionPelis")

    return render_template("SignIn.html")


@app.route("/InSessionPelis", methods=['GET', 'POST'])
def logeadoPeliculas():
    if 'userid' not in session:
        return redirect("/SignIn")
    return render_template("LogeadoPeliculas.html", Usuario=Usuario.getUsuario(session["userid"]), listaPeliculas=Pelicula.getPeliculas())


@app.route("/InSessionSerie", methods=['GET','POST'])
def logeadoSeries():
    if 'userid' not in session:
        return redirect("/SignIn")
    return render_template("LogeadoSeries.html", Usuario=Usuario.getUsuario(session["userid"]), listaSeries=Serie.getSeries())


@app.route("/pelicula", methods=['GET', 'POST'])
def pelicula():
    if 'userid' not in session:
        return redirect("/SignIn")

    miPelicula = Pelicula.getPelicula(int(request.args.get("id")))
    estado = 0

    for item in Like.getLikesPelicula(miPelicula.idTitulo):
        if item.Usuario.idUsuario == session["userid"]:
            estado = 1

    return render_template("pelicula.html", Usuario=Usuario.getUsuario(session["userid"]), pelicula=miPelicula, comentarios=Comentario.getComentariosPelicula(miPelicula.idTitulo), likes=Like.getCantLikesPelicula(miPelicula.idTitulo), estado=estado)

@app.route("/LikePelicula", methods=['GET', 'POST'])
def darLikePelicula():

    unLike = Like()

    miPelicula = Pelicula.getPelicula(int(request.args.get("id")))
    unLike.Pelicula = miPelicula

    for item in Usuario.getUsuarios():
        if item.idUsuario == session['userid']:
            unLike.Usuario = item

    if not Like.getLikeUserPelicula(unLike.Usuario.idUsuario, unLike.Pelicula.idTitulo):
        unLike.altaLikePelicula()

    return redirect("/pelicula?id=" + str(miPelicula.idTitulo))

@app.route("/DislikePelicula", methods=['GET', 'POST'])
def darDislikePelicula():

    miPelicula = Pelicula.getPelicula(int(request.args.get("id")))

    for item in Like.getLikes():
        if item.Usuario.idUsuario == session['userid'] and item.Pelicula.idTitulo == miPelicula.idTitulo:
            item.bajaLikePelicula()

    return redirect("/pelicula?id=" + str(miPelicula.idTitulo))

@app.route("/Comentario",methods=['GET','POST'])
def agregarComentarioPelicula():

    if request.method == 'POST':
        unComentario = Comentario()

        miPelicula = Pelicula.getPelicula(int(request.form.get("idPelicula")))
        unComentario.Pelicula = miPelicula
        unComentario.descripcion = request.form.get("inputComment")

        for item in Usuario.getUsuarios():
            if item.idUsuario == session['userid']:
                unComentario.Usuario = item

        unComentario.altaComentarioPelicula()
    return redirect("/pelicula?id="+str(miPelicula.idTitulo))


@app.route('/LogOut')
def logout():
    session.pop('userid', None)
    return redirect('/Home')

DB().setconnection('localhost','root','alumno','mydb')

if __name__ == "__main__":
    app.run(debug=True)