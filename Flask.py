from usuario import Usuario
from flask import *
from titulo import Pelicula
from likes  import *
from comentarios import *
import hashlib
app = Flask(__name__, static_url_path="/static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# administradores van a poder cargar peliculas (agregar, modif, borrar)
# borrar comentario, solo el usuario que lo puso LISTO o un mopderador
# paginar
# una pagina donde el usuario pueda ver todos sus likes LISTO


@app.route("/")
def index():
    return redirect("/Home")

@app.route("/Home")
def inicio():
    if 'userid' in session:
        return redirect("/InSessionPelis")
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

                    # if item.nickName == 'admin':
                    #     return redirect("/adminSession")

                    return redirect("/InSessionPelis")

    return render_template("SignIn.html")

@app.route("/InSessionPelis", methods=['GET', 'POST'])
def logeadoPeliculas():
    if 'userid' not in session:
        return redirect("/SignIn")
    return render_template("LogeadoPeliculas.html", usuario=Usuario.getUsuario(session["userid"]), listaPeliculas=Pelicula.getPeliculas())

@app.route("/InSessionSerie", methods=['GET','POST'])
def logeadoSeries():
    if 'userid' not in session:
        return redirect("/SignIn")
    return render_template("LogeadoSeries.html", usuario=Usuario.getUsuario(session["userid"]), listaSeries=Serie.getSeries())

@app.route("/pelicula", methods=['GET', 'POST'])
def pelicula():
    if 'userid' not in session:
        return redirect("/SignIn")

    miPelicula = Pelicula.getPelicula(int(request.args.get("idPelicula")))
    estado = 0

    for item in Like.getLikesPelicula(miPelicula.idTitulo):
        if item.Usuario.idUsuario == session["userid"]:
            estado = 1

    return render_template("pelicula.html", usuario=Usuario.getUsuario(session["userid"]), pelicula=miPelicula, comentarios=Comentario.getComentariosPelicula(miPelicula.idTitulo), likes=Like.getCantLikesPelicula(miPelicula.idTitulo), estado=estado)

@app.route("/serie", methods=['GET','POST'])
def serie():
    if 'userid' not in session:
        return redirect("/SignIn")

    miSerie = Serie.getSerie(int(request.args.get("idSerie")))
    estado = 0

    for item in Like.getLikesSerie(miSerie.idTitulo):
        if item.Usuario.idUsuario == session["userid"]:
            estado = 1

    return render_template("serie.html", usuario=Usuario.getUsuario(session["userid"]), serie=miSerie, likes=Like.getCantLikesSerie(miSerie.idTitulo), estado=estado, capitulos=Capitulo.getCapitulos(miSerie.idTitulo))

@app.route("/LikePelicula", methods=['GET', 'POST'])
def darLikePelicula():

    unLike = Like()

    miPelicula = Pelicula.getPelicula(int(request.args.get("idPelicula")))
    unLike.Pelicula = miPelicula

    for item in Usuario.getUsuarios():
        if item.idUsuario == session['userid']:
            unLike.Usuario = item

    if not Like.getLikeUserPelicula(unLike.Usuario.idUsuario, unLike.Pelicula.idTitulo):
        unLike.altaLikePelicula()

    return redirect("/pelicula?idPelicula=" + str(miPelicula.idTitulo))

@app.route("/DislikePelicula", methods=['GET', 'POST'])
def darDislikePelicula():

    miPelicula = Pelicula.getPelicula(int(request.args.get("idPelicula")))

    for item in Like.getLikes():
        if item.Pelicula==None:
            continue
        if item.Usuario.idUsuario == session['userid'] and item.Pelicula.idTitulo == miPelicula.idTitulo:
            item.bajaLike()

    return redirect("/pelicula?idPelicula=" + str(miPelicula.idTitulo))

@app.route("/LikeSerie",methods=['GET','POST'])
def darLikeSerie():
    unLike = Like()

    miSerie = Serie.getSerie(int(request.args.get("idSerie")))
    unLike.Serie = miSerie

    for item in Usuario.getUsuarios():
        if item.idUsuario == session['userid']:
            unLike.Usuario = item

    if not Like.getLikeUserSerie(unLike.Usuario.idUsuario, unLike.Serie.idTitulo):
        unLike.altaLikeSerie()

    return redirect("/serie?idSerie=" + str(miSerie.idTitulo))

@app.route("/DislikeSerie", methods=['GET', 'POST'])
def darDislikeSerie():
    miSerie = Serie.getSerie(int(request.args.get("idSerie")))

    for item in Like.getLikes():
        if item.Serie == None:
            continue
        if item.Usuario.idUsuario == session['userid'] and item.Serie.idTitulo == miSerie.idTitulo:
            item.bajaLike()

    return redirect("/serie?idSerie=" + str(miSerie.idTitulo))

@app.route("/ComentarioPelicula",methods=['GET','POST'])
def agregarComentarioPelicula():

    miPelicula = Pelicula.getPelicula(int(request.form.get("idPelicula")))

    if request.method == 'POST':
        unComentario = Comentario()

        unComentario.Pelicula = miPelicula
        unComentario.descripcion = request.form.get("inputComment")

        for item in Usuario.getUsuarios():
            if item.idUsuario == session['userid']:
                unComentario.Usuario = item

        unComentario.altaComentarioPelicula()

    return redirect("/pelicula?idPelicula="+str(miPelicula.idTitulo))

@app.route('/pelisLikeadas',methods=['GET','POST'])
def pelisLikeadas():
    if 'userid' not in session:
        return redirect("/SignIn")

    return render_template("pelisLikeadas.html", pelis=Like.pelisLikeUsuario(session['userid']), usuario=Usuario.getUsuario(session["userid"]))

@app.route('/seriesLikeadas',methods=['GET','POST'])
def seriesLikeadas():
    if 'userid' not in session:
        return redirect("/SignIn")

    return render_template("seriesLikeadas.html", series=Like.seriesLikeUsuario(session['userid']), usuario=Usuario.getUsuario(session["userid"]))

@app.route('/borrarComentario',methods=['GET','POST'])
def borrarComentario():
    if 'userid' not in session:
        return redirect("/SignIn")

    miPelicula = Pelicula.getPelicula(int(request.args.get("idPelicula")))

    for item in Comentario.getComentarios():
        if item.idComentario == int(request.args.get('idComentario')):
            item.bajaComentarioPelicula()

    return redirect("/pelicula?idPelicula=" + str(miPelicula.idTitulo))

@app.route('/LogOut')
def logout():
    session.pop('userid', None)
    return redirect('/Home')

DB().setconnection('localhost','root','alumno','mydb')

if __name__ == "__main__":
    app.run(debug=True)