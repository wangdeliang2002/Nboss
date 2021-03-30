-- MySQL dump 10.14  Distrib 5.5.68-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: nboss
-- ------------------------------------------------------
-- Server version	5.5.68-MariaDB

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(100) DEFAULT NULL,
  `manager` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manager` (`manager`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'pbkdf2:sha256:50000$TkExX9Jm$d63477853a17dcaedcd52be4b6213ebb74b61a12456762ac19d6b7dfb559aa57','deliangw',NULL);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('6ee0a90d1f2f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_id` (`goods_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_cart_addtime` (`addtime`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`goods_id`) REFERENCES `devices` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (112,10,7,NULL,'2021-03-28 23:24:28');
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `devices`
--

DROP TABLE IF EXISTS `devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `introduction` text,
  `addtime` datetime DEFAULT NULL,
  `views_count` int(11) DEFAULT '0',
  `subcat_id` int(11) DEFAULT NULL,
  `supercat_id` int(11) DEFAULT NULL,
  `right` varchar(4) DEFAULT '0',
  `status` varchar(10) DEFAULT NULL,
  `device_ip` varchar(15) DEFAULT NULL,
  `hostname` varchar(255) DEFAULT NULL,
  `system` varchar(40) DEFAULT NULL,
  `kernel` varchar(40) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `devices_supercat_id_index` (`supercat_id`),
  KEY `devices_subcat_id_index` (`subcat_id`),
  KEY `devices_addtime_index` (`addtime`),
  CONSTRAINT `devices_subcat__fk` FOREIGN KEY (`subcat_id`) REFERENCES `subcat` (`id`),
  CONSTRAINT `devices_supercat_id_fk` FOREIGN KEY (`supercat_id`) REFERENCES `supercat` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devices`
--

LOCK TABLES `devices` WRITE;
/*!40000 ALTER TABLE `devices` DISABLE KEYS */;
INSERT INTO `devices` VALUES (10,'金桥#6 B101 A07','101.jpg','DS-LITE服务器','2021-03-28 23:23:37',0,1,1,'0',NULL,'135.251.196.198',NULL,NULL,NULL,'tester','123456');
/*!40000 ALTER TABLE `devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `original_price` decimal(10,2) DEFAULT NULL,
  `current_price` decimal(10,2) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `introduction` text,
  `is_sale` tinyint(1) DEFAULT NULL,
  `is_new` tinyint(1) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `views_count` int(11) DEFAULT NULL,
  `subcat_id` int(11) DEFAULT NULL,
  `supercat_id` int(11) DEFAULT NULL,
  `right` varchar(4) DEFAULT '0',
  `status` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_goods_addtime` (`addtime`),
  KEY `supercat_id` (`supercat_id`),
  KEY `subcat_id` (`subcat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (62,'192.168.3.58',1.00,0.00,'101.jpg','CentOS IPv6 Server',0,1,'2021-03-20 11:39:29',1,40,31,'0','on'),(63,'192.168.3.30',1.00,0.00,'105.jpg','Raspberry Pi Server',0,0,'2021-03-21 22:22:43',2,51,31,'0','on'),(64,'135.251.196.200',1.00,0.00,'102.jpg','Windows Server',0,0,'2021-03-21 22:27:16',4,41,31,'0','on'),(65,'135.251.0.0',1.00,0.00,'103.jpg','Cisco Switch',0,0,'2021-03-21 22:28:29',2,53,32,'0','on'),(66,'135.251.1.1',1.00,0.00,'104.jpg','华为Switch',0,0,'2021-03-21 22:29:38',9,52,32,'0','on'),(67,'135.251.2.2',1.00,0.00,'104.jpg','华为Switch',0,0,'2021-03-21 22:32:11',2,52,32,'0','on'),(68,'135.251.3.3',1.00,0.00,'106.jpg','OMNI Switch',0,0,'2021-03-21 22:36:31',2,54,32,'0','on'),(69,'135.251.4.4',1.00,0.00,'107.jpg','7360 OLT',0,0,'2021-03-21 22:50:49',10,42,35,'0','on'),(70,'135.251.5.5',1.00,0.00,'108.jpg','7342 OLT',0,0,'2021-03-21 22:52:52',6,43,35,'0','on');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_devices`
--

DROP TABLE IF EXISTS `my_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_devices` (
  `id` int(11) NOT NULL DEFAULT '0',
  `devices_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `my_devices_devices__fk` (`devices_id`),
  KEY `my_devices_addtime_index` (`addtime`),
  KEY `my_devices_user_id_index` (`user_id`),
  CONSTRAINT `my_devices_devices__fk` FOREIGN KEY (`devices_id`) REFERENCES `devices` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_devices`
--

LOCK TABLES `my_devices` WRITE;
/*!40000 ALTER TABLE `my_devices` DISABLE KEYS */;
/*!40000 ALTER TABLE `my_devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `recevie_name` varchar(255) DEFAULT NULL,
  `recevie_address` varchar(255) DEFAULT NULL,
  `recevie_tel` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_orders_addtime` (`addtime`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_detail`
--

DROP TABLE IF EXISTS `orders_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_id` (`goods_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `orders_detail_ibfk_1` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `orders_detail_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_detail`
--

LOCK TABLES `orders_detail` WRITE;
/*!40000 ALTER TABLE `orders_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ports_info`
--

DROP TABLE IF EXISTS `ports_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ports_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `port_name` varchar(20) DEFAULT NULL,
  `mtu` varchar(5) DEFAULT NULL,
  `mac` varchar(17) DEFAULT NULL,
  `ipv4` varchar(15) DEFAULT NULL,
  `ipv6_local` varchar(30) DEFAULT NULL,
  `ipv6_global` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ports_info`
--

LOCK TABLES `ports_info` WRITE;
/*!40000 ALTER TABLE `ports_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `ports_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcat`
--

DROP TABLE IF EXISTS `subcat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subcat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(100) DEFAULT NULL,
  `addtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `super_cat_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `super_cat_id` (`super_cat_id`),
  KEY `ix_subcat_addtime` (`addtime`),
  CONSTRAINT `super_cat_id_fk` FOREIGN KEY (`super_cat_id`) REFERENCES `supercat` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcat`
--

LOCK TABLES `subcat` WRITE;
/*!40000 ALTER TABLE `subcat` DISABLE KEYS */;
INSERT INTO `subcat` VALUES (1,'Centos','2021-03-28 12:52:01',1),(2,'Windows','2021-03-28 12:52:44',1),(3,'SpeedTest','2021-03-28 12:52:52',1),(4,'OMNI','2021-03-28 12:53:05',2),(5,'华为','2021-03-28 12:53:17',2),(7,'Cisco','2021-03-28 12:59:42',2);
/*!40000 ALTER TABLE `subcat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supercat`
--

DROP TABLE IF EXISTS `supercat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supercat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(100) DEFAULT NULL,
  `addtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ix_supercat_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supercat`
--

LOCK TABLES `supercat` WRITE;
/*!40000 ALTER TABLE `supercat` DISABLE KEYS */;
INSERT INTO `supercat` VALUES (1,'服务器','2021-03-28 11:34:52'),(2,'交换机','2021-03-28 11:35:22'),(3,'电脑','2021-03-28 11:35:39'),(4,'OLT','2021-03-28 11:35:53'),(5,'RGW','2021-03-28 11:36:15');
/*!40000 ALTER TABLE `supercat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `consumption` decimal(10,2) DEFAULT NULL,
  `right` varchar(4) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `ix_user_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (7,'deliangw','wangdeliang2002@163.com','13482050248','2021-03-20 12:06:22','pbkdf2:sha256:150000$fYNUqTYa$b81d006a9ae5a309a0309f60b078129ebfed2f98a104c6646900a7fbaf416285',0.00,'0');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-28 23:39:34
