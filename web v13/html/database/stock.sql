-- MySQL dump 10.16  Distrib 10.1.23-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: stock
-- ------------------------------------------------------
-- Server version	10.1.23-MariaDB-9+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `errorlog`
--

DROP TABLE IF EXISTS `errorlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `errorlog` (
  `id_errorlog` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_transacc` int(50) NOT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_errorlog`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `errorlog`
--

LOCK TABLES `errorlog` WRITE;
/*!40000 ALTER TABLE `errorlog` DISABLE KEYS */;
INSERT INTO `errorlog` VALUES (1,'2018-10-29 20:52:21',1,'desc5555'),(2,'2018-11-14 21:56:17',0,'Se escaneo el código: T\0imeOut que no existe en el stock.'),(3,'2018-11-14 23:01:16',0,'Se escaneo el código: 212 que no existe en el stock.'),(4,'2018-11-14 23:13:07',0,'Se escaneo el codigo:  cuyo stock es 0'),(5,'2018-11-20 23:46:09',1,'Se escaneo el codigo:  cuyo stock es 0'),(6,'2018-11-20 23:57:07',2,'Se escaneo el codigo: 1 que no existe en el stock.'),(7,'2018-11-20 23:57:11',2,'Se escaneo el codigo: 1 que no existe en el stock.'),(8,'2018-11-20 23:57:15',2,'Se escaneo el codigo: 345 que no existe en el stock.'),(9,'2018-11-21 18:51:28',2,'Se escaneo el codigo: 345 que no existe en el stock.'),(10,'2018-11-27 16:58:28',4,'Se escaneo el codigo: 0000000 que no existe en el stock.'),(11,'2018-11-28 21:49:46',4,'Se escaneo el codigo: a que no existe en el stock.'),(12,'2018-11-28 21:50:44',4,'Se escaneo el codigo: 983 que no existe en el stock.'),(13,'2018-11-28 21:50:48',4,'Se escaneo el codigo: a que no existe en el stock.'),(14,'2018-11-28 21:53:07',4,'Se escaneo el codigo: 983 que no existe en el stock.'),(15,'2018-11-28 21:53:14',4,'Se escaneo el codigo: a que no existe en el stock.'),(16,'2018-11-28 21:57:18',4,'Se escaneo el codigo: 2s2 que no existe en el stock.'),(17,'2018-11-28 21:57:31',4,'Se escaneo el codigo: 983 que no existe en el stock.'),(18,'2018-11-28 21:57:36',4,'Se escaneo el codigo: 1r3 que no existe en el stock.'),(19,'2018-11-28 21:57:48',4,'Se escaneo el codigo: 1r3 que no existe en el stock.'),(20,'2018-11-28 21:57:55',4,'Se escaneo el codigo: 2q3 que no existe en el stock.');
/*!40000 ALTER TABLE `errorlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `precio` int(50) NOT NULL,
  `cantidad` int(50) NOT NULL,
  `umbral` int(50) NOT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `id_producto` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'123','Producto 1',10,27,10),(2,'0987654321','Producto 2',4,1,2),(3,'121212121212','Producto 3',47,1,2),(4,'212','Producto 4',47,18,2),(5,'322323232323','Producto 5',47,1,2),(6,'TimeOut','dfghjk',23456,8,12),(7,'1','wertyudfg',3434,10,78);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transacclog`
--

DROP TABLE IF EXISTS `transacclog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transacclog` (
  `id_transacclog` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_transacc` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  PRIMARY KEY (`id_transacclog`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transacclog`
--

LOCK TABLES `transacclog` WRITE;
/*!40000 ALTER TABLE `transacclog` DISABLE KEYS */;
INSERT INTO `transacclog` VALUES (1,'2018-10-29 21:55:51',1,1),(2,'2018-11-14 23:05:01',0,1),(3,'2018-11-14 23:05:01',0,1),(4,'2018-11-14 23:05:01',0,4),(5,'2018-11-14 23:13:07',0,1),(6,'2018-11-14 23:13:07',0,1),(7,'2018-11-14 23:13:24',0,1),(8,'2018-11-14 23:17:11',1,4),(9,'2018-11-14 23:17:11',1,4),(10,'2018-11-14 23:17:11',1,4),(11,'2018-11-20 23:46:09',1,1),(12,'2018-11-20 23:46:09',1,1),(13,'2018-11-20 23:46:09',1,1),(14,'2018-11-20 23:46:09',1,1),(15,'2018-11-20 23:46:09',1,6),(16,'2018-11-20 23:46:09',1,1),(17,'2018-11-20 23:46:09',1,4),(18,'2018-11-20 23:46:09',1,4),(19,'2018-11-20 23:51:00',1,1),(20,'2018-11-20 23:51:00',1,1),(21,'2018-11-20 23:51:00',1,1),(22,'2018-11-20 23:51:00',1,1),(23,'2018-11-20 23:51:00',1,1),(24,'2018-11-21 21:35:46',2,1),(25,'2018-11-21 21:35:46',2,1),(26,'2018-11-21 21:35:46',2,4),(27,'2018-11-21 21:35:46',2,1),(28,'2018-11-21 23:00:14',3,1),(29,'2018-11-21 23:00:14',3,1);
/*!40000 ALTER TABLE `transacclog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variables`
--

DROP TABLE IF EXISTS `variables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `variables` (
  `id_variables` int(11) NOT NULL AUTO_INCREMENT,
  `mail` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `asunto_alerta` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `mensaje_ticket` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `nombre_establecim` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  PRIMARY KEY (`id_variables`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variables`
--

LOCK TABLES `variables` WRITE;
/*!40000 ALTER TABLE `variables` DISABLE KEYS */;
INSERT INTO `variables` VALUES (1,'edutk@vera.com.uy','Alerta de stock minimo','Gracias por su compra','Local Kiosko');
/*!40000 ALTER TABLE `variables` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-28 22:00:33
