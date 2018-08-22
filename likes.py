from BD import DB

class Like(object):
    idLike = None
    Usuario = None
    Pelicula = None
    Serie = None

    def altaLikePelicula(self):
        DB().run("INSERT INTO Like(idLike,Usuario_idUsuario,Serie_idSerie,Pelicula_idPelicula) VALUES (NULL, " +
            str(self.Usuario.idUsuario)+", NULL, "+str(self.Pelicula.idTitulo)+ ");")
    def altaLikeSerie(self):
        DB().run("INSERT INTO Like(idLike,Usuario_idUsuario,Serie_idSerie,Pelicula_idPelicula) VALUES ( NULL " + ", " +
            str(self.Usuario.idUsuario) + ", " + str(self.Serie.idTitulo) + ", NULL);")

    def bajaLikePelicula(self):
        DB().run("DELETE FROM Like WHERE idLike = " + str(self.idLike) + ";")
    def bajaLikeSerie(self):
        DB().run("DELETE FROM Like WHERE idLike = "+ str(self.idLike) + ";")