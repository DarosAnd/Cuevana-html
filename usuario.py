from BD import DB

class Usuario(object):
    idUsuario = None
    nombreUsuario = None
    apellidoUsuario = None
    contrasenia = None
    nickName = None
    mail = None

    def registrarUsuario(self):
        DB().run("INSERT INTO Usuario(idUsuario,nombreUsuario,apellidoUsuario,nickName,contraseña,mail)" +
                 "VALUES (NULL,'"+self.nombreUsuario+"','"+self.apellidoUsuario+"','" + self.contrasenia+"','"+self.nickName+"','"+self.mail+"');")

    def modificacionContrasenia(self):
        DB().run("UPDATE Usuario SET contraseña = '"+self.contrasenia + "';")

    def modificacionNickName(self):
        DB().run("UPDATE Usuario SET nickName = '"+self.nickName + "';")

    @staticmethod
    def getUsuarios():
        listaUsuarios = []

        cursor = DB().run("SELECT * FROM Usuario")

        for item in cursor:
            unUsuario = Usuario()
            unUsuario.idUsuario = item['idUsuario']
            unUsuario.nombreUsuario = item['nombreUsuario']
            unUsuario.apellidoUsuario = item['apellidoUsuario']
            unUsuario.nickName = item['nickName']
            unUsuario.contrasenia = item['contraseña']
            unUsuario.mail = item['mail']

            listaUsuarios.append(unUsuario)

        return listaUsuarios