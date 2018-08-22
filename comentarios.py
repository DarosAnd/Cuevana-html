from BD import DB

class Comentario(object):
    idComentario = None
    descripcion = None
    Usuario = None
    Pelicula = None
    Capitulo = None

    def altaComentarioPelicula(self):
        DB().run("INSERT INTO Comentario(idComentario,descripcion,Usuario_idUsuario,Pelicula_idPelicula,Capitulo_idCapitulo) VALUES (NULL, '"
                 + self.descripcion + "', " + self.Usuario.idUsuario + "," +
                 self.Pelicula.idTitulo + ", NULL);")
    def altaComentarioCapitulo(self):
        DB().run("INSERT INTO Comentario(idComentario,descripcion,Usuario_idUsuario,Pelicula_idPelicula,Capitulo_idCapitulo) VALUES (NULL, '"
+ self.descripcion + "', " + self.Usuario.idUsuario + ", NULL," + self.Capitulo.idCapitulo+");")