CREATE DATABASE  IF NOT EXISTS `erp_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `erp_db`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: erp_db
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `accountbook`
--

DROP TABLE IF EXISTS `accountbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountbook` (
  `bk_id` varchar(15) NOT NULL,
  `bk_date` date NOT NULL,
  `bk_type` varchar(4) NOT NULL,
  `bk_description` varchar(100) DEFAULT NULL,
  `bk_amount` bigint NOT NULL,
  `bk_create_date` date DEFAULT NULL,
  `bk_creater` varchar(20) DEFAULT NULL,
  `bk_approval_state` varchar(4) DEFAULT '미결',
  `bk_approval_date` date DEFAULT NULL,
  `bk_approval_p` varchar(20) DEFAULT NULL,
  `employee_code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountbook`
--

LOCK TABLES `accountbook` WRITE;
/*!40000 ALTER TABLE `accountbook` DISABLE KEYS */;
INSERT INTO `accountbook` VALUES ('20250317030001','2025-03-17','대체전표','회사 시작',10000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL),('20250317030002','2025-03-17','대체전표','현금 계좌에 입금',4000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL),('20250325030001','2025-03-25','대체전표','직원 급여 분개',3000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL),('20250325030002','2025-03-25','대체전표','직원 급여 보통예금 계좌에서 지급',3000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL);
/*!40000 ALTER TABLE `accountbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accountsubject`
--

DROP TABLE IF EXISTS `accountsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountsubject` (
  `account_code` int NOT NULL,
  `account_name` varchar(45) NOT NULL,
  `account_type` varchar(20) NOT NULL,
  PRIMARY KEY (`account_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountsubject`
--

LOCK TABLES `accountsubject` WRITE;
/*!40000 ALTER TABLE `accountsubject` DISABLE KEYS */;
INSERT INTO `accountsubject` VALUES (101,'현금','자산'),(103,'보통예금','자산'),(107,'유가증권','자산'),(108,'외상매출금','자산'),(110,'받을어음','자산'),(114,'단기대여금','자산'),(120,'미수금','자산'),(131,'선급금','자산'),(135,'부가세대급금','자산'),(146,'상품','자산'),(150,'제품','자산'),(153,'원재료','자산'),(212,'비품','자산'),(239,'개발비','자산'),(253,'미지급금','부채'),(254,'예수금','부채'),(255,'부가세예수금','부채'),(259,'선수금','부채'),(262,'미지급비용','부채'),(263,'선수수익','부채'),(331,'자본금','자본'),(401,'상품매출','수익'),(404,'제품매출','수익'),(451,'상품매출원가','비용'),(455,'제품매출원가','비용'),(501,'재료비','비용'),(503,'급여(제조)','비용'),(504,'임금(제조)','비용'),(505,'상여금(제조)','비용'),(507,'잡급(제조)','비용'),(510,'퇴직급여','비용'),(511,'경비(제조)','비용'),(801,'급여','비용'),(803,'상여금','비용'),(811,'경비','비용'),(813,'세금과공과금','비용'),(901,'이자수익','수익'),(930,'잡이익','수익'),(999,'테스트용','자산');
/*!40000 ALTER TABLE `accountsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analysis_report`
--

DROP TABLE IF EXISTS `analysis_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analysis_report` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `analysis_reportcol` varchar(45) DEFAULT NULL,
  `estimated_cost` bigint NOT NULL,
  `actual_cost` bigint NOT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analysis_report`
--

LOCK TABLES `analysis_report` WRITE;
/*!40000 ALTER TABLE `analysis_report` DISABLE KEYS */;
INSERT INTO `analysis_report` VALUES (11,'원재료',1000000,1200000),(12,'급여',15000000,12000000),(13,'원재료',1300000,900000),(14,'경비',2000000,2600000);
/*!40000 ALTER TABLE `analysis_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `approval`
--

DROP TABLE IF EXISTS `approval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `approval` (
  `appr_id` int NOT NULL AUTO_INCREMENT,
  `appr_state` int NOT NULL,
  `appr_line1` tinyint NOT NULL,
  `appr_line2` tinyint NOT NULL,
  `appr_line3` tinyint NOT NULL,
  `employee_code` varchar(20) NOT NULL,
  `appr_type` varchar(30) NOT NULL,
  `appr_content` varchar(200) DEFAULT NULL,
  `appr_deny` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`appr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `approval`
--

LOCK TABLES `approval` WRITE;
/*!40000 ALTER TABLE `approval` DISABLE KEYS */;
/*!40000 ALTER TABLE `approval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bom`
--

DROP TABLE IF EXISTS `bom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom` (
  `bom_code` varchar(255) NOT NULL,
  `sop_code` varchar(255) DEFAULT NULL,
  `written_date` varchar(255) DEFAULT NULL,
  `order_code` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`bom_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('BOM1','SOP1','2025-03-11','ORD001','PRD001','완제품1'),('BOM2','SOP2','2025-03-12','ORD002','PRD002','완제품2'),('BOM3','SOP3','2025-03-12','ORD003','PRD003','완제품3');
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bom_f`
--

DROP TABLE IF EXISTS `bom_f`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom_f` (
  `bom_code` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `unit` varchar(255) DEFAULT NULL,
  `purchase_price` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom_f`
--

LOCK TABLES `bom_f` WRITE;
/*!40000 ALTER TABLE `bom_f` DISABLE KEYS */;
INSERT INTO `bom_f` VALUES ('BOM1','MAT001','원자재1','4','EA','200'),('BOM1','MAT002','원자재2','1','EA','20000'),('BOM2','MAT003','원자재3','4','EA','20000'),('BOM2','MAT005','원자재5','5','EA','20000'),('BOM3','MAT001','원자재1','4','EA','200'),('BOM3','MAT002','원자재2','1','EA','20000');
/*!40000 ALTER TABLE `bom_f` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_messages`
--

DROP TABLE IF EXISTS `chat_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_messages` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `room_id` int NOT NULL,
  `sender_id` varchar(50) NOT NULL,
  `sender_name` varchar(100) DEFAULT NULL,
  `message` text NOT NULL,
  `send_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`message_id`),
  KEY `room_id` (`room_id`),
  CONSTRAINT `chat_messages_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `chat_rooms` (`room_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=283 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_messages`
--

LOCK TABLES `chat_messages` WRITE;
/*!40000 ALTER TABLE `chat_messages` DISABLE KEYS */;
INSERT INTO `chat_messages` VALUES (112,16,'e006','육육름','ㅎㅇ','2025-03-19 14:21:16'),(113,16,'e006','육육름','ㅎㅇ','2025-03-19 14:21:17'),(114,16,'e006','육육름','ㅎㅇ','2025-03-19 14:21:19'),(115,16,'e006','육육름','ㅎㅇ','2025-03-19 14:21:20'),(116,16,'e006','육육름','ㅎㅇ','2025-03-19 14:21:22'),(117,16,'e006','육육름','ㅎㅇ','2025-03-19 14:21:23'),(118,16,'e006','육육름','ㅎㅇ','2025-03-19 14:22:42'),(119,16,'e006','육육름','gd','2025-03-19 14:23:19'),(120,16,'e006','육육름','h','2025-03-19 14:25:36'),(121,16,'e006','육육름','asd','2025-03-19 15:34:12'),(122,16,'e006','육육름','asdㅁㄴㅇ','2025-03-19 15:34:13'),(123,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:14'),(124,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:14'),(125,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:15'),(126,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:15'),(127,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:15'),(128,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:16'),(129,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:16'),(130,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:16'),(131,16,'e006','육육름','ㅁㄴㅇ','2025-03-19 15:34:17'),(132,16,'e006','육육름','ㅁ','2025-03-19 15:34:17'),(133,16,'e006','육육름','ㅁ','2025-03-19 15:34:18'),(134,16,'e006','육육름','ㅁ','2025-03-19 15:34:18'),(135,16,'e006','육육름','ㅁ','2025-03-19 15:34:18'),(136,16,'e006','육육름','ㅁ','2025-03-19 15:34:18'),(137,16,'e006','육육름','ㅁ','2025-03-19 15:34:18'),(138,17,'e222','이회계','ㅁㅁㅁㅁ','2025-03-19 15:43:15'),(139,17,'e222','이회계','ㅁㅁㅁㅁ','2025-03-19 15:43:17'),(140,17,'e222','이회계','ㄴㅁㄻㄴㄹㄴㅁ','2025-03-19 15:43:23'),(141,17,'e222','이회계','ㄴㄻㄴㄹㄴㅁㅇㄹ','2025-03-19 15:43:24'),(142,17,'e006','육육름','sdfdsfsfsdf','2025-03-19 15:43:27'),(143,17,'e222','이회계','ㄴㅇㄹㄴㅇㄹㄴㅇㄹㄴㅇ','2025-03-19 15:43:32'),(144,17,'e006','육육름','dgdfgfdgdfgdf','2025-03-19 15:43:35'),(145,17,'e222','이회계','ㅁㅁㅁㅁㅁ','2025-03-19 15:45:10'),(146,17,'e222','이회계','ㅁㅁㅁㅁㅁ','2025-03-19 15:45:13'),(147,17,'e006','육육름','aaaaaa','2025-03-19 15:45:16'),(148,17,'e006','육육름','aaaaaa','2025-03-19 15:45:18'),(149,17,'e222','이회계','ㅁㅁㅁㅁㅁㅁ','2025-03-19 15:45:21'),(150,17,'e222','이회계','sdgfsdfgsfdg','2025-03-19 15:47:30'),(151,17,'e222','이회계','asdfasfsfdsf','2025-03-19 15:47:49'),(152,17,'e222','이회계','sdfsdfsdf','2025-03-19 15:48:00'),(153,17,'e222','이회계','jkljkljkljk','2025-03-19 15:52:29'),(154,17,'e222','이회계','jklkjljkljk','2025-03-19 15:52:33'),(155,17,'e222','이회계','hjklhjlhjk','2025-03-19 15:52:37'),(156,17,'e006','육육름','fhfhfghfgh+','2025-03-19 15:52:45'),(157,17,'e006','육육름','fghfgh','2025-03-19 15:52:46'),(158,17,'e222','이회계','fghfhfghfgh','2025-03-19 15:52:58'),(159,17,'e222','이회계','fghfghfghfghfg','2025-03-19 15:53:00'),(160,17,'e222','이회계','fdghfhfhgfh','2025-03-19 15:53:03'),(161,17,'e006','육육름','dfgdfgdfgfd','2025-03-19 15:53:08'),(162,17,'e006','육육름','sdgdfgdf','2025-03-19 15:53:12'),(163,17,'e006','육육름','dfgdfgd','2025-03-19 15:53:14'),(164,17,'e006','육육름','asdfasfas','2025-03-19 16:05:29'),(165,17,'e222','이회계','asdfasfsda','2025-03-19 16:05:49'),(166,17,'e222','이회계','asdfasfsda','2025-03-19 16:05:57'),(167,17,'e222','이회계','asdfasdfsadfsdaf','2025-03-19 16:06:06'),(168,17,'e222','이회계','sdfsdfdsfsd','2025-03-19 16:06:15'),(169,17,'e222','이회계','dfgdgdf','2025-03-19 16:07:59'),(170,17,'e222','이회계','dfgdfgdfgfd','2025-03-19 16:08:03'),(171,17,'e222','이회계','123','2025-03-19 16:22:47'),(172,17,'e006','육육름','1234567890','2025-03-19 16:25:41'),(173,17,'e006','육육름','123','2025-03-19 16:29:47'),(174,17,'e222','이회계','제발요 ㅠㅠ','2025-03-19 16:42:52'),(175,17,'e006','육육름','d?','2025-03-19 16:42:57'),(176,17,'e006','육육름','?','2025-03-19 16:42:59'),(177,17,'e006','육육름','ㅇㅇ?','2025-03-19 16:43:01'),(178,17,'e222','이회계','ㅇㅇ','2025-03-19 16:43:03'),(179,17,'e222','이회계','ㅁㄴㅇ','2025-03-19 16:43:05'),(180,17,'e006','육육름','ㅠㅠ 너무슬퍼','2025-03-19 16:45:02'),(181,17,'e222','이회계','왜?','2025-03-19 16:45:37'),(182,17,'e222','이회계','11','2025-03-19 16:47:16'),(183,17,'e222','이회계','12356','2025-03-19 16:47:24'),(184,17,'e006','육육름','1','2025-03-19 16:47:29'),(185,17,'e006','육육름','dddd','2025-03-19 16:49:12'),(186,17,'e006','육육름','aaaa','2025-03-19 16:51:29'),(187,17,'e006','육육름','asdfsdfasfd','2025-03-19 16:58:20'),(188,17,'e222','이회계','sdfsfsdfsdfsd','2025-03-19 16:58:24'),(189,17,'e006','육육름','asdfasfdasdfasdfsdafasfds','2025-03-19 16:58:29'),(190,17,'e222','이회계','sdfsfsdfsdfsdfsd','2025-03-19 16:58:32'),(191,17,'e006','육육름','asdfasdfasdfasdfsadfsda','2025-03-19 16:58:36'),(192,17,'e006','육육름','asdfasfdsdfsdfsdfdsf','2025-03-19 16:58:39'),(193,17,'e006','육육름','asd','2025-03-19 18:00:46'),(194,17,'e006','육육름','sd','2025-03-19 18:00:47'),(195,17,'e006','육육름','asd','2025-03-19 18:00:48'),(196,17,'e006','육육름','asd','2025-03-19 18:00:48'),(197,17,'e006','육육름','asd','2025-03-19 18:00:48'),(198,17,'e006','육육름','asd','2025-03-19 18:00:49'),(199,17,'e006','육육름','asd','2025-03-19 18:00:49'),(200,17,'e006','육육름','asd','2025-03-19 18:00:55'),(201,17,'e006','육육름','asd','2025-03-19 18:00:56'),(202,16,'e006','육육름','gd','2025-03-19 18:57:52'),(203,16,'e006','육육름','d','2025-03-19 18:57:53'),(204,16,'e001','성진하','gd','2025-03-19 18:57:55'),(205,16,'e001','성진하','d','2025-03-19 18:57:56'),(206,16,'e001','성진하','d','2025-03-19 18:57:57'),(207,16,'e001','성진하','ㅇ','2025-03-19 18:57:59'),(208,16,'e001','성진하','ㅇ','2025-03-19 18:57:59'),(209,16,'e001','성진하','ㅇ','2025-03-19 18:57:59'),(210,16,'e001','성진하','ㅇ','2025-03-19 18:57:59'),(211,16,'e001','성진하','ㅇ','2025-03-19 18:57:59'),(212,16,'e001','성진하','ㅇ','2025-03-19 18:58:00'),(213,16,'e001','성진하','ㅇ','2025-03-19 18:58:00'),(214,16,'e001','성진하','ㅇ','2025-03-19 18:58:00'),(215,16,'e001','성진하','ㅇ','2025-03-19 18:58:01'),(216,16,'e001','성진하','ㅇ','2025-03-19 18:58:01'),(217,16,'e001','성진하','ㅇ','2025-03-19 18:58:02'),(218,16,'e001','성진하','ㅇ','2025-03-19 18:58:02'),(219,16,'e006','육육름','d','2025-03-19 18:58:04'),(220,16,'e006','육육름','d','2025-03-19 18:58:05'),(221,16,'e006','육육름','d','2025-03-19 18:58:05'),(222,16,'e006','육육름','d','2025-03-19 18:58:06'),(223,16,'e006','육육름','d','2025-03-19 18:58:06'),(224,16,'e006','육육름','d','2025-03-19 18:58:07'),(225,16,'e006','육육름','d','2025-03-19 18:58:08'),(226,16,'e006','육육름','d','2025-03-19 18:58:09'),(227,16,'e001','성진하','ㅇ','2025-03-19 18:58:11'),(228,16,'e001','성진하','ㅇ','2025-03-19 18:58:11'),(229,16,'e001','성진하','ㅇ','2025-03-19 18:58:12'),(230,16,'e001','성진하','ㅇ','2025-03-19 18:58:12'),(231,16,'e001','성진하','aa','2025-03-19 19:06:13'),(232,16,'e001','성진하','aa','2025-03-19 19:06:23'),(233,16,'e001','성진하','a','2025-03-19 19:06:24'),(234,16,'e001','성진하','zz','2025-03-19 19:06:25'),(235,16,'e001','성진하','z','2025-03-19 19:06:27'),(236,16,'e001','성진하','z','2025-03-19 19:06:27'),(237,16,'e001','성진하','z','2025-03-19 19:06:28'),(238,16,'e001','성진하','z','2025-03-19 19:06:28'),(239,16,'e001','성진하','z','2025-03-19 19:06:28'),(240,16,'e001','성진하','z','2025-03-19 19:06:28'),(241,16,'e001','성진하','z','2025-03-19 19:06:29'),(242,16,'e001','성진하','z','2025-03-19 19:06:29'),(243,16,'e001','성진하','z','2025-03-19 19:06:30'),(244,16,'e001','성진하','z','2025-03-19 19:06:30'),(245,16,'e001','성진하','z','2025-03-19 19:06:30'),(246,16,'e001','성진하','z','2025-03-19 19:06:31'),(247,16,'e001','성진하','z','2025-03-19 19:06:31'),(248,16,'e001','성진하','z','2025-03-19 19:06:32'),(249,16,'e001','성진하','z','2025-03-19 19:06:32'),(250,16,'e001','성진하','z','2025-03-19 19:06:32'),(251,16,'e001','성진하','z','2025-03-19 19:06:33'),(252,16,'e001','성진하','z','2025-03-19 19:06:33'),(253,16,'e001','성진하','z','2025-03-19 19:06:34'),(254,16,'e001','성진하','z','2025-03-19 19:06:34'),(255,16,'e001','성진하','z','2025-03-19 19:06:34'),(256,16,'e001','성진하','z','2025-03-19 19:06:35'),(257,16,'e001','성진하','z','2025-03-19 19:06:35'),(258,16,'e001','성진하','ㅋ','2025-03-19 19:06:36'),(259,16,'e001','성진하','z','2025-03-19 19:15:51'),(260,16,'e001','성진하','z','2025-03-19 19:15:56'),(261,16,'e001','성진하','zz','2025-03-19 19:15:59'),(262,16,'e001','성진하','ㅋㅋ','2025-03-19 19:16:02'),(263,16,'e006','육육름','z','2025-03-19 19:16:04'),(264,16,'e006','육육름','z','2025-03-19 19:16:05'),(265,16,'e006','육육름','z','2025-03-19 19:16:05'),(266,16,'e006','육육름','z','2025-03-19 19:16:05'),(267,16,'e006','육육름','ㅋㅋ','2025-03-19 19:16:06'),(268,16,'e006','육육름','ㅋ','2025-03-19 19:16:06'),(269,16,'e006','육육름','ㅋ','2025-03-19 19:16:07'),(270,16,'e006','육육름','ㅋ','2025-03-19 19:16:07'),(271,16,'e001','성진하','ㅋ','2025-03-19 19:16:10'),(272,16,'e001','성진하','\\ㅋ','2025-03-19 19:16:11'),(273,16,'e001','성진하','ㅋ','2025-03-19 19:16:11'),(274,16,'e001','성진하','ㅋ','2025-03-19 19:16:12'),(275,16,'e001','성진하','ㅋ','2025-03-19 19:16:12'),(276,16,'e001','성진하','ㅋ','2025-03-19 19:16:12'),(277,16,'e001','성진하','ㅋ','2025-03-19 19:16:12'),(278,16,'e001','성진하','ㅋ','2025-03-19 19:16:12'),(279,16,'e001','성진하','ㅋ','2025-03-19 19:16:13'),(280,16,'e001','성진하','ㅋ','2025-03-19 19:16:13'),(281,16,'e001','성진하','ㅋ','2025-03-19 19:16:13'),(282,16,'e001','성진하','ㅋ','2025-03-19 19:16:14');
/*!40000 ALTER TABLE `chat_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_room`
--

DROP TABLE IF EXISTS `chat_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_room` (
  `employee_code` varchar(20) NOT NULL,
  `room_code` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_room`
--

LOCK TABLES `chat_room` WRITE;
/*!40000 ALTER TABLE `chat_room` DISABLE KEYS */;
INSERT INTO `chat_room` VALUES ('e001','r001'),('e002','r001'),('e003','r001'),('e003','r002'),('e004','r002');
/*!40000 ALTER TABLE `chat_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_rooms`
--

DROP TABLE IF EXISTS `chat_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_rooms` (
  `room_id` int NOT NULL AUTO_INCREMENT,
  `room_name` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `members` json DEFAULT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_rooms`
--

LOCK TABLES `chat_rooms` WRITE;
/*!40000 ALTER TABLE `chat_rooms` DISABLE KEYS */;
INSERT INTO `chat_rooms` VALUES (15,'개인톡: 김진범','2025-03-19 14:19:05','[\"9999\"]'),(16,'개인톡: 성진하','2025-03-19 14:19:07','[\"e001\", \"e006\"]'),(17,'단체방: 육육름 (외 1명)','2025-03-19 15:43:08','[\"e222\"]');
/*!40000 ALTER TABLE `chat_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyfile`
--

DROP TABLE IF EXISTS `companyfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyfile` (
  `fiscal_year` varchar(50) NOT NULL,
  `business_registration_number` varchar(20) NOT NULL,
  `corporation_registration_number` int NOT NULL,
  `representative_foreign` tinyint(1) DEFAULT NULL,
  `representative_resident_number` varchar(13) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `detailed_address` varchar(50) DEFAULT NULL,
  `business_type` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `fax_number` varchar(20) DEFAULT NULL,
  `establishment_date` date DEFAULT NULL,
  `closed_date` date DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`fiscal_year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyfile`
--

LOCK TABLES `companyfile` WRITE;
/*!40000 ALTER TABLE `companyfile` DISABLE KEYS */;
/*!40000 ALTER TABLE `companyfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyinformation`
--

DROP TABLE IF EXISTS `companyinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyinformation` (
  `business_registration_number` varchar(20) NOT NULL,
  `fiscal_year` varchar(45) NOT NULL,
  `corporation_registration_number` varchar(20) NOT NULL,
  `representative_foreign` varchar(20) NOT NULL,
  `representative_resident_number` varchar(20) NOT NULL,
  `zip_code` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `detailed_address` varchar(255) NOT NULL,
  `business_type` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `fax_number` varchar(20) NOT NULL,
  `establishment_date` date NOT NULL,
  `closed_date` date NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`business_registration_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyinformation`
--

LOCK TABLES `companyinformation` WRITE;
/*!40000 ALTER TABLE `companyinformation` DISABLE KEYS */;
/*!40000 ALTER TABLE `companyinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyprofile`
--

DROP TABLE IF EXISTS `companyprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyprofile` (
  `FY` varchar(50) NOT NULL,
  `coperationNumber` int DEFAULT NULL,
  `representativeNumber` varchar(50) DEFAULT NULL,
  `proprietor` tinyint(1) DEFAULT NULL,
  `resodentRegistrationNumber` varchar(13) DEFAULT NULL,
  `zipcode` varchar(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `particularAddress` varchar(50) DEFAULT NULL,
  `businessType` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `phoneNumber` varchar(50) DEFAULT NULL,
  `faxNumber` int DEFAULT NULL,
  `establishmentDate` date DEFAULT NULL,
  ` closedDownDate` date DEFAULT NULL,
  `userdOrNot` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`FY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyprofile`
--

LOCK TABLES `companyprofile` WRITE;
/*!40000 ALTER TABLE `companyprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `companyprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_management`
--

DROP TABLE IF EXISTS `customer_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_management` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Customer_name` char(100) DEFAULT NULL,
  `business_number` char(15) DEFAULT NULL,
  `Customer_code` char(100) DEFAULT NULL,
  `Type_business` char(100) DEFAULT NULL,
  `business_adress` char(250) DEFAULT NULL,
  `ContactPerson_name` char(100) DEFAULT NULL,
  `Country` char(50) DEFAULT NULL,
  `ContactPerson_phone` char(100) DEFAULT NULL,
  `e_mail` char(100) DEFAULT NULL,
  `Memo` char(250) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_management`
--

LOCK TABLES `customer_management` WRITE;
/*!40000 ALTER TABLE `customer_management` DISABLE KEYS */;
INSERT INTO `customer_management` VALUES (2,'삼송','123-12-12345','0001','해외매출거래처','대전광역시 유성구','권태희','한국','010-2502-0952','sest@hanmail.net','잘생김'),(3,'헬지','123-12-15564','0002','해외매출거래처','대전광역시 동구','은지원','일본','010-2502-0952','sest@hanmail.net','부자임'),(4,'삼송','123-58-18866','0003','국내매출거래처','대전광역시 유성구','성진하','미국','010-2629-5468','wlsgkWkd@naver.com','차은우'),(5,'상심당','158-18-81116','0004','국내매출거래처','대전광역시 유성구','김동현','한국','010-4861-8721','ehdgus@naver.com','이종격투기선수아님'),(6,'파인애플','158-87-81047','0005','해외매입거래처','대전광역시 서구','송기윤','중국','010-5418-8971','rldbs@hanmail.net','씨름선수출신'),(7,'육뚜기','156-88-54889','0006','국내매출거래처','대전광역시 동구','양승준','일본','010-5848-1058','tmdwns@naver.com','메이플로 돈벌고있음'),(8,'구팡','058-98-87451','0007','국내매입거래처','대전광역시 서구','최정윤','중국','010-8486-1584','wjddbs@hanmail.net','내뽀또먹음'),(9,'마이크로소프트콘','156-84-85498','0008','해외매입거래처','대전광역시 서구','박민환','일본','010-5874-8715','alsghks@naver.com','말이많음'),(10,'삼송','848-04-14568','0009','국내매입거래처','대전광역시 유성구','김태연','한국','010-5846-6879','xodus@hanmail.net','나에게 하리보를 줌');
/*!40000 ALTER TABLE `customer_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_code` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `name_eng` varchar(50) DEFAULT NULL,
  `name_hanja` varchar(50) DEFAULT NULL,
  `e_mail` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `detail_address` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `emergency_number` varchar(20) DEFAULT NULL,
  `date_of_employment` date DEFAULT NULL,
  `date_of_retirement` date DEFAULT NULL,
  `employment_status` varchar(20) DEFAULT NULL,
  `employment_type` varchar(20) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `job_grade` varchar(50) DEFAULT NULL,
  `work_place` varchar(50) DEFAULT NULL,
  `basic_salary` int DEFAULT NULL,
  `allowance` int DEFAULT NULL,
  `bonus` int DEFAULT NULL,
  `account` varchar(50) DEFAULT NULL,
  `this_month_state` varchar(20) DEFAULT NULL,
  `pic` longblob,
  PRIMARY KEY (`employee_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('9999','김진범','kimjinbim','ㅎㅁㄴ','1@gmail.com','12345','아ㅜㅁㄱ','ㅓ나','010-1',NULL,'2025-03-19',NULL,'재직','인턴','인사부','사원','1',100,123,123,'0',NULL,_binary 'aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUl3QUFBQzBDQVlBQUFCRzZjVCtBQUJEUWtsRVFWUjRu\nTzI5Q1poa1YzVW0rSjl6MzRzbE0ydFhMYXBWRWdVU0pmWVNVcFVRcm5ZREJyZVJsLzRzMmJTbk1Y\nUjdMR3hMNEdYY3l6ZTRpK3FlenpNTVE3ZEZTY0pnZXNEdXB1Mld2SU14RERhMkd0QUc1VGFTVllB\na0pOV21LdFdlbFZ0RXZIZnZtZS9jK3lMaVJXUkVaa1JXWkZZV3l2TXBWSkV2NHI1NzQ3M3p6ajNM\nZjg2aExUZmYvVElBRUdkbzB0bVRxd3NvVmxLelFvOFJ5K1NSaCs1NkFmM1FaMjlaaFkxbURELzRZ\nTnJ0SzV0M2ZiUU1GSjh3VWVsbDFsWis5K2pEZDc2bnJ6bVc2SkpSQk1kZjBUZkVNUTJKL0t1cXhl\ndUpvM2NCSWlMdUVRQS8xZE9aZnU5dHd5aE0vUVlFUDRSVGsvOEV3SW41WHZ3U0xUeEZ4TkZXZlVN\nY0liVzE1UURXR1k2MkFBSnJxMGQ2T3N1bjk1UlFtUG8wU3RGdG1FeW5BR1BtZStGTGRHa29Fckho\nblZnUXdSRmd3ekVCQVYyM2xSWXFwLzhXaGVnMlZQMjVhdk82NGlXNnBCUmQ5QmsrZTh0T0FMK094\nQTFrUVV1MHVJa0hjSTUvaDVqTGNES0FVeTNSOXpmRC9KYzM3VUpFUDd3a1hWNDZkSEVNWS9DTGlD\nakdrbkI1eWREY0dlYitOMjBGMFk4aVhaSXVMeVdhTzhPazlPTW84Z29zOGN0TGl1YkdNSHQxbk55\nK3hDd3ZQWm9idzF4L3kzVWd2SEZwTzNycDBkd1l4dUlkS0pyQ2tyTDcwcVArSFhmcUFQNEQrWkg1\nMm82MjNYVHZLeDI1M3laVGhDUzEvM2prc1R2L2JINW1XcUlaYWEvd2xpL2QreW1PaWkrVGRPcC9I\nbjdrL2I4OE40YjVyemR1Z3NGTzJMbHp6TkZIZnEyeVpmZCtMNStvRVpzSWxBcXRNRkhoQjRoak9K\nUGVuLzlzMjU1UGw2UTJmcXNGbFVBNVQ2RURHNkt6aHg4Ky9RVmczN1NGcmQ5OTM3b0k3dTB0WTNM\nRXpyQWplL1RZdysvM2dkZzZiWHpqL2pVVXl3OTMreDNzREtmaWpoOS85SzR2dDZ6enRmOXBwUzNI\nUHlKTUdtbHBHME1HUXQ4Nzh1aWRYMnMvMzdVM2YyclpoRlRlS1VTbWZad25pWWdwdWJCcjA1V2Zm\nK0NCMnh0ZjJIclRmVHNGN3RYT3VBNmhIQU5qcW45OStLdS9lcngrWlBzN3ZsQ3NqVDU3cXdYSzdk\nZEUxMWR6eGYveDRqNDhqMTNZVFZ5NHprbTFFUnZzbjJGTVlSY0t0QUpKdi91UjBOYmQ5KzBXaXhF\nQ1lpZHVXTVJCaURadjNYWGZXeDFjNUdKNjB0U1FpRXVVbGFZeGs2bE5MVStBKzVob0RZU2FIMmdR\nREZUZHZHdk5ucU9QNExIMm1RdVVYZ3Z3NzdhTXlSRVpBM2J1aXdCYUdJWWp2b2JFL1o2dVJVVnJP\nNUZoUk03OUxZQVdockhsYUF1UmZKcEVyMi9ybk1vTGp1eXhWK3o1eE91ZmV2Q08wL25QeG0yeWdS\nbi9tVVJLN2VQQ1dNVVEwTk9Qblp6NGtsY01NaElqN3lLS2Y0MWRiZG9pTmFqc0V2a1lnRjl1ekRQ\nKzlQSlkrRDVtdnFMOW1wQ0pVZVRrM1FBOUI5eFQ5ZmVDcERaM0hZYndGci95UG1ubnprOUdEdTZU\nWk9pTHd2TG5SSFNsdUpwZWxyY0ozQmVaNDcrTXJQdHh4N1hxTEF0Z2dLbjFSY1NtVUNLaHQzVWYx\nejZtN1NWNjNqbU1RNWR4L256VHZ5LzZBY1diSnlyVk4zWWMxbVhjVFBPSk9CM1RaYTFDSUx4dCsv\nYTdpN05meC9xMTZQSms5YzB3bjlnWkEzTHpuT05HUWdiRXBQYzN2M0wvMkJGRHBLZjFTSGphMjE0\naStsdGZQK093bVY2a0o1akRPSFJWL2FYN1hBeU82SFZkaGtuLzgxSFhNZUtzUHBUYnh0Y09iK2g5\nbnU3VUg4T1V5bGREOElvNUs3eitwblJhVkRpbW05QWN6NnlRUVQzRk5kaTdkeEFCMVhrbmNYVHRB\nczJrdDNrNHBwckhQVjBzOVhkeEMzSURpcWEwR0NQVEFxZVhadjIydjEycElMQkZUazZmK29IY3dG\nNkkySUNjdXdRTUE3cTVneTYyT0VnRVJMSUNGYXpFWWljUjNTelc3ZHo1aVhoaEpsU2p3RzFhV0lZ\nSjRZQWJPbGw3aTRhRXlvbUpGejNEU0VBenJqeTNDa01MTmlsaC9jSXl6R3ZlckJOZXV4aTNvMENx\nOURMSG9GVzRERWhBdzhta0dWNjRHZW1LaFdXWUtsNEo1cFdMbDJHOGNhMmF6T0xYWWNRcithVTRT\naGFJWWJ5dDRWT0hGbzVoeUwwQjhXSlZZT3JrSFhqTGNCa1FDZUpxSlZtNExRa1lHY1JKZXZmMENu\nWXUvbUFqcWNkMklCZG1ma204NlJMRlZGNm8rUWcwdEhBUzVtLzJxSXY3VlpjRi9vVVg2aVpjSkhs\ndnVTMWhJU2o0KzBwQjExNEloams2dFFHRXJZdFpmMm1Rb00wRnZqaUpkUHNVTGl6TWJQNit4ZmhI\nZTgzQ01Fd1Vid2ZUOHA0WWhoREJhRDdjcFNFUldhQ2JjTEdrZm0yM1lHc1ZVTFRqMVBVWDdRWHY5\nUVN2bWxYaDlYRXIvKzV4V0o3RUpTTHkwSURMZ0VqZFJndTNWaUl4dGEzSGFXR1VYcUpYei9pNUQ2\nTEtPQkw4S3FybUFiejNhK2N4VHlRS0Nwa1dzTTJDai81dDkwaHJVM2RvKzRvR1BqSDk1b2tUNWtn\ndjBYUjRnN2p1SGt3UlM2UUQvVHFsazBrOTR4THJhMnIvbmNwZmtxYlRwUktCL1Z5ZEF1Y2FZOHUr\nbEV3dDczQnRmTEMvWlY2UjduQ0VhRmFYWkpoMEJ6U0NQdE0zRS9jcitKbUhQalh6K1lnNjNyQnM0\nUnI2bjJsNFZEQ3VWck5IeGJtSitvVWdEV2dLbG9PNGJrN1BjQTVTSmpoUDVDWmFMNHBUUk0ycDlt\nK2JnanZwVXZzWkR4Rm9DWXdLRWVSV0lGN2RjWjJReElrY0VYRW16eHc2U0VUV0VMRlhka1U2Yjkz\nZW4rVFN2M2V3ZjBmRXVRdnZtRUhIRDQzWDJybjF2RGgzWEZ5cnprQ1FDRVJyNi9MTVZzKzJQeW1x\nZUU5Q2NLNTVQUndScFpOemxUQ0N2MWs3Z2hOMEZXeVhwNkxBUU1YKzBhek1FaTVZVldBVERicFBu\neW5WVFMrZDZkbDc2aCs5Y0hickg2OS9zeHVlYXZ6d0lWcVJUTXJVenhCRkg1OWxkaCtFRTJjL09F\nU0YzNXVRMFVZY1Ixd1J3enlrcUswV092elY5ejhINEwyZHpyWjU5ejBIbUhoMXAvWGV1SFhUVXc4\nZk9USU52bEMwVVZveDVzUEUwZnRtbERJY2FYR0VQejcyOEozL0FUMlFyY1lmTVRIdFYrOXFuY3dV\nTzRtTHExMXN2MDdFR3pxQ0loUmNaZFA3aDZuOC92cjEwR3V4N01MWmNhQnoxSDlHaGlITEZwTlhi\nUVN3dGlIeVczNFlnTVJOZ1BDaDJYN1VnUU4zcEZ0dTN2OVAySm9DOFhUdWMybkM1V2pvOUlSVXIr\ndDZNZmZ0YzRlQmMrMkh0OTE0OTk4N1NrR3pHaDJxYU5yeDd6NzhjMk80S05ycjVYYTNUelA0NU5s\nT24yM1pkZSszdWlINFdxZzNiSkNuNHdmdVVJblFTU3FjMzdMcm5pTlFodWxpcVFGUytlNURIYTdI\nYmZjYkhEblpwNFRSdTFEbGx5SGlZc2RuUC9iUzVYNzhzNjgvaWRsSmVxbG10WG5YeHduVVg0UlRV\nTGdna3FiVWkwNDJ3LzY4TU1SbmU5SmhCa1FDbkErTTBZMzZ1eDR6YzdHUUlESFh3WFRXbFpDSUFq\nNC9nVXRNam0yTmlLWnRLWXVTSkswc0pNTUFyanJJSjJSbWhnbjY2WFVkZjU5aExUMzBEYnpyYTkr\nWXk4UnI5OXd6c25uWC9wbXRyeDRwYkhHWGdWTVIzZ2haWUg5NW4rSjZ6Z3lqdHlDeVJUaHM3NnEv\nQUgvZzQzMTErdDIzck1FZjNQSmVmSHJQckppVVl0WDlHK2I0UWMxRG12UHFsMmpCYVVZSjQ0cSs1\ndDMwa0lCS25xcWJCTGt2Tkk3OS9wdTNvRkQ5RWtRK2ptaHF4Z0RndHRkK2VpVVJ2WWRNWVpWanVR\nd3JhTzV6YXMvUDd4emRRT21YbHJvcmlVNWdoNnJyQUV5djBCQXhVSE9QNGFjZmVoYnYwdElmdHhX\nUXZ2QTdHSXAyWXRLT29zZ3ovbGczUEhrakVHM1NOQk1CL1JCMmZ1S0RPSERINHROQmJydmZyRG4y\nM0xRb3I2dUtXa256NjZVVktxMS96VWVHMDVHbUEwelNFaFZ0S2Myc29zWEdNSUFkbmxSekxKcW1I\nbmpkeG4zQis5cVU3UEgzb0dqZWptcVAyN056YjlhRUtVMlNJc2kxbStOazIxSGdHU3d5Mm5yOHpM\nVWl3NStlOWtIc2MzMWUzcFpuTnpEeTE0WGwzZkZRNlFjTHVYd3BpZzFaVTNzY3dNOWgwVEdNQU9t\nS3FRS012bW43TEhHcHV2VDgreis5ZVJrbTVkZjdVZVdFOEliQWE2TE9vN0wzSkM5Q2huRXBSdGhF\nTjNZUERjajg3VVprTmpIenBuWkhHOXZlQ3B2T0Y4Mmc5QkxTbGVPdEhuRWxOYkVGenlGeXdmZFNr\nWjlFd1d6dnRmU0hWZ0VuNEJWTlo2K1B0M1MwbGdTNHROc1VPUkY5TmpxOE1OOVdtYVlSZDVyN1Vs\nd1R6ZUdaVmNLd0lGMHhIc0lvZVlwOEpkK0hjZnNqVTdqL05vUGtoWjlEMVB2RlM2bTRMaGJaMEZ5\nRG1tTjJ4N1ExcXJnWDkyT2JkOTI3Q1hCUEhIM2tyai9wZVpJbEdoaHAvanNJMTJ6ZWZjOEhaMkFZ\nZ3JDRFhhWU0wMzRHN3dIK3FuL3ZUcndXRWIyeHgvTFBuZ3FnVGNJMDBqeXZNZ3hkTlgybFRwUGti\nMlV1M0dwdDViOERXR0tZUzBHZVlmaHFKdlp4clM2SjVJQXJwTEREVTYwU1J0L1dWQ09UVUNIQnVY\nK0ttT04rTEVBSDJVYWtmTnFBSStnVUc5VWk2TFJZbFRUVGFtWXMwUUtUK1B1Z3I0NE1RMEp3cFJw\nY3VkcktNSXA3QVk0Z1NwLzJpZmxFUDlJMWl0MkZOREU4ajBEUXJZbEFxNlBTaXNzaW4raWxUbDBs\nakIydVFPSzBnOElyajN2OVpkV3cxcm03dnY5bm56Wk54ejdKc0VTMWdTUmFMZEg4VXJmYUpyQWpr\nNEN4MDdjazVtdzdrcmVnME45MkZNN3ROcllxUmdMbXlKalVxcE53aVJZNWRUR3JDWGJaaE5hdmFq\nMnNFQWVtYi9yM0ltK2RpMlVwd0xwcG1yUkc1Q2hhWXBqTGdMcjZZZExsYmQ1bmxTNnBHd2RxQjcy\nelRtUm52L29MdEZvQllkVjBSbE5RcWx0aW1NdVdZVWpDbHBUZmpyeitRb2Z3NUNQSE1VR3ZCZFA2\nZnZPVXJpMmFFZ21XNS94QURSS0NZaytYNkxKakdFY1E0Nll6ak04TXdFSHM4M2Y3RmhTMEZscC9r\nMVdTeWpDSU9pYWdNMU5IUVBVU1hRWVNScTBqVzFZZkROb1VYbms4US9YdG1vdis0bUtyekZLZXJp\naUxDcXZNckY1OFFlc2xtbEhDTUZ3eGdTc2xyUkltN0NMZjhubldoRmYzcmIvb0tXdzBqRzZaaVNJ\nREtVY3hHd25Qa3JlMFJEUFN0TkFBQ3lNcFZ5RnhqbUhxSHQ3SWZoc242Qm9Gdjg4bHo5cVFYU1pz\nVENjSlEvTmVwaVBNeVpwalBHZWlUbi9QRXdOMndsSDdZNWUwNkdQVUVRY3pWQUdNOC9wTWM2RnlF\nc2RYSHNINjhSOUZ4UEZjdXJBSnk3RGFRK0s5ZlZuR1hhaCtxZjhGb0JJcG5tTCtJc0hpNWxnblJi\nUkl1WStJTnUra1MzV3g4OUlVVlNBSzNxNjJwTE5ZeXlDTTR4SlNoK0NqT3UybWdnOUdFL2ZxRnBK\nMWgvQ0JMMWJ4KzIrNllhNDhMbzZIS2NBalZHdEp5T0VjaUwxZmhnaGFwb09DRG5QeHZVczdrdGZE\nc0tIdllUN2hxL3BodHZMZk5IeGFKMmVxYkp3TS9BWXF1TXdsdFU4NkovZEFOSHNtVUJ3TEZkaGRN\nclFkT3Q0WkRRdW9oWlRId1FRR2Vjci9uK2gxYzhXOU04dHdJd1BSMm04QzlIOEMwT1lUeWtXbEhU\ndjJ4bU1xWWVZTGx4VHlvZCsrWmRmK1oxdU9rOExFNVBsakQ3Ly9MenFQVklBZEh6bjgySjBIZTVs\nbjg2NlByaVlVYi9QcHFSWVBjR1J1RU9CYWcrU2JUaWlkL1huem1VUW5qMzNqcm5ETmU2UWRPL1lX\nUmxlcy9Ta2lXaWxpbjJ6dm5UQS9ES1A1cWo1SzNYWmM1S0RIdjlnWFhqN1hPakhXY3Rrb25nWXF1\nZEp2cEVuODE2YVFuQ2JRV2hFVXprUWpjWXRHN0F1RVI0QkxCbE9lMUVNcStUVWd0S1RWYWlsRnNU\nV3QzLzhYTTZSb1JiMVBWTkI0MlcvN2l0L0dmUjBpdnhERnd6L20wckY3bVBDblBaMkMvRVhxaXly\nbGpXV1M1UDh5cHJUUnBsUC90YjEzd3R3cFBPUktMY3l1ZnpoV3A5MVVxOUtsRW9YTVFlQ0ZUUkJz\nbkhOaElmYmJUbGlDMEhjOG1GbHdWUGNqSW9wTEZNVmtWUzBJaTRSTEQ0dE5Ecmk2ZEpzcjJUd292\nZHZhQjU0dUpQTjQ3aGtvQjB3YkNIazljOHk1NUlDKzJwNGFBeGVuY09WS3E0V2tHRjdDMDdCOEhX\nSXF6clVUbXlGWGFvQ2pXSTVrcHo4RzR0Y0xFTlZXRGtWeFZUdHlLRWRIaW9MNUQ0Y2ZldCtuTHZv\nbnMySXQ4MGM2b01JR256WWk5WXNZU3VMcjZlYzdOY1hYeDZrYkRRT1pLeFF3d0dOSEg3N3JyZnIz\nOU8yMFVJTjRIRXhqQlRyM2Vhd3VId1BrVmYwTHlpWTU0V0tvZVpHS2RSVEtheEJlOVArSVJQSDRS\nTnhlQ3dZRElPdThkWE54Rm5BZnlmR0RJRkp6Y3ZGUVl5MnRpN0pxVWxmaENqa2ZqTWRvMHdtOC9j\nc1RFTHo2WXZpV01xZWRRSktJM1dnNGh0QXppSWhUS2tia3plckJraUhOQWIrSXhMQlEwNmFFQlNY\ndG1iVDRxSlZobkVFeU1nbW5UcnZHTjN3dG5VUGhEN21vU3VERUhJVktBbFJKRWpPaHh5ekVNNDVB\nVEd4VXN4cDhhRUNiakVsdy9zeWR5QzB3SXBBWEpRS3hWZVJiaGxzK0JVUXFhbkk2RFBDOUFNbkVs\naGtsalBwWW5CUzdGVVVVNTJKZldRdFNLOFZUdnZxTlFjTVJSYzdVek13NWszTWpjYlVxa1ZINDRO\neTJPTlc1d05kZHVmTVRRMjcxaGR4dlc0OTQ3SlE3K3NpdnFaVXdPUElwT1BKeUxWakFoU2xwbmEv\na2pqNXkrMkRuNjRPbVhVQk5MZEdNZ1pibjBlRnBMQi9hQUxpMVhTV01wczhtN2hCRS9qM3MrUFJL\nTkg1bkMrVzNSQ2hKbzJFdlNod3d4ZHFKUklpY0t6RHpQRGhPaGFiQVZBTlJhUzQ3VSthL2VVY1VK\nNDlpckZrR21HaUNISXIvQU9DbkI3cGNwNEJyN0M3VzVCR3FsaHNMSmhvbm9kRkRPMjY3L3ljT1Bu\nRDd2SGlZKzJJWVl3MlMxV00rSjZsQnlpQ0dud1p3TlppTEhZT091bTA1ZVJHSi9CamUvZlZ2ZFoz\nTjEzenpFc1lXYW9tL0M0UTZod2lKRVliM29RM3M5NFV6QzArUlNBV0V2dm9Ra0RiUTFCbzVvY1pk\nbWRpOHF2WHpDR1FIbVlxb1FsY3ZrWHErcVVnVVhaL1gwMzFSUkp1T1RKeWN1R1FLOGJTSjA1Vmpi\nU2c3Mzhuek1DeGUwYkd3a0pJZVQyWGZqTXdTa0pqMVBjNk5salZZNVhXWFpyUExuQnU4SHhMbkYx\nYldUclFFbXVia3M5Vkt4WXVEUHEwa3N2cTBTQzdWSXAzK0dxRFNSWlRQQ093OEg0Z3VpV1RwempD\nclJsdE5hbzJWbU5xTGdHaVd3SFJTejIzTlBvRTQvVXl2a3c0NnVtaUt3MGN0NFdaeHlTMkpTZTly\nLy96Rnh4K3JRSEMrWDdQYVJvVTBTSmlGSVhiT0VnMjJBTkM4YmtrMnRveFNwWXg2OVhWdjBOQnBQ\nRm04Z0d2VDdSMGRscUZ4NlcvNzFKTmVkRG4yZ1VaZW5aUzhJNFp6L29id2hQWHZGRHowNEhzckFC\nN3UvbzBITExEbmRJaU85MzVlcnRsVUlySHFSc1FDVU9wTXl1eWM5bEZkckFXMVdpNkVpMnZLUUd0\nYUpJeklDWHpvUVF1aWJkTitoUDZ3eEo2R285N1NXSWt5YmlCT3F0YlA3ZkxPT1MwOXB2ZG5Ib2dZ\nUi91V01FVkpJUFUxeno5RjVhcnFRN3J2TE5TVXVvV2J1VEdNUHR2Rm1uYThXTjJ3SlBSVHdtRjg3\ncDFsQ0RaTXM1QjBPM0w0Sy96enJ6YTZyczlJZGZTM1NEeUZNYTlya0ZvdTZ2MGxPRTduOGVaWSts\nNi9RNXlsS2tHMGlNMkNVRnFKYXd1cG8zanJRanBqckh0Z0dGR0dHV3FwT09XakFuUUlFNk5yQUdr\neVVuTkdWZXA3VHBJWGpRbUV5cWVGcUZqMFhsOFNoVHlFajNVUHh6eVJrRHZZNzNablUxVEREVndZ\nanFsZW1OU1NYTlYrbGZNNWsrY1hXVHRuSGNhVkt5TUF0U0hTNkhtSWJFVEVoUmFUV3JlcnhKMkR5\nTmQ2bll4WXhhM0NNYVdvczRVMTB6Si9lWVJjelpBcmhwaDVQNytodDdrVDk3Z2pXMldLaXQ3YXlI\nNkRMOU5QUm1lYzVwTWFHa29xdGhwWEZxcXk3L3JYVEZiSGpnd3ZJRURLYWdtY1YyN2R2ZitkNGtJ\nWmNXMll3WEg4cmNNN25ud1JSOWJPc2lVTkpjc2hHR3BJRWc5cmNJZEFkTlUwazFxM0k1Ry93ejk3\ncUxmdEtLd21FN2RVWkppQTRSV3M4VWRJWEV5U2FHTUh6QU1kT1hEMk9STDNXVUNlRGNWbmZPSC84\nK0xzZDhTbFR4R1FoVCthRkpkWmE5U1BEL0tKRnllc2tYaDlDYmZxa0FjZjJLY3hyN0UrYXkzUFNB\nVEU2bTZBVUtGajdSZm1UUUw2Y3hCOVVWL00wVi9DcG0vUnF1dWR6dGRjc0JPNFVuVVZpSXFOd0s3\nQ0dLd2NoN2hycGwyekVKVFVzbVU5Ni9NYUVnajlwWmxGbk05REV0TFVXYjhqMnBwNDkvMDgwVDUz\nNUpHNy9pVU0zd0tpODJ5OEpmZ0hSeDY1ODVXSDQrUFhIL21oMHovZlB1S1pMMzZnQm8xMURlb0dr\ndUpINkFWbmt6L1ZGMWxWeEtmaExNNE9kQXNVK3FxelUzOE80UE5ITDF6SWJmbDFkNEcvMlFwSUN1\nMVR0SnVKQ3diSjdGdFNvYllhdnVsVHBqaXJkN1JRT2dWWG0xN3dKM0hLZ1QxdlI1NDQ2NTVBQmhi\ncHhteVNLek9KbGhZTkVpU3VYOFc5THlwSWxGWXpYeHZWbGZBSDk2VjRzT1BYZFdXbkJpWmhCSVVq\nMzdqelNlejh4TzMrN3dOM3BjRDcyNzRpSndjcFlvOXNYZmVSbmMvK0ZSOFl1Vkp3Y0o5L0lHbXFK\nTWdIbU51S0l4QjFqK2hGclVXRWtpc2FUWGVDejJJVTFmRXhSUEhXRnJWQ0E0aVZRclh3MVBhajFY\nNTR4dEpVbUpIQVF0dTF5UU1CbTdNRkp4TnVMQjJHN2xUelp5dzUyM2NsOVdNRFYzb1AxRXZNM2pI\nLzh6MXd1ejNRVnBESnhPTk9xRENudmIvRlNwS0N2VUx0M09ZbmNnYXl3a0t3cWNXa1pvZjQxSXJD\nRlY5NFk1OTlsOTFVVGd5K1p0Tk5xMTRtb0kwK0dreElWcDE4ZFUzTS9PZ3djeVVoZW5aQjV4T1o5\nL2tLSTRsZTVEbFpwQzFia2tUV0s2Qk5DVU1uVVpJSUZxM0Zma2hRT0xYT0ZDY0svUVh6T0pxb3gw\nZ2d1SVU1K2pCbFBXdEVxUExNenp5YWJQbnk5THBDVzI3ZXY5RUovV1N2ODdCcTZKUStkK1NodTNU\ndnZpZ2lrZTh1SkNhWFNKNXFXSEh6UkJOazBoaVVhSktUekpsaGxEOEt5VkRUeSt1djFuRlVrMlV3\ndExKRndnaWhjUElLemNHZXRhZEFucXhOSjAzd0h1dVZXVXRrZmtJdlRtaDlLQlhWekdYM3Zlckdh\neGtuQ1cwM3hlTGR2VUlUMUNwd2Rsd1I4eGZOTUFBOTRXeFNJZVkyYUVTOXM5eGdVMjlySXQ4cE9I\ndU9PRnFWaThzT2RMNDF4N1lsRjVhL1dKM0x6dGZja3RScFc2NDFUeEhXZGd5U3JnRXJqaVIzUEls\nUU9Mc1N0bWo3eW9jbU51Tk43RUltYWZ3SFhxME0vb2NPWnJYV0cvSmw1dnQ0cVFNTUE2Q2pXOVk5\nUjhCWENKeTdlN3AvaC9DeHh1a3hRRHI1NkMrL0tNSmZVQkhaV2pteUhyTDJ4eStLRGg1OFVzOHhK\neEJXczQ2OTFvUXArZ3VkSXptR21OY2p5dG1WSk9ESk1xS3hZY0FrZlpYb0lPdDdOZnFzZ09rZmlv\nZHNManA2NEhaYmRPNWRRdWExSWppcDVyaUEvdEE1ZTdXMWZIVk01a2NIUFdXdEpPOER1MnNGOGx3\nMjMxK0YrV3BYczZVZlBQVGdlNm9YMzF3RDQzTnhGMFJORjcrRkZGVjV6MDRTR09jRmtHektxbWNH\nSW9mby9BaTRxdGIzVkYrNDB6U1NjU05JaU5xZFNPcEVNeDdidXhqcG1jYytjT0hhbXo5MWVNSXJp\ncjdQNmZqUnh6N1E3a01aR0oxNjhNN3gyMjY3ZitxUm95ZTFnWmszRm82MXpIZm54VThpMURmY0l5\nZGhRaEVoS2VRa2pJZVYyaGNoc3JsMWhDQSt1d0krNFpPb0w0WmhLK01nS1BLdGpSVFFGcklJTHFx\nNHdqelNGUHRJdmlkWmdKU1Qvemwydk43L3VGRzJZWkRFZ2pNWHdURGVRdEtDUDluTjgxNWVnU21l\nZ2REbVZyOE9lWVlKb1dmcGIwdGkzOTVXRTdjN2ZkcXhxZVlTelE4SmgzeXdmaW1BSnRWcEYxdEk1\nTTNkN0l5b2dOTUxnR3hzWVJqSGlNNHU4MXNUVUs4YTFSdVo0b1ZKRWhycjVEa2xKeUUvYVlrV2hF\nVGdNMC9uSm1HRWZBRWgwYnE4eld6SGNSaW5XTmgxRFhOU09hc1dJN293N0hGRkpPakxTanIwNEQ1\nTnFUemZTY0k2VU1kTWd5V2FIM0lrejgvRnY5VFlrclMzZ0s4SjR3SHlmbWM2ajByQlFYQkYwNlFX\nbUtrU3pLUW01YW1CckZXak9qZkU3a0lhcURnOWZVdHlZSU1saGxsQWlxeDdWbHphTjlhbktXRTBQ\nYlpleURsSWdMTndUalhRbFMwTU16WUVyLy81WUtjczM3eHJlUVlBN3BFRUoxb1hTVDRQeHlheUlB\neGpDK1Vtb2szeXZwV1pxVm9lMFlzckxVSExiblA0MU56Yys2eVI2bXpqOHZUTVgvcEllZDRFbVpW\ncThhckdHbWVEbGlhMjlMeHVTNkdNQjdXOFJEb25JaW8xTkg4dGhOakFMb1dhQTZjUjJTRUlheUhE\nOENVU1JCZEdRTmJVbVd1WW8zS3BQeWVRSEp0MlJGeUZUUzBrNXcrS0NFNHpGVTJjdmxFdmdJL0Fr\nb2l0amEwR0tBcHRYZHlXTFRkLzdNM2l0S2V5VndRWk5qbmowdkl6cHBEYzRMRXJQbktiZ3NkSGx3\na1UrcUcvMjIxc0h5ZVFjK3lxM3lVcDdoUnRJSmFSQWUwV2tYWHF0UlhJcHZaeHhybFJLcDQrNkNw\ncmIxQjhjMzArdXNXSFRJYjhEUkdzM2J6N25oK29OMm5YY1F3M1ZqenBucWhkUVRkWW9WaHpxQXlm\nSEhaT1N1RzN5Wlg1dWZ3NHpVaE5hZXJZbzZlK29hVldOdS82MkIrS3VEdEZlODgxdnBSR1lGUHRn\nV0gwd1d1V1pvSGdGQkF0Qjd1bUJOSFc4Nk1qelR3UlF0bWxwTERPY3ozZlI4MXhham5ncjhGNUNB\nWnJKVGxLVE1GZVE4RG5sVnVhVDZ1ZnNPeDhnMUo1SndtOWxiUjlpOGUwRzNKa3Zsd3Mybjl0UlQ1\nSHJIMTZkSnpSN3hKSS9EaUEzd0tSTjdXTXMvYnJISlhmSjliOUNZR0dRWnFVNTcwMjkyclF4VmxO\nYktDM1E3Q25NVTdMQk1COWt5b3JmMVpZL3BDSnRNSzZudy9PNndZbFoydDYyVzhDUkh0c2VtSXdp\nZEEvVEY2Wi9LUkppNy9Qekd2VTgrcTBIcDdlRTZkajZCOURvR3RzWEJJVy9YMzJ1U3QzYnJ6eCtB\nRzFWcE45dG1idUpXN0dmWnpUYzBkbnRFRXFqcHpzeGpBVUpFejk1Q0dPZEJMazFtUXBzT0c0RUtK\nUnRaQjhDeEk5VW81WVlaMTkzRWVXdzV5TGtmZ2lpV0pQSG4za3dnVU1tTVNtaGlJemtxRzlHalBX\nZVljODlDMVhKTkVqTzJoSXJKYzFJMW85b05NNCtKVEhISlRWODZNZGNxblRlTjR5VWtuVUhGZHU3\nTUFkeGdrd0xPTGhqRHJmVUpmNVRFdEI3QUJ5R2hZWDZaMFlJVC9PZFZwaksrelUvejVmSzlsVGxo\nUGUyVnE2NW43VGc0UnBPZnVMZ0wxQ2hWK0RMTHZvUWxtTEN3VUFOeWkyaVBvcWw4cldIUkdUNnY2\nbnVNRjZLWTNEUUFEM0RKUjh2VHgvQmJzaytyU2wxQ2thc0s0dmVIMURwVVJ2NDFEWFU3STlwT1c3\nM2NhaGJUNDlUN2NBYTh0eG4wcWJ6VWRkeG5WS0YvUUhMaXIwbm5HRHp4aG9uK0FVTEs5dmF6MThn\nYWVpWjBPb1FDOFNreFhxcnlEelZIeGNWRDlxbU5iZUtydTRrbVJMdEdDVW9ldlFHa2Z5MG8zUEFO\nSmtHR1VTZHFlcFVuNnFIbHZ5a3BMN1k1akRUL3pDZVJJODc5VUtUK28xRksyQUVQNVNQZE5MWUYv\nL09iUGltc2Z5cndaNVNHcnJaMW9DN1NLdXl4TEJTNitvL1ZwbWJ5UlVuYXBUeUVFL0R3Vm81MkVO\nTENlaVNueWttWEpLSU51ZnQ5ZERrbkRQRXdUZTdXZDJxU09ESitxZmNrVGp6cVlIU01pdzN4YjFt\nQnV6emgxb2lsM1YrVkJrWUlmZmQwUjArendrV2JkNlRXMGxvbStMVTZqRVlxcjhkUm5SanR0RWp0\nejN1TE0xVlVFT3RqQ01jTVl3OVd3Qkt3Nkd4K0NvNmJRTGxhaU9zVzRwb1daM0lPMS8xQ2VSYUI2\nMC9MeFh3cXc5WHBTVmpTM3B5TWFWMzluMjFMRzN5akpESTZOWGVNakRvZmpVUDJ3N3Y5SVg1Vk15\nMFpCTWNMSTVObmlZbzhJeTJNb0RjYTN3UVp0T0JyTnptYUZrS3FwR1JiY2pxQWxMMURmdEl6ZDU4\nNGZ2R09abFVkVlFRNXBFbmlIVWkrRDdPemFnRFZXZ05nVm5jbDVlLzcramxNWW5XLzFQL1FVZ1Ba\nbjRxK0tTU1RMRklTZnVvV2NlL3VkTkMrbUIyKzBoTmJQejlPQyt0UDNZbHRmdkh4WnZKSGpMb1BM\nc2dUdW13U08yM0x5Lzc2VXRVWlBPUFBTdng4NmdsVUlCTVhhQlliSVVGUjlScmxFQ29wVjVUWmpP\ncnJaa3FkM24wcmVFT2ZMUXp5dlErY0dnaDlCL3d4ekkrbnA0alpVdFNaRUZvdUJ4TkE1TzY5cWg0\nUjBlUjBIRmptZ21aQ0FobEo3ZHVBYU9SbHVLQnpmNkhQVkRKT1Q0TjF3eTlYOGNyVVZkcTI4djBl\nSWpMOVFWQzZNdkgzajBQaTRaUTZLT0gxbldCRlFSaWlkWHIzS2dNZkU1YklHSTBSY1F2RTZISC8z\nRkE1cWhNNmdmc2tRTEttRnNhRG5jOUl1TWFwZ3UzejFORVhieHVlRlZITkdrYXFyMStJRXNVR09z\nSlZvY3hENVNyZEtsRWFuMi96OFBGdzJoanIwbEFTVUdabUo0aFZDcWdha1FuUEllUml6YnFkMWls\nK2dsSkdFVWJXZGFzREJuRWFjalBsc2dLNUZQMVJoY2laZTdvcHBZTk9tTEFBV2JkV1M4ZUg1UlZx\nMWVvc0ZUc0pJVW1wbXYvV2MxZW15VzU0MFByaFJBdFhqWUN4ZHBwb1JvOEd5VXIxaGltSmNJZVQr\nTWRqRHhHRjJOdFlXdVpRbzFXTldNc2lyU3JnQzJOT1FpeDRTQXkxVi9EQUhsWWxMVENPaGc4U3dE\nSUswMUUzYlZMUFkxRzRYb2NSWXVFWTE3OUR3T0dzYndEbkF4V1NabnovTmxMVTk4cVkyZXg3blFw\nMHQ4M0tSSGIzYjQza1c1dm9PblZ4bEdjVHROYS9sOEs4TUFyTEJNUjJVdXBnV1g4Z1dmc3gvaXBV\nVkw2VHczK0p3YkdWQnF4WTcyekRBS0p5R01hYnNjQ0o4VnNWSFA0MWpHeUJqbnJEc25Za3U5bGMz\neGNQZ0xiRmhyZjU5WFBFYlA2Y0NnQ3h5UlE0M09pMWpsb0o3R0FUUnE0bFZ6cnRFWitXcUUzc3Vi\nUDZjSGFtOXJIdEJzeDVKaWdtSWtLSlBpZlJ2ZnBjak5lMGZZdVZGOENnZmRPcmV6NXdIQ29JZ25o\nODY4Y0daODlmb2J0UzFscitORWFwVjFVeU1uVHcxRnU4Vk85ZmdVTTV4ejFXdktyem54M05RVGI1\nYkk0Mmw2b0FKc0tyV1hGOCtlZU41dCtNZmFvNkhuY2FhV0hQLzZiWXJtbWhPRjRHT2VZVUxWd3RF\nV2x6OEJacktvZUNLeWJJWUo2dTBOVDYyUER0dnFuSHd4ODAzUFBQT0JLcDVCMzlVek0rcTc3TWJS\nOE05ei9ZNDdOc2R4TDRSL251OTNIUERMbUN0eEkyT2dydlFHdE42NDkrRG12THgrUzlLS1ZoNy9J\nczJ5V3I3U2xWbVVETE5FZzZmQU1Ia0o0ekhPM214ZWtXY1lNeFdndlk1RTQwczUvSzAzeFJlOHQw\nK1NRK1puamJDWGFBRW8yNUp5MEFZbkRoRk53Ym1tQjlleU42czlid2l0SlBYVHRGQi9PZFp6cGMy\nN2ZtYzFVZldQQVZxcDhYVVNESXVyYWlYSTkyN2V0WCtuVFFvL2ZmekFIVXNabFBOSVhzbHE1RlI3\na2hxUUt1eGNFZXpCYWVjTXVCb0hoaUczeGs3TEVwZ0R4R0VPRk10RURNRWJ5TVN2WlRJN2ZGWEty\nRGdSUitXM21EaDVPNzdQYU9jY3ZlamF3M3FldHFRNkZrYkp1M2xyd2ZXTGtjYVdsQmgxMmpVUzhO\nbVhpbWl4ekJaRXdoQVgxTFZjRTZmV1o3NitqL3FRZkxtSk4rSDdpTGJ1dnZmbWswWDN1VTAzZm5K\nelgrTnV1bS9uK0lvTm45dDZ5MzNYREhwTm1tWVJQTDJvYjBtb0lFb2RMSVh5WlZwQUtJbjhTNHNP\nc2JBYThSZW9ZZmY3Ym1welVubzM3L3BvbWJqMFprWWhTcEI4NzRXSGZ2RzdjLzhwV2xpUlhvbnZH\neEp5dU9mZm1HaloyMFV1dkEvQUIzc2Q2ZGo5ZWhRdi82RTBHZFZDTXIvYXk1Z3RiOXgvQThlbGRW\nYXE0MGNmUHZVMVgzU29BN0V5Z2NmQ05McjB5aVNzSmlOUnN5bDVMUWI1V3I4K25VRWx6TGlJMXBG\ndk9NVG14REFwclZnSGNaOUhGUDhGT2Z1LzRtTElPN3hrODdZOW4vNitDRk5zdk9HK3pRRHRFVHVs\ndiszSGQreTR2NmN0NXByZDk2MGo0SzNPVHFsejc1MmEvZG5MT0RIMG14UVYvZ0tDeit6WWNYMVhB\nTDNheVNGYTNhUXBKSW54YlhBekp1SWN3d2pSQ29sY3BkR0pMRFM0V3o2WFluM2syOTJnS2s3VGp5\nK3VkbHVvblVlcnAwejZmUUczNE1qZHdCUXREM1VBNmVVVHkwNjlySmR4TlhGdklESnJRcVZTdXJw\nUXFGemI0NVExdlE4TkpFSzNkWGs4cjJlWWVxU2FKbERTakRrTndtUktyNVluYzRGaFNHU0ZTelhy\ndjE1SnlrZXNsMjNiODVuK2t2SUhUVm8zRURKU251cXZqTnJpSmJvcHhLZ0ViT0tDWlhsZGIrUGtS\nbDlKWFpQeVRCUlpvVGNNY2xYczhid0tubXJnZVdVQ0tldk5iNGdscldkSExzQVpBQ3pUOVd1NVZ4\nL3BEaUFxVGYrOHhGdUJ6d1lzSUYwWUUzKytpVWhlMnd6dStaaFRUd3hEUksvTHA5dUd2d2RIWHNJ\nMDBYYit1aytBcVFpdWw4dVY0SU5wMHJDNFJELzBESlBSa0V2R2U5b3I1NVBVeXJhbXowek1SVWpi\nMy9HRklvU3VhUVlpL1dNNXUwSy9aNjgrNU50Yng5RjE4eUJoY2tuNG9ERTRHV3BVemxRZFJyY2tW\nVkdDejZOczRTSUJoWTdmSVhXNVpKTmNVdnVsSWcxVG9MOVd3NHVScHM0K3ZWWUlHeG8xamJXMHZ1\nRHFqQ0c2MHZyYWV2V0hYZGxJQS9JTjJyRnRrSWFBWnhndlllbzZLMnNjeVEwM1VCTWFSOHE4dk5t\nQkVuR2htRzhMUXlTRmlOMGlpRmg3ak00aVdNZkZFWm5vU3RVTDY1Q0ZUS0ZmLzRyeGpUTmFvN0hZ\nOVJCWlZaY3dJYjlmMXJuRURzeXh5cjdjYXI3YmlhTHBXTXRINUw1VTB5M0ptNjJLTWpHUWRJaFFy\nL09xVXNlUU5kRWllYko5dlpyTG5UWVJhUWV6bkVKUGJtVTFtcHk1M1I1aEl6aFNqVGNiNTdXWUVV\nYkY5NlFhQkxHWEx2WEtYZUgrajRkYUpmWEZRcWphckVpazZDNU9XWi9pUmp6SjkyVnlicEZFck9u\neTk4T0liRzd0Zkt3S2ZSU25pTmJQUEk0M3R4UXAwSEZzakhYUmhrRXRqVlYvYVpFd1lJVTJOTVU2\nU1VxV1F3SysvOXVudXE5d2VZaURod2J6b21BWVlwbVhHTXFDRXRPbTlrTlpwWXdyWng3b3BvM3pK\namJWbTVrTllHbmVwRzVwL3E3V1Q5YnBOZkJENHN1TU5RUWtlWWdEdDBBY0ZpNEFPUnM1dTBoTGlm\nZERZanN3aGxaTXk1VmY2VVNFanBLRXRJWDBRSFVZbi81WVQ4UjNXcTA3Yi9Fa3lFc1lKYWN0aWFm\nVnRWc1UvZzlXTVBWbFRnUmExd2tUTEtBTmN4blhqWkhtTG1IcVNXeGhyaWxmVDYzdXlDT3BrVFZI\nOHd0aDhHb0xQdGVTcUQrbkhPdTVrRmFhekJjUDh0dGgvZ3VYZTJJK1FhaGg2YlI5TUZ1UGFlMHYz\nbmJJeC8rbWR5MmJJMFVTdFFVbGhhWWd1UW93d2pWMjFOSnEyRU1jTEVaUjk5OTRtbjhQNjFUTmpF\nY0Z1MWRzYmNqWEpRcU02a2pvRmpIUnJmZytvQjA3OXNZWFNGWk03NVVXWW1YZFIrN1ZJTS9LRnUy\naVFUT042NDhpYnlYVnR5VGxuY2hVNEZ3bVliekdYcVVrT3RHc0NhT3hJMTVsbzNRc0QzR0FoMjdP\nTDJsdFdRQjN0eC9mdXZ1ZUF3UjhYekJNYldSMWlVRExtbzNJNnVSdDVLN1hlUE91NjR1UWs4dGE5\nZEhHdUlGNXY5bERHeG9tdEU2bUJXenpOYWFvaXFxY2dpL1pVSWN6dUZWa2FVSnpKQnJIWkc0UWgw\nRlFTamdqenZwT28vMGcyUnFvdEQxN28rQU5EWXJjbHB2Mi8rcldHeHJnSTlyK2pydUwrdm5PTnZT\nYjRubTI3TnIvYnpmdittakxFNnpmOTNWdXMvSGI5dXd0WmQ3V1dSZG9TY3BBUzQydlFJRVBsbXR6\nekU3ak9EcGRJcExoYVl6bWc3STBzUHgzUmg3YUVJUjhEWXh5cm8xZkphcVZ6Z29oMUdYMXdvaFd4\nSkd0Z0tTWmxBOVpOcHZyZXY0b21STEs0Qlk5MHNtNDl1L0dscS85WFgyL0pibGlyNjJOUDczMWxv\nK3YzSFRUeDE5T0p2Nm9pOTIvME0rMjNuTGZ5c29vSDNCcDdkQ0xjZTNoYlh2K1UvUEJvTUlQY0R6\nMG00VFNPL05NVkRuUEI3WWNPZmx6K3ZmVk4vM1dPbGU5NG5GbmswTmJkdTMveUd6cmNpaVdJY2pW\nK2EyVEJua3h2UDNsSCt2b05oQm55eUxkZkZBeWZEUzVVQmlZbGVURldLaHRKN0EyYVpiNXlLcFJW\nVWZVSXRMT0puVTR3M0lMRG4wRHM2ZGFnR1Zyc2ZhU09NME1XSHN2OWxWL1ZvRGxRc0VWSUk2djAy\nTE1oNy8yNGloVCtoWXlCVlV3MytwUmIrbVVhdjdyQ2JLT1RXR25xL0tibTJlaGQ0U204UExEamJV\nVXVVaUViVUx3Q3FvdE9CYWk5YVRsNDRuZWUvVk52eldqYWV5aXFXSHR3VHBOVUhqbm5ReVpkY05k\nYm54QkV3eUw3Y3B5Sm5ISzhkREs0dUFZcG5uNnJGQ00xdFJ2Q05DcDBsTWpZNzdyYXoxdUtoZ2hq\nclZrOGtUengyQjRGZUpMNkdYdE0vdVRGTEJCUWJ5U1hBbTRFd3BMRk1KdUVWOHIrUlViYnZuWUZZ\nVWswZTlZUFlhUWVINWpiczRiRkhRa3dPdDIzQllRY2FaVzFNQ2JZYmljNFNCV01jaEVablZDOVBx\nWmYwWmMxbktudVlYbTN4Ykh5bE5kSkV4TkliVzViU2UvYzBtQjQxd0xnSXNnaHNrQjNRaXBSckFn\nR2JZbGJFbVRyei83dnloalREUWJZOGx3S0pOZWI1YmxkWmpTYUdYeTBrZXMrNktzV0pMV0l4YjJp\nWVNrY0FCL2MybGxaS09yeGtaR1d2WnNBVHhjWVBXTmR5OG40T3JRTDF3Mm5UOXh5a3VPU2lMNmxC\nZWM1RXE5MTBuZEFHSm13YWVZY21nMjc2LzFHZWZjdm5yMWJuRW9taW5kcmpvUWNRbWtHQ1p2WDQy\nS3lJY0VJWGRMMjR5aldoM0l3OHcyYjFZTFVxUythVkp6VVlMSkI4S1RPTmFvWlU5VVltY0xFTG5R\nck1wT3BVS2s1VUF1SHhLQlUyVlVRRmM0d1pFTU43dkpTd1BXQmlHNHBsaXROaGxHdkNUZG9tL0xK\nT3RGc0NaSURoNkpyUXZJZm5KbE1Cdks5d2JJRThtT21kZGtoMEloQjE5UStmSGFHUDAvbWhYcmp4\nRmlTb3RkSklXVVBiekRsL3FYYjlzay9naUVEdnRlRGtReG1XN2o1aEo4OUQvRWMzU0tLTldyVW1n\nQmhZZTNGM0k2VEFIYStKdm9YUDBZbUNMV0lvcVhFNUdtN1oxYnBUb1pNUTVQckQycE9zM3F1djdt\nNEs0eXhkV052VTQ4WElEVzNYYmIvWVpOWVFPejhjM1BTY3NvT1BLTVJFVXUrUUNnZElxYWE3OHl1\nbXJHSlJIcGRjMVFkdlRrcVlOM2prUGsyVkFhaENJeWxXSzNjVUhhSzB4YnZxMHVDQUtleVRCQ2hy\nZzZLQjBtSjNFYmxvWTA5MEpIUVUveGRlL3Ezek1rbXBUdjg1UHFReG5XWFc1b045SXlLMnVJWXkz\nd2NTUzE2bHJQTEVUL01XMngxYk10Wml3QnkvLzJwQW9ZYlBDQnZmcFJEdDEzS1dWTlF0ZHd5M1FK\nRXlUVSt1M2J2OUQ5NWxubngzdHlqUVQ5UTJHMVlyUTMwbXpqaU5nWEVpQ2llcUsrU1cyWHJheFBZ\nb2xhdkxVSlVpMTZsMU9lRkJRZTNtUVZHekk0ZzVjbXJVbjVDK0c4R3lTUlR3S08xb2VDQXU0b3Uz\nU0Rkc1NwWTMrWXNLRmFMSnEycmlWRFE1alFMbU1iV2hSTEZ5TEpZdEtoTEZUaEpReFZDamtKNWMr\nN2VuekQwOTBsTVpuc3hpcUt3SG05U3NESFFwaUdtQ1BUVWVrbHBrSmQyanVRTHdqaHRKbFpHQWRH\nUENBL2pMZU9HOXVQZGdyVlh4dmx1ckQ1TGFrMTJLaVJVNFU0NUZzSGU4RHhvZ2hBOWs0K2YzS2ph\ncE11ZFNkSXNENUFOUnFNc0tac3gzeWJIci9Oa0U4VUxacks2REp4SE9JNlRkU2hCeWtaSjFvT1JS\nK29saTJwamxOUkMzTTROVjBsc2JEejhFYTF5cHdZbnlkTzRrNWxlcUwyeStwNDQ1M1VZUjJpQlRp\neWNlcHdEZHVyOWVjZHRGa3RXdjFicmMwY0NrZTBjNWVubHVpMFJicWE0Vm9oRG01eFJLeDdKM1ZB\nOFVaeGljUm0rSlFEcmN1YXQvM2Z6aWI2ZEs4eFNkbkREWjFMbnhOblh3QXpWN2d3QW5acm9NbDhZ\ndis5YzdXYUFGbUFMK2d1a2s4RUpCTG43TE1RTjBITWhVUzRLOE9RemJZY1ZhYWxPdWJmc2w3NzRD\ndHpxZXZvSENYZklUNHdHa1BiUit2ZERRRmlaV0MybmNmTkNVRFZKRTNFOXlYWnc4bTlCTTBrekxS\nRzVENmdkVW1TOGdkSXhPSzJDREJtemt5ZVorSzF6bGFTdEJaL2hFbStMdUxXQ0VjbDlkK1JjM2VR\neUh0MEVNTXRFOEVWenFVbjB0cVpEd055RUNEUE1FRjM4ZXBuR1h2M3NyaWF2NHNzNmJzaDlCK1pD\nd3l1ZGQyNmhVUTdxU2tXTnlYTzlFYzQ5WU5sV3JydEtHRUVmaTlWUmhPeTdNYzVSVTgyRkhpSkJt\nd2wrVmNOV2pZcnVDK3o0MXJJT2NmbGpZRzBPdVZMazVRL0tOSjJPUUxaREpIVFdxMHFtTW55Z3BZ\nTWNaQW5mRXM5VXFzSHdvWk94Y3NLajRtNENXVVlGbHBGb084ZVA3QnZra0FINjdFMHF2dGZDS1Z0\nZjR1Q0x5QVFHc1NjRk5qUHE3ZVR0RUpwRnlMRlRBZEtJVkVvTFdZOWdzQ3pvZUVXREdhRE9HQTk5\nR3ZxSk16RzJTa2ZORll6cWN1NHVXVU5OSzRnSmJCZXVtU05yVHptMjNlTU5lSnl6SkZWY1NBWmJS\nYmo4LzZaeTRoaFNJaEUzZmdiaUVKZkp0R2lBaFI2SUxMd3M3NDVjNXI2QW9kcW5hdzZwOXV6WEJE\naFlhZXhzM3FaTVcvMkJxdklFUTluRmRKTDQ4bFF6RndNMmdlanlFbDZSR3d0ZFROMHNSTktRODhu\nSW1za2VGV1pxTkV1VDdMT3N0UEdhV0hFTU5DNlFuRFljY3lOdm94K3B4cVlEcE0xeS9KYmtub0w2\nemxKZXR5bUlTVGc2THoybDI0U3JhSXFUNFN5R3pUd01QcThrKzhGU1dVQnJaTjZ1VGh5K3VUNzk5\nWTVqd0Vpam90ZTF4RkxCdzdjb1ZVU0p3QXVFMUhaWmN6bC94VXE2QlpFMGpDbmk0VllMWjVnWklx\nTHVURDZuRzdyNTRobnlwMEtYbDRSY1lrTkY5d0pwNDBvdEtuZm5MYWZFengyWHMweEdQS001dU1S\nMlpZa0hMcmNYaXh4UzhsNEg1SG1aa1hHWUVaNmhuSGl4c1J6VFBEMk1zbEtVZ3RLc3RKaElRMWI2\nOTlkRm9nM3ZiQWlXRTdpNGFaWlBVTU1DZUI3NzByRWVuTWR5SmRRRmE5VHdyK3JBcWtXS2loNjYw\nWEp5V25OVU4vKzZPcFlyU0NmMUU0YVQ0cExrOW1XaE1qU004L3Nyd3Jodk9RNzJiWlRYWUpvcjJM\nbEUvKysyU1o0cGlia1RRbzdFcVhOY1lPaUpzT0V4U1p3b1daTStOdHp0SWN3bUVJNlJsVFA3UGZo\neHVXT2pYWml6MHA0K3FEa3N1M2JPNGZmRngwRnhKNHE2U05NNUJtR1JOc0NCdVdlSGNZRmxKTFQy\nRkJ1R0pFVDMrSVhCaVo4MTdBdlEwdm5MdmljNGhFbnFYZHlValV0a1VteTBRMWRkVlJjOE5ITXND\nNi85MmliNGZDK3lTU2hFWHFQTkJqWFN3dXhhNWxmYW1DSkczNElYWHZpTzN1amtuak4yME1jZk1R\nYXN0ekVxcEtqMFhkQTkzRjNWV2xPUVM3TlhzRUNrZ2hiVWdnQ0c0WEJaNVZQU2NWQjFoMnVxcmlH\nVk0zZ1lINW5nbFMwS0M5WUZXYXk3TTFlSjdIbWNra3hHU29RWkJsNUthVVhyMUNtcVZMSVVCZnRQ\nK241WVl5MGxNb01LOHZDTHhSci9WM1BrTEZwWEo2Y3RNa1RxYndNbzlseWFEN0dhb0xYd3psWjIr\nTFpTT2V0YlQxT015ZmpONzZkU1pqRzJpRXdJWWx0bFJsUmE2blJZd0RhL1QxOFo3d3BZV2c0UFRj\neHA4eEQ4YUNoQlNUdE04ckZJWDg1bmRReHk0WW85Rkd3eFpHcVNoZ0hOV05iN2xFaGpOZVFzbGI3\nMFJSVlYxRmZTd3lLL1haRFVFZWJOcW9mOGpIYlZ0SUhyS3NVcHJvVlFtUXN4ZjVlV0FuT1BIOVlN\nVXNkQjJaNElBM2FaT0VENS8rdGh4bDYyNTYwZ0YxbDJaVTh5NVpVajZiN3h5ak81VkZicEtGQnBE\nbC9SQmxuM0hPNk53MHhsRlp0UktSUFREMWlMU1VYRitZWXNiNEVmWmU4R1dvVGRuU3Fua1l1b2hZ\nSkVGdHJDYjRtZTRnVmFOUDBQWHNqVlhhSnRmaVJPbWVDRmVMQ2RaT2FTd3NRR2hhaDA4cE5Hb0Nr\nekVwcXpvbXE2anZkbHFSTUd2NlZpR3l0SGlaUXlJTi9maTNuZzMvNWNVSEJKVzJhbHFyZTVabW5Y\nTDgzcmlWbzJHMXV2OVFoYy9KWTE0ZVg2eGlpTUVJU3Z5VTF6MkFodm5nUURoN2NweGRsTE9jMkw3\nSlJxVUJhWmo2c2o2akFtRVBFT21qeVc5WEt5TXBFa0tMZ2U4SEFYZ3o1Qmh1Q2lpUHRSK0FYb241\nZS80QVVhb25lQUNjaFZBSTI1TGJhOVZwWmRFVlFmRDNnd04vY3hHbXJBSkc0WE5BSGFKaEVUb3Nn\nWlU1SDJLZ1RPUDlUS1lGMDk0bVFsbzRLUHBkSW9wRGp6a1pOK0hBcDZuTjJIT2ZmR0JJVHZNMGNx\nYlFMV3hLYkhpcDgrZUFvclVpU29tSjdjdmVoYWNoRWJjWldBcGRIZThHaXpFbXVCVU11WWsyUktt\nL2t1NzNXOTBsbUo5NC8wUitKdGtiR0c3ZDhhZTFuc2Z1ZVVFcUNyaVRDL2o4Ni9OQmRmOVQzK1hx\nZE5qeFJSWWxjdHIwU1dRbWkyMFREQXEzTXBnb25FVnlxVmc5MktQWkY0Q2E5S09Dd1BTZ3orVjlS\ndFpHSlJCdVRuU0VnRWZBd203SkkybndveVR1dU9wdkcvblBqR2pmZVNUQy9uWmdWaHVyV2FmWjUr\nMjh4bktnTTB0QkdtcUVHbkpPVmFvVjdFMFViWC9Sd1JiU2NDenQ3NytaZCsxOGcybThnNjBodzM2\nR2pqK3o5M3hXUkdQbTg2bWJCSW1XT1lDVUZ6dFFJV0dNaUVSbXRJK3pVc1dqWWprZytLT2tCUEdu\nZkVldWdNTk15NHVpbm02ZlNCZ3cxRGRQUEc4UDRlWWdMa2JaYkJyN3JMWlNzV2ExTko4aDdHTmly\na3hwTi9CTVI1NlV2aVZOZlRBTm5vRjU4Tlp3aTBybzVyS2ovczluV05rS2VZY1piWnZUMlpCY1NS\nelhkL2ZUR0cyZlhoUGxrYmIwOFhMYjlUU01XVmg5YThCV0xKclQ1aXBkWGhLYjBHdmx1T3ZGbUpM\nMEVITCtsdVdzWU9GdjVMbTY3L29ONHdETkhDK0l1VWY5Z2JuaUtOTWN3b0xOTmJaMWh5YTFncXdI\nSVhKK2N2c0lEcWpQVzhSWDZNT2V2QlYxMG9jUlpLWUNmNEt4cmxNUElkQllrWmNlb0diWUVSWEVy\na20yamIzY29hVTJrTU1hY2FvOGMvOTJJMmFoY3NoUkZEQ2s2b1hNRXFhakZGTnB0NSswSTMzeTFx\nOFdpMjExMnF6S3NzWCszTVJoUFlwM3JmT1BGSnJWY0ZtaVdmQytic25FYVBaMk5ZWEsrbnF3bHRa\nL2NMN1ZSdlVQcmRMUmllaWtYMVNTeUtEWVpobHVDalFxaHRxdGFnNUlFMTBmRW1wTWhCVjBQM0xu\nVUgzbW9oczg5SmlIcmJJQUpKSk9SOGFhelpMVlFzdUxSQktvYTBtZ3c2ZWJnSHk2TEtHT2NWQ3VU\nRitGd0JxQXBJWjd1b0JOWHBKbDZJekJYY21HQXEvMi93TGI2amhteDdjd3dKamZPWTQyYjQzUjNN\nck5KbUxxVk5RczErL01FY2FZUStGWWRob2J5bU5iVzZEU1pWUkRiY296N1NKbmxxS3FZeFN3Wjdo\nSVNTWGdpRlRaQ3dhbW1Kcklxbmd6VkdUS2xqMExhamJBTHVseWs2RHIxcUhwdk1DbmpxRXVZMlZj\nSTFES1MweG1HVVJZZkcrcTZHQjlvRExWZGNOMzI3WGNYUVhLTmR6cERVakZSNTdIQ3FuQ0ZjY0Mx\nMlBtSm1MVGVuWWVGaW9XbEdjdXA2cmw3dVZUc1k5T05TVlhDWkdIeWNJbFNqRFkxTmpzTjRxQndC\najBtYzRJNDFNUm9QdEg4Ymp1OUVBVUpvNUFDb2RBc1RNaVZSZmRMNnpMZElBTXRpRnhJcTRuMmsx\nTFYxVE9FUkdxVmtJaE5mWVVBSWZ3bVVYUzkrTksxYlZPQlJ1b3BPeDFKRW4valF4aElYbHU5d3J3\nSFFwdDk2Z3VRdXJUYmplY3BsWUErdGtkMC9kWkM3YjBBWGFYanZBSStDOE5BZ2tkL052S0ZuWnQv\ncVVrWEZMdnc2OFFpbW1xSUt0TUdjVkRtWU9LbTVlUURjYjJYa1M4YUpQMW1MTTRIU1ZZL2hjSmU3\nZGZ2VEtSUjUwZ0tVZTVDa200TEoxZE5qVjJBc0ZVcnhIODM5SkFTaFJCb3kxV202R1Vnby9ucFEy\nS0xRWFpuSGxxQnJPQ2d2SFVtaWliRDl1YzE3UTBnZkp4OCtvaG50dXBRa1dkZ21IcXdFV3NFOU51\nYXg1U0ZjV3BTeUNBUDNZaVZpYWxQaGdsSk5rMGZnU09MZFNzYUVrYTREYzRBN1R0Z3hwcU5JdFI4\nY3oxdlNkWHlpT1p4MXhZNEtwQWpwd2xnYW83Nm5DSlI3STlhSk42am1xNGlOVGhFbjh5R3lRQ0lP\nM1B3NEw0YXlDWGVDdkhRRDlFYmxEcGloYVBGNFhwb3FyY2JjV21jeWVyZytJUFFTcUc2ZDN3NkVX\ndEF0MFhxNWk5TzFVMVZ1bXhueVZRamZ0RXl6bC9kcWsxbXJ2QU5xV08zKzJFWXZ5VzE2VENqWXcw\nSkkxWkcxWmVWUzhwZm5WcmJtcFN2amJsNnBEWEh2cWMxNCtzUTBJVWxBVHViMUNBNEtNQTZkVkNS\nd3hoVEFITTdjR0NpbWxObHNvSDNZS2tYakNTVkVwc2F4UWhKYWd5T0NHcHRONVRXWVZzTW03NmE1\nNXVybTlXdnNrcWNUSXNYMUltNE1Lbm5hbitHc29kcUVxdTczWGlQVzZxMkZ5UUl6a21wSkJNemIw\nbUM3bXZLazBjMTU4eGkzUUNiRW9iRllxTHAyalpVdk9DQjRqazRReHc1TFNHZkplWDcveThEZWt2\nS1AzandRd241V05UQ1N4Z05kZ2FubzhJcnNXYnRuclZEVU9pQklLU0xHTGROUGQzNit4UzBGR0RP\nck1qRDRNa1c5WHBMeURFaVhLMEZzWDNjcWVXRzBaQ3JLYkJKYlMwMVJ5dWJ5RVFsenFmc3RLK0xh\nMU4xVC9JMEVwbDQ1cWF6SGJkd1oxT05aM1hjZG9nd3VmV1dlT1llQXJtVW9SbS9GMnJEMUdmMSsw\nMWdHRjJ2ZzRWaW96TktvblJDUktwMUo1SW10RnNGOTRnMEV2V1ZZYTdjdWJIUWV3U3dHVnBZVU5J\nKzArcFhZdm91RVE4WHBxenFJMmUwbUlOMkFDSHdLLzBXNVdJdlljVFpJK0pTZGZrdmIzVGVkZklL\nL3hsRWsvbEhHWWliRmROQ1Nrb3hDcERMdE9qR1FPNk5USkdhaFZsRWZEcVo4WGlLTWxoc0M0VnJO\nSVo5bmR2U2lDdm9scVJ3MGZhQitobzc4TWs3WnRZVnVRM1EzKzFyclhBbjNYd2xsekZBRG12WE5o\nYklTV0VpWUh3emR6TmhoQ04ybE9VdUJSZTBEQlBYbXNsZ3M1REdYUzZGaEJFU0l5U25MTnozTkMw\nV29EVUtucUtvT0d3S3lZK0p5QzRTTitxTXh0SUlWdEovQVhHL1NZUTFlL2JzMVVyb3A4RG1xaTAz\nZmZ4V2dGNGxKT3A3S1RYS3B3WGxzMnlyaXJVRm14U2ZBS0lQcXY5TTBZdmQxc1dqRmJXU1FwQzNo\nYnpDM1hYYzhRT3JxZ3FkbUhZdGZkQXljd1BNZEQzMDkvVFErN3ExVHpLemhXdmJrazRwZ2pHUXZj\nSlZWQ3pXZjR6V0svRkorY2dpMXVHNUtrdWg5NGkxb0xVYzJzS1JoM2FmaFlLbk5OR0xhQjFJbWRk\ndnRiOURKcm9lb05PMnJIcUJrTEY4SEl4blJhVDhuWE12ODJnNzRqZ0MyYzh5RjdSVTJDbnJRdlpo\nTG9lcEZKRnZsazVrQ2o5TVpLNVdMVHZpdU9zTmZPYVpEOVJJVkFKMWtoVHRsVXZ6ZExzV0t6emYr\nZG5USk1TWmlTRUtVdTlWaDhuSUo3WGt3NUZrOGVRRGpTOGNMNitxVWwzREQwOVFLY05lWkVuNVhn\neVg0cVRTY3hVSHBwQUdlbW5Jd1ZCMDBqOVp4RmNhQllQNzl6UWNrdGh4Wm1nc3hDdGN3VVVNMHZ6\neUdNTXZEa3NHSEVmbXpSWHdTY1BSa0ZaTWNNNSt4emw3SENSRGlVSWVWSTc2MC9neUloTVNkZGRo\nc3IxTUdYbmFCd1FFU0dqM29ia3dUWE1VU1lCdnpEalN5SWxRUVhWbWFkL1dpZDNIQ1RJSjR6OXcr\nRkNPb3g2NDNZcEdySnR3aGlJNExZa2dPK2JyMzhXRXVHZUlnN1h1ZTcySXd2a2hNbFMxWjhVbGFs\nOXZjZnFVZWR4MU1BUUk4dUtFTGZrT1Y1RVRGcHRlSUlFcEpzTWpSaFFzWGkrbnI0eXZJQ3k3U216\nMU9adFUzZ3drSHlTRmY0YlUxZ3htNzNGSG85WFNoUXN6TDB0T2RicHhkYnh4MTJIKzgwN2paTVp4\nU2xQTUN2bzY1ZU5STTFEN3B4bkV2UEczOTBlM0xFcVpvMkZDTTlXYzBjU3Rsb2kxaS9yQXhGRDhs\nSE5wWjZ0ZzNrbW81azdwelJzVGxzM0dQNGthcEF0cjBSeGxFNDluMEVjbTR4U1NLWlRHeVlwVUdT\nYm5rN0pPamptdEFnRWFQWDdnZnp0TkZCMFZRY3d1WHhYS3A5Q2VldkgvKy9XWlhRbENKem9jMU9N\nemJ0OUM2REJPL1dlemIvdW5IcnhUcmRYdnRaV3duYzF4RjJSejY5L3QxSnFVejFxb2o1cWkwSE5v\nNWdIdGhWYU1yVGxFaEtmWUZEV2xvK1UxRXpJdFQrS003b2VsTUtiRmp6U3JhYTJKYU9MN0p0Q21J\ncFhPUXRDdzJwam9lWnVNWk1xWm9UVEd1QkFzK1hpWlBTWk9NU1lldGFmMjBWSGZlcWVlK0NjYXJZ\nWUJhVjVUZHBGRFlyeFdWWjhsNEZySEdMZjhTTjIrVDh6NGU3cU1NOUtBb000OEsvQS8ydStCdmtM\nTnZVQ3RGMWVCd3BUcE1NR2hQWTFoSE1uNW5GYXM3TFVDMGhxeDdnZmljUERnN2JVdE45N3pHNDdT\nV3pXMjFseTlNTEY1dEpkemxDSTdXazM1NDVKT2xVSFMwNWhzclJtQ1JFNkswTWJ2UHZ3dko3YnN1\ndWNFRWEvTGdHL1BwaU9KejQwUVk0a24wa2xYTHRTWVpIVjErY3BIQytNWHpwR20xN3EwUWk0NkN0\naVZrbUdDZlFxT2wrQmNFcW1YdnZUVzVheWRjNG5Oa2RhU2ZZb0NTRk15blNSUG51Ulk2elB1bWRt\nUk1UMHhURXI0REtkVDZ4WFgyemdqck1xQUkzamdTWDl2VklQUHplZWZCR3BOOW1xbGVocEdrOXdx\nYW1HWVVQZ1pmZENSeCs3OE13RDZtaE05ODdVUHFGTDNTLzJQRFBkUm9BcXN2TjQvSUhUUDA0QjVE\nU1NadExYQzg4dHFNTFdDUmpDWTRpdDVxam9xRlN0WTgrS1gzejJ4ZWRjOVI0bk5XaUI5Y1gzQ0ox\nOHN1R1VNQ2tZQmhhaHpDaW16WXFZODZmTkkzNXB0Vlpad2pKMTI3VzJJYmQzTVJxTTA5VlpjTjBx\nSmp4bVhha3lpYWN5SW03QTFGeFQwV2VqRXczZXFBZktMZlNpOVlYbTU5NTFFWjV1SnhxdEQzblh1\nQ0YwR09kYXFuemZUVGw5US84cVZPL2NPQWU2Ym1rUW9vT2VQajd6aWhWcnNhNGNwSHB5ZStlSUhx\naEJVMkpkbzl3TDRjUysyQ2Q4T1daRnVwV2kvcWJBMWh4Ump4OE0rdjFWMU82dVJhUHpkYkV1TE5l\ndFNVWDExNHlKSXBwUGxzWTB6bXNlUnFiMG9MWTNQdktWM3l0bFNUMDY1WGloblZtc3VvSytQbGpl\ncnB6R004NURNTmppRFZaeE1TMkdpUmM4d0dmNmpYalR3aUtKejJLeGVMUkovSmNPVVBJUUhmekIx\nVmozdVdZMWlKWkt6OVZSWElmeVZaeTZoci9pL3hhZVorSnNxemxaRTQwMitsSmhtQ25oczlGOGZm\nZVNVcnc0MUUxVnJwMDU1SjJMZEp2Rmx4K2g1M2I1bkduZjR6T2daSWpyZU51NXdWa0Y5SURSZEpm\nYlhLdmZYOUFFNTV2QlNjelViWE1oYkRISVpWSEZnU2Y4eldMUkNKUXpoczQ3a0oycGxjMzc1aFJO\nL2I5T3ArOEh3Ulo5WFRweld4TE9mTlZQMktmM2JnbjlCQ1AvRnYyZjVVbG9iK3h5eC9XTi9Ucmgv\nNVJMK3BMNWZkbjc5YVFaK0trMXFmOFBNUCt0YzhoTkFkRWUzanZONVVrWGNKL28zQktEWGttZlZm\nWEJ3WDAzMXJwWnhBci91UWRFc0ZzVjBIVVphS2paNFdxVjFTRm9RZnJMNFM1Y2RldlJYdmwxLy8z\nell1NzBEVVpXaDdlKzQrOTErK3ducE5mcFVld21pOU1MRHYvUlFZOC8vMmdkT2Jkdno2ZHNQUGZo\nZUgvUTcvTWo3djE3L0xKTUdmNTM5ZVJqOUV2SGpBTDhsL0tFaEYvNzczc2JoV3dBMUtwTVRvN2R4\nUFJKN2x0R1g2c1ZxSWFrbk05WXdtdCtlcGdVUkhhd1BBeWlxUDBSd0ZVdmlSVy96bUsrQ2ZYa2s1\nWGVpT3JQMFFvY3laaGs0T2ZkWW94aVFUVkpuMHA1dVBEbCtMRHpRbXRDU09ISG13Q0NYRmVIOHlu\nL3c3d3JFcUpyVEdENzlPS3J1SzFudXh6U05ucVZ3VWlUOWdpQXRhajQ2aUo2V29qMUhWZnE4UTdX\nc3h3ZzR0R2ZQaDh5RER5NEMrT1ZsU21UY04wU1NTYUpvQ0VpZmcwMTYybHFjSkg5SHdoZVk0dVhp\na3FOVFhQejJRTmVGdSs0T3hmMlNtSEJtYWd5LytPY0pucysyS29VMjNINndYZEhTN2g2RlpDcVVJ\nNDNMcStXWkw3Ni90djBkSDJzZU83WmF0S0xUSUJmNjBxTzl2SFgzMmk5Uk5QeFdtMDc4MXRHSDcv\neVYzc1lKYmQ1OTc1K1phUGhXbTB4ODh1Z2pkOTR4eUZWZHR0dkdTNEcyM0x6L1I0SDRuc1RhdDU5\nNDlKZDZsaFJiM3JUL2JTVHgvNXNpdmZXRmgrNGNxQTd6L3dOaXZoeHB0VzM2TXdBQUFBQkpSVTVF\ncmtKZ2dnPT0=\n'),('e000','신청자','','','@','','','','',NULL,'2025-03-18',NULL,'','','인사부','사원','',123,123,123,'',NULL,_binary 'aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUl3QUFBQzBDQVlBQUFCRzZjVCtBQUJWYTBsRVFWUjRu\nTzI5ZWJoa1Yxa3V2cVk5MVhqcXpPZjBtRTVub0R0QXlFQUNLQW1UTnlDYXk1WE9WVVR4WHFFams0\nQTQ0SUNkOWlySWZDRU1ON2tvUmxINXBYRUFnMGFOU21RR3d4QklaK3FrNXpPZnFsUGpIdGIwZTc2\nMXErclVmT29rOGVvZjlUNVBKWDJxZHUxYWErMXZyZldONzBKb2hCRkdHR0dFRVVZWVlZUVJSaGho\naEJGR0dHR0VFVVlZWVlRUlJoaGhoQkZHR0dHRUVVWVlZWVFSUmhoaGhCRkdHR0dFRVVZWVlZUVJS\naGhoaEJGR0dHR0VFVVlZWVlRUlJoaGhoQkZHR0dHRUVVWVlZWVFSUmhoaGhCRkdHS0V2Y09zZmgz\nL3AvWlBYdnVnbGM1MFgyYmFOL0ZyTmY5Mk5WNTc0eEoxZjNaR2VuaGxIUEVMclN5ZFB2K1ZuWGxa\ncVhQZlJPNys2ZjJ4NnhxdVdDbnpodnI5NTVPalJvK3Jqbi8zbXZrdzJuWXlpcUc4ajRQN3JaMDR1\ndmVYblg3WUtmMy84VDcrVVM4M1A3UkMxamMzMjJSWTYvY0REeGFOdnZla00vSG5rdzMrYjJYTmd4\neDdiU3FIYSttcmg4RTljZTY1eDZmLytzM3RtSnVjdm1JNnFGWFQ2NU1Nbmo3N3Bwa3JyNy8zODI0\nNk1QKy9GLzIzSGFuNGgrcldmK2EzSEVicVA5MnJYMjM3M0V6dkVjclIyNjYxdkNYdU4zU2MrKzdY\nOUU1TTczUFdWYy9uWDMvVGM4ejJ1b2UrNi9Rc1g3cjVnbjlQWmYraHpGVlhQM1B5U3E0cDlCd1lo\nOU1tLy9uTGFUVTdzM1dyOHFuNlYzL01uNzNuMDJMRmo4c2lSSTJUSE0xKzJuem11ZzFDamF4YXEx\nVXJxYzUrNzdkUS9mdnJUMWRidmYrRE91OGVucHZiUGQ0NzNZOS85ZnVuM2Z1WFZwMXV2WlcyOWMv\nU05Vb3BmWWhaRFdtMityN1JHR3FNSEVFSTNhVUplaTVVOEpMVkVnUkJ2UVFqOVUvTm1Gdms5ck5S\nbFNLbkZTaXAxSTBLb2lyRzRCU0YwNWFCQlFaaG9aVnNmUkFqOUlmd1o2dWdGYWNHUElrUTMyNlla\nVWtqK0MwTG9GK0h2VkFaZmdSWDVLRllTYVlUK0NpSDB6c2ExQkR1SHNKYS9BTlBCWWU3ckVFSmZh\nL3M5U205QVd2OEdVZmo4SmM5Uy8rUGg3NkNGbmcvQ3NsOVhkY3AvZ2hCNnJPdkQ2NjZqaEtEM2Fp\nSXY0b3IvQmNodzV5WHA5UHdZeGVxRFVxa0xPai9UQ0dzUzRsOUdDTjA5YUdqOE1yL1NUdWlQZGs3\ndVZraXBrSlpxYWVyQWRUY2lkS3p5alc5OHc3cnhtVGQ4MEtGMEQzd1dEekZHU09Nd3hjWmZqeEQ2\nVnV2M1dXaTlHQXYrenM3eEpoYTlGeUgwcHJackcvOTR3eHVPcEdaMjdQbXZ0dU1lTUc4UXZmbGxT\naEVQZzRUcHFKSTdHR01INC9ldFhjM3hPM0tFOFNoNk5pRmtyeFI4SjFFNUF1OXpIajJUTUhxQXFz\nM0dkSUl4Q3dtdExtejhUUkNlUzJmR0xvdWl6WW5OR0VQWjNIajZ0Yi82KysvOTVIdmZBYXRKMG1M\nMlFZd3BpcUxvOGRiN0tTUXVwWVFldEcwSDdwWnQvZXpRMjk3bTdkcHo4WTJXNHh4a2xuM3c1YTg4\nL0VNUGYrZjFkM2EyNmNpUlQ3bjIyTmlQVWN1NnI2ZkFWQ280aXNJckNXVzdwQkFQOWVyWGEzL3BO\nNjZ4SFBlbGhCQ0NXRXYvTlV3dUMwV0YyZzYwQmFUV0U0eFpCN1ZTZlVXR0VJb0VqeTdJT0JvNlhF\nbW4wMFFyZlcwNm01c1FJbDVoQ01iSXNtejB0SU5YdlBDdk9nUUdVVDJmenVZdWk4S2diYnd6dWZI\nczYzL3BmNzNuRXg5ODU5bm0rODEvWkZON3AyYm5YN1N5ZEhaRGNCSGgxdVlSUkJsaEcvQlAzNitj\nUFhQeWtacVNTdHZNOGhxWFhKVzYwQW1xMWRMcHh4L2FjQjF2WlJKTm12Y0QzMTgrYy9MUkRhUjB6\nMlVmZ0FsTllFcGFCa21GK2RWRkVJU1dhekFhbjVyZE03ZGpKNnhXNXdoejExY1d6aFlqSHNDQXlk\nYjc4U2dncHg1N3FHVGJEZ1ZaYlAwczQwenRtSnJkZWNQeXd1bWk0eWF5ODdzdWVDVkNxRXRnQk5O\nVFU3bXBBNHhhejBRSS9VM241NGYydlJ6N3ZyOXc4cEVISmpCQ1BmZUx1ZDE3WCtFbWsrVGM2Uk1y\nR09ITjhkUWFFV1lsdEJvd2l4cnRJREk4ZitieHN1UlIwSHFMRGhETHNpb3BkOHcyZiszY2lZUVFo\nZlcxeFFuSkc5M1h5RXVrME15T1BUK0tFSHB2TExiMThSSTRIdTh3YkJ2dmlhblpYYVhkRjE2RkVP\nb1dtUEg1UFZlSFFmQVE1OUhuWk1TNXhtMGRKTWpGVC91MTM3OHRLd1ZmRmxMOG9aS29xdlhtYzVw\nTnppU2xpcjRVUmVHcTY3algwNVFlQTJrUGc5cDN0ZFpmUVppMFBiZzJhSlN4UGE4NWVGTHlrbDhw\nLzE5RXlVYnpFb0V4ajZJckhEY0pIZmdjaXBUUFVmQ0ZLQXdlc1d4MzdOQ1JJL2F4bzBjaldIY2wv\nNXZsa1BNUE1XcGRnVENiYnYycG5iTjdyb3FDNEtUZzRxOHdDYWUwVU5lKzQ5MS9tdnY5WC8vcFF1\ndDFMSlBZSVhqMFZTbEZjMUswSW5kZ25vVkI5V3NJa1grd2JYZjI4RzIzV2JmZmZITnpVdnpLcjd3\nbmpUQysxUGVybjR5aTRDVEdkSE04bFVJTTRTbEdhUXB0Z1Vqd1NFZnlVNUtISzRoc1RxcFdZS3d3\nSWVTQVNqb3dTeGYzenM2eUtQRHZZWlIrWGlNVlB5UU5rNzNtY2M1LytEYytlTnZzdTM3cDVzWEc5\nNFVJaXRWeTZmK1M3dkcrM0Uwa1lZTENsdDh1TUc0aThlenpweC83elB0LzgyYVF2aTY4LzQ2NzM1\nSE1Ua3dMclZha1FCK1ZLanF2US9LcXh1ZlVJU2t1MWQyLy9ZWlgzdldSUC8rWEE5S3haeEE2dEZD\ncmxMLzU3bC81dWM4T0doUVFSTS9iOWR2MWZWcnowTi9ZMkNpODh6ZmYrcXJsMXV0ZS8rdnYvNjk3\nTDNyYVQ4Ty9xMEV4SWd6OTlXKy80WlhIM3YxLzd6bzhqL2JDbGhsZGQ5MHRsSWZQT0hQa2pUL3hx\nWS84K2IxdkVvTHZiYjJIbDhvOGUrbmN5Yjk4ejYrLzduZHl1WDNaWDM3WEIvK09XUml1YVJNWXkz\nYm56cDk3L0krU2llVHVRNGNPVVZBbVVRdHlIcklxNWRJWDMvT3IvL056Ny9uVTMzNWdMa2lBWURV\nRmh1WnljNElMKzQ5dis4QnYvZUFiLzl6V0Q4QnRuLyszM1pXTmpkZWlMYUJERVdKaTMvcmJiL3l4\nRTRPdWUrK243bjRkb3k0WUxOK25NbUd2TEozNy9IdmY4Zk4vMTNHWjlUc2YrK3pudk9RVWJQOU5n\nZkZyNVkzaTRzSTczLzJicjJ0cjUrRmZlL2VQWFhqSk0zNjI5VDBqc29jT0hiSzFVcFBWZkw2cHdI\nYkNZamExcVRXQnRLN0ttcS9COG1DTXdRd3hNeWRmWFBVNEQ4dm1wb1NPTVdwUEluUk1LYUg2YmtV\nTnZPY2RONWNvb1pOSFhuTUU5bUNFRVZHbmp6OXM3dFdLUjA4ZS95YlNHci90QXgvd1pCVDZGR0dq\nMFVuRjFkaTRhUXU2L3ZxOURDTmtIaTZtMk1ZVU4vVUVlUEFJb1psU1lmMGUrTHRRZUx5b0pQK21s\nM0F1NmZ3dFRJZ1hsS3Mvd0lpRTh3ZGVsdTdWYnFHNDJZb290ZEtJdEs4V2liSEppNFhnMytzbExJ\nQ2M3VllJcFROYmpRMG9JMHJwTnF1bUZ5aGx5cUtXdVY4VWhwaExzYW1RYklJcnJiN0JzTFd2NDFm\nVTk3LzJyYTd4ZnZqeGg3NmxsTlp2T1BMUlZKdkFURi80L0xSU1NxNzkzYmUvMzdmaGxLVVlaWk5V\nU1ovWWVBcmVzeXc3ZGZqd2JXYVZFaXB5bXdvV1pkT0VFdGdLTkdIRTJxcXpiMy83K3hMVXNpYlIz\nb094WW8wVTJYUGdrcTZIZE05bi9uQkJTMTN3Y0dvTUNWNGpsQm1GRmh1OW5KcC8xM2JsTEdyRnV4\ndldlb1lTMW5RVHpCNzRvYVNVR24veitKZS8yM2d2aklJdkU4WTZCakMrcDVQSkxCS01xNTZyeG51\nMW14SEw2QXlNMHB6bnVtM0tOV04wdndocTdkWlpDemFxbFFSak1FWkhldTh6ZFNoTU1DRTRPZWdh\nMDE2TUU0U3dXZmkzN1RqYW9zenRlWjJTMzlRYWRTamJpano5T1ZkM2pmZTl4KzVZRXB5djU5S0pY\nT005MDlqY3p0bFpyZVQ1WThlUDlUWDJNU0VNMmRhc2lLS2E3YVRNdnE2VmN1Ym16RktNeHRKWngz\nT1RJTldZVXBxaEZ0bHk5alJRTGxjMFJtVE1IYk15VzEwcnBUenJldGxwNUxrMXFhUjVZSTdsY1Vv\nczgxQnJLMFU3akNLendtaU0wb3pFc3c0d1BqazlxNFJZdnUrdXUvekdlNzZNam11RWV3aUVSTWxF\nc29LUTNpQzJHMnZ3ZlVBSVRTQ2JUYlM5aDlCTXBNUVArbjZIV2dwak5uSDQ4SHpQQjd0ZFlJb3ha\nWFIrcSt1NFgzMGNZOWx6eGV3RnFmZ1o1aVRNQXRFVUdJdVNlU25GNmNFTkFrbW5jMXpMR21HNDNr\nbE1FNU5wczF4aGhCM01hSEQ0OEdHR01FNWlUTG9jZ1AxUUtKUTBvU3lKMGs1VGt2dEJLWFRXSXU3\nVXZGVUlZUlV3bldBMFpOUXhEeXpyRWx1anVrV0dhUXBSTW5YZGRVZk1La2lJTTZlMVBOTnFJWlRY\nVnM5cnBLMURkOTdaWnJGSXBkVEJhUlFoU2RZdHh5aVRmWUVKY2doeG1vTUtqak9OVktJYWxVLzEr\ndzVsUWhGS3h0Snpja3ZGZDFoUXV2V1lsMnZsWlkweGd6WU9jMCtsMFJtYldSUHRBa1BJTE1MNjVK\nWU5JblNlRWUwckVacFZoVHFPRmd5Qk5ZUXFVV0JYUzM3Z3pNMTVTR3UzTGpCOTdjQzJUcFFmVkFn\nanoyRzBPZWg5b2VVaUlXVGk4T0hEd2p3cTh5T3lpbTNiZk5mTDVPeUU2NW1WMHFKMmltS2N1K1Jh\nenl6cGpLQVpMbmpiUXl3OHZxK2l0YWp0ZTd6UTl1RENXa1hmYzg4OU9rUjhGUk05c0YwWUUyYlZ0\nd05BS25XaHB6UVM0MUcrVFpGdVJiR2t3QkROZUxsczIxYjJSSUdOcVJTM0lYVGNUU2RhQnhhTzd5\nZ1RRbmtwYzlEb2kxdUJZcktBS0c3ZmtoRENPYVhRK1MwYlJjaWN2MUdORkVIbXh5Z21nam5VU0I5\nQnhORWlDcHdrV0N2WXdaUk9YM25sbFF5VEZnL2c0QTVibExFdHR6R2gwWXBDS0kweGp1K3JOWllD\nVlJGU3hud1dLbktrbHZXdFZhY3dwYWxjYnM0OEZJM1J1SlM2clovSGp0MGt0ZFJGMTgxbE81Vkkr\nRC8zK1RyUjJFeUtBU0NFMHVic0xsQ2N3VnBWamg0OTJ0ZVZZRHRLRTB3OHk3Tjc2a2ZiaHNLS1lE\nSU5pcjBUSmZxT09mUlhLVlZ6YkpZWTZyWmNyR0pGa20wQ294RktpSTNhNnVCdmFrVUltY2tYRnFS\nV3hPZ09XcWtBWThzOEtOZDJyY1JZT3BoSXBST0VVZ3VzbmgwN251bHFpQ3RzZ1JNbllNUUpRUmh2\ndVFjalVjb2pxWXpBYWkzMWtWdHVvUkhWRllxSVdRV0NjczN4cXhYamdWSlNwQmlqVGpxVk1ROEZL\nNXlVVWJUUzNUZXlUaDNhdGgwbWttazlOemVuMVRxSFZXTGc0R0tNTlcwUkdJczZPYTF4ZnRCM3VK\nUWFFV3hUNHJUNWlaNHdzQVpuekxpemU3ZnJCOUhBTVZkS0ZKT2VHbW9yNURJb2FCenJpZ0FDZXhu\nQmlFVWwxWFRhOUlJR2k0ZlFTYzRqVUdmcS9odFZKWlNhRG1zdFdVbUZBWGE5SkFGL1BjYmpPM2Rl\nbXNSa2E0R3A5eGkwNVMzMzROQ3ZsQkd1KzQvQUdUZy9iMXVZbEFtTlY3cWtsN1NaNHhtVEVsT2Na\nSmFEV1NMZXJyU1dkaEJzZFBWVGFiMkdzVzViWVZ3M2FkcWRTSndGQlptOCtjTWY3cnVFWTRRMXhy\nUzVKUkZNY2dqTDlTRjZ6QnoyMUFpTTFsb1RTak96TXhlazNTMEVCaWxkSWppeHBlVUZXT05oUmVs\nTmZ4M0o1OGN0aEtnNmRlcnZhNE8raUJHc01EakhVcE5NNjFoM1VKcVVLWTZ0b1NnTTJlTVBmUTA4\ncldsTUNNUXVNc25aOFN4MFpKaUdRV2lNa3EwRnhnbHRYelZYUnN6RGRkZnpDQ3RUS3pheGJkZHlr\nbDQ2UU9nUUpZUWxJQTVHS1RFUFUyT2kvY1VIdTMwYVdxMXBwZHNzTkdyYjZPREJneHEyRlkwVVQx\nVlNmUzA0aU0wU2hKdmJLYVY0VENHeU5xZ2ZMcGNhSTB3WTJ4UzBKd1dzRldQTVN6clQ0MHB0cUlH\nWEVsTENRZ3dsTUk0WEJLUWxLRW1TODVNSnJIWFU2Y25zL2hXc0NLSHA5TmlFQytFOUFLVzRoT3NQ\nZ3pDTG9uUG5Ja1JwR29KaDRCZHcwOTY0bHJGemJlc09JNFV4TXZlUy9ZTUk2T0RCWEtqcmpqbWxW\nZVFrVTk1cWRhbUtFVXBDZUlDSHZsMnJsSUpYdi8zWllNbDVFT0dnMUpwRDExM0g0TUhmZnZ2dFhY\nZFhTaFp3cDYrRHRBeVNSbVdhU0k5dnNSMU12dm5OOFNxRU1VMHJvZm9xdksyZ2JPdEpNZ3hnWXRx\nMmkyelhuVktLREJ4eklsVko2cWhueUtNVDQvazgxNUxMTyt0V0pIRVNibEpqNUcvZElLU1paZHZK\nUkNKZFh6WEFPQ2hpRXVzT2pERU1RbWRobElFVmhqTEdITmViQmpmbGNCMkdMWTlNZ1JKTENPMzdu\nWnR1dWtraXBSUmNoeEVKcUcxN2p6Mnk0SU9pUGVuT0pKWFFWcWxXRFhhTmp5ZTAxbVpRR0dWekw5\nbTF5eUdZUWorNzdzMkVMakxDK2xzTkdPVXBSbjB0SlF6YUVjRTVOVWRpdlFEckpPWjY0QlpmL3lK\nczgwL05DcVBpQ0xqTnJCbndhdzI2VkdKWkVVSU1wY05BVHBQV1NKNDlpNHdlUTJ4WHB4RGEydldz\nRVVpd2d4aWg0d2dqQVI1ZVA2aVdNRUxqMTExM1hYT1BzOXhFQnZSWHloaXlMR2NPSEJyRE5BeGpw\nQkJoNDYvKzVmY24xSmJibUVLdmZ2LzdFd1FqbnpMbGhXZStHWURYYXRySjVqQWoxbGc2RVJCYkp3\nZ2hEdHdLTEpqNTJXZUFzNnJudGlzd3JVckIyM0tEMmo2WFlwVVNQRDFRdjhNa05jYlN4cHFpak5t\nU2lmSVFuVllJeHpyZ1V3R2pDakE4SDRiMUxhQVBtSFNxTnRuYVNkcTgzckZ4Q1JYTjVDTmE2eFJH\ncEMwanJSOGdWOER4RWhOYUtwNit5TE1qWGkxalF0TVhQdnRsbmhEQ1BHU01ZdVVSdGlWcTJWTnFD\nS1gzeElsVldERmdXYytNajQrbHlCYmZBWUdjMVpOcExGQk5jNUdJdDFPc25XUjZnaEhNU0NJWEpP\neE1rbUJpYTYxQUNaMllHQi9MSUUxNlRvekZVaUhRcW1XajdvRGthaFVqMU9iSjdWcDliWnQ1bWJH\nNnBhVXRKTHlCT2lFQWczMUd5UVRrRXFFbkNRSTVicER6WXJ2VHAxQmZmNkVCbHpJQVY4cXc5emFw\nR1RSclZpU2lPVW9SckxZV0dOQTBJUS9Jc3FhRlZOeHlVeTRtdU1Jb2RlZG1wc2FNRDliWTdadktv\nMlZiUXpZS1VpUzFvb1E0ZS9mdVRRb3BWUlNCSTdjM1hDK2prMjU2REZ1a2dtbTg3VUJjbDVyOVc5\nSnpqejhjdXRueEZNS1l3ZTZGTUU0bkxTL0xsZDlUWU9iUUFpanJvRWozOUg0cXJOY1VSUU1jYkZw\nRGNsSW1QV0ZXR0FYcElCdGp2WUovblYrRFB1ZjJib3c5ZVc4dnN3UklydTE1NDJHdE50Qmhtc2hh\nc0NJUDdmOVJXbUZreGI0b3BobExLSUpMVzM4TGNRTHVPVVNTQktQRkZMVmNZdkVLTElTTUpiSlkx\neVBFQkxjTTdHYWk1elhYdkhCRzJ6VFI2Y2dMZ2dEWlZzSldDdG5naThHV1p5RlVSTGFUbE85NDF4\nMFRWcEpkeGpCUmdrZms1S1AzUC9qcC8vT0JGWXlSc0MxclF2S29pREUxYm51dGRjMnhyUEZhaElJ\ndkhsK045dTIvT0Uxb25JT0NNWkdJSXBjaDFqb3g0SHNnUVA3Um8wZmw3MzdpTCtoclhuUEV2dU9P\nbzEwUE9wUzY1R2pzSGpwMEp3WEhWNi9oZ1JYVmN0ellQMFcwUG5od2RXQ1UzcE9SRDFLS01IRzhN\nZEgwYy9RQ3N5eTlmLzkrSnpGM3dUeU1YMmZ3cVZ5cHFOTEcydXpjamwwSUpsM3JaNy8xL2p1ZWhT\nMW1KbkcxV0N4OThMZmY4SjBRODRCWlRyYVJUbEx2Z1hySHJYZE1XS28rM2xxUlJ4Lzd3VU9mK2Np\nN2x5bXpCSlBhQ0JpanpITDlXbVVKYlFHRkZPZ3hKcG1LRVJ5SU1FeWNXZnArWWV6cE13SXhlOHl5\nTFROQXpMS2JBcU9FYkZvSzN2VFV0UlRUZlFqak5pc2xxWlNtdG1WSkpkTmFLOFdrQWtWUVI2ck1h\nY0srakZINlhxUkpSSmxsSjlNVFJ4RkNmOHNGRHlFYVhsemZXQnlibkluSFQrc3lZMlFNSWIxeS9O\naFJ6bS80bXd3OFJKTXNnVkZKU1VHeDFnMkJJUmMvL2FxclM4V04wMHRuVGh5SGIxUEs2UGd6TXVD\nZzZ4S1k5Ly95ejlSdStjUmZvS2tERDhCcTFtTTFqc2NjVzNYckJCTmhsUE1COFAwdzloOXJqVzNi\nR3JnaVdBNlJMRHMzUHBrYi8zRUlBYlRtM2dLbzYvRktxZkJNME5lMGp2VVhRbUpqQTF2V0d5MUNM\nNE54c0J3YlVrbGZPeEV3dit5eE5Iamk3N3N2VG9EZktLK0lTVy9uWmN5aTcwV0lSQlFqTzJWbjNn\nWEphcTd0aGxqRjRSR0dsSEtsME1aSyt1bkRiNTE3em90LzRpZVM2VFJSOWVUaEJvU1F6NVZTZ0hz\nZFM2NENpOUJFNGZqeFVGLzJFbTR4bklzRVRCaXpueHRwQnQxQmlxaTVjajM3ZVQveVBNZjFycGFT\ncTA2bkZ5Z1p0bVduUUJ5Ykh4Q214akxqV2N0MkxsZEtDZ0xSY3NxdUJvRWh6SWI5YWtaUVVwT0tH\nNEVoQkplMDBtT01VZkJZYThkMmpiVUdVRXFYaWVWWUROdW1uMi83blU4OFBUdVdlM1VRaHFjK2U5\ndWYvODZKRTNlSDBDaWJUc0xXa08vbHlUMXk2N0VnbWJnRStqWncrNGJNTzlDU0czOGYvY2l4bDE1\nd3lZR0xPRzh2UEZBYUpRa2hicXhQREFhT2hIcmVDMjZZbXAzZGRTTzBCU1p2MjcyVWxybUo2VjJx\nbmx6WGlreDIvRkxMc2krSDUyRW5FdE52T1BMUnlZV0Y5RnIySXBsNDRVMDN1UTJCa1JxcnpOakVt\nR1c3bHlzZGp6ZkdacncvaHdnS0VZMlZmcVkwZHlpS3plcGtadnFabExBUElRMmUzSGFoaDZUZ1Jy\nNUxFQVZCT3BQMVFObTgvcWEzaHN4bTQ2Vml5YXhTV3V1MEVYT2xRTWhLNERnRDdMMzQ0T1dwVk9a\nNjNwTFkzVFlvR0VQcVFuT2c4L2s4bXQxMUVVc20wemJua1cwN0xsZ2ZsOE5ubnVmNmdhOHVvU3J5\nWVJ6TTl3a3RjaUZ5amQ5ekhDOERpYy94WU1nU3N5MUdxR1VlVGphWGUvNytwMTMrcW1KaGJlbFp6\nOXQzNjRrVGFBa21Kd1EzRUVKbmVyWlBxNktUTUNrTVBTc01BRVJwUGNkempnYk5zUDQxWnJFM0lv\nUit0SE04SVluZlJFT1EzbEk1RGtLdUxuN2FzM0pUcy9NdnFJOXh6K3VrN0NFd1l4T3U2M21PRkFJ\nSnp2ZUdRYmpyeUJ0ZnNQU2hULyt6bTBqc0FzdlJXSFBWbXE4enVXbnFKanhid0hqYkRoZ3Racnls\nVWlIa09NRy9HWUc4QW91YWdkeTEvNUlmeXVRbUdNUUtPaHZGZVQwNUt1NmtEdy9IakFqR05Zekpa\nTkpPRzlXY0VBeCtHdk45UW1pSmdNSmtJdDNFY2x6UGZMOFQ4Rk9pWXdiV0J4VlRDb3VnTXQ4amxK\nbFlVMUNyQllTU21jZnZleWk2L0NVekprRkxSTHlJTWRzWCtQR0VsVW8ydDBZdFpVa0lUaUsvWWo1\nTXBjZXVkTndFY3R6RXpNVlB2d3FTcDVac3grVVk2YjZXRU1aNHpjSnlvQWtNM1Y0ckxUczdKbmVa\nenZ6cTczOTRSeW96ZGhYMEczd2tuWDN1WEhVR2dZRnk0c2I2ZlMrQmFabHJIZTJHdUNpVURXbmtl\nalpPZUtuWTd3TUdGVE1UcERrQmNIMjhvVUlCRTRvWXRjeDRSNUVJYkRzT0RCT01DSlVrRVlMalBK\ndWJ1QW9lVHExYVFYNnQydllTY1RZaU5CYmIxS3NwTGVNa0txMnJHcUVwTzA2ZWd0UTM0ekZWRXZ4\ncnVxTHF5ZVJTS1I0R1B1cjFpa0svNXlBb0RjOWFtTUVRbk1QT05RWjd2dURjaDhqc0F3Lzh2WVQy\ndzdWYzhBMElYZkM2ZWE5YUJFWnBWQ0pTMG55cEVFTDdIUzk1cVYrcklNdDJjQ296Y2JGcE4yRVJa\nYXl2YzA1aHZvcjExdWtYbHJKdGphaVJCTStaMkpmTVptZXFsVkxYZUFaK3RlOUswUXNDcG5tZjhZ\nTVhqRTh2Z0Y3WUdFTlk1SWdkKzMxQWpGQTkwMkR6MnBieEZoeUViUXlpMzFwSm41STRIa2M0NXlT\nZ0tuemIyMzdKWmN6Wm8zdnNnNjJBOGhNSkRqTnNHZDFCS1FueHBLbml4bkp3NU1pL01JU1JpZG9w\ncVVRWVZDdWtzUzg4U2NEZ1lrSlNoMis1eFpOSUJlQVZqcUlJZ3dEQTV4YWpHMGpMbkpkS213MmVr\namhsMC93YjY3THJwdW5NcnBud1YzLzF2U25HMkN6czk3QnFPVzdDRkprSkhnVzB2dXoyYmdCWndS\nVDNYWUhNV0dpdGs4NkVMZXY2bkpmTFhRanUrdTBJeHI4bnpOelZzYlZER2NNdWl6TU4rbzQzUnNu\nWjJRTkptN0dBTVRKNXlHd1VHT0ZGdE1qbDVCN3cwRTczMmdkYm9iVEdGYjRXWUJybnhDQ3RTd1Ro\nS1JFR2ZpVjExa0VhbTVWSGFjVnJsWElOZk9aUFJXZkJRc01ZZStQT1BzOUJMQ0NFamw5d3dZME1Z\nMm5DRkpyZ290Sm9qTEk0ZGtWcGJFb0NwRlpsTGlWMTUrM0lucGthSTRUbVRHRlliTEthWWp5TVVZ\nM1NBZms0b2NvcmhXSFBIOWlmcEdkWkJCR3p3cmkydTdmWEZ2d2ZDVnJQZzJhTUtZendnTENFaGtG\neFV4ZGU0cm5KYklBd0hYZGUvWGFYSk5JWmZmdmh3eUtUblo0a0dCbjlZeEJnbjFzNnN4eEFrcG41\nbTVDU3huZ3FPVHZsUjFFaGdUQnlqWHNCbzlBaXVJYWxjWWc5ZVlERUkyeW41ajJYTUJKQktQL3BU\nNS96VENEeTBDR2lBbGxFU0k5VkN3WFRBUWlVUWw5Z2l3M0NzRnlwYktCZmZPbExvOVQwL0RnbUpO\nblFzeWlMazhRejZVeUZzTTJzdVU3a1Q2K1ZNY0xXa2V1TzlQVUlFNnExd0RXTGVvNFJHSXJaenY4\nc3Ewc0RydVBGSGx2d1RiVWt5SGNDZEI1Q2lEMCtPZU1tSENzaWhHUm1MN3dzVFdURTRlbnFwSnVZ\nb0VZejJ6cjBzLzVvUGxSS0dJSFJDQlVacFpPa3pJTk1ka2NDWTF4ZmVYQVExWVNQNmxiTFV3S01y\nWVNWY3l3dnhRbWhTVzl1TmtrUTVvZDJYbXZ6eUM4UlROS1VPYVlER21tVDZHd1VacVVycnV0aU1F\na1p3aE9NeFhXcjVtRmlBZzQ4aktpdUVSd0hVbHR4NE1BaFk0V1pnbnl0VlhEdC9NQzBBSitIbGlZ\nNkZoaEtaLzZ6Q1F3bThRNmdrUmEwbnNzMEFBekx3QkVhQzhnR3NOTDJHS2xWUzJhQVBjZWJvTlF5\nMnZzZ2FJWHgzWGZmR2lHdFRmeERjMW0wYkNmNzJQZStGVXg3WTBtTXdOT0lZVXZ5TjhybkEzaEtU\nNTBPZzZsQzBxYVdKd2dtTGtzNFdZeHBkT0FaVnppU29oSmwxTXRPVE5Zci9VeFFGWFFzWk51Snl0\nakVlR3l0WVRRT3BuZTh3aWhFS0lHdGl4YnlwUURGVmxLYmhNOWV1Sm1KcDdDdW9WbTdiN2lERXFw\nRkpXU1Y5WUxSUURHaEUvL1pCRVpJYmlZMGFNS0VERkxpUVFuUXVCYldMRCtzU0lTSm5VNTVPWERR\ncVViblFIRWVFaHJYM2U0S3NyY0lWZVd2bndvRlJTbDRxUEVWdW5wbU9SOXBGWnZWVHdVd1VCNzRu\nQkVxSVduY1NuaXByT0F5dEtMQVUwcFdDV0ZjQ1JHWWdqVU1lYWlnOWdzVmhaV2FFSFdub0ViallE\nTEdUVFErdy9RYmpoeHhBMW56RVNIWnQ3LzlmVTNQK3dNUFBLQ2ZjY1h6ZGpTQ2d3VHBnc3NHVnhD\nNHVTelZ4SXFnQ2dGVEFnbGs2RDhUcEZEeHpxQ1ZnTURuNEtzMWpnTEpsQjlKVTh2UHZIRkNiRHRl\nd2pFYkgyWXhnT1IwK0QrdDE2Y3BKY29Ja3dyVU5FVmhBSXF6V1ZUQTNONklscURTN2lrVEdJQ1VB\nZ3RaQllXR3VvNDNKZ1VQZE9Bbm9wb0Z6c2RLRk5ZcWlRTUhMRUpwQXA2VjFwb1hOL0pCdFZvMlQw\nNGpuR3YyMC9pS2lIZkJoYzlOTUk3QVZFL2F1M2FrV25OQnB1WjM3ajZJcG93UWFZeFdFVFlGZWow\nQkR0Nnh6RGhOZWFrbzkwQUJackp4WXY2bkFnUkc0NjVEUXB3SktCTFZKLzlJUTNVUndRS3EveUFQ\nemJYSFNUcWRpV01QR0kzaDRhcENESVNNTk13aVp0bGxyWlh4RmpLTFpnZ0Z5OXI4V29VLy9qanNr\nK2pmQjVnZ29zY0lvMzRvUk9KNHZoSW9yVXJNZGF1SjBQV3doaGdkQ0M0S2tZZ0NIb0s3Q01oM3ZL\nYjFaSjZsUm5abFBaL0lKZDBRSXUrZVk3ZmxpWGh1Y3RhMnN2WENMN1dDQnk3akNHR2hhU3FUNUVs\nRVhJU3g5NTl0aFdrQU5tUkNTQnB5dWxzaUdmMnZON1UwVm80a1hNL3MrUVRITWFDaGYxQnllYUE2\nWlJFaHEwb0trMTNtMkpaSm5xcWpmTjk5OThsVy93M003TTdYTmp1SmtPTXFoTHk2VDBHTlVZSjlh\naUh2Mk5HYnVCSjh3L095dFZ4cUR1b3NHbEhiZ0NzYU50d0ZOTlpaV21FaFFSTk9jandpR051TXRK\nZVVNTmNkVDQyNXhuY1JTYktHRVJtWXNzRjVSRFMxdWVXNVlBQU1qRUp2RjczR2I3dGppQW5aOUp0\nb2xFVG9JSGo3ZTBvMXhQazh5NUtDUnZBcjRDREpzWEs1MkhCSXBNMERHZmFIS2VQaDBvTG5UMldx\ndHAweUFUdGkyWmxHQjRUZ0VIaUVTbkx6aHRZb25VeG5nWmlvN1Q1aDZDTU92Q1JEZFJ3cmg5cUNt\nU3BNeU9xenM4VktPY2lrY3lBRU1KblhsemNXZ3RSMEpvbHB3MXJUQVhWWWFHSExkRTdLMWtwRG8w\naXo4ZmxKTDE5U1BEc0JBUXkzVFdBb0llbTA2NEM1L1VCK1lXMWpidGQwWHl1SlVZWTJDaXZFSmxK\nTXo4Mm1vQnIwcVZoaExOdldVZ1pXc3A2SDNuclAyRE8vZFhKZkE1UlJvNUFUeU9QSDJsc01IdmRt\neU43ZWpZVHlHWWFsUjVNdzJVSGZIV09WYXRWSUhNV3hTOS9jTEU3aWJ2c3VXQlN0WUJoRktjZDFS\nUlRXbVBSTWhyeXFaOXVaNjVYdTVHNjd2MXdxSkVWSDhGRXJ2WVBROXBxZ0FSQkNzMGhKS0hTQjl1\nRXNENVZQeCtOSXFwSnlyVmhZRHJLeisyY2dSbWJ1ajNRdFVJU25rM0haaUVhNnJjYUlVb2F4dzl6\nSEhubEFYakZ4T2JLdDlxUXZTaTJud2JSMTcyUEwxZisrYTVvZVBueTRMOEVBZUorcnk2dHkrdUp4\nbDJBSTRocUhveG5UVGd3N1FVRS8xUnB2bEVzYjlWcnR6ZTlwaFIyRTlmNmhyVkVjbS93Z0FCZ1Rl\neUl6NGZiTm9ZYXNlWVdqckEyQmRiTnpaSm1NZ25vT0IzWWJrbXZadHFFUmF4OEkrSjNOKzRMeFFi\nT09seWJKbWxEY0ZJZHBwYktObkJ6Q1dGdFNGaWI2WFZqalZGM25haUtNcXIrVHp1UmUwWWhWOWUw\nbkpraXBTS3dVejRjRXFZVHJqTU9pbFBheWxpLzl1SFJYQ0xFOEdlS1FZSll4bkFjUUFWZWlrcWFS\nU09ibVRlTWgyYnZSVCtPR3dSanhJTExEVTE5VitwblBCTWRXMndxRGdRbUkyWVpqNXZpeFd6aSsv\naS80M0NVdlRwOWRLdkdwRG0xR0tnbWxGVmhYYXFvV2hJN3JwdUpTWGlpKzlzQ24yZklzUUxrS3Q4\neTlOL0M1c2wyUFBXaForS2ZpWjdGNUp5NkNDeTNML2l3MndyazFwQkFtT2s0dFdLZXBOYjVuemky\ndGxib0VwbTY0OEdwUmhibWNkaG5Hd1BtWFpsQTNXZTlCWENKQkNQTDk2cmN4MU5TMmRsQ3FTeEtw\nOUVYTkg5WTRRS0ZPY0EvbEJlZUdBd1czeEcrUWJsOWhYditLNS9STU5QM0laNzY0WklRVDFIWU5C\nWVI5UWdrbURLTEN5dmtObjd1WkxFSWdNRGpGYWp4VUdXQ0xORUs5TkQ5L2JWaWlHNUJ0VjI4SHF0\nUWlLYWZySEhPWTBiYU1OTGhPS3VGODYxdmZVdGZlK0hvbE5XcGJZV0E4R0tOMVVpS3NNYnF6Z2h3\nMEhxbkNZcTgwWHhEVFdpQmt4QU1YR0tOQVdLUVVwVnE1K0NYZEtPK05jNTl0ak9rTGhsRkN0Skxr\nVjM3MlpaQWQyTVVHOFo1UC9rTitZblpLd3hqQ0M2TFRnMitHNG9tc01hTVd3MHBUbC9RcVp3YUJR\nVHJZaUVxMWFUK2RkandQMXNvVTBTak9sTklxVGhPRXZCY3BvNC82VWZSenJhOG9Dai9mdXVxQXNx\na3hUNXpKZnp1czFJb21GNFl4eUVTUFhlNWhXTjA2N1ROT2w0Z1ZRNlBBOVRmVGpJS25VWTFWSDZ4\nVi9JcHQ4cElwVFpTcStRalhTMFI4djd4dzg4MVhDWXlFVWI3aFpnU1RpbG9wS01IalpZVmdjQ3pX\neDZldXljRmtPWDc4dUFRaW90YTBpUGgzdGFLVTdHbjhMVFhLSXl5blE3WFEweVZ1V3hhbU5wZEVZ\nOGRzUlpSQ3U4OElyZHJHRXdmaG02UVNWVmlNdHhvanhtTDlxL2Z2MlZtSTRKdk9tZ0dNZzdIOUlG\nV2NCYW1rdEdDTXVCOTR2Wkx1NHhWRzFTb1AvM08xN0pmdDJCa3JFNnhSKzZ3UmJrcURVbUxwemYv\ndGg5dEtQVC95NS8rYU4va1lPclkrRkxaOElpUHYyNlhQODh2SksrTUNkeVdiMlhZYURaRW5iRnBH\nU0g1dEtWOHBGVGMwMGlvb1YwSTc0ZUZlSFZCSUY4ZHZ2WldUajExdm03K1ZTangyZG9sUDd0aG4y\nbDRwcmtNN05LTjJOcmFpVEZwRkNlcDBWRDN0QVRVY2kvR1NoVGJXVndNcEJEdzA0N1ZwalhMWGZ4\najhGVHNQSFRwaUh6dDJOTkpTcmhMS3BsYnllYjJ2UnlRR0pod2tJekZxV1kzRlEyTWQzZnhqVjdW\nVlFoNjU3a2h4NTl0dkJNOWgwcmFNUXZhRVlGbVVDTUdEOVpYRk5TaTFFWUcvL0l3REIzcmVEeWF5\naktTcG9SZFMyTEQ2RWFVOTNVT0hnYzlnbDdqampqdWkzLytoRzIwelhBaDVoTEtZcFFBY1ladE9w\nbTZ5UHFEd01yU2NHQm1saVZIaUswcTllNC9lSzg2ZVBtVzJMNDFReXJqY0lYNUQyM1dZZnNDWWtw\nV2xjeWVQZi9lYlgzemtCOS8rMStQM2Y3VUtwa212RG9DT2NoUWg1YmllQTM5cnBkeVY0NmRFbzBS\na1pYblJDSzVsV2JFdVpiTDRSQkg0WndTSGdra3pHK3A2QllZdHpGOWJPdmRZUTVqQWtjd1lheVBi\nQWNZd1F0ajA5SVZPL0w2U0t3VGpTUytUNlRQckdhUk1hS0I0aTZlOVNUeWxuWHdzODRldmgveGpz\nQ09yRWE4TDh4TUFjUndzb3FqNjhBUGYrZkx4NzM3anl3OCs4SjJIczRsZFhScTIwZFdpRUFWQk5l\nYTIwd3FTN3BIbGVJNFEzWDRZTXlHbEJOMVVhVXdnRUFkenpXM1NjUUE1ajhrVDZOTXdjQTBYOHF0\nL3I1VTBSTVE4REFMS1lscXM4dG5sTlhESEU4S013SUJhaEJVSFcyK1ltY09ZNWR5L1VWcTd3MlVl\nV2xHbE12aVUzRVFTRm12TG1PSlJaQlR4cFhPbkhvVXZKRndQOWwwUUlvZnpuS2lYaU9Cd3VXQm1q\neFNnZk5laDRqMWJpZnBLV3RlNm9kRE9MNVQvTVF4cmYyTjdYbGhmMElGTnRuMnlhSzBzMjBsa0p1\nZEF4VjFIb1Y3VEZocGpZVWpqT29tT0IwZ3dkcXMxRFpiL0lQWEVjMjFTRTN5OW1GLy9WQkI1dzl2\nRkhhQkVZRTFJNkZjcmZ4NEZ0WkFMZkc3SC9BeER0TGxoWkdBTXRWUm9kZVU4WDFvNWJWSlFDV1hB\nNFlNU3FiUmRLcTF6RVBMR2VJdjZlSytjTzIySUdCUEp0Qmx2eXBqVDFLeE5idjBBWUl6WTh2bFQz\nL3J0Tng3NkJ2d05wSVNPSGVzTy8vaVBuNjYrNXNnUmw5U3o3YVFRV2tKYTJSQUNvN1drdWR6VTR1\nZi8rT1AvMm5qdnZ6ejNSbHpNUzBoOHIxYkx4WFZJRDZXTW9scWwvRzB6U0pSNUptV1RNV3Zmdm9K\nWklhKzc3anA2N05qSFRZSzIxcHZtUFNiRUtOK1EwMXIvck5tbWpmVzF1OHVuejMwbU16RjVUWDBR\ndE1hNnpjOEM2NFB0T3N4TnAyRURlZ2lsaWh1WUpMMEpiNjZuVXc2MkpQTkFpRFZRTjVFT0k5TG4x\nVSsrNXpmdWVQVFI3MjJaMXpzSWpGTDB6Q3N1K01vN2JyN1o5UFhBdTI2ZEFIOWtIV2NyNWVJNGRJ\nUkg0ZU4zSHZzRG8yOFNnazNkdVdXYjBoaGVMbW96M3BWeWNWM0NlRnNVbFV1RmVMd1o4OHoyUll4\nanM3N0NtRTBydGdyYVNKMmJBNGR4TXBWcW1nVkpLeDFFVWRpME9HYTllUWRwRlpNYWFoM1ZPSzRj\nT25Sb3FMMlprRTJteXdibXBsSVdvZWpiV3F1Zmc1a01rNVdIM0pBMlJvRVBSV3JRVnV2WXNXUDY4\naC81R1gzRkZUOXUzWHZ2dlVZcW1MMVpCcW9VTC9tNURCYjE1UUJLdUdHcmlLSkFocnoyL2FsTDlo\nTUNGZUgxaGx1MFFiUVRYNCtCejR6WnlMRVN1K0h2NDlQVC90UFhORTdaa3duVnc3b0E1MTNKUzBI\ncGpGbGg2b2xmWGNJajRuS2E5SE5mOXBQV294LytIbnFpa01hMEpCbHRUNE4xMTdSTWxhb3ZBQVFm\nd2Rwd0prUGlTbVg1L3Z0OUtHM1dHbm5RdGxxbDVDQ0JxcnZtY2xiSTFiZnR4bmlEM092UVdHVmhM\nVXJpTWFNejFxZURHWm00VDRKekxYclVLMkNDdGUwbW00US9rcUJRNDAyR3pJeWJodGhKSEtRREI2\nNzJheXNySzNqL0ZoMnVGN0x2N1BwQVJleDFOejRIWnNOZFhSOWhWT2ZWaTNsTENFSXlzM2NhMm1J\nY0c0UlNvMitBTHFXUnFnOWlTNWNJZ1pUTVdxMWNPWlhadWRlamplaTFDWm1nTGxZRHNIUnN4b3hw\nZmV5bW0rUXpQdkhaa0tYZExCamtmZnZWWXZFcDFXREUyZ1FYU2xOaUpTODVjQkMydXNHMXJRT2ds\nTktNa1NTTzBIeXYrOXo4NDFkOXVmTzk2ZWtySEF6eGxaaEUyenhEZ2poNzAwM1g5Qnh2alZYS1dL\nbkF5Tkw2QWVScmhrR04xNHJGSHVuc0dQSzVtM2JCV2pVZkVaaE9kZFM0U0dBTUZwVEpqQXR6VFBu\nVDA5ZHZhVExDTXlYRWNLdTBLV3EyN2ZRM0pUMDNEYTV0SmFYNWpsQ0NwOTFzYzR2UVdqV3o3Y0tJ\nbHk1SnA5cFdPa2d6VmhxdGYzWHhnVHg0VVJ2Q1JCQldXa2h6UUFHSlZicllBTmRRSmhVNzd3d2tM\ncVlTOWdRZnd1OGZ1eGlDNHNHRHQrQk9CaXBNc0VQWjFseTlneUJCS1NNRS9KRkQzMmZmbGMreGdT\nN05XRTFjbW1kb0RSaHZ4M0ZOeUFkV21KWUhxbUpMaFBNTkpYaFhjUldHWW5sTXBnOGZ2czFJNUpu\nS1kxQVBUWXdQQUc2YXpTYmk1Q2t6dGYweUwyeGRXeHpmR0g1NDhpV3ZmdnZROUtORTQ5aDhiOVJD\nS3hTVmNWelFGaTg0Mkt4QXhpY3BjTm4zSzgySGhUVUdQaEZESW5UZjdiZjd0UXBFZmxxc0JJS2RL\nNjg4M0NhOHNIUlR4bmExVUx5dEUyWk5VZEYvaFdrRU82V1VXbkN4T2pYVnZjMkRkNVlOUWFLMEZT\nQzhRVzFyNlBzUVZ6UjNBM0JuYlhVOWVOVE5QeUFicEpHdkFnYWVNVlUxV2xKV1hDYlJCcTBWWVRR\nM1BoNEg3NDRkUFdwMnJqdnJnemhtSjVOUS9BNExsOVN5ZHZ6ZWU2UFoyVGpMYldEak1aWVkwN0dE\nbDE0OGRMUzg0Vnd6eEU5UURlcllJWXFrR1lEOSsyK3dDTUltWnhmYVoxbE9PWmxNNExhRUh1Z24w\ncVpDRXVzS2dhTVY2bU9nQ1dIT3k5LzBITnJLT2dIM1laVE1YM3Zva0prUUV1a1ZUTWcwcWllY2R3\nS211bFJ4OEUyWjgyZjA0dXJxQTZTVGdRb29zWEM5MXVvSnc4UnR3WWs1L0gwSXJ5UzBWbERPQUFr\ndmRCQWZEMERLT04wMVhua2JNQ3NJTER0aWpTTGNwY09BZThWaWRvSk9wQnF4Rm9VMTBWKzQ1WS9p\nUWpJaVV5RHA5WXVyeDQ0ZEU4UG1aUUQzVUdvUXcxTTNZdmM5N0g3R0JTbENhc1VucTd6aUZTK3dN\nU1VKYzJlbGVSUlZxMEhDQlY3cWVtRitUSXVCTkRhT05DRWlEUFRvcld5ZXE2ZVNiWEVaazhwSjZO\nUVZCNjQyZ2lvNVg4VUlUNmdlMllTTjNCSlZMd2xXU2tVSTRYd3FaZmVjUE1PUU1XOE40TUFoUTkv\nSGNZRlNoY1lWbzBPRUpneG5Yd3pZZytvL1dTL2kxbHF2OThyQTBoZ1lxQ3pMUzJlYWxoSncvVHRC\nWkdZZGo4STRGOGI4dnVHYlVhWHgvSmFOQVN2RWRsenNKVk1EVXgvYnZrUEl1RkVmNHUwUVM2RURt\nN0NZa1h6bkJaQTRWYmZXVkZqZTJLaU5qNDhqaTduMXRzU3JndFlxcnFIV05hSzRJUkdNaFE4am12\nWUtiVDRXeUtBSFZvcXAzRTRURmZjRlg4Y1laYlZxZUkwM0FjTG5weW9ZemorSW5jbmExeGdJRnRh\nNm5aRUUrR0dlL0pZVXA1b096MlJsSjl3c01KM0d0VWZBampCNGJoTkt6WGlibEhtdGVUMWZwWm5i\nVzZDMGg4QVlEaFFIT1U2TGNvVzFtSmpQeFRFbzJ6TnNDZlZpcWJvanF1MGdrWjZBSDRWaWhXUXFP\nVFFURTZFczlwS2FyUDREY0xDTUx5TnVCQ2JTQ09JS0poRWRGbXlHbEw5cnp3WGE4NUxtZ1JFU3I1\nNVNjcFAwSlNtaEFzNXh1UEpLRUJZTWlsMUZSYXcxdmhLWC9USmdXelRXM0ZwRmxpQlREemlNT3Rz\nV1JiNE9hZ25NUldTT2lzTUlVajl4cmVEMldtRk0yR0htMEtHdDlZaEJnUFl4UmlmcmgyOXNDY2Jz\nTVZNU08yU3VEaUVrMTdpV2JDNnIyb2dad1dTai9XQy9UY0NQNE5paVFRMVN3Z1NMS3lBdFNKNnFt\nLzZRS2psVVMrcGJCQWlhYlhsRE1XS0REd0Z5VVZzN3F5bjJsYTZmYXlRSTVCSFVMU1lkSUJzYjVk\ndHl3WkkwUFRRSlJGd0kwMGJYU2pCWUZRN3Myd2R1TzRnMzBLQmM2aG9CS1lTa3pEVyttRHVPL2cr\nb3ZGU00xRG50V2hEeFNET2lpZVJOVGRxbjFQSnprOU85bmc3MGZTS1JlTTJXQjNnTU1xdnJLMFht\nZ1FlR0V6d0dDZjlERnRqQmVHUGNGQmhOR25FYmdra0VleldQZ29xZGNLTGVERlRnRDJiTnJVTmpG\nR29TSzVzSXhaYUx1VlNZc0FBYUwyMjlKU2twSTJQalE4TEZFTGprcGE5S0FnRmhvd1BtbDdVS3RF\nVk1POXhKMTFDVjFhTTR0Vy84M1RmRDlUVnpKcEFaVENrNTFCY2hhalBUeG13bVRWUHBySmhLSk1E\nUkJuc3FTU2NuU1Z0QURtTTRuR3FSNGMyb05TYkVkeE9wTHIxTFJWekx5S2RtYkV5WmkvS1JWdUZQ\nL2ZDKzd1UVhESW5ZSkoxS1hUSVVCV292UkR5Sy9VeVk0TjI3eThNRk1RbWJhMlJCd0tMSytxMFFN\nTjdYdmhTTW1jWUUxWXhSTy9id1VnS0Y2ckJoVi9MbkYyWmUrR00vT2VPNkRzWVdENy93WjM5V0p3\nYUM4djVZUHpDL0szV0k2L1NkdWlYYkRpSGNkVkxxclgvMjVmbnMzUGg0VkdtWHhUQ3N6alpTY29a\nQnpzMWxDY0taZUZiRkJENWMwNENST0NYVHhuYUswTmkvcEpXczNYMzNyZndGci96dnR1OVhZMjdo\nK2psQ0dHTkRYMFlRdFJ6WGxaZnMzUXZDUWlIR1pyTkUyMHdGbjQrSXdyTTROb0dOTERKSzF3bHhl\nMUNOQ1JCQ1FnbUxMVTJNYTBJSWN2aFgvdGUrYzZkT1ZLSHE0UlNxNVYwdm9TUGcvTUhJOWlZekEx\nY1lXQUp2dSszZkxEd3VMM1l6RG00OVlKYno0TUo2S3NMUVk0aGJEckdRalpyaFBwaWFuSVRpZ0V4\nY2VZb1VjMnpYREE3R2NUMnc3WG1WMVljWG4rY2tFaGNEK1QrWEdBNnQrRXRnQURIWHRld0Z4R0sr\nRVBFS2cxdVNxekdqWFFKanUrdzFtT05YR1FLbEZqaTJDMGZsRGQxWmw2cEppRkxFM0hWYWVaNm4v\nVW9wU0tUU01aMDhVdWw0b1lCSXRlSHVVNmZQTHVqSmlWaXAwUWdGOEYzdXg3d2dGYi9zT2s1YVhy\nanJXZFNZVWxwaHozVklxOUpydGxxTXptSnNNcVpBOENURytMeGx1VS9yTEdTRFpLVFF6bExQU1lU\nd1l4YWpmdEd2cE5kV2wzNEtVMUpoMktGVGhlVTdtVDFiamRTYW1XbVJQVGhhTFcwc0Z5cVBUTzFn\nRjMxS0NJZ0JiVGJPWW81amRNZTZNajhNQ0NMempaSUpyYUV5RFZLQmVvTzUyU2xNU2RKNENUQ1JM\nSm5NbUprbmhmRE5yRVhFbjVqWmNaWHRKU2ljREJyNi9yY1ErcU8vN05rUnJnS3NZK3RrTTQ5RXc1\nYlVwY01vaEM1S1pjY3VpNEoyUFJIU0ZMY1E4alk0ampkdldmRUpXbkE0YUNxVjByNE93aVNLWnlr\na2JUZjJaMXdueXhHb29HU1VhS1ExVktHTmtzdjRQQUk0VklQTHN1TmxZZFFwMkVPdTB4NDRoQlVH\nWTd5TU1ibjBMVzg1a3Y3d2g0OXVJSTBYRk1MTmszQWJjTDJNU2xocHFuZ0VlVFpnTlFXT2sweGZl\nTW5sTi9Bb0NDRjdmWFY1N3A4cnptcVorTVB0SUF6T0phREFjVzVmblVwblk0ZGtZMXlWUXEybndX\nNEZVSXd4d2ZOeG1iQXhjZ2FhU0xibjdOd2NieVRCQVJMenEvQ29BZzRxSG9YaGpsMFhQQTJUL1RP\nUUFsQXA5ZmZZQmxFWWVLNFhuMmFDU2N3OHBSVVEvblFKakZiSXI1YUxYWjJEaGdPNzFMQ3dtTE1Y\nTXY5TUNnVW04dnJycjFlcHFkMWg1TmZxWVdLV2FhUm5Za3FNd0lRSXN1Tmd5d0dvaWpFUjY4NUpt\nM3BPRUpYV3JDeFE5MldCaGhZN21SUnBkZHlaZkdLRU5nalNjdXlpQzBHSDI2ajQ1V1VtN1ZLbkR5\nWTdPU1daVHJMRmhSTitNcHRUUXZBd2tVb21MM242RmMrT2dnaFdJSlNiV016eFF2bUU0MjZqc2dk\nenhYbmtWeXNscjNNTEIyTmtXSlR0MlNUNGJPQTUxVWt1QjVJM1dvVHNOK3hqSE9qcWlDUys3OGY3\nUGNabEdNaFNxVkFGWlMyZEhYTlNtYXhqMlU1ZmhjeGl0S2JxR1hpbXlxL3Vzd0RtcWM1cktWQVMx\naGtUV2wvYkJXRjBmeVA0cTdYaXQ5eHlpNjQ4VnVTMHZxdzA2Q3pNS1VwQ21uWXM1L1BhZGRQeFNp\ncnJSWGVFeFRPTHFDUkRMRncrVjdHVmtsQ0ZaNnI5Mm40VWlIZ000eVl1dVc3R09NaHFoVW9oTEpX\nNlRvQUJ2U3JTa1NXWVh3TjJPcTIxcUZiS3BVUXlZOE40SnROWng3RmFncjdiQVl6Z2t4ekRTL2Rm\nTUVrSmE5Wjh1NDQ3VUI5Z2xuMXBrNDFXSTA2SytYVXpIU21oUmRoenkvbDhPUWo4UlZnSkFyOW1y\nSmgrTjdNOHorZXl6dUtnVlV3a0JQeXBqdFVsTUlQeWRiY0RTdG5Gb09EVk9mSEF3dEpIano0Z01H\nTm1CS2kxbVRFbkJEZTYxTzR3Vkc0NkZoaXRSQkhHeW1GV2ZGNkJST2xFTmhVUUZkcGdQSUd0MWlz\nUm5SSWFLYVNXS2JhTmFiMk9GaXFGOWFYbXlhd3hHT0pCcUtxbGdqV2RtL2N4QVVaT3JaZk9QSDYr\nVmlsQllOZThtb24zMjRBTExDckRGVzhOUkRJN3VaY3ltamFSZk1PU2JrV3FYdjdjQTVoWjl0T01R\nbTFVZlIwU0ZVWHhRRXFaTjlGTFFpcEk2M1BEbExtVW8xcklaZFJZMHN5c2tWSm9IdFY2TUUxdXI3\nTzlpSjFmOGVwZm1HYVdkYW5KdmpBcGhLb2U4enFxNE5BbzB3akttcm0wd0t3Si95OFVDZ3JYL1Ux\nQ2lEd01sdU1tR3J6Q3lhaUdhOGxzRWh3MWNQd2dvc1RGbmRsMG1oQ3RwRHhMR0RPbTlWNkVvdlds\nNWJaakR5RXNWaTJXNE5odGEwd3VCMUN4QU84R1FlMjBOSG1RVC94NUN4RGlwNEFJdzBra3I3YnNX\nQVdBY2F6NjVSQ3lCSG1QOGY2UlE2KyswTEtjaTRCK0RzWlVDQkV5WnRjOWtFS3N3OEhsQ1RjWllJ\nM1Btc1p0c2R5RmxUWHVzRVJqQmFwN2pNMFMzSU54ZTN1OFFxbFVSZ0dGNlFWeVIrb2tQVitCUThS\nbjkremZiMW5XVHBpZ2tNT2l0VzRxUkR3S1lvNjk1bllDNm10c3JkMTU1NTNxZlgvdytmcDFZaDA0\nM0JyZWJLREdlV2g1MWI5MDk2UUxZVGlqQnpzT1FuVnl4VGFxTmhHY3RwM1VDeHVGK2dqdDd6cGlP\nT0tCc0MxcTMzenp6Znkydi94R0NVUk5rdkM4VkRLZ3pIckt6bmNjRnUvNTVGK24xOVlSZXQrdi9k\nY3k1QlY3VHVJYTJMMWhQcGowajZBV0lNUVN5UlJSUis3OGdiMlBWZE9ON2VIUis3OXhuV1U1d0s1\ndWNvSzBWajdKWm5QbVNRWmh1QzZGaEQwZThwNDdsdG8rZ0hXa1JjYzIvZ0Nsb2xDeDJwUGRrZ1J5\nK000d2U0RGo4TVBwUEhrR3ZIZkJ4VSsvMW5FVFZxendZcE9JM3JoZU4rZzhHbjlyalVRWW1MN0R0\nbFd0bVNaaEVjbDFJUHlqOVMxTWE1bmFpMDVGcnBXRXZOVllEK0p4dUtTai9kUVAvVE1FYmVZRUlY\nU2lhN3NtekpMcHNSbmphWlpTRkRUUzlQUjlqMjBvcGNwUGxDb0hSTmQxWVZYUW00Vk5XNkJCN0J5\nRTRtMmU0Ny9WdkptK2VEeVJ5bHplU0wzUVdpc1lRMWhoVnRhTGZJY1RYS0dUcVQveWJOdThMamw0\nNVpzSWhRd0drK01FQVU2ZkdKNFhyWEhrKzJ0Q0NtNGpBbXJMdWUyWXVtM0FPRkFxcnE1cjc4SDJi\naFB3Z21SZWNrY2lrWDVWTXBrMFRKZWVtNXBoOFZIUkRmVE5oUVdoVW1JelpSRnc1TWdSR2tTVmRT\nbEVLRFVXTDM3eG9TelN4SWJWQWtwV2VwV3pibllMRTFHcm5ZZnkzQ09iaDBsMFBUOHZtZUVOL2or\nbDlUSjg4NjY3YnE4aHBkZi9JL2p1Yk5kOXFaTk0zQWlyUzAzNk5yUHR5Y2F6aGZpaFp1WklJQlJL\nQXM2Z1hhbFU1dVdOMTlqRTFPWHRTald1a0ZKNUF4KysvWGJtYnhSWHRWWVZSRkhFUS9VNExOdmJa\nZ1l3MW9zT1ZGRHVNc1diNVVCOVFIRDcvZ2ZFem1QWkhKdVoyMGx6azNNbWZvVzFXbWw5UnVBSzZI\nZS9lTitOTFNKQU1wRkc4L1B6OW1MaGtYVkkyNlRVcnVUMnp1MXZiRTFLYTJCYjZOOUFyVW5wZEhr\nRk11c2plN3huTFRqRUZpUVN2RlFwR29FUlhKeUhXUXovbGtvdGJWV1VPQWp4cWplZ2ZSanBkRHJk\nSmNEWnNYRTNsNXVjS1pVeXp2b2FLaU90U2czV0J5aUYxVFVHbkxja0RHcFl3NzRaMUl5eEE2ODJG\nd2pvTUZGWWdqN3FkTW16RjB1ckcwcXF0WFF1K3lNYTZTdWZnQ0pmVjN0MGJjbGZHSjZ4dUE0dVky\nYWtWbENMUWJrSkJEWk4vRXB3dnRibXRObzhPNkFMU29IVEd3N1BhRjZyOHpMbGZPMzQ4WW9VY3RH\nMjZjdXVlUFlMYjFKS0dUMkVFV0RQNnY5QWxjS2t6bk1YZWRtcC9xUkN0UkljNHRGSStUaUJNWjcv\ndmR2KytnVUlRODNXRTF5MWg0RTVsM0ZuMTZ5MGJaZFl0ak0yTlRXWitGNVJCdUE1YVNGVWl2d1NV\nTFhGTUFRTkl1YnBoUmRNdW83ZktCSEhkblJxekhYKzRMMi9XcEZTbk1YVWZnZXoyWnZpKzIzUHhx\nL3JNSlU3amg3dGNnYTFsbmYwUWdUTzJsN0V6c0ExcHBVSjhuSE84M0YrZW53clNuSFBlcDU2aW9W\nVVlQSFZ3VU5mckZjaTUvaXhZenppMFFtazFTMlRNenZmSEVXMUIrRnp3cGc1ZXRDd25GbmRwYWtO\nV1ZJSTVWMTNyS3ZLd1h3bU1WYWhqRHduWmZiTlVxWDRvTmJvYVpqUTl4T0VMMjFMQlgwQ1ZsSy9N\nbGlUWGFpMVk4OTJ4NlFVekJ5TlhKeWJUdDkzKzgxUTlOZGNZYUNVSzFoNzFGaEp3N1NCV3F3SUdv\nMndGSVU2WUYwcGJYd3JrODFkTURZK2VhbVhTQ0l2a1lMUkgrcDhZMEM4ekptZ1huZUpGOFl1M0Mr\nK2IvY0x6b2pzZTErb3ZBZWhFdEVHVkRVMDNoZWkvMG00V3Ntb1dxbHM2amlZQ0NkaHdjelh4Znph\nVjhMQVQxZkxSVjhVZlZNY2h6R3VsOWRDdGZtQW1TTFZFbXFwdFc3L1NHSk5lS1JrbkZSVzJ5Zzl3\nc09nTmpVOWQwVXluUmx6dkhoTXRScU9hYUVWdG1LRTJiYmptWHUwdjJBVkJrOTdabjZtdStKUm15\nT1NHV1htSEN1dGxOb3cvWXduZDgxMWZiOVg1bUFYdEFhMjlTTGhJaEk2akFPSTV4NS82RXVDUjlK\nVUJScUs4d3BjdUkwaUs2Z1Y2bjNhaDFZcWhQdDFVcWczWHBURTZRbmQ3VFRQenVnTUVRK0tTa29J\nL01WV2tJaDZIc1JwVWsyMURtdlZVclB0bHUxeWg4UU9pQWUrOWFWL1BYZjZzWk9MNTA3OTNlKzk4\nN1ZuelhjSWFlUUphMW56ZGIvTUVxM1VHVXBwVDRFQlR3bG5xYWpCVlBtQmQ3NzJMQlRmUVUwNldH\nYStvZVN2UU5yYXRwY2FUS2dTRVE5N2p4KzRlNUFhODhhNml1dkFhdytoRkltVlNhM1ZTaFJpNGdO\nSXg1VndHRHN3YncxUmNHaGlWZ1ZHS09ZUmowODFLMVRXdjBNSmVSdHdxMGpnS1RCNW05b01LR1Fw\nYnRrcGFFVGRIZCtKV3FYMFYxRlFPOFU3Nm9naDU0L1dyRVFVQlQxRC9OQmhRdUFjSkxQRWxDRHRF\nckx0VGR5TEE1bHpqM2FZUStkd0lHcWJmaG80Ulk2d09PLzNrZTkrNzdGTExyL21sdEN2bnFzbi9V\nRzVSanlnc0NWQk1YMHpwYk1kU292VEZOc3Y3ZmtaeHJqOHFCL2xyc2cwSGh5RWdqK0tNZjE3a3hx\ncTRuT25LQ0dQRUY2MTBKQ3hKQVlFa0tGYXE1UUs3NlRNcHAzNnBaMXdlVlN0UGl1YlNJS3UxK1li\nZ2ljSUN3QWk4YVNUU3BqVTFMaklMZzdPS2pqUGR3RHFkZFpJUldLZElXSUZpRlROZHZDWmo3MXY0\nVE1mZTkrdDZFbEF5dDRDODVaWHZlQWZFRUwvMU1NVVZhblUzUGh2L08vYjN0SElOV25yY0V5Tm1q\nWHBoeHVsQ3NLb2hqRk9Ram11MGxIdkxTbmVuLzNWeWtaVCtkWlNoQWpicHAvZis5NjlHOTk3Mjcx\nLzNQb1ZjL0NGdVJDYzN2MVB3cFZSZU1heVhYUDZMWGo5T2orLy9mYWIrZTk5OHE2bThCOTU0MDk4\nb2RkOWJ2dlRmeGs2aDFrclJtNisrU1V3T2Y1M0wxTWU1c010SC9uTXphbDB4bENyZFg1bzZ0Qkov\nY2crcmV1c0hHYW9lMDY0WHBBd0tCaXRFY0dsVDRqN2hETyt1b0Ixdi9STW1CYWdESXVPbDZwVVVN\nMW1OcHo3M0wya3hxZkNwdlplOVY4U3AwNHR3SFpYQld0R1N5VWtsL21lVFRETVU3TDY0QmNmYlRy\nV2lJVjloS0srbmxiV1NIVFdXbFpxb1VSOUlzQytDaGF3MW1rNEpLUHpzOFl1aHBVRXRvWW5mZkJu\nRC9RYVA3Tzl1Y0FJejNvZHJnRzErZ1RPdWpFQ294QnVyakJLb1ppQ1pJdVdOa3p3SUJRUXNSYzF5\ncnB6VTU4b2NBZnoxREE0Zk9RV0NJSk5rSDJaN3NPMzQ3eU5aTmJLcGU2NDQyZ0lacUZ4YlNzWllP\nbjNXV0hNbmx1NTc3N05RODJKaldwYXh5VzJ2VWxGRzZVVVN2bEJuU2l5Qi9KTEszblk4WktaMmI2\nOGZIQ2s5dUw4L0ZQS29Ma1YzRVRTNmw4NWdKRk5yUG9LbzB3c0xRYjR0WWFCMmI2cUFza0NvZFN1\nRXJ5WmovdGtVQ2Y1MjdiQUZFb1ZUU2pKcG13MzNWdnBKUzVKbWMvQU9RbUhxNE51VlZrb2wzcXVa\nakVaamxHK204dDM0SE9mNk40VDQ0WWJmaEVJaXVLOFZZd2xFN1crV1doTHg3OE1hUTYxaWRSMFYy\nbHE0enNnMEhNa04zeVN6MU9BdUdLMmQ4bUtHVUVhbjQwa05aektBZ0lEd2NTWWFtNHJHSU5lcWVM\ncTJSTWJCRHVrUW5wa3Z6L0JSaU9CeExZRkpwRXZBZk5US3UxbHhubzNHTmxJeDlXT1Vzb040MkxY\nYXYza0F1OXZ3ZUZZb1dzaWtEV0VPcmhmNnBpNVpwOW42b3hpaTB5R3ZQOFpRTWVPSFFPcmU5MXlF\nanNIL0xaZ2tmWFViZk5EZ3BCK0s0ekpwSXkzSks0S2tGRUFnV1lwZWQvakNGdGhKcWdTNi9mZGM2\neEdkSUFoS1BhVUNBeG8wandJdDAyT3M3eWNoNkpSejFMeGtjTGRPZ3dVYnNRMDUxTHlBa1NxcFpC\nTGQ5LzZscDY1T3ZXazZMWjJSTFZhRlhLQmUxMC9tOXVSZ1dLQnhxbXNDdm1DRHFqWVVFb3VFRUw2\nRmwxaHBRT3R4Vk95YWc4TE9HMlcwdmo4bzlCeHV3d0hoTFRaUW9OS3NRU3VDY2lnQzJyKythRUZS\ncXFsKys2N1R4QWVyQUduT2xnUFR6clpBdlpHcGJ1ejdZWnFGQ2FXdG5vZnh3Sm1JUndJWHI5eTNU\nQlQ4Z2hNNHI3V2pCTHRKbmVVejllQXlxT1RPZ3pnSnF4eFNtSTJBNEt4eUl4UEQvU1RLS2xQRTlU\nYkZ4TTNVVmR0YTJqdTRhY0VFUHFBVStwNmhubmpyUlltSEE2RHFBUVpCVUpFVWJGT1pya2xnTzVN\nUkpEN0F5ZTRuNnBoalp6RGh3OC9TYTFlUTlVZ1VFTU1QS2EzRjA2Z1J3MGZMclY2VUYvRWg0MGlt\nMUd6cEdLdDg2QXJSWkdBYW9haHpmc3paNzRaQURYOEtkUW9jdHVFUStnMGxJNmErMlBNa1pzVkE3\nTFFrT0Q4Tk1hb1ozakFOQm5Kc3NidDV5bitlOE9jWjQzeDVBMDN2Tmx5NEF5czF2YkVKU0laT0tk\nNmd4Y3FDaW9ucEN4dW5IMjhLOFcwMzBJUTFmekhVRjBhWVVQRDN0eHpudFNlVytjUFFWbzBNL0NH\neDRtNEtKeVF6WHFaem50VFpvNEFocG1VaDhCWVVLcytQT2lXV3NlTTE2MjZCeGlWR1h0M2wySk5D\nZHRKZ1ZJV2VGZUZpUEkvK0VkSkJqaXp1TS9QRVlJbldrcFRvVVM4K2JuaVlnTmh0ZVdCb2s4dGdJ\nWUQ1eTUvL2xVcERjZEs5WEJOUFBmbFArdFZ3aldnZWcyRWlCWUtaK3VjdllNQUxnckJvU3dIRGts\nSHhPU0NhQzFTcWVTVFhrS2hZZHpRVzJ3ZndNSkxVVytCQWJDNmxxOHhMdFRLWlZIeFM0OXNjY3R1\nQmdwTXdsVGE3WnI1akZxN0c3eStVcW5vL3Z2dkgzandaVkF1TG1GTXZQVGVxNHdqc0pPRk80cGtR\nYUx1MDkzK1BRRm1BQno1azB6YVl6VS82SForRXBwMEo2ZFNkeHc5R2lDc0tqeUtIZ1lhMlg3M2F3\nUW9ZWFVQZmI5YVdTODBWeGhRcjZ2TWxrK2FSZURKQUNoUE1TRkdhZXZrallYMFFHSTU1Z0ZvcEV0\nK3JmTG8wdG44eVNmd0kyVWJ4V2N4dDRJeUNtZFh4OVFObFBqMzNudXZIRlNsZko2RHQxVHJYZk83\nNHhJYnh0cU91YkVVWDZmSUhBMzQveEJZMlk2SHJZUXpJVkcrYTlKaVFqSmpxWEdqaUVzaDEwdWw0\nbGY2M1FsVzIwUXFBK3laS0pNZFE5VnE2VEVINlhOTmdWRkk1NmxGVFRiOGZ4UWd4N3ArRmxGSGlR\nY0dDWWVVM1pqTUo2cVZvOEEvYzhlSDM5WTNVdDBQV3RFMXk3TGErZ25iQ3JYWUJRMW5GaFR5RFZL\nbUc4WDRrSXZqSlJOR3dERUNQcHBOT0JLODNUajk1amUvdVl2ZDRkOExzQ1JhbG8wbzg2WUVXbXdU\nbURoMzEvZHRyY3gyTElWWUMydVZubHU2NFM4T0EzOTlaZUgwK3VyU21menE4dWxhcGZKUFI0L2VI\nQ2ZadzMrMGlCWXdZVmVoLzBEVXVlNG1EbDk1MkxBcHRLNHUrYldsOVpYRmM2YkJvZWFsaE9YMkRB\nbHNDU25PWTRwZTFQcVdaVjJZb1pqdU5ZVmRoSUpyd0tRc0tybUYxYWpSTXJGc29ESDdPcVIzdGli\nTVZ5cVArVzR1UjZ6cFM4SHFNOEhiZjNmVUU3VXRhczNlZjd5Z3I3ODZmaHR5YUNCUXU3eHc1aEZh\ncjV4VFNxNW1NK08xZmhacHRWSjg3RXYzZlA3anRtVXhqSm5PcE5MLzNQamNDRXpJL2ZPZWs3NnB2\ndUwwMUVFYTlLeWRhQkJEOThOV253TnNHMUlMelFxVDlWNytuQ1NVSDlxcG5HU01BTHNCbERlY2o4\nSmc0VTZ0NldOL2RQY0d3VVQwQ2xSdTlYc3lpaGJzdExzSCtGaU9IWXQxbk5sTGQrKzFiQWZZcEl6\nQWFLM2FLaDRnVDZqWHZaUlU1d2xqdTY0OGZOZ2ljTGg3aThDQVh2aWVUMzZoblBReUYvY1RHRk9N\najRZRDY1SFExZXY1Z0VlV3NKanJybkYrZC9OTXBVcjUzOUp1bk42aGtjbzdYckxOV3NSMlNsSm1L\nU2dMQm5yOHYvelVoLysrSGg2RDN6N1IvQjM0anlqTEJZdGFPMTk4NkhDWEJmSC9ESWJUbnlRbnA5\nSlorTGQ1ejVRZkVSamNNOGxVOXNRRGYvVFg2Y201TEdqMkhoQTViL2NucW1GaGlUQTZoMUp2YnRK\nMGVNbk1GWmJqdUxBbHhZbEYvZE0rV3lHVlBFVTEyWDFnZkcvVDZkY0tRdGtDODV3cjBmOWpNTHNl\nZ055TW9oblhSREk3OWhXc1k0WUxxR0JRU0hTYi9YVzZOY3QyWWZVQnh2Q1RuVlN1Um1EeUUwRUpP\nQzhPWEhUZ2hVM3Fydml6eGd1RkxVeVVyU2dVVmcweFliOTB6bXFsU0hyY3IvV0ZqeDgvUm9EYUhK\neDNpY3lFSmJoUC91b1Q3NTQvZGZKaDgyQUpvUUhSdXZ6MXozOTIzMisrK1NmSGxGVHVKYTk2VmRz\nTUNZS3FhVit0RnRONjlNTFgvWVdxYmJ0c2ZzOGxMNjYvbGN1TTVWNU1TSHhDcmhtek9obFNFTWIz\nQzJxVm52Y1RNanF0dExpQWhmd3l4bGp6cktrR3NGTG52RVRxZW1ETWFCbnI1bmgrK24yLzFYSzJ3\neUFJZE4rWHY5Q1lIUDNHRUpVMzF1dVUrRUFja2RDcnEwc1FTcG5tUERMalpIbnVjbVVqRDBJeXNi\nRzJTakRlUElTRFJ4SDlsODk4WXY3VXlRZGpYeGVjQTlJUkRXL2JrcUJJN0dQSHZoS2tjbU92UkFq\nZE56czdDd0xRSE1UbDVXV2ZpN0NMSVFxNGRHdVZ5cmlMMEc2bGxOMjVRNGk5VEpHOFNvK051YnNk\nSjl0VDRLSW9VbU5qWXk2VXg4TU16MlF6YUdQOXZEMS80VVZYVmtzYisrdTBGSkFaeUwzVTJMUG5w\nL1l0SXFUVDllQmVjeC9XVWtHa2V5ZVBncjR1K1h1UEhoWC8vZGhYSytsTTdoQkM2RXRYUHU5Ris3\nMUU4Z1d0UE5iMW93Y2h4QUgzMjhGNTFQTitJaFJuSGN2WmtVeG5yNmVRMHRiMThQVloxMDFjYzky\nUHZPTEtiMzdwcjM2UXljdzBUZTlpY1ZrNnM5TU5yK3dXYmdnZ0w4WHpyb3Y4YkxZN0JiUDVmSGhV\nZjlpVVROZjJRakwzN2t1ZitleXJsWkl4MzU5UVhFcytONzk3OTdNZ2F4UmhxQlZ2TkJYWnV5OCtl\nRldsbEsvemNQZjNRVFU3b2JWZTJMSG53dXMvOE1mMy9BNHpwVXFiQW9NSjQ3WnRYUTFwaHEyb1JT\nVysvMm1Ydi95OWYvNHZMN1p0ZDBZQkxVVUxsdWJteExNenFlZjg3dTMvOEh6UmVveFk2N0NDendz\ncGF0dk9KSVNpT1pVcWs1dEkzL2lxTi93OFl5elhlSmlZc2VwenJ2L1JWMTl6M1EwbHgwdnNSbEcx\nTFJvOFBqTi84Y2Z1L05MMTFMS3VFcnkvNzFCcGVYNXUxOTRmL2VDZi9OUC9raUxNMmE0MzJackJS\nb0d5RFdxK3NtTVhmL3pZbDUrUE1iMjYxLzFPbnppNS9NeHJya3BjOUxUTGY5eWs2WFdvT2xFdFdF\nbU9qVGsvOXRPLzhLWlh2T1pOcTQzamYxdW9YejFNaVljNllsNmRjTDJzODl3WHZlTHcxYzkvV2JI\ndEhpMkE1ME1wZlJvNE5BRUhEaURoN3J6aStmc1BYUGtpMjNHZ2Z6cUtvdXJVM083OWJ6bnk4YXVT\ncWV3RlNvdG1lbXNtTTVaNXhjKzg0YWN0bStXNktnWDZDWXdVNHN6MDNNNDlVb3JYOUxvUVNvTWJE\nV3ArdVhLT3AxTFAvZUhNK01RODFMR0lLR3FiTFVDei9zTFBmdld5OGVuWmErRkVra0dBejRYZ1F2\nZytzR282TS9ON1hod0dmdXc5QnVGbHFEUzNjOC96cUdXaGFxVVVNR20zNWM0a1VxbWRVN003ZnhZ\nT3pPeHNaOXZ2aE9HWm1aMTdkaWdwZjg0NEdxT3duWitHSUNNd2x1UHN5dVdtWGgzZnIzc1EvK0JE\nYnk5Ky9MTmZEY2NtSnEvd3E5MG45aXlXQ29XSlhUdHJjN3N1K05GZVJZR21qaDNLT1ZxUzJuc0J6\nbDBhbjVwOXhhQStBYUNOalhhQzB2MS8vdkxybDQyTlQrMkRuRi9PUXgxVi9DQTFPejgrTWJQRHRH\nZDlaZkdMamUrNlhzS1ozYlh2UmZGNER4YVlaaStWNEl0Z1d2YWlrNmhUbkhaOStlR0h5MW9ab2xG\nekpsQy9qcGpQQjc3TWdNWTNFSnpnNGtZaGpBZW9mbE90eWZMaTZsb1kxT0R3QUZDSUhJKzJINXNz\nZ2J4L1FEc2FFRklzMUlXd3E0ekc1QW1ITWJzbTkvMnQ3aWVGNU9mNnhXenZmK1JmeTFycGpmaUls\nRDc5Umx1REIxVU43ZHBxRER1ZkR6Y0hSTVVzVThaVFJMVU1vOUFFRzgxNFk5eFUvTXVsa3E5YXgz\nc1lnUW1GV0liWkJ0VnV2VjY5SlB5aGg4NUlLY1FxckE3OWlyU1VFc3RSMlArKzVnV3p2TjVoMjZL\na1dxbXNCZFdLS2FveUhkU1luSHJrL29JVVlvWHpDSlJnckNsdTA2bVU1Q3Y5MnRsMkhlZkxQQXcw\nWEd0V2w5WWpmWVZBa1I5WElvaUlMOEtNRzNRL0tlVEpmclZHOTk1eFI2aVVYSVB0ckZlZjRiZUhV\nWHA5RVc0RXRhcUFNUjQwaHAzcWd1UjhxYlYvbERJZFJ1SEp4clVZeDZVNzVqZXFwUlcvWmJ5SEVo\nZ1pSc3ZRdWUyVXg1NDRjVGRYVWowNnFBNUtTdkhnZHU2cHBTQWlDRTVLS2Z3R2NSQWhCSWNySitE\nbzAwWDRMY014cStMOGpnYVVsZytvSWNKWWl2dkxRbkRWV2VWWVAvRk55U2hPKytRaS9HNkRWcVJ2\nMzBSNEtuN29mZFF6clpZN3VZbTJpM0poN1pTUUhFcFVoN3BlMWZVY2d2R2pyYWZ1QU9jTm9mZ1JH\nS042WmlGTXVEaERVS2tUVW9yYU1LVzh6U3VpYW1WZFNRa2xITnZwRDBobFRBM1NCMUtwMDl1cG9O\nUVdKV2lqdUtLVWJMSWRhS1VJbklXa3RGcUNFa1J6dUpiZGZyNjBpSUt6VW5DZzFoeDQvNDJ3dWc1\nVXFKMzloRCtWVm1GUUs4Y0hjbkYreWdqV2dIdnhnSjgySzFDZmk2UVNRNlZBRHNMSjVRZlhsVlNG\nN2RabFM2WGFISWFHQmtXamN3TEdLRWIyd0tGREpxVmpKYit5SWx2R2V4Q2FyU2lFdFlMV2V0dVVG\nRXJwZ2RRZ1NnVExzZVk5M0gzaHlOMzN2LytYYTByclFvTW91dm1aa0N2R1NRUlo4TXh1NDhpdFZU\nand2b2l0Mm45MmVhbW90UzUyQ3d4SWpLcVdOdUk4R2hYS3ZCUXhoM0EvQkdGd05vckMrT3lDSHVC\neVNOcVVBVGoyb1E4R1dxdjF6ckhvaDhaVm5QUGx0b21xS1FueTVieXNIM0NKRVU0L2EvYUFzVFFo\nOWRLTTkzWUVocTZWb0Vnc0xxUGNCaVFTaTRPb1FVSS9XaFZTeUdGdkMyV040STdYV3E5MXRrV2p6\nUWZRU0dwdXdBOEtVSGNOTlVzRDc4OGZDNnBheXE3Qmlhc2xVVEd3WXpOM1BWamFRRXBWQnQydlVD\nc3NEZUo5VVVJdVBoRWV2M1pnS0c5ZDNmWnpFZEVTNkdRTndMYnUxOHI1UnVnREU1cWMyelZsZkRT\nUWVvbVU2aHJ2Z1FMem9RKzkzVmRLbXZUSDdZRHpDSFNDdm50OTFhK3RLVGd5Wk1nT2I1WU15dFhP\ndGdpeEtUQVV4MG5ORGZqbno1ZFVqNVdqRTVBRElsWDN2ZXVuMU9adlAzcXpDVDQrL09oM0swcnJq\nVUhqc1hqbWUzbXQ1RHJFWHdCUUx0WDZ1Ulo4Y1NzbGZCaG9JWmUybTBHcmxUSUdRbU04T0ZMa08x\nLzZia2xKVlRKdWQwSzhaR0s2a2N1dGxaWXJ3eno3dGl1a2xFdmJsZVFvREZlbGxMd2Z3VlIxZmFN\nQU5iemIzK3Bna0RyZjA0c054NUt1RitnM01ENk9hdkRBaCttMFVtcXg1d3FqSk9nYzVxSGZWU2lF\nU3NNRUd0RHUxVlZmd1ppWktnWW80bTlmYXNNd2dNbGthc0dmREtRVWk5c1ZtTnBHTmErMDhoc1RH\nVmFZdSsrK05kSks1MDNJakdBN25VNDFZNGRLNktIeWU5c0ZSc2x6MnlYZUsrZkxCU2xsbHhMWndO\nS0pVeFdsMWNaMjc5dUxOaTNnNFVwRGFjUElKRFUzY2ZUb1VhSDFjRXUzbE1Ja0E3WEJWRXVDWDZX\nT1k4ZWsxbXA1VUx1UEhUc0dicWF6VFhLQU1HcnpldmxybGRWaHRzbXRJTFJlR01aSDBvcml4dHBH\nbTA0YXUyakJwN01XRXo5U1NnbWM3eDFEU2ZFRUJDWXltZUhid3ZMS2Q0cElxNzVid1lFREdUakRZ\nRzI3VzUwU3dqZ1MyOXJuVjlkZ05ZTi9hMnlLNTl0dXFxUmNIdWJoQ0NGNldtNDhrbTM5aDlLS3Jl\nNG5oVGhWcDRCRjVVcWh6Umx5YXVVeHNEeTNiZUYwUW5HK3RGMUdzTkxDdDh0YXl1YVdTdXM1eWxy\nSkpReDB6cFNDVXQ2ME5LV3FqL2NXdjlIV2t5Z0lUbTJYOU9haHI5NEsvQ0w1Zm9OaWNvYmxjUHRq\nS3pRWHk2MUtHNkJjTFJiQWtvRi9VMHpTMTczbU5mWjJMTFlHZUxWNnBzVzhqTDhyQkFxRG9DMlVy\nNGV3Y25qRVQ5VVBKQVhmWmR1SkpYOTY2OUVxS0w1UGx0dE9pWEJaaXZpRXQyRnh4eDEzd0VUdDBr\na1Zpc2ZJbkU5QU5yZjFYdVBkQzIxM3E1WFdUL0VvM05hZWU5OTlTSUFXUDhoQkJmckl0blVqbjY4\nYVAwakw5MDZkUGxzQ2t4aitqUWxKUDJmdW1yWjRrcEppcUVxK2NtWDlqT0FSYjl6YnBDWHlVRlVy\nRzIwQ0kxUnM1UXhxdW9qNGFhQ014d2pMaEpmdHBKdVZuSWVudGp0Wk9sR3BWZGFsTWpRbjIvbWFs\na3F0ZEQ0WHhkVlNmSlkyZ2FTcnBzQ0VQT29hNzE1bzYwbStzbnBlQ0Y3WTVvelFTb0NEcXY5M3RK\nVGI5a2VFWWJTdXBRcGFPM0RzZ1MvQ1NTUXgrd0RGaWRTZXliWmNXck9zYmhGdEJWUUtLNHVDOC9V\nR2F5YXNqa0x3RGQrdnREbTdJck1WREw1ZmpWZlBpeWdTTUVkbDFNSjRWWWNJbzRIbE1NT2d0TEsr\nQVZSdzJ6WWNaTGZqa1BOb3FURkd3RmpSZkw5V3ljTjRiMnRMK3NFWGF5dUM4N09Od3gyMnA4WDNo\nd2lqZ2I2YVhpanJ3b2JTcU4zSEFkNWVZeEpEVVFyMkxDdmRWdUxMRlRjbS9sWURPMjVINjV6elU0\nMStRdWt0OVB0ZnozeW5qYzBnVXY1S2ZEUlAvL3RWbG9vclVnazQ4Q0pZT24rK2k5QTZDQ28vZ0cz\nK3lTaStqMy8vbnJJQ0VvTHQ2b0U5dGxTTXdxVjZMS25OK1hrbUtCUzd4cnNIMmxwdzc3MUhSUlRV\ndmdmNVFOdUJWTENDREFyclJrdEtiVTgzV2k4dlZNQ1IyQ254U3Nhc2w1aGdTK3VPQUtRZmdWSU16\nb2VCOXdhOUt2QXIzMjJjQWdKbEZhSHYzMy9mN2JlM0thM0tEMEZwYlZ2bE9vSDl5b2FXcXFDVXFp\nNVhIdXNTbUxXMTVlTmg2RmZKTms0YzZjUmRkOTBWYXFVR20vZzlvS1RvY2h4RzhSakYvU1NiVzVL\nSzh1VmhITGRkSWx2YXlIOWpxOXlWVGtqTkYrTURyL3A4anZoeXF4TnBHRURCbFhHSmQ4d3FyWnRL\nR3lGMTNyWUdxbjY1b0pXcURuVk9RbUg5NnhDNU5SejZQRUtWNHNZM09xK0pTclVDUW5xVHByUUh3\nT0VKSzZ5U1l1M1RIL2hBMTViMC8zM2k5MDZHZnUzMGt6U3R3Y1d6c20xdnIrSm0rMmtsK0kxRUFN\nN0d1SjBZNTFySFd5bTVwUityNjlOQ1llWEw2NnZMWjlMWkhFcW1NdTJ2ZEJZODFWMmtQMEx3RmR0\neG9QZ0puSjFkKzFsWThkZEJUMGhseHJydjJmSnlFMG1HVzc0dmxTeEJPMXBwT3FTV0t4NFVXSTFO\nZ0tuVVZwUzI4VmlsQ0NaWk9wT0RFUnJJejFJcTVMKzJ2cnAwSXB1YlFCdjUxZlA1cGNVdmRWNnpF\nSjBwUzZWNE9qc0dlWUZ1djN0VmlodVBWQ3NsWU9Qc1dtWVhGeGY5dGFYemQ0RUoxZFgvTktUMDRE\nR2kxWlo3alpJaW44eGtCNDRmUEIrTVViUGtPZVI4bGRtMmViL0IzRms3dDFCVXdKZWZNZGZ1Z1VO\nQUI0MTNKN3JXeVk4Y2ZldngzL2pBbjN3cE56VjlRNmVaWlZZZUhWTmV0U0tLd3VYU1JtSE5xQllF\nem1ydkdMU1N2ekVueENPVlNtbEM5MUVpWTErR2tCTFQ1dkttcFh5b1dpNWVqUkZ1N3NWQ2lGUGxZ\nc0VvckhEUWV1czlQdjd4Ti9rZmY5RlhqMWNycFlOYTY1NE1tODErL3U1YkgvMzE5MzdxaTdNNzkr\nUUs2OHRmK2NpNzM5ckZEUWV6N3RuSGZnVHVCem5IaFg3M0toYlcvczJ5WXY2OEh0QVBmdnZyZnpz\nMXQvTlZXbW12TmFNTkd4MUs1eVVlZkNvYVFDbjFTTFZVV28raS9xZXZ4Yzlua3hSUiszSzFVdHBZ\nQnRwVnpKVDU0dnZlOTJ2K0ovN2lhdzlVeTZVRFlIWjduZ2VOTUwrdnRZYnh2a3JyemZIdVJLK05W\nYWtvK0JCQjZET2RGb2RTR2dtcHUycWFFN1o3V212MGMyQjBxTkRxY3Y0VjBFSkp5MmU4U1N2bG9E\nNENvNEhwRVJQbE05M2tMTUVTL2FGQzZwOEkzblJiVXlLL2hwSCtPVGpJQ3luKy9ZN2JTS1RVYnlH\nTnNrcFRVencrQ0R6aUgwTktmazVLdzhUVXMyRlM0cU5hb1J4aHFPLzlsRVJmaUdqOVJMZ2VXTXl2\nMzYrVWVwM1NpclgyWDhlOHdCRktiVjBVTDRqOHJGTDYvbjdqWjlxaE5KSjBNNjJoeUdzTFUxcitU\neWpnNFRYeWVLTkxtdURmMUVwbU1jR1ZhNjY1aHQ5OTk5M21BMEwwSHlpazdpR0lQT20wakJGR0dH\nR0VFVVlZWVlRUlJoaGhoQkZHR0dHRUVVWVlZWVFSUmhoaGhCRkdHR0dFRVVZWVlZUVJSaGhoaEJG\nR0dHR0VFVVlZWVlRUlJoaGhoQkZHR0dHRUVVWVlZWVFSUmhoaGhCRkdHR0dFRVVZWVlZUVJSaGho\naEJGR0dHR0VFVVlZWVFUMFZPTC9COUVRSWxTNkJsRm1BQUFBQUVsRlRrU3VRbUND\n'),('e001','성진하','sung','성성성','@','1323','내맘속','깊은곳','01041234123',NULL,'2025-03-07',NULL,'재직','정규직','인사부','사원','asd',5000000,10000,10000,'123123',NULL,_binary 'aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUl3QUFBQzBDQVlBQUFCRzZjVCtBQUJEUWtsRVFWUjRu\nTzI5Q1poa1YzVW0rSjl6MzRzbE0ydFhMYXBWRWdVU0pmWVNVcFVRcm5ZREJyZVJsLzRzMmJTbk1Y\nUjdMR3hMNEdYY3l6ZTRpK3FlenpNTVE3ZEZTY0pnZXNEdXB1Mld2SU14RERhMkd0QUc1VGFTVllB\na0pOV21LdFdlbFZ0RXZIZnZtZS9jK3lMaVJXUkVaa1JXWkZZV3l2TXBWSkV2NHI1NzQ3M3p6ajNM\nZjg2aExUZmYvVElBRUdkbzB0bVRxd3NvVmxLelFvOFJ5K1NSaCs1NkFmM1FaMjlaaFkxbURELzRZ\nTnJ0SzV0M2ZiUU1GSjh3VWVsbDFsWis5K2pEZDc2bnJ6bVc2SkpSQk1kZjBUZkVNUTJKL0t1cXhl\ndUpvM2NCSWlMdUVRQS8xZE9aZnU5dHd5aE0vUVlFUDRSVGsvOEV3SW41WHZ3U0xUeEZ4TkZXZlVN\nY0liVzE1UURXR1k2MkFBSnJxMGQ2T3N1bjk1UlFtUG8wU3RGdG1FeW5BR1BtZStGTGRHa29Fckho\nblZnUXdSRmd3ekVCQVYyM2xSWXFwLzhXaGVnMlZQMjVhdk82NGlXNnBCUmQ5QmsrZTh0T0FMK094\nQTFrUVV1MHVJa0hjSTUvaDVqTGNES0FVeTNSOXpmRC9KYzM3VUpFUDd3a1hWNDZkSEVNWS9DTGlD\nakdrbkI1eWREY0dlYitOMjBGMFk4aVhaSXVMeVdhTzhPazlPTW84Z29zOGN0TGl1YkdNSHQxbk55\nK3hDd3ZQWm9idzF4L3kzVWd2SEZwTzNycDBkd1l4dUlkS0pyQ2tyTDcwcVArSFhmcUFQNEQrWkg1\nMm82MjNYVHZLeDI1M3laVGhDUzEvM2prc1R2L2JINW1XcUlaYWEvd2xpL2QreW1PaWkrVGRPcC9I\nbjdrL2I4OE40YjVyemR1Z3NGTzJMbHp6TkZIZnEyeVpmZCtMNStvRVpzSWxBcXRNRkhoQjRoak9K\nUGVuLzlzMjU1UGw2UTJmcXNGbFVBNVQ2RURHNkt6aHg4Ky9RVmczN1NGcmQ5OTM3b0k3dTB0WTNM\nRXpyQWplL1RZdysvM2dkZzZiWHpqL2pVVXl3OTMreDNzREtmaWpoOS85SzR2dDZ6enRmOXBwUzNI\nUHlKTUdtbHBHME1HUXQ4Nzh1aWRYMnMvMzdVM2YyclpoRlRlS1VTbWZad25pWWdwdWJCcjA1V2Zm\nK0NCMnh0ZjJIclRmVHNGN3RYT3VBNmhIQU5qcW45OStLdS9lcngrWlBzN3ZsQ3NqVDU3cXdYSzdk\nZEUxMWR6eGYveDRqNDhqMTNZVFZ5NHprbTFFUnZzbjJGTVlSY0t0QUpKdi91UjBOYmQ5KzBXaXhF\nQ1lpZHVXTVJCaURadjNYWGZXeDFjNUdKNjB0U1FpRXVVbGFZeGs2bE5MVStBKzVob0RZU2FIMmdR\nREZUZHZHdk5ucU9QNExIMm1RdVVYZ3Z3NzdhTXlSRVpBM2J1aXdCYUdJWWp2b2JFL1o2dVJVVnJP\nNUZoUk03OUxZQVdockhsYUF1UmZKcEVyMi9ybk1vTGp1eXhWK3o1eE91ZmV2Q08wL25QeG0yeWdS\nbi9tVVJLN2VQQ1dNVVEwTk9Qblp6NGtsY01NaElqN3lLS2Y0MWRiZG9pTmFqc0V2a1lnRjl1ekRQ\nKzlQSlkrRDVtdnFMOW1wQ0pVZVRrM1FBOUI5eFQ5ZmVDcERaM0hZYndGci95UG1ubnprOUdEdTZU\nWk9pTHd2TG5SSFNsdUpwZWxyY0ozQmVaNDcrTXJQdHh4N1hxTEF0Z2dLbjFSY1NtVUNLaHQzVWYx\nejZtN1NWNjNqbU1RNWR4L256VHZ5LzZBY1diSnlyVk4zWWMxbVhjVFBPSk9CM1RaYTFDSUx4dCsv\nYTdpN05meC9xMTZQSms5YzB3bjlnWkEzTHpuT05HUWdiRXBQYzN2M0wvMkJGRHBLZjFTSGphMjE0\naStsdGZQK093bVY2a0o1akRPSFJWL2FYN1hBeU82SFZkaGtuLzgxSFhNZUtzUHBUYnh0Y09iK2g5\nbnU3VUg4T1V5bGREOElvNUs3eitwblJhVkRpbW05QWN6NnlRUVQzRk5kaTdkeEFCMVhrbmNYVHRB\nczJrdDNrNHBwckhQVjBzOVhkeEMzSURpcWEwR0NQVEFxZVhadjIydjEycElMQkZUazZmK29IY3dG\nNkkySUNjdXdRTUE3cTVneTYyT0VnRVJMSUNGYXpFWWljUjNTelc3ZHo1aVhoaEpsU2p3RzFhV0lZ\nSjRZQWJPbGw3aTRhRXlvbUpGejNEU0VBenJqeTNDa01MTmlsaC9jSXl6R3ZlckJOZXV4aTNvMENx\nOURMSG9GVzRERWhBdzhta0dWNjRHZW1LaFdXWUtsNEo1cFdMbDJHOGNhMmF6T0xYWWNRcithVTRT\naGFJWWJ5dDRWT0hGbzVoeUwwQjhXSlZZT3JrSFhqTGNCa1FDZUpxSlZtNExRa1lHY1JKZXZmMENu\nWXUvbUFqcWNkMklCZG1ma204NlJMRlZGNm8rUWcwdEhBUzVtLzJxSXY3VlpjRi9vVVg2aVpjSkhs\ndnVTMWhJU2o0KzBwQjExNEloams2dFFHRXJZdFpmMm1Rb00wRnZqaUpkUHNVTGl6TWJQNit4ZmhI\nZTgzQ01Fd1Vid2ZUOHA0WWhoREJhRDdjcFNFUldhQ2JjTEdrZm0yM1lHc1ZVTFRqMVBVWDdRWHY5\nUVN2bWxYaDlYRXIvKzV4V0o3RUpTTHkwSURMZ0VqZFJndTNWaUl4dGEzSGFXR1VYcUpYei9pNUQ2\nTEtPQkw4S3FybUFiejNhK2N4VHlRS0Nwa1dzTTJDai81dDkwaHJVM2RvKzRvR1BqSDk1b2tUNWtn\ndjBYUjRnN2p1SGt3UlM2UUQvVHFsazBrOTR4THJhMnIvbmNwZmtxYlRwUktCL1Z5ZEF1Y2FZOHUr\nbEV3dDczQnRmTEMvWlY2UjduQ0VhRmFYWkpoMEJ6U0NQdE0zRS9jcitKbUhQalh6K1lnNjNyQnM0\nUnI2bjJsNFZEQ3VWck5IeGJtSitvVWdEV2dLbG9PNGJrN1BjQTVTSmpoUDVDWmFMNHBUUk0ycDlt\nK2JnanZwVXZzWkR4Rm9DWXdLRWVSV0lGN2RjWjJReElrY0VYRW16eHc2U0VUV0VMRlhka1U2Yjkz\nZW4rVFN2M2V3ZjBmRXVRdnZtRUhIRDQzWDJybjF2RGgzWEZ5cnprQ1FDRVJyNi9MTVZzKzJQeW1x\nZUU5Q2NLNTVQUndScFpOemxUQ0N2MWs3Z2hOMEZXeVhwNkxBUU1YKzBhek1FaTVZVldBVERicFBu\neW5WVFMrZDZkbDc2aCs5Y0hickg2OS9zeHVlYXZ6d0lWcVJUTXJVenhCRkg1OWxkaCtFRTJjL09F\nU0YzNXVRMFVZY1Ixd1J3enlrcUswV092elY5ejhINEwyZHpyWjU5ejBIbUhoMXAvWGV1SFhUVXc4\nZk9USU52bEMwVVZveDVzUEUwZnRtbERJY2FYR0VQejcyOEozL0FUMlFyY1lmTVRIdFYrOXFuY3dV\nTzRtTHExMXN2MDdFR3pxQ0loUmNaZFA3aDZuOC92cjEwR3V4N01MWmNhQnoxSDlHaGlITEZwTlhi\nUVN3dGlIeVczNFlnTVJOZ1BDaDJYN1VnUU4zcEZ0dTN2OVAySm9DOFhUdWMybkM1V2pvOUlSVXIr\ndDZNZmZ0YzRlQmMrMkh0OTE0OTk4N1NrR3pHaDJxYU5yeDd6NzhjMk80S05ycjVYYTNUelA0NU5s\nT24yM1pkZSszdWlINFdxZzNiSkNuNHdmdVVJblFTU3FjMzdMcm5pTlFodWxpcVFGUytlNURIYTdI\nYmZjYkhEblpwNFRSdTFEbGx5SGlZc2RuUC9iUzVYNzhzNjgvaWRsSmVxbG10WG5YeHduVVg0UlRV\nTGdna3FiVWkwNDJ3LzY4TU1SbmU5SmhCa1FDbkErTTBZMzZ1eDR6YzdHUUlESFh3WFRXbFpDSUFq\nNC9nVXRNam0yTmlLWnRLWXVTSkswc0pNTUFyanJJSjJSbWhnbjY2WFVkZjU5aExUMzBEYnpyYTkr\nWXk4UnI5OXd6c25uWC9wbXRyeDRwYkhHWGdWTVIzZ2haWUg5NW4rSjZ6Z3lqdHlDeVJUaHM3NnEv\nQUgvZzQzMTErdDIzck1FZjNQSmVmSHJQckppVVl0WDlHK2I0UWMxRG12UHFsMmpCYVVZSjQ0cSs1\ndDMwa0lCS25xcWJCTGt2Tkk3OS9wdTNvRkQ5RWtRK2ptaHF4Z0RndHRkK2VpVVJ2WWRNWVpWanVR\nd3JhTzV6YXMvUDd4emRRT21YbHJvcmlVNWdoNnJyQUV5djBCQXhVSE9QNGFjZmVoYnYwdElmdHhX\nUXZ2QTdHSXAyWXRLT29zZ3ovbGczUEhrakVHM1NOQk1CL1JCMmZ1S0RPSERINHROQmJydmZyRG4y\nM0xRb3I2dUtXa256NjZVVktxMS96VWVHMDVHbUEwelNFaFZ0S2Myc29zWEdNSUFkbmxSekxKcW1I\nbmpkeG4zQis5cVU3UEgzb0dqZWptcVAyN056YjlhRUtVMlNJc2kxbStOazIxSGdHU3d5Mm5yOHpM\nVWl3NStlOWtIc2MzMWUzcFpuTnpEeTE0WGwzZkZRNlFjTHVYd3BpZzFaVTNzY3dNOWgwVEdNQU9t\nS3FRS012bW43TEhHcHV2VDgreis5ZVJrbTVkZjdVZVdFOEliQWE2TE9vN0wzSkM5Q2huRXBSdGhF\nTjNZUERjajg3VVprTmpIenBuWkhHOXZlQ3B2T0Y4Mmc5QkxTbGVPdEhuRWxOYkVGenlGeXdmZFNr\nWjlFd1d6dnRmU0hWZ0VuNEJWTlo2K1B0M1MwbGdTNHROc1VPUkY5TmpxOE1OOVdtYVlSZDVyN1Vs\nd1R6ZUdaVmNLd0lGMHhIc0lvZVlwOEpkK0hjZnNqVTdqL05vUGtoWjlEMVB2RlM2bTRMaGJaMEZ5\nRG1tTjJ4N1ExcXJnWDkyT2JkOTI3Q1hCUEhIM2tyai9wZVpJbEdoaHAvanNJMTJ6ZWZjOEhaMkFZ\nZ3JDRFhhWU0wMzRHN3dIK3FuL3ZUcndXRWIyeHgvTFBuZ3FnVGNJMDBqeXZNZ3hkTlgybFRwUGti\nMlV1M0dwdDViOERXR0tZUzBHZVlmaHFKdlp4clM2SjVJQXJwTEREVTYwU1J0L1dWQ09UVUNIQnVY\nK0ttT04rTEVBSDJVYWtmTnFBSStnVUc5VWk2TFJZbFRUVGFtWXMwUUtUK1B1Z3I0NE1RMEp3cFJw\nY3VkcktNSXA3QVk0Z1NwLzJpZmxFUDlJMWl0MkZOREU4ajBEUXJZbEFxNlBTaXNzaW4raWxUbDBs\nakIydVFPSzBnOElyajN2OVpkV3cxcm03dnY5bm56Wk54ejdKc0VTMWdTUmFMZEg4VXJmYUpyQWpr\nNEN4MDdjazVtdzdrcmVnME45MkZNN3ROcllxUmdMbXlKalVxcE53aVJZNWRUR3JDWGJaaE5hdmFq\nMnNFQWVtYi9yM0ltK2RpMlVwd0xwcG1yUkc1Q2hhWXBqTGdMcjZZZExsYmQ1bmxTNnBHd2RxQjcy\nelRtUm52L29MdEZvQllkVjBSbE5RcWx0aW1NdVdZVWpDbHBUZmpyeitRb2Z3NUNQSE1VR3ZCZFA2\nZnZPVXJpMmFFZ21XNS94QURSS0NZaytYNkxKakdFY1E0Nll6ak04TXdFSHM4M2Y3RmhTMEZscC9r\nMVdTeWpDSU9pYWdNMU5IUVBVU1hRWVNScTBqVzFZZkROb1VYbms4US9YdG1vdis0bUtyekZLZXJp\naUxDcXZNckY1OFFlc2xtbEhDTUZ3eGdTc2xyUkltN0NMZjhubldoRmYzcmIvb0tXdzBqRzZaaVNJ\nREtVY3hHd25Qa3JlMFJEUFN0TkFBQ3lNcFZ5RnhqbUhxSHQ3SWZoc242Qm9Gdjg4bHo5cVFYU1pz\nVENjSlEvTmVwaVBNeVpwalBHZWlUbi9QRXdOMndsSDdZNWUwNkdQVUVRY3pWQUdNOC9wTWM2RnlF\nc2RYSHNINjhSOUZ4UEZjdXJBSnk3RGFRK0s5ZlZuR1hhaCtxZjhGb0JJcG5tTCtJc0hpNWxnblJi\nUkl1WStJTnUra1MzV3g4OUlVVlNBSzNxNjJwTE5ZeXlDTTR4SlNoK0NqT3UybWdnOUdFL2ZxRnBK\nMWgvQ0JMMWJ4KzIrNllhNDhMbzZIS2NBalZHdEp5T0VjaUwxZmhnaGFwb09DRG5QeHZVczdrdGZE\nc0tIdllUN2hxL3BodHZMZk5IeGFKMmVxYkp3TS9BWXF1TXdsdFU4NkovZEFOSHNtVUJ3TEZkaGRN\nclFkT3Q0WkRRdW9oWlRId1FRR2Vjci9uK2gxYzhXOU04dHdJd1BSMm04QzlIOEMwT1lUeWtXbEhU\ndjJ4bU1xWWVZTGx4VHlvZCsrWmRmK1oxdU9rOExFNVBsakQ3Ly9MenFQVklBZEh6bjgySjBIZTVs\nbjg2NlByaVlVYi9QcHFSWVBjR1J1RU9CYWcrU2JUaWlkL1huem1VUW5qMzNqcm5ETmU2UWRPL1lX\nUmxlcy9Ta2lXaWxpbjJ6dm5UQS9ES1A1cWo1SzNYWmM1S0RIdjlnWFhqN1hPakhXY3Rrb25nWXF1\nZEp2cEVuODE2YVFuQ2JRV2hFVXprUWpjWXRHN0F1RVI0QkxCbE9lMUVNcStUVWd0S1RWYWlsRnNU\nV3QzLzhYTTZSb1JiMVBWTkI0MlcvN2l0L0dmUjBpdnhERnd6L20wckY3bVBDblBaMkMvRVhxaXly\nbGpXV1M1UDh5cHJUUnBsUC90YjEzd3R3cFBPUktMY3l1ZnpoV3A5MVVxOUtsRW9YTVFlQ0ZUUkJz\nbkhOaElmYmJUbGlDMEhjOG1GbHdWUGNqSW9wTEZNVmtWUzBJaTRSTEQ0dE5Ecmk2ZEpzcjJUd292\nZHZhQjU0dUpQTjQ3aGtvQjB3YkNIazljOHk1NUlDKzJwNGFBeGVuY09WS3E0V2tHRjdDMDdCOEhX\nSXF6clVUbXlGWGFvQ2pXSTVrcHo4RzR0Y0xFTlZXRGtWeFZUdHlLRWRIaW9MNUQ0Y2ZldCtuTHZv\nbnMySXQ4MGM2b01JR256WWk5WXNZU3VMcjZlYzdOY1hYeDZrYkRRT1pLeFF3d0dOSEg3N3JyZnIz\nOU8yMFVJTjRIRXhqQlRyM2Vhd3VId1BrVmYwTHlpWTU0V0tvZVpHS2RSVEtheEJlOVArSVJQSDRS\nTnhlQ3dZRElPdThkWE54Rm5BZnlmR0RJRkp6Y3ZGUVl5MnRpN0pxVWxmaENqa2ZqTWRvMHdtOC9j\nc1RFTHo2WXZpV01xZWRRSktJM1dnNGh0QXppSWhUS2tia3plckJraUhOQWIrSXhMQlEwNmFFQlNY\ndG1iVDRxSlZobkVFeU1nbW5UcnZHTjN3dG5VUGhEN21vU3VERUhJVktBbFJKRWpPaHh5ekVNNDVB\nVEd4VXN4cDhhRUNiakVsdy9zeWR5QzB3SXBBWEpRS3hWZVJiaGxzK0JVUXFhbkk2RFBDOUFNbkVs\naGtsalBwWW5CUzdGVVVVNTJKZldRdFNLOFZUdnZxTlFjTVJSYzdVek13NWszTWpjYlVxa1ZINDRO\neTJPTlc1d05kZHVmTVRRMjcxaGR4dlc0OTQ3SlE3K3NpdnFaVXdPUElwT1BKeUxWakFoU2xwbmEv\na2pqNXkrMkRuNjRPbVhVQk5MZEdNZ1pibjBlRnBMQi9hQUxpMVhTV01wczhtN2hCRS9qM3MrUFJL\nTkg1bkMrVzNSQ2hKbzJFdlNod3d4ZHFKUklpY0t6RHpQRGhPaGFiQVZBTlJhUzQ3VSthL2VVY1VK\nNDlpckZrR21HaUNISXIvQU9DbkI3cGNwNEJyN0M3VzVCR3FsaHNMSmhvbm9kRkRPMjY3L3ljT1Bu\nRDd2SGlZKzJJWVl3MlMxV00rSjZsQnlpQ0dud1p3TlppTEhZT091bTA1ZVJHSi9CamUvZlZ2ZFoz\nTjEzenpFc1lXYW9tL0M0UTZod2lKRVliM29RM3M5NFV6QzArUlNBV0V2dm9Ra0RiUTFCbzVvY1pk\nbWRpOHF2WHpDR1FIbVlxb1FsY3ZrWHErcVVnVVhaL1gwMzFSUkp1T1RKeWN1R1FLOGJTSjA1Vmpi\nU2c3Mzhuek1DeGUwYkd3a0pJZVQyWGZqTXdTa0pqMVBjNk5salZZNVhXWFpyUExuQnU4SHhMbkYx\nYldUclFFbXVia3M5Vkt4WXVEUHEwa3N2cTBTQzdWSXAzK0dxRFNSWlRQQ093OEg0Z3VpV1RwempD\nclJsdE5hbzJWbU5xTGdHaVd3SFJTejIzTlBvRTQvVXl2a3c0NnVtaUt3MGN0NFdaeHlTMkpTZTly\nLy96Rnh4K3JRSEMrWDdQYVJvVTBTSmlGSVhiT0VnMjJBTkM4YmtrMnRveFNwWXg2OVhWdjBOQnBQ\nRm04Z0d2VDdSMGRscUZ4NlcvNzFKTmVkRG4yZ1VaZW5aUzhJNFp6L29id2hQWHZGRHowNEhzckFC\nN3UvbzBITExEbmRJaU85MzVlcnRsVUlySHFSc1FDVU9wTXl1eWM5bEZkckFXMVdpNkVpMnZLUUd0\nYUpJeklDWHpvUVF1aWJkTitoUDZ3eEo2R285N1NXSWt5YmlCT3F0YlA3ZkxPT1MwOXB2ZG5Ib2dZ\nUi91V01FVkpJUFUxeno5RjVhcnFRN3J2TE5TVXVvV2J1VEdNUHR2Rm1uYThXTjJ3SlBSVHdtRjg3\ncDFsQ0RaTXM1QjBPM0w0Sy96enJ6YTZyczlJZGZTM1NEeUZNYTlya0ZvdTZ2MGxPRTduOGVaWSts\nNi9RNXlsS2tHMGlNMkNVRnFKYXd1cG8zanJRanBqckh0Z0dGR0dHV3FwT09XakFuUUlFNk5yQUdr\neVVuTkdWZXA3VHBJWGpRbUV5cWVGcUZqMFhsOFNoVHlFajNVUHh6eVJrRHZZNzNablUxVEREVndZ\nanFsZW1OU1NYTlYrbGZNNWsrY1hXVHRuSGNhVkt5TUF0U0hTNkhtSWJFVEVoUmFUV3JlcnhKMkR5\nTmQ2bll4WXhhM0NNYVdvczRVMTB6Si9lWVJjelpBcmhwaDVQNytodDdrVDk3Z2pXMldLaXQ3YXlI\nNkRMOU5QUm1lYzVwTWFHa29xdGhwWEZxcXk3L3JYVEZiSGpnd3ZJRURLYWdtY1YyN2R2ZitkNGtJ\nWmNXMll3WEg4cmNNN25ud1JSOWJPc2lVTkpjc2hHR3BJRWc5cmNJZEFkTlUwazFxM0k1Ry93ejk3\ncUxmdEtLd21FN2RVWkppQTRSV3M4VWRJWEV5U2FHTUh6QU1kT1hEMk9STDNXVUNlRGNWbmZPSC84\nK0xzZDhTbFR4R1FoVCthRkpkWmE5U1BEL0tKRnllc2tYaDlDYmZxa0FjZjJLY3hyN0UrYXkzUFNB\nVEU2bTZBVUtGajdSZm1UUUw2Y3hCOVVWL00wVi9DcG0vUnF1dWR6dGRjc0JPNFVuVVZpSXFOd0s3\nQ0dLd2NoN2hycGwyekVKVFVzbVU5Ni9NYUVnajlwWmxGbk05REV0TFVXYjhqMnBwNDkvMDgwVDUz\nNUpHNy9pVU0zd0tpODJ5OEpmZ0hSeDY1ODVXSDQrUFhIL21oMHovZlB1S1pMMzZnQm8xMURlb0dr\ndUpINkFWbmt6L1ZGMWxWeEtmaExNNE9kQXNVK3FxelUzOE80UE5ITDF6SWJmbDFkNEcvMlFwSUN1\nMVR0SnVKQ3diSjdGdFNvYllhdnVsVHBqaXJkN1JRT2dWWG0xN3dKM0hLZ1QxdlI1NDQ2NTVBQmhi\ncHhteVNLek9KbGhZTkVpU3VYOFc5THlwSWxGWXpYeHZWbGZBSDk2VjRzT1BYZFdXbkJpWmhCSVVq\nMzdqelNlejh4TzMrN3dOM3BjRDcyNzRpSndjcFlvOXNYZmVSbmMvK0ZSOFl1Vkp3Y0o5L0lHbXFK\nTWdIbU51S0l4QjFqK2hGclVXRWtpc2FUWGVDejJJVTFmRXhSUEhXRnJWQ0E0aVZRclh3MVBhajFY\nNTR4dEpVbUpIQVF0dTF5UU1CbTdNRkp4TnVMQjJHN2xUelp5dzUyM2NsOVdNRFYzb1AxRXZNM2pI\nLzh6MXd1ejNRVnBESnhPTk9xRENudmIvRlNwS0N2VUx0M09ZbmNnYXl3a0t3cWNXa1pvZjQxSXJD\nRlY5NFk1OTlsOTFVVGd5K1p0Tk5xMTRtb0kwK0dreElWcDE4ZFUzTS9PZ3djeVVoZW5aQjV4T1o5\nL2tLSTRsZTVEbFpwQzFia2tUV0s2Qk5DVU1uVVpJSUZxM0Zma2hRT0xYT0ZDY0svUVh6T0pxb3gw\nZ2d1SVU1K2pCbFBXdEVxUExNenp5YWJQbnk5THBDVzI3ZXY5RUovV1N2ODdCcTZKUStkK1NodTNU\ndnZpZ2lrZTh1SkNhWFNKNXFXSEh6UkJOazBoaVVhSktUekpsaGxEOEt5VkRUeSt1djFuRlVrMlV3\ndExKRndnaWhjUElLemNHZXRhZEFucXhOSjAzd0h1dVZXVXRrZmtJdlRtaDlLQlhWekdYM3Zlckdh\neGtuQ1cwM3hlTGR2VUlUMUNwd2Rsd1I4eGZOTUFBOTRXeFNJZVkyYUVTOXM5eGdVMjlySXQ4cE9I\ndU9PRnFWaThzT2RMNDF4N1lsRjVhL1dKM0x6dGZja3RScFc2NDFUeEhXZGd5U3JnRXJqaVIzUEls\nUU9Mc1N0bWo3eW9jbU51Tk43RUltYWZ3SFhxME0vb2NPWnJYV0cvSmw1dnQ0cVFNTUE2Q2pXOVk5\nUjhCWENKeTdlN3AvaC9DeHh1a3hRRHI1NkMrL0tNSmZVQkhaV2pteUhyTDJ4eStLRGg1OFVzOHhK\neEJXczQ2OTFvUXArZ3VkSXptR21OY2p5dG1WSk9ESk1xS3hZY0FrZlpYb0lPdDdOZnFzZ09rZmlv\nZHNManA2NEhaYmRPNWRRdWExSWppcDVyaUEvdEE1ZTdXMWZIVk01a2NIUFdXdEpPOER1MnNGOGx3\nMjMxK0YrV3BYczZVZlBQVGdlNm9YMzF3RDQzTnhGMFJORjcrRkZGVjV6MDRTR09jRmtHektxbWNH\nSW9mby9BaTRxdGIzVkYrNDB6U1NjU05JaU5xZFNPcEVNeDdidXhqcG1jYytjT0hhbXo5MWVNSXJp\ncjdQNmZqUnh6N1E3a01aR0oxNjhNN3gyMjY3ZitxUm95ZTFnWmszRm82MXpIZm54VThpMURmY0l5\nZGhRaEVoS2VRa2pJZVYyaGNoc3JsMWhDQSt1d0krNFpPb0w0WmhLK01nS1BLdGpSVFFGcklJTHFx\nNHdqelNGUHRJdmlkWmdKU1Qvemwydk43L3VGRzJZWkRFZ2pNWHdURGVRdEtDUDluTjgxNWVnU21l\nZ2REbVZyOE9lWVlKb1dmcGIwdGkzOTVXRTdjN2ZkcXhxZVlTelE4SmgzeXdmaW1BSnRWcEYxdEk1\nTTNkN0l5b2dOTUxnR3hzWVJqSGlNNHU4MXNUVUs4YTFSdVo0b1ZKRWhycjVEa2xKeUUvYVlrV2hF\nVGdNMC9uSm1HRWZBRWgwYnE4eld6SGNSaW5XTmgxRFhOU09hc1dJN293N0hGRkpPakxTanIwNEQ1\nTnFUemZTY0k2VU1kTWd5V2FIM0lrejgvRnY5VFlrclMzZ0s4SjR3SHlmbWM2ajByQlFYQkYwNlFX\nbUtrU3pLUW01YW1CckZXak9qZkU3a0lhcURnOWZVdHlZSU1saGxsQWlxeDdWbHphTjlhbktXRTBQ\nYlpleURsSWdMTndUalhRbFMwTU16WUVyLy81WUtjczM3eHJlUVlBN3BFRUoxb1hTVDRQeHlheUlB\neGpDK1Vtb2szeXZwV1pxVm9lMFlzckxVSExiblA0MU56Yys2eVI2bXpqOHZUTVgvcEllZDRFbVpW\ncThhckdHbWVEbGlhMjlMeHVTNkdNQjdXOFJEb25JaW8xTkg4dGhOakFMb1dhQTZjUjJTRUlheUhE\nOENVU1JCZEdRTmJVbVd1WW8zS3BQeWVRSEp0MlJGeUZUUzBrNXcrS0NFNHpGVTJjdmxFdmdJL0Fr\nb2l0amEwR0tBcHRYZHlXTFRkLzdNM2l0S2V5VndRWk5qbmowdkl6cHBEYzRMRXJQbktiZ3NkSGx3\na1UrcUcvMjIxc0h5ZVFjK3lxM3lVcDdoUnRJSmFSQWUwV2tYWHF0UlhJcHZaeHhybFJLcDQrNkNw\ncmIxQjhjMzArdXNXSFRJYjhEUkdzM2J6N25oK29OMm5YY1F3M1ZqenBucWhkUVRkWW9WaHpxQXlm\nSEhaT1N1RzN5Wlg1dWZ3NHpVaE5hZXJZbzZlK29hVldOdS82MkIrS3VEdEZlODgxdnBSR1lGUHRn\nV0gwd1d1V1pvSGdGQkF0Qjd1bUJOSFc4Nk1qelR3UlF0bWxwTERPY3ozZlI4MXhham5ncjhGNUNB\nWnJKVGxLVE1GZVE4RG5sVnVhVDZ1ZnNPeDhnMUo1SndtOWxiUjlpOGUwRzNKa3Zsd3Mybjl0UlQ1\nSHJIMTZkSnpSN3hKSS9EaUEzd0tSTjdXTXMvYnJISlhmSjliOUNZR0dRWnFVNTcwMjkyclF4VmxO\nYktDM1E3Q25NVTdMQk1COWt5b3JmMVpZL3BDSnRNSzZudy9PNndZbFoydDYyVzhDUkh0c2VtSXdp\nZEEvVEY2Wi9LUkppNy9Qekd2VTgrcTBIcDdlRTZkajZCOURvR3RzWEJJVy9YMzJ1U3QzYnJ6eCtB\nRzFWcE45dG1idUpXN0dmWnpUYzBkbnRFRXFqcHpzeGpBVUpFejk1Q0dPZEJMazFtUXBzT0c0RUtK\nUnRaQjhDeEk5VW81WVlaMTkzRWVXdzV5TGtmZ2lpV0pQSG4za3dnVU1tTVNtaGlJemtxRzlHalBX\nZVljODlDMVhKTkVqTzJoSXJKYzFJMW85b05NNCtKVEhISlRWODZNZGNxblRlTjR5VWtuVUhGZHU3\nTUFkeGdrd0xPTGhqRHJmVUpmNVRFdEI3QUJ5R2hZWDZaMFlJVC9PZFZwaksrelUvejVmSzlsVGxo\nUGUyVnE2NW43VGc0UnBPZnVMZ0wxQ2hWK0RMTHZvUWxtTEN3VUFOeWkyaVBvcWw4cldIUkdUNnY2\nbnVNRjZLWTNEUUFEM0RKUjh2VHgvQmJzaytyU2wxQ2thc0s0dmVIMURwVVJ2NDFEWFU3STlwT1c3\nM2NhaGJUNDlUN2NBYTh0eG4wcWJ6VWRkeG5WS0YvUUhMaXIwbm5HRHp4aG9uK0FVTEs5dmF6MThn\nYWVpWjBPb1FDOFNreFhxcnlEelZIeGNWRDlxbU5iZUtydTRrbVJMdEdDVW9ldlFHa2Z5MG8zUEFO\nSmtHR1VTZHFlcFVuNnFIbHZ5a3BMN1k1akRUL3pDZVJJODc5VUtUK28xRksyQUVQNVNQZE5MWUYv\nL09iUGltc2Z5cndaNVNHcnJaMW9DN1NLdXl4TEJTNitvL1ZwbWJ5UlVuYXBUeUVFL0R3Vm81MkVO\nTENlaVNueWttWEpLSU51ZnQ5ZERrbkRQRXdUZTdXZDJxU09ESitxZmNrVGp6cVlIU01pdzN4YjFt\nQnV6emgxb2lsM1YrVkJrWUlmZmQwUjArendrV2JkNlRXMGxvbStMVTZqRVlxcjhkUm5SanR0RWp0\nejN1TE0xVlVFT3RqQ01jTVl3OVd3Qkt3Nkd4K0NvNmJRTGxhaU9zVzRwb1daM0lPMS8xQ2VSYUI2\nMC9MeFh3cXc5WHBTVmpTM3B5TWFWMzluMjFMRzN5akpESTZOWGVNakRvZmpVUDJ3N3Y5SVg1Vk15\nMFpCTWNMSTVObmlZbzhJeTJNb0RjYTN3UVp0T0JyTnptYUZrS3FwR1JiY2pxQWxMMURmdEl6ZDU4\nNGZ2R09abFVkVlFRNXBFbmlIVWkrRDdPemFnRFZXZ05nVm5jbDVlLzcramxNWW5XLzFQL1FVZ1Ba\nbjRxK0tTU1RMRklTZnVvV2NlL3VkTkMrbUIyKzBoTmJQejlPQyt0UDNZbHRmdkh4WnZKSGpMb1BM\nc2dUdW13U08yM0x5Lzc2VXRVWlBPUFBTdng4NmdsVUlCTVhhQlliSVVGUjlScmxFQ29wVjVUWmpP\ncnJaa3FkM24wcmVFT2ZMUXp5dlErY0dnaDlCL3d4ekkrbnA0alpVdFNaRUZvdUJ4TkE1TzY5cWg0\nUjBlUjBIRmptZ21aQ0FobEo3ZHVBYU9SbHVLQnpmNkhQVkRKT1Q0TjF3eTlYOGNyVVZkcTI4djBl\nSWpMOVFWQzZNdkgzajBQaTRaUTZLT0gxbldCRlFSaWlkWHIzS2dNZkU1YklHSTBSY1F2RTZISC8z\nRkE1cWhNNmdmc2tRTEttRnNhRG5jOUl1TWFwZ3UzejFORVhieHVlRlZITkdrYXFyMStJRXNVR09z\nSlZvY3hENVNyZEtsRWFuMi96OFBGdzJoanIwbEFTVUdabUo0aFZDcWdha1FuUEllUml6YnFkMWls\nK2dsSkdFVWJXZGFzREJuRWFjalBsc2dLNUZQMVJoY2laZTdvcHBZTk9tTEFBV2JkV1M4ZUg1UlZx\nMWVvc0ZUc0pJVW1wbXYvV2MxZW15VzU0MFByaFJBdFhqWUN4ZHBwb1JvOEd5VXIxaGltSmNJZVQr\nTWRqRHhHRjJOdFlXdVpRbzFXTldNc2lyU3JnQzJOT1FpeDRTQXkxVi9EQUhsWWxMVENPaGc4U3dE\nSUswMUUzYlZMUFkxRzRYb2NSWXVFWTE3OUR3T0dzYndEbkF4V1NabnovTmxMVTk4cVkyZXg3blFw\nMHQ4M0tSSGIzYjQza1c1dm9PblZ4bEdjVHROYS9sOEs4TUFyTEJNUjJVdXBnV1g4Z1dmc3gvaXBV\nVkw2VHczK0p3YkdWQnF4WTcyekRBS0p5R01hYnNjQ0o4VnNWSFA0MWpHeUJqbnJEc25Za3U5bGMz\neGNQZ0xiRmhyZjU5WFBFYlA2Y0NnQ3h5UlE0M09pMWpsb0o3R0FUUnE0bFZ6cnRFWitXcUUzc3Vi\nUDZjSGFtOXJIdEJzeDVKaWdtSWtLSlBpZlJ2ZnBjak5lMGZZdVZGOENnZmRPcmV6NXdIQ29JZ25o\nODY4Y0daODlmb2J0UzFscitORWFwVjFVeU1uVHcxRnU4Vk85ZmdVTTV4ejFXdktyem54M05RVGI1\nYkk0Mmw2b0FKc0tyV1hGOCtlZU41dCtNZmFvNkhuY2FhV0hQLzZiWXJtbWhPRjRHT2VZVUxWd3RF\nV2x6OEJacktvZUNLeWJJWUo2dTBOVDYyUER0dnFuSHd4ODAzUFBQT0JLcDVCMzlVek0rcTc3TWJS\nOE05ei9ZNDdOc2R4TDRSL251OTNIUERMbUN0eEkyT2dydlFHdE42NDkrRG12THgrUzlLS1ZoNy9J\nczJ5V3I3U2xWbVVETE5FZzZmQU1Ia0o0ekhPM214ZWtXY1lNeFdndlk1RTQwczUvSzAzeFJlOHQw\nK1NRK1puamJDWGFBRW8yNUp5MEFZbkRoRk53Ym1tQjlleU42czlid2l0SlBYVHRGQi9PZFp6cGMy\nN2ZtYzFVZldQQVZxcDhYVVNESXVyYWlYSTkyN2V0WCtuVFFvL2ZmekFIVXNabFBOSVhzbHE1RlI3\na2hxUUt1eGNFZXpCYWVjTXVCb0hoaUczeGs3TEVwZ0R4R0VPRk10RURNRWJ5TVN2WlRJN2ZGWEty\nRGdSUitXM21EaDVPNzdQYU9jY3ZlamF3M3FldHFRNkZrYkp1M2xyd2ZXTGtjYVdsQmgxMmpVUzhO\nbVhpbWl4ekJaRXdoQVgxTFZjRTZmV1o3NitqL3FRZkxtSk4rSDdpTGJ1dnZmbWswWDN1VTAzZm5K\nelgrTnV1bS9uK0lvTm45dDZ5MzNYREhwTm1tWVJQTDJvYjBtb0lFb2RMSVh5WlZwQUtJbjhTNHNP\nc2JBYThSZW9ZZmY3Ym1welVubzM3L3BvbWJqMFprWWhTcEI4NzRXSGZ2RzdjLzhwV2xpUlhvbnZH\neEp5dU9mZm1HaloyMFV1dkEvQUIzc2Q2ZGo5ZWhRdi82RTBHZFZDTXIvYXk1Z3RiOXgvQThlbGRW\nYXE0MGNmUHZVMVgzU29BN0V5Z2NmQ05McjB5aVNzSmlOUnN5bDVMUWI1V3I4K25VRWx6TGlJMXBG\ndk9NVG14REFwclZnSGNaOUhGUDhGT2Z1LzRtTElPN3hrODdZOW4vNitDRk5zdk9HK3pRRHRFVHVs\ndiszSGQreTR2NmN0NXByZDk2MGo0SzNPVHFsejc1MmEvZG5MT0RIMG14UVYvZ0tDeit6WWNYMVhB\nTDNheVNGYTNhUXBKSW54YlhBekp1SWN3d2pSQ29sY3BkR0pMRFM0V3o2WFluM2syOTJnS2s3VGp5\nK3VkbHVvblVlcnAwejZmUUczNE1qZHdCUXREM1VBNmVVVHkwNjlySmR4TlhGdklESnJRcVZTdXJw\nUXFGemI0NVExdlE4TkpFSzNkWGs4cjJlWWVxU2FKbERTakRrTndtUktyNVluYzRGaFNHU0ZTelhy\ndjE1SnlrZXNsMjNiODVuK2t2SUhUVm8zRURKU251cXZqTnJpSmJvcHhLZ0ViT0tDWlhsZGIrUGtS\nbDlKWFpQeVRCUlpvVGNNY2xYczhid0tubXJnZVdVQ0tldk5iNGdscldkSExzQVpBQ3pUOVd1NVZ4\nL3BEaUFxVGYrOHhGdUJ6d1lzSUYwWUUzKytpVWhlMnd6dStaaFRUd3hEUksvTHA5dUd2d2RIWHNJ\nMDBYYit1aytBcVFpdWw4dVY0SU5wMHJDNFJELzBESlBSa0V2R2U5b3I1NVBVeXJhbXowek1SVWpi\nMy9HRklvU3VhUVlpL1dNNXUwSy9aNjgrNU50Yng5RjE4eUJoY2tuNG9ERTRHV3BVemxRZFJyY2tW\nVkdDejZOczRTSUJoWTdmSVhXNVpKTmNVdnVsSWcxVG9MOVd3NHVScHM0K3ZWWUlHeG8xamJXMHZ1\nRHFqQ0c2MHZyYWV2V0hYZGxJQS9JTjJyRnRrSWFBWnhndlllbzZLMnNjeVEwM1VCTWFSOHE4dk5t\nQkVuR2htRzhMUXlTRmlOMGlpRmg3ak00aVdNZkZFWm5vU3RVTDY1Q0ZUS0ZmLzRyeGpUTmFvN0hZ\nOVJCWlZaY3dJYjlmMXJuRURzeXh5cjdjYXI3YmlhTHBXTXRINUw1VTB5M0ptNjJLTWpHUWRJaFFy\nL09xVXNlUU5kRWllYko5dlpyTG5UWVJhUWV6bkVKUGJtVTFtcHk1M1I1aEl6aFNqVGNiNTdXWUVV\nYkY5NlFhQkxHWEx2WEtYZUgrajRkYUpmWEZRcWphckVpazZDNU9XWi9pUmp6SjkyVnlicEZFck9u\neTk4T0liRzd0Zkt3S2ZSU25pTmJQUEk0M3R4UXAwSEZzakhYUmhrRXRqVlYvYVpFd1lJVTJOTVU2\nU1VxV1F3SysvOXVudXE5d2VZaURod2J6b21BWVlwbVhHTXFDRXRPbTlrTlpwWXdyWng3b3BvM3pK\namJWbTVrTllHbmVwRzVwL3E3V1Q5YnBOZkJENHN1TU5RUWtlWWdEdDBBY0ZpNEFPUnM1dTBoTGlm\nZERZanN3aGxaTXk1VmY2VVNFanBLRXRJWDBRSFVZbi81WVQ4UjNXcTA3Yi9Fa3lFc1lKYWN0aWFm\nVnRWc1UvZzlXTVBWbFRnUmExd2tUTEtBTmN4blhqWkhtTG1IcVNXeGhyaWxmVDYzdXlDT3BrVFZI\nOHd0aDhHb0xQdGVTcUQrbkhPdTVrRmFhekJjUDh0dGgvZ3VYZTJJK1FhaGg2YlI5TUZ1UGFlMHYz\nbmJJeC8rbWR5MmJJMFVTdFFVbGhhWWd1UW93d2pWMjFOSnEyRU1jTEVaUjk5OTRtbjhQNjFUTmpF\nY0Z1MWRzYmNqWEpRcU02a2pvRmpIUnJmZytvQjA3OXNZWFNGWk03NVVXWW1YZFIrN1ZJTS9LRnUy\naVFUT042NDhpYnlYVnR5VGxuY2hVNEZ3bVliekdYcVVrT3RHc0NhT3hJMTVsbzNRc0QzR0FoMjdP\nTDJsdFdRQjN0eC9mdXZ1ZUF3UjhYekJNYldSMWlVRExtbzNJNnVSdDVLN1hlUE91NjR1UWs4dGE5\nZEhHdUlGNXY5bERHeG9tdEU2bUJXenpOYWFvaXFxY2dpL1pVSWN6dUZWa2FVSnpKQnJIWkc0UWgw\nRlFTamdqenZwT28vMGcyUnFvdEQxN28rQU5EWXJjbHB2Mi8rcldHeHJnSTlyK2pydUwrdm5PTnZT\nYjRubTI3TnIvYnpmdittakxFNnpmOTNWdXMvSGI5dXd0WmQ3V1dSZG9TY3BBUzQydlFJRVBsbXR6\nekU3ak9EcGRJcExoYVl6bWc3STBzUHgzUmg3YUVJUjhEWXh5cm8xZkphcVZ6Z29oMUdYMXdvaFd4\nSkd0Z0tTWmxBOVpOcHZyZXY0b21STEs0Qlk5MHNtNDl1L0dscS85WFgyL0pibGlyNjJOUDczMWxv\nK3YzSFRUeDE5T0p2Nm9pOTIvME0rMjNuTGZ5c29vSDNCcDdkQ0xjZTNoYlh2K1UvUEJvTUlQY0R6\nMG00VFNPL05NVkRuUEI3WWNPZmx6K3ZmVk4vM1dPbGU5NG5GbmswTmJkdTMveUd6cmNpaVdJY2pW\nK2EyVEJua3h2UDNsSCt2b05oQm55eUxkZkZBeWZEUzVVQmlZbGVURldLaHRKN0EyYVpiNXlLcFJW\nVWZVSXRMT0puVTR3M0lMRG4wRHM2ZGFnR1Zyc2ZhU09NME1XSHN2OWxWL1ZvRGxRc0VWSUk2djAy\nTE1oNy8yNGloVCtoWXlCVlV3MytwUmIrbVVhdjdyQ2JLT1RXR25xL0tibTJlaGQ0U204UExEamJV\nVXVVaUViVUx3Q3FvdE9CYWk5YVRsNDRuZWUvVk52eldqYWV5aXFXSHR3VHBOVUhqbm5ReVpkY05k\nYm54QkV3eUw3Y3B5Sm5ISzhkREs0dUFZcG5uNnJGQ00xdFJ2Q05DcDBsTWpZNzdyYXoxdUtoZ2hq\nclZrOGtUengyQjRGZUpMNkdYdE0vdVRGTEJCUWJ5U1hBbTRFd3BMRk1KdUVWOHIrUlViYnZuWUZZ\nVWswZTlZUFlhUWVINWpiczRiRkhRa3dPdDIzQllRY2FaVzFNQ2JZYmljNFNCV01jaEVablZDOVBx\nWmYwWmMxbktudVlYbTN4Ykh5bE5kSkV4TkliVzViU2UvYzBtQjQxd0xnSXNnaHNrQjNRaXBSckFn\nR2JZbGJFbVRyei83dnloalREUWJZOGx3S0pOZWI1YmxkWmpTYUdYeTBrZXMrNktzV0pMV0l4YjJp\nWVNrY0FCL2MybGxaS09yeGtaR1d2WnNBVHhjWVBXTmR5OG40T3JRTDF3Mm5UOXh5a3VPU2lMNmxC\nZWM1RXE5MTBuZEFHSm13YWVZY21nMjc2LzFHZWZjdm5yMWJuRW9taW5kcmpvUWNRbWtHQ1p2WDQy\nS3lJY0VJWGRMMjR5aldoM0l3OHcyYjFZTFVxUythVkp6VVlMSkI4S1RPTmFvWlU5VVltY0xFTG5R\nck1wT3BVS2s1VUF1SHhLQlUyVlVRRmM0d1pFTU43dkpTd1BXQmlHNHBsaXROaGxHdkNUZG9tL0xK\nT3RGc0NaSURoNkpyUXZJZm5KbE1Cdks5d2JJRThtT21kZGtoMEloQjE5UStmSGFHUDAvbWhYcmp4\nRmlTb3RkSklXVVBiekRsL3FYYjlzay9naUVEdnRlRGtReG1XN2o1aEo4OUQvRWMzU0tLTldyVW1n\nQmhZZTNGM0k2VEFIYStKdm9YUDBZbUNMV0lvcVhFNUdtN1oxYnBUb1pNUTVQckQycE9zM3F1djdt\nNEs0eXhkV052VTQ4WElEVzNYYmIvWVpOWVFPejhjM1BTY3NvT1BLTVJFVXUrUUNnZElxYWE3OHl1\nbXJHSlJIcGRjMVFkdlRrcVlOM2prUGsyVkFhaENJeWxXSzNjVUhhSzB4YnZxMHVDQUtleVRCQ2hy\nZzZLQjBtSjNFYmxvWTA5MEpIUVUveGRlL3Ezek1rbXBUdjg1UHFReG5XWFc1b045SXlLMnVJWXkz\nd2NTUzE2bHJQTEVUL01XMngxYk10Wml3QnkvLzJwQW9ZYlBDQnZmcFJEdDEzS1dWTlF0ZHd5M1FK\nRXlUVSt1M2J2OUQ5NWxubngzdHlqUVQ5UTJHMVlyUTMwbXpqaU5nWEVpQ2llcUsrU1cyWHJheFBZ\nb2xhdkxVSlVpMTZsMU9lRkJRZTNtUVZHekk0ZzVjbXJVbjVDK0c4R3lTUlR3S08xb2VDQXU0b3Uz\nU0Rkc1NwWTMrWXNLRmFMSnEycmlWRFE1alFMbU1iV2hSTEZ5TEpZdEtoTEZUaEpReFZDamtKNWMr\nN2VuekQwOTBsTVpuc3hpcUt3SG05U3NESFFwaUdtQ1BUVWVrbHBrSmQyanVRTHdqaHRKbFpHQWRH\nUENBL2pMZU9HOXVQZGdyVlh4dmx1ckQ1TGFrMTJLaVJVNFU0NUZzSGU4RHhvZ2hBOWs0K2YzS2ph\ncE11ZFNkSXNENUFOUnFNc0tac3gzeWJIci9Oa0U4VUxacks2REp4SE9JNlRkU2hCeWtaSjFvT1JS\nK29saTJwamxOUkMzTTROVjBsc2JEejhFYTF5cHdZbnlkTzRrNWxlcUwyeStwNDQ1M1VZUjJpQlRp\neWNlcHdEZHVyOWVjZHRGa3RXdjFicmMwY0NrZTBjNWVubHVpMFJicWE0Vm9oRG01eFJLeDdKM1ZB\nOFVaeGljUm0rSlFEcmN1YXQvM2Z6aWI2ZEs4eFNkbkREWjFMbnhOblh3QXpWN2d3QW5acm9NbDhZ\ndis5YzdXYUFGbUFMK2d1a2s4RUpCTG43TE1RTjBITWhVUzRLOE9RemJZY1ZhYWxPdWJmc2w3NzRD\ndHpxZXZvSENYZklUNHdHa1BiUit2ZERRRmlaV0MybmNmTkNVRFZKRTNFOXlYWnc4bTlCTTBrekxS\nRzVENmdkVW1TOGdkSXhPSzJDREJtemt5ZVorSzF6bGFTdEJaL2hFbStMdUxXQ0VjbDlkK1JjM2VR\neUh0MEVNTXRFOEVWenFVbjB0cVpEd055RUNEUE1FRjM4ZXBuR1h2M3NyaWF2NHNzNmJzaDlCK1pD\nd3l1ZGQyNmhVUTdxU2tXTnlYTzlFYzQ5WU5sV3JydEtHRUVmaTlWUmhPeTdNYzVSVTgyRkhpSkJt\nd2wrVmNOV2pZcnVDK3o0MXJJT2NmbGpZRzBPdVZMazVRL0tOSjJPUUxaREpIVFdxMHFtTW55Z3BZ\nTWNaQW5mRXM5VXFzSHdvWk94Y3NLajRtNENXVVlGbHBGb084ZVA3QnZra0FINjdFMHF2dGZDS1Z0\nZjR1Q0x5QVFHc1NjRk5qUHE3ZVR0RUpwRnlMRlRBZEtJVkVvTFdZOWdzQ3pvZUVXREdhRE9HQTk5\nR3ZxSk16RzJTa2ZORll6cWN1NHVXVU5OSzRnSmJCZXVtU05yVHptMjNlTU5lSnl6SkZWY1NBWmJS\nYmo4LzZaeTRoaFNJaEUzZmdiaUVKZkp0R2lBaFI2SUxMd3M3NDVjNXI2QW9kcW5hdzZwOXV6WEJE\naFlhZXhzM3FaTVcvMkJxdklFUTluRmRKTDQ4bFF6RndNMmdlanlFbDZSR3d0ZFROMHNSTktRODhu\nSW1za2VGV1pxTkV1VDdMT3N0UEdhV0hFTU5DNlFuRFljY3lOdm94K3B4cVlEcE0xeS9KYmtub0w2\nemxKZXR5bUlTVGc2THoybDI0U3JhSXFUNFN5R3pUd01QcThrKzhGU1dVQnJaTjZ1VGh5K3VUNzk5\nWTVqd0Vpam90ZTF4RkxCdzdjb1ZVU0p3QXVFMUhaWmN6bC94VXE2QlpFMGpDbmk0VllMWjVnWklx\nTHVURDZuRzdyNTRobnlwMEtYbDRSY1lrTkY5d0pwNDBvdEtuZm5MYWZFengyWHMweEdQS001dU1S\nMlpZa0hMcmNYaXh4UzhsNEg1SG1aa1hHWUVaNmhuSGl4c1J6VFBEMk1zbEtVZ3RLc3RKaElRMWI2\nOTlkRm9nM3ZiQWlXRTdpNGFaWlBVTU1DZUI3NzByRWVuTWR5SmRRRmE5VHdyK3JBcWtXS2loNjYw\nWEp5V25OVU4vKzZPcFlyU0NmMUU0YVQ0cExrOW1XaE1qU004L3Nyd3Jodk9RNzJiWlRYWUpvcjJM\nbEUvKysyU1o0cGlia1RRbzdFcVhOY1lPaUpzT0V4U1p3b1daTStOdHp0SWN3bUVJNlJsVFA3UGZo\neHVXT2pYWml6MHA0K3FEa3N1M2JPNGZmRngwRnhKNHE2U05NNUJtR1JOc0NCdVdlSGNZRmxKTFQy\nRkJ1R0pFVDMrSVhCaVo4MTdBdlEwdm5MdmljNGhFbnFYZHlValV0a1VteTBRMWRkVlJjOE5ITXND\nNi85MmliNGZDK3lTU2hFWHFQTkJqWFN3dXhhNWxmYW1DSkczNElYWHZpTzN1amtuak4yME1jZk1R\nYXN0ekVxcEtqMFhkQTkzRjNWV2xPUVM3TlhzRUNrZ2hiVWdnQ0c0WEJaNVZQU2NWQjFoMnVxcmlH\nVk0zZ1lINW5nbFMwS0M5WUZXYXk3TTFlSjdIbWNra3hHU29RWkJsNUthVVhyMUNtcVZMSVVCZnRQ\nK241WVl5MGxNb01LOHZDTHhSci9WM1BrTEZwWEo2Y3RNa1RxYndNbzlseWFEN0dhb0xYd3psWjIr\nTFpTT2V0YlQxT015ZmpONzZkU1pqRzJpRXdJWWx0bFJsUmE2blJZd0RhL1QxOFo3d3BZV2c0UFRj\neHA4eEQ4YUNoQlNUdE04ckZJWDg1bmRReHk0WW85Rkd3eFpHcVNoZ0hOV05iN2xFaGpOZVFzbGI3\nMFJSVlYxRmZTd3lLL1haRFVFZWJOcW9mOGpIYlZ0SUhyS3NVcHJvVlFtUXN4ZjVlV0FuT1BIOVlN\nVXNkQjJaNElBM2FaT0VENS8rdGh4bDYyNTYwZ0YxbDJaVTh5NVpVajZiN3h5ak81VkZicEtGQnBE\nbC9SQmxuM0hPNk53MHhsRlp0UktSUFREMWlMU1VYRitZWXNiNEVmWmU4R1dvVGRuU3Fua1l1b2hZ\nSkVGdHJDYjRtZTRnVmFOUDBQWHNqVlhhSnRmaVJPbWVDRmVMQ2RaT2FTd3NRR2hhaDA4cE5Hb0Nr\nekVwcXpvbXE2anZkbHFSTUd2NlZpR3l0SGlaUXlJTi9maTNuZzMvNWNVSEJKVzJhbHFyZTVabW5Y\nTDgzcmlWbzJHMXV2OVFoYy9KWTE0ZVg2eGlpTUVJU3Z5VTF6MkFodm5nUURoN2NweGRsTE9jMkw3\nSlJxVUJhWmo2c2o2akFtRVBFT21qeVc5WEt5TXBFa0tMZ2U4SEFYZ3o1Qmh1Q2lpUHRSK0FYb241\nZS80QVVhb25lQUNjaFZBSTI1TGJhOVZwWmRFVlFmRDNnd04vY3hHbXJBSkc0WE5BSGFKaEVUb3Nn\nWlU1SDJLZ1RPUDlUS1lGMDk0bVFsbzRLUHBkSW9wRGp6a1pOK0hBcDZuTjJIT2ZmR0JJVHZNMGNx\nYlFMV3hLYkhpcDgrZUFvclVpU29tSjdjdmVoYWNoRWJjWldBcGRIZThHaXpFbXVCVU11WWsyUktt\nL2t1NzNXOTBsbUo5NC8wUitKdGtiR0c3ZDhhZTFuc2Z1ZVVFcUNyaVRDL2o4Ni9OQmRmOVQzK1hx\nZE5qeFJSWWxjdHIwU1dRbWkyMFREQXEzTXBnb25FVnlxVmc5MktQWkY0Q2E5S09Dd1BTZ3orVjlS\ndFpHSlJCdVRuU0VnRWZBd203SkkybndveVR1dU9wdkcvblBqR2pmZVNUQy9uWmdWaHVyV2FmWjUr\nMjh4bktnTTB0QkdtcUVHbkpPVmFvVjdFMFViWC9Sd1JiU2NDenQ3NytaZCsxOGcybThnNjBodzM2\nR2pqK3o5M3hXUkdQbTg2bWJCSW1XT1lDVUZ6dFFJV0dNaUVSbXRJK3pVc1dqWWprZytLT2tCUEdu\nZkVldWdNTk15NHVpbm02ZlNCZ3cxRGRQUEc4UDRlWWdMa2JaYkJyN3JMWlNzV2ExTko4aDdHTmly\na3hwTi9CTVI1NlV2aVZOZlRBTm5vRjU4Tlp3aTBybzVyS2ovczluV05rS2VZY1piWnZUMlpCY1NS\nelhkL2ZUR0cyZlhoUGxrYmIwOFhMYjlUU01XVmg5YThCV0xKclQ1aXBkWGhLYjBHdmx1T3ZGbUpM\nMEVITCtsdVdzWU9GdjVMbTY3L29ONHdETkhDK0l1VWY5Z2JuaUtOTWN3b0xOTmJaMWh5YTFncXdI\nSVhKK2N2c0lEcWpQVzhSWDZNT2V2QlYxMG9jUlpLWUNmNEt4cmxNUElkQllrWmNlb0diWUVSWEVy\na20yamIzY29hVTJrTU1hY2FvOGMvOTJJMmFoY3NoUkZEQ2s2b1hNRXFhakZGTnB0NSswSTMzeTFx\nOFdpMjExMnF6S3NzWCszTVJoUFlwM3JmT1BGSnJWY0ZtaVdmQytic25FYVBaMk5ZWEsrbnF3bHRa\nL2NMN1ZSdlVQcmRMUmllaWtYMVNTeUtEWVpobHVDalFxaHRxdGFnNUlFMTBmRW1wTWhCVjBQM0xu\nVUgzbW9oczg5SmlIcmJJQUpKSk9SOGFhelpMVlFzdUxSQktvYTBtZ3c2ZWJnSHk2TEtHT2NWQ3VU\nRitGd0JxQXBJWjd1b0JOWHBKbDZJekJYY21HQXEvMi93TGI2amhteDdjd3dKamZPWTQyYjQzUjNN\nck5KbUxxVk5RczErL01FY2FZUStGWWRob2J5bU5iVzZEU1pWUkRiY296N1NKbmxxS3FZeFN3Wjdo\nSVNTWGdpRlRaQ3dhbW1Kcklxbmd6VkdUS2xqMExhamJBTHVseWs2RHIxcUhwdk1DbmpxRXVZMlZj\nSTFES1MweG1HVVJZZkcrcTZHQjlvRExWZGNOMzI3WGNYUVhLTmR6cERVakZSNTdIQ3FuQ0ZjY0Mx\nMlBtSm1MVGVuWWVGaW9XbEdjdXA2cmw3dVZUc1k5T05TVlhDWkdIeWNJbFNqRFkxTmpzTjRxQndC\najBtYzRJNDFNUm9QdEg4Ymp1OUVBVUpvNUFDb2RBc1RNaVZSZmRMNnpMZElBTXRpRnhJcTRuMmsx\nTFYxVE9FUkdxVmtJaE5mWVVBSWZ3bVVYUzkrTksxYlZPQlJ1b3BPeDFKRW4valF4aElYbHU5d3J3\nSFFwdDk2Z3VRdXJUYmplY3BsWUErdGtkMC9kWkM3YjBBWGFYanZBSStDOE5BZ2tkL052S0ZuWnQv\ncVVrWEZMdnc2OFFpbW1xSUt0TUdjVkRtWU9LbTVlUURjYjJYa1M4YUpQMW1MTTRIU1ZZL2hjSmU3\nZGZ2VEtSUjUwZ0tVZTVDa200TEoxZE5qVjJBc0ZVcnhIODM5SkFTaFJCb3kxV202R1Vnby9ucFEy\nS0xRWFpuSGxxQnJPQ2d2SFVtaWliRDl1YzE3UTBnZkp4OCtvaG50dXBRa1dkZ21IcXdFV3NFOU51\nYXg1U0ZjV3BTeUNBUDNZaVZpYWxQaGdsSk5rMGZnU09MZFNzYUVrYTREYzRBN1R0Z3hwcU5JdFI4\nY3oxdlNkWHlpT1p4MXhZNEtwQWpwd2xnYW83Nm5DSlI3STlhSk42am1xNGlOVGhFbjh5R3lRQ0lP\nM1B3NEw0YXlDWGVDdkhRRDlFYmxEcGloYVBGNFhwb3FyY2JjV21jeWVyZytJUFFTcUc2ZDN3NkVX\ndEF0MFhxNWk5TzFVMVZ1bXhueVZRamZ0RXl6bC9kcWsxbXJ2QU5xV08zKzJFWXZ5VzE2VENqWXcw\nSkkxWkcxWmVWUzhwZm5WcmJtcFN2amJsNnBEWEh2cWMxNCtzUTBJVWxBVHViMUNBNEtNQTZkVkNS\nd3hoVEFITTdjR0NpbWxObHNvSDNZS2tYakNTVkVwc2F4UWhKYWd5T0NHcHRONVRXWVZzTW03NmE1\nNXVybTlXdnNrcWNUSXNYMUltNE1Lbm5hbitHc29kcUVxdTczWGlQVzZxMkZ5UUl6a21wSkJNemIw\nbUM3bXZLazBjMTU4eGkzUUNiRW9iRllxTHAyalpVdk9DQjRqazRReHc1TFNHZkplWDcveThEZWt2\nS1AzandRd241V05UQ1N4Z05kZ2FubzhJcnNXYnRuclZEVU9pQklLU0xHTGROUGQzNit4UzBGR0RP\nck1qRDRNa1c5WHBMeURFaVhLMEZzWDNjcWVXRzBaQ3JLYkJKYlMwMVJ5dWJ5RVFsenFmc3RLK0xh\nMU4xVC9JMEVwbDQ1cWF6SGJkd1oxT05aM1hjZG9nd3VmV1dlT1llQXJtVW9SbS9GMnJEMUdmMSsw\nMWdHRjJ2ZzRWaW96TktvblJDUktwMUo1SW10RnNGOTRnMEV2V1ZZYTdjdWJIUWV3U3dHVnBZVU5J\nKzArcFhZdm91RVE4WHBxenFJMmUwbUlOMkFDSHdLLzBXNVdJdlljVFpJK0pTZGZrdmIzVGVkZklL\nL3hsRWsvbEhHWWliRmROQ1Nrb3hDcERMdE9qR1FPNk5USkdhaFZsRWZEcVo4WGlLTWxoc0M0VnJO\nSVo5bmR2U2lDdm9scVJ3MGZhQitobzc4TWs3WnRZVnVRM1EzKzFyclhBbjNYd2xsekZBRG12WE5o\nYklTV0VpWUh3emR6TmhoQ04ybE9VdUJSZTBEQlBYbXNsZ3M1REdYUzZGaEJFU0l5U25MTnozTkMw\nV29EVUtucUtvT0d3S3lZK0p5QzRTTitxTXh0SUlWdEovQVhHL1NZUTFlL2JzMVVyb3A4RG1xaTAz\nZmZ4V2dGNGxKT3A3S1RYS3B3WGxzMnlyaXJVRm14U2ZBS0lQcXY5TTBZdmQxc1dqRmJXU1FwQzNo\nYnpDM1hYYzhRT3JxZ3FkbUhZdGZkQXljd1BNZEQzMDkvVFErN3ExVHpLemhXdmJrazRwZ2pHUXZj\nSlZWQ3pXZjR6V0svRkorY2dpMXVHNUtrdWg5NGkxb0xVYzJzS1JoM2FmaFlLbk5OR0xhQjFJbWRk\ndnRiOURKcm9lb05PMnJIcUJrTEY4SEl4blJhVDhuWE12ODJnNzRqZ0MyYzh5RjdSVTJDbnJRdlpo\nTG9lcEZKRnZsazVrQ2o5TVpLNVdMVHZpdU9zTmZPYVpEOVJJVkFKMWtoVHRsVXZ6ZExzV0t6emYr\nZG5USk1TWmlTRUtVdTlWaDhuSUo3WGt3NUZrOGVRRGpTOGNMNitxVWwzREQwOVFLY05lWkVuNVhn\neVg0cVRTY3hVSHBwQUdlbW5Jd1ZCMDBqOVp4RmNhQllQNzl6UWNrdGh4Wm1nc3hDdGN3VVVNMHZ6\neUdNTXZEa3NHSEVmbXpSWHdTY1BSa0ZaTWNNNSt4emw3SENSRGlVSWVWSTc2MC9neUloTVNkZGRo\nc3IxTUdYbmFCd1FFU0dqM29ia3dUWE1VU1lCdnpEalN5SWxRUVhWbWFkL1dpZDNIQ1RJSjR6OXcr\nRkNPb3g2NDNZcEdySnR3aGlJNExZa2dPK2JyMzhXRXVHZUlnN1h1ZTcySXd2a2hNbFMxWjhVbGFs\nOXZjZnFVZWR4MU1BUUk4dUtFTGZrT1Y1RVRGcHRlSUlFcEpzTWpSaFFzWGkrbnI0eXZJQ3k3U216\nMU9adFUzZ3drSHlTRmY0YlUxZ3htNzNGSG85WFNoUXN6TDB0T2RicHhkYnh4MTJIKzgwN2paTVp4\nU2xQTUN2bzY1ZU5STTFEN3B4bkV2UEczOTBlM0xFcVpvMkZDTTlXYzBjU3Rsb2kxaS9yQXhGRDhs\nSE5wWjZ0ZzNrbW81azdwelJzVGxzM0dQNGthcEF0cjBSeGxFNDluMEVjbTR4U1NLWlRHeVlwVUdT\nYm5rN0pPamptdEFnRWFQWDdnZnp0TkZCMFZRY3d1WHhYS3A5Q2VldkgvKy9XWlhRbENKem9jMU9N\nemJ0OUM2REJPL1dlemIvdW5IcnhUcmRYdnRaV3duYzF4RjJSejY5L3QxSnFVejFxb2o1cWkwSE5v\nNWdIdGhWYU1yVGxFaEtmWUZEV2xvK1UxRXpJdFQrS003b2VsTUtiRmp6U3JhYTJKYU9MN0p0Q21J\ncFhPUXRDdzJwam9lWnVNWk1xWm9UVEd1QkFzK1hpWlBTWk9NU1lldGFmMjBWSGZlcWVlK0NjYXJZ\nWUJhVjVUZHBGRFlyeFdWWjhsNEZySEdMZjhTTjIrVDh6NGU3cU1NOUtBb000OEsvQS8ydStCdmtM\nTnZVQ3RGMWVCd3BUcE1NR2hQWTFoSE1uNW5GYXM3TFVDMGhxeDdnZmljUERnN2JVdE45N3pHNDdT\nV3pXMjFseTlNTEY1dEpkemxDSTdXazM1NDVKT2xVSFMwNWhzclJtQ1JFNkswTWJ2UHZ3dko3YnN1\ndWNFRWEvTGdHL1BwaU9KejQwUVk0a24wa2xYTHRTWVpIVjErY3BIQytNWHpwR20xN3EwUWk0NkN0\naVZrbUdDZlFxT2wrQmNFcW1YdnZUVzVheWRjNG5Oa2RhU2ZZb0NTRk15blNSUG51Ulk2elB1bWRt\nUk1UMHhURXI0REtkVDZ4WFgyemdqck1xQUkzamdTWDl2VklQUHplZWZCR3BOOW1xbGVocEdrOXdx\nYW1HWVVQZ1pmZENSeCs3OE13RDZtaE05ODdVUHFGTDNTLzJQRFBkUm9BcXN2TjQvSUhUUDA0QjVE\nU1NadExYQzg4dHFNTFdDUmpDWTRpdDVxam9xRlN0WTgrS1gzejJ4ZWRjOVI0bk5XaUI5Y1gzQ0ox\nOHN1R1VNQ2tZQmhhaHpDaW16WXFZODZmTkkzNXB0Vlpad2pKMTI3VzJJYmQzTVJxTTA5VlpjTjBx\nSmp4bVhha3lpYWN5SW03QTFGeFQwV2VqRXczZXFBZktMZlNpOVlYbTU5NTFFWjV1SnhxdEQzblh1\nQ0YwR09kYXFuemZUVGw5US84cVZPL2NPQWU2Ym1rUW9vT2VQajd6aWhWcnNhNGNwSHB5ZStlSUhx\naEJVMkpkbzl3TDRjUysyQ2Q4T1daRnVwV2kvcWJBMWh4Ump4OE0rdjFWMU82dVJhUHpkYkV1TE5l\ndFNVWDExNHlKSXBwUGxzWTB6bXNlUnFiMG9MWTNQdktWM3l0bFNUMDY1WGloblZtc3VvSytQbGpl\ncnB6R004NURNTmppRFZaeE1TMkdpUmM4d0dmNmpYalR3aUtKejJLeGVMUkovSmNPVVBJUUhmekIx\nVmozdVdZMWlKWkt6OVZSWElmeVZaeTZoci9pL3hhZVorSnNxemxaRTQwMitsSmhtQ25oczlGOGZm\nZVNVcnc0MUUxVnJwMDU1SjJMZEp2Rmx4K2g1M2I1bkduZjR6T2daSWpyZU51NXdWa0Y5SURSZEpm\nYlhLdmZYOUFFNTV2QlNjelViWE1oYkRISVpWSEZnU2Y4eldMUkNKUXpoczQ3a0oycGxjMzc1aFJO\nL2I5T3ArOEh3Ulo5WFRweld4TE9mTlZQMktmM2JnbjlCQ1AvRnYyZjVVbG9iK3h5eC9XTi9Ucmgv\nNVJMK3BMNWZkbjc5YVFaK0trMXFmOFBNUCt0YzhoTkFkRWUzanZONVVrWGNKL28zQktEWGttZlZm\nWEJ3WDAzMXJwWnhBci91UWRFc0ZzVjBIVVphS2paNFdxVjFTRm9RZnJMNFM1Y2RldlJYdmwxLy8z\nell1NzBEVVpXaDdlKzQrOTErK3ducE5mcFVld21pOU1MRHYvUlFZOC8vMmdkT2Jkdno2ZHNQUGZo\nZUgvUTcvTWo3djE3L0xKTUdmNTM5ZVJqOUV2SGpBTDhsL0tFaEYvNzczc2JoV3dBMUtwTVRvN2R4\nUFJKN2x0R1g2c1ZxSWFrbk05WXdtdCtlcGdVUkhhd1BBeWlxUDBSd0ZVdmlSVy96bUsrQ2ZYa2s1\nWGVpT3JQMFFvY3laaGs0T2ZkWW94aVFUVkpuMHA1dVBEbCtMRHpRbXRDU09ISG13Q0NYRmVIOHlu\nL3c3d3JFcUpyVEdENzlPS3J1SzFudXh6U05ucVZ3VWlUOWdpQXRhajQ2aUo2V29qMUhWZnE4UTdX\nc3h3ZzR0R2ZQaDh5RER5NEMrT1ZsU21UY04wU1NTYUpvQ0VpZmcwMTYybHFjSkg5SHdoZVk0dVhp\na3FOVFhQejJRTmVGdSs0T3hmMlNtSEJtYWd5LytPY0pucysyS29VMjNINndYZEhTN2g2RlpDcVVJ\nNDNMcStXWkw3Ni90djBkSDJzZU83WmF0S0xUSUJmNjBxTzl2SFgzMmk5Uk5QeFdtMDc4MXRHSDcv\neVYzc1lKYmQ1OTc1K1phUGhXbTB4ODh1Z2pkOTR4eUZWZHR0dkdTNEcyM0x6L1I0SDRuc1RhdDU5\nNDlKZDZsaFJiM3JUL2JTVHgvNXNpdmZXRmgrNGNxQTd6L3dOaXZoeHB0VzM2TXdBQUFBQkpSVTVF\ncmtKZ2dnPT0=\n'),('e002','침팬치','dg651sdg','5gsd51','@','','박민환 집 주인','0000','0123123',NULL,'2025-03-17',NULL,'휴식','인턴','회계부','사원','',500,10,50,'12',NULL,_binary 'aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUl3QUFBQzBDQVlBQUFCRzZjVCtBQUFHUlVsRVFWUjRu\nTzNiUzZ4Y2N4ekE4Vzl2UzRXcVIwT3JLZzBxSkI3eGJGa2dJU1JhQzRtV3NDRmlRVUlFQ3hZc1BN\nTUdDNkt0V0ZRalJDcnhDQnUwSGkzMWJoZEVpS0JCUzl0RjIwUmIxSlUvL3l2WDdjeWM4N3QzWnM2\nWk85OVA4aythM3BrejUvRzlNMmZPLzl3SmxETUp1QUM0SERnYm1BMGNDQXlVZkw3cTVTOWdCL0E5\nOENHd0FuZ2IrS01kQzErUUYvWW5NT2hnUEk0VXlydkFwV01KWlNxd0dOaFRndzF5MEpXUjNubVdB\nQWRGWXpraXY2dFV2UUVPS2hudkFEUEx4bklvc0tZR0srMmcwdkYrYnFIdzVIWkZEVmJXUVMzR2l0\neEVVN2ZVWUNVZDFHcWtKdjR6WWRpL2o4MWZzYWExQ0NvdDREUGdFMkJUUGtrYXZnelYzMkMrSERJ\nRE9CTTR2ZUFZYmdYbUFkK08vTUhTZ3RKV0F4Y0IrM1IyZTlSRjZWaGVtTDlTdHpyMnFZMy9tUU5z\nYi9HRTlQVjYvMjV1aWJvcUhkc25XeHovYmJtUi85emQ0c0hMdmFMYkZ3YUFaUzA2dUd2b2daUHpl\nVW1qQjMxWjVxdVZ4bzFEOGpGdjFNSm51WlYvVG54Mk5YaEFPcUc5b3VvdFVOY3R5c2QrWkErcGtU\nUFNBMjVyVXRTNm9hTFVWeWJuWTkrb2lWdlQ1OWJjSms5OEVkamQ1WlZWOVhibkMzYU56RTNCbk5E\nZ0Ira3RhV1dIVjB6MXRTbzNNTkkvcld4cThOYXpCWmplL2ZWVVRVelBEWXpzWXVOQXZvMWhwTTM1\ndW96NjAvYmN3RWhUQjVxYzJPNXMxOTFYNmtucDJQL1c0UC8zRzJoeVVXN29hNVg2MDJDVGM1Z0Jy\nK0FxeEdBVVlqQUtNUmlGR0l4Q0RFWWhCcU1RZzFHSXdTakVZQlJpTUFveEdJVVlqRUlNUmlFR294\nQ0RVWWpCS01SZ0ZHSXdDakVZaFJpTVFneEdJUWFqRUlOUmlNRW94R0FVWWpBS01SaUZHSXhDREVZ\naEJxTVFnMUdJd1NqRVlCUmlNQW94R0lVWWpFSU1SaUVHb3hDRFVZakJLTVJnRkdJd0NqRVloUmlN\nUWd4R0lRYWpFSU5SaU1Fb3hHQVVZakFLTVJpRkdJeENERVloQnFNUWcxR0l3U2pFWUJSaU1Bb3hH\nSVVZakVJTVJpRUdveENEVVlqQktNUmdGR0l3Q2pFWWhSaU1RZ3hHSVFhakVJTlJpTUVveEdBVVlq\nQUtNUmlGR0l4Q0RFWWhCcU1RZzFHSXdTakVZQlJpTUFveEdJVVlqRUlNUmlFR294Q0RVWWpCS01S\nZ0ZHSXdDakVZaFJpTVFneEdJUWFqRUlOUmlNRW94R0FVWWpBS01SaUZHSXhDREVZaEJxTVFnMUdJ\nd1NqRVlCUmlNQW94R0lVWWpFSU1SaUVHb3hDRFVZakJLTVJnRkdJd0NqRVloUmlNUWd4R0lRYWpF\nSU5SaU1Hb0xjSDhCZXlKTFVyanlKN2N3RjRtTlhuQ0xPRGVaaytxTU82ZmdLWEFJT1BIYWNCbCtk\nK0ROZHJYcVlHR0JudHNwSkRIaTVPQkgycXdUeU9qOGhVWXpiaWQzbmNjOEhVTjltVmZCUE1uY0Iy\nOWF4YXd2Z2I3c1crQ1NXTVhzSkRlY3ppd3RnYjdyKytDU1dNYmNCRzk0MkRnclJyc3Q3NE5KbzFm\nZ1huVTMvN0FxelhZWDJNYUU0Q04xTi9Vdk1PYjJRRE1CNzZnbmlZRHk0QXJDeDczeTlCdmNWMmxZ\nR1pRYjJrSHpnRmVBR2EyZU54WE9acnZxSmVKd0dMZytvTEhQUUE4bnJjM0hSZU4wYm5BMW9LM3pJ\nOXIrQXZ3V0ltMytrZU5wRE1XQURzS2R2N0tmSEpaQi9lVmlPV3BGbGZjMVFaWEE3c0xEc0xMQmVj\nODNYQkhpVmlleStjMzZyQWI4d1JacTRQeERMQlBSZXQzVTRuMWV3VTRvS0wxNjB0bGZvTWZyK0FX\nam11QTN3dlc2ODBhZld6MmxZZEtSSlBPSTdwbEliQ3pZSDArQUE3cjRqcHBtSUg4bGJVT2s1V1hB\nTnNMMW1OZHE5c0cxQjM3NXBQSG9zbktvdXNnWTNFZXNLVmdIYjdLMTVOVUExT0ExeXVhckR3TCtM\nbmd0ZE05THlkMTRMVTFCdE9BMVFVSExuMWtYTnpHMXp3eFgxbHU5WnBwNnVYTU5yNm0ydWpJZko3\nUTZnQnVCczVwdzJ2TnlSOHpyVjRyWFprK3Z3MnZwUTdmeWZaTndZSGNrRytQSEsxWndPY2wzczNT\naWJCNndLbjVodkdpazlCalJua0QxSnFDWmFldjFvczZzRjNxOEdSbDBUZVhUNE9UbFFjRGJ4UXM4\ndy9nMmc1dWx6cG9mb25KeWxVbHI3b2VBTHhVc0t6MFp6azNkMkc3MUVGWDVhL1VSZk02clNZcjB3\nVGhzd1hMU09QT0xtNlhPdWlHRXBPQnkvTkZ3SkhTclFkTFNzUnlmd1hicFlvbks1OW9jQ1BUSXlX\nZTk1ZzNRSTFQRDVjNCtFOERwK1FyczB0SzNnQTFzZW9OVTdXVGxidEt6RG9QQXM5N0E5VDR0Mjgr\nMElOakhLL2xPU3oxZ1NuNWdJODJsbFhBSVZWdmhMby9XZm5lS0dKWkMweXZldVZWM1dSbDBaelE4\nTEVlT0tycWxWYTFacGVZR3hwNlp6bTY2cFZWZmY0VTl4N2d4eWIzc3p6b1Rkdi84bUxUM2pQUmM0\nSGo4NzVKdDBsODFDTi9meTVKOUxhL0FXSTJnb3NQUjZJN0FBQUFBRWxGVGtTdVFtQ0M=\n'),('e003','이이름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','사원',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e004','사사름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','사원',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e005','오오름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','대리',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e006','육육름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','과장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e007','칠칠름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','부장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e008','팔팔름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','사원',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e009','구구름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','대리',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e010','십십름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','과장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e011','십일름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','부장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e012','십이름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','사장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e013','이일삼',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'회계부','대리',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e014','이일사',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'회계부','부장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e015','이일오',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'회계부','과장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e016','이일육',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'기술부','사원',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e017','이일칠',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'기술부','대리',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e018','이일팔',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'기술부','과장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e019','이일구',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'기술부','부장',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e020','이이공',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e222','이회계',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'회계부','사원',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('e333','진하핑','jinha','ㅋ','asd@naver.com','123','asd','asd','asd',NULL,'2025-03-13',NULL,'재직','정규직','회계부','부장','asd',1000,1000,1000,'1000',NULL,_binary 'aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUl3QUFBQzBDQVlBQUFCRzZjVCtBQUJEUWtsRVFWUjRu\nTzI5Q1poa1YzVW0rSjl6MzRzbE0ydFhMYXBWRWdVU0pmWVNVcFVRcm5ZREJyZVJsLzRzMmJTbk1Y\nUjdMR3hMNEdYY3l6ZTRpK3FlenpNTVE3ZEZTY0pnZXNEdXB1Mld2SU14RERhMkd0QUc1VGFTVllB\na0pOV21LdFdlbFZ0RXZIZnZtZS9jK3lMaVJXUkVaa1JXWkZZV3l2TXBWSkV2NHI1NzQ3M3p6ajNM\nZjg2aExUZmYvVElBRUdkbzB0bVRxd3NvVmxLelFvOFJ5K1NSaCs1NkFmM1FaMjlaaFkxbURELzRZ\nTnJ0SzV0M2ZiUU1GSjh3VWVsbDFsWis5K2pEZDc2bnJ6bVc2SkpSQk1kZjBUZkVNUTJKL0t1cXhl\ndUpvM2NCSWlMdUVRQS8xZE9aZnU5dHd5aE0vUVlFUDRSVGsvOEV3SW41WHZ3U0xUeEZ4TkZXZlVN\nY0liVzE1UURXR1k2MkFBSnJxMGQ2T3N1bjk1UlFtUG8wU3RGdG1FeW5BR1BtZStGTGRHa29Fckho\nblZnUXdSRmd3ekVCQVYyM2xSWXFwLzhXaGVnMlZQMjVhdk82NGlXNnBCUmQ5QmsrZTh0T0FMK094\nQTFrUVV1MHVJa0hjSTUvaDVqTGNES0FVeTNSOXpmRC9KYzM3VUpFUDd3a1hWNDZkSEVNWS9DTGlD\nakdrbkI1eWREY0dlYitOMjBGMFk4aVhaSXVMeVdhTzhPazlPTW84Z29zOGN0TGl1YkdNSHQxbk55\nK3hDd3ZQWm9idzF4L3kzVWd2SEZwTzNycDBkd1l4dUlkS0pyQ2tyTDcwcVArSFhmcUFQNEQrWkg1\nMm82MjNYVHZLeDI1M3laVGhDUzEvM2prc1R2L2JINW1XcUlaYWEvd2xpL2QreW1PaWkrVGRPcC9I\nbjdrL2I4OE40YjVyemR1Z3NGTzJMbHp6TkZIZnEyeVpmZCtMNStvRVpzSWxBcXRNRkhoQjRoak9K\nUGVuLzlzMjU1UGw2UTJmcXNGbFVBNVQ2RURHNkt6aHg4Ky9RVmczN1NGcmQ5OTM3b0k3dTB0WTNM\nRXpyQWplL1RZdysvM2dkZzZiWHpqL2pVVXl3OTMreDNzREtmaWpoOS85SzR2dDZ6enRmOXBwUzNI\nUHlKTUdtbHBHME1HUXQ4Nzh1aWRYMnMvMzdVM2YyclpoRlRlS1VTbWZad25pWWdwdWJCcjA1V2Zm\nK0NCMnh0ZjJIclRmVHNGN3RYT3VBNmhIQU5qcW45OStLdS9lcngrWlBzN3ZsQ3NqVDU3cXdYSzdk\nZEUxMWR6eGYveDRqNDhqMTNZVFZ5NHprbTFFUnZzbjJGTVlSY0t0QUpKdi91UjBOYmQ5KzBXaXhF\nQ1lpZHVXTVJCaURadjNYWGZXeDFjNUdKNjB0U1FpRXVVbGFZeGs2bE5MVStBKzVob0RZU2FIMmdR\nREZUZHZHdk5ucU9QNExIMm1RdVVYZ3Z3NzdhTXlSRVpBM2J1aXdCYUdJWWp2b2JFL1o2dVJVVnJP\nNUZoUk03OUxZQVdockhsYUF1UmZKcEVyMi9ybk1vTGp1eXhWK3o1eE91ZmV2Q08wL25QeG0yeWdS\nbi9tVVJLN2VQQ1dNVVEwTk9Qblp6NGtsY01NaElqN3lLS2Y0MWRiZG9pTmFqc0V2a1lnRjl1ekRQ\nKzlQSlkrRDVtdnFMOW1wQ0pVZVRrM1FBOUI5eFQ5ZmVDcERaM0hZYndGci95UG1ubnprOUdEdTZU\nWk9pTHd2TG5SSFNsdUpwZWxyY0ozQmVaNDcrTXJQdHh4N1hxTEF0Z2dLbjFSY1NtVUNLaHQzVWYx\nejZtN1NWNjNqbU1RNWR4L256VHZ5LzZBY1diSnlyVk4zWWMxbVhjVFBPSk9CM1RaYTFDSUx4dCsv\nYTdpN05meC9xMTZQSms5YzB3bjlnWkEzTHpuT05HUWdiRXBQYzN2M0wvMkJGRHBLZjFTSGphMjE0\naStsdGZQK093bVY2a0o1akRPSFJWL2FYN1hBeU82SFZkaGtuLzgxSFhNZUtzUHBUYnh0Y09iK2g5\nbnU3VUg4T1V5bGREOElvNUs3eitwblJhVkRpbW05QWN6NnlRUVQzRk5kaTdkeEFCMVhrbmNYVHRB\nczJrdDNrNHBwckhQVjBzOVhkeEMzSURpcWEwR0NQVEFxZVhadjIydjEycElMQkZUazZmK29IY3dG\nNkkySUNjdXdRTUE3cTVneTYyT0VnRVJMSUNGYXpFWWljUjNTelc3ZHo1aVhoaEpsU2p3RzFhV0lZ\nSjRZQWJPbGw3aTRhRXlvbUpGejNEU0VBenJqeTNDa01MTmlsaC9jSXl6R3ZlckJOZXV4aTNvMENx\nOURMSG9GVzRERWhBdzhta0dWNjRHZW1LaFdXWUtsNEo1cFdMbDJHOGNhMmF6T0xYWWNRcithVTRT\naGFJWWJ5dDRWT0hGbzVoeUwwQjhXSlZZT3JrSFhqTGNCa1FDZUpxSlZtNExRa1lHY1JKZXZmMENu\nWXUvbUFqcWNkMklCZG1ma204NlJMRlZGNm8rUWcwdEhBUzVtLzJxSXY3VlpjRi9vVVg2aVpjSkhs\ndnVTMWhJU2o0KzBwQjExNEloams2dFFHRXJZdFpmMm1Rb00wRnZqaUpkUHNVTGl6TWJQNit4ZmhI\nZTgzQ01Fd1Vid2ZUOHA0WWhoREJhRDdjcFNFUldhQ2JjTEdrZm0yM1lHc1ZVTFRqMVBVWDdRWHY5\nUVN2bWxYaDlYRXIvKzV4V0o3RUpTTHkwSURMZ0VqZFJndTNWaUl4dGEzSGFXR1VYcUpYei9pNUQ2\nTEtPQkw4S3FybUFiejNhK2N4VHlRS0Nwa1dzTTJDai81dDkwaHJVM2RvKzRvR1BqSDk1b2tUNWtn\ndjBYUjRnN2p1SGt3UlM2UUQvVHFsazBrOTR4THJhMnIvbmNwZmtxYlRwUktCL1Z5ZEF1Y2FZOHUr\nbEV3dDczQnRmTEMvWlY2UjduQ0VhRmFYWkpoMEJ6U0NQdE0zRS9jcitKbUhQalh6K1lnNjNyQnM0\nUnI2bjJsNFZEQ3VWck5IeGJtSitvVWdEV2dLbG9PNGJrN1BjQTVTSmpoUDVDWmFMNHBUUk0ycDlt\nK2JnanZwVXZzWkR4Rm9DWXdLRWVSV0lGN2RjWjJReElrY0VYRW16eHc2U0VUV0VMRlhka1U2Yjkz\nZW4rVFN2M2V3ZjBmRXVRdnZtRUhIRDQzWDJybjF2RGgzWEZ5cnprQ1FDRVJyNi9MTVZzKzJQeW1x\nZUU5Q2NLNTVQUndScFpOemxUQ0N2MWs3Z2hOMEZXeVhwNkxBUU1YKzBhek1FaTVZVldBVERicFBu\neW5WVFMrZDZkbDc2aCs5Y0hickg2OS9zeHVlYXZ6d0lWcVJUTXJVenhCRkg1OWxkaCtFRTJjL09F\nU0YzNXVRMFVZY1Ixd1J3enlrcUswV092elY5ejhINEwyZHpyWjU5ejBIbUhoMXAvWGV1SFhUVXc4\nZk9USU52bEMwVVZveDVzUEUwZnRtbERJY2FYR0VQejcyOEozL0FUMlFyY1lmTVRIdFYrOXFuY3dV\nTzRtTHExMXN2MDdFR3pxQ0loUmNaZFA3aDZuOC92cjEwR3V4N01MWmNhQnoxSDlHaGlITEZwTlhi\nUVN3dGlIeVczNFlnTVJOZ1BDaDJYN1VnUU4zcEZ0dTN2OVAySm9DOFhUdWMybkM1V2pvOUlSVXIr\ndDZNZmZ0YzRlQmMrMkh0OTE0OTk4N1NrR3pHaDJxYU5yeDd6NzhjMk80S05ycjVYYTNUelA0NU5s\nT24yM1pkZSszdWlINFdxZzNiSkNuNHdmdVVJblFTU3FjMzdMcm5pTlFodWxpcVFGUytlNURIYTdI\nYmZjYkhEblpwNFRSdTFEbGx5SGlZc2RuUC9iUzVYNzhzNjgvaWRsSmVxbG10WG5YeHduVVg0UlRV\nTGdna3FiVWkwNDJ3LzY4TU1SbmU5SmhCa1FDbkErTTBZMzZ1eDR6YzdHUUlESFh3WFRXbFpDSUFq\nNC9nVXRNam0yTmlLWnRLWXVTSkswc0pNTUFyanJJSjJSbWhnbjY2WFVkZjU5aExUMzBEYnpyYTkr\nWXk4UnI5OXd6c25uWC9wbXRyeDRwYkhHWGdWTVIzZ2haWUg5NW4rSjZ6Z3lqdHlDeVJUaHM3NnEv\nQUgvZzQzMTErdDIzck1FZjNQSmVmSHJQckppVVl0WDlHK2I0UWMxRG12UHFsMmpCYVVZSjQ0cSs1\ndDMwa0lCS25xcWJCTGt2Tkk3OS9wdTNvRkQ5RWtRK2ptaHF4Z0RndHRkK2VpVVJ2WWRNWVpWanVR\nd3JhTzV6YXMvUDd4emRRT21YbHJvcmlVNWdoNnJyQUV5djBCQXhVSE9QNGFjZmVoYnYwdElmdHhX\nUXZ2QTdHSXAyWXRLT29zZ3ovbGczUEhrakVHM1NOQk1CL1JCMmZ1S0RPSERINHROQmJydmZyRG4y\nM0xRb3I2dUtXa256NjZVVktxMS96VWVHMDVHbUEwelNFaFZ0S2Myc29zWEdNSUFkbmxSekxKcW1I\nbmpkeG4zQis5cVU3UEgzb0dqZWptcVAyN056YjlhRUtVMlNJc2kxbStOazIxSGdHU3d5Mm5yOHpM\nVWl3NStlOWtIc2MzMWUzcFpuTnpEeTE0WGwzZkZRNlFjTHVYd3BpZzFaVTNzY3dNOWgwVEdNQU9t\nS3FRS012bW43TEhHcHV2VDgreis5ZVJrbTVkZjdVZVdFOEliQWE2TE9vN0wzSkM5Q2huRXBSdGhF\nTjNZUERjajg3VVprTmpIenBuWkhHOXZlQ3B2T0Y4Mmc5QkxTbGVPdEhuRWxOYkVGenlGeXdmZFNr\nWjlFd1d6dnRmU0hWZ0VuNEJWTlo2K1B0M1MwbGdTNHROc1VPUkY5TmpxOE1OOVdtYVlSZDVyN1Vs\nd1R6ZUdaVmNLd0lGMHhIc0lvZVlwOEpkK0hjZnNqVTdqL05vUGtoWjlEMVB2RlM2bTRMaGJaMEZ5\nRG1tTjJ4N1ExcXJnWDkyT2JkOTI3Q1hCUEhIM2tyai9wZVpJbEdoaHAvanNJMTJ6ZWZjOEhaMkFZ\nZ3JDRFhhWU0wMzRHN3dIK3FuL3ZUcndXRWIyeHgvTFBuZ3FnVGNJMDBqeXZNZ3hkTlgybFRwUGti\nMlV1M0dwdDViOERXR0tZUzBHZVlmaHFKdlp4clM2SjVJQXJwTEREVTYwU1J0L1dWQ09UVUNIQnVY\nK0ttT04rTEVBSDJVYWtmTnFBSStnVUc5VWk2TFJZbFRUVGFtWXMwUUtUK1B1Z3I0NE1RMEp3cFJw\nY3VkcktNSXA3QVk0Z1NwLzJpZmxFUDlJMWl0MkZOREU4ajBEUXJZbEFxNlBTaXNzaW4raWxUbDBs\nakIydVFPSzBnOElyajN2OVpkV3cxcm03dnY5bm56Wk54ejdKc0VTMWdTUmFMZEg4VXJmYUpyQWpr\nNEN4MDdjazVtdzdrcmVnME45MkZNN3ROcllxUmdMbXlKalVxcE53aVJZNWRUR3JDWGJaaE5hdmFq\nMnNFQWVtYi9yM0ltK2RpMlVwd0xwcG1yUkc1Q2hhWXBqTGdMcjZZZExsYmQ1bmxTNnBHd2RxQjcy\nelRtUm52L29MdEZvQllkVjBSbE5RcWx0aW1NdVdZVWpDbHBUZmpyeitRb2Z3NUNQSE1VR3ZCZFA2\nZnZPVXJpMmFFZ21XNS94QURSS0NZaytYNkxKakdFY1E0Nll6ak04TXdFSHM4M2Y3RmhTMEZscC9r\nMVdTeWpDSU9pYWdNMU5IUVBVU1hRWVNScTBqVzFZZkROb1VYbms4US9YdG1vdis0bUtyekZLZXJp\naUxDcXZNckY1OFFlc2xtbEhDTUZ3eGdTc2xyUkltN0NMZjhubldoRmYzcmIvb0tXdzBqRzZaaVNJ\nREtVY3hHd25Qa3JlMFJEUFN0TkFBQ3lNcFZ5RnhqbUhxSHQ3SWZoc242Qm9Gdjg4bHo5cVFYU1pz\nVENjSlEvTmVwaVBNeVpwalBHZWlUbi9QRXdOMndsSDdZNWUwNkdQVUVRY3pWQUdNOC9wTWM2RnlF\nc2RYSHNINjhSOUZ4UEZjdXJBSnk3RGFRK0s5ZlZuR1hhaCtxZjhGb0JJcG5tTCtJc0hpNWxnblJi\nUkl1WStJTnUra1MzV3g4OUlVVlNBSzNxNjJwTE5ZeXlDTTR4SlNoK0NqT3UybWdnOUdFL2ZxRnBK\nMWgvQ0JMMWJ4KzIrNllhNDhMbzZIS2NBalZHdEp5T0VjaUwxZmhnaGFwb09DRG5QeHZVczdrdGZE\nc0tIdllUN2hxL3BodHZMZk5IeGFKMmVxYkp3TS9BWXF1TXdsdFU4NkovZEFOSHNtVUJ3TEZkaGRN\nclFkT3Q0WkRRdW9oWlRId1FRR2Vjci9uK2gxYzhXOU04dHdJd1BSMm04QzlIOEMwT1lUeWtXbEhU\ndjJ4bU1xWWVZTGx4VHlvZCsrWmRmK1oxdU9rOExFNVBsakQ3Ly9MenFQVklBZEh6bjgySjBIZTVs\nbjg2NlByaVlVYi9QcHFSWVBjR1J1RU9CYWcrU2JUaWlkL1huem1VUW5qMzNqcm5ETmU2UWRPL1lX\nUmxlcy9Ta2lXaWxpbjJ6dm5UQS9ES1A1cWo1SzNYWmM1S0RIdjlnWFhqN1hPakhXY3Rrb25nWXF1\nZEp2cEVuODE2YVFuQ2JRV2hFVXprUWpjWXRHN0F1RVI0QkxCbE9lMUVNcStUVWd0S1RWYWlsRnNU\nV3QzLzhYTTZSb1JiMVBWTkI0MlcvN2l0L0dmUjBpdnhERnd6L20wckY3bVBDblBaMkMvRVhxaXly\nbGpXV1M1UDh5cHJUUnBsUC90YjEzd3R3cFBPUktMY3l1ZnpoV3A5MVVxOUtsRW9YTVFlQ0ZUUkJz\nbkhOaElmYmJUbGlDMEhjOG1GbHdWUGNqSW9wTEZNVmtWUzBJaTRSTEQ0dE5Ecmk2ZEpzcjJUd292\nZHZhQjU0dUpQTjQ3aGtvQjB3YkNIazljOHk1NUlDKzJwNGFBeGVuY09WS3E0V2tHRjdDMDdCOEhX\nSXF6clVUbXlGWGFvQ2pXSTVrcHo4RzR0Y0xFTlZXRGtWeFZUdHlLRWRIaW9MNUQ0Y2ZldCtuTHZv\nbnMySXQ4MGM2b01JR256WWk5WXNZU3VMcjZlYzdOY1hYeDZrYkRRT1pLeFF3d0dOSEg3N3JyZnIz\nOU8yMFVJTjRIRXhqQlRyM2Vhd3VId1BrVmYwTHlpWTU0V0tvZVpHS2RSVEtheEJlOVArSVJQSDRS\nTnhlQ3dZRElPdThkWE54Rm5BZnlmR0RJRkp6Y3ZGUVl5MnRpN0pxVWxmaENqa2ZqTWRvMHdtOC9j\nc1RFTHo2WXZpV01xZWRRSktJM1dnNGh0QXppSWhUS2tia3plckJraUhOQWIrSXhMQlEwNmFFQlNY\ndG1iVDRxSlZobkVFeU1nbW5UcnZHTjN3dG5VUGhEN21vU3VERUhJVktBbFJKRWpPaHh5ekVNNDVB\nVEd4VXN4cDhhRUNiakVsdy9zeWR5QzB3SXBBWEpRS3hWZVJiaGxzK0JVUXFhbkk2RFBDOUFNbkVs\naGtsalBwWW5CUzdGVVVVNTJKZldRdFNLOFZUdnZxTlFjTVJSYzdVek13NWszTWpjYlVxa1ZINDRO\neTJPTlc1d05kZHVmTVRRMjcxaGR4dlc0OTQ3SlE3K3NpdnFaVXdPUElwT1BKeUxWakFoU2xwbmEv\na2pqNXkrMkRuNjRPbVhVQk5MZEdNZ1pibjBlRnBMQi9hQUxpMVhTV01wczhtN2hCRS9qM3MrUFJL\nTkg1bkMrVzNSQ2hKbzJFdlNod3d4ZHFKUklpY0t6RHpQRGhPaGFiQVZBTlJhUzQ3VSthL2VVY1VK\nNDlpckZrR21HaUNISXIvQU9DbkI3cGNwNEJyN0M3VzVCR3FsaHNMSmhvbm9kRkRPMjY3L3ljT1Bu\nRDd2SGlZKzJJWVl3MlMxV00rSjZsQnlpQ0dud1p3TlppTEhZT091bTA1ZVJHSi9CamUvZlZ2ZFoz\nTjEzenpFc1lXYW9tL0M0UTZod2lKRVliM29RM3M5NFV6QzArUlNBV0V2dm9Ra0RiUTFCbzVvY1pk\nbWRpOHF2WHpDR1FIbVlxb1FsY3ZrWHErcVVnVVhaL1gwMzFSUkp1T1RKeWN1R1FLOGJTSjA1Vmpi\nU2c3Mzhuek1DeGUwYkd3a0pJZVQyWGZqTXdTa0pqMVBjNk5salZZNVhXWFpyUExuQnU4SHhMbkYx\nYldUclFFbXVia3M5Vkt4WXVEUHEwa3N2cTBTQzdWSXAzK0dxRFNSWlRQQ093OEg0Z3VpV1RwempD\nclJsdE5hbzJWbU5xTGdHaVd3SFJTejIzTlBvRTQvVXl2a3c0NnVtaUt3MGN0NFdaeHlTMkpTZTly\nLy96Rnh4K3JRSEMrWDdQYVJvVTBTSmlGSVhiT0VnMjJBTkM4YmtrMnRveFNwWXg2OVhWdjBOQnBQ\nRm04Z0d2VDdSMGRscUZ4NlcvNzFKTmVkRG4yZ1VaZW5aUzhJNFp6L29id2hQWHZGRHowNEhzckFC\nN3UvbzBITExEbmRJaU85MzVlcnRsVUlySHFSc1FDVU9wTXl1eWM5bEZkckFXMVdpNkVpMnZLUUd0\nYUpJeklDWHpvUVF1aWJkTitoUDZ3eEo2R285N1NXSWt5YmlCT3F0YlA3ZkxPT1MwOXB2ZG5Ib2dZ\nUi91V01FVkpJUFUxeno5RjVhcnFRN3J2TE5TVXVvV2J1VEdNUHR2Rm1uYThXTjJ3SlBSVHdtRjg3\ncDFsQ0RaTXM1QjBPM0w0Sy96enJ6YTZyczlJZGZTM1NEeUZNYTlya0ZvdTZ2MGxPRTduOGVaWSts\nNi9RNXlsS2tHMGlNMkNVRnFKYXd1cG8zanJRanBqckh0Z0dGR0dHV3FwT09XakFuUUlFNk5yQUdr\neVVuTkdWZXA3VHBJWGpRbUV5cWVGcUZqMFhsOFNoVHlFajNVUHh6eVJrRHZZNzNablUxVEREVndZ\nanFsZW1OU1NYTlYrbGZNNWsrY1hXVHRuSGNhVkt5TUF0U0hTNkhtSWJFVEVoUmFUV3JlcnhKMkR5\nTmQ2bll4WXhhM0NNYVdvczRVMTB6Si9lWVJjelpBcmhwaDVQNytodDdrVDk3Z2pXMldLaXQ3YXlI\nNkRMOU5QUm1lYzVwTWFHa29xdGhwWEZxcXk3L3JYVEZiSGpnd3ZJRURLYWdtY1YyN2R2ZitkNGtJ\nWmNXMll3WEg4cmNNN25ud1JSOWJPc2lVTkpjc2hHR3BJRWc5cmNJZEFkTlUwazFxM0k1Ry93ejk3\ncUxmdEtLd21FN2RVWkppQTRSV3M4VWRJWEV5U2FHTUh6QU1kT1hEMk9STDNXVUNlRGNWbmZPSC84\nK0xzZDhTbFR4R1FoVCthRkpkWmE5U1BEL0tKRnllc2tYaDlDYmZxa0FjZjJLY3hyN0UrYXkzUFNB\nVEU2bTZBVUtGajdSZm1UUUw2Y3hCOVVWL00wVi9DcG0vUnF1dWR6dGRjc0JPNFVuVVZpSXFOd0s3\nQ0dLd2NoN2hycGwyekVKVFVzbVU5Ni9NYUVnajlwWmxGbk05REV0TFVXYjhqMnBwNDkvMDgwVDUz\nNUpHNy9pVU0zd0tpODJ5OEpmZ0hSeDY1ODVXSDQrUFhIL21oMHovZlB1S1pMMzZnQm8xMURlb0dr\ndUpINkFWbmt6L1ZGMWxWeEtmaExNNE9kQXNVK3FxelUzOE80UE5ITDF6SWJmbDFkNEcvMlFwSUN1\nMVR0SnVKQ3diSjdGdFNvYllhdnVsVHBqaXJkN1JRT2dWWG0xN3dKM0hLZ1QxdlI1NDQ2NTVBQmhi\ncHhteVNLek9KbGhZTkVpU3VYOFc5THlwSWxGWXpYeHZWbGZBSDk2VjRzT1BYZFdXbkJpWmhCSVVq\nMzdqelNlejh4TzMrN3dOM3BjRDcyNzRpSndjcFlvOXNYZmVSbmMvK0ZSOFl1Vkp3Y0o5L0lHbXFK\nTWdIbU51S0l4QjFqK2hGclVXRWtpc2FUWGVDejJJVTFmRXhSUEhXRnJWQ0E0aVZRclh3MVBhajFY\nNTR4dEpVbUpIQVF0dTF5UU1CbTdNRkp4TnVMQjJHN2xUelp5dzUyM2NsOVdNRFYzb1AxRXZNM2pI\nLzh6MXd1ejNRVnBESnhPTk9xRENudmIvRlNwS0N2VUx0M09ZbmNnYXl3a0t3cWNXa1pvZjQxSXJD\nRlY5NFk1OTlsOTFVVGd5K1p0Tk5xMTRtb0kwK0dreElWcDE4ZFUzTS9PZ3djeVVoZW5aQjV4T1o5\nL2tLSTRsZTVEbFpwQzFia2tUV0s2Qk5DVU1uVVpJSUZxM0Zma2hRT0xYT0ZDY0svUVh6T0pxb3gw\nZ2d1SVU1K2pCbFBXdEVxUExNenp5YWJQbnk5THBDVzI3ZXY5RUovV1N2ODdCcTZKUStkK1NodTNU\ndnZpZ2lrZTh1SkNhWFNKNXFXSEh6UkJOazBoaVVhSktUekpsaGxEOEt5VkRUeSt1djFuRlVrMlV3\ndExKRndnaWhjUElLemNHZXRhZEFucXhOSjAzd0h1dVZXVXRrZmtJdlRtaDlLQlhWekdYM3Zlckdh\neGtuQ1cwM3hlTGR2VUlUMUNwd2Rsd1I4eGZOTUFBOTRXeFNJZVkyYUVTOXM5eGdVMjlySXQ4cE9I\ndU9PRnFWaThzT2RMNDF4N1lsRjVhL1dKM0x6dGZja3RScFc2NDFUeEhXZGd5U3JnRXJqaVIzUEls\nUU9Mc1N0bWo3eW9jbU51Tk43RUltYWZ3SFhxME0vb2NPWnJYV0cvSmw1dnQ0cVFNTUE2Q2pXOVk5\nUjhCWENKeTdlN3AvaC9DeHh1a3hRRHI1NkMrL0tNSmZVQkhaV2pteUhyTDJ4eStLRGg1OFVzOHhK\neEJXczQ2OTFvUXArZ3VkSXptR21OY2p5dG1WSk9ESk1xS3hZY0FrZlpYb0lPdDdOZnFzZ09rZmlv\nZHNManA2NEhaYmRPNWRRdWExSWppcDVyaUEvdEE1ZTdXMWZIVk01a2NIUFdXdEpPOER1MnNGOGx3\nMjMxK0YrV3BYczZVZlBQVGdlNm9YMzF3RDQzTnhGMFJORjcrRkZGVjV6MDRTR09jRmtHektxbWNH\nSW9mby9BaTRxdGIzVkYrNDB6U1NjU05JaU5xZFNPcEVNeDdidXhqcG1jYytjT0hhbXo5MWVNSXJp\ncjdQNmZqUnh6N1E3a01aR0oxNjhNN3gyMjY3ZitxUm95ZTFnWmszRm82MXpIZm54VThpMURmY0l5\nZGhRaEVoS2VRa2pJZVYyaGNoc3JsMWhDQSt1d0krNFpPb0w0WmhLK01nS1BLdGpSVFFGcklJTHFx\nNHdqelNGUHRJdmlkWmdKU1Qvemwydk43L3VGRzJZWkRFZ2pNWHdURGVRdEtDUDluTjgxNWVnU21l\nZ2REbVZyOE9lWVlKb1dmcGIwdGkzOTVXRTdjN2ZkcXhxZVlTelE4SmgzeXdmaW1BSnRWcEYxdEk1\nTTNkN0l5b2dOTUxnR3hzWVJqSGlNNHU4MXNUVUs4YTFSdVo0b1ZKRWhycjVEa2xKeUUvYVlrV2hF\nVGdNMC9uSm1HRWZBRWgwYnE4eld6SGNSaW5XTmgxRFhOU09hc1dJN293N0hGRkpPakxTanIwNEQ1\nTnFUemZTY0k2VU1kTWd5V2FIM0lrejgvRnY5VFlrclMzZ0s4SjR3SHlmbWM2ajByQlFYQkYwNlFX\nbUtrU3pLUW01YW1CckZXak9qZkU3a0lhcURnOWZVdHlZSU1saGxsQWlxeDdWbHphTjlhbktXRTBQ\nYlpleURsSWdMTndUalhRbFMwTU16WUVyLy81WUtjczM3eHJlUVlBN3BFRUoxb1hTVDRQeHlheUlB\neGpDK1Vtb2szeXZwV1pxVm9lMFlzckxVSExiblA0MU56Yys2eVI2bXpqOHZUTVgvcEllZDRFbVpW\ncThhckdHbWVEbGlhMjlMeHVTNkdNQjdXOFJEb25JaW8xTkg4dGhOakFMb1dhQTZjUjJTRUlheUhE\nOENVU1JCZEdRTmJVbVd1WW8zS3BQeWVRSEp0MlJGeUZUUzBrNXcrS0NFNHpGVTJjdmxFdmdJL0Fr\nb2l0amEwR0tBcHRYZHlXTFRkLzdNM2l0S2V5VndRWk5qbmowdkl6cHBEYzRMRXJQbktiZ3NkSGx3\na1UrcUcvMjIxc0h5ZVFjK3lxM3lVcDdoUnRJSmFSQWUwV2tYWHF0UlhJcHZaeHhybFJLcDQrNkNw\ncmIxQjhjMzArdXNXSFRJYjhEUkdzM2J6N25oK29OMm5YY1F3M1ZqenBucWhkUVRkWW9WaHpxQXlm\nSEhaT1N1RzN5Wlg1dWZ3NHpVaE5hZXJZbzZlK29hVldOdS82MkIrS3VEdEZlODgxdnBSR1lGUHRn\nV0gwd1d1V1pvSGdGQkF0Qjd1bUJOSFc4Nk1qelR3UlF0bWxwTERPY3ozZlI4MXhham5ncjhGNUNB\nWnJKVGxLVE1GZVE4RG5sVnVhVDZ1ZnNPeDhnMUo1SndtOWxiUjlpOGUwRzNKa3Zsd3Mybjl0UlQ1\nSHJIMTZkSnpSN3hKSS9EaUEzd0tSTjdXTXMvYnJISlhmSjliOUNZR0dRWnFVNTcwMjkyclF4VmxO\nYktDM1E3Q25NVTdMQk1COWt5b3JmMVpZL3BDSnRNSzZudy9PNndZbFoydDYyVzhDUkh0c2VtSXdp\nZEEvVEY2Wi9LUkppNy9Qekd2VTgrcTBIcDdlRTZkajZCOURvR3RzWEJJVy9YMzJ1U3QzYnJ6eCtB\nRzFWcE45dG1idUpXN0dmWnpUYzBkbnRFRXFqcHpzeGpBVUpFejk1Q0dPZEJMazFtUXBzT0c0RUtK\nUnRaQjhDeEk5VW81WVlaMTkzRWVXdzV5TGtmZ2lpV0pQSG4za3dnVU1tTVNtaGlJemtxRzlHalBX\nZVljODlDMVhKTkVqTzJoSXJKYzFJMW85b05NNCtKVEhISlRWODZNZGNxblRlTjR5VWtuVUhGZHU3\nTUFkeGdrd0xPTGhqRHJmVUpmNVRFdEI3QUJ5R2hZWDZaMFlJVC9PZFZwaksrelUvejVmSzlsVGxo\nUGUyVnE2NW43VGc0UnBPZnVMZ0wxQ2hWK0RMTHZvUWxtTEN3VUFOeWkyaVBvcWw4cldIUkdUNnY2\nbnVNRjZLWTNEUUFEM0RKUjh2VHgvQmJzaytyU2wxQ2thc0s0dmVIMURwVVJ2NDFEWFU3STlwT1c3\nM2NhaGJUNDlUN2NBYTh0eG4wcWJ6VWRkeG5WS0YvUUhMaXIwbm5HRHp4aG9uK0FVTEs5dmF6MThn\nYWVpWjBPb1FDOFNreFhxcnlEelZIeGNWRDlxbU5iZUtydTRrbVJMdEdDVW9ldlFHa2Z5MG8zUEFO\nSmtHR1VTZHFlcFVuNnFIbHZ5a3BMN1k1akRUL3pDZVJJODc5VUtUK28xRksyQUVQNVNQZE5MWUYv\nL09iUGltc2Z5cndaNVNHcnJaMW9DN1NLdXl4TEJTNitvL1ZwbWJ5UlVuYXBUeUVFL0R3Vm81MkVO\nTENlaVNueWttWEpLSU51ZnQ5ZERrbkRQRXdUZTdXZDJxU09ESitxZmNrVGp6cVlIU01pdzN4YjFt\nQnV6emgxb2lsM1YrVkJrWUlmZmQwUjArendrV2JkNlRXMGxvbStMVTZqRVlxcjhkUm5SanR0RWp0\nejN1TE0xVlVFT3RqQ01jTVl3OVd3Qkt3Nkd4K0NvNmJRTGxhaU9zVzRwb1daM0lPMS8xQ2VSYUI2\nMC9MeFh3cXc5WHBTVmpTM3B5TWFWMzluMjFMRzN5akpESTZOWGVNakRvZmpVUDJ3N3Y5SVg1Vk15\nMFpCTWNMSTVObmlZbzhJeTJNb0RjYTN3UVp0T0JyTnptYUZrS3FwR1JiY2pxQWxMMURmdEl6ZDU4\nNGZ2R09abFVkVlFRNXBFbmlIVWkrRDdPemFnRFZXZ05nVm5jbDVlLzcramxNWW5XLzFQL1FVZ1Ba\nbjRxK0tTU1RMRklTZnVvV2NlL3VkTkMrbUIyKzBoTmJQejlPQyt0UDNZbHRmdkh4WnZKSGpMb1BM\nc2dUdW13U08yM0x5Lzc2VXRVWlBPUFBTdng4NmdsVUlCTVhhQlliSVVGUjlScmxFQ29wVjVUWmpP\ncnJaa3FkM24wcmVFT2ZMUXp5dlErY0dnaDlCL3d4ekkrbnA0alpVdFNaRUZvdUJ4TkE1TzY5cWg0\nUjBlUjBIRmptZ21aQ0FobEo3ZHVBYU9SbHVLQnpmNkhQVkRKT1Q0TjF3eTlYOGNyVVZkcTI4djBl\nSWpMOVFWQzZNdkgzajBQaTRaUTZLT0gxbldCRlFSaWlkWHIzS2dNZkU1YklHSTBSY1F2RTZISC8z\nRkE1cWhNNmdmc2tRTEttRnNhRG5jOUl1TWFwZ3UzejFORVhieHVlRlZITkdrYXFyMStJRXNVR09z\nSlZvY3hENVNyZEtsRWFuMi96OFBGdzJoanIwbEFTVUdabUo0aFZDcWdha1FuUEllUml6YnFkMWls\nK2dsSkdFVWJXZGFzREJuRWFjalBsc2dLNUZQMVJoY2laZTdvcHBZTk9tTEFBV2JkV1M4ZUg1UlZx\nMWVvc0ZUc0pJVW1wbXYvV2MxZW15VzU0MFByaFJBdFhqWUN4ZHBwb1JvOEd5VXIxaGltSmNJZVQr\nTWRqRHhHRjJOdFlXdVpRbzFXTldNc2lyU3JnQzJOT1FpeDRTQXkxVi9EQUhsWWxMVENPaGc4U3dE\nSUswMUUzYlZMUFkxRzRYb2NSWXVFWTE3OUR3T0dzYndEbkF4V1NabnovTmxMVTk4cVkyZXg3blFw\nMHQ4M0tSSGIzYjQza1c1dm9PblZ4bEdjVHROYS9sOEs4TUFyTEJNUjJVdXBnV1g4Z1dmc3gvaXBV\nVkw2VHczK0p3YkdWQnF4WTcyekRBS0p5R01hYnNjQ0o4VnNWSFA0MWpHeUJqbnJEc25Za3U5bGMz\neGNQZ0xiRmhyZjU5WFBFYlA2Y0NnQ3h5UlE0M09pMWpsb0o3R0FUUnE0bFZ6cnRFWitXcUUzc3Vi\nUDZjSGFtOXJIdEJzeDVKaWdtSWtLSlBpZlJ2ZnBjak5lMGZZdVZGOENnZmRPcmV6NXdIQ29JZ25o\nODY4Y0daODlmb2J0UzFscitORWFwVjFVeU1uVHcxRnU4Vk85ZmdVTTV4ejFXdktyem54M05RVGI1\nYkk0Mmw2b0FKc0tyV1hGOCtlZU41dCtNZmFvNkhuY2FhV0hQLzZiWXJtbWhPRjRHT2VZVUxWd3RF\nV2x6OEJacktvZUNLeWJJWUo2dTBOVDYyUER0dnFuSHd4ODAzUFBQT0JLcDVCMzlVek0rcTc3TWJS\nOE05ei9ZNDdOc2R4TDRSL251OTNIUERMbUN0eEkyT2dydlFHdE42NDkrRG12THgrUzlLS1ZoNy9J\nczJ5V3I3U2xWbVVETE5FZzZmQU1Ia0o0ekhPM214ZWtXY1lNeFdndlk1RTQwczUvSzAzeFJlOHQw\nK1NRK1puamJDWGFBRW8yNUp5MEFZbkRoRk53Ym1tQjlleU42czlid2l0SlBYVHRGQi9PZFp6cGMy\nN2ZtYzFVZldQQVZxcDhYVVNESXVyYWlYSTkyN2V0WCtuVFFvL2ZmekFIVXNabFBOSVhzbHE1RlI3\na2hxUUt1eGNFZXpCYWVjTXVCb0hoaUczeGs3TEVwZ0R4R0VPRk10RURNRWJ5TVN2WlRJN2ZGWEty\nRGdSUitXM21EaDVPNzdQYU9jY3ZlamF3M3FldHFRNkZrYkp1M2xyd2ZXTGtjYVdsQmgxMmpVUzhO\nbVhpbWl4ekJaRXdoQVgxTFZjRTZmV1o3NitqL3FRZkxtSk4rSDdpTGJ1dnZmbWswWDN1VTAzZm5K\nelgrTnV1bS9uK0lvTm45dDZ5MzNYREhwTm1tWVJQTDJvYjBtb0lFb2RMSVh5WlZwQUtJbjhTNHNP\nc2JBYThSZW9ZZmY3Ym1welVubzM3L3BvbWJqMFprWWhTcEI4NzRXSGZ2RzdjLzhwV2xpUlhvbnZH\neEp5dU9mZm1HaloyMFV1dkEvQUIzc2Q2ZGo5ZWhRdi82RTBHZFZDTXIvYXk1Z3RiOXgvQThlbGRW\nYXE0MGNmUHZVMVgzU29BN0V5Z2NmQ05McjB5aVNzSmlOUnN5bDVMUWI1V3I4K25VRWx6TGlJMXBG\ndk9NVG14REFwclZnSGNaOUhGUDhGT2Z1LzRtTElPN3hrODdZOW4vNitDRk5zdk9HK3pRRHRFVHVs\ndiszSGQreTR2NmN0NXByZDk2MGo0SzNPVHFsejc1MmEvZG5MT0RIMG14UVYvZ0tDeit6WWNYMVhB\nTDNheVNGYTNhUXBKSW54YlhBekp1SWN3d2pSQ29sY3BkR0pMRFM0V3o2WFluM2syOTJnS2s3VGp5\nK3VkbHVvblVlcnAwejZmUUczNE1qZHdCUXREM1VBNmVVVHkwNjlySmR4TlhGdklESnJRcVZTdXJw\nUXFGemI0NVExdlE4TkpFSzNkWGs4cjJlWWVxU2FKbERTakRrTndtUktyNVluYzRGaFNHU0ZTelhy\ndjE1SnlrZXNsMjNiODVuK2t2SUhUVm8zRURKU251cXZqTnJpSmJvcHhLZ0ViT0tDWlhsZGIrUGtS\nbDlKWFpQeVRCUlpvVGNNY2xYczhid0tubXJnZVdVQ0tldk5iNGdscldkSExzQVpBQ3pUOVd1NVZ4\nL3BEaUFxVGYrOHhGdUJ6d1lzSUYwWUUzKytpVWhlMnd6dStaaFRUd3hEUksvTHA5dUd2d2RIWHNJ\nMDBYYit1aytBcVFpdWw4dVY0SU5wMHJDNFJELzBESlBSa0V2R2U5b3I1NVBVeXJhbXowek1SVWpi\nMy9HRklvU3VhUVlpL1dNNXUwSy9aNjgrNU50Yng5RjE4eUJoY2tuNG9ERTRHV3BVemxRZFJyY2tW\nVkdDejZOczRTSUJoWTdmSVhXNVpKTmNVdnVsSWcxVG9MOVd3NHVScHM0K3ZWWUlHeG8xamJXMHZ1\nRHFqQ0c2MHZyYWV2V0hYZGxJQS9JTjJyRnRrSWFBWnhndlllbzZLMnNjeVEwM1VCTWFSOHE4dk5t\nQkVuR2htRzhMUXlTRmlOMGlpRmg3ak00aVdNZkZFWm5vU3RVTDY1Q0ZUS0ZmLzRyeGpUTmFvN0hZ\nOVJCWlZaY3dJYjlmMXJuRURzeXh5cjdjYXI3YmlhTHBXTXRINUw1VTB5M0ptNjJLTWpHUWRJaFFy\nL09xVXNlUU5kRWllYko5dlpyTG5UWVJhUWV6bkVKUGJtVTFtcHk1M1I1aEl6aFNqVGNiNTdXWUVV\nYkY5NlFhQkxHWEx2WEtYZUgrajRkYUpmWEZRcWphckVpazZDNU9XWi9pUmp6SjkyVnlicEZFck9u\neTk4T0liRzd0Zkt3S2ZSU25pTmJQUEk0M3R4UXAwSEZzakhYUmhrRXRqVlYvYVpFd1lJVTJOTVU2\nU1VxV1F3SysvOXVudXE5d2VZaURod2J6b21BWVlwbVhHTXFDRXRPbTlrTlpwWXdyWng3b3BvM3pK\namJWbTVrTllHbmVwRzVwL3E3V1Q5YnBOZkJENHN1TU5RUWtlWWdEdDBBY0ZpNEFPUnM1dTBoTGlm\nZERZanN3aGxaTXk1VmY2VVNFanBLRXRJWDBRSFVZbi81WVQ4UjNXcTA3Yi9Fa3lFc1lKYWN0aWFm\nVnRWc1UvZzlXTVBWbFRnUmExd2tUTEtBTmN4blhqWkhtTG1IcVNXeGhyaWxmVDYzdXlDT3BrVFZI\nOHd0aDhHb0xQdGVTcUQrbkhPdTVrRmFhekJjUDh0dGgvZ3VYZTJJK1FhaGg2YlI5TUZ1UGFlMHYz\nbmJJeC8rbWR5MmJJMFVTdFFVbGhhWWd1UW93d2pWMjFOSnEyRU1jTEVaUjk5OTRtbjhQNjFUTmpF\nY0Z1MWRzYmNqWEpRcU02a2pvRmpIUnJmZytvQjA3OXNZWFNGWk03NVVXWW1YZFIrN1ZJTS9LRnUy\naVFUT042NDhpYnlYVnR5VGxuY2hVNEZ3bVliekdYcVVrT3RHc0NhT3hJMTVsbzNRc0QzR0FoMjdP\nTDJsdFdRQjN0eC9mdXZ1ZUF3UjhYekJNYldSMWlVRExtbzNJNnVSdDVLN1hlUE91NjR1UWs4dGE5\nZEhHdUlGNXY5bERHeG9tdEU2bUJXenpOYWFvaXFxY2dpL1pVSWN6dUZWa2FVSnpKQnJIWkc0UWgw\nRlFTamdqenZwT28vMGcyUnFvdEQxN28rQU5EWXJjbHB2Mi8rcldHeHJnSTlyK2pydUwrdm5PTnZT\nYjRubTI3TnIvYnpmdittakxFNnpmOTNWdXMvSGI5dXd0WmQ3V1dSZG9TY3BBUzQydlFJRVBsbXR6\nekU3ak9EcGRJcExoYVl6bWc3STBzUHgzUmg3YUVJUjhEWXh5cm8xZkphcVZ6Z29oMUdYMXdvaFd4\nSkd0Z0tTWmxBOVpOcHZyZXY0b21STEs0Qlk5MHNtNDl1L0dscS85WFgyL0pibGlyNjJOUDczMWxv\nK3YzSFRUeDE5T0p2Nm9pOTIvME0rMjNuTGZ5c29vSDNCcDdkQ0xjZTNoYlh2K1UvUEJvTUlQY0R6\nMG00VFNPL05NVkRuUEI3WWNPZmx6K3ZmVk4vM1dPbGU5NG5GbmswTmJkdTMveUd6cmNpaVdJY2pW\nK2EyVEJua3h2UDNsSCt2b05oQm55eUxkZkZBeWZEUzVVQmlZbGVURldLaHRKN0EyYVpiNXlLcFJW\nVWZVSXRMT0puVTR3M0lMRG4wRHM2ZGFnR1Zyc2ZhU09NME1XSHN2OWxWL1ZvRGxRc0VWSUk2djAy\nTE1oNy8yNGloVCtoWXlCVlV3MytwUmIrbVVhdjdyQ2JLT1RXR25xL0tibTJlaGQ0U204UExEamJV\nVXVVaUViVUx3Q3FvdE9CYWk5YVRsNDRuZWUvVk52eldqYWV5aXFXSHR3VHBOVUhqbm5ReVpkY05k\nYm54QkV3eUw3Y3B5Sm5ISzhkREs0dUFZcG5uNnJGQ00xdFJ2Q05DcDBsTWpZNzdyYXoxdUtoZ2hq\nclZrOGtUengyQjRGZUpMNkdYdE0vdVRGTEJCUWJ5U1hBbTRFd3BMRk1KdUVWOHIrUlViYnZuWUZZ\nVWswZTlZUFlhUWVINWpiczRiRkhRa3dPdDIzQllRY2FaVzFNQ2JZYmljNFNCV01jaEVablZDOVBx\nWmYwWmMxbktudVlYbTN4Ykh5bE5kSkV4TkliVzViU2UvYzBtQjQxd0xnSXNnaHNrQjNRaXBSckFn\nR2JZbGJFbVRyei83dnloalREUWJZOGx3S0pOZWI1YmxkWmpTYUdYeTBrZXMrNktzV0pMV0l4YjJp\nWVNrY0FCL2MybGxaS09yeGtaR1d2WnNBVHhjWVBXTmR5OG40T3JRTDF3Mm5UOXh5a3VPU2lMNmxC\nZWM1RXE5MTBuZEFHSm13YWVZY21nMjc2LzFHZWZjdm5yMWJuRW9taW5kcmpvUWNRbWtHQ1p2WDQy\nS3lJY0VJWGRMMjR5aldoM0l3OHcyYjFZTFVxUythVkp6VVlMSkI4S1RPTmFvWlU5VVltY0xFTG5R\nck1wT3BVS2s1VUF1SHhLQlUyVlVRRmM0d1pFTU43dkpTd1BXQmlHNHBsaXROaGxHdkNUZG9tL0xK\nT3RGc0NaSURoNkpyUXZJZm5KbE1Cdks5d2JJRThtT21kZGtoMEloQjE5UStmSGFHUDAvbWhYcmp4\nRmlTb3RkSklXVVBiekRsL3FYYjlzay9naUVEdnRlRGtReG1XN2o1aEo4OUQvRWMzU0tLTldyVW1n\nQmhZZTNGM0k2VEFIYStKdm9YUDBZbUNMV0lvcVhFNUdtN1oxYnBUb1pNUTVQckQycE9zM3F1djdt\nNEs0eXhkV052VTQ4WElEVzNYYmIvWVpOWVFPejhjM1BTY3NvT1BLTVJFVXUrUUNnZElxYWE3OHl1\nbXJHSlJIcGRjMVFkdlRrcVlOM2prUGsyVkFhaENJeWxXSzNjVUhhSzB4YnZxMHVDQUtleVRCQ2hy\nZzZLQjBtSjNFYmxvWTA5MEpIUVUveGRlL3Ezek1rbXBUdjg1UHFReG5XWFc1b045SXlLMnVJWXkz\nd2NTUzE2bHJQTEVUL01XMngxYk10Wml3QnkvLzJwQW9ZYlBDQnZmcFJEdDEzS1dWTlF0ZHd5M1FK\nRXlUVSt1M2J2OUQ5NWxubngzdHlqUVQ5UTJHMVlyUTMwbXpqaU5nWEVpQ2llcUsrU1cyWHJheFBZ\nb2xhdkxVSlVpMTZsMU9lRkJRZTNtUVZHekk0ZzVjbXJVbjVDK0c4R3lTUlR3S08xb2VDQXU0b3Uz\nU0Rkc1NwWTMrWXNLRmFMSnEycmlWRFE1alFMbU1iV2hSTEZ5TEpZdEtoTEZUaEpReFZDamtKNWMr\nN2VuekQwOTBsTVpuc3hpcUt3SG05U3NESFFwaUdtQ1BUVWVrbHBrSmQyanVRTHdqaHRKbFpHQWRH\nUENBL2pMZU9HOXVQZGdyVlh4dmx1ckQ1TGFrMTJLaVJVNFU0NUZzSGU4RHhvZ2hBOWs0K2YzS2ph\ncE11ZFNkSXNENUFOUnFNc0tac3gzeWJIci9Oa0U4VUxacks2REp4SE9JNlRkU2hCeWtaSjFvT1JS\nK29saTJwamxOUkMzTTROVjBsc2JEejhFYTF5cHdZbnlkTzRrNWxlcUwyeStwNDQ1M1VZUjJpQlRp\neWNlcHdEZHVyOWVjZHRGa3RXdjFicmMwY0NrZTBjNWVubHVpMFJicWE0Vm9oRG01eFJLeDdKM1ZB\nOFVaeGljUm0rSlFEcmN1YXQvM2Z6aWI2ZEs4eFNkbkREWjFMbnhOblh3QXpWN2d3QW5acm9NbDhZ\ndis5YzdXYUFGbUFMK2d1a2s4RUpCTG43TE1RTjBITWhVUzRLOE9RemJZY1ZhYWxPdWJmc2w3NzRD\ndHpxZXZvSENYZklUNHdHa1BiUit2ZERRRmlaV0MybmNmTkNVRFZKRTNFOXlYWnc4bTlCTTBrekxS\nRzVENmdkVW1TOGdkSXhPSzJDREJtemt5ZVorSzF6bGFTdEJaL2hFbStMdUxXQ0VjbDlkK1JjM2VR\neUh0MEVNTXRFOEVWenFVbjB0cVpEd055RUNEUE1FRjM4ZXBuR1h2M3NyaWF2NHNzNmJzaDlCK1pD\nd3l1ZGQyNmhVUTdxU2tXTnlYTzlFYzQ5WU5sV3JydEtHRUVmaTlWUmhPeTdNYzVSVTgyRkhpSkJt\nd2wrVmNOV2pZcnVDK3o0MXJJT2NmbGpZRzBPdVZMazVRL0tOSjJPUUxaREpIVFdxMHFtTW55Z3BZ\nTWNaQW5mRXM5VXFzSHdvWk94Y3NLajRtNENXVVlGbHBGb084ZVA3QnZra0FINjdFMHF2dGZDS1Z0\nZjR1Q0x5QVFHc1NjRk5qUHE3ZVR0RUpwRnlMRlRBZEtJVkVvTFdZOWdzQ3pvZUVXREdhRE9HQTk5\nR3ZxSk16RzJTa2ZORll6cWN1NHVXVU5OSzRnSmJCZXVtU05yVHptMjNlTU5lSnl6SkZWY1NBWmJS\nYmo4LzZaeTRoaFNJaEUzZmdiaUVKZkp0R2lBaFI2SUxMd3M3NDVjNXI2QW9kcW5hdzZwOXV6WEJE\naFlhZXhzM3FaTVcvMkJxdklFUTluRmRKTDQ4bFF6RndNMmdlanlFbDZSR3d0ZFROMHNSTktRODhu\nSW1za2VGV1pxTkV1VDdMT3N0UEdhV0hFTU5DNlFuRFljY3lOdm94K3B4cVlEcE0xeS9KYmtub0w2\nemxKZXR5bUlTVGc2THoybDI0U3JhSXFUNFN5R3pUd01QcThrKzhGU1dVQnJaTjZ1VGh5K3VUNzk5\nWTVqd0Vpam90ZTF4RkxCdzdjb1ZVU0p3QXVFMUhaWmN6bC94VXE2QlpFMGpDbmk0VllMWjVnWklx\nTHVURDZuRzdyNTRobnlwMEtYbDRSY1lrTkY5d0pwNDBvdEtuZm5MYWZFengyWHMweEdQS001dU1S\nMlpZa0hMcmNYaXh4UzhsNEg1SG1aa1hHWUVaNmhuSGl4c1J6VFBEMk1zbEtVZ3RLc3RKaElRMWI2\nOTlkRm9nM3ZiQWlXRTdpNGFaWlBVTU1DZUI3NzByRWVuTWR5SmRRRmE5VHdyK3JBcWtXS2loNjYw\nWEp5V25OVU4vKzZPcFlyU0NmMUU0YVQ0cExrOW1XaE1qU004L3Nyd3Jodk9RNzJiWlRYWUpvcjJM\nbEUvKysyU1o0cGlia1RRbzdFcVhOY1lPaUpzT0V4U1p3b1daTStOdHp0SWN3bUVJNlJsVFA3UGZo\neHVXT2pYWml6MHA0K3FEa3N1M2JPNGZmRngwRnhKNHE2U05NNUJtR1JOc0NCdVdlSGNZRmxKTFQy\nRkJ1R0pFVDMrSVhCaVo4MTdBdlEwdm5MdmljNGhFbnFYZHlValV0a1VteTBRMWRkVlJjOE5ITXND\nNi85MmliNGZDK3lTU2hFWHFQTkJqWFN3dXhhNWxmYW1DSkczNElYWHZpTzN1amtuak4yME1jZk1R\nYXN0ekVxcEtqMFhkQTkzRjNWV2xPUVM3TlhzRUNrZ2hiVWdnQ0c0WEJaNVZQU2NWQjFoMnVxcmlH\nVk0zZ1lINW5nbFMwS0M5WUZXYXk3TTFlSjdIbWNra3hHU29RWkJsNUthVVhyMUNtcVZMSVVCZnRQ\nK241WVl5MGxNb01LOHZDTHhSci9WM1BrTEZwWEo2Y3RNa1RxYndNbzlseWFEN0dhb0xYd3psWjIr\nTFpTT2V0YlQxT015ZmpONzZkU1pqRzJpRXdJWWx0bFJsUmE2blJZd0RhL1QxOFo3d3BZV2c0UFRj\neHA4eEQ4YUNoQlNUdE04ckZJWDg1bmRReHk0WW85Rkd3eFpHcVNoZ0hOV05iN2xFaGpOZVFzbGI3\nMFJSVlYxRmZTd3lLL1haRFVFZWJOcW9mOGpIYlZ0SUhyS3NVcHJvVlFtUXN4ZjVlV0FuT1BIOVlN\nVXNkQjJaNElBM2FaT0VENS8rdGh4bDYyNTYwZ0YxbDJaVTh5NVpVajZiN3h5ak81VkZicEtGQnBE\nbC9SQmxuM0hPNk53MHhsRlp0UktSUFREMWlMU1VYRitZWXNiNEVmWmU4R1dvVGRuU3Fua1l1b2hZ\nSkVGdHJDYjRtZTRnVmFOUDBQWHNqVlhhSnRmaVJPbWVDRmVMQ2RaT2FTd3NRR2hhaDA4cE5Hb0Nr\nekVwcXpvbXE2anZkbHFSTUd2NlZpR3l0SGlaUXlJTi9maTNuZzMvNWNVSEJKVzJhbHFyZTVabW5Y\nTDgzcmlWbzJHMXV2OVFoYy9KWTE0ZVg2eGlpTUVJU3Z5VTF6MkFodm5nUURoN2NweGRsTE9jMkw3\nSlJxVUJhWmo2c2o2akFtRVBFT21qeVc5WEt5TXBFa0tMZ2U4SEFYZ3o1Qmh1Q2lpUHRSK0FYb241\nZS80QVVhb25lQUNjaFZBSTI1TGJhOVZwWmRFVlFmRDNnd04vY3hHbXJBSkc0WE5BSGFKaEVUb3Nn\nWlU1SDJLZ1RPUDlUS1lGMDk0bVFsbzRLUHBkSW9wRGp6a1pOK0hBcDZuTjJIT2ZmR0JJVHZNMGNx\nYlFMV3hLYkhpcDgrZUFvclVpU29tSjdjdmVoYWNoRWJjWldBcGRIZThHaXpFbXVCVU11WWsyUktt\nL2t1NzNXOTBsbUo5NC8wUitKdGtiR0c3ZDhhZTFuc2Z1ZVVFcUNyaVRDL2o4Ni9OQmRmOVQzK1hx\nZE5qeFJSWWxjdHIwU1dRbWkyMFREQXEzTXBnb25FVnlxVmc5MktQWkY0Q2E5S09Dd1BTZ3orVjlS\ndFpHSlJCdVRuU0VnRWZBd203SkkybndveVR1dU9wdkcvblBqR2pmZVNUQy9uWmdWaHVyV2FmWjUr\nMjh4bktnTTB0QkdtcUVHbkpPVmFvVjdFMFViWC9Sd1JiU2NDenQ3NytaZCsxOGcybThnNjBodzM2\nR2pqK3o5M3hXUkdQbTg2bWJCSW1XT1lDVUZ6dFFJV0dNaUVSbXRJK3pVc1dqWWprZytLT2tCUEdu\nZkVldWdNTk15NHVpbm02ZlNCZ3cxRGRQUEc4UDRlWWdMa2JaYkJyN3JMWlNzV2ExTko4aDdHTmly\na3hwTi9CTVI1NlV2aVZOZlRBTm5vRjU4Tlp3aTBybzVyS2ovczluV05rS2VZY1piWnZUMlpCY1NS\nelhkL2ZUR0cyZlhoUGxrYmIwOFhMYjlUU01XVmg5YThCV0xKclQ1aXBkWGhLYjBHdmx1T3ZGbUpM\nMEVITCtsdVdzWU9GdjVMbTY3L29ONHdETkhDK0l1VWY5Z2JuaUtOTWN3b0xOTmJaMWh5YTFncXdI\nSVhKK2N2c0lEcWpQVzhSWDZNT2V2QlYxMG9jUlpLWUNmNEt4cmxNUElkQllrWmNlb0diWUVSWEVy\na20yamIzY29hVTJrTU1hY2FvOGMvOTJJMmFoY3NoUkZEQ2s2b1hNRXFhakZGTnB0NSswSTMzeTFx\nOFdpMjExMnF6S3NzWCszTVJoUFlwM3JmT1BGSnJWY0ZtaVdmQytic25FYVBaMk5ZWEsrbnF3bHRa\nL2NMN1ZSdlVQcmRMUmllaWtYMVNTeUtEWVpobHVDalFxaHRxdGFnNUlFMTBmRW1wTWhCVjBQM0xu\nVUgzbW9oczg5SmlIcmJJQUpKSk9SOGFhelpMVlFzdUxSQktvYTBtZ3c2ZWJnSHk2TEtHT2NWQ3VU\nRitGd0JxQXBJWjd1b0JOWHBKbDZJekJYY21HQXEvMi93TGI2amhteDdjd3dKamZPWTQyYjQzUjNN\nck5KbUxxVk5RczErL01FY2FZUStGWWRob2J5bU5iVzZEU1pWUkRiY296N1NKbmxxS3FZeFN3Wjdo\nSVNTWGdpRlRaQ3dhbW1Kcklxbmd6VkdUS2xqMExhamJBTHVseWs2RHIxcUhwdk1DbmpxRXVZMlZj\nSTFES1MweG1HVVJZZkcrcTZHQjlvRExWZGNOMzI3WGNYUVhLTmR6cERVakZSNTdIQ3FuQ0ZjY0Mx\nMlBtSm1MVGVuWWVGaW9XbEdjdXA2cmw3dVZUc1k5T05TVlhDWkdIeWNJbFNqRFkxTmpzTjRxQndC\najBtYzRJNDFNUm9QdEg4Ymp1OUVBVUpvNUFDb2RBc1RNaVZSZmRMNnpMZElBTXRpRnhJcTRuMmsx\nTFYxVE9FUkdxVmtJaE5mWVVBSWZ3bVVYUzkrTksxYlZPQlJ1b3BPeDFKRW4valF4aElYbHU5d3J3\nSFFwdDk2Z3VRdXJUYmplY3BsWUErdGtkMC9kWkM3YjBBWGFYanZBSStDOE5BZ2tkL052S0ZuWnQv\ncVVrWEZMdnc2OFFpbW1xSUt0TUdjVkRtWU9LbTVlUURjYjJYa1M4YUpQMW1MTTRIU1ZZL2hjSmU3\nZGZ2VEtSUjUwZ0tVZTVDa200TEoxZE5qVjJBc0ZVcnhIODM5SkFTaFJCb3kxV202R1Vnby9ucFEy\nS0xRWFpuSGxxQnJPQ2d2SFVtaWliRDl1YzE3UTBnZkp4OCtvaG50dXBRa1dkZ21IcXdFV3NFOU51\nYXg1U0ZjV3BTeUNBUDNZaVZpYWxQaGdsSk5rMGZnU09MZFNzYUVrYTREYzRBN1R0Z3hwcU5JdFI4\nY3oxdlNkWHlpT1p4MXhZNEtwQWpwd2xnYW83Nm5DSlI3STlhSk42am1xNGlOVGhFbjh5R3lRQ0lP\nM1B3NEw0YXlDWGVDdkhRRDlFYmxEcGloYVBGNFhwb3FyY2JjV21jeWVyZytJUFFTcUc2ZDN3NkVX\ndEF0MFhxNWk5TzFVMVZ1bXhueVZRamZ0RXl6bC9kcWsxbXJ2QU5xV08zKzJFWXZ5VzE2VENqWXcw\nSkkxWkcxWmVWUzhwZm5WcmJtcFN2amJsNnBEWEh2cWMxNCtzUTBJVWxBVHViMUNBNEtNQTZkVkNS\nd3hoVEFITTdjR0NpbWxObHNvSDNZS2tYakNTVkVwc2F4UWhKYWd5T0NHcHRONVRXWVZzTW03NmE1\nNXVybTlXdnNrcWNUSXNYMUltNE1Lbm5hbitHc29kcUVxdTczWGlQVzZxMkZ5UUl6a21wSkJNemIw\nbUM3bXZLazBjMTU4eGkzUUNiRW9iRllxTHAyalpVdk9DQjRqazRReHc1TFNHZkplWDcveThEZWt2\nS1AzandRd241V05UQ1N4Z05kZ2FubzhJcnNXYnRuclZEVU9pQklLU0xHTGROUGQzNit4UzBGR0RP\nck1qRDRNa1c5WHBMeURFaVhLMEZzWDNjcWVXRzBaQ3JLYkJKYlMwMVJ5dWJ5RVFsenFmc3RLK0xh\nMU4xVC9JMEVwbDQ1cWF6SGJkd1oxT05aM1hjZG9nd3VmV1dlT1llQXJtVW9SbS9GMnJEMUdmMSsw\nMWdHRjJ2ZzRWaW96TktvblJDUktwMUo1SW10RnNGOTRnMEV2V1ZZYTdjdWJIUWV3U3dHVnBZVU5J\nKzArcFhZdm91RVE4WHBxenFJMmUwbUlOMkFDSHdLLzBXNVdJdlljVFpJK0pTZGZrdmIzVGVkZklL\nL3hsRWsvbEhHWWliRmROQ1Nrb3hDcERMdE9qR1FPNk5USkdhaFZsRWZEcVo4WGlLTWxoc0M0VnJO\nSVo5bmR2U2lDdm9scVJ3MGZhQitobzc4TWs3WnRZVnVRM1EzKzFyclhBbjNYd2xsekZBRG12WE5o\nYklTV0VpWUh3emR6TmhoQ04ybE9VdUJSZTBEQlBYbXNsZ3M1REdYUzZGaEJFU0l5U25MTnozTkMw\nV29EVUtucUtvT0d3S3lZK0p5QzRTTitxTXh0SUlWdEovQVhHL1NZUTFlL2JzMVVyb3A4RG1xaTAz\nZmZ4V2dGNGxKT3A3S1RYS3B3WGxzMnlyaXJVRm14U2ZBS0lQcXY5TTBZdmQxc1dqRmJXU1FwQzNo\nYnpDM1hYYzhRT3JxZ3FkbUhZdGZkQXljd1BNZEQzMDkvVFErN3ExVHpLemhXdmJrazRwZ2pHUXZj\nSlZWQ3pXZjR6V0svRkorY2dpMXVHNUtrdWg5NGkxb0xVYzJzS1JoM2FmaFlLbk5OR0xhQjFJbWRk\ndnRiOURKcm9lb05PMnJIcUJrTEY4SEl4blJhVDhuWE12ODJnNzRqZ0MyYzh5RjdSVTJDbnJRdlpo\nTG9lcEZKRnZsazVrQ2o5TVpLNVdMVHZpdU9zTmZPYVpEOVJJVkFKMWtoVHRsVXZ6ZExzV0t6emYr\nZG5USk1TWmlTRUtVdTlWaDhuSUo3WGt3NUZrOGVRRGpTOGNMNitxVWwzREQwOVFLY05lWkVuNVhn\neVg0cVRTY3hVSHBwQUdlbW5Jd1ZCMDBqOVp4RmNhQllQNzl6UWNrdGh4Wm1nc3hDdGN3VVVNMHZ6\neUdNTXZEa3NHSEVmbXpSWHdTY1BSa0ZaTWNNNSt4emw3SENSRGlVSWVWSTc2MC9neUloTVNkZGRo\nc3IxTUdYbmFCd1FFU0dqM29ia3dUWE1VU1lCdnpEalN5SWxRUVhWbWFkL1dpZDNIQ1RJSjR6OXcr\nRkNPb3g2NDNZcEdySnR3aGlJNExZa2dPK2JyMzhXRXVHZUlnN1h1ZTcySXd2a2hNbFMxWjhVbGFs\nOXZjZnFVZWR4MU1BUUk4dUtFTGZrT1Y1RVRGcHRlSUlFcEpzTWpSaFFzWGkrbnI0eXZJQ3k3U216\nMU9adFUzZ3drSHlTRmY0YlUxZ3htNzNGSG85WFNoUXN6TDB0T2RicHhkYnh4MTJIKzgwN2paTVp4\nU2xQTUN2bzY1ZU5STTFEN3B4bkV2UEczOTBlM0xFcVpvMkZDTTlXYzBjU3Rsb2kxaS9yQXhGRDhs\nSE5wWjZ0ZzNrbW81azdwelJzVGxzM0dQNGthcEF0cjBSeGxFNDluMEVjbTR4U1NLWlRHeVlwVUdT\nYm5rN0pPamptdEFnRWFQWDdnZnp0TkZCMFZRY3d1WHhYS3A5Q2VldkgvKy9XWlhRbENKem9jMU9N\nemJ0OUM2REJPL1dlemIvdW5IcnhUcmRYdnRaV3duYzF4RjJSejY5L3QxSnFVejFxb2o1cWkwSE5v\nNWdIdGhWYU1yVGxFaEtmWUZEV2xvK1UxRXpJdFQrS003b2VsTUtiRmp6U3JhYTJKYU9MN0p0Q21J\ncFhPUXRDdzJwam9lWnVNWk1xWm9UVEd1QkFzK1hpWlBTWk9NU1lldGFmMjBWSGZlcWVlK0NjYXJZ\nWUJhVjVUZHBGRFlyeFdWWjhsNEZySEdMZjhTTjIrVDh6NGU3cU1NOUtBb000OEsvQS8ydStCdmtM\nTnZVQ3RGMWVCd3BUcE1NR2hQWTFoSE1uNW5GYXM3TFVDMGhxeDdnZmljUERnN2JVdE45N3pHNDdT\nV3pXMjFseTlNTEY1dEpkemxDSTdXazM1NDVKT2xVSFMwNWhzclJtQ1JFNkswTWJ2UHZ3dko3YnN1\ndWNFRWEvTGdHL1BwaU9KejQwUVk0a24wa2xYTHRTWVpIVjErY3BIQytNWHpwR20xN3EwUWk0NkN0\naVZrbUdDZlFxT2wrQmNFcW1YdnZUVzVheWRjNG5Oa2RhU2ZZb0NTRk15blNSUG51Ulk2elB1bWRt\nUk1UMHhURXI0REtkVDZ4WFgyemdqck1xQUkzamdTWDl2VklQUHplZWZCR3BOOW1xbGVocEdrOXdx\nYW1HWVVQZ1pmZENSeCs3OE13RDZtaE05ODdVUHFGTDNTLzJQRFBkUm9BcXN2TjQvSUhUUDA0QjVE\nU1NadExYQzg4dHFNTFdDUmpDWTRpdDVxam9xRlN0WTgrS1gzejJ4ZWRjOVI0bk5XaUI5Y1gzQ0ox\nOHN1R1VNQ2tZQmhhaHpDaW16WXFZODZmTkkzNXB0Vlpad2pKMTI3VzJJYmQzTVJxTTA5VlpjTjBx\nSmp4bVhha3lpYWN5SW03QTFGeFQwV2VqRXczZXFBZktMZlNpOVlYbTU5NTFFWjV1SnhxdEQzblh1\nQ0YwR09kYXFuemZUVGw5US84cVZPL2NPQWU2Ym1rUW9vT2VQajd6aWhWcnNhNGNwSHB5ZStlSUhx\naEJVMkpkbzl3TDRjUysyQ2Q4T1daRnVwV2kvcWJBMWh4Ump4OE0rdjFWMU82dVJhUHpkYkV1TE5l\ndFNVWDExNHlKSXBwUGxzWTB6bXNlUnFiMG9MWTNQdktWM3l0bFNUMDY1WGloblZtc3VvSytQbGpl\ncnB6R004NURNTmppRFZaeE1TMkdpUmM4d0dmNmpYalR3aUtKejJLeGVMUkovSmNPVVBJUUhmekIx\nVmozdVdZMWlKWkt6OVZSWElmeVZaeTZoci9pL3hhZVorSnNxemxaRTQwMitsSmhtQ25oczlGOGZm\nZVNVcnc0MUUxVnJwMDU1SjJMZEp2Rmx4K2g1M2I1bkduZjR6T2daSWpyZU51NXdWa0Y5SURSZEpm\nYlhLdmZYOUFFNTV2QlNjelViWE1oYkRISVpWSEZnU2Y4eldMUkNKUXpoczQ3a0oycGxjMzc1aFJO\nL2I5T3ArOEh3Ulo5WFRweld4TE9mTlZQMktmM2JnbjlCQ1AvRnYyZjVVbG9iK3h5eC9XTi9Ucmgv\nNVJMK3BMNWZkbjc5YVFaK0trMXFmOFBNUCt0YzhoTkFkRWUzanZONVVrWGNKL28zQktEWGttZlZm\nWEJ3WDAzMXJwWnhBci91UWRFc0ZzVjBIVVphS2paNFdxVjFTRm9RZnJMNFM1Y2RldlJYdmwxLy8z\nell1NzBEVVpXaDdlKzQrOTErK3ducE5mcFVld21pOU1MRHYvUlFZOC8vMmdkT2Jkdno2ZHNQUGZo\nZUgvUTcvTWo3djE3L0xKTUdmNTM5ZVJqOUV2SGpBTDhsL0tFaEYvNzczc2JoV3dBMUtwTVRvN2R4\nUFJKN2x0R1g2c1ZxSWFrbk05WXdtdCtlcGdVUkhhd1BBeWlxUDBSd0ZVdmlSVy96bUsrQ2ZYa2s1\nWGVpT3JQMFFvY3laaGs0T2ZkWW94aVFUVkpuMHA1dVBEbCtMRHpRbXRDU09ISG13Q0NYRmVIOHlu\nL3c3d3JFcUpyVEdENzlPS3J1SzFudXh6U05ucVZ3VWlUOWdpQXRhajQ2aUo2V29qMUhWZnE4UTdX\nc3h3ZzR0R2ZQaDh5RER5NEMrT1ZsU21UY04wU1NTYUpvQ0VpZmcwMTYybHFjSkg5SHdoZVk0dVhp\na3FOVFhQejJRTmVGdSs0T3hmMlNtSEJtYWd5LytPY0pucysyS29VMjNINndYZEhTN2g2RlpDcVVJ\nNDNMcStXWkw3Ni90djBkSDJzZU83WmF0S0xUSUJmNjBxTzl2SFgzMmk5Uk5QeFdtMDc4MXRHSDcv\neVYzc1lKYmQ1OTc1K1phUGhXbTB4ODh1Z2pkOTR4eUZWZHR0dkdTNEcyM0x6L1I0SDRuc1RhdDU5\nNDlKZDZsaFJiM3JUL2JTVHgvNXNpdmZXRmgrNGNxQTd6L3dOaXZoeHB0VzM2TXdBQUFBQkpSVTVF\ncmtKZ2dnPT0=\n');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `financial_report`
--

DROP TABLE IF EXISTS `financial_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `financial_report` (
  `financial_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) NOT NULL,
  `dr_cost` bigint DEFAULT NULL,
  `cr_cost` bigint DEFAULT NULL,
  PRIMARY KEY (`financial_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `financial_report`
--

LOCK TABLES `financial_report` WRITE;
/*!40000 ALTER TABLE `financial_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `financial_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incomel_report`
--

DROP TABLE IF EXISTS `incomel_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incomel_report` (
  `income_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) NOT NULL,
  `dr_cost` bigint DEFAULT NULL,
  `cr_cost` bigint DEFAULT NULL,
  PRIMARY KEY (`income_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incomel_report`
--

LOCK TABLES `incomel_report` WRITE;
/*!40000 ALTER TABLE `incomel_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `incomel_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journalizingbook`
--

DROP TABLE IF EXISTS `journalizingbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `journalizingbook` (
  `jr_id` int NOT NULL AUTO_INCREMENT,
  `jr_type` varchar(2) NOT NULL,
  `account_code` varchar(5) NOT NULL,
  `account_name` varchar(45) DEFAULT NULL,
  `business_code` varchar(5) DEFAULT NULL,
  `business_client` varchar(45) DEFAULT NULL,
  `jr_dr` varchar(14) DEFAULT '0',
  `jr_cr` varchar(14) DEFAULT '0',
  `jr_description` varchar(100) DEFAULT NULL,
  `jr_evidence` varchar(6) DEFAULT NULL,
  `bk_id` varchar(15) DEFAULT NULL,
  `ti_id` varchar(15) DEFAULT NULL,
  `jr_base` varchar(2) NOT NULL,
  PRIMARY KEY (`jr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journalizingbook`
--

LOCK TABLES `journalizingbook` WRITE;
/*!40000 ALTER TABLE `journalizingbook` DISABLE KEYS */;
INSERT INTO `journalizingbook` VALUES (1,'차변','101','현금','','','10000000','','','','20250317030001',NULL,'bk'),(2,'대변','331','자본금','','','','10000000','','','20250317030001',NULL,'bk'),(3,'차변','135','부가세대급금','','','100000','','','세금계산서',NULL,'20250317120001','ti'),(4,'대변','101','현금','','','','1100000','','',NULL,'20250317120001','ti'),(5,'차변','153','원재료','','','1000000','','','',NULL,'20250317120001','ti'),(6,'차변','103','보통예금','','국민은행','4000000','','','','20250317030002',NULL,'bk'),(7,'대변','101','현금','','','','4000000','','','20250317030002',NULL,'bk'),(8,'차변','801','급여','','','3000000','','','','20250325030001',NULL,'bk'),(9,'대변','254','예수금','','','','300000','소득세 등 예수금','','20250325030001',NULL,'bk'),(10,'대변','262','미지급비용','','','','2700000','','','20250325030001',NULL,'bk'),(11,'차변','254','예수금','','','300000','','','','20250325030002',NULL,'bk'),(12,'대변','103','보통예금','','','','3000000','','','20250325030002',NULL,'bk'),(13,'차변','262','미지급비용','','','2700000','','','','20250325030002',NULL,'bk'),(14,'대변','255','부가세예수금','','','','200000','','세금계산서',NULL,'20250320110001','ti'),(15,'차변','103','보통예금','','','2200000','','상품 매출 후 계좌로 입금 받음','',NULL,'20250320110001','ti'),(16,'대변','146','상품','','','','2000000','','',NULL,'20250320110001','ti'),(17,'대변','255','부가세예수금','','','','400000','','세금계산서',NULL,'20250321110001','ti'),(18,'차변','103','보통예금','','','4400000','','','',NULL,'20250321110001','ti'),(19,'대변','401','상품매출','','','','4000000','','',NULL,'20250321110001','ti');
/*!40000 ALTER TABLE `journalizingbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialtable`
--

DROP TABLE IF EXISTS `materialtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialtable` (
  `materialCode` varchar(10) NOT NULL,
  `materialName` varchar(255) DEFAULT NULL,
  `materialType` varchar(10) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `sellingPrice` int DEFAULT NULL,
  `purchasePrice` int DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `correspondentCode` varchar(15) DEFAULT NULL,
  `correspondentName` varchar(15) DEFAULT NULL,
  `Date_up` varchar(10) DEFAULT NULL,
  `department` varchar(10) DEFAULT NULL,
  `manager` char(10) DEFAULT NULL,
  PRIMARY KEY (`materialCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialtable`
--

LOCK TABLES `materialtable` WRITE;
/*!40000 ALTER TABLE `materialtable` DISABLE KEYS */;
INSERT INTO `materialtable` VALUES ('MAT001','원자재1','원자재',1200,NULL,2400,'kg',5,'c001','e001','2025-03-19','Dept1','e001'),('MAT002','원자재2','원자재',1200,NULL,2400,'kg',5,'c002','e001','2025-03-19','Dept1','e001'),('MAT003','원자재3','원자재',2500,NULL,3400,'kg',5,'c003','e001','2025-03-19','Dept1','e001'),('MAT004','원자재4','원자재',2040,NULL,2400,'kg',5,'c001','e001','2025-03-19','Dept1','e001'),('MAT005','원자재5','원자재',200,NULL,2400,'kg',5,'c002','e001','2025-03-19','Dept1','e001'),('MAT006','원자재6','원자재',1300,NULL,2900,'kg',5,'c003','e001','2025-03-19','Dept1','e001'),('MAT007','원자재7','원자재',1700,NULL,2800,'kg',5,'c001','e001','2025-03-19','Dept1','e001'),('MAT008','원자재8','원자재',1010,NULL,1400,'kg',5,'c002','e001','2025-03-19','Dept1','e001'),('MAT009','원자재9','원자재',3070,NULL,4400,'kg',5,'c003','e001','2025-03-19','Dept1','e001'),('PRD001','완제품1','완제품',NULL,2400,NULL,'kg',5,'c001','e001','2025-03-19','Dept1','e001'),('PRD002','완제품2','완제품',NULL,5000,NULL,'kg',3,'c002','e001','2025-03-19','Dept1','e001');
/*!40000 ALTER TABLE `materialtable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mo`
--

DROP TABLE IF EXISTS `mo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mo` (
  `mo_code` varchar(255) NOT NULL,
  `sop_code` varchar(255) DEFAULT NULL,
  `bom_code` varchar(255) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `order_code` varchar(255) DEFAULT NULL,
  `due_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mo_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mo`
--

LOCK TABLES `mo` WRITE;
/*!40000 ALTER TABLE `mo` DISABLE KEYS */;
INSERT INTO `mo` VALUES ('MO001','SOP1','BOM1','100','생산 완료','PRD001','완제품1','ORD001','2025-03-15'),('MO002','SOP2','BOM2','200','생산 완료','PRD002','완제품2','ORD002','2025-03-14');
/*!40000 ALTER TABLE `mo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `msg` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (56,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(57,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(58,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(59,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(60,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(61,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(62,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(63,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(64,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}'),(65,'e007','{\"from_id\": \"e006\", \"from_name\": \"육육름\", \"type\": \"appr\", \"msg\": {\"name\": \"테스트\", \"appr_type\": \"aa\", \"appr_contents\": \"bb\", \"sign\": [\"육육름\"]}}');
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_form`
--

DROP TABLE IF EXISTS `order_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_form` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_code` varchar(20) NOT NULL,
  `internal_external` varchar(20) NOT NULL,
  `creator_name` varchar(50) NOT NULL,
  `creator_position` varchar(30) DEFAULT NULL,
  `creator_phone` varchar(20) DEFAULT NULL,
  `creator_email` varchar(50) DEFAULT NULL,
  `administrator_name` varchar(50) NOT NULL,
  `administrator_position` varchar(30) DEFAULT NULL,
  `administrator_phone` varchar(20) DEFAULT NULL,
  `administrator_email` varchar(50) DEFAULT NULL,
  `product_code` varchar(100) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `unit_price` int DEFAULT NULL,
  `stock` varchar(30) DEFAULT NULL,
  `transaction_quantity` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `order_vat` int DEFAULT NULL,
  `Customer_code` char(100) DEFAULT NULL,
  `sledding` varchar(50) DEFAULT NULL,
  `delivery_date` datetime DEFAULT NULL,
  `creation_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_form`
--

LOCK TABLES `order_form` WRITE;
/*!40000 ALTER TABLE `order_form` DISABLE KEYS */;
INSERT INTO `order_form` VALUES (1,'ORD001','1','1','1','1','1','1','1','1','1','PRD001','완제품1',1,'1',1,1,1,'0001','1','2025-03-14 00:00:00','2025-03-14 00:00:00','2025-03-14 00:00:00'),(2,'ORD002','1','1','1','1','1','1','1','1','1','PRD002','완제품2',1,'1',1,1,1,'0002','1','2025-03-14 00:00:00','2025-03-14 00:00:00','2025-03-14 00:00:00'),(3,'ORD003','1','1','1','1','1','1','1','1','1','PRD003','완제품3',1,'1',1,1,1,'0003','1','2025-03-14 00:00:00','2025-03-14 00:00:00','2025-03-14 00:00:00');
/*!40000 ALTER TABLE `order_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overtime`
--

DROP TABLE IF EXISTS `overtime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overtime` (
  `employee_code` varchar(20) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `department` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `work_start_time` varchar(20) DEFAULT NULL,
  `work_end_time` varchar(20) DEFAULT NULL,
  `overtime` varchar(20) DEFAULT NULL,
  `Approval_status` int DEFAULT NULL,
  `pay` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overtime`
--

LOCK TABLES `overtime` WRITE;
/*!40000 ALTER TABLE `overtime` DISABLE KEYS */;
/*!40000 ALTER TABLE `overtime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pay_stub`
--

DROP TABLE IF EXISTS `pay_stub`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pay_stub` (
  `pay_stub_id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `date_of_paystub` date NOT NULL,
  `total_salary` int NOT NULL,
  `deductible` int NOT NULL,
  `actual_salary` int NOT NULL,
  PRIMARY KEY (`pay_stub_id`),
  KEY `employee_code` (`employee_code`),
  CONSTRAINT `pay_stub_ibfk_1` FOREIGN KEY (`employee_code`) REFERENCES `employee` (`employee_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pay_stub`
--

LOCK TABLES `pay_stub` WRITE;
/*!40000 ALTER TABLE `pay_stub` DISABLE KEYS */;
/*!40000 ALTER TABLE `pay_stub` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plant`
--

DROP TABLE IF EXISTS `plant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant` (
  `plant_code` varchar(45) NOT NULL,
  `plant_name` char(50) NOT NULL,
  `location` varchar(45) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `changed_by` varchar(20) DEFAULT NULL,
  `changed_on` datetime DEFAULT NULL,
  `del_flag` char(1) DEFAULT NULL,
  PRIMARY KEY (`plant_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant`
--

LOCK TABLES `plant` WRITE;
/*!40000 ALTER TABLE `plant` DISABLE KEYS */;
INSERT INTO `plant` VALUES ('P001','대전창고','대전광역시','04200000000',NULL,'daejeon@gmail.com',NULL,'2025-03-11 00:00:00','USER01','2025-03-17 09:56:22',NULL),('P002','인천창고','인천광역시','03277776666',NULL,'incheonsea@naver.com','USER01','2025-03-14 20:13:05','e001','2025-03-18 12:25:54',NULL),('P003','부산창고','부산광역시','05293939393',NULL,'majashinitna@hanmail.net','USER01','2025-03-17 09:16:21',NULL,NULL,NULL),('P004','포항창고','포항시 포항군','06154545454',NULL,'pohanghang@daum.net','USER01','2025-03-17 09:17:26',NULL,NULL,'X'),('P005','서울창고','서울시 영등포구','0212345678',NULL,'iseoulyou@naver.com','USER01','2025-03-17 09:19:38',NULL,NULL,NULL),('P006','울산창고','울산시 울산구','05263636363',NULL,'gdpgood@naver.com','USER01','2025-03-17 09:21:05',NULL,NULL,NULL),('P007','세종창고','윤서네집','04412341234',NULL,'yonseo@naver.com','USER01','2025-03-17 09:55:32',NULL,NULL,NULL),('P008','쿠팡','쿠팡','01000000000','12345','asa@daum.net','e006','2025-03-19 10:23:21',NULL,NULL,NULL);
/*!40000 ALTER TABLE `plant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plant_material`
--

DROP TABLE IF EXISTS `plant_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant_material` (
  `material_code` varchar(50) NOT NULL,
  `material_name` varchar(50) DEFAULT NULL,
  `material_type` varchar(50) DEFAULT NULL,
  `plant_name` varchar(50) DEFAULT NULL,
  `plant_code` varchar(50) DEFAULT NULL,
  `plant_location` varchar(50) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `unit` varchar(50) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`material_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant_material`
--

LOCK TABLES `plant_material` WRITE;
/*!40000 ALTER TABLE `plant_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `plant_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchasing_order`
--

DROP TABLE IF EXISTS `purchasing_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchasing_order` (
  `num` varchar(1) DEFAULT NULL,
  `po_num` varchar(6) NOT NULL,
  `vendor` varchar(6) DEFAULT NULL,
  `mat_code` varchar(45) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `measure` varchar(4) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `measure2` varchar(4) DEFAULT NULL,
  `plant` varchar(4) DEFAULT NULL,
  `manufactoring_code` varchar(10) DEFAULT NULL,
  `manager` varchar(20) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `changed_by` varchar(20) DEFAULT NULL,
  `changed_on` datetime DEFAULT NULL,
  `del_flag` char(1) DEFAULT NULL,
  `stat` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchasing_order`
--

LOCK TABLES `purchasing_order` WRITE;
/*!40000 ALTER TABLE `purchasing_order` DISABLE KEYS */;
INSERT INTO `purchasing_order` VALUES (NULL,'po0001','c001','MAT004',5,'box',5000,NULL,NULL,'MO001',NULL,NULL,NULL,'2025-03-11 00:00:00',NULL,NULL,NULL,'H'),(NULL,'po0001','c001','MAT003',5,'box',2000,NULL,NULL,'MO001','e001','e001','e001','2025-03-18 12:37:53',NULL,NULL,NULL,'B'),(NULL,'po0002','c002','MAT002',5,'box',11000,NULL,NULL,'MO002','e001','d001','e001','2025-03-18 12:41:12',NULL,NULL,NULL,'H'),(NULL,'po0002','c002','MAT001',2,'box',5800,NULL,NULL,'MO002','e001','d001','e001','2025-03-18 12:41:12',NULL,NULL,NULL,'B');
/*!40000 ALTER TABLE `purchasing_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receiving`
--

DROP TABLE IF EXISTS `receiving`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receiving` (
  `receiving_code` varchar(10) NOT NULL,
  `order_code` varchar(20) DEFAULT NULL,
  `receiving_classification` varchar(20) DEFAULT NULL,
  `client_code` varchar(10) DEFAULT NULL,
  `client_name` varchar(50) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `material_code` varchar(50) DEFAULT NULL,
  `material_name` varchar(50) DEFAULT NULL,
  `receiving_responsibility` varchar(20) DEFAULT NULL,
  `purchase_order_code` varchar(10) DEFAULT NULL,
  `plant_code` varchar(20) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`receiving_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receiving`
--

LOCK TABLES `receiving` WRITE;
/*!40000 ALTER TABLE `receiving` DISABLE KEYS */;
INSERT INTO `receiving` VALUES ('REC001','ORD001','원자재','C001','e001',100,'kg','MAT001','e001','e006','po0001','p001',10000),('REC002','ORD002','원자재','C002','e001',200,'kg','MAT002','e002','e007','po0002','p002',12000);
/*!40000 ALTER TABLE `receiving` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary_details`
--

DROP TABLE IF EXISTS `salary_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary_details` (
  `pay_stub_id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `pay_out_date` date DEFAULT NULL,
  `basic_salary` int DEFAULT '0',
  `allowance` int DEFAULT '0',
  `bonus` int DEFAULT '0',
  `additional_allowance` int DEFAULT '0',
  `annual_leave_allowance` int DEFAULT '0',
  `total_salary` int DEFAULT '0',
  `income_tax` int DEFAULT '0',
  `final_payment` int DEFAULT '0',
  PRIMARY KEY (`pay_stub_id`),
  KEY `fk_salarydetails_employee` (`employee_code`),
  CONSTRAINT `fk_salarydetails_employee` FOREIGN KEY (`employee_code`) REFERENCES `employee` (`employee_code`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary_details`
--

LOCK TABLES `salary_details` WRITE;
/*!40000 ALTER TABLE `salary_details` DISABLE KEYS */;
INSERT INTO `salary_details` VALUES (27,'e001','2025-03-17',5000000,1000,1000,0,0,5002000,165066,4836934),(28,'e002','2025-03-17',500,1000000,50000,0,0,1050500,34666,1015834),(29,'9999','2025-03-19',100,0,0,0,0,100,3,97),(30,'9999','2025-03-19',100,0,1,0,0,101,3,98),(31,'9999','2025-03-02',100,0,0,0,0,100,3,97);
/*!40000 ALTER TABLE `salary_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `severance_pay`
--

DROP TABLE IF EXISTS `severance_pay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `severance_pay` (
  `severance_pay_id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `calculation_period` varchar(50) NOT NULL,
  `total_days` int NOT NULL,
  `basic_salary` int NOT NULL,
  `additional_allowance` int DEFAULT NULL,
  `total_salary` int NOT NULL,
  `annual_bonus_total` int DEFAULT NULL,
  `average_daily_wage` int DEFAULT NULL,
  `annual_leave_allowance` int DEFAULT NULL,
  `severance_income` int DEFAULT NULL,
  `income_tax` int DEFAULT NULL,
  `local_income_tax` int DEFAULT NULL,
  `final_payment` int DEFAULT NULL,
  PRIMARY KEY (`severance_pay_id`),
  KEY `employee_code` (`employee_code`),
  CONSTRAINT `severance_pay_ibfk_1` FOREIGN KEY (`employee_code`) REFERENCES `employee` (`employee_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `severance_pay`
--

LOCK TABLES `severance_pay` WRITE;
/*!40000 ALTER TABLE `severance_pay` DISABLE KEYS */;
/*!40000 ALTER TABLE `severance_pay` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipping`
--

DROP TABLE IF EXISTS `shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipping` (
  `shipping_code` varchar(10) NOT NULL,
  `order_code` varchar(20) DEFAULT NULL,
  `material_classification` varchar(20) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `selling_price` int DEFAULT NULL,
  `vat_price` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `material_code` varchar(50) DEFAULT NULL,
  `material_name` varchar(50) DEFAULT NULL,
  `sales_order_number` varchar(20) DEFAULT NULL,
  `purchase_order_code` varchar(10) DEFAULT NULL,
  `client_code` char(10) DEFAULT NULL,
  `client_name` char(50) DEFAULT NULL,
  PRIMARY KEY (`shipping_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipping`
--

LOCK TABLES `shipping` WRITE;
/*!40000 ALTER TABLE `shipping` DISABLE KEYS */;
INSERT INTO `shipping` VALUES ('SHP001','ORD001','원자재',100,'kg',15000,1500,16500,'MAT001','원자재1',NULL,NULL,'C001','e001'),('SHP002','ORD002','원자재',200,'kg',18000,1800,19800,'MAT002','원자재2',NULL,NULL,'C002','e001');
/*!40000 ALTER TABLE `shipping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sop`
--

DROP TABLE IF EXISTS `sop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sop` (
  `SOP_Code` varchar(255) NOT NULL,
  `BOM_Code` varchar(255) DEFAULT NULL,
  `order_code` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `writter` varchar(255) DEFAULT NULL,
  `written_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SOP_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sop`
--

LOCK TABLES `sop` WRITE;
/*!40000 ALTER TABLE `sop` DISABLE KEYS */;
INSERT INTO `sop` VALUES ('SOP1','BOM1','ORD001','PRD001','완제품1','e001','2025-03-11'),('SOP2','BOM2','ORD002','PRD002','완제품2','e009','2025-03-12'),('SOP3','BOM3','ORD003','PRD003','완제품3','e010','2025-03-12');
/*!40000 ALTER TABLE `sop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sop_f`
--

DROP TABLE IF EXISTS `sop_f`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sop_f` (
  `sop_code` varchar(255) DEFAULT NULL,
  `work_name` varchar(255) DEFAULT NULL,
  `working` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sop_f`
--

LOCK TABLES `sop_f` WRITE;
/*!40000 ALTER TABLE `sop_f` DISABLE KEYS */;
INSERT INTO `sop_f` VALUES ('sop11','조립1','핸들 장착','사진1'),('sop11','조립2','바퀴 장착','사진2'),('sop22','조립1','안장 장착','사진'),('SOP3','조립1','바퀴 장착',''),('SOP3','조립2','핸들 장착','');
/*!40000 ALTER TABLE `sop_f` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taxinvoice`
--

DROP TABLE IF EXISTS `taxinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taxinvoice` (
  `ti_id` varchar(15) NOT NULL,
  `ti_create_date` date NOT NULL,
  `ti_type` varchar(2) NOT NULL,
  `business_client` varchar(45) DEFAULT NULL,
  `business_number` varchar(14) NOT NULL,
  `business_code` varchar(5) DEFAULT NULL,
  `ti_description` varchar(100) DEFAULT NULL,
  `ti_ori_amount` bigint NOT NULL,
  `ti_tax_rate` char(3) DEFAULT '10%',
  `ti_vat` bigint NOT NULL,
  `ti_amount` bigint NOT NULL,
  `ti_publish_state` varchar(4) DEFAULT 'None',
  PRIMARY KEY (`ti_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taxinvoice`
--

LOCK TABLES `taxinvoice` WRITE;
/*!40000 ALTER TABLE `taxinvoice` DISABLE KEYS */;
INSERT INTO `taxinvoice` VALUES ('20250317120001','2025-03-17','매입','대전시','123-12-12345',NULL,'원재료매입',1000000,'10%',100000,1100000,'발행'),('20250320110001','2025-03-20','매출','부산시','456-45-45678',NULL,'상품 매출',2000000,'10%',200000,2200000,''),('20250321110001','2025-03-21','매출','서울시','512-32-58385',NULL,'상품 매출',4000000,'10%',400000,4400000,'발행');
/*!40000 ALTER TABLE `taxinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `work_name` varchar(255) DEFAULT NULL,
  `working` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `sop_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test1`
--

DROP TABLE IF EXISTS `test1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test1` (
  `work_name` varchar(255) DEFAULT NULL,
  `working` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `sop_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test1`
--

LOCK TABLES `test1` WRITE;
/*!40000 ALTER TABLE `test1` DISABLE KEYS */;
/*!40000 ALTER TABLE `test1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_history_inquiry`
--

DROP TABLE IF EXISTS `transaction_history_inquiry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_history_inquiry` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Transaction_date` char(100) DEFAULT NULL,
  `Customer_name` char(100) DEFAULT NULL,
  `business_number` int DEFAULT NULL,
  `Customer_code` char(100) DEFAULT NULL,
  `Type_business` char(100) DEFAULT NULL,
  `Country` char(100) DEFAULT NULL,
  `item` char(100) DEFAULT NULL,
  `quantity` char(50) DEFAULT NULL,
  `unit_price` char(100) DEFAULT NULL,
  `total_price` char(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_history_inquiry`
--

LOCK TABLES `transaction_history_inquiry` WRITE;
/*!40000 ALTER TABLE `transaction_history_inquiry` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction_history_inquiry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'erp_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-19 20:45:54
