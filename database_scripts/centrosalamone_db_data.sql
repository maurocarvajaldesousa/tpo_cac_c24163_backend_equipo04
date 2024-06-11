-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: centrosalamone_db
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Cementerio',1),(2,'Municipalidad',1),(3,'Cruz',1),(4,'Matadero',1);
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ruta`
--

LOCK TABLES `ruta` WRITE;
/*!40000 ALTER TABLE `ruta` DISABLE KEYS */;
INSERT INTO `ruta` VALUES (1,'Sur',1),(2,'Oeste',1),(3,'Centro',1),(4,'Norte',1);
/*!40000 ALTER TABLE `ruta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `obra`
--

LOCK TABLES `obra` WRITE;
/*!40000 ALTER TABLE `obra` DISABLE KEYS */;
INSERT INTO `obra` VALUES (1,'Cementerio de Saldungaray','1938','TORNQUIST','SALDUNGARAY',-38.089060,-62.216740,'https://maps.app.goo.gl/ACfZ52YgRNcAsrTE6','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_01.png',1,1,1),(2,'Municipalidad de Tornquist','1937','TORNQUIST','TORNQUIST',-38.099880,-62.219960,'https://maps.app.goo.gl/m4wGekTZRnbH9CcP9','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_02.png',1,2,1),(3,'Municipalidad de Carhue','1938','ADOLFO ALSINA','CARHUÉ',-37.177140,-62.711070,'https://maps.app.goo.gl/QrPzLmUz63TAfiK9A','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_03.png',2,2,1),(4,'Cruz de Adolfo Alsina (Arano)','1937','ADOLFO ALSINA','ARANO',-37.048730,-63.282970,'https://maps.app.goo.gl/5ETgXh8cYx1Fvvux6','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_04.png',2,3,1),(5,'Matadero de Villa Epecuén','1938','ADOLFO ALSINA','VILLA EPECUÉN',-37.144830,-62.783200,'https://maps.app.goo.gl/KF1NenFeo6L3XEjQ9','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_05.png',2,4,1),(6,'Cruz de Villa Epecuén','1938','ADOLFO ALSINA','VILLA EPECUÉN',-37.129750,-62.804460,'https://maps.app.goo.gl/YgBdC3FDYrqcfLMz6','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_06.png',2,3,1),(7,'Matadero de Guaminí','1937','GUAMINÍ','GUAMINÍ',-37.012480,-62.377510,'https://maps.app.goo.gl/7XjdjF4WL3r4hR2AA','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_07.png',2,4,1),(8,'Municipalidad de Guaminí','1937','GUAMINÍ','GUAMINÍ',-37.010550,-62.422190,'https://maps.app.goo.gl/6kPnCHKiGs4FUAg77','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_08.png',2,2,1),(9,'Cementerio de Azul','1938','AZUL','AZUL',-36.773190,-59.847270,'https://maps.app.goo.gl/ccHhBgXSPfaXVtPE9','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_09.png',3,1,1),(10,'Municipalidad de Alberti','1937','ALBERTI','ALBERTI',-35.030500,-60.277630,'https://maps.app.goo.gl/EmT3GmGWntTAQiYJ7','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_10.png',4,2,1),(11,'Municipalidad de Adolfo Gonzales Chaves','1939','ADOLFO GONZALES CHAVES','ADOLFO GONZALES CHAVES',-38.032560,-60.097820,'https://maps.app.goo.gl/KYt6ShrDuUfmLqYJA','https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/blob/3fa2bc65ed933bd0d3bd3fa0d08f50f9a4f9b03c/img/obras/obra_11.png',3,2,1);
/*!40000 ALTER TABLE `obra` ENABLE KEYS */;
UNLOCK TABLES;


/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-07 21:17:44