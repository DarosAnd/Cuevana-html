from BD import DB
from titulo import Pelicula
from titulo import Serie
from usuario import Usuario

class Like(object):
    idLike = None
    Usuario = None
    Pelicula = None
    Serie = None

    @staticmethod
    def getLikesPelicula(idPelicula):
        listaLikes = []

        cursor = DB().run("SELECT * FROM `Like` WHERE Pelicula_idPelicula = " + str(idPelicula)+";")

        for item in cursor:
            unLike = Like()
            unLike.idLike = item['idLike']


            for item2 in Pelicula.getPeliculas():
                if item2.idTitulo == item['Pelicula_idPelicula']:
                    unLike.Pelicula = item2
            for item2 in Usuario.getUsuarios():
                if item2.idUsuario == item['Usuario_idUsuario']:
                    unLike.Usuario = item2

            listaLikes.append(unLike)

        return len(listaLikes)

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