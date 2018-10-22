-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Capitulo`
--

DROP TABLE IF EXISTS `Capitulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Capitulo` (
  `idCapitulo` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCapitulo` varchar(45) DEFAULT NULL,
  `nroCapitulo` int(11) DEFAULT NULL,
  `nroTemporada` int(11) DEFAULT NULL,
  `Serie_idSerie` int(11) NOT NULL,
  `linkCapitulo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCapitulo`),
  KEY `fk_Capitulo_Serie_idx` (`Serie_idSerie`),
  CONSTRAINT `fk_Capitulo_Serie` FOREIGN KEY (`Serie_idSerie`) REFERENCES `Serie` (`idSerie`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Capitulo`
--

LOCK TABLES `Capitulo` WRITE;
/*!40000 ALTER TABLE `Capitulo` DISABLE KEYS */;
INSERT INTO `Capitulo` VALUES (1,'Capitulo 1',1,1,3,'pitoPara1.com'),(2,'Capitulo 2',2,1,3,'pitoPara2.com'),(3,'Capitulo 3',3,1,3,'pitoPara3.com'),(4,'Capitulo 1',1,2,3,'pitoPara1_2.com'),(5,'Capitulo 2',2,2,3,'pitoPara2_2.com'),(6,'Capitulo 1',1,1,3,'pitoPara1.com'),(7,'Capitulo 2',2,1,3,'pitoPara2.com'),(8,'Capitulo 3',3,1,3,'pitoPara3.com'),(9,'Capitulo 1',1,2,3,'pitoPara1_2.com'),(10,'Capitulo 2',2,2,3,'pitoPara2_2.com'),(11,'Capitulo 1',1,1,3,'pitoPara1.com'),(12,'Capitulo 2',2,1,3,'pitoPara2.com'),(13,'Capitulo 3',3,1,3,'pitoPara3.com'),(14,'Capitulo 1',1,2,3,'pitoPara1_2.com'),(15,'Capitulo 2',2,2,3,'pitoPara2_2.com');
/*!40000 ALTER TABLE `Capitulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Categoria`
--

DROP TABLE IF EXISTS `Categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Categoria` (
  `idCategoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCategoria` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categoria`
--

LOCK TABLES `Categoria` WRITE;
/*!40000 ALTER TABLE `Categoria` DISABLE KEYS */;
INSERT INTO `Categoria` VALUES (1,'Accion'),(2,'Comedia'),(3,'Ciencia Ficcion'),(4,'Terror');
/*!40000 ALTER TABLE `Categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comentario`
--

DROP TABLE IF EXISTS `Comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comentario` (
  `idComentario` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) DEFAULT NULL,
  `Usuario_idUsuario` int(11) NOT NULL,
  `Pelicula_idPelicula` int(11) DEFAULT NULL,
  `Capitulo_idCapitulo` int(11) DEFAULT NULL,
  PRIMARY KEY (`idComentario`),
  KEY `fk_Comentario_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_Comentario_Pelicula1_idx` (`Pelicula_idPelicula`),
  KEY `fk_Comentario_Capitulo1_idx` (`Capitulo_idCapitulo`),
  CONSTRAINT `fk_Comentario_Capitulo1` FOREIGN KEY (`Capitulo_idCapitulo`) REFERENCES `Capitulo` (`idCapitulo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comentario_Pelicula1` FOREIGN KEY (`Pelicula_idPelicula`) REFERENCES `Pelicula` (`idPelicula`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comentario_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `Usuario` (`idUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comentario`
--

LOCK TABLES `Comentario` WRITE;
/*!40000 ALTER TABLE `Comentario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comentario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Like`
--

DROP TABLE IF EXISTS `Like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Like` (
  `idLike` int(11) NOT NULL AUTO_INCREMENT,
  `Usuario_idUsuario` int(11) NOT NULL,
  `Serie_idSerie` int(11) DEFAULT NULL,
  `Pelicula_idPelicula` int(11) DEFAULT NULL,
  PRIMARY KEY (`idLike`),
  KEY `fk_Like_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_Like_Serie1_idx` (`Serie_idSerie`),
  KEY `fk_Like_Pelicula1_idx` (`Pelicula_idPelicula`),
  CONSTRAINT `fk_Like_Pelicula1` FOREIGN KEY (`Pelicula_idPelicula`) REFERENCES `Pelicula` (`idPelicula`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Like_Serie1` FOREIGN KEY (`Serie_idSerie`) REFERENCES `Serie` (`idSerie`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Like_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `Usuario` (`idUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Like`
--

LOCK TABLES `Like` WRITE;
/*!40000 ALTER TABLE `Like` DISABLE KEYS */;
INSERT INTO `Like` VALUES (38,1,3,NULL);
/*!40000 ALTER TABLE `Like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pelicula`
--

DROP TABLE IF EXISTS `Pelicula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pelicula` (
  `idPelicula` int(11) NOT NULL AUTO_INCREMENT,
  `nombrePelicula` varchar(45) DEFAULT NULL,
  `linkPelicula` varchar(200) DEFAULT NULL,
  `Categoria_idCategoria` int(11) NOT NULL,
  `linkImagenPelicula` varchar(200) NOT NULL,
  PRIMARY KEY (`idPelicula`),
  KEY `fk_Pelicula_Categoria1_idx` (`Categoria_idCategoria`),
  CONSTRAINT `fk_Pelicula_Categoria1` FOREIGN KEY (`Categoria_idCategoria`) REFERENCES `Categoria` (`idCategoria`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pelicula`
--

LOCK TABLES `Pelicula` WRITE;
/*!40000 ALTER TABLE `Pelicula` DISABLE KEYS */;
INSERT INTO `Pelicula` VALUES (12,'Dirty Grandpa','https://goo.gl/axUPPw',2,'https://goo.gl/tFtnSH'),(15,'Busqueda Implacable','https://goo.gl/dPQ8bW',1,'https://goo.gl/QAnSnG'),(17,'Infiniy War','https://goo.gl/73AFum',1,'https://goo.gl/dUMe8Y'),(18,'Star Wars: El despertar de la fuerza','https://goo.gl/ptvrQp',3,'https://goo.gl/UVAVYp'),(19,'Dumb and Dumber','',2,'https://goo.gl/Qeey62');
/*!40000 ALTER TABLE `Pelicula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Serie`
--

DROP TABLE IF EXISTS `Serie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Serie` (
  `idSerie` int(11) NOT NULL AUTO_INCREMENT,
  `nombreSerie` varchar(45) DEFAULT NULL,
  `Categoria_idCategoria` int(11) NOT NULL,
  `linkImagenSerie` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idSerie`),
  KEY `fk_Serie_Categoria1_idx` (`Categoria_idCategoria`),
  CONSTRAINT `fk_Serie_Categoria1` FOREIGN KEY (`Categoria_idCategoria`) REFERENCES `Categoria` (`idCategoria`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Serie`
--

LOCK TABLES `Serie` WRITE;
/*!40000 ALTER TABLE `Serie` DISABLE KEYS */;
INSERT INTO `Serie` VALUES (3,'Merli',1,'https://goo.gl/K3QtPc'),(6,'El Marginal',1,'https://goo.gl/cWbSfC'),(7,'El Marginal',1,'https://goo.gl/cWbSfC');
/*!40000 ALTER TABLE `Serie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario` (
  `idUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombreUsuario` varchar(45) DEFAULT NULL,
  `apellidoUsuario` varchar(45) DEFAULT NULL,
  `nickName` varchar(45) DEFAULT NULL,
  `contrasenia` varchar(1000) DEFAULT NULL,
  `mail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES (1,'Nico','Manuel','NickManu','5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5','nicoManue@gmail.com'),(2,'admin','istrador','admin','677790ddd4e4193d9193143c3a227cf79f76804236163f6659b3333853ae4fe0','admin@gmail.com'),(3,'pito','pitos','pitoPito','5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5','pitos@gmail.com');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-22 16:20:51
