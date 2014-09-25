-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: oferclub
-- ------------------------------------------------------
-- Server version	5.5.38-0ubuntu0.14.04.1

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
-- Table structure for table `account_account`
--

DROP TABLE IF EXISTS `account_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `provider` varchar(20) NOT NULL,
  `provider_id` varchar(100) NOT NULL,
  `provider_username` varchar(100) NOT NULL,
  `oauth_token` varchar(254) NOT NULL,
  `oauth_token_secret` varchar(254) NOT NULL,
  `refresh_token` varchar(254) NOT NULL,
  `expires_in` datetime DEFAULT NULL,
  `created_on` datetime NOT NULL,
  `updated_on` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_account_6340c63c` (`user_id`),
  KEY `account_account_3f126c2d` (`provider`),
  CONSTRAINT `user_id_refs_oferclubabstractuser_ptr_id_33bcbf58` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubuser` (`oferclubabstractuser_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_account`
--

LOCK TABLES `account_account` WRITE;
/*!40000 ALTER TABLE `account_account` DISABLE KEYS */;
INSERT INTO `account_account` VALUES (1,2,'facebook','833139646718184','833139646718184','CAAE15daDi5cBAIdyzGYSVUTRGhZAZA3dVGZBaVcUNrf4raAoNxekZB3agzwFMyW3bq2qxlilZAez2vPmBZBwctI1oAPmxKHT3kW7s542G0IIsadcPCEnpZC4QdYXWZCHPlz7P5HH82FZB2dZANuT4KkaqA4wNr4HjCHLZARuPQd59WJ06BL1EqNLQOZBbBc6FphWwi0yvTTHJwJD8ypZAbhsBOZB5U','','','2014-11-16 23:39:07','2014-09-17 23:45:08','2014-09-17 23:45:08');
/*!40000 ALTER TABLE `account_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_address`
--

DROP TABLE IF EXISTS `account_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cep` varchar(9) NOT NULL,
  `street` varchar(255) NOT NULL,
  `number` varchar(100) NOT NULL,
  `complement` varchar(100) NOT NULL,
  `neighborhood` varchar(100) NOT NULL,
  `city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_address_b376980e` (`city_id`),
  CONSTRAINT `city_id_refs_id_38c63089` FOREIGN KEY (`city_id`) REFERENCES `account_city` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_address`
--

LOCK TABLES `account_address` WRITE;
/*!40000 ALTER TABLE `account_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_affiliate`
--

DROP TABLE IF EXISTS `account_affiliate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_affiliate` (
  `oferclubabstractuser_ptr_id` int(11) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `phone` varchar(20),
  `cellphone` varchar(20),
  `owner_name` varchar(200) DEFAULT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `agency` varchar(100) DEFAULT NULL,
  `number` varchar(100) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `percent` decimal(10,2),
  PRIMARY KEY (`oferclubabstractuser_ptr_id`),
  KEY `account_affiliate_b376980e` (`city_id`),
  CONSTRAINT `city_id_refs_id_c927fe33` FOREIGN KEY (`city_id`) REFERENCES `account_city` (`id`),
  CONSTRAINT `oferclubabstractuser_ptr_id_refs_id_8b94a588` FOREIGN KEY (`oferclubabstractuser_ptr_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_affiliate`
--

LOCK TABLES `account_affiliate` WRITE;
/*!40000 ALTER TABLE `account_affiliate` DISABLE KEYS */;
INSERT INTO `account_affiliate` VALUES (4,NULL,'','','','','','','',NULL);
/*!40000 ALTER TABLE `account_affiliate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_city`
--

DROP TABLE IF EXISTS `account_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `state_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_city_5654bf12` (`state_id`),
  CONSTRAINT `state_id_refs_id_bf1aeefd` FOREIGN KEY (`state_id`) REFERENCES `account_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_city`
--

LOCK TABLES `account_city` WRITE;
/*!40000 ALTER TABLE `account_city` DISABLE KEYS */;
INSERT INTO `account_city` VALUES (1,'Olinda',1),(2,'Recife',1),(3,'Camaragibe',1),(4,'Jaboatão dos Guararapes',1);
/*!40000 ALTER TABLE `account_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_filial`
--

DROP TABLE IF EXISTS `account_filial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_filial` (
  `oferclubabstractuser_ptr_id` int(11) NOT NULL,
  `partner_id` int(11) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `phone` varchar(20),
  `cellphone` varchar(20),
  `owner_name` varchar(200) DEFAULT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `agency` varchar(100) DEFAULT NULL,
  `number` varchar(100) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`oferclubabstractuser_ptr_id`),
  KEY `account_filial_42b53b76` (`partner_id`),
  KEY `account_filial_b376980e` (`city_id`),
  CONSTRAINT `city_id_refs_id_2febff6c` FOREIGN KEY (`city_id`) REFERENCES `account_city` (`id`),
  CONSTRAINT `oferclubabstractuser_ptr_id_refs_id_316b1f69` FOREIGN KEY (`oferclubabstractuser_ptr_id`) REFERENCES `account_oferclubabstractuser` (`id`),
  CONSTRAINT `partner_id_refs_id_1b04cda4` FOREIGN KEY (`partner_id`) REFERENCES `account_partner` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_filial`
--

LOCK TABLES `account_filial` WRITE;
/*!40000 ALTER TABLE `account_filial` DISABLE KEYS */;
INSERT INTO `account_filial` VALUES (3,1,NULL,'','','','','','','');
/*!40000 ALTER TABLE `account_filial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_oferclubabstractuser`
--

DROP TABLE IF EXISTS `account_oferclubabstractuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_oferclubabstractuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `slug` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_oferclubabstractuser`
--

LOCK TABLES `account_oferclubabstractuser` WRITE;
/*!40000 ALTER TABLE `account_oferclubabstractuser` DISABLE KEYS */;
INSERT INTO `account_oferclubabstractuser` VALUES (1,'pbkdf2_sha256$12000$59XA12uTlZq2$SZJa7smALpUb68iIx10w8erdArPU40rrNsGEKo1CJJs=','2014-09-25 18:41:53',1,'adm','adm@adm.adm',1,1,'2014-09-17 23:02:07','adm'),(2,'pbkdf2_sha256$12000$2qvqoHebOku0$Rv6ydj6XlybAEX2kR8Se8rCGfNseq3UIhvwEsdC1urc=','2014-09-25 15:19:04',0,'Victor Lunaaa','victorluna22@gmail.com',0,1,'2014-09-17 23:42:20','victorlunaaa'),(3,'pbkdf2_sha256$12000$Oxst570ui00P$SVgCmWI6MDLEUpUjPEYUc9H83cJGD8OWtnQ4iZ3ctk4=','2014-09-18 00:23:59',0,'dasasd','adasd@dasdas.das',0,1,'2014-09-18 00:23:59','dasasd'),(4,'pbkdf2_sha256$12000$eBziIfBHgrno$oy06AvbXPvj/reu5Kcl1NlfNSxf3k7PDucjmKvmvOh8=','2014-09-18 00:30:56',0,'dasasdfd','sadasd@dasd.fsd',0,1,'2014-09-18 00:30:56','dasasdfd'),(5,'pbkdf2_sha256$12000$POZIfLTgDZRY$kQvymdqi8eY4/awFAQnE/Sp4zRu6JpM02BEHlIT8GEk=','2014-09-18 01:24:30',0,'teste','teste@tesee.asd',0,1,'2014-09-18 01:24:30','teste');
/*!40000 ALTER TABLE `account_oferclubabstractuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_oferclubabstractuser_groups`
--

DROP TABLE IF EXISTS `account_oferclubabstractuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_oferclubabstractuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `oferclubabstractuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oferclubabstractuser_id` (`oferclubabstractuser_id`,`group_id`),
  KEY `account_oferclubabstractuser_groups_23d603a2` (`oferclubabstractuser_id`),
  KEY `account_oferclubabstractuser_groups_5f412f9a` (`group_id`),
  CONSTRAINT `oferclubabstractuser_id_refs_id_5014f50c` FOREIGN KEY (`oferclubabstractuser_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_oferclubabstractuser_groups`
--

LOCK TABLES `account_oferclubabstractuser_groups` WRITE;
/*!40000 ALTER TABLE `account_oferclubabstractuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_oferclubabstractuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_oferclubabstractuser_user_permissions`
--

DROP TABLE IF EXISTS `account_oferclubabstractuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_oferclubabstractuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `oferclubabstractuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oferclubabstractuser_id` (`oferclubabstractuser_id`,`permission_id`),
  KEY `account_oferclubabstractuser_user_permissions_23d603a2` (`oferclubabstractuser_id`),
  KEY `account_oferclubabstractuser_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `oferclubabstractuser_id_refs_id_af16e411` FOREIGN KEY (`oferclubabstractuser_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_oferclubabstractuser_user_permissions`
--

LOCK TABLES `account_oferclubabstractuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `account_oferclubabstractuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_oferclubabstractuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_oferclubuser`
--

DROP TABLE IF EXISTS `account_oferclubuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_oferclubuser` (
  `oferclubabstractuser_ptr_id` int(11) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `credit` decimal(9,2) NOT NULL,
  PRIMARY KEY (`oferclubabstractuser_ptr_id`),
  KEY `account_oferclubuser_b376980e` (`city_id`),
  CONSTRAINT `city_id_refs_id_6f34b115` FOREIGN KEY (`city_id`) REFERENCES `account_city` (`id`),
  CONSTRAINT `oferclubabstractuser_ptr_id_refs_id_60f3a80f` FOREIGN KEY (`oferclubabstractuser_ptr_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_oferclubuser`
--

LOCK TABLES `account_oferclubuser` WRITE;
/*!40000 ALTER TABLE `account_oferclubuser` DISABLE KEYS */;
INSERT INTO `account_oferclubuser` VALUES (2,1,'M','1990-11-22',350.00),(5,NULL,'M','1990-11-22',0.00);
/*!40000 ALTER TABLE `account_oferclubuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_partner`
--

DROP TABLE IF EXISTS `account_partner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_partner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `cnpj` varchar(18) NOT NULL,
  `phone` varchar(20),
  `cellphone` varchar(20),
  `logo` varchar(100),
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_partner`
--

LOCK TABLES `account_partner` WRITE;
/*!40000 ALTER TABLE `account_partner` DISABLE KEYS */;
INSERT INTO `account_partner` VALUES (1,'walmart','walmart@walmart.com','walmart','1231231231','9898989898','9898989898',NULL);
/*!40000 ALTER TABLE `account_partner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_state`
--

DROP TABLE IF EXISTS `account_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `acronym` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_state`
--

LOCK TABLES `account_state` WRITE;
/*!40000 ALTER TABLE `account_state` DISABLE KEYS */;
INSERT INTO `account_state` VALUES (1,'Pernambuco','PE');
/*!40000 ALTER TABLE `account_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'parceiro');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (3,1,67),(1,1,72),(2,1,73),(4,1,75);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add usuário do Lua de Véu',6,'add_oferclubabstractuser'),(17,'Can change usuário do Lua de Véu',6,'change_oferclubabstractuser'),(18,'Can delete usuário do Lua de Véu',6,'delete_oferclubabstractuser'),(19,'Can add state',7,'add_state'),(20,'Can change state',7,'change_state'),(21,'Can delete state',7,'delete_state'),(22,'Can add city',8,'add_city'),(23,'Can change city',8,'change_city'),(24,'Can delete city',8,'delete_city'),(25,'Can add address',9,'add_address'),(26,'Can change address',9,'change_address'),(27,'Can delete address',9,'delete_address'),(28,'Can add Usuário',10,'add_oferclubuser'),(29,'Can change Usuário',10,'change_oferclubuser'),(30,'Can delete Usuário',10,'delete_oferclubuser'),(31,'Can add Parceiro',11,'add_partner'),(32,'Can change Parceiro',11,'change_partner'),(33,'Can delete Parceiro',11,'delete_partner'),(34,'Can add Filial',12,'add_filial'),(35,'Can change Filial',12,'change_filial'),(36,'Can delete Filial',12,'delete_filial'),(37,'Can add Afiliado',13,'add_affiliate'),(38,'Can change Afiliado',13,'change_affiliate'),(39,'Can delete Afiliado',13,'delete_affiliate'),(40,'Can add conta',14,'add_account'),(41,'Can change conta',14,'change_account'),(42,'Can delete conta',14,'delete_account'),(43,'Can add category',15,'add_category'),(44,'Can change category',15,'change_category'),(45,'Can delete category',15,'delete_category'),(46,'Can add offer',16,'add_offer'),(47,'Can change offer',16,'change_offer'),(48,'Can delete offer',16,'delete_offer'),(49,'Can add image',17,'add_image'),(50,'Can change image',17,'change_image'),(51,'Can delete image',17,'delete_image'),(52,'Can add option',18,'add_option'),(53,'Can change option',18,'change_option'),(54,'Can delete option',18,'delete_option'),(55,'Can add Pedido',19,'add_order'),(56,'Can change Pedido',19,'change_order'),(57,'Can delete Pedido',19,'delete_order'),(58,'Can add Cupom',20,'add_coupon'),(59,'Can change Cupom',20,'change_coupon'),(60,'Can delete Cupom',20,'delete_coupon'),(61,'Can view address',9,'view_address'),(62,'Can view Afiliado',13,'view_affiliate'),(63,'Can view category',15,'view_category'),(64,'Can view city',8,'view_city'),(65,'Can view conta',14,'view_account'),(66,'Can view content type',4,'view_contenttype'),(67,'Can view Cupom',20,'view_coupon'),(68,'Can view Filial',12,'view_filial'),(69,'Can view group',3,'view_group'),(70,'Can view image',17,'view_image'),(71,'Can view log entry',1,'view_logentry'),(72,'Can view offer',16,'view_offer'),(73,'Can view option',18,'view_option'),(74,'Can view Parceiro',11,'view_partner'),(75,'Can view Pedido',19,'view_order'),(76,'Can view permission',2,'view_permission'),(77,'Can view session',5,'view_session'),(78,'Can view state',7,'view_state'),(79,'Can view Usuário',10,'view_oferclubuser'),(80,'Can view usuário do Lua de Véu',6,'view_oferclubabstractuser'),(81,'Can add Bookmark',21,'add_bookmark'),(82,'Can change Bookmark',21,'change_bookmark'),(83,'Can delete Bookmark',21,'delete_bookmark'),(84,'Can add User Setting',23,'add_usersettings'),(85,'Can change User Setting',23,'change_usersettings'),(86,'Can delete User Setting',23,'delete_usersettings'),(87,'Can add User Widget',22,'add_userwidget'),(88,'Can change User Widget',22,'change_userwidget'),(89,'Can delete User Widget',22,'delete_userwidget'),(90,'Can view Bookmark',21,'view_bookmark'),(91,'Can view User Setting',23,'view_usersettings'),(92,'Can view User Widget',22,'view_userwidget'),(93,'Can add revision',25,'add_revision'),(94,'Can change revision',25,'change_revision'),(95,'Can delete revision',25,'delete_revision'),(96,'Can add version',24,'add_version'),(97,'Can change version',24,'change_version'),(98,'Can delete version',24,'delete_version'),(99,'Can view revision',25,'view_revision'),(100,'Can view version',24,'view_version'),(101,'Can add Operação',26,'add_operation'),(102,'Can change Operação',26,'change_operation'),(103,'Can delete Operação',26,'delete_operation'),(104,'Can view Operação',26,'view_operation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checkout_coupon`
--

DROP TABLE IF EXISTS `checkout_coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkout_coupon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_consumer` varchar(200),
  `code` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `is_consumed` tinyint(1) NOT NULL,
  `date_expiration` date NOT NULL,
  `date_consumed` datetime,
  `date_created` datetime NOT NULL,
  `address_id` int(11),
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `checkout_coupon_ea8e5d12` (`address_id`),
  KEY `checkout_coupon_69dfcb07` (`order_id`),
  CONSTRAINT `checkout_coupon_order_id_12712e0225504a11_fk_checkout_order_id` FOREIGN KEY (`order_id`) REFERENCES `checkout_order` (`id`),
  CONSTRAINT `checkout_coupo_address_id_295721fb3ad8b851_fk_account_address_id` FOREIGN KEY (`address_id`) REFERENCES `account_address` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkout_coupon`
--

LOCK TABLES `checkout_coupon` WRITE;
/*!40000 ALTER TABLE `checkout_coupon` DISABLE KEYS */;
INSERT INTO `checkout_coupon` VALUES (6,NULL,'0ab15f15f635ea096e4316c7be7ee6',1000.00,0,'2014-11-19',NULL,'2014-09-24 20:31:33',NULL,12),(7,NULL,'6fdfdbf7499e3644868490f404b715',1000.00,0,'2014-11-19',NULL,'2014-09-24 20:31:33',NULL,12),(8,NULL,'A7ECBBFAEC',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:35:39',NULL,13),(9,NULL,'66CF788B6815838E',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:36:15',NULL,14),(10,NULL,'51EDBCA7056667F6',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:37:10',NULL,15),(11,NULL,'A4941844035D7096',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:37:11',NULL,15),(12,NULL,'235D285A1EC1AC79',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:37:11',NULL,15),(13,NULL,'B25747F0FD9ENONE',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:40:37',NULL,17),(14,NULL,'A593CDC2A81DNONE',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:40:56',NULL,18),(15,NULL,'24E6C5F4661319',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:50:00',NULL,19),(16,NULL,'C9FAFC9B7C2920',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:50:13',NULL,20),(17,NULL,'5ED00A1B4C2F219',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:52:24',NULL,21),(18,NULL,'EBD8BF27B8A4220',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:52:40',NULL,22),(19,NULL,'BC5B995CC490234',1000.00,0,'2014-11-19',NULL,'2014-09-24 21:52:54',NULL,23),(20,NULL,'42904FF57C03246',1000.00,0,'2014-11-19',NULL,'2014-09-24 22:30:02',NULL,24),(21,NULL,'5F65BE670B45258',1000.00,0,'2014-11-19',NULL,'2014-09-25 17:37:08',NULL,25),(22,NULL,'60D6C2C0692B265',1000.00,0,'2014-11-19',NULL,'2014-09-25 17:41:40',NULL,26),(23,NULL,'BDE85235E262275',1000.00,0,'2014-11-19',NULL,'2014-09-25 17:45:56',NULL,27),(24,NULL,'F7652EA9DF7F284',1000.00,0,'2014-11-19',NULL,'2014-09-25 17:46:14',NULL,28);
/*!40000 ALTER TABLE `checkout_coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checkout_operation`
--

DROP TABLE IF EXISTS `checkout_operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkout_operation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_operation` tinyint(1) NOT NULL,
  `value` decimal(10,2) NOT NULL,
  `created_at` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `checkout_operation_e8701ad4` (`user_id`),
  CONSTRAINT `D2f17ec7181714dae74871a02549cd86` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubuser` (`oferclubabstractuser_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkout_operation`
--

LOCK TABLES `checkout_operation` WRITE;
/*!40000 ALTER TABLE `checkout_operation` DISABLE KEYS */;
INSERT INTO `checkout_operation` VALUES (1,1,100.00,'2014-09-25 17:37:08',2,''),(2,1,100.00,'2014-09-25 17:41:40',2,'CashBack'),(3,1,100.00,'2014-09-25 17:45:56',2,'CashBack'),(4,1,50.00,'2014-09-25 17:46:14',2,'CashBack');
/*!40000 ALTER TABLE `checkout_operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checkout_order`
--

DROP TABLE IF EXISTS `checkout_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkout_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total` decimal(10,2) NOT NULL,
  `status` smallint(5) unsigned,
  `purchase_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `option_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `checkout_order_e8701ad4` (`user_id`),
  KEY `checkout_order_28df3725` (`option_id`),
  CONSTRAINT `caf3285b361c230594d56dcb3de992a3` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubuser` (`oferclubabstractuser_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkout_order`
--

LOCK TABLES `checkout_order` WRITE;
/*!40000 ALTER TABLE `checkout_order` DISABLE KEYS */;
INSERT INTO `checkout_order` VALUES (12,2000.00,2,'2014-09-24 20:31:33',2,1,2),(13,1000.00,2,'2014-09-24 21:35:39',2,1,1),(14,1000.00,2,'2014-09-24 21:36:15',2,1,1),(15,3000.00,2,'2014-09-24 21:37:10',2,1,3),(16,1000.00,2,'2014-09-24 21:39:24',2,1,1),(17,1000.00,2,'2014-09-24 21:40:37',2,1,1),(18,1000.00,2,'2014-09-24 21:40:56',2,1,1),(19,1000.00,2,'2014-09-24 21:50:00',2,1,1),(20,1000.00,2,'2014-09-24 21:50:13',2,1,1),(21,1000.00,2,'2014-09-24 21:52:24',2,1,1),(22,1000.00,2,'2014-09-24 21:52:40',2,1,1),(23,1000.00,2,'2014-09-24 21:52:54',2,1,1),(24,1000.00,2,'2014-09-24 22:30:02',2,1,1),(25,1000.00,2,'2014-09-25 17:37:07',2,1,1),(26,1000.00,2,'2014-09-25 17:41:40',2,1,1),(27,1000.00,2,'2014-09-25 17:45:55',2,1,1),(28,1000.00,2,'2014-09-25 17:46:14',2,1,1);
/*!40000 ALTER TABLE `checkout_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `djan_user_id_52fdd58701c5f563_fk_account_oferclubabstractuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-09-18 00:23:53','1','walmart (walmart@walmart.com)',1,'',11,1),(2,'2014-09-18 00:23:59','3','dasasd (adasd@dasdas.das)',1,'',12,1),(3,'2014-09-18 00:30:36','3','dasasd (adasd@dasdas.das)',2,'Nenhum campo modificado.',12,1),(4,'2014-09-18 00:30:56','4','dasasdfd (sadasd@dasd.fsd)',1,'',13,1),(5,'2014-09-18 00:31:35','4','dasasdfd (sadasd@dasd.fsd)',2,'Nenhum campo modificado.',13,1),(6,'2014-09-18 20:30:32','1','Produto',1,'',15,1),(7,'2014-09-18 20:30:41','2','Serviço',1,'',15,1),(8,'2014-09-18 20:30:45','3','Viagens',1,'',15,1),(9,'2014-09-18 20:31:08','4','Fast Food',1,'',15,1),(10,'2014-09-19 18:54:28','2','Victor Luna - 1000.00',1,'',19,1),(11,'2014-09-19 18:57:07','1','teste',1,'',16,1),(12,'2014-09-19 19:01:29','1','victor - dsadasdasda',1,'',20,1),(13,'2014-09-22 14:06:12','1','teste',2,'Modificado city. Adicionado Imagem \"oferta/tenis_2Lwca3y.jpg\"',16,1),(14,'2014-09-22 21:10:34','1','teste',2,'Nenhum campo modificado.',16,1),(15,'2014-09-25 17:21:52','1','teste',2,'Modificado percent_cashback.',16,1),(16,'2014-09-25 17:46:07','1','teste',2,'Modificado percent_cashback.',16,1),(17,'2014-09-25 18:46:17','1','parceiro',1,'',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'usuário do Lua de Véu','account','oferclubabstractuser'),(7,'state','account','state'),(8,'city','account','city'),(9,'address','account','address'),(10,'Usuário','account','oferclubuser'),(11,'Parceiro','account','partner'),(12,'Filial','account','filial'),(13,'Afiliado','account','affiliate'),(14,'conta','account','account'),(15,'category','offer','category'),(16,'offer','offer','offer'),(17,'image','offer','image'),(18,'option','offer','option'),(19,'Pedido','checkout','order'),(20,'Cupom','checkout','coupon'),(21,'Bookmark','xadmin','bookmark'),(22,'User Widget','xadmin','userwidget'),(23,'User Setting','xadmin','usersettings'),(24,'version','reversion','version'),(25,'revision','reversion','revision'),(26,'Operação','checkout','operation');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2014-09-17 23:00:10'),(2,'admin','0001_initial','2014-09-17 23:00:11'),(3,'auth','0001_initial','2014-09-17 23:00:13'),(4,'sessions','0001_initial','2014-09-17 23:00:14'),(5,'account','0001_initial','2014-09-17 23:01:14'),(6,'account','0002_auto_20140918_0030','2014-09-18 00:30:26'),(8,'offer','0001_initial','2014-09-18 20:19:34'),(9,'offer','0002_offer_title','2014-09-18 20:22:41'),(10,'offer','0003_auto_20140918_2048','2014-09-18 20:49:04'),(11,'offer','0004_auto_20140918_1843','2014-09-18 21:43:53'),(12,'offer','0005_auto_20140919_1552','2014-09-19 18:53:18'),(13,'checkout','0001_initial','2014-09-19 18:53:20'),(14,'checkout','0002_auto_20140919_1601','2014-09-19 19:01:20'),(15,'checkout','0003_coupon_order','2014-09-19 19:15:48'),(16,'offer','0006_auto_20140919_1717','2014-09-19 20:17:57'),(17,'reversion','0001_initial','2014-09-19 20:17:59'),(18,'offer','0007_remove_offer_percent_by_affiliate','2014-09-22 13:44:13'),(19,'account','0003_affiliate_percent','2014-09-22 13:44:28'),(20,'account','0004_partner_logo','2014-09-22 14:10:38'),(21,'offer','0008_auto_20140922_1212','2014-09-22 15:12:50'),(22,'checkout','0004_auto_20140922_1212','2014-09-22 18:22:46'),(23,'checkout','0005_operation','2014-09-22 18:22:51'),(24,'checkout','0006_operation_total','2014-09-22 18:28:27'),(25,'offer','0009_offer_slug','2014-09-22 21:05:52'),(26,'checkout','0007_auto_20140922_1929','2014-09-22 22:29:17'),(27,'checkout','0008_auto_20140924_1716','2014-09-24 20:16:34'),(28,'offer','0010_auto_20140925_1418','2014-09-25 17:18:34'),(29,'checkout','0009_remove_operation_total','2014-09-25 17:28:07'),(30,'checkout','0010_operation_description','2014-09-25 17:39:00');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('15utrrxxhcq4t0zzvpm1m1lftokczywn','NWVmODRiM2M5MGY2ZDBiN2Y0N2I3OTNiYTZiYjI2NzIwMzBlMjkwODp7fQ==','2014-10-02 00:48:23'),('4femqpzesi6f5e0riq19tumibkp1dsiv','MDk5Y2NjZWExMGFmMjAyMWI1MTVkZWJjN2VhYjVmOGNkNDNkYzkzMjp7Il9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9oYXNoIjoiYzFhODU5MWYxMWVjNzQ2MmRlMWE0MGYzNzY2MDc1Njg4MjI4YTRmYyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-10-07 18:47:28'),('8k308v5iq0v8a0xxvsg0115xacgqnvui','OTlkMjVkZTcxMTJhZGVmMWU4YjgyNDk5ZjUxYzg2NDdhZDlkY2I4Mjp7Il9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9oYXNoIjoiYjk3NmEwNjE1YWU4MDAwMDM0MDA0NGUyYjljNzg0NjJhMTRlMDQ0MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFjY291bnQuYmFja2VuZHMuQWNjb3VudHNCYWNrZW5kLkFjY291bnRzQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9','2014-10-06 22:19:12'),('9tih3hv3qcoq38pylhwo7lx3eazpynpx','ZTlhNDU5NTUyNjc5MTNhMDRiNGFjZTI0NzZmMDAzMTU3YmVkZDU5Mzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiTElTVF9RVUVSWSI6W1siYXV0aCIsImdyb3VwIl0sIiJdLCJfYXV0aF91c2VyX2hhc2giOiJjMWE4NTkxZjExZWM3NDYyZGUxYTQwZjM3NjYwNzU2ODgyMjhhNGZjIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-10-03 20:46:00'),('csm651f1lu17twwqbkndzujqbfhlem4o','OTlkMjVkZTcxMTJhZGVmMWU4YjgyNDk5ZjUxYzg2NDdhZDlkY2I4Mjp7Il9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9oYXNoIjoiYjk3NmEwNjE1YWU4MDAwMDM0MDA0NGUyYjljNzg0NjJhMTRlMDQ0MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFjY291bnQuYmFja2VuZHMuQWNjb3VudHNCYWNrZW5kLkFjY291bnRzQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9','2014-10-08 18:46:33'),('ensuhkhtdoyn7n8bsoqdw5jpezeyg1pn','MDBjYTNjYTljNzc4NjUwMTdhNzIwMTM3ZjQ4MDM5YzE5ZDgwZTk3Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImMxYTg1OTFmMTFlYzc0NjJkZTFhNDBmMzc2NjA3NTY4ODIyOGE0ZmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2014-10-02 01:24:51'),('gfgap5sb3dx082vv3jw73bjvwadbz040','MDBjYTNjYTljNzc4NjUwMTdhNzIwMTM3ZjQ4MDM5YzE5ZDgwZTk3Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImMxYTg1OTFmMTFlYzc0NjJkZTFhNDBmMzc2NjA3NTY4ODIyOGE0ZmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2014-10-08 20:03:28'),('j6s82d3k0vtdj0hugrgddnwqlf89g0uu','MDBjYTNjYTljNzc4NjUwMTdhNzIwMTM3ZjQ4MDM5YzE5ZDgwZTk3Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImMxYTg1OTFmMTFlYzc0NjJkZTFhNDBmMzc2NjA3NTY4ODIyOGE0ZmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2014-10-09 18:41:53');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer_category`
--

DROP TABLE IF EXISTS `offer_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer_category`
--

LOCK TABLES `offer_category` WRITE;
/*!40000 ALTER TABLE `offer_category` DISABLE KEYS */;
INSERT INTO `offer_category` VALUES (1,'Produto'),(2,'Serviço'),(3,'Viagens'),(4,'Fast Food');
/*!40000 ALTER TABLE `offer_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer_image`
--

DROP TABLE IF EXISTS `offer_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `offer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `offer_image_bf98d991` (`offer_id`),
  CONSTRAINT `offer_image_offer_id_2f7fed8543d8fb2_fk_offer_offer_id` FOREIGN KEY (`offer_id`) REFERENCES `offer_offer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer_image`
--

LOCK TABLES `offer_image` WRITE;
/*!40000 ALTER TABLE `offer_image` DISABLE KEYS */;
INSERT INTO `offer_image` VALUES (4,'oferta/tenis_2Lwca3y.jpg',1);
/*!40000 ALTER TABLE `offer_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer_offer`
--

DROP TABLE IF EXISTS `offer_offer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer_offer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `highlight` tinyint(1) NOT NULL,
  `highlight_image` varchar(100) NOT NULL,
  `bought` int(11) NOT NULL,
  `bought_virtual` int(11) NOT NULL,
  `max_by_user` int(11) DEFAULT NULL,
  `percent_by_site` decimal(10,2) NOT NULL,
  `description` longtext NOT NULL,
  `regulation` longtext NOT NULL,
  `date_created` datetime NOT NULL,
  `affiliate_id` int(11),
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `percent_cashback` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `offer_offer_afb2f3b6` (`affiliate_id`),
  CONSTRAINT `D2d2ed30c2e8132ef2d86bac13088710` FOREIGN KEY (`affiliate_id`) REFERENCES `account_affiliate` (`oferclubabstractuser_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer_offer`
--

LOCK TABLES `offer_offer` WRITE;
/*!40000 ALTER TABLE `offer_offer` DISABLE KEYS */;
INSERT INTO `offer_offer` VALUES (1,1,'oferta/mulher.jpg',0,0,10,20.00,'<p>sadasddasd</p>','<p>dasdasdasdasd</p>','2014-09-19 18:57:07',4,'teste','teste',5.00);
/*!40000 ALTER TABLE `offer_offer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer_offer_city`
--

DROP TABLE IF EXISTS `offer_offer_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer_offer_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `offer_id` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `offer_id` (`offer_id`,`city_id`),
  KEY `offer_offer_city_bf98d991` (`offer_id`),
  KEY `offer_offer_city_c7141997` (`city_id`),
  CONSTRAINT `offer_offer_city_city_id_2fc517d1d8ff8eae_fk_account_city_id` FOREIGN KEY (`city_id`) REFERENCES `account_city` (`id`),
  CONSTRAINT `offer_offer_city_offer_id_283273ad3d6559b4_fk_offer_offer_id` FOREIGN KEY (`offer_id`) REFERENCES `offer_offer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer_offer_city`
--

LOCK TABLES `offer_offer_city` WRITE;
/*!40000 ALTER TABLE `offer_offer_city` DISABLE KEYS */;
INSERT INTO `offer_offer_city` VALUES (19,1,1),(20,1,2),(21,1,3);
/*!40000 ALTER TABLE `offer_offer_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer_option`
--

DROP TABLE IF EXISTS `offer_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer_option` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `old_price` decimal(10,2) DEFAULT NULL,
  `new_price` decimal(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `date_expiration` date NOT NULL,
  `date_created` datetime NOT NULL,
  `filial_id` int(11) NOT NULL,
  `offer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `offer_option_ce4d2499` (`filial_id`),
  KEY `offer_option_bf98d991` (`offer_id`),
  CONSTRAINT `D2385b7329027ab0014f76d59da889f6` FOREIGN KEY (`filial_id`) REFERENCES `account_filial` (`oferclubabstractuser_ptr_id`),
  CONSTRAINT `offer_option_offer_id_6e0b959b1433a2cd_fk_offer_offer_id` FOREIGN KEY (`offer_id`) REFERENCES `offer_offer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer_option`
--

LOCK TABLES `offer_option` WRITE;
/*!40000 ALTER TABLE `offer_option` DISABLE KEYS */;
INSERT INTO `offer_option` VALUES (1,'teste boa vista',2000.00,1000.00,10,'2014-09-19 18:56:54','2014-10-19 18:56:56','2014-11-19','2014-09-19 18:57:07',3,1);
/*!40000 ALTER TABLE `offer_option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reversion_revision`
--

DROP TABLE IF EXISTS `reversion_revision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reversion_revision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_slug` varchar(200) NOT NULL,
  `date_created` datetime NOT NULL,
  `comment` longtext NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reversion_revision_b16b0f06` (`manager_slug`),
  KEY `reversion_revision_c69e55a4` (`date_created`),
  KEY `reversion_revision_e8701ad4` (`user_id`),
  CONSTRAINT `reve_user_id_53d027e45b2ec55e_fk_account_oferclubabstractuser_id` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reversion_revision`
--

LOCK TABLES `reversion_revision` WRITE;
/*!40000 ALTER TABLE `reversion_revision` DISABLE KEYS */;
/*!40000 ALTER TABLE `reversion_revision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reversion_version`
--

DROP TABLE IF EXISTS `reversion_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reversion_version` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` longtext NOT NULL,
  `object_id_int` int(11) DEFAULT NULL,
  `format` varchar(255) NOT NULL,
  `serialized_data` longtext NOT NULL,
  `object_repr` longtext NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `revision_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reversion_version_0c9ba3a3` (`object_id_int`),
  KEY `reversion_version_417f1b1c` (`content_type_id`),
  KEY `reversion_version_5de09a8d` (`revision_id`),
  CONSTRAINT `reversion_v_revision_id_48ec3744916a950_fk_reversion_revision_id` FOREIGN KEY (`revision_id`) REFERENCES `reversion_revision` (`id`),
  CONSTRAINT `revers_content_type_id_c01a11926d4c4a9_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reversion_version`
--

LOCK TABLES `reversion_version` WRITE;
/*!40000 ALTER TABLE `reversion_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `reversion_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_bookmark`
--

DROP TABLE IF EXISTS `xadmin_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `url_name` varchar(64) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_6340c63c` (`user_id`),
  KEY `xadmin_bookmark_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_af66fd92` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_736683e0` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_bookmark`
--

LOCK TABLES `xadmin_bookmark` WRITE;
/*!40000 ALTER TABLE `xadmin_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_usersettings`
--

DROP TABLE IF EXISTS `xadmin_usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_abf4e307` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_usersettings`
--

LOCK TABLES `xadmin_usersettings` WRITE;
/*!40000 ALTER TABLE `xadmin_usersettings` DISABLE KEYS */;
INSERT INTO `xadmin_usersettings` VALUES (1,1,'dashboard:home:pos','');
/*!40000 ALTER TABLE `xadmin_usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_userwidget`
--

DROP TABLE IF EXISTS `xadmin_userwidget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_d31ca3f8` FOREIGN KEY (`user_id`) REFERENCES `account_oferclubabstractuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_userwidget`
--

LOCK TABLES `xadmin_userwidget` WRITE;
/*!40000 ALTER TABLE `xadmin_userwidget` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_userwidget` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-09-25 19:34:58
