-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: registration
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `new_student`
--

DROP TABLE IF EXISTS `new_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_student` (
  `rno` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `addr` varchar(255) NOT NULL,
  `field` varchar(45) NOT NULL,
  `branch` varchar(45) NOT NULL,
  `phn` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `perc` float NOT NULL,
  `pwd` varchar(255) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rno`),
  KEY `fk_student_principle` (`role`),
  CONSTRAINT `fk_student_principle` FOREIGN KEY (`role`) REFERENCES `principle` (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_student`
--

LOCK TABLES `new_student` WRITE;
/*!40000 ALTER TABLE `new_student` DISABLE KEYS */;
INSERT INTO `new_student` VALUES (1,'Aditya Ashok Kachare','aadityakachare132@gmail.com','Thane','B.Tech','Information Technology Engineering','1234567890','2003-02-27',93,'123','student'),(2,'Shubham','sahiljadhav@gmail.com','Thane','B.Tech','Computer Engineering','8177847299','2023-04-15',96,'123','student'),(3,'Sahil','sahil@gmail.com','Wadala','BSc','Physics','5678906533','2003-02-27',84,'123','student'),(4,'Pranay','pranay@gmail.com','Thane','B.Tech','Computer Engineering','1234567890','2016-02-12',85,'123','student'),(5,'Swayam Thanekar','el.17.swayam.thanekar@gmail.com','123 Main Street','B.Tech','Computer Engineering','8472849583','2003-02-04',75,'123',NULL),(6,'Ayush Acharekar','ayush5acharekar@gmail.com','Dadar West 400028','BSc','Information Technology','7355608892','2002-09-05',75,'123',NULL),(7,'Shubham Powale','spowale16@gmail.com','Thane','B.Tech','Information Technology Engineering','9987017427','2003-02-15',92,'123',NULL),(8,'Shubham','shubhampowale3@gmail.com','123','M.Tech','Computer Engineering','9987017427','2023-05-10',89,'123',NULL),(9,'Aarav Kale','aaravdemo@gmail.com','123 Pune','B.Tech','Electrical Engineering','1234567890','2023-05-01',76,'123',NULL),(10,'Aditya','aadityakachare132@gmail.com','Thane','B.Tech','Information Technology Engineering','8923829292','2003-02-27',93,'123',NULL);
/*!40000 ALTER TABLE `new_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_teacher`
--

DROP TABLE IF EXISTS `new_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_teacher` (
  `eid` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `addr` varchar(255) NOT NULL,
  `field` varchar(255) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `phn` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `qual` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`eid`),
  KEY `fk_teacher_principle` (`role`),
  CONSTRAINT `fk_teacher_principle` FOREIGN KEY (`role`) REFERENCES `principle` (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_teacher`
--

LOCK TABLES `new_teacher` WRITE;
/*!40000 ALTER TABLE `new_teacher` DISABLE KEYS */;
INSERT INTO `new_teacher` VALUES (1,'Lily','lily@gmail.com','lily 123','B.Tech','Computer Engineering','1234568902','2023-05-03','M.Tech','lily@123',NULL),(2,'Shubham Powale','spowale16@gmail.com','123','B.Tech','Electronics and Telecommunication Engineering','9987017427','2023-05-04','M.E.','123',NULL);
/*!40000 ALTER TABLE `new_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `principle`
--

DROP TABLE IF EXISTS `principle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `principle` (
  `eid` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `addr` varchar(255) DEFAULT NULL,
  `phn` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `pwd` varchar(255) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`eid`),
  KEY `idx_principle_role` (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `principle`
--

LOCK TABLES `principle` WRITE;
/*!40000 ALTER TABLE `principle` DISABLE KEYS */;
INSERT INTO `principle` VALUES (1,'Ben Dover','ben@spark.com','Main Street','8472849582','1999-01-07','principal@spark','principal'),(2,'John Doe','johndoe@example.com','123 Main Street','555-1234','1980-05-15','password123','student'),(3,'John Doe','johndoe@example.com','123 Main Street','555-1234','1980-05-15','password123','teacher');
/*!40000 ALTER TABLE `principle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sleave`
--

DROP TABLE IF EXISTS `sleave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sleave` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `duration` varchar(255) DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sleave`
--

LOCK TABLES `sleave` WRITE;
/*!40000 ALTER TABLE `sleave` DISABLE KEYS */;
INSERT INTO `sleave` VALUES (1,'Pranay','pranay@gmail.com','2023-05-03','Full Day','Test'),(2,'Shubham Powale','spowale16@gmail.com','2023-05-10','Full Day','Test'),(3,'Shubham Powale','spowale16@gmail.com','2023-05-04','Half Day','sick leave'),(4,'Aarav Kolhe','demonslayer0700@gmail.com','2023-05-16','Half Day','test');
/*!40000 ALTER TABLE `sleave` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tleave`
--

DROP TABLE IF EXISTS `tleave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tleave` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `duration` varchar(255) DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tleave`
--

LOCK TABLES `tleave` WRITE;
/*!40000 ALTER TABLE `tleave` DISABLE KEYS */;
INSERT INTO `tleave` VALUES (1,'Lily','lily@gmail.com','2023-05-11','Full Day','sick leave'),(2,'Shubham Powale','spowale16@gmail.com','2023-05-16','Full Day','Family function');
/*!40000 ALTER TABLE `tleave` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-04 22:39:19
