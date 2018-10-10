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

    @staticmethod
    def getPelicula(id):
        cursor = DB().run("SELECT * FROM Pelicula where idPelicula="+str(id)+";")
        unaPelicula = Pelicula()
        for item in cursor:

            unaPelicula.idTitulo = item['idPelicula']
            unaPelicula.nombreTitulo = item['nombrePelicula']
            unaPelicula.Linkimagen = item['linkImagenPelicula']
            unaPelicula.linkPelicula = item['linkPelicula']

            for item2 in Categoria.getCategorias():
                if item2.idCategoria == item['Categoria_idCategoria']:
                    unaPelicula.Categoria = item2

        return unaPelicula

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

    @staticmethod
    def getSeries():
        listaSeries = []

        cursor = DB().run("SELECT * FROM Serie")

        for item in cursor:
            unaSeries = Pelicula()
            unaSeries.idTitulo = item['idSerie']
            unaSeries.nombreTitulo = item['nombreSerie']
            unaSeries.Linkimagen = item['linkImagenSerie']

            for item2 in Categoria.getCategorias():
                if item2.idCategoria == item['Categoria_idCategoria']:
                    unaSeries.Categoria = item2

            listaSeries.append(unaSeries)

        return listaSeries

    @staticmethod
    def getSerie(id):

        cursor = DB().run("SELECT * FROM Serie where idSerie=" + str(id) + ";")

        unaSerie = Serie()

        for item in cursor:

            unaSerie.idTitulo = item['idSerie']
            unaSerie.nombreTitulo = item['nombreSerie']
            unaSerie.Linkimagen = item['linkImagenSerie']

            for item2 in Categoria.getCategorias():
                if item2.idCategoria == item['Categoria_idCategoria']:
                    unaSerie.Categoria = item2

        return unaSerie


class Capitulo(object):
    idCapitulo = None
    linkCapitulo = None
    nombreCapitulo = None
    nroCapitulo = None
    nroTemporada = None
    Serie = None

    @staticmethod
    def getCapitulos(idSerie):
        listaCapitulos = []

        cursor = DB().run("SELECT * FROM Capitulo WHERE Serie_idSerie = " + str(idSerie) + ";")

        for item in cursor:
            unCapitulo = Capitulo()
            unCapitulo.idCapitulo = item['idCapitulo']
            unCapitulo.nombreCapitulo = item['nombreCapitulo']
            unCapitulo.nroCapitulo = item['nroCapitulo']
            unCapitulo.nroTemporada = item['nroTemporada']
            unCapitulo.linkCapitulo = item['linkCapitulo']

            for item2 in Serie.getSeries():
                if item2.idTitulo == item['Serie_idSerie']:
                    unCapitulo.Serie = item2

            listaCapitulos.append(unCapitulo)

        return listaCapitulos

    def altaCapitulo(self):
        DB().run("INSERT INTO Capitulo(idCapitulo,nombreCapitulo,nroCapitulo,nroTemporada,Serie_idSerie,linkCapitulo)" +
                 "VALUES (NULL,'" + self.nombreCapitulo + "'," + str(self.nroCapitulo) + "," + str(self.nroTemporada)  +
                 "," + str(self.Serie.idTitulo) + ",'" + self.linkCapitulo + "');")

    def bajaCapitulo(self):
            DB().run("DELETE FROM Serie WHERE idSerie = " + str(self.idCapitulo) + ";")

    def modificacionLinkCapitulo(self):
        DB().run("UPDATE Capitulo SET linkCapitulo = '" + self.linkCapitulo + "' WHERE idCapitulo = " + str(self.idCapitulo) + ";")