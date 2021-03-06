from BD import DB
from titulo import *
from usuario import *

class Comentario(object):
    idComentario = None
    descripcion = None
    Usuario = None
    Pelicula = None
    Capitulo = None

    @staticmethod
    def getComentarios():
        listaComentarios = []

        cursor = DB().run("SELECT * FROM Comentario")

        for item in cursor:
            unComentario = Comentario()
            unComentario.idComentario = item['idComentario']
            unComentario.descripcion = item['descripcion']

            for item3 in Usuario.getUsuarios():
                if item3.idUsuario == item['Usuario_idUsuario']:
                    unComentario.Usuario = item3

            for item2 in Pelicula.getPeliculas(1000, 0):
                if item2.idTitulo == item['Pelicula_idPelicula']:
                    unComentario.Pelicula = item2

            listaComentarios.append(unComentario)

        return listaComentarios

    @staticmethod
    def getComentariosPelicula(idPelicula):
        listaComentarios = []

        cursor = DB().run("SELECT * FROM Comentario WHERE Pelicula_idPelicula = " + str(idPelicula) + ";")

        for item in cursor:
            unComentario = Comentario()
            unComentario.idComentario = item['idComentario']
            unComentario.descripcion = item['descripcion']

            for item2 in Pelicula.getPeliculas(1000, 0):
                if item2.idTitulo == item['Pelicula_idPelicula']:
                    unComentario.Pelicula = item2
            for item3 in Usuario.getUsuarios():
                if item3.idUsuario == item['Usuario_idUsuario']:
                    unComentario.Usuario = item3

            listaComentarios.append(unComentario)

        return listaComentarios


    def altaComentarioPelicula(self):
        c = DB().run("INSERT INTO Comentario(idComentario,descripcion,Usuario_idUsuario,Pelicula_idPelicula,Capitulo_idCapitulo) VALUES (NULL, '" + self.descripcion + "', " + str(self.Usuario.idUsuario) + "," + str(self.Pelicula.idTitulo) + ", NULL);")

        self.idComentario = c.lastrowid

    def bajaComentarioPelicula(self):
        DB().run("DELETE FROM Comentario WHERE idComentario = "+str(self.idComentario)+";")

    def altaComentarioCapitulo(self):
        DB().run("INSERT INTO Comentario(idComentario,descripcion,Usuario_idUsuario,Pelicula_idPelicula,Capitulo_idCapitulo) VALUES (NULL, '" + self.descripcion + "', " + self.Usuario.idUsuario + ", NULL," + self.Capitulo.idCapitulo+");")

    def bajaComentarioCapitulo(self):
        DB().run("DELETE FROM Comentario WHERE idComentario = "+str(self.idComentario)+";")