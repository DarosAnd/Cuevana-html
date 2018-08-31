# -*- coding: utf-8 -*-
from BD import DB
from pymysql import *

class Usuario(object):
    idUsuario = None
    nombreUsuario = None
    apellidoUsuario = None
    contrasenia = None
    nickName = None
    mail = None

    def registrarUsuario(self):
        DB().run("INSERT INTO Usuario(idUsuario,nombreUsuario,apellidoUsuario,nickName,contrasenia,mail)" +
        "VALUES (NULL,'"+self.nombreUsuario+"','"+self.apellidoUsuario+"','" + self.nickName+"','"+self.contrasenia+"','"+self.mail+"');")

        for item in Usuario.getUsuarios():
            if item == self.nickName:
                self.idUsuario = item.idUsuario

    def modificacionContrasenia(self):
        DB().run("UPDATE Usuario SET contrasenia = '"+self.contrasenia + "' WHERE idUsuario = "+ str(self.idUsuario)+";")

    def modificacionNickName(self):
        DB().run("UPDATE Usuario SET nickName = '"+self.nickName + "'WHERE idUsuario = "+ str(self.idUsuario)+";")


    @staticmethod
    def devolverIdUsuarioPorNickName(nickname):
        for item in Usuario.getUsuarios():
            if item.nickName == nickname:

                return item.idUsuario
        return


    @staticmethod
    def getUsuario(id):
        unUsuario = Usuario()

        cursor = DB().run("SELECT * FROM Usuario WHERE idUsuario = "+ str(id)+";")

        dict = cursor.fetchone()

        unUsuario.idUsuario = dict['idUsuario']
        unUsuario.nombreUsuario = dict['nombreUsuario']
        unUsuario.apellidoUsuario = dict['apellidoUsuario']
        unUsuario.nickName = dict['nickName']
        unUsuario.contrasenia = dict['contrasenia']
        unUsuario.mail = dict['mail']

        return unUsuario
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
            unUsuario.contrasenia = item['contrasenia']
            unUsuario.mail = item['mail']

            listaUsuarios.append(unUsuario)

        return listaUsuarios