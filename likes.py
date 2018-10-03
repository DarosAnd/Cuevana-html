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
    def getLikeUserPelicula(iduser, idpelicula):
        unLike = Like()

        cursor = DB().run("SELECT * FROM `Like` WHERE Usuario_idUsuario = "+ str(iduser) +" AND Pelicula_idPelicula = "+str(idpelicula) +";")

        dict = cursor.fetchone()

        if dict is None:
            return False
        return True

    @staticmethod
    def getLikeUserSerie(iduser, idserie):
        unLike = Like()

        cursor = DB().run(
            "SELECT * FROM `Like` WHERE Usuario_idUsuario = " + str(iduser) + " AND Serie_idSerie = " + str(idserie) + ";")

        dict = cursor.fetchone()

        if dict is None:
            return False
        return True


    @staticmethod
    def getCantLikesPelicula(idPelicula):
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

    @staticmethod
    def getCantLikesSerie(idSerie):
        listaLikes = []

        cursor = DB().run("SELECT * FROM `Like` WHERE Serie_idSerie= " + str(idSerie) + ";")

        for item in cursor:
            unLike = Like()
            unLike.idLike = item['idLike']

            for item2 in Pelicula.getPeliculas():
                if item2.idTitulo == item['Serie_idSerie']:
                    unLike.Serie = item2
            for item2 in Usuario.getUsuarios():
                if item2.idUsuario == item['Usuario_idUsuario']:
                    unLike.Usuario = item2

            listaLikes.append(unLike)

        return len(listaLikes)


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

        return listaLikes

    @staticmethod
    def getLikesSerie(idSerie):
        listaLikes = []

        cursor = DB().run("SELECT * FROM `Like` WHERE Serie_idSerie = " + str(idSerie) + ";")

        for item in cursor:
            unLike = Like()
            unLike.idLike = item['idLike']

            for item2 in Pelicula.getPeliculas():
                if item2.idTitulo == item['Serie_idSerie']:
                    unLike.Serie = item2
            for item2 in Usuario.getUsuarios():
                if item2.idUsuario == item['Usuario_idUsuario']:
                    unLike.Usuario = item2

            listaLikes.append(unLike)

        return listaLikes

    @staticmethod
    def getLikes():
        listaLikes = []

        cursor = DB().run("SELECT * FROM `Like`;")

        for item in cursor:
            unLike = Like()
            unLike.idLike = item['idLike']

            for item2 in Pelicula.getPeliculas():
                if item2.idTitulo == item['Pelicula_idPelicula']:
                    unLike.Pelicula = item2
            for item3 in Usuario.getUsuarios():
                if item3.idUsuario == item['Usuario_idUsuario']:
                    unLike.Usuario = item3

            listaLikes.append(unLike)

        return listaLikes


    def altaLikePelicula(self):
        DB().run("INSERT INTO `Like`(idLike,Usuario_idUsuario,Serie_idSerie,Pelicula_idPelicula) VALUES (NULL, " + str(self.Usuario.idUsuario)+", NULL, "+str(self.Pelicula.idTitulo) + ");")

        for item in Like.getLikes():
            if item.Pelicula == None:
                continue
            if item.Pelicula.idTitulo == self.Pelicula.idTitulo and item.Usuario.idUsuario == self.Usuario.idUsuario:
                self.idLike = item.idLike

    def altaLikeSerie(self):
        DB().run("INSERT INTO `Like`(idLike,Usuario_idUsuario,Serie_idSerie,Pelicula_idPelicula) VALUES ( NULL " + ", " +
            str(self.Usuario.idUsuario) + ", " + str(self.Serie.idTitulo) + ", NULL);")

        for item in Like.getLikes():
            if item.Serie == None:
                continue
            if item.Serie.idTitulo == self.Serie.idTitulo and item.Usuario.idUsuario == self.Usuario.idUsuario:
                self.idLike = item.idLike

    def bajaLikePelicula(self):
        DB().run("DELETE FROM `Like` WHERE idLike = " + str(self.idLike) + ";")
    def bajaLikeSerie(self):
        DB().run("DELETE FROM `Like` WHERE idLike = "+ str(self.idLike) + ";")