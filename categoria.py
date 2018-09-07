from BD import DB

class Categoria(object):
    idCategoria = None
    nombreCategoria = None

    @staticmethod
    def getCategorias():
        listaCategoria = []

        cursor = DB().run("SELECT * FROM Categoria")

        for item in cursor:
            unaCategoria = Categoria()
            unaCategoria.idCategoria = item['idCategoria']
            unaCategoria.nombreCategoria = item['nombreCategoria']

            listaCategoria.append(unaCategoria)

        return listaCategoria

    def altaCategoria(self):
        DB().run("INSERT INTO Categoria(idCategoria,nombreCategoria)" +
                 "VALUES (NULL, '" + self.nombreCategoria + "');")

    def bajaCategoria(self):
        DB().run("DELETE FROM Categoria WHERE idCategoria = " + str(self.idCategoria) + ";")