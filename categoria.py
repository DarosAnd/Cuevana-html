from BD import DB

class Categoria(object):
    idCategoria = None
    nombreCategoria = None

    def altaCategoria(self):
        DB().run("INSERT INTO Categoria(idCategoria,nombreCategoria)" +
                 "VALUES (NULL, '" + self.nombreCategoria + "');")

    def bajaCategoria(self):
        DB().run("DELETE FROM Categoria WHERE idCategoria = " + str(self.idCategoria) + ";")