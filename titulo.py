from BD import DB
from categoria import Categoria

class Titulo(object):
    idTitulo = None
    nombreTitulo = None
    Categoria = None
    Linkimagen = None

class Pelicula(Titulo):
    linkPelicula = None

    @staticmethod
    def getPeliculas():
        listaPeliculas = []

        cursor = DB().run("SELECT * FROM Pelicula")

        for item in cursor:
            unaPelicula = Pelicula()
            unaPelicula.idTitulo = item['idPelicula']
            unaPelicula.nombreTitulo = item['nombrePelicula']
            unaPelicula.Linkimagen = item['linkImagenPelicula']
            unaPelicula.linkPelicula = item['linkPelicula']

            for item2 in Categoria.getCategorias():
                if item2.idCategoria == item['Categoria_idCategoria']:
                    unaPelicula.Categoria = item2

            listaPeliculas.append(unaPelicula)

        return listaPeliculas

    def altaPelicula(self):
        DB().run("INSERT INTO Pelicula(idPelicula,nombrePelicula,linkPelicula,Categoria_idCategoria)" +
                 "VALUES (NULL,'" + self.nombreTitulo + "','" + self.linkPelicula + "','" +
                 self.Categoria.idCategoria + "');")

    def bajaPelicula(self):
            DB().run("DELETE FROM Pelicula WHERE idPelicula = " + str(self.idTitulo) + ";")

    def modificacionPelicula(self):
        DB().run("UPDATE Usuario SET linkPelicula = '" + self.linkPelicula +
                 "', Categoria_idCategoria = '" + self.Categoria.idCategoria + "' WHERE idPelicula = " + str(self.idTitulo) + ";")


class Serie(Titulo):
    def altaSerie(self):
        DB().run("INSERT INTO Serie(idSerie,nombreSerie,Categoria_idCategoria)" +
                 "VALUES (NULL,'" + self.nombreTitulo + "','" + self.Categoria.idCategoria + "');")

    def bajaSerie(self):
            DB().run("DELETE FROM Serie WHERE idSerie = " + str(self.idTitulo) + ";")

    def modificacionSerie(self):
        DB().run("UPDATE Usuario SET Categoria_idCategoria = '" + self.Categoria.idCategoria +
                 "' WHERE idPelicula = " + str(self.idTitulo) + ";")

class Capitulo(object):
    idCapitulo = None
    linkCapitulo = None
    nombreCapitulo = None
    nroCapitulo = None
    nroTemporada = None
    Serie = None

    def altaCapitulo(self):
        DB().run("INSERT INTO Capitulo(idCapitulo,nombreCapitulo,nroCapitulo,nroTemporada,Serie_idSerie,linkCapitulo)" +
                 "VALUES (NULL,'" + self.nombreCapitulo + "'," + str(self.nroCapitulo) + "," + str(self.nroTemporada)  +
                 "," + str(self.Serie.idTitulo) + ",'" + self.linkCapitulo + "');")

    def bajaCapitulo(self):
            DB().run("DELETE FROM Serie WHERE idSerie = " + str(self.idCapitulo) + ";")

    def modificacionLinkCapitulo(self):
        DB().run("UPDATE Capitulo SET linkCapitulo = '" + self.linkCapitulo + "' WHERE idCapitulo = " +
str(self.idCapitulo) + ";")