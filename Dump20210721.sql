-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: messaging_platform
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'system');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63),(64,1,64),(65,1,65),(66,1,66),(67,1,67),(68,1,68),(69,1,69),(70,1,70),(71,1,71),(72,1,72),(73,1,73),(74,1,74),(75,1,75),(76,1,76),(77,1,77),(78,1,78),(79,1,79),(80,1,80),(81,1,81),(82,1,82),(83,1,83),(84,1,84),(85,1,85),(86,1,86),(87,1,87),(88,1,88),(89,1,89),(90,1,90),(91,1,91),(92,1,92),(93,1,93),(94,1,94),(95,1,95),(96,1,96),(97,1,97),(98,1,98),(99,1,99),(100,1,100),(101,1,101),(102,1,102),(103,1,103),(104,1,104),(105,1,105),(106,1,106),(107,1,107),(108,1,108),(109,1,109),(110,1,110),(111,1,111),(112,1,112),(113,1,113),(114,1,114),(115,1,115),(116,1,116),(117,1,117),(118,1,118),(119,1,119),(120,1,120),(121,1,121),(122,1,122),(123,1,123),(124,1,124),(125,1,125),(126,1,126),(127,1,127),(128,1,128),(129,1,129),(130,1,130),(131,1,131),(132,1,132),(133,1,133),(134,1,134),(135,1,135),(136,1,136),(137,1,137),(138,1,138),(139,1,139),(140,1,140),(141,1,141),(142,1,142),(143,1,143),(144,1,144),(145,1,145),(146,1,146),(147,1,147),(148,1,148),(149,1,149),(150,1,150),(151,1,151),(152,1,152),(153,1,153),(154,1,154),(155,1,155),(156,1,156),(157,1,157),(158,1,158),(159,1,159);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=460 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add EndUserFacebook',7,'add_enduserfacebook'),(20,'Can change EndUserFacebook',7,'change_enduserfacebook'),(21,'Can delete EndUserFacebook',7,'delete_enduserfacebook'),(22,'Can add Vendor',8,'add_vendor'),(23,'Can change Vendor',8,'change_vendor'),(24,'Can delete Vendor',8,'delete_vendor'),(25,'Can add EndUserLINE',9,'add_enduserline'),(26,'Can change EndUserLINE',9,'change_enduserline'),(27,'Can delete EndUserLINE',9,'delete_enduserline'),(28,'Can add VendorBranch',10,'add_vendorbranch'),(29,'Can change VendorBranch',10,'change_vendorbranch'),(30,'Can delete VendorBranch',10,'delete_vendorbranch'),(31,'Can add Service',11,'add_service'),(32,'Can change Service',11,'change_service'),(33,'Can delete Service',11,'delete_service'),(34,'Can add EndUser',12,'add_enduser'),(35,'Can change EndUser',12,'change_enduser'),(36,'Can delete EndUser',12,'delete_enduser'),(37,'Can add TagCategory',13,'add_tagcategory'),(38,'Can change TagCategory',13,'change_tagcategory'),(39,'Can delete TagCategory',13,'delete_tagcategory'),(40,'Can add ReservationHistory',14,'add_reservationhistory'),(41,'Can change ReservationHistory',14,'change_reservationhistory'),(42,'Can delete ReservationHistory',14,'delete_reservationhistory'),(43,'Can add VendorUser',15,'add_vendoruser'),(44,'Can change VendorUser',15,'change_vendoruser'),(45,'Can delete VendorUser',15,'delete_vendoruser'),(46,'Can add Reservation',16,'add_reservation'),(47,'Can change Reservation',16,'change_reservation'),(48,'Can delete Reservation',16,'delete_reservation'),(49,'Can add EndUserStory',17,'add_enduserstory'),(50,'Can change EndUserStory',17,'change_enduserstory'),(51,'Can delete EndUserStory',17,'delete_enduserstory'),(52,'Can add Payload',18,'add_payload'),(53,'Can change Payload',18,'change_payload'),(54,'Can delete Payload',18,'delete_payload'),(55,'Can add EndUserState',19,'add_enduserstate'),(56,'Can change EndUserState',19,'change_enduserstate'),(57,'Can delete EndUserState',19,'delete_enduserstate'),(58,'Can add MessagingAPIType',20,'add_messagingapitype'),(59,'Can change MessagingAPIType',20,'change_messagingapitype'),(60,'Can delete MessagingAPIType',20,'delete_messagingapitype'),(61,'Can add AutomessageController',21,'add_automessagecontroller'),(62,'Can change AutomessageController',21,'change_automessagecontroller'),(63,'Can delete AutomessageController',21,'delete_automessagecontroller'),(64,'Can add AutomessageTrigger',22,'add_automessagetrigger'),(65,'Can change AutomessageTrigger',22,'change_automessagetrigger'),(66,'Can delete AutomessageTrigger',22,'delete_automessagetrigger'),(67,'Can add AutomessageCondition',23,'add_automessagecondition'),(68,'Can change AutomessageCondition',23,'change_automessagecondition'),(69,'Can delete AutomessageCondition',23,'delete_automessagecondition'),(70,'Can add ManualMessageController',24,'add_manualmessagecontroller'),(71,'Can change ManualMessageController',24,'change_manualmessagecontroller'),(72,'Can delete ManualMessageController',24,'delete_manualmessagecontroller'),(73,'Can add ManualMessageOverview',25,'add_manualmessageoverview'),(74,'Can change ManualMessageOverview',25,'change_manualmessageoverview'),(75,'Can delete ManualMessageOverview',25,'delete_manualmessageoverview'),(76,'Can add AutoMessageHistory',26,'add_automessagehistory'),(77,'Can change AutoMessageHistory',26,'change_automessagehistory'),(78,'Can delete AutoMessageHistory',26,'delete_automessagehistory'),(79,'Can add AutoMessageType',27,'add_automessagetype'),(80,'Can change AutoMessageType',27,'change_automessagetype'),(81,'Can delete AutoMessageType',27,'delete_automessagetype'),(82,'Can add ManualMessageHistory',28,'add_manualmessagehistory'),(83,'Can change ManualMessageHistory',28,'change_manualmessagehistory'),(84,'Can delete ManualMessageHistory',28,'delete_manualmessagehistory'),(85,'Can add EndUserAutoMessage',29,'add_enduserautomessage'),(86,'Can change EndUserAutoMessage',29,'change_enduserautomessage'),(87,'Can delete EndUserAutoMessage',29,'delete_enduserautomessage'),(88,'Can add VendorReservationSettings',30,'add_vendorreservationsettings'),(89,'Can change VendorReservationSettings',30,'change_vendorreservationsettings'),(90,'Can delete VendorReservationSettings',30,'delete_vendorreservationsettings'),(91,'Can add Tag',31,'add_tag'),(92,'Can change Tag',31,'change_tag'),(93,'Can delete Tag',31,'delete_tag'),(94,'Can add Tagged Item',32,'add_taggeditem'),(95,'Can change Tagged Item',32,'change_taggeditem'),(96,'Can delete Tagged Item',32,'delete_taggeditem'),(97,'Can add a model',33,'add_amodel'),(98,'Can change a model',33,'change_amodel'),(99,'Can delete a model',33,'delete_amodel'),(100,'Can add EndUserStoryHistory',34,'add_enduserstoryhistory'),(101,'Can change EndUserStoryHistory',34,'change_enduserstoryhistory'),(102,'Can delete EndUserStoryHistory',34,'delete_enduserstoryhistory'),(103,'Can add EndUserState',35,'add_todoactionstatus'),(104,'Can change EndUserState',35,'change_todoactionstatus'),(105,'Can delete EndUserState',35,'delete_todoactionstatus'),(106,'Can add ReservationEvent',36,'add_reservationevent'),(107,'Can change ReservationEvent',36,'change_reservationevent'),(108,'Can delete ReservationEvent',36,'delete_reservationevent'),(109,'Can add Event',37,'add_event'),(110,'Can change Event',37,'change_event'),(111,'Can delete Event',37,'delete_event'),(112,'Can add EventCategory',38,'add_eventcategory'),(113,'Can change EventCategory',38,'change_eventcategory'),(114,'Can delete EventCategory',38,'delete_eventcategory'),(115,'Can add EventReservation',39,'add_eventreservation'),(116,'Can change EventReservation',39,'change_eventreservation'),(117,'Can delete EventReservation',39,'delete_eventreservation'),(118,'Can add EventReservationStatus',40,'add_eventreservationstatus'),(119,'Can change EventReservationStatus',40,'change_eventreservationstatus'),(120,'Can delete EventReservationStatus',40,'delete_eventreservationstatus'),(121,'Can add VendorEventSettings',41,'add_vendoreventsettings'),(122,'Can change VendorEventSettings',41,'change_vendoreventsettings'),(123,'Can delete VendorEventSettings',41,'delete_vendoreventsettings'),(124,'Can add Tag',42,'add_tag'),(125,'Can change Tag',42,'change_tag'),(126,'Can delete Tag',42,'delete_tag'),(127,'Can add MessageStatus',43,'add_messagestatus'),(128,'Can change MessageStatus',43,'change_messagestatus'),(129,'Can delete MessageStatus',43,'delete_messagestatus'),(130,'Can add EndUserStoryTemplate',44,'add_enduserstorytemplate'),(131,'Can change EndUserStoryTemplate',44,'change_enduserstorytemplate'),(132,'Can delete EndUserStoryTemplate',44,'delete_enduserstorytemplate'),(133,'Can add EndUserStoryTemplateCategory',45,'add_enduserstorytemplatecategory'),(134,'Can change EndUserStoryTemplateCategory',45,'change_enduserstorytemplatecategory'),(135,'Can delete EndUserStoryTemplateCategory',45,'delete_enduserstorytemplatecategory'),(136,'Can add WorkerSQSStatus',46,'add_workersqsstatus'),(137,'Can change WorkerSQSStatus',46,'change_workersqsstatus'),(138,'Can delete WorkerSQSStatus',46,'delete_workersqsstatus'),(139,'Can add EndUserSequenceState',47,'add_endusersequencestate'),(140,'Can change EndUserSequenceState',47,'change_endusersequencestate'),(141,'Can delete EndUserSequenceState',47,'delete_endusersequencestate'),(142,'Can add MessageSequence',48,'add_messagesequence'),(143,'Can change MessageSequence',48,'change_messagesequence'),(144,'Can delete MessageSequence',48,'delete_messagesequence'),(145,'Can add MessageBlock',49,'add_messageblock'),(146,'Can change MessageBlock',49,'change_messageblock'),(147,'Can delete MessageBlock',49,'delete_messageblock'),(148,'Can add Todo',50,'add_todo'),(149,'Can change Todo',50,'change_todo'),(150,'Can delete Todo',50,'delete_todo'),(151,'Can add TmpEntry',51,'add_tmpentry'),(152,'Can change TmpEntry',51,'change_tmpentry'),(153,'Can delete TmpEntry',51,'delete_tmpentry'),(154,'Can add Affiliate',52,'add_affiliate'),(155,'Can change Affiliate',52,'change_affiliate'),(156,'Can delete Affiliate',52,'delete_affiliate'),(157,'Can add TmpEntry',53,'add_tmpregistrationentry'),(158,'Can change TmpEntry',53,'change_tmpregistrationentry'),(159,'Can delete TmpEntry',53,'delete_tmpregistrationentry'),(160,'Can add test model',54,'add_testmodel'),(161,'Can change test model',54,'change_testmodel'),(162,'Can delete test model',54,'delete_testmodel'),(163,'Can add EndUserContactChat',55,'add_endusercontactchat'),(164,'Can change EndUserContactChat',55,'change_endusercontactchat'),(165,'Can delete EndUserContactChat',55,'delete_endusercontactchat'),(166,'Can add SummaryLogEndUser',56,'add_summarylogendusers'),(167,'Can change SummaryLogEndUser',56,'change_summarylogendusers'),(168,'Can delete SummaryLogEndUser',56,'delete_summarylogendusers'),(169,'Can add SummaryLogVendorUser',57,'add_summarylogvendorusers'),(170,'Can change SummaryLogVendorUser',57,'change_summarylogvendorusers'),(171,'Can delete SummaryLogVendorUser',57,'delete_summarylogvendorusers'),(172,'Can add event_start_dt',58,'add_logshistory'),(173,'Can change event_start_dt',58,'change_logshistory'),(174,'Can delete event_start_dt',58,'delete_logshistory'),(175,'Can add document',59,'add_document'),(176,'Can change document',59,'change_document'),(177,'Can delete document',59,'delete_document'),(178,'Can add VendorPlan',60,'add_vendorplan'),(179,'Can change VendorPlan',60,'change_vendorplan'),(180,'Can delete VendorPlan',60,'delete_vendorplan'),(181,'Can add VendorUser',61,'add_vendoruser'),(182,'Can change VendorUser',61,'change_vendoruser'),(183,'Can delete VendorUser',61,'delete_vendoruser'),(184,'Can add VendorService',62,'add_vendorservice'),(185,'Can change VendorService',62,'change_vendorservice'),(186,'Can delete VendorService',62,'delete_vendorservice'),(187,'Can add Service',63,'add_service'),(188,'Can change Service',63,'change_service'),(189,'Can delete Service',63,'delete_service'),(190,'Can add Plan',64,'add_plan'),(191,'Can change Plan',64,'change_plan'),(192,'Can delete Plan',64,'delete_plan'),(193,'Can add NotificationSetting',65,'add_notificationsetting'),(194,'Can change NotificationSetting',65,'change_notificationsetting'),(195,'Can delete NotificationSetting',65,'delete_notificationsetting'),(196,'Can add NotificationService',66,'add_notificationservice'),(197,'Can change NotificationService',66,'change_notificationservice'),(198,'Can delete NotificationService',66,'delete_notificationservice'),(199,'Can add CouponType',67,'add_coupontype'),(200,'Can change CouponType',67,'change_coupontype'),(201,'Can delete CouponType',67,'delete_coupontype'),(202,'Can add NotificationService',68,'add_coupon'),(203,'Can change NotificationService',68,'change_coupon'),(204,'Can delete NotificationService',68,'delete_coupon'),(205,'Can add Question',69,'add_question'),(206,'Can change Question',69,'change_question'),(207,'Can delete Question',69,'delete_question'),(208,'Can add Questionnaire',70,'add_questionnaire'),(209,'Can change Questionnaire',70,'change_questionnaire'),(210,'Can delete Questionnaire',70,'delete_questionnaire'),(211,'Can add Questionnaire Question',71,'add_questionnairequestion'),(212,'Can change Questionnaire Question',71,'change_questionnairequestion'),(213,'Can delete Questionnaire Question',71,'delete_questionnairequestion'),(214,'Can add QuestionType',72,'add_questiontype'),(215,'Can change QuestionType',72,'change_questiontype'),(216,'Can delete QuestionType',72,'delete_questiontype'),(217,'Can add EndUserQuestionnaire',73,'add_enduserquestionnaire'),(218,'Can change EndUserQuestionnaire',73,'change_enduserquestionnaire'),(219,'Can delete EndUserQuestionnaire',73,'delete_enduserquestionnaire'),(220,'Can add Response',74,'add_response'),(221,'Can change Response',74,'change_response'),(222,'Can delete Response',74,'delete_response'),(223,'Can add SenbayUser',75,'add_senbayuser'),(224,'Can change SenbayUser',75,'change_senbayuser'),(225,'Can delete SenbayUser',75,'delete_senbayuser'),(226,'Can add VendorBusinessPartner',76,'add_vendorbusinesspartner'),(227,'Can change VendorBusinessPartner',76,'change_vendorbusinesspartner'),(228,'Can delete VendorBusinessPartner',76,'delete_vendorbusinesspartner'),(229,'Can add VendorBusinessPartnerTag',77,'add_vendorbusinesspartnertag'),(230,'Can change VendorBusinessPartnerTag',77,'change_vendorbusinesspartnertag'),(231,'Can delete VendorBusinessPartnerTag',77,'delete_vendorbusinesspartnertag'),(232,'Can add Message',78,'add_message'),(233,'Can change Message',78,'change_message'),(234,'Can delete Message',78,'delete_message'),(235,'Can add MaTriggerType',79,'add_matriggertype'),(236,'Can change MaTriggerType',79,'change_matriggertype'),(237,'Can delete MaTriggerType',79,'delete_matriggertype'),(238,'Can add MaTrigger',80,'add_matrigger'),(239,'Can change MaTrigger',80,'change_matrigger'),(240,'Can delete MaTrigger',80,'delete_matrigger'),(241,'Can add CouponClaim',81,'add_couponclaim'),(242,'Can change CouponClaim',81,'change_couponclaim'),(243,'Can delete CouponClaim',81,'delete_couponclaim'),(244,'Can add Product',82,'add_product'),(245,'Can change Product',82,'change_product'),(246,'Can delete Product',82,'delete_product'),(247,'Can add ProductCategory',83,'add_productcategory'),(248,'Can change ProductCategory',83,'change_productcategory'),(249,'Can delete ProductCategory',83,'delete_productcategory'),(250,'Can add Receiving History',84,'add_receivinghistory'),(251,'Can change Receiving History',84,'change_receivinghistory'),(252,'Can delete Receiving History',84,'delete_receivinghistory'),(253,'Can add Shipping History',85,'add_shippinghistory'),(254,'Can change Shipping History',85,'change_shippinghistory'),(255,'Can delete Shipping History',85,'delete_shippinghistory'),(256,'Can add Stock',86,'add_stock'),(257,'Can change Stock',86,'change_stock'),(258,'Can delete Stock',86,'delete_stock'),(259,'Can add StockSpace',87,'add_stockspace'),(260,'Can change StockSpace',87,'change_stockspace'),(261,'Can delete StockSpace',87,'delete_stockspace'),(262,'Can add Questionnaire Template',88,'add_questionnairetemplate'),(263,'Can change Questionnaire Template',88,'change_questionnairetemplate'),(264,'Can delete Questionnaire Template',88,'delete_questionnairetemplate'),(265,'Can add Questionnaire Template Question',89,'add_questionnairetemplatequestion'),(266,'Can change Questionnaire Template Question',89,'change_questionnairetemplatequestion'),(267,'Can delete Questionnaire Template Question',89,'delete_questionnairetemplatequestion'),(268,'Can add Business',90,'add_business'),(269,'Can change Business',90,'change_business'),(270,'Can delete Business',90,'delete_business'),(271,'Can add BusinessPlan',91,'add_businessplan'),(272,'Can change BusinessPlan',91,'change_businessplan'),(273,'Can delete BusinessPlan',91,'delete_businessplan'),(274,'Can add VendorUser',92,'add_vendoruser'),(275,'Can change VendorUser',92,'change_vendoruser'),(276,'Can delete VendorUser',92,'delete_vendoruser'),(277,'Can add NotificationHistory',93,'add_notificationhistory'),(278,'Can change NotificationHistory',93,'change_notificationhistory'),(279,'Can delete NotificationHistory',93,'delete_notificationhistory'),(280,'Can add Notification',94,'add_notification'),(281,'Can change Notification',94,'change_notification'),(282,'Can delete Notification',94,'delete_notification'),(283,'Can add MaTrigger',95,'add_matrigger'),(284,'Can change MaTrigger',95,'change_matrigger'),(285,'Can delete MaTrigger',95,'delete_matrigger'),(286,'Can add Message',96,'add_message'),(287,'Can change Message',96,'change_message'),(288,'Can delete Message',96,'delete_message'),(289,'Can add MaTriggerType',97,'add_matriggertype'),(290,'Can change MaTriggerType',97,'change_matriggertype'),(291,'Can delete MaTriggerType',97,'delete_matriggertype'),(292,'Can add MessageHistory',98,'add_messagehistory'),(293,'Can change MessageHistory',98,'change_messagehistory'),(294,'Can delete MessageHistory',98,'delete_messagehistory'),(295,'Can add file',59,'add_file'),(296,'Can change file',59,'change_file'),(297,'Can delete file',59,'delete_file'),(298,'Can add Bot',99,'add_bot'),(299,'Can change Bot',99,'change_bot'),(300,'Can delete Bot',99,'delete_bot'),(301,'Can add BotScenario',100,'add_botscenario'),(302,'Can change BotScenario',100,'change_botscenario'),(303,'Can delete BotScenario',100,'delete_botscenario'),(304,'Can add Scenario',101,'add_scenario'),(305,'Can change Scenario',101,'change_scenario'),(306,'Can delete Scenario',101,'delete_scenario'),(307,'Can add MessageTemplate',102,'add_messagetemplate'),(308,'Can change MessageTemplate',102,'change_messagetemplate'),(309,'Can delete MessageTemplate',102,'delete_messagetemplate'),(310,'Can add MessageTemplateCategory',103,'add_messagetemplatecategory'),(311,'Can change MessageTemplateCategory',103,'change_messagetemplatecategory'),(312,'Can delete MessageTemplateCategory',103,'delete_messagetemplatecategory'),(313,'Can add Message',104,'add_message'),(314,'Can change Message',104,'change_message'),(315,'Can delete Message',104,'delete_message'),(316,'Can add MessageType',105,'add_messagetype'),(317,'Can change MessageType',105,'change_messagetype'),(318,'Can delete MessageType',105,'delete_messagetype'),(319,'Can add PaymentHistory',106,'add_paymenthistory'),(320,'Can change PaymentHistory',106,'change_paymenthistory'),(321,'Can delete PaymentHistory',106,'delete_paymenthistory'),(322,'Can add MessageBlock',107,'add_messageblock'),(323,'Can change MessageBlock',107,'change_messageblock'),(324,'Can delete MessageBlock',107,'delete_messageblock'),(325,'Can add Settings',108,'add_settings'),(326,'Can change Settings',108,'change_settings'),(327,'Can delete Settings',108,'delete_settings'),(328,'Can add file',109,'add_file'),(329,'Can change file',109,'change_file'),(330,'Can delete file',109,'delete_file'),(331,'Can add EndUser',110,'add_enduser'),(332,'Can change EndUser',110,'change_enduser'),(333,'Can delete EndUser',110,'delete_enduser'),(334,'Can add EndUserBotScenario',111,'add_enduserbotscenario'),(335,'Can change EndUserBotScenario',111,'change_enduserbotscenario'),(336,'Can delete EndUserBotScenario',111,'delete_enduserbotscenario'),(337,'Can add Response',112,'add_response'),(338,'Can change Response',112,'change_response'),(339,'Can delete Response',112,'delete_response'),(340,'Can add LogLine',113,'add_logline'),(341,'Can change LogLine',113,'change_logline'),(342,'Can delete LogLine',113,'delete_logline'),(343,'Can add EndUser',114,'add_enduser'),(344,'Can change EndUser',114,'change_enduser'),(345,'Can delete EndUser',114,'delete_enduser'),(346,'Can add Settings',115,'add_settings'),(347,'Can change Settings',115,'change_settings'),(348,'Can delete Settings',115,'delete_settings'),(349,'Can view log entry',1,'view_logentry'),(350,'Can view permission',2,'view_permission'),(351,'Can view group',3,'view_group'),(352,'Can view user',4,'view_user'),(353,'Can view content type',5,'view_contenttype'),(354,'Can view session',6,'view_session'),(355,'Can view tag',31,'view_tag'),(356,'Can view tagged item',32,'view_taggeditem'),(357,'Can view EndUser',12,'view_enduser'),(358,'Can view EndUserFacebook',7,'view_enduserfacebook'),(359,'Can view EndUserLINE',9,'view_enduserline'),(360,'Can view Service',11,'view_service'),(361,'Can view Vendor',8,'view_vendor'),(362,'Can view VendorBranch',10,'view_vendorbranch'),(363,'Can view TagCategory',13,'view_tagcategory'),(364,'Can view VendorUser',15,'view_vendoruser'),(365,'Can view EndUserState',19,'view_enduserstate'),(366,'Can view EndUserStory',17,'view_enduserstory'),(367,'Can view MessagingAPIType',20,'view_messagingapitype'),(368,'Can view Payload',18,'view_payload'),(369,'Can view AutoMessageCondition',23,'view_automessagecondition'),(370,'Can view AutomessageController',21,'view_automessagecontroller'),(371,'Can view AutomessageTrigger',22,'view_automessagetrigger'),(372,'Can view ManualMessageController',24,'view_manualmessagecontroller'),(373,'Can view ManualMessageOverview',25,'view_manualmessageoverview'),(374,'Can view AutoMessageHistory',26,'view_automessagehistory'),(375,'Can view AutoMessageType',27,'view_automessagetype'),(376,'Can view ManualMessageHistory',28,'view_manualmessagehistory'),(377,'Can view EndUserAutoMessage',29,'view_enduserautomessage'),(378,'Can view EndUserStoryHistory',34,'view_enduserstoryhistory'),(379,'Can view TodoActionStatus',35,'view_todoactionstatus'),(380,'Can view Event',37,'view_event'),(381,'Can view EventCategory',38,'view_eventcategory'),(382,'Can view EventReservation',39,'view_eventreservation'),(383,'Can view EventReservationStatus',40,'view_eventreservationstatus'),(384,'Can view VendorEventSettings',41,'view_vendoreventsettings'),(385,'Can view Tag',42,'view_tag'),(386,'Can view MessageStatus',43,'view_messagestatus'),(387,'Can view EndUserStoryTemplate',44,'view_enduserstorytemplate'),(388,'Can view EndUserStoryTemplateCategory',45,'view_enduserstorytemplatecategory'),(389,'Can view WorkerSQSStatus',46,'view_workersqsstatus'),(390,'Can view EndUserSequenceState',47,'view_endusersequencestate'),(391,'Can view MessageBlock',49,'view_messageblock'),(392,'Can view MessageSequence',48,'view_messagesequence'),(393,'Can view TmpEntry',51,'view_tmpentry'),(394,'Can view Todo',50,'view_todo'),(395,'Can view Affiliate',52,'view_affiliate'),(396,'Can view TmpEntry',53,'view_tmpregistrationentry'),(397,'Can view SummaryLogEndUser',56,'view_summarylogendusers'),(398,'Can view SummaryLogVendorUser',57,'view_summarylogvendorusers'),(399,'Can view event_start_dt',58,'view_logshistory'),(400,'Can view EndUserContactChat',55,'view_endusercontactchat'),(401,'Can view file',59,'view_file'),(402,'Can view Plan',64,'view_plan'),(403,'Can view Service',63,'view_service'),(404,'Can view VendorPlan',60,'view_vendorplan'),(405,'Can view VendorService',62,'view_vendorservice'),(406,'Can view VendorUser',61,'view_vendoruser'),(407,'Can view NotificationService',66,'view_notificationservice'),(408,'Can view NotificationSetting',65,'view_notificationsetting'),(409,'Can view Coupon',68,'view_coupon'),(410,'Can view CouponType',67,'view_coupontype'),(411,'Can view Question',69,'view_question'),(412,'Can view Questionnaire',70,'view_questionnaire'),(413,'Can view Questionnaire Question',71,'view_questionnairequestion'),(414,'Can view QuestionType',72,'view_questiontype'),(415,'Can view EndUserQuestionnaire',73,'view_enduserquestionnaire'),(416,'Can view Response',74,'view_response'),(417,'Can view SenbayUser',75,'view_senbayuser'),(418,'Can view VendorBusinessPartner',76,'view_vendorbusinesspartner'),(419,'Can view VendorBusinessPartnerTag',77,'view_vendorbusinesspartnertag'),(420,'Can view Message',78,'view_message'),(421,'Can view MaTrigger',80,'view_matrigger'),(422,'Can view MaTriggerType',79,'view_matriggertype'),(423,'Can view CouponClaim',81,'view_couponclaim'),(424,'Can view Product',82,'view_product'),(425,'Can view ProductCategory',83,'view_productcategory'),(426,'Can view Receiving History',84,'view_receivinghistory'),(427,'Can view Shipping History',85,'view_shippinghistory'),(428,'Can view Stock',86,'view_stock'),(429,'Can view StockSpace',87,'view_stockspace'),(430,'Can view Questionnaire Template',88,'view_questionnairetemplate'),(431,'Can view Questionnaire Template Question',89,'view_questionnairetemplatequestion'),(432,'Can view Notification',94,'view_notification'),(433,'Can view NotificationHistory',93,'view_notificationhistory'),(434,'Can view Business',90,'view_business'),(435,'Can view BusinessPlan',91,'view_businessplan'),(436,'Can view VendorUser',92,'view_vendoruser'),(437,'Can view PaymentHistory',106,'view_paymenthistory'),(438,'Can view Settings',108,'view_settings'),(439,'Can view file',109,'view_file'),(440,'Can view Bot',99,'view_bot'),(441,'Can view BotScenario',100,'view_botscenario'),(442,'Can view Message',104,'view_message'),(443,'Can view MessageBlock',107,'view_messageblock'),(444,'Can view MessageType',105,'view_messagetype'),(445,'Can view Scenario',101,'view_scenario'),(446,'Can view EndUserBotScenario',111,'view_enduserbotscenario'),(447,'Can view EndUser',114,'view_enduser'),(448,'Can view LogLine',113,'view_logline'),(449,'Can view Settings',115,'view_settings'),(450,'Can view MaTrigger',95,'view_matrigger'),(451,'Can view MaTriggerType',97,'view_matriggertype'),(452,'Can view Message',96,'view_message'),(453,'Can view MessageHistory',98,'view_messagehistory'),(454,'Can view MessageTemplate',102,'view_messagetemplate'),(455,'Can view MessageTemplateCategory',103,'view_messagetemplatecategory'),(456,'Can view test model',54,'view_testmodel'),(457,'Can add document',116,'add_document'),(458,'Can change document',116,'change_document'),(459,'Can delete document',116,'delete_document');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=232 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$fAN536rPNE5K$lDBtWCGlYWPBG3SWtfFB89DcoxbAkghbqshi94S9Ppc=','2019-08-26 08:33:06.832618',1,'admin','','','',1,1,'2018-05-31 02:49:37.587196'),(6,'pbkdf2_sha256$100000$ERELICDgYSL3$zwrsZihPgPslLIRFdtrwN58Opw6pxzJ+0uwPEXqE8RQ=',NULL,0,'Jun Kawajiri_gId3ij','','','',0,1,'2018-06-05 04:16:30.598538'),(7,'pbkdf2_sha256$100000$AqDpYrJ5QLHj$1JLXQ/ReU/jI5JaBzJgmw5iCtb9uibE7Ev87nepIIVg=','2021-07-19 08:39:35.198275',0,'test01@test.com','','','test01@test.com',0,1,'2018-06-17 12:57:30.000000'),(8,'pbkdf2_sha256$100000$YrkkXrYHt6C2$3NyPQVJGNjQVs73/2zCMUgR//vHNBC4Wf4JHdOFExrk=','2019-11-07 06:52:24.345162',0,'test02@test.com','','','test02@test.com',0,1,'2018-06-17 12:59:25.000000'),(9,'pbkdf2_sha256$100000$r9eOdUfoSsIF$+/NqebFzzs6lYM1YJaRMyXskPsMeKbE7/5LIxpYFzfI=','2018-06-29 08:06:22.051174',0,'vendor2','','','',0,1,'2018-06-29 06:53:10.582190'),(10,'pbkdf2_sha256$100000$MZspJMAiOVSa$Yn110c345trzHWKfsxgB21ugz8Sa1g9JXnd9Ck9H7aw=',NULL,0,'Martijn Bruning_Fl9GDN','','','',0,1,'2018-07-02 08:11:09.153127'),(11,'pbkdf2_sha256$100000$o58kK84muWwk$15esqYOs+nANFBW7jwNBAtUyf6BERczItP3+PF6bTE0=',NULL,0,'Martin_gH2qN2','','','',0,1,'2018-07-30 01:41:47.762316'),(16,'pbkdf2_sha256$100000$LEDDAbvQotff$kAEH/D+m8qVx2DlkisOi34V7++B0TvbbfYDIUzvx10s=',NULL,0,'template@template.com','','','template@template.com',0,1,'2018-08-20 08:40:21.310246'),(17,'pbkdf2_sha256$100000$E8qZW5BQJJUy$LPotLJ5aG3YoyDk2vgXu5++I4D6v5UIx/TW/hW1mjDU=',NULL,0,'_IVqZjt','','','',0,1,'2018-11-05 05:59:10.663609'),(18,'pbkdf2_sha256$100000$KvH0mLVC1Gex$m/ybKhfpWgQRd3D5oy5FDjcAwdAl+fd3obrzUWkjVxA=',NULL,0,'_aIT4IZ','','','',0,1,'2018-11-05 05:59:48.331865'),(19,'pbkdf2_sha256$100000$8Sb1i8RaxNB9$JRAu6Hh52cOm0OAIAfWgqhOitZtQxnemYAiiue5QDSA=',NULL,0,'_uKhNZZ','','','',0,1,'2018-11-05 06:01:27.692328'),(20,'pbkdf2_sha256$100000$rHc0jrzWw99z$kPJho/wvPGKKB4Ma7pmcFoWfm5l4YFzjZgXahcQkVf0=',NULL,0,'_6W6rVn','','','',0,1,'2018-11-05 06:03:03.616809'),(21,'pbkdf2_sha256$100000$UJDlM07Ct8bq$gIuyfrqMGrXrhym1BrtVnQchvs7DzIFkVcuqAh9eJx4=',NULL,0,'_zT4XZA','','','',0,1,'2018-11-05 06:10:15.440331'),(22,'pbkdf2_sha256$100000$FTZ6o2f0jJRW$AqrTDVdWpbJLiVhScIkkYhq2Zjj8od4wjVhmIcsUm1Q=',NULL,0,'_66gWcT','','','',0,1,'2018-11-05 06:10:18.947341'),(23,'pbkdf2_sha256$100000$wO11whWQ70l6$nsjVCzKSarkJ1iFQ69CVgUJyV6iYeCuk76rU9OWIzQk=',NULL,0,'_24HMuA','','','',0,1,'2018-11-05 06:10:22.356582'),(24,'pbkdf2_sha256$100000$wJ2PKkL9i3uM$BaqIfza9Std2ctrDSUmMk7iMyhdN9j3Zb0aDvtvC/2M=',NULL,0,'_7SgIWC','','','',0,1,'2018-11-05 06:10:25.692721'),(25,'pbkdf2_sha256$100000$EwSz4WWEf8dc$zKtspLg+2WvxZzaBim44vCsKHwEwCuNzVtTMfSrPj38=',NULL,0,'_yKmb4t','','','',0,1,'2018-11-05 06:10:28.694306'),(26,'pbkdf2_sha256$100000$a9eJDoEAHtfr$IvGcI/9rdg1d9MNLEyfLDezwSE0RZDF82fB2+liSVjY=',NULL,0,'_AtrSfK','','','',0,1,'2018-11-05 06:10:32.075376'),(27,'pbkdf2_sha256$100000$L2XiO2SvHUOi$W6BBNLxEiz42mcjRoFs4uxv3ErdwM2iN3SgYTapkWfE=',NULL,0,'_SE64F7','','','',0,1,'2018-11-05 06:10:35.192594'),(28,'pbkdf2_sha256$100000$7Oho5NgW2KDJ$KMO7OxuTX86DyDS9zEgWZKMgKBtz5W4S8+/QHRqmeRw=',NULL,0,'_hbVCq2','','','',0,1,'2018-11-05 06:10:38.716280'),(29,'pbkdf2_sha256$100000$6JI66FU2qBn2$G/962YPczz9BQJqfxR9Roqwu1TIgNpe1TsLrPe/914g=',NULL,0,'_5WKFHz','','','',0,1,'2018-11-05 06:10:42.387022'),(30,'pbkdf2_sha256$100000$sJXrvVCRWph0$gJgVGpWmJCQeBGAO00wVFjJhdCI+rRzFmZgsm+yvbU0=',NULL,0,'_jAmp7L','','','',0,1,'2018-11-05 06:10:45.576588'),(31,'pbkdf2_sha256$100000$JtwKOAvnAZiP$6qbip38tl5wIE6kSL9a8m/KSn4XEMo4eCzo/xJp8k+I=',NULL,0,'_mkvaIy','','','',0,1,'2018-11-05 06:10:55.434530'),(32,'pbkdf2_sha256$100000$rra39CSN6cDq$TJXGrpR1CjFhsw6v3lB8sZL9epDM1xIganO9W0/uNz0=',NULL,0,'_Fzp0Lh','','','',0,1,'2018-11-05 06:11:01.474319'),(33,'pbkdf2_sha256$100000$6uOTgva6oCFk$kS+XwREjz0i5Ii3EP9OeSGr45RSAh5UyOJmqU2CHeCM=',NULL,0,'_ErmmjY','','','',0,1,'2018-11-05 06:11:04.486233'),(34,'pbkdf2_sha256$100000$tIFarGnvMoQi$0m8Dx8S7GAiGuON4w0tBVn+hIE1M1m71fUSQjuJAsus=',NULL,0,'_Wk4S1u','','','',0,1,'2018-11-05 06:11:07.837293'),(35,'pbkdf2_sha256$100000$fEkPnRhrgcMx$zmnJHWytLxwHjW+uSPBgFUyJLzZfaXZRkCrZkO2M+og=',NULL,0,'_J5NWEB','','','',0,1,'2018-11-05 06:11:11.658550'),(36,'pbkdf2_sha256$100000$B7MXxo7O6NwK$z+LHpWXOLbDJ+VgHeFv7Dyx0CiRqSgrRrS+QE2z4w0k=',NULL,0,'_harPk9','','','',0,1,'2018-11-05 06:11:15.517503'),(37,'pbkdf2_sha256$100000$yCFHvlmyfNGY$OQEZEgh6vJOAQvna42+HUOgV3NTxR3RW60Vfoq9mIpU=',NULL,0,'_Yt5WSZ','','','',0,1,'2018-11-05 06:11:19.202992'),(38,'pbkdf2_sha256$100000$aaKxIKdpxCC1$yZsRSgBcdZsULVT4BNou2kuwN+IB8+6LpeDE2lKdt20=',NULL,0,'_qXAsAb','','','',0,1,'2018-11-05 06:11:22.437735'),(39,'pbkdf2_sha256$100000$gzcAL6xA7rYc$EjEO8h4u4nWy8ItXr445N1BeGdlmItofXK596dUGeKY=',NULL,0,'_hvqv4O','','','',0,1,'2018-11-05 06:11:31.051733'),(40,'pbkdf2_sha256$100000$2ltJwtuUdPKp$dY4sQwsZ1Wt8jokGBT7gZACu9J3fkqLjv1j3bvo4bnQ=',NULL,0,'_yXQViY','','','',0,1,'2018-11-05 06:11:33.924671'),(41,'pbkdf2_sha256$100000$Mav0riJDKuyo$6qUntTzxDGqxYUPPaKRJR1i3WVaBhHD6Z1YGIzl2oVg=',NULL,0,'_97QFWV','','','',0,1,'2018-11-05 06:11:38.354442'),(42,'pbkdf2_sha256$100000$EEysmTWRTTGd$3+TsTTJE4Urp/COMD7esn6+0i2Ffn0gnbRYC1wMHoew=',NULL,0,'_L8VLWp','','','',0,1,'2018-11-05 06:11:43.139566'),(43,'pbkdf2_sha256$100000$dMqvQgBByth4$57l2nBSM+CMTPUpGiys67MGGQKdHIbHXXx8245oJehA=',NULL,0,'_lPp4YJ','','','',0,1,'2018-11-05 06:11:48.512867'),(44,'pbkdf2_sha256$100000$Ft2IpFswsWrc$1AxaXZsfiVI/GCWue1uJ07K6R/VfCzuHIaUq+FuKc1s=',NULL,0,'_EqTnIX','','','',0,1,'2018-11-05 06:11:54.198343'),(45,'pbkdf2_sha256$100000$j10kmjiiK4M4$sJL7g3kByACN2jVt7mGhxssMPdTseIXmY4A9DRkeLIM=',NULL,0,'_h65jNe','','','',0,1,'2018-11-05 06:11:57.798179'),(46,'pbkdf2_sha256$100000$z98SUk0092dr$8i0uCt6fwfsyL4xY0ykHfKI3wEb3qoU5q/7NbIISeFU=',NULL,0,'_NHaN7A','','','',0,1,'2018-11-05 06:12:01.000314'),(47,'pbkdf2_sha256$100000$3JnXj0vyHyG8$OqDEb211/yCGPwap8Aofr4U45sGbpSWymutKWYKwnCM=',NULL,0,'_g1qH3K','','','',0,1,'2018-11-05 06:12:06.369873'),(48,'pbkdf2_sha256$100000$bzusBNt54ExA$N9zIEXEB2EYhvUk1Ar8+lJkuPQEmed8yu7eFtgYUwak=',NULL,0,'_6KTbam','','','',0,1,'2018-11-05 06:12:09.690258'),(49,'pbkdf2_sha256$100000$2H4xmTzn6ySf$Zb8y1JMBNXDsYH+fpDRMLHcaSgxjE6wA9Ud00q41TBY=',NULL,0,'_2Bmul7','','','',0,1,'2018-11-05 06:12:12.682247'),(50,'pbkdf2_sha256$100000$o8kNdG9zQE7r$6se5FOK3xws7aqqjsZt51Rwqmo2sRQ5J+Sq72ij3jpE=',NULL,0,'_cZe7Rb','','','',0,1,'2018-11-05 06:12:16.418840'),(51,'pbkdf2_sha256$100000$uCeRCmWBJHWH$8g+Cwz6XBy0j2pbwkElvjdJIj4pjt9zP/nLGqCZ3ezA=',NULL,0,'_w0Zbzm','','','',0,1,'2018-11-05 06:12:19.739519'),(52,'pbkdf2_sha256$100000$H6dTL6aYyeqp$dHWFiNUmZURXwRT2QtCtHv9TdPlsmVxJd7yFyhNpgeM=',NULL,0,'_CvxG5L','','','',0,1,'2018-11-05 06:12:23.355351'),(53,'pbkdf2_sha256$100000$PSX2bo4QTWa1$Oo4Th6qXTaMUC4Dp2I3+vGeHsUhWkghF6Pi2BY9Se+g=',NULL,0,'_y0sYoa','','','',0,1,'2018-11-05 06:12:27.844162'),(54,'pbkdf2_sha256$100000$gAhqmSunHcQm$hOb0SfnW+jqcTyOXo59d+TzR7Z9bm4w45hvOfZIviE0=',NULL,0,'_0uM294','','','',0,1,'2018-11-05 06:12:40.030684'),(55,'pbkdf2_sha256$100000$YQ2buINLbRXh$qcyjB8woDqhQnAzYsn2fKeXrk9FwNwTCk1Ad8fk359o=',NULL,0,'_uTE1gC','','','',0,1,'2018-11-05 06:12:43.613832'),(56,'pbkdf2_sha256$100000$Ck4IE7G8jLvf$6ZTjmO+/2nhK/two/B6pnzX05sTkkBUHqRyUVj9bKIc=',NULL,0,'_92Zjfp','','','',0,1,'2018-11-05 06:12:47.304647'),(57,'pbkdf2_sha256$100000$QmZGIeqySiX8$qliZVM0bDrsE/W8IOSu5Yv4nPH+2jHWxvTj5rfO+0QI=',NULL,0,'_AlMEeV','','','',0,1,'2018-11-05 06:12:50.805264'),(58,'pbkdf2_sha256$100000$gKUnaEE7VlTb$Om2wqpkSL8sgXS5YXNU3VrKLo0ojctEQJaRVVJ69CLk=',NULL,0,'_HeZA7E','','','',0,1,'2018-11-05 06:12:54.164746'),(59,'pbkdf2_sha256$100000$4bdAnSDEFeYe$TxVTrBpJyU7+9gODb7IaFP551jGMT+pcFUm03SGEHeA=',NULL,0,'_z4ATaJ','','','',0,1,'2018-11-05 06:12:56.896788'),(60,'pbkdf2_sha256$100000$9wdH2tWlZIBU$q+D99Odh3dFY/4dsDsIY6hwTvQ516DSi9cN5xlhYOYo=',NULL,0,'_DTTNkQ','','','',0,1,'2018-11-05 06:13:03.029395'),(61,'pbkdf2_sha256$100000$RsTid8k4cKiJ$fLQenMV03ol9Chi6GPLvbN5CQFr/iBfNKJAd24xwTTw=',NULL,0,'_7GhLIw','','','',0,1,'2018-11-05 06:13:06.609910'),(62,'pbkdf2_sha256$100000$86NZdeUSwDGD$8i47c6/TJwGh1i0ZO20AjC33xtsf8z4eFELjShqqDr8=',NULL,0,'_HjrkZK','','','',0,1,'2018-11-05 06:13:10.638408'),(63,'pbkdf2_sha256$100000$mucaasGRpmOZ$8GwBUaEORGybbUC5TeO2XQSofLd3EBnBFRUBU/RcqgI=',NULL,0,'_H5RAhx','','','',0,1,'2018-11-05 06:13:13.694552'),(64,'pbkdf2_sha256$100000$E5PjPftLKEEj$9RgtRV1PTTKmcfVIQCY1vT+fMlM5fkvpT4BbjqCgxoM=',NULL,0,'_YhQG08','','','',0,1,'2018-11-05 06:13:17.009031'),(65,'pbkdf2_sha256$100000$zOMQWdyjY4Ot$Ho98pp0a2ZgAi4RdEUkm8shg0NKP9l+8Wg0MtSPinmk=',NULL,0,'_YDVw5J','','','',0,1,'2018-11-05 06:13:21.402424'),(66,'pbkdf2_sha256$100000$vc7YWe0dZrgf$VOKKubijleU24pwobx8GdQDsZVyINtIH1Y3U4uWvcZQ=',NULL,0,'_jOMnMJ','','','',0,1,'2018-11-05 06:13:27.588787'),(67,'pbkdf2_sha256$100000$vDKeMcA0onBg$i22hNw0ZTAlXJ7g45+Og0pg3AUJFcjywZLYNbp8z5yc=',NULL,0,'_hUAiTg','','','',0,1,'2018-11-05 06:13:30.463492'),(68,'pbkdf2_sha256$100000$LxhWERArELFX$KeMriJqOf7EuQZ+fQnWcpM3ZqWCpYool+moOaAxw+Dc=',NULL,0,'_H8fFOi','','','',0,1,'2018-11-05 06:13:36.702489'),(69,'pbkdf2_sha256$100000$lTV7PmfVJKEm$Jphi9r9B4Vw48rf3XMRrHZhsxI1SlXqN1zKkgjfJELw=',NULL,0,'_LXJbg2','','','',0,1,'2018-11-05 06:13:40.064718'),(70,'pbkdf2_sha256$100000$E32R86hKaHOh$Kwj/a3BoOT0x9T2h3MCfI8+JskE8Jf1Ol9kUe6IMyqg=',NULL,0,'_nfYoH5','','','',0,1,'2018-11-05 06:13:43.410218'),(71,'pbkdf2_sha256$100000$ZpGMBfbgAoJf$g2wEYJLz3+kpPaluzJnEpRJkps0bIED68XVZQr+FFbs=',NULL,0,'_8mvIFF','','','',0,1,'2018-11-05 06:13:46.818994'),(72,'pbkdf2_sha256$100000$ROpEJruZ7wcO$Opr+p330EM63Dj8pwXgooegtQWqGg6A09CiVvnJELeM=',NULL,0,'_nwHlkJ','','','',0,1,'2018-11-05 06:13:51.511363'),(73,'pbkdf2_sha256$100000$LVNduj1sHeaC$fHtC1ogl16NkUt+U6Ii1BfBJbT5JMxPzm7pxBVbrT0Y=',NULL,0,'_x2d42A','','','',0,1,'2018-11-05 06:14:04.684787'),(74,'pbkdf2_sha256$100000$AP31Nflc43t8$LdYNb+CkzjS/kymdXhljcavhHmr8QV+F7azpt62Pya0=',NULL,0,'_OSBBlE','','','',0,1,'2018-11-05 06:14:13.798443'),(75,'pbkdf2_sha256$100000$RuRD1K2Y0Utd$b56g7JpAy56jA4qa9ARfvhcgyO4rgfOAKVxLjCcgcrI=',NULL,0,'_P82FtR','','','',0,1,'2018-11-05 06:14:16.681298'),(76,'pbkdf2_sha256$100000$4wwHPfYcjvtR$YcxZ150ua2GP6z7nCJpo/7w8tQ2+2DZRloEDMUTJmjo=',NULL,0,'_rm8N2j','','','',0,1,'2018-11-05 06:14:21.618690'),(77,'pbkdf2_sha256$100000$wVOjXDFcJVzX$yGIfnheXJFANqrJXaNInMgxvWWNr4S2udMN99F8Yn20=',NULL,0,'_YTIYHz','','','',0,1,'2018-11-05 06:14:25.373193'),(78,'pbkdf2_sha256$100000$tpeBfA8sFL08$FudBZWiKCVzlmuF3++QpgtKLR4SbbCFRH0UpZlU5K1U=',NULL,0,'_eHs563','','','',0,1,'2018-11-05 06:14:29.101591'),(79,'pbkdf2_sha256$100000$rZpNQ2Ot8RDj$OyjlyY7I02Z2bXL9jWamL7wlIAOm+xis0r9eqZMP/+s=',NULL,0,'_QRm1xn','','','',0,1,'2018-11-05 06:14:39.750182'),(80,'pbkdf2_sha256$100000$9bidkUrLEEJs$8/8ULgc/Zr9PWhJBZdYyFjjUiayADfvXxz0uwVLxbqg=',NULL,0,'_Y90Pj2','','','',0,1,'2018-11-05 06:14:44.955156'),(81,'pbkdf2_sha256$100000$xZ1YgfvvZ6So$IUQ/3WEq5ZRWB4NsCHnu3AAPQqkH/QuHSHYPplFXlaM=',NULL,0,'_YW03sw','','','',0,1,'2018-11-05 06:14:48.563490'),(82,'pbkdf2_sha256$100000$7Z8HCAWvgA9M$2XPCu1hTcsTawJZk8jE6E0vLt/ldWascsXcL/bfibqY=',NULL,0,'_RBF9oy','','','',0,1,'2018-11-05 06:15:00.331617'),(83,'pbkdf2_sha256$100000$04n5krmxrnFF$0+Shjl2LERH/eiNlTOwuYAR2um2e9LL18g2C5YLI54k=',NULL,0,'_RiV4mS','','','',0,1,'2018-11-05 06:15:03.143534'),(84,'pbkdf2_sha256$100000$8F1wenpcIDf6$MQ/f7YhN7nbMBLMOwB4XYcAYuOJrwn1f2rLTN9sdUcA=',NULL,0,'_GXPDAm','','','',0,1,'2018-11-05 06:15:10.997513'),(85,'pbkdf2_sha256$100000$DZhkElkGZ8JT$XExKXv877vZBq/zNnBbTNmSqxwHZX6iUr349/7/NIfM=',NULL,0,'_jrTuSo','','','',0,1,'2018-11-05 06:15:14.377513'),(86,'pbkdf2_sha256$100000$c35Iyth5bszP$5PfqXjd06Q73gUH/Yw2PDhYtHzCccpaDZcXT02KW9vQ=',NULL,0,'_pvQb4b','','','',0,1,'2018-11-05 06:15:20.664692'),(87,'pbkdf2_sha256$100000$stYumU09ijlx$OnHH9KxjcXaKPBQwAuBWGVqvCZ+vTkEwKc8KEsbPtkY=',NULL,0,'_NB56tj','','','',0,1,'2018-11-05 06:15:25.029661'),(88,'pbkdf2_sha256$100000$gCRKmdwJNlUO$EqIM1YXDhNvP99gcJXn6Z9JID9hqmOO6qFuCqSLrixY=',NULL,0,'_TUa0sD','','','',0,1,'2018-11-05 06:15:28.569053'),(89,'pbkdf2_sha256$100000$6VsVigldf04d$Obh2jB5nxY6c03OQdpqRXCaoXYsE+mRFaeW8Cu6U36I=',NULL,0,'_sueGr9','','','',0,1,'2018-11-05 06:15:32.010474'),(90,'pbkdf2_sha256$100000$vgJx0oVY2gAb$dFkNnz0gGSFCHurXKNo87tCpP3W1qioaWNYYGSS79q0=',NULL,0,'_Tu1lYy','','','',0,1,'2018-11-05 06:15:35.428227'),(91,'pbkdf2_sha256$100000$GTG4dCNydG8q$CI7F8z1XKzHYLl8UsDMVXfYL9gfuEXtywctEHmAV8M4=',NULL,0,'_oJnmB7','','','',0,1,'2018-11-05 06:15:39.284748'),(92,'pbkdf2_sha256$100000$q76d92XxzdQo$ixNsqSrOtQnzIJ59RnwlHlwxL4K6/v+rHV21WM8s/2k=',NULL,0,'_ppHhwZ','','','',0,1,'2018-11-05 06:15:42.822251'),(93,'pbkdf2_sha256$100000$qEmnQ94HaiJH$2LET6PiGGXuT9WZodG8K2NuQf6E61MBFwDI4RrcSuy4=',NULL,0,'_pTZ9PH','','','',0,1,'2018-11-05 06:15:46.271799'),(94,'pbkdf2_sha256$100000$W2DU2KwBTAb0$y8vV4Lt+a78UnTfRXdoIAm7dWtTFblefRjLhKEgOYqQ=',NULL,0,'_ybsRf4','','','',0,1,'2018-11-05 06:15:55.677490'),(95,'pbkdf2_sha256$100000$c63VUkK9xosz$ZQDjvPBSgNCsCigemcmGBQx3AGW212l4fKOFr7VsrwI=',NULL,0,'_G3ChsQ','','','',0,1,'2018-11-05 06:15:58.974500'),(96,'pbkdf2_sha256$100000$T4EOPn7lgnJ6$FMpevxEY/sdvZ8nE4ZwZxxXo6UoL4VhMetwjPGUFgh0=',NULL,0,'_Ca46k3','','','',0,1,'2018-11-05 06:16:03.749153'),(97,'pbkdf2_sha256$100000$XVGpRg9Zu2JS$jVDyqmHX41ZQBuRHVe5OHh8fH4Qtv7dXNcXTOJ9lwF8=',NULL,0,'_KkEZB8','','','',0,1,'2018-11-05 06:16:07.523477'),(98,'pbkdf2_sha256$100000$T8eABvYYz26i$pLdqKEcX+qKCgi42qXrYY1HNTn0O0mhxEJ6QUWM6nko=',NULL,0,'_UV7Es4','','','',0,1,'2018-11-05 06:16:12.891314'),(99,'pbkdf2_sha256$100000$defPolumUEVe$YqFy3PL6W6x5gu+agNgVt6s9iSl8NLrw5yJnJul7a0I=',NULL,0,'_n4ibvz','','','',0,1,'2018-11-05 06:16:23.945954'),(100,'pbkdf2_sha256$100000$gs0dvqhJMAkV$MpIq2qqkh0aHqDOqe1uXoatLBFKS608XCDYIFnIlDWQ=',NULL,0,'_UPwSJ0','','','',0,1,'2018-11-05 06:16:32.286721'),(101,'pbkdf2_sha256$100000$lYnZVZwrsg30$DCIDXX4G0XWg5HB+L4M+WWzIlbbfAwC1Az3MFDIje0w=',NULL,0,'_YciVab','','','',0,1,'2018-11-05 06:16:35.638790'),(102,'pbkdf2_sha256$100000$tMCsQDMDP9BH$wTA3siZPbXatJdz9z+m7c6SePhRzqAhbEEJU4E1ixrs=',NULL,0,'_Dl9Mug','','','',0,1,'2018-11-05 06:16:40.858321'),(103,'pbkdf2_sha256$100000$w2nIQDedKFxb$aHgngn7MKUH/e9ATP5Mk3+u61/HLF2rnFphbFT6LPX4=',NULL,0,'_knGCht','','','',0,1,'2018-11-05 06:16:46.732560'),(104,'pbkdf2_sha256$100000$5a8S8Y1BVQxY$xfp2PxhXP9TwDFKC8FsqzVgvqG1ZvluIx/aJJNpzt1s=',NULL,0,'_KVK7NX','','','',0,1,'2018-11-05 06:16:50.287718'),(105,'pbkdf2_sha256$100000$K1M3B2pu73qY$cxaPyNxEcmAcY19QDKnlmj5DU9u8GDg3aS4qPdx9i4M=',NULL,0,'_JJod31','','','',0,1,'2018-11-05 06:16:57.282802'),(106,'pbkdf2_sha256$100000$UxjeTJicYANE$wqOYoPaoXPYlDkj+ZJTHutAB+FDLnnxhFebPnV1PvHg=',NULL,0,'_oXacjr','','','',0,1,'2018-11-05 06:17:01.254651'),(107,'pbkdf2_sha256$100000$OIuFjMj6EyO5$SUInqphSowGFj9jpRxbTPmdsKTU31peFG1rahvqSAmc=',NULL,0,'_ZtEfvL','','','',0,1,'2018-11-05 06:17:04.227862'),(108,'pbkdf2_sha256$100000$L0WyS0wvZnHG$jf2hkm9Ax4t7UEaZdg+ZIux6rZwtrTfV0xsJoXtOWg0=',NULL,0,'_sCW4kh','','','',0,1,'2018-11-05 06:17:10.277405'),(109,'pbkdf2_sha256$100000$uGx5XV8iq4LT$r3vIH6p1+b6iZnDKAdb/soB5jadpp8e1Z8wDWhEr1/0=',NULL,0,'_7BelDA','','','',0,1,'2018-11-05 06:17:15.315715'),(110,'pbkdf2_sha256$100000$SJy4f7tSLuah$/kEIa9KqimSpYwvuxWuRlIgEwngHnlxLjfb11cfUB/g=',NULL,0,'_nPa0oF','','','',0,1,'2018-11-05 06:17:19.055236'),(111,'pbkdf2_sha256$100000$kpKLmT9KYMq3$SRU/ArJXsBFRtlwvuhiR0VBex27QM/ik2vkK0VE/ppM=',NULL,0,'_jt4EzC','','','',0,1,'2018-11-05 06:17:21.868605'),(112,'pbkdf2_sha256$100000$4G2uRCm8bkp2$7tabiuHqmKwev1PmDn5IMjDjgUvLrP/ofB8pbuD9sV0=',NULL,0,'_87YT9L','','','',0,1,'2018-11-05 06:17:25.611935'),(113,'pbkdf2_sha256$100000$3ZjSn8AlOX4R$p2h2UQBhUeJ8hw1EMsbGJ0scj8qvtUF8YEpdyxtDTyg=',NULL,0,'_O2Xhob','','','',0,1,'2018-11-05 06:17:31.574914'),(114,'pbkdf2_sha256$100000$5aYw1CnJyuYR$XvnhReSI2hWzi66zLOL/IQ7V9AdylfAux5JY0r9J7Z4=',NULL,0,'_nct0kp','','','',0,1,'2018-11-05 06:17:35.475353'),(115,'pbkdf2_sha256$100000$UGzp16WpIMuU$0N/Ge//eyYjkMCb+cccqf82qTPp/Hs7ZSNn0lg8afeI=',NULL,0,'_YFkJ6G','','','',0,1,'2018-11-05 06:17:39.260656'),(116,'pbkdf2_sha256$100000$UpGiTMXPHxe9$90uaD3jv4acaa5C2RoC+IFb6NU9WAzjVosscXv5bWho=',NULL,0,'_VFredj','','','',0,1,'2018-11-05 06:17:42.688044'),(117,'pbkdf2_sha256$100000$QzbUnAIxLpu3$+zUVhncIoArBZa7saFxuUMw6R78CpJ47bSVe2wf7Hy8=',NULL,0,'_5P9lEN','','','',0,1,'2018-11-05 06:17:46.246768'),(118,'pbkdf2_sha256$100000$4LFIawFcKKA3$NYuJRJ5rwHW2DlsK0NpeIN1heq+k5TZQKVGVJxQa9+c=',NULL,0,'_hWz5er','','','',0,1,'2018-11-05 06:17:49.647122'),(119,'pbkdf2_sha256$100000$Wky7jklsPhWa$UTOZ5HljV60XxPDh9WB6jI+vNL9gJ3uvEXLqu1VyChc=',NULL,0,'_sSGxQH','','','',0,1,'2018-11-05 06:17:53.016330'),(120,'pbkdf2_sha256$100000$LVh4MUJBxRWn$ThHLbW34IwEVzyyXsIdd4QLvpo3ETOXFXddgGkPJ3sc=',NULL,0,'_irOLFb','','','',0,1,'2018-11-05 06:17:56.784252'),(121,'pbkdf2_sha256$100000$aNdxXst1Y17W$aCHwYOyLXbmBQxQMsTLA0GpgkQw8Uw6Mc69myK+JUzI=',NULL,0,'_A7j5em','','','',0,1,'2018-11-05 06:18:01.515486'),(122,'pbkdf2_sha256$100000$Pe4C4Ol9XIu5$9lAzc8G6AtLv0vYsjCx1iMvCWn+VTcuAzIwyBMzyXe8=',NULL,0,'_qX9MrY','','','',0,1,'2018-11-05 06:18:05.305746'),(123,'pbkdf2_sha256$100000$Nrdrv1kUsUHn$ooGdbmLHPCZ1J3jxQQH57trCbW34HAdOZBGUnGGYaUI=',NULL,0,'_8t0anX','','','',0,1,'2018-11-05 06:18:11.563698'),(124,'pbkdf2_sha256$100000$bRLhEc4K9qM1$6Z1WBGudI+ZlFier/vvwFl7JLukfUBcdr0fJBBVD7cU=',NULL,0,'_UyfzGp','','','',0,1,'2018-11-05 06:18:21.712682'),(125,'pbkdf2_sha256$100000$t9ZQk1CdOMjz$j5C3+YOSMQZu686QjyEDV23/MNVFcTFWWnqJWghKiMU=',NULL,0,'_KDhddk','','','',0,1,'2018-11-05 06:18:33.988417'),(126,'pbkdf2_sha256$100000$zItI1fgLQQdQ$vAZoXZJgsOgJB+EqYJxu7nPK/oZXqR+9ylk5CXAX/s0=',NULL,0,'_oFCHnf','','','',0,1,'2018-11-05 06:18:43.222340'),(127,'pbkdf2_sha256$100000$9A2MUNUye2S5$YFaQ2npb61QmFCIlG+7XWZYLOlIoWHNpQMehJ/8KvCo=',NULL,0,'_ozhXGL','','','',0,1,'2018-11-05 06:18:46.165073'),(128,'pbkdf2_sha256$100000$K4xqdb9RFyaG$Mv8Cv2bljGrbLNTHPOwq7gSLd4zNBzP+BEQiy7R6A5k=',NULL,0,'_pWcXLd','','','',0,1,'2018-11-05 06:18:49.232130'),(129,'pbkdf2_sha256$100000$dJ8JmHoln4Gp$UnGcvMK/iTMBFbbJWOowcLXIctqEx9DU7xZ9vCkr7WM=',NULL,0,'_opkcOH','','','',0,1,'2018-11-05 06:18:52.759887'),(130,'pbkdf2_sha256$100000$pWFuacnIoS1J$xNq5kyCgH19g+QBKeMvd5y/bMu6x/iC6qC3XwWQXdAw=',NULL,0,'_RW4BmZ','','','',0,1,'2018-11-05 06:18:55.839921'),(131,'pbkdf2_sha256$100000$CWv4aZJrNhoC$f8SA1hggy4WKLmp5L3h9mnSoJtJKRBBYowXhM2v0OK0=',NULL,0,'_lsiI9S','','','',0,1,'2018-11-05 06:18:59.876079'),(132,'pbkdf2_sha256$100000$VK0mFndpRums$Zx/OQ+mRfVOV7+x2dObuTXJzcwkSB33aKAOUcrvNTdg=',NULL,0,'_z2G6VH','','','',0,1,'2018-11-05 06:19:03.775524'),(133,'pbkdf2_sha256$100000$Izi2Eqyp4gSs$eRFUlTULAHgRIRh/y4xliualm90rVl1lW8itC6MY4rM=',NULL,0,'_N90LtX','','','',0,1,'2018-11-05 06:19:14.643028'),(134,'pbkdf2_sha256$100000$i4XyC3V4IlqH$wWZbxYl1KPFoHNQ5GzTDh+E28tR14uRYFaNmEg0BbNc=',NULL,0,'_xzAkBs','','','',0,1,'2018-11-05 06:19:19.729686'),(135,'pbkdf2_sha256$100000$Ouh7pAbcGZMk$Jh2e4IlbI1klq37gMZZmOkOKR4sPSyA5eTikO8MgvUo=',NULL,0,'_jVrYLM','','','',0,1,'2018-11-05 06:19:24.457454'),(136,'pbkdf2_sha256$100000$2apzgnUWQWcw$n9B+Z3RyUU31Qe2ejtntF0ju0O1HgGVjlimkv3zZ6Rw=',NULL,0,'_NOE9Oj','','','',0,1,'2018-11-05 06:19:37.408441'),(137,'pbkdf2_sha256$100000$CcvEXhVTssBj$aXtxIcfijB9hG/pjLqahFI5iVdFXI32Z6Ne9b1wBXfM=',NULL,0,'_R8Bwdt','','','',0,1,'2018-11-05 06:22:08.110216'),(138,'pbkdf2_sha256$100000$Ql6736XzJq9S$37+jBE4lvzcRR4hSySNLMolYSa+wDX8s7dQAgB7G6xM=',NULL,0,'_M9ZOIx','','','',0,1,'2018-11-19 05:15:30.567588'),(139,'pbkdf2_sha256$100000$ScyHuBuBDCwh$nyS07HtTNL89ZquKWPxqJDoAqI9VemKtOMfh0ag4CvA=','2019-03-07 08:07:15.138896',0,'test99@test.com','','','test99@test.com',0,1,'2019-03-07 07:16:09.163880'),(141,'pbkdf2_sha256$100000$B5LRiG6Redg1$CVN3wcbR93foiHvQyFz7dSLncKOaYPDLh5uIX8vB9Hg=','2019-03-07 08:16:38.502055',0,'test98@test.com','','','test98@test.com',0,1,'2019-03-07 08:13:13.304259'),(143,'pbkdf2_sha256$100000$fgls2aK0hzz7$6EfzBu937pLirADDYcb7J15ZyH5dbly+t7dRaJYijKA=','2019-03-07 08:19:01.997319',0,'test97@test.com','','','test97@test.com',0,1,'2019-03-07 08:18:15.543131'),(144,'pbkdf2_sha256$100000$PfIeRXx7FvrH$LNbL3M9dfLXlF5ty8ow/vIsA+YCSvyRyEpktTnLSG2E=','2019-05-09 02:55:07.076928',0,'donvermo@gmail.com','','','donvermo@gmail.com',0,1,'2019-05-08 06:03:40.335648'),(145,'pbkdf2_sha256$100000$LsRmFOHYIBN4$xrJUuKYXvrKRcWZ/yfb4XGS0+fEIS5e9sZTzcXMDpRc=',NULL,0,'123132131test@test.com','','','123132131test@test.com',0,1,'2019-07-10 05:51:32.511332'),(146,'pbkdf2_sha256$100000$p7BF9cOgG8o0$i+GT3zfV6lJQPvAfrxiAcr9LyHzxstuPGYXhclxNPIE=',NULL,0,'derp@derp.com','','','derp@derp.com',0,1,'2019-07-11 07:15:06.993236'),(147,'pbkdf2_sha256$100000$25BSQjXnHp7Z$et9f/a+YWLoYiijv4zCbJ6X05l2zA+TM/Gy+WS2+IKw=','2019-11-07 07:14:13.956558',0,'test900@test.com','','','test900@test.com',0,1,'2019-10-28 09:29:15.944504'),(148,'pbkdf2_sha256$100000$qYva9moncp0P$PXwZG/nwVikhe7YbbTDCHlWYkKlKmdlYCN4EnuydGFw=',NULL,0,'test03@test.com','','','test03@test.com',0,1,'2019-11-07 07:09:02.061240'),(149,'pbkdf2_sha256$100000$uSrQapzfhSm3$0rOme+tdvAgCnxoKEzVRXg4WXg1WNxO7jm20+zr8CzI=',NULL,0,'new@user.com','','','new@user.com',0,1,'2019-11-07 07:10:46.476627'),(150,'pbkdf2_sha256$100000$o3MquQxEc9dK$7wXUUH2DeiJQGuWCPJmNrw7byN+PoxrdDx9tIoXYBZ0=',NULL,0,'Chaz Wilson_stphG8','','','',0,1,'2019-11-13 09:12:16.449076'),(151,'pbkdf2_sha256$100000$pUjcPd02VoSj$03rTO7+dUQAwdKOmAlNhMPiEwTFbdShHT8MALvm0uR0=',NULL,0,'Chaz Wilson_hmtVgC','','','',0,1,'2019-11-13 09:12:16.731296'),(152,'pbkdf2_sha256$100000$c22gwEg80AIa$IWoQRYKS9ailRaZCLEQ+fInNoyo0o4l2CYV/mHaC6c0=',NULL,0,'Chaz Wilson_gvneTr','','','',0,1,'2019-11-13 09:38:22.545675'),(153,'pbkdf2_sha256$100000$yJ2GiWmbIim0$gKqGK4bStlaL9b/pCUkIO5zjLfTApq+AuU/ldhMz4aE=',NULL,0,'Chaz Wilson_XZFEvx','','','',0,1,'2019-11-19 06:45:15.028693'),(154,'pbkdf2_sha256$100000$CLSgw2KC9AdD$H4yVnazpag/qb/Adm6TBEPIWDg/EssSc9Jh4uoe9aQQ=',NULL,0,'Chaz Wilson_JgDpuH','','','',0,1,'2019-11-21 01:35:37.340924'),(155,'pbkdf2_sha256$100000$D91ZG9DOtC5p$q4N30lEyEdZSIBsjyhJsPIqg6cenacoPT0H83c1Wfsw=',NULL,0,'Chaz Wilson_tWNfPB','','','',0,1,'2019-11-21 02:35:28.402644'),(156,'pbkdf2_sha256$100000$YcpJ4q5oRcSj$/oXjO5Oeuv05wFnImBeJZ7jD89cBlYQcBAebPqx/DUg=',NULL,0,'Chaz Wilson_6VNDqF','','','',0,1,'2019-11-21 02:35:31.070539'),(157,'pbkdf2_sha256$100000$b5kG5318J5Z4$PGjnDbLANomDoV8egMDxd6hd4oPa8KoMOnr/frcLQLM=',NULL,0,'Chaz Wilson_YWKVWg','','','',0,1,'2019-11-21 02:35:32.980606'),(158,'pbkdf2_sha256$100000$DqBkcmnuh3iR$x7qBI2gUghDo9FKbcGvuwUmA2qREt9kTh4mxUKYiOfg=',NULL,0,'Chaz Wilson_HWrPuD','','','',0,1,'2019-11-21 02:35:34.731189'),(159,'pbkdf2_sha256$100000$zFk6FAZpDI6h$u8Ptmquyffn7R9CrVL5jyss/uxPSByViEuB9mOPQzY8=',NULL,0,'Chaz Wilson_EF9BnW','','','',0,1,'2019-11-21 02:35:36.067033'),(160,'pbkdf2_sha256$100000$0MuSWoXNhePE$cbYqQE9WNbT8ayG2/Inqjm0bolROUX53+q4insPv2UQ=',NULL,0,'Chaz Wilson_EGeT6Q','','','',0,1,'2019-11-21 02:35:37.294608'),(161,'pbkdf2_sha256$100000$9FTH31j3dQBf$HHO6SyvrlaqICtRjchrB810+dRETmgucqPTvPtnSPWw=',NULL,0,'Chaz Wilson_MADkPc','','','',0,1,'2019-11-21 02:35:39.033554'),(162,'pbkdf2_sha256$100000$pO59RJ0dlKkI$qtsKblrP6dOgGo2VUFwDSEWjqahAOFbjuK8h7HtjpJA=',NULL,0,'Chaz Wilson_d6FjKv','','','',0,1,'2019-11-28 02:30:55.743862'),(163,'pbkdf2_sha256$100000$WzrPapGBbo9M$rX8uExrPllKEavHt3QuS+Sb7MgP5cFkyVwzVMC7VkAc=',NULL,0,'Chaz Wilson_dQPmGv','','','',0,1,'2019-11-28 02:31:28.487548'),(164,'pbkdf2_sha256$100000$U2yQFJ0CL8Gb$SzRdSeL2DWwXbXgtOcNow+bcPtuECFFtj0X/IS663uU=',NULL,0,'Chaz Wilson_bMt9Yh','','','',0,1,'2019-11-28 02:32:12.625576'),(165,'pbkdf2_sha256$100000$GlKrhRFxisW8$738nm76PaSmbrSQaGp4F1oWWFjvHEQ3L9Z8/gNCXaoE=',NULL,0,'Chaz Wilson_4gRzGq','','','',0,1,'2019-11-28 02:41:18.628226'),(166,'pbkdf2_sha256$100000$Q7fmcQhypHBP$q7CXYNIjz6zbHq95XCdTWU8zMX1yk9qOEeGmyb5wqGs=',NULL,0,'Chaz Wilson_SZ7xw9','','','',0,1,'2019-12-02 01:34:57.173501'),(167,'pbkdf2_sha256$100000$ddoj90dirTec$WyYe0KRFNyvXrKhfZIX9jNIwf+eaLRtTGHUPnbOp1bw=',NULL,0,'Chaz Wilson_WkbPdQ','','','',0,1,'2019-12-02 01:41:45.245126'),(168,'pbkdf2_sha256$100000$INtEI8Gm4mGa$S95Y4E55hxFg/xBO6L+d7aLn4ZXLLgG9NBABLbxjPXA=',NULL,0,'Chaz Wilson_K7xYPX','','','',0,1,'2019-12-02 02:45:49.105065'),(169,'pbkdf2_sha256$100000$KrAOTPrjXe9d$oM/mBE2A9uwAykrAyEMh9Tc58zQKv/iM91ivdwV6q4k=',NULL,0,'Chaz Wilson_4jPt6h','','','',0,1,'2019-12-03 02:12:24.914099'),(170,'pbkdf2_sha256$100000$1nwFR3SoDCIU$vi7fFNERqtDi8pLy6KUvtvV2DFIPzzeKnIHoRhnJOgs=',NULL,0,'Chaz Wilson_VmvK9v','','','',0,1,'2019-12-03 02:12:25.855431'),(171,'pbkdf2_sha256$100000$037PNpVgRZGj$0B5arPG2LXFo0S2UBKbiA8BmByu+LQ4EYnHYP8KNt+M=',NULL,0,'Chaz Wilson_c4Lhzz','','','',0,1,'2019-12-03 02:16:53.466614'),(172,'pbkdf2_sha256$100000$ppWRvx1YWIds$99z1XkvNTd1TDSz30+L6i4TfZ3dBCrEV5/enJMGNZzA=',NULL,0,'Chaz Wilson_t8u6Tx','','','',0,1,'2019-12-03 02:16:59.071292'),(173,'pbkdf2_sha256$100000$agFqRUJxLFNj$HbyQG63x+NOEWcHDabiPsXkUpku15QeAoErBrZxnYl8=',NULL,0,'Chaz Wilson_quj6kC','','','',0,1,'2019-12-03 02:46:57.668609'),(174,'pbkdf2_sha256$100000$to4JnwQBTqTh$MNKSf5E1xaG3oTDw2INZsWhOhTjqQT2XSPdiVd5PSAo=',NULL,0,'Chaz Wilson_WBx6hU','','','',0,1,'2019-12-03 02:49:04.100828'),(175,'pbkdf2_sha256$100000$eoNvDcrNt8fX$Vd5LutenTzh55ynU9Gjd4pwZXH+f4emO8pX6YcvbTss=',NULL,0,'Chaz Wilson_Hr43Bb','','','',0,1,'2019-12-03 02:51:58.172478'),(176,'pbkdf2_sha256$100000$DyNFxdZnrG9M$wyZ6ppw5ujlm+sxLnpRVlFegdC0THNpcCdJUZzna/34=',NULL,0,'Chaz Wilson_9nb7PE','','','',0,1,'2019-12-03 02:51:59.181792'),(177,'pbkdf2_sha256$100000$hVj0T2Fft5og$ei4X0I/nkNuC5uk0Asw19U+IKDZYIQ5NTCE9VVmw4PU=',NULL,0,'Chaz Wilson_NpM2Dv','','','',0,1,'2019-12-03 03:03:49.638364'),(178,'pbkdf2_sha256$100000$vUhKQRfp0sBX$QF5LueEqgB394YuD0ciT8GDufCVkJW97WH+x5LzLYUQ=',NULL,0,'Chaz Wilson_dNdxXz','','','',0,1,'2019-12-03 03:03:51.286251'),(179,'pbkdf2_sha256$100000$WYLDdVYVZpdV$bBdllpTpuT3jbATGxifjkW07HFD67/l8Lu3WASl2PRI=',NULL,0,'Chaz Wilson_zbtReb','','','',0,1,'2019-12-03 03:03:52.827953'),(180,'pbkdf2_sha256$100000$RvCmNgW6lb7K$3IuXOXE/cIVHd48pRne15GWFSknDbbKMDqYj9fpIGFE=','2019-12-10 06:51:57.098784',0,'childaccount@test.com','','','childaccount@test.com',0,1,'2019-12-10 06:20:07.224615'),(181,'pbkdf2_sha256$100000$lcdyo7W06h0N$y4+2Trma1IHpNhAar4/8f7EbkhIMW/BeT3fg+lg+dzo=',NULL,0,'account@hasparent.com','','','account@hasparent.com',0,1,'2019-12-11 02:10:53.189153'),(182,'pbkdf2_sha256$100000$uOsJhsbVO44J$u32nnGAQzDCcnXbq2TfN9iQ2bTIZIP8QMGZHibbqgE4=',NULL,0,'account2@hasparent.com','','','account2@hasparent.com',0,1,'2019-12-11 02:24:16.488143'),(183,'pbkdf2_sha256$100000$2f5DXrii4XRd$z2i3L+Sx/oxH99MIz/4UenYQ0gowqR/ubkTfxQz5sqE=',NULL,0,'account3@hasparent.com','','','account3@hasparent.com',0,1,'2019-12-11 02:29:50.445303'),(184,'pbkdf2_sha256$100000$YKZa6eH4QeeZ$NqxAjpDJtzPN79fKJvWIuLQNuei0PLGuP71UQZX7oLE=',NULL,0,'account4@hasparent.com','','','account4@hasparent.com',0,1,'2019-12-11 02:36:49.550108'),(185,'pbkdf2_sha256$100000$RO175JUiPU1V$fiIg4wHudgsZsYGWOpd3Gubv+q5hansn02+3Mgppf7U=',NULL,0,'account6@hasparent.com','','','account6@hasparent.com',0,1,'2019-12-11 02:57:57.006726'),(186,'pbkdf2_sha256$100000$dPQafEoWYHeg$yjx/dxIoqGaB8QLdE5wII0BqMtjBild08dNmH85Zegk=',NULL,0,'account8@hasparent.com','','','account8@hasparent.com',0,1,'2019-12-11 03:01:00.324844'),(187,'pbkdf2_sha256$100000$Ef0cQHQFRBxX$OLRKJsITUpBZJi3XuNvMyu7le3vq2bbsSoPUjFmB8wY=',NULL,0,'account9@hasparent.com','','','account9@hasparent.com',0,1,'2019-12-11 03:02:41.218227'),(188,'pbkdf2_sha256$100000$yP1rBrg13HD5$U55NHbi3gV3jhd0MfVbvKE2F34gzj+lPDAWBRi+iT6A=',NULL,0,'account12@hasparent.com','','','account12@hasparent.com',0,1,'2019-12-11 03:19:47.209435'),(189,'pbkdf2_sha256$100000$M3DWCnt3QPWU$8iUl+D+d0g3CBSFoeaKIEq5IQyacb042X/KGqcnkbf8=',NULL,0,'account13@hasparent.com','','','account13@hasparent.com',0,1,'2019-12-11 03:22:37.228822'),(190,'pbkdf2_sha256$100000$VqMwPYtNQMrN$cnCNOJlpYdw0WqrLJlZ16vNWgGxZhohioPiclAg75OI=',NULL,0,'account14@hasparent.com','','','account14@hasparent.com',0,1,'2019-12-11 03:26:14.941463'),(191,'pbkdf2_sha256$100000$mJgzqOJ0xBov$bZWjY6q5MRTNHApZN7ma/se0tCtFcLT+0bduAw1j0UY=','2019-12-11 06:50:59.270710',0,'hasparent3@test.com','','','hasparent3@test.com',0,1,'2019-12-11 06:11:28.537930'),(192,'pbkdf2_sha256$100000$onC85zbovkmo$5QWYOereJyRmbNYwz0bpscIOPzC/hloy7lXfgT7FMQ0=','2020-01-28 02:56:36.846637',0,'test2@test.com','','','test2@test.com',0,1,'2019-12-11 08:38:22.228522'),(193,'pbkdf2_sha256$100000$XUlX0lbDJQew$4ZBx8esv3Jt/2hX166uWavE1/KVoaIvwDd5AhaX/Ucc=',NULL,0,'Chaz Wilson_yVzHyZ','','','Chaz Wilson_yVzHyZ',0,1,'2019-12-12 09:14:55.315568'),(194,'pbkdf2_sha256$100000$JDYWpPbs0Agi$RdnWD9xVowlaMAEm5XGTqUtaDBwdId2QQuPZAv5NQG8=','2019-12-13 02:24:34.927184',0,'access1@test.com','','','access1@test.com',0,1,'2019-12-13 02:22:32.212223'),(195,'pbkdf2_sha256$100000$mqaW2vuyFlcw$ea6Wyfn/wXOnrweOP0DC9j3yfXrKWrCpifunYD/bozc=',NULL,0,'access2@test.com','','','access2@test.com',0,1,'2019-12-13 02:30:03.433496'),(196,'pbkdf2_sha256$100000$BGfV0g2YAPaj$ed150arYK9UsQgErz//EQTgM/KQR3egXGFY6e+vDdco=',NULL,0,'access3@test.com','','','access3@test.com',0,1,'2019-12-13 02:39:16.116880'),(197,'pbkdf2_sha256$100000$tn5PJvmGSYT1$QW3j02fMCL+C/W7cBJepl5uoqoLn/N6cW3ELuaixV5Q=',NULL,0,'access4@test.com','','','access4@test.com',0,1,'2019-12-13 02:42:20.849739'),(198,'pbkdf2_sha256$100000$a3rr9wKHzNvx$6Ex7zSqCiEqC4YcHnzgvoPgTN1y8eNURZsm+eFfZ7eY=',NULL,0,'access5@test.com','','','access5@test.com',0,1,'2019-12-13 02:50:58.429881'),(199,'pbkdf2_sha256$100000$DYbjluu1HM6l$F+n9h2x6vkc5rLpiGiPnM3NclxF0QCQCcPhoLIfhx5k=',NULL,0,'access6@test.com','','','access6@test.com',0,1,'2019-12-13 02:53:33.854266'),(200,'pbkdf2_sha256$100000$ZjgmNIgGdjiY$r7gi5NuY1tbclW5CGK7S2zUaaN+UdT3MZfXlBiMU7Ws=',NULL,0,'access7@test.com','','','access7@test.com',0,1,'2019-12-13 02:58:35.169710'),(201,'pbkdf2_sha256$100000$RC77vwhd6k3U$9ViExxaM3i1Cs/MkdwuMfjN/6uI1TaVvCMXYOLYukB4=',NULL,0,'access8@test.com','','','access8@test.com',0,1,'2019-12-13 02:59:41.531007'),(202,'pbkdf2_sha256$100000$Exy9nDVqyHZq$7sfPC4KdPv1sPaSdhmc4b32PQSo/c9H9z7hy75eq6B8=','2019-12-13 03:07:15.025555',0,'access9@test.com','','','access9@test.com',0,1,'2019-12-13 03:00:16.417131'),(203,'pbkdf2_sha256$100000$ZNq43JUbqlgY$mvZpwaEx6BYx6pKVNs/X8HBgLopfUepUYJxp807F+ys=',NULL,0,'Chaz Wilson_Qhbkhx','','','Chaz Wilson_Qhbkhx',0,1,'2019-12-13 03:40:29.837031'),(204,'pbkdf2_sha256$100000$rkjn4MIS05Vy$hH+Vm1ooRBEUQAsTq39UTZZdsegR6c+5vYMgfncEOII=',NULL,0,'Chaz Wilson_J6xYMN','','','Chaz Wilson_J6xYMN',0,1,'2019-12-13 04:19:48.114776'),(205,'pbkdf2_sha256$100000$Jdu3hY7cLmjk$z7H0GyOWMIeryONPAsNZU+aVWi0S4EBRTG3OOYNelcU=',NULL,0,'Chaz Wilson_jRTrG8','','','Chaz Wilson_jRTrG8',0,1,'2019-12-13 04:38:47.756951'),(206,'pbkdf2_sha256$100000$K62WgvGJPVgw$bBez7oSUwuFtNrGaZ1+Q/4mcelr8ZO/hzgZrS1g2Qjg=',NULL,0,'Chaz Wilson_Qu5bux','','','Chaz Wilson_Qu5bux',0,1,'2019-12-13 04:41:51.955519'),(207,'pbkdf2_sha256$100000$3FtoLBFC4qoq$KEd1Xbyp7k0IvRAy8vDSggve6Ahrs7a2VnZHZTktXiQ=',NULL,0,'Chaz Wilson_8cMJhX','','','Chaz Wilson_8cMJhX',0,1,'2019-12-13 04:43:08.542900'),(208,'pbkdf2_sha256$100000$4fUTDLOeTHoA$34hpqOHWio/SNvVEQ1BCtbgsXaPIbXiiDZyNUS5GK7I=',NULL,0,'Chaz Wilson_MgYjvu','','','Chaz Wilson_MgYjvu',0,1,'2019-12-13 04:49:05.878385'),(209,'pbkdf2_sha256$100000$jIqlGOWU9n45$Tr1dkMPz+VKEIOZEH/in80mZTgATAGus0N+qR2PRu3Y=',NULL,0,'Chaz Wilson_mXhBJk','','','Chaz Wilson_mXhBJk',0,1,'2019-12-13 04:55:17.102415'),(210,'pbkdf2_sha256$100000$zzkhQkjCJPHW$QeuyenI3Jxe7m5j8IZhWgf8Op/Dw51BDXiJ7PPeuC88=',NULL,0,'Chaz Wilson_UVeTGJ','','','Chaz Wilson_UVeTGJ',0,1,'2019-12-13 04:56:54.272555'),(211,'pbkdf2_sha256$100000$17BosulbXRRv$BhBahaZVk9bkD5bLDJtqpaP8E3O07J6c5MxTXKNpaZg=',NULL,0,'Chaz Wilson_BdzptG','','','Chaz Wilson_BdzptG',0,1,'2019-12-13 05:03:22.396799'),(212,'pbkdf2_sha256$100000$M2onMlccVXXH$B3MqImQhS9kbXUk0KGgxl9gCfZt5jYM6/FQmhL9+fV0=',NULL,0,'Chaz Wilson_k4pEFv','','','Chaz Wilson_k4pEFv',0,1,'2019-12-13 05:04:58.807785'),(213,'pbkdf2_sha256$100000$v9mnIIHNeSfJ$tu0pnW1h+t5fwc5O3VeUKtyIx9kOtTtgjY6OXKqfY3E=',NULL,0,'Chaz Wilson_DcNgbP','','','Chaz Wilson_DcNgbP',0,1,'2019-12-13 05:09:22.193542'),(214,'pbkdf2_sha256$100000$7z3UdJ3IRnyd$IqTzvVsVgi6TsjRfNKdWK45Mthd5ReU94IX6k9F4Yns=',NULL,0,'Chaz Wilson_rjRmZD','','','Chaz Wilson_rjRmZD',0,1,'2019-12-13 05:22:28.550607'),(215,'pbkdf2_sha256$100000$nwHT0CBHQrop$iJqkjXO7BozhP0dg+fVrQaExIPqzqk0dN7OehosBWLo=',NULL,0,'Chaz Wilson_hzS88J','','','Chaz Wilson_hzS88J',0,1,'2019-12-13 06:28:31.276897'),(216,'pbkdf2_sha256$100000$AxU8dHD5ji40$W3/0E76a35qHUmH0EQI0JJ3t4rDzr1R4flK5iVZ15G4=',NULL,0,'Chaz Wilson_vhVjsm','','','Chaz Wilson_vhVjsm',0,1,'2019-12-13 06:37:58.464236'),(217,'pbkdf2_sha256$100000$BTYfIFrisKfm$pQDgKKr1Lvbcv+8vau4klWhosCFAZmxV0rJhQE5SBqM=',NULL,0,'Chaz Wilson_zgVNzy','','','Chaz Wilson_zgVNzy',0,1,'2019-12-13 06:40:43.513161'),(218,'pbkdf2_sha256$100000$PG6LRomYES5A$hcUlZLUdZrcRJS3H8WVVGCHCRfx1iejvzLh65wjTc7Y=',NULL,0,'Chaz Wilson_2ZH7ar','','','Chaz Wilson_2ZH7ar',0,1,'2019-12-13 06:43:32.309974'),(219,'pbkdf2_sha256$100000$1NHyovQNTVRA$4nvkr5tuznXmfe1IAHIyzvUjrq2SqEgsIPaOFz/Jg+o=',NULL,0,'Chaz Wilson_XS54Xa','','','Chaz Wilson_XS54Xa',0,1,'2019-12-13 06:58:55.788145'),(220,'pbkdf2_sha256$100000$efNiN5Von3OG$tu1jzlGCPfEuJegwmvkwEG8/EnAmuw1Csa4FFd02R+M=',NULL,0,'Chaz Wilson_yMLDRu','','','Chaz Wilson_yMLDRu',0,1,'2019-12-13 07:03:31.793328'),(221,'pbkdf2_sha256$100000$jwO3G4q6xqWe$XZQUO4zseRh8X/y0UGCmnAbcqREjO07vR1Tn6hlYoUo=',NULL,0,'bot@test.com','','','bot@test.com',0,1,'2019-12-16 03:15:20.149826'),(222,'pbkdf2_sha256$100000$rkN43aVIpoL1$uEC0o4Z7rdtb7V7tHgeXx0Qot1uY48NBzHah38f/a5U=',NULL,0,'bot2@test.com','','','bot2@test.com',0,1,'2019-12-16 03:17:39.234654'),(223,'pbkdf2_sha256$100000$lbn79L7jQosX$w+BctMZit7HOAjw53hNAuOpKd5zHu8xlWekNN9oseBQ=',NULL,0,'Bot3@test.com','','','Bot3@test.com',0,1,'2019-12-16 03:22:00.699249'),(224,'pbkdf2_sha256$100000$CTeBvy57H5uY$Js1lLmNwM/RdSBfk/ZvW1+3OfSP+/G1LVfn0J//35M8=',NULL,0,'Bot4@test.com','','','Bot4@test.com',0,1,'2019-12-16 03:23:39.733655'),(225,'pbkdf2_sha256$100000$MbmEkDZ7Z7lb$wGDlANSexP77msdjDdYWh8Na0QqwV9xdt5EL+VR2NeE=',NULL,0,'Bot5@test.com','','','Bot5@test.com',0,1,'2019-12-16 03:25:17.986164'),(226,'pbkdf2_sha256$100000$3d1xW6kiz9cl$oYaV9sMWg9/iHhf9U8apxXRXCI44i2wVRmMyIuWE9wg=',NULL,0,'Bot6@test.com','','','Bot6@test.com',0,1,'2019-12-16 03:26:27.222313'),(227,'pbkdf2_sha256$100000$E4EH0yrIhtgQ$gqhOJA/c6wq8jQ36xsSoffaCUJFU6Y6Lt+UWYxOMvVU=',NULL,0,'test7@yahoo.com','','','test7@yahoo.com',0,1,'2019-12-16 03:28:15.299490'),(228,'pbkdf2_sha256$100000$jaAszdG2WCyG$DNOxRpjjclE4R9GiAVJWMqtt6PtBZaw9VcpnSXK71T0=',NULL,0,'test8@yahoo.com','','','test8@yahoo.com',0,1,'2019-12-16 03:34:21.445031'),(229,'pbkdf2_sha256$100000$k114gpIoEQzq$LmR+N6j11YFrvDeIALTXE+jZbHuIqfwyk6ACmFX6fuI=','2019-12-16 03:36:28.525288',0,'test9@test.com','','','test9@test.com',0,1,'2019-12-16 03:35:46.153878'),(230,'pbkdf2_sha256$100000$eWBP2PF3qybK$3tZPLmE9Njx1qkIU7uCZsaB8Sb4DCLIrbOfcA47YSlI=','2019-12-16 04:30:01.453007',0,'test10@test.com','','','test10@test.com',0,1,'2019-12-16 03:51:03.843588'),(231,'pbkdf2_sha256$100000$D2c1zElULka0$cDYBz28uczcMoIayKdbRqlmN7iJTYEs3x5LT/nUlcWs=',NULL,0,'Chaz Wilson_FTMkGV','','','Chaz Wilson_FTMkGV',0,1,'2019-12-16 04:35:08.468287');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,7,1),(2,8,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_affiliate`
--

DROP TABLE IF EXISTS `core_affiliate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_affiliate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `tag_name` varchar(64) DEFAULT NULL,
  `url_part` varchar(64) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `start_dt` datetime(6) DEFAULT NULL,
  `end_dt` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_affiliate_vendor_branch_id_63f91a30_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `core_affiliate_vendor_branch_id_63f91a30_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_affiliate`
--

LOCK TABLES `core_affiliate` WRITE;
/*!40000 ALTER TABLE `core_affiliate` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_affiliate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_automessagecondition`
--

DROP TABLE IF EXISTS `core_automessagecondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_automessagecondition` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `is_share` tinyint(1) NOT NULL,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `auto_message_type_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_automessagecond_vendor_branch_id_2b683039_fk_core_vend` (`vendor_branch_id`),
  KEY `core_automessagecond_auto_message_type_id_90140968_fk_core_auto` (`auto_message_type_id`),
  CONSTRAINT `core_automessagecond_auto_message_type_id_90140968_fk_core_auto` FOREIGN KEY (`auto_message_type_id`) REFERENCES `core_automessagetype` (`id`),
  CONSTRAINT `core_automessagecond_vendor_branch_id_2b683039_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_automessagecondition`
--

LOCK TABLES `core_automessagecondition` WRITE;
/*!40000 ALTER TABLE `core_automessagecondition` DISABLE KEYS */;
INSERT INTO `core_automessagecondition` VALUES (1,'step message from regist_dt',1,1,'2018-06-06 12:29:07.267172','2018-06-06 12:30:39.954381',0,1,1),(2,'remind RESERVATION',1,2,'2018-06-06 12:29:32.937413','2018-06-06 12:30:21.844884',0,1,2),(3,'follow up',1,3,'2018-06-06 12:30:05.817585','2018-06-06 12:30:05.817624',0,1,3),(4,'登録日',1,NULL,'2018-06-30 14:31:14.715874','2018-06-30 14:31:14.715925',0,2,1),(5,'予約日',1,NULL,'2018-06-30 14:31:14.723954','2018-06-30 14:31:14.723999',0,2,2),(6,'訪問日',1,NULL,'2018-06-30 14:31:14.725977','2018-06-30 14:31:14.726012',0,2,3),(7,'登録日からの',1,NULL,'2018-06-30 14:35:29.858111','2018-06-30 14:35:29.858176',0,3,1),(8,'予約日前のー',1,NULL,'2018-06-30 14:35:29.870565','2018-06-30 14:35:29.870630',0,3,2),(9,'訪問日の',1,NULL,'2018-06-30 14:35:29.873896','2018-06-30 14:35:29.873944',0,3,3),(10,'ll',1,NULL,'2018-06-30 14:37:04.055886','2018-06-30 14:37:04.055942',0,4,1),(11,'l',1,NULL,'2018-06-30 14:37:04.059961','2018-06-30 14:37:04.060020',0,4,2),(12,'l',1,NULL,'2018-06-30 14:37:04.063556','2018-06-30 14:37:04.063624',0,4,3),(13,'登録日',1,NULL,'2018-07-02 12:53:51.829181','2018-07-02 12:53:51.829246',0,5,1),(14,'予約日前のー',1,NULL,'2018-07-02 12:53:51.838559','2018-07-02 12:53:51.838609',0,5,2),(15,'訪問日の',1,NULL,'2018-07-02 12:53:51.839755','2018-07-02 12:53:51.839789',0,5,3),(16,'登録日',1,NULL,'2018-07-02 12:55:02.837036','2018-07-02 12:55:02.837099',0,6,1),(17,'予約日前のー',1,NULL,'2018-07-02 12:55:02.840483','2018-07-02 12:55:02.840548',0,6,2),(18,'訪問日の',1,NULL,'2018-07-02 12:55:02.841863','2018-07-02 12:55:02.841908',0,6,3),(19,'登録日',1,NULL,'2018-07-02 12:55:26.038532','2018-07-02 12:55:26.038597',0,7,1),(20,'予約日前のー',1,NULL,'2018-07-02 12:55:26.044065','2018-07-02 12:55:26.044112',0,7,2),(21,'訪問日の',1,NULL,'2018-07-02 12:55:26.046391','2018-07-02 12:55:26.046428',0,7,3),(22,'登録日',1,NULL,'2018-07-02 12:56:05.063910','2018-07-02 12:56:05.063945',0,8,1),(23,'予約日前のー',1,NULL,'2018-07-02 12:56:05.066024','2018-07-02 12:56:05.066090',0,8,2),(24,'訪問日の',1,NULL,'2018-07-02 12:56:05.072693','2018-07-02 12:56:05.072761',0,8,3),(25,'登録日',1,NULL,'2018-07-02 12:57:42.120476','2018-07-02 12:57:42.120551',0,9,1),(26,'予約日前のー',1,NULL,'2018-07-02 12:57:42.128559','2018-07-02 12:57:42.128623',0,9,2),(27,'訪問日の',1,NULL,'2018-07-02 12:57:42.129983','2018-07-02 12:57:42.130019',0,9,3),(28,'登録日',1,NULL,'2018-07-02 12:59:50.524647','2018-07-02 12:59:50.524713',0,10,1),(29,'予約日前のー',1,NULL,'2018-07-02 12:59:50.526542','2018-07-02 12:59:50.526602',0,10,2),(30,'訪問日の',1,NULL,'2018-07-02 12:59:50.528903','2018-07-02 12:59:50.528946',0,10,3),(31,'kk',1,NULL,'2018-07-02 13:10:47.680568','2018-07-02 13:10:47.680618',0,11,1),(32,'k',1,NULL,'2018-07-02 13:10:47.681895','2018-07-02 13:10:47.681958',0,11,2),(33,'k',1,NULL,'2018-07-02 13:10:47.684641','2018-07-02 13:10:47.684687',0,11,3),(37,'l',1,NULL,'2018-07-02 13:12:46.238305','2018-07-02 13:12:46.238417',0,13,1),(38,'l',1,NULL,'2018-07-02 13:12:46.239421','2018-07-02 13:12:46.239477',0,13,2),(39,'l',1,NULL,'2018-07-02 13:12:46.241920','2018-07-02 13:12:46.241987',0,13,3),(43,'l',1,NULL,'2018-07-02 13:31:25.602762','2018-07-02 13:31:25.602832',0,15,1),(44,'l',1,NULL,'2018-07-02 13:31:25.609243','2018-07-02 13:31:25.609307',0,15,2),(45,'l',1,NULL,'2018-07-02 13:31:25.610207','2018-07-02 13:31:25.610257',0,15,3),(46,'jj',1,NULL,'2018-07-02 13:32:56.651092','2018-07-02 13:32:56.651161',0,16,1),(47,'j',1,NULL,'2018-07-02 13:32:56.654099','2018-07-02 13:32:56.654162',0,16,2),(48,'j',1,NULL,'2018-07-02 13:32:56.656731','2018-07-02 13:32:56.656803',0,16,3),(49,'hh',1,NULL,'2018-07-02 13:34:24.018565','2018-07-02 13:34:24.018635',0,17,1),(50,'h',1,NULL,'2018-07-02 13:34:24.019589','2018-07-02 13:34:24.019643',0,17,2),(51,'h',1,NULL,'2018-07-02 13:34:24.020555','2018-07-02 13:34:24.020607',0,17,3),(52,'i',1,NULL,'2018-07-02 13:35:51.476061','2018-07-02 13:35:51.476120',0,18,1),(53,'i',1,NULL,'2018-07-02 13:35:51.479457','2018-07-02 13:35:51.479498',0,18,2),(54,'i',1,NULL,'2018-07-02 13:35:51.480129','2018-07-02 13:35:51.480164',0,18,3),(67,'登録日時',1,NULL,'2018-08-20 08:40:21.307067','2018-08-20 08:40:21.307087',0,7,1),(68,'das',1,NULL,'2018-08-20 08:40:21.307478','2018-08-20 08:40:21.307497',0,7,2),(69,'asd',1,NULL,'2018-08-20 08:40:21.307857','2018-08-20 08:40:21.307879',0,7,3);
/*!40000 ALTER TABLE `core_automessagecondition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_automessagecontroller`
--

DROP TABLE IF EXISTS `core_automessagecontroller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_automessagecontroller` (
  `id` int NOT NULL AUTO_INCREMENT,
  `messaging_api_param_json` longtext,
  `run_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `messaging_api_type_id` int DEFAULT NULL,
  `admin_text` longtext,
  `auto_message_trigger_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_automessagecont_messaging_api_type_i_04e6c6b6_fk_core_mess` (`messaging_api_type_id`),
  KEY `core_automessagecont_auto_message_trigger_b4406c85_fk_core_auto` (`auto_message_trigger_id`),
  CONSTRAINT `core_automessagecont_auto_message_trigger_b4406c85_fk_core_auto` FOREIGN KEY (`auto_message_trigger_id`) REFERENCES `core_automessagetrigger` (`id`),
  CONSTRAINT `core_automessagecont_messaging_api_type_i_04e6c6b6_fk_core_mess` FOREIGN KEY (`messaging_api_type_id`) REFERENCES `core_messagingapitype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=216 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_automessagecontroller`
--

LOCK TABLES `core_automessagecontroller` WRITE;
/*!40000 ALTER TABLE `core_automessagecontroller` DISABLE KEYS */;
INSERT INTO `core_automessagecontroller` VALUES (83,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test2\'}',1,'2018-06-18 03:08:02.354715','2018-06-18 03:08:02.354782',0,1,NULL,2),(192,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'registration datetime \\r\\nafter 1 day test\'}',1,'2018-07-09 02:48:38.397704','2018-07-09 02:48:38.397768',0,1,NULL,12),(193,'{\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\'}',2,'2018-07-09 02:48:38.402574','2018-07-09 02:48:38.402626',0,5,NULL,12),(194,'{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'test1\', \'image_url\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\', \'subtitle\': \'test2\', \'actions\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\'}]}',3,'2018-07-09 02:48:38.405712','2018-07-09 02:48:38.405791',0,3,NULL,12),(204,'{\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\'}',1,'2018-08-17 03:16:18.961189','2018-08-17 03:16:18.961215',0,5,NULL,1),(205,'{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'Title 1\', \'image_url\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/static/core/assets/images/logo.png\', \'subtitle\': \'Description 1\', \'actions\': \'https://smartsec.co\'}, {\'title\': \'Title 2\', \'image_url\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/static/core/assets/images/logo.png\', \'subtitle\': \'Description 2\', \'actions\': \'https://smartsec.co\'}, {\'title\': \'titile1\', \'image_url\': \'https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\', \'subtitle\': \'subtitle1111\', \'actions\': \'https://sushitimes.co\'}]}',2,'2018-08-17 03:16:18.962450','2018-08-17 03:16:18.962473',0,3,NULL,1),(206,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test text de\'}',3,'2018-08-17 03:16:18.963871','2018-08-17 03:16:18.963895',0,1,NULL,1),(215,'{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'test\', \'image_url\': \'test\', \'subtitle\': \'test\', \'actions\': \'https://www.test.com\'}]}',1,'2018-08-17 05:21:49.532769','2018-08-17 05:21:49.532793',0,3,NULL,9);
/*!40000 ALTER TABLE `core_automessagecontroller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_automessagehistory`
--

DROP TABLE IF EXISTS `core_automessagehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_automessagehistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_text` varchar(64) DEFAULT NULL,
  `send_dt` datetime(6) DEFAULT NULL,
  `send_user_count` int DEFAULT NULL,
  `send_user_id_csv` varchar(64) DEFAULT NULL,
  `selected_tag_csv` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auto_message_condition_id` int DEFAULT NULL,
  `auto_message_trigger_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `message_status_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_automessagehist_vendor_branch_id_902aa77f_fk_core_vend` (`vendor_branch_id`),
  KEY `core_automessagehist_auto_message_conditi_934c2d65_fk_core_auto` (`auto_message_condition_id`),
  KEY `core_automessagehist_auto_message_trigger_903b7d07_fk_core_auto` (`auto_message_trigger_id`),
  KEY `core_automessagehist_message_status_id_c22482e1_fk_core_mess` (`message_status_id`),
  CONSTRAINT `core_automessagehist_auto_message_conditi_934c2d65_fk_core_auto` FOREIGN KEY (`auto_message_condition_id`) REFERENCES `core_automessagecondition` (`id`),
  CONSTRAINT `core_automessagehist_auto_message_trigger_903b7d07_fk_core_auto` FOREIGN KEY (`auto_message_trigger_id`) REFERENCES `core_automessagetrigger` (`id`),
  CONSTRAINT `core_automessagehist_message_status_id_c22482e1_fk_core_mess` FOREIGN KEY (`message_status_id`) REFERENCES `core_messagestatus` (`id`),
  CONSTRAINT `core_automessagehist_vendor_branch_id_902aa77f_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_automessagehistory`
--

LOCK TABLES `core_automessagehistory` WRITE;
/*!40000 ALTER TABLE `core_automessagehistory` DISABLE KEYS */;
INSERT INTO `core_automessagehistory` VALUES (50,NULL,'2018-07-03 05:51:03.879326',2,'8,9',NULL,'2018-07-03 05:51:03.991854','2018-07-03 05:51:04.001582',0,1,1,1,NULL);
/*!40000 ALTER TABLE `core_automessagehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_automessagetrigger`
--

DROP TABLE IF EXISTS `core_automessagetrigger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_automessagetrigger` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trigger_days_num` int DEFAULT NULL,
  `is_trigger_after` tinyint(1) NOT NULL,
  `trigger_time` time(6) DEFAULT NULL,
  `title_name` varchar(128) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auto_message_condition_id` int DEFAULT NULL,
  `message_status_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_automessagetrig_auto_message_conditi_4d471af8_fk_core_auto` (`auto_message_condition_id`),
  KEY `core_automessagetrig_message_status_id_d3d135c0_fk_core_mess` (`message_status_id`),
  CONSTRAINT `core_automessagetrig_auto_message_conditi_4d471af8_fk_core_auto` FOREIGN KEY (`auto_message_condition_id`) REFERENCES `core_automessagecondition` (`id`),
  CONSTRAINT `core_automessagetrig_message_status_id_d3d135c0_fk_core_mess` FOREIGN KEY (`message_status_id`) REFERENCES `core_messagestatus` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_automessagetrigger`
--

LOCK TABLES `core_automessagetrigger` WRITE;
/*!40000 ALTER TABLE `core_automessagetrigger` DISABLE KEYS */;
INSERT INTO `core_automessagetrigger` VALUES (1,1,1,'02:50:00.000000','registration date','2018-06-08 13:19:17.014802','2018-12-06 03:07:36.915287',0,1,3),(2,1,0,'12:00:00.000000','remind','2018-06-08 13:19:24.478977','2018-06-18 03:08:05.977096',0,2,3),(3,3,1,'14:14:00.000000','follow up','2018-06-12 06:22:24.354185','2018-06-12 06:22:24.354227',0,3,3),(4,13,1,'13:11:00.000000','testing add','2018-06-12 08:08:38.551443','2018-06-12 08:48:58.010218',1,1,1),(5,NULL,1,NULL,NULL,'2018-06-13 07:39:28.739640','2018-06-13 08:02:20.323316',1,1,1),(6,NULL,1,NULL,NULL,'2018-06-13 07:41:06.054960','2018-06-13 08:02:21.464775',1,1,1),(7,NULL,1,NULL,NULL,'2018-06-13 07:47:36.770466','2018-06-13 09:08:43.536677',1,1,1),(8,NULL,1,NULL,NULL,'2018-06-13 08:02:23.915964','2018-06-13 08:05:47.844039',1,1,1),(9,123,0,'13:13:00.000000','test123','2018-06-13 09:08:56.679843','2018-08-17 05:22:46.178786',1,1,3),(10,NULL,1,NULL,NULL,'2018-06-14 04:26:24.089110','2018-06-15 00:58:03.629331',1,1,1),(11,12,1,'12:12:00.000000','test','2018-06-14 07:26:16.707540','2018-06-15 00:58:56.894609',1,1,3),(12,1,1,'10:28:00.000000','test0002','2018-06-14 07:27:23.769425','2018-12-06 01:50:30.659854',0,1,3),(13,NULL,1,NULL,NULL,'2018-07-13 07:21:46.806051','2018-08-01 02:00:03.087730',1,1,1),(14,3,1,'03:33:00.000000','test','2018-08-01 02:00:23.944866','2018-08-01 02:00:44.369211',1,1,3),(15,1,1,'12:12:00.000000','esrt123','2018-08-17 03:16:23.942268','2018-08-17 03:16:43.318605',1,1,1),(16,NULL,1,NULL,NULL,'2018-08-17 03:24:39.799802','2018-08-17 05:08:07.352415',1,1,1),(17,NULL,1,NULL,NULL,'2018-08-17 03:59:36.366602','2018-08-17 05:08:10.345274',1,1,1),(18,NULL,1,NULL,NULL,'2018-08-17 03:59:37.305933','2018-08-17 05:08:13.190494',1,1,1),(19,NULL,1,NULL,NULL,'2018-08-17 03:59:41.387382','2018-08-17 05:08:16.055591',1,1,1),(20,NULL,1,NULL,NULL,'2018-09-03 08:43:33.891272','2018-09-18 02:30:10.699348',1,1,1),(21,NULL,1,NULL,NULL,'2018-09-18 02:30:05.752024','2018-09-18 02:30:18.443477',1,1,1),(22,NULL,1,NULL,NULL,'2018-09-18 02:30:13.145719','2018-11-30 08:23:46.245004',1,1,1);
/*!40000 ALTER TABLE `core_automessagetrigger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_automessagetype`
--

DROP TABLE IF EXISTS `core_automessagetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_automessagetype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_automessagetype`
--

LOCK TABLES `core_automessagetype` WRITE;
/*!40000 ALTER TABLE `core_automessagetype` DISABLE KEYS */;
INSERT INTO `core_automessagetype` VALUES (1,'Registration Date','2018-06-06 12:16:04.698391','2018-06-06 12:16:04.698560',0),(2,'RESEVATION DATA','2018-06-06 12:16:17.779669','2018-06-06 12:16:21.087210',0),(3,'LAST VISIT','2018-06-06 12:16:37.149344','2018-06-06 12:16:37.149386',0);
/*!40000 ALTER TABLE `core_automessagetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduser`
--

DROP TABLE IF EXISTS `core_enduser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `django_pass_cd` varchar(2048) DEFAULT NULL,
  `last_name` varchar(64) DEFAULT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `last_name_kana` varchar(64) DEFAULT NULL,
  `first_name_kana` varchar(64) DEFAULT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `age` varchar(25) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `email` varchar(2048) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `prefecture` varchar(32) DEFAULT NULL,
  `address1` varchar(256) DEFAULT NULL,
  `address2` varchar(256) DEFAULT NULL,
  `tel1` varchar(32) DEFAULT NULL,
  `tel2` varchar(32) DEFAULT NULL,
  `admin_text` longtext,
  `last_login_dt` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auth_user_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `end_user_state_id` int DEFAULT NULL,
  `reservation_data_json` longtext,
  `attribute_json` longtext,
  `subscribed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_enduser_auth_user_id_6cb647f9_fk_auth_user_id` (`auth_user_id`),
  KEY `core_enduser_vendor_branch_id_53f71efe_fk_core_vendorbranch_id` (`vendor_branch_id`),
  KEY `core_enduser_end_user_state_id_0574a7f5_fk_core_enduserstate_id` (`end_user_state_id`),
  CONSTRAINT `core_enduser_auth_user_id_6cb647f9_fk_auth_user_id` FOREIGN KEY (`auth_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `core_enduser_end_user_state_id_0574a7f5_fk_core_enduserstate_id` FOREIGN KEY (`end_user_state_id`) REFERENCES `core_enduserstate` (`id`),
  CONSTRAINT `core_enduser_vendor_branch_id_53f71efe_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduser`
--

LOCK TABLES `core_enduser` WRITE;
/*!40000 ALTER TABLE `core_enduser` DISABLE KEYS */;
INSERT INTO `core_enduser` VALUES (5,'XcKGVGOu43','Kawajiri','Jun','test','test','male','30','2018-06-14','test2@test.com','0091','東京都','158','test','test','test','test','2018-06-14 06:09:22.000000','2018-06-05 04:16:30.780513','2018-08-08 06:21:02.342240',0,6,1,1,'test',NULL,1),(6,'111','test','test','test','test','male',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,6,1,1,NULL,NULL,1),(7,'CFn7HQq9Av','Bruning','Martijn',NULL,NULL,'male','',NULL,'Test@test.com','','','','','',NULL,'',NULL,'2018-07-02 08:11:09.299837','2018-08-02 04:44:27.425250',0,10,1,1,NULL,NULL,1),(8,'jETTuLwsAz','test','Martin',NULL,NULL,'','61','1999-11-11','','','','','',NULL,NULL,'',NULL,'2018-07-30 01:41:47.899886','2018-09-03 07:50:22.537993',0,11,1,1,NULL,NULL,1),(9,'06JhfN9GEI',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 05:59:10.776908','2018-12-03 06:40:36.053502',1,17,1,1,NULL,NULL,1),(10,'i5JnMTkjzs',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 05:59:48.453902','2018-11-05 05:59:48.453932',1,18,1,1,NULL,NULL,1),(11,'oqoHN6g8Xv',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:01:27.803075','2018-11-29 03:01:38.574620',1,19,1,1,NULL,NULL,1),(12,'h9bBV7g1Q6',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:03:03.732694','2018-11-05 06:05:05.120355',1,20,1,1,NULL,NULL,1),(13,'vRKAjM8Hbn',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:15.566189','2018-11-05 06:10:15.566599',1,21,1,1,NULL,NULL,1),(14,'IfV3K26Xkt',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:19.052710','2018-11-05 06:10:19.052991',1,22,1,1,NULL,NULL,1),(15,'iQbgl1zTId',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:22.458229','2018-11-05 06:10:22.458492',1,23,1,1,NULL,NULL,1),(16,'bm5jGb4vaV',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:25.798355','2018-11-05 06:10:25.798623',1,24,1,1,NULL,NULL,1),(17,'U5HMoGPVG9',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:28.797272','2018-11-05 06:10:28.797524',1,25,1,1,NULL,NULL,1),(18,'Awq8jBc3de',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:32.195901','2018-11-05 06:10:32.196694',1,26,1,1,NULL,NULL,1),(19,'A40PjWAZHF',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:35.298003','2018-11-05 06:10:35.298258',1,27,1,1,NULL,NULL,1),(20,'dQMGUocYBy',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:38.818816','2018-11-05 06:10:38.819076',1,28,1,1,NULL,NULL,1),(21,'JqKgymcev2',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:42.501101','2018-11-05 06:10:42.501348',1,29,1,1,NULL,NULL,1),(22,'GTRHyDbwO3',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:45.677961','2018-11-05 06:10:45.678221',1,30,1,1,NULL,NULL,1),(23,'fTCkFpBMdL',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:10:55.535061','2018-11-05 06:10:55.535318',1,31,1,1,NULL,NULL,1),(24,'YD3t2eiql0',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:01.579179','2018-11-05 06:11:01.579489',1,32,1,1,NULL,NULL,1),(25,'uREUf05Tc4',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:04.590212','2018-11-05 06:11:04.590548',1,33,1,1,NULL,NULL,1),(26,'JXrEIh2Evi',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:07.937298','2018-11-05 06:11:07.937577',1,34,1,1,NULL,NULL,1),(27,'oEXmoNYtyI',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:11.762898','2018-11-05 06:11:11.763170',1,35,1,1,NULL,NULL,1),(28,'2oIi7Zlhtr',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:15.620171','2018-11-05 06:11:15.620478',1,36,1,1,NULL,NULL,1),(29,'ng2eaARhs9',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:19.303182','2018-11-05 06:11:19.303434',1,37,1,1,NULL,NULL,1),(30,'RnGvLcXnw9',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:22.601898','2018-11-05 06:11:22.602279',1,38,1,1,NULL,NULL,1),(31,'PGmoDLrbmq',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:31.155027','2018-11-05 06:11:31.155328',1,39,1,1,NULL,NULL,1),(32,'ngZy3kBO5J',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:34.027998','2018-11-05 06:11:34.028258',1,40,1,1,NULL,NULL,1),(33,'F9EMVdjRsc',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:38.471693','2018-11-05 06:11:38.472091',1,41,1,1,NULL,NULL,1),(34,'glXEcJKDYe',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:43.241903','2018-11-05 06:11:43.242183',1,42,1,1,NULL,NULL,1),(35,'BmsJbm73J6',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:48.633501','2018-11-05 06:11:48.633782',1,43,1,1,NULL,NULL,1),(36,'U6z3IDSh6K',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:54.298713','2018-11-05 06:11:54.299043',1,44,1,1,NULL,NULL,1),(37,'oJ8PthQSFJ',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:11:57.910831','2018-11-05 06:11:57.911289',1,45,1,1,NULL,NULL,1),(38,'ylp64OTEm5',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:01.100657','2018-11-05 06:12:01.100902',1,46,1,1,NULL,NULL,1),(39,'ndeRNjrhEy',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:06.474947','2018-11-05 06:12:06.475199',1,47,1,1,NULL,NULL,1),(40,'yj1mDV5jtI',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:09.791060','2018-11-05 06:12:09.791306',1,48,1,1,NULL,NULL,1),(41,'66KQd3qrJR',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:12.783489','2018-11-05 06:12:12.783742',1,49,1,1,NULL,NULL,1),(42,'u4zQtES3tB',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:16.520759','2018-11-05 06:12:16.521010',1,50,1,1,NULL,NULL,1),(43,'BStmM5fQ0h',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:19.844636','2018-11-05 06:12:19.844966',1,51,1,1,NULL,NULL,1),(44,'0YUPiT5YHT',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:23.454647','2018-11-05 06:12:23.454901',1,52,1,1,NULL,NULL,1),(45,'pJQ4LXCiJn',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:27.942834','2018-11-05 06:12:27.943076',1,53,1,1,NULL,NULL,1),(46,'t7hHAsXFBB',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:40.134992','2018-11-05 06:12:40.135247',1,54,1,1,NULL,NULL,1),(47,'YlhoAibmnu',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:43.720110','2018-11-05 06:12:43.720363',1,55,1,1,NULL,NULL,1),(48,'jQZK1a6QgY',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:47.408598','2018-11-05 06:12:47.408852',1,56,1,1,NULL,NULL,1),(49,'yen3D7fJKC',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:50.909936','2018-11-05 06:12:50.910186',1,57,1,1,NULL,NULL,1),(50,'W3tvt0pGGH',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:54.265257','2018-11-05 06:12:54.265560',1,58,1,1,NULL,NULL,1),(51,'ChUacGou2w',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:12:56.996285','2018-11-05 06:12:56.996546',1,59,1,1,NULL,NULL,1),(52,'m9oyDzMTzL',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:03.127290','2018-11-05 06:13:03.127520',1,60,1,1,NULL,NULL,1),(53,'3kfFuPh7fI',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:06.713059','2018-11-05 06:13:06.713386',1,61,1,1,NULL,NULL,1),(54,'Qmh613pKL2',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:10.741665','2018-11-05 06:13:10.741917',1,62,1,1,NULL,NULL,1),(55,'I5EX0xLJ7D',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:13.803083','2018-11-05 06:13:13.803336',1,63,1,1,NULL,NULL,1),(56,'kqS3B9QBkw',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:17.126568','2018-11-05 06:13:17.126990',1,64,1,1,NULL,NULL,1),(57,'FsDia5keTx',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:21.514154','2018-11-05 06:13:21.514491',1,65,1,1,NULL,NULL,1),(58,'AWUVjbHWGr',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:27.692149','2018-11-05 06:13:27.692404',1,66,1,1,NULL,NULL,1),(59,'NtRuporw86',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:30.562274','2018-11-05 06:13:30.562586',1,67,1,1,NULL,NULL,1),(60,'AiAAkAExLP',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:36.808333','2018-11-05 06:13:36.808587',1,68,1,1,NULL,NULL,1),(61,'RtAedwbWHp',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:40.162625','2018-11-05 06:13:40.162869',1,69,1,1,NULL,NULL,1),(62,'7JziI6bKhx',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:43.507010','2018-11-05 06:13:43.507272',1,70,1,1,NULL,NULL,1),(63,'H4RNdtndhg',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:46.919898','2018-11-05 06:13:46.920218',1,71,1,1,NULL,NULL,1),(64,'GjtSyVVxwU',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:13:51.617184','2018-11-05 06:13:51.617444',1,72,1,1,NULL,NULL,1),(65,'zhj0yOgw90',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:04.789347','2018-11-05 06:14:04.789602',1,73,1,1,NULL,NULL,1),(66,'v34XKi5knP',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:13.898945','2018-11-05 06:14:13.899178',1,74,1,1,NULL,NULL,1),(67,'64G7kAwmIP',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:16.782139','2018-11-05 06:14:16.782414',1,75,1,1,NULL,NULL,1),(68,'fFAZ9kA7M4',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:21.718735','2018-11-05 06:14:21.718981',1,76,1,1,NULL,NULL,1),(69,'I6qETM3qL0',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:25.477158','2018-11-05 06:14:25.477465',1,77,1,1,NULL,NULL,1),(70,'p3CChonvmc',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:29.204251','2018-11-05 06:14:29.204531',1,78,1,1,NULL,NULL,1),(71,'oJhE9DC9lL',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:39.853766','2018-11-05 06:14:39.854028',1,79,1,1,NULL,NULL,1),(72,'00If7yMElh',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:45.055511','2018-11-05 06:14:45.055766',1,80,1,1,NULL,NULL,1),(73,'ontAg21HJd',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:14:48.683871','2018-11-05 06:14:48.684301',1,81,1,1,NULL,NULL,1),(74,'ZVc7NtHQdP',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:00.432666','2018-11-05 06:15:00.432921',1,82,1,1,NULL,NULL,1),(75,'lB1yNpBqGp',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:03.244563','2018-11-05 06:15:03.244803',1,83,1,1,NULL,NULL,1),(76,'zFheoXxLrF',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:11.097861','2018-11-05 06:15:11.098111',1,84,1,1,NULL,NULL,1),(77,'cU2PB57N7X',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:14.477708','2018-11-29 03:01:36.511903',1,85,1,1,NULL,NULL,1),(78,'r7PIPSflRU',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:20.769106','2018-11-05 06:15:20.769436',1,86,1,1,NULL,NULL,1),(79,'OQTu5Wf0dN',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:25.129552','2018-11-05 06:15:25.129876',1,87,1,1,NULL,NULL,1),(80,'SXAYDM33Qs',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:28.679036','2018-11-05 06:15:28.679267',1,88,1,1,NULL,NULL,1),(81,'YuvruaSoEh',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:32.111320','2018-11-05 06:15:32.111553',1,89,1,1,NULL,NULL,1),(82,'MyRPOXUoCR',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:35.530263','2018-11-05 06:15:35.530681',1,90,1,1,NULL,NULL,1),(83,'TO3AdrL7cY',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:39.385371','2018-11-05 06:15:39.385665',1,91,1,1,NULL,NULL,1),(84,'GXlujpPEfE',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:42.920322','2018-11-05 06:15:42.920572',1,92,1,1,NULL,NULL,1),(85,'rJEjoAcEI4',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:46.371442','2018-11-05 06:15:46.371685',1,93,1,1,NULL,NULL,1),(86,'E3WfwiWGQn',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:55.783816','2018-11-05 06:15:55.784070',1,94,1,1,NULL,NULL,1),(87,'gkV4RarSaD',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:15:59.077109','2018-11-05 06:15:59.077470',1,95,1,1,NULL,NULL,1),(88,'mGsUT8HFkB',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:03.852984','2018-11-05 06:16:03.853289',1,96,1,1,NULL,NULL,1),(89,'w94Iyfe688',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:07.623673','2018-11-05 06:16:07.623928',1,97,1,1,NULL,NULL,1),(90,'iPqLJJX1Jh',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:12.992152','2018-11-05 06:16:12.992409',1,98,1,1,NULL,NULL,1),(91,'Uc4qztyArG',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:24.038126','2018-11-05 06:16:24.038363',1,99,1,1,NULL,NULL,1),(92,'Ajq11LxTBC',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:32.389386','2018-11-05 06:16:32.389635',1,100,1,1,NULL,NULL,1),(93,'ZBYJxuFO3N',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:35.736992','2018-11-05 06:16:35.737248',1,101,1,1,NULL,NULL,1),(94,'fT2fTW5mKO',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:40.959559','2018-11-05 06:16:40.959910',1,102,1,1,NULL,NULL,1),(95,'Kiv2I652WH',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:46.832989','2018-11-05 06:16:46.833244',1,103,1,1,NULL,NULL,1),(96,'X1wBAsyDmK',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:50.392531','2018-11-05 06:16:50.392800',1,104,1,1,NULL,NULL,1),(97,'hAnuYJQWiz',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:16:57.380757','2018-11-05 06:16:57.381070',1,105,1,1,NULL,NULL,1),(98,'kPsrtVFC2E',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:01.351903','2018-11-05 06:17:01.352139',1,106,1,1,NULL,NULL,1),(99,'fsJ7dXm2Gm',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:04.330866','2018-11-05 06:17:04.331273',1,107,1,1,NULL,NULL,1),(100,'yQWqrSKWom',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:10.374951','2018-11-05 06:17:10.375182',1,108,1,1,NULL,NULL,1),(101,'9SlF1x4rdg',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:15.408273','2018-11-05 06:17:15.408557',1,109,1,1,NULL,NULL,1),(102,'qTOAD4aAby',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:19.154867','2018-11-05 06:17:19.155122',1,110,1,1,NULL,NULL,1),(103,'hWkud2Oh7x',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:21.975047','2018-11-05 06:17:21.975317',1,111,1,1,NULL,NULL,1),(104,'XnE92M2qSo',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:25.708104','2018-11-05 06:17:25.708362',1,112,1,1,NULL,NULL,1),(105,'QampqmUPea',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:31.670651','2018-11-05 06:17:31.670894',1,113,1,1,NULL,NULL,1),(106,'O4BOSAX67C',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:35.573592','2018-11-05 06:17:35.573853',1,114,1,1,NULL,NULL,1),(107,'tcIfFWVrSs',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:39.362166','2018-11-05 06:17:39.362435',1,115,1,1,NULL,NULL,1),(108,'EztnTyIOjj',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:42.786162','2018-11-05 06:17:42.786418',1,116,1,1,NULL,NULL,1),(109,'fYak2qU2Jx',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:46.354330','2018-11-05 06:17:46.354635',1,117,1,1,NULL,NULL,1),(110,'VO9XZWRdpf',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:49.743722','2018-11-05 06:17:49.743954',1,118,1,1,NULL,NULL,1),(111,'j12uuK382U',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:53.116364','2018-11-05 06:17:53.116609',1,119,1,1,NULL,NULL,1),(112,'3c32YqOk3A',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:17:56.882356','2018-11-05 06:17:56.882626',1,120,1,1,NULL,NULL,1),(113,'Z7IVOAwIcu',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:01.625832','2018-11-05 06:18:01.626239',1,121,1,1,NULL,NULL,1),(114,'4sAZAy2kgf',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:05.405995','2018-11-05 06:18:05.406294',1,122,1,1,NULL,NULL,1),(115,'yJTcyv81kv',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:11.660028','2018-11-05 06:18:11.660336',1,123,1,1,NULL,NULL,1),(116,'Fq6rvHC3Hp',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:21.813417','2018-11-05 06:18:21.813835',1,124,1,1,NULL,NULL,1),(117,'30Urhemkdb',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:34.091568','2018-11-05 06:18:34.091860',1,125,1,1,NULL,NULL,1),(118,'EYnHJcQtBI',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:43.325579','2018-11-05 06:18:43.325896',1,126,1,1,NULL,NULL,1),(119,'ztMAWQxU9O',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:46.264508','2018-11-05 06:18:46.264761',1,127,1,1,NULL,NULL,1),(120,'qL1FfG0kOf',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:49.334164','2018-11-05 06:18:49.334415',1,128,1,1,NULL,NULL,1),(121,'ATRWOgIDFj',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:52.861812','2018-11-05 06:18:52.862085',1,129,1,1,NULL,NULL,1),(122,'L4Vwi2XJio',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:55.944010','2018-11-05 06:18:55.944271',1,130,1,1,NULL,NULL,1),(123,'vyWo77lpib',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:18:59.979487','2018-11-05 06:18:59.979751',1,131,1,1,NULL,NULL,1),(124,'79OIXcIhL8',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:19:03.877873','2018-11-05 06:19:03.878136',1,132,1,1,NULL,NULL,1),(125,'h9J2rHMg47',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:19:14.746051','2018-11-05 06:19:14.746327',1,133,1,1,NULL,NULL,1),(126,'Wyn9XjJ3Fb',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:19:19.834777','2018-11-05 06:19:19.835251',1,134,1,1,NULL,NULL,1),(127,'VA62eI6Kio',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:19:24.560394','2018-11-05 06:19:24.560647',1,135,1,1,NULL,NULL,1),(128,'Up1hbbUAkV',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:19:37.507454','2018-11-29 03:01:32.425328',1,136,1,1,NULL,NULL,1),(129,'Z0nzVHCrxz',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-05 06:22:08.217203','2018-11-29 02:57:11.776902',1,137,1,1,NULL,NULL,1),(130,'dHaCj7LkvR','Doe','John',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-19 05:15:30.662351','2018-11-29 02:56:56.958161',1,138,1,1,NULL,NULL,1);
/*!40000 ALTER TABLE `core_enduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserautomessage`
--

DROP TABLE IF EXISTS `core_enduserautomessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserautomessage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message_target_dt` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auto_message_type_id` int DEFAULT NULL,
  `end_user_id` int DEFAULT NULL,
  `admin_text` longtext,
  PRIMARY KEY (`id`),
  KEY `core_enduserautomess_auto_message_type_id_88dd825c_fk_core_auto` (`auto_message_type_id`),
  KEY `core_enduserautomessage_end_user_id_06739821_fk_core_enduser_id` (`end_user_id`),
  CONSTRAINT `core_enduserautomess_auto_message_type_id_88dd825c_fk_core_auto` FOREIGN KEY (`auto_message_type_id`) REFERENCES `core_automessagetype` (`id`),
  CONSTRAINT `core_enduserautomessage_end_user_id_06739821_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserautomessage`
--

LOCK TABLES `core_enduserautomessage` WRITE;
/*!40000 ALTER TABLE `core_enduserautomessage` DISABLE KEYS */;
INSERT INTO `core_enduserautomessage` VALUES (3,'1992-05-31 15:00:00.000000','2018-06-16 12:41:45.308442','2018-08-08 06:21:02.328125',0,1,5,'hoge'),(4,'2018-06-22 02:41:00.000000','2018-06-16 12:42:01.327612','2018-08-08 06:21:02.332793',0,2,5,'hoge'),(5,'2018-05-23 03:42:00.000000','2018-06-16 12:42:14.326407','2018-08-08 06:21:02.335961',0,3,5,'hoge'),(6,NULL,'2018-07-02 08:11:09.334334','2018-07-02 08:11:09.334374',0,1,7,NULL),(7,NULL,'2018-07-02 08:11:09.348626','2018-07-02 08:11:09.348681',0,2,7,NULL),(8,NULL,'2018-07-02 08:11:09.350048','2018-07-02 08:11:09.350086',0,3,7,NULL),(9,'2018-07-30 01:41:00.000000','2018-07-30 01:41:47.906077','2018-08-03 05:20:01.917010',0,1,8,NULL),(10,NULL,'2018-07-30 01:41:47.907638','2018-07-30 01:41:47.907673',0,2,8,NULL),(11,NULL,'2018-07-30 01:41:47.908618','2018-07-30 01:41:47.908648',0,3,8,NULL);
/*!40000 ALTER TABLE `core_enduserautomessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_endusercontactchat`
--

DROP TABLE IF EXISTS `core_endusercontactchat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_endusercontactchat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_endusercontactchat_end_user_id_fe9b7864_fk_core_enduser_id` (`end_user_id`),
  CONSTRAINT `core_endusercontactchat_end_user_id_fe9b7864_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_endusercontactchat`
--

LOCK TABLES `core_endusercontactchat` WRITE;
/*!40000 ALTER TABLE `core_endusercontactchat` DISABLE KEYS */;
INSERT INTO `core_endusercontactchat` VALUES (1,'GAocG-7Hk3eLB7LrAAAA','2018-11-05 05:59:10.787135','2018-11-05 05:59:10.787211',0,9),(2,'U-939tk87nJLW5H3AAAB','2018-11-05 05:59:48.455716','2018-11-05 05:59:48.455747',0,10),(3,'Ai8-5ykOR27bBNRLAAAE','2018-11-05 06:01:27.806055','2018-11-05 06:01:27.806154',0,11),(4,'9KEm3JhaWaKWyWyKAAAG','2018-11-05 06:03:03.736986','2018-11-05 06:03:03.737160',0,12),(5,'-XU8bd3yt_N-1_hiAAAI','2018-11-05 06:10:15.573598','2018-11-05 06:10:15.573895',0,13),(6,'BEFrM4RJ1-BKUeh8AAAJ','2018-11-05 06:10:19.059890','2018-11-05 06:10:19.060191',0,14),(7,'xI9UzcczQI6wRQLIAAAK','2018-11-05 06:10:22.464552','2018-11-05 06:10:22.464803',0,15),(8,'VwqOcxPa3EgwD5jqAAAL','2018-11-05 06:10:25.804375','2018-11-05 06:10:25.804685',0,16),(9,'BBV0SlWbqA5eiob-AAAM','2018-11-05 06:10:28.803768','2018-11-05 06:10:28.804079',0,17),(10,'jFBROXzoI9zrsxVwAAAN','2018-11-05 06:10:32.211053','2018-11-05 06:10:32.211696',0,18),(11,'xGkUpFYTlThizetZAAAO','2018-11-05 06:10:35.304952','2018-11-05 06:10:35.305249',0,19),(12,'T9RXNsbWHahIgsTxAAAP','2018-11-05 06:10:38.825451','2018-11-05 06:10:38.825749',0,20),(13,'bp_Y2AWxdqz2Iwr1AAAQ','2018-11-05 06:10:42.507451','2018-11-05 06:10:42.507750',0,21),(14,'LZ2Dx4cT374ZpIvBAAAR','2018-11-05 06:10:45.684469','2018-11-05 06:10:45.684723',0,22),(15,'C84a_towKMrcxDciAAAS','2018-11-05 06:10:55.541754','2018-11-05 06:10:55.542061',0,23),(16,'lBRHCo4yjJW9tnvOAAAT','2018-11-05 06:11:01.585491','2018-11-05 06:11:01.585748',0,24),(17,'Ls2YEPcqSG_3yAd3AAAU','2018-11-05 06:11:04.598692','2018-11-05 06:11:04.599097',0,25),(18,'tPDa4-TsowdZ87xVAAAV','2018-11-05 06:11:07.943683','2018-11-05 06:11:07.944087',0,26),(19,'nHDPJ2IBO92br2SVAAAW','2018-11-05 06:11:11.769945','2018-11-05 06:11:11.770294',0,27),(20,'wt8n3aU0OuASiDBTAAAX','2018-11-05 06:11:15.626328','2018-11-05 06:11:15.626586',0,28),(21,'lLFLwQWPPcbVKf5OAAAY','2018-11-05 06:11:19.309406','2018-11-05 06:11:19.309675',0,29),(22,'lZbrizOQN6iy5QiZAAAZ','2018-11-05 06:11:22.610439','2018-11-05 06:11:22.610789',0,30),(23,'z6XxpMUZMXdFCKFoAAAa','2018-11-05 06:11:31.160943','2018-11-05 06:11:31.161196',0,31),(24,'Q_uasvGh04sZKcjSAAAb','2018-11-05 06:11:34.035648','2018-11-05 06:11:34.036027',0,32),(25,'u-c2NTHnCeSlUuzTAAAc','2018-11-05 06:11:38.481489','2018-11-05 06:11:38.481885',0,33),(26,'DO6qz2j_HbhFjpPsAAAd','2018-11-05 06:11:43.249749','2018-11-05 06:11:43.250078',0,34),(27,'_ivHsyjYF2zC42u4AAAe','2018-11-05 06:11:48.639553','2018-11-05 06:11:48.639811',0,35),(28,'dScLPdCfCNd2chiSAAAf','2018-11-05 06:11:54.305483','2018-11-05 06:11:54.305763',0,36),(29,'CXk2QQ_kVpaD_bCpAAAg','2018-11-05 06:11:57.917059','2018-11-05 06:11:57.917323',0,37),(30,'F984tTJwy7ItuucYAAAh','2018-11-05 06:12:01.106742','2018-11-05 06:12:01.107045',0,38),(31,'SO7_yEhqp737q-6kAAAi','2018-11-05 06:12:06.481880','2018-11-05 06:12:06.482178',0,39),(32,'8aw9fRkxGjf2QLiNAAAj','2018-11-05 06:12:09.797512','2018-11-05 06:12:09.797795',0,40),(33,'JXGnKzVyGM32tEv5AAAk','2018-11-05 06:12:12.790067','2018-11-05 06:12:12.790330',0,41),(34,'OasB9ofzUm2kUljrAAAl','2018-11-05 06:12:16.527403','2018-11-05 06:12:16.527699',0,42),(35,'QpNMjLAw2wGi6lbYAAAm','2018-11-05 06:12:19.850783','2018-11-05 06:12:19.851040',0,43),(36,'0aziUqGc2jPVJaQHAAAn','2018-11-05 06:12:23.460857','2018-11-05 06:12:23.461169',0,44),(37,'BbFeWekK07yUbMKrAAAo','2018-11-05 06:12:27.948875','2018-11-05 06:12:27.949157',0,45),(38,'MGCEXJBTA0VWRTepAAAp','2018-11-05 06:12:40.141271','2018-11-05 06:12:40.141588',0,46),(39,'udjIIxET0zUMDw0qAAAq','2018-11-05 06:12:43.726149','2018-11-05 06:12:43.726481',0,47),(40,'RfEX0DwLqwPFuV15AAAr','2018-11-05 06:12:47.415294','2018-11-05 06:12:47.415567',0,48),(41,'hCuTOpcYkTyIl3e7AAAs','2018-11-05 06:12:50.916470','2018-11-05 06:12:50.916737',0,49),(42,'Ne74kLgRSoIpk-d0AAAt','2018-11-05 06:12:54.271409','2018-11-05 06:12:54.271666',0,50),(43,'LcVGpCUO_KPlTNw3AAAu','2018-11-05 06:12:57.002575','2018-11-05 06:12:57.002842',0,51),(44,'ZOQIIJZkLKGm1uHiAAAv','2018-11-05 06:13:03.132737','2018-11-05 06:13:03.133023',0,52),(45,'upUfQG8A-V0COHhfAAAw','2018-11-05 06:13:06.720357','2018-11-05 06:13:06.720619',0,53),(46,'HYWsVMHeQAuo4bMwAAAx','2018-11-05 06:13:10.747658','2018-11-05 06:13:10.748010',0,54),(47,'3Y41OJ_rDMSXHAO1AAAy','2018-11-05 06:13:13.810348','2018-11-05 06:13:13.810971',0,55),(48,'vL9eb3vohGuQU_rvAAAz','2018-11-05 06:13:17.133291','2018-11-05 06:13:17.133549',0,56),(49,'XTwf0gJSZfxHaUjBAAA0','2018-11-05 06:13:21.521395','2018-11-05 06:13:21.521669',0,57),(50,'Iralj7-rji1xlj45AAA1','2018-11-05 06:13:27.699176','2018-11-05 06:13:27.699558',0,58),(51,'TlJ_EZm-te1g-dAGAAA2','2018-11-05 06:13:30.569501','2018-11-05 06:13:30.569759',0,59),(52,'mO4r4XO0tGogJhs0AAA3','2018-11-05 06:13:36.813916','2018-11-05 06:13:36.814162',0,60),(53,'9jFqsAlSeLbBrgPTAAA4','2018-11-05 06:13:40.168770','2018-11-05 06:13:40.169057',0,61),(54,'vc2zaFSU7ZMcaiVtAAA5','2018-11-05 06:13:43.513749','2018-11-05 06:13:43.514005',0,62),(55,'1Mj6-SOF7Zgu51NyAAA6','2018-11-05 06:13:46.926715','2018-11-05 06:13:46.926994',0,63),(56,'6Ve7X5NikNO5GOvnAAA7','2018-11-05 06:13:51.623183','2018-11-05 06:13:51.623550',0,64),(57,'4JJWgVE9I5aSzQdnAAA8','2018-11-05 06:14:04.794992','2018-11-05 06:14:04.795235',0,65),(58,'AV0EVeX0PoyOdwGdAAA9','2018-11-05 06:14:13.905125','2018-11-05 06:14:13.905410',0,66),(59,'JgNAMbQRYo8jzNmrAAA-','2018-11-05 06:14:16.788438','2018-11-05 06:14:16.788748',0,67),(60,'-WJcX1Ez5K6sx8UWAAA_','2018-11-05 06:14:21.724843','2018-11-05 06:14:21.725080',0,68),(61,'IUL2MYG-ef-NXFk6AABA','2018-11-05 06:14:25.484071','2018-11-05 06:14:25.484350',0,69),(62,'qJs46uz_2RXbq5VeAABB','2018-11-05 06:14:29.211461','2018-11-05 06:14:29.211718',0,70),(63,'6cI2oih56lTFXhE5AABC','2018-11-05 06:14:39.859929','2018-11-05 06:14:39.860244',0,71),(64,'bvZhM9ZM_KgW2gh3AABD','2018-11-05 06:14:45.060987','2018-11-05 06:14:45.061231',0,72),(65,'vUzGHQIW2wZLwvIIAABE','2018-11-05 06:14:48.691559','2018-11-05 06:14:48.691863',0,73),(66,'fMEf8OMFtp49-N-xAABF','2018-11-05 06:15:00.439188','2018-11-05 06:15:00.439469',0,74),(67,'OuFHK1vG-qt1xzywAABG','2018-11-05 06:15:03.251269','2018-11-05 06:15:03.251550',0,75),(68,'J7XHy2uLnLXFkMEOAABH','2018-11-05 06:15:11.104215','2018-11-05 06:15:11.104462',0,76),(69,'oqFczpOVvunJChTTAABI','2018-11-05 06:15:14.483711','2018-11-05 06:15:14.484020',0,77),(70,'iwGrLJ-OHZnZzAdAAABJ','2018-11-05 06:15:20.775447','2018-11-05 06:15:20.775708',0,78),(71,'AcZhh0K_DiFLTcqcAABK','2018-11-05 06:15:25.135674','2018-11-05 06:15:25.135933',0,79),(72,'_CHI9Ur-o-hvmo8bAABL','2018-11-05 06:15:28.685161','2018-11-05 06:15:28.685418',0,80),(73,'iBVmWRZe9rUAM3H_AABM','2018-11-05 06:15:32.116996','2018-11-05 06:15:32.117294',0,81),(74,'GEgyYSVqyteRX1lxAABN','2018-11-05 06:15:35.538803','2018-11-05 06:15:35.539170',0,82),(75,'HCjb1o7L2ynxbr-7AABO','2018-11-05 06:15:39.391852','2018-11-05 06:15:39.392147',0,83),(76,'yxaQzkQC5hwgH6qbAABP','2018-11-05 06:15:42.926226','2018-11-05 06:15:42.926550',0,84),(77,'Ufh6xcvK0w5wLMuhAABQ','2018-11-05 06:15:46.377705','2018-11-05 06:15:46.378075',0,85),(78,'qr8Oge-j7-vDA9ZcAABR','2018-11-05 06:15:55.790266','2018-11-05 06:15:55.790536',0,86),(79,'M4dcRyFj8BoY_sUpAABS','2018-11-05 06:15:59.083388','2018-11-05 06:15:59.083666',0,87),(80,'niySTFr5ia06dNKOAABT','2018-11-05 06:16:03.860496','2018-11-05 06:16:03.860787',0,88),(81,'Of85v9FkdWuppG8nAABU','2018-11-05 06:16:07.629158','2018-11-05 06:16:07.629407',0,89),(82,'f5v1AHcBvCCW78GXAABV','2018-11-05 06:16:12.997777','2018-11-05 06:16:12.998020',0,90),(83,'EvXAV6SzgBjybAFcAABW','2018-11-05 06:16:24.043495','2018-11-05 06:16:24.043721',0,91),(84,'D0CqLumpYoZkaWbRAABX','2018-11-05 06:16:32.395082','2018-11-05 06:16:32.395395',0,92),(85,'H-BI8MGi4Ez6XP2bAABY','2018-11-05 06:16:35.742568','2018-11-05 06:16:35.742871',0,93),(86,'yTmG-cbV3UW07__aAABZ','2018-11-05 06:16:40.965551','2018-11-05 06:16:40.965801',0,94),(87,'lAAEUj192_hjlgaZAABa','2018-11-05 06:16:46.838713','2018-11-05 06:16:46.839048',0,95),(88,'ZdkDTJhXCt-Ib7ChAABb','2018-11-05 06:16:50.398510','2018-11-05 06:16:50.398764',0,96),(89,'UKtJNl2ki-nsVo-HAABc','2018-11-05 06:16:57.386695','2018-11-05 06:16:57.386945',0,97),(90,'N4eyImZhWpOtEhC7AABd','2018-11-05 06:17:01.357534','2018-11-05 06:17:01.357757',0,98),(91,'TKaMKbv5YmAQjuziAABe','2018-11-05 06:17:04.341879','2018-11-05 06:17:04.342426',0,99),(92,'AzPsbjlV88ufBCNBAABf','2018-11-05 06:17:10.380613','2018-11-05 06:17:10.380919',0,100),(93,'vecXOr-Ek5TeQDHlAABg','2018-11-05 06:17:15.414116','2018-11-05 06:17:15.414361',0,101),(94,'LiJNbE5-qmu1Q_4YAABh','2018-11-05 06:17:19.161331','2018-11-05 06:17:19.161594',0,102),(95,'FDlYfyGDgjRgOjXdAABi','2018-11-05 06:17:21.981242','2018-11-05 06:17:21.981565',0,103),(96,'ZPQDvAsWPrP-PVYHAABj','2018-11-05 06:17:25.714282','2018-11-05 06:17:25.714720',0,104),(97,'ClsBUxFXpL0aEY_JAABk','2018-11-05 06:17:31.676272','2018-11-05 06:17:31.676505',0,105),(98,'pqKNU0dL5dyACbpcAABl','2018-11-05 06:17:35.579187','2018-11-05 06:17:35.579434',0,106),(99,'lD3BNXbpF5_dGRkJAABm','2018-11-05 06:17:39.367889','2018-11-05 06:17:39.368201',0,107),(100,'BjdAPjpZxAWIo0iAAABn','2018-11-05 06:17:42.791651','2018-11-05 06:17:42.791895',0,108),(101,'0d4VaDuubI_W0Z11AABo','2018-11-05 06:17:46.360424','2018-11-05 06:17:46.360728',0,109),(102,'XKhFriKkIdloXJXkAABp','2018-11-05 06:17:49.749689','2018-11-05 06:17:49.750024',0,110),(103,'fOMrqVfOQ83s2xtmAABq','2018-11-05 06:17:53.121946','2018-11-05 06:17:53.122313',0,111),(104,'i3foMhoxS8gYDcVtAABr','2018-11-05 06:17:56.888112','2018-11-05 06:17:56.888369',0,112),(105,'hcEPwu3BX9QGiinBAABs','2018-11-05 06:18:01.635088','2018-11-05 06:18:01.635458',0,113),(106,'DWUS2iLI02v--Kl7AABt','2018-11-05 06:18:05.413217','2018-11-05 06:18:05.413539',0,114),(107,'Tdmrg63-h7G8SxzQAABu','2018-11-05 06:18:11.666570','2018-11-05 06:18:11.666892',0,115),(108,'G0mafXqnqdNn7BpqAABv','2018-11-05 06:18:21.820251','2018-11-05 06:18:21.820570',0,116),(109,'89Vs4oy5X9YUxbbqAABw','2018-11-05 06:18:34.097727','2018-11-05 06:18:34.098006',0,117),(110,'U-T1329CHEKkxUp1AABx','2018-11-05 06:18:43.333536','2018-11-05 06:18:43.333892',0,118),(111,'vPx6pVVqaYgYSnbfAABy','2018-11-05 06:18:46.270571','2018-11-05 06:18:46.270878',0,119),(112,'EoQhEPgvRoUREcHdAABz','2018-11-05 06:18:49.340423','2018-11-05 06:18:49.340680',0,120),(113,'16RyZQCRv_zsEa5sAAB0','2018-11-05 06:18:52.868095','2018-11-05 06:18:52.868367',0,121),(114,'UR-JrKKGFvBDHPRbAAB1','2018-11-05 06:18:55.949704','2018-11-05 06:18:55.949960',0,122),(115,'yX8sw3CZ77arBgadAAB2','2018-11-05 06:18:59.985572','2018-11-05 06:18:59.985884',0,123),(116,'ZskL9cnLF-V7wMuTAAB3','2018-11-05 06:19:03.883961','2018-11-05 06:19:03.884212',0,124),(117,'H2L_7NRNzBCAnz0PAAB4','2018-11-05 06:19:14.752069','2018-11-05 06:19:14.752328',0,125),(118,'20PC3TwER42x-K0CAAB5','2018-11-05 06:19:19.840950','2018-11-05 06:19:19.841239',0,126),(119,'UZyc-bZoGf-tmA6-AAB6','2018-11-05 06:19:24.566111','2018-11-05 06:19:24.566424',0,127),(120,'Nj-smVED2O_EFyYZAAAA','2018-11-05 06:19:37.513164','2018-11-05 06:19:37.513482',0,128),(121,'z4jE3BOy412RaTLPAAAB','2018-11-05 06:22:08.227204','2018-11-05 06:22:08.227623',0,129),(122,'sT6yVBx0kgVGaXibAAAA','2019-03-07 05:15:30.666134','2019-03-07 05:15:30.666134',0,130);
/*!40000 ALTER TABLE `core_endusercontactchat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserfacebook`
--

DROP TABLE IF EXISTS `core_enduserfacebook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserfacebook` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sender_id` varchar(256) DEFAULT NULL,
  `last_name` varchar(64) DEFAULT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `locale` varchar(25) DEFAULT NULL,
  `profile_pic_url` varchar(2024) DEFAULT NULL,
  `timezone` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_enduserfacebook_end_user_id_a386c264_fk_core_enduser_id` (`end_user_id`),
  CONSTRAINT `core_enduserfacebook_end_user_id_a386c264_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserfacebook`
--

LOCK TABLES `core_enduserfacebook` WRITE;
/*!40000 ALTER TABLE `core_enduserfacebook` DISABLE KEYS */;
INSERT INTO `core_enduserfacebook` VALUES (4,'2201067469910921','Kawajiri','Jun','male','ja_JP','http://dl.profile.line-cdn.net/0m000c342772518ed81916c12a2208a8ec9b119aa83e23',9,'2018-06-05 04:16:30.786106','2018-06-08 09:02:07.128440',0,5),(5,'1707325986040863','Bruning','Martijn','male','en_US','https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=1707325986040863&width=1024&ext=1535777035&hash=AeTFygX7JeQQws3c',9,'2018-07-02 08:11:09.316652','2018-08-02 04:43:55.244731',0,7);
/*!40000 ALTER TABLE `core_enduserfacebook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserline`
--

DROP TABLE IF EXISTS `core_enduserline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserline` (
  `id` int NOT NULL AUTO_INCREMENT,
  `display_name` varchar(256) DEFAULT NULL,
  `user_id` varchar(64) DEFAULT NULL,
  `picture_url` varchar(2048) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_id` int DEFAULT NULL,
  `payload` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_enduserline_end_user_id_b53cea1a_fk_core_enduser_id` (`end_user_id`),
  CONSTRAINT `core_enduserline_end_user_id_b53cea1a_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserline`
--

LOCK TABLES `core_enduserline` WRITE;
/*!40000 ALTER TABLE `core_enduserline` DISABLE KEYS */;
INSERT INTO `core_enduserline` VALUES (1,'Martin','U7706e7572608377a906c13e1204f959f',NULL,'2018-07-30 01:41:47.903090','2018-09-03 07:50:31.340982',0,8,'6');
/*!40000 ALTER TABLE `core_enduserline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_endusersequencestate`
--

DROP TABLE IF EXISTS `core_endusersequencestate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_endusersequencestate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `step` int NOT NULL,
  `end_user_state_id` int DEFAULT NULL,
  `message_block_id` int DEFAULT NULL,
  `sequence_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_endusersequence_end_user_state_id_12b4723e_fk_core_endu` (`end_user_state_id`),
  KEY `core_endusersequence_message_block_id_51763794_fk_core_mess` (`message_block_id`),
  KEY `core_endusersequence_sequence_id_a71293fe_fk_core_mess` (`sequence_id`),
  KEY `core_endusersequencestate_user_id_099ff407_fk_core_enduser_id` (`user_id`),
  CONSTRAINT `core_endusersequence_end_user_state_id_12b4723e_fk_core_endu` FOREIGN KEY (`end_user_state_id`) REFERENCES `core_enduserstate` (`id`),
  CONSTRAINT `core_endusersequence_message_block_id_51763794_fk_core_mess` FOREIGN KEY (`message_block_id`) REFERENCES `core_messageblock` (`id`),
  CONSTRAINT `core_endusersequence_sequence_id_a71293fe_fk_core_mess` FOREIGN KEY (`sequence_id`) REFERENCES `core_messagesequence` (`id`),
  CONSTRAINT `core_endusersequencestate_user_id_099ff407_fk_core_enduser_id` FOREIGN KEY (`user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_endusersequencestate`
--

LOCK TABLES `core_endusersequencestate` WRITE;
/*!40000 ALTER TABLE `core_endusersequencestate` DISABLE KEYS */;
INSERT INTO `core_endusersequencestate` VALUES (1,3,NULL,6,1,7),(2,0,NULL,6,1,8),(3,1,NULL,1,1,9),(4,1,NULL,1,1,10),(5,1,NULL,1,1,11),(6,0,NULL,6,1,12),(7,1,NULL,1,1,13),(8,1,NULL,1,1,14),(9,1,NULL,1,1,15),(10,1,NULL,1,1,16),(11,1,NULL,1,1,17),(12,1,NULL,1,1,18),(13,1,NULL,1,1,19),(14,1,NULL,1,1,20),(15,1,NULL,1,1,21),(16,1,NULL,1,1,22),(17,1,NULL,1,1,23),(18,1,NULL,1,1,24),(19,1,NULL,1,1,25),(20,1,NULL,1,1,26),(21,1,NULL,1,1,27),(22,1,NULL,1,1,28),(23,1,NULL,1,1,29),(24,1,NULL,1,1,30),(25,1,NULL,1,1,31),(26,1,NULL,1,1,32),(27,1,NULL,1,1,33),(28,1,NULL,1,1,34),(29,1,NULL,1,1,35),(30,1,NULL,1,1,36),(31,1,NULL,1,1,37),(32,1,NULL,1,1,38),(33,1,NULL,1,1,39),(34,1,NULL,1,1,40),(35,1,NULL,1,1,41),(36,1,NULL,1,1,42),(37,1,NULL,1,1,43),(38,1,NULL,1,1,44),(39,1,NULL,1,1,45),(40,1,NULL,1,1,46),(41,1,NULL,1,1,47),(42,1,NULL,1,1,48),(43,1,NULL,1,1,49),(44,1,NULL,1,1,50),(45,1,NULL,1,1,51),(46,1,NULL,1,1,52),(47,1,NULL,1,1,53),(48,1,NULL,1,1,54),(49,1,NULL,1,1,55),(50,1,NULL,1,1,56),(51,1,NULL,1,1,57),(52,1,NULL,1,1,58),(53,1,NULL,1,1,59),(54,1,NULL,1,1,60),(55,1,NULL,1,1,61),(56,1,NULL,1,1,62),(57,1,NULL,1,1,63),(58,1,NULL,1,1,64),(59,1,NULL,1,1,65),(60,1,NULL,1,1,66),(61,1,NULL,1,1,67),(62,1,NULL,1,1,68),(63,1,NULL,1,1,69),(64,1,NULL,1,1,70),(65,1,NULL,1,1,71),(66,1,NULL,1,1,72),(67,1,NULL,1,1,73),(68,1,NULL,1,1,74),(69,1,NULL,1,1,75),(70,1,NULL,1,1,76),(71,1,NULL,1,1,77),(72,1,NULL,1,1,78),(73,1,NULL,1,1,79),(74,1,NULL,1,1,80),(75,1,NULL,1,1,81),(76,1,NULL,1,1,82),(77,1,NULL,1,1,83),(78,1,NULL,1,1,84),(79,1,NULL,1,1,85),(80,1,NULL,1,1,86),(81,1,NULL,1,1,87),(82,1,NULL,1,1,88),(83,1,NULL,1,1,89),(84,1,NULL,1,1,90),(85,1,NULL,1,1,91),(86,1,NULL,1,1,92),(87,1,NULL,1,1,93),(88,1,NULL,1,1,94),(89,1,NULL,1,1,95),(90,1,NULL,1,1,96),(91,1,NULL,1,1,97),(92,1,NULL,1,1,98),(93,1,NULL,1,1,99),(94,1,NULL,1,1,100),(95,1,NULL,1,1,101),(96,1,NULL,1,1,102),(97,1,NULL,1,1,103),(98,1,NULL,1,1,104),(99,1,NULL,1,1,105),(100,1,NULL,1,1,106),(101,1,NULL,1,1,107),(102,1,NULL,1,1,108),(103,1,NULL,1,1,109),(104,1,NULL,1,1,110),(105,1,NULL,1,1,111),(106,1,NULL,1,1,112),(107,1,NULL,1,1,113),(108,1,NULL,1,1,114),(109,1,NULL,1,1,115),(110,1,NULL,1,1,116),(111,1,NULL,1,1,117),(112,1,NULL,1,1,118),(113,1,NULL,1,1,119),(114,1,NULL,1,1,120),(115,1,NULL,1,1,121),(116,1,NULL,1,1,122),(117,1,NULL,1,1,123),(118,1,NULL,1,1,124),(119,1,NULL,1,1,125),(120,1,NULL,1,1,126),(121,1,NULL,1,1,127),(122,1,NULL,1,1,128),(123,4,NULL,1,1,129);
/*!40000 ALTER TABLE `core_endusersequencestate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserstate`
--

DROP TABLE IF EXISTS `core_enduserstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserstate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserstate`
--

LOCK TABLES `core_enduserstate` WRITE;
/*!40000 ALTER TABLE `core_enduserstate` DISABLE KEYS */;
INSERT INTO `core_enduserstate` VALUES (1,'INITIAL','2018-06-05 03:22:33.611279','2018-06-05 03:22:33.611357',0),(2,'TEST','2018-06-05 10:41:26.473287','2018-06-05 10:41:26.473542',0),(3,'WAIT_TEXT','2018-06-05 10:41:26.473287','2018-06-05 10:41:26.473542',0),(4,'INITIAL','2018-07-02 12:56:05.227471','2018-07-02 12:56:05.227538',0),(5,'INITIAL','2018-07-02 12:57:42.280629','2018-07-02 12:57:42.280688',0),(6,'INITIAL','2018-07-02 12:59:50.675441','2018-07-02 12:59:50.675519',0),(7,'WAIT_TEXT','2018-07-02 12:59:50.751248','2018-07-02 12:59:50.751298',0),(8,'INITIAL','2018-07-02 13:10:47.828061','2018-07-02 13:10:47.828106',0),(9,'WAIT_TEXT','2018-07-02 13:10:47.897203','2018-07-02 13:10:47.897249',0),(10,'INITIAL','2018-07-02 13:12:46.399170','2018-07-02 13:12:46.399211',0),(11,'WAIT_TEXT','2018-07-02 13:12:46.455882','2018-07-02 13:12:46.455918',0),(12,'INITIAL','2018-07-02 13:34:24.177133','2018-07-02 13:34:24.177172',0),(13,'WAIT_TEXT','2018-07-02 13:34:24.233597','2018-07-02 13:34:24.233624',0),(14,'WAIT_INPUT',NULL,NULL,0);
/*!40000 ALTER TABLE `core_enduserstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserstory`
--

DROP TABLE IF EXISTS `core_enduserstory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserstory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `messaging_api_param_json` longtext,
  `run_order_num` int DEFAULT NULL,
  `admin_text` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_state_id` int DEFAULT NULL,
  `messaging_api_type_id` int DEFAULT NULL,
  `next_end_user_state_id` int DEFAULT NULL,
  `payload_id` int DEFAULT NULL,
  `is_todo` tinyint(1) NOT NULL,
  `todo_title` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_enduserstory_end_user_state_id_c3f2eefa_fk_core_endu` (`end_user_state_id`),
  KEY `core_enduserstory_messaging_api_type_i_8703c6d7_fk_core_mess` (`messaging_api_type_id`),
  KEY `core_enduserstory_next_end_user_state__66d5c023_fk_core_endu` (`next_end_user_state_id`),
  KEY `core_enduserstory_payload_id_cc88f979_fk_core_payload_id` (`payload_id`),
  CONSTRAINT `core_enduserstory_end_user_state_id_c3f2eefa_fk_core_endu` FOREIGN KEY (`end_user_state_id`) REFERENCES `core_enduserstate` (`id`),
  CONSTRAINT `core_enduserstory_messaging_api_type_i_8703c6d7_fk_core_mess` FOREIGN KEY (`messaging_api_type_id`) REFERENCES `core_messagingapitype` (`id`),
  CONSTRAINT `core_enduserstory_next_end_user_state__66d5c023_fk_core_endu` FOREIGN KEY (`next_end_user_state_id`) REFERENCES `core_enduserstate` (`id`),
  CONSTRAINT `core_enduserstory_payload_id_cc88f979_fk_core_payload_id` FOREIGN KEY (`payload_id`) REFERENCES `core_payload` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserstory`
--

LOCK TABLES `core_enduserstory` WRITE;
/*!40000 ALTER TABLE `core_enduserstory` DISABLE KEYS */;
INSERT INTO `core_enduserstory` VALUES (1,'{\"text\": \"text\"}',1,'text','2018-06-05 10:03:25.076941','2018-06-06 05:40:27.397223',1,1,1,1,2,0,NULL),(2,'{\r\n\"type\": \"image\",\r\n\"url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\"\r\n}',2,'image','2018-06-05 10:03:25.076941','2018-06-06 05:36:00.755683',1,1,2,1,2,0,NULL),(3,'{\r\n    \"elements\": [\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    },\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            },\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            }\r\n        ]\r\n}',1,'carousel','2018-06-05 10:03:25.076941','2018-06-06 03:25:47.264928',1,1,3,1,1,0,NULL),(4,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',4,'file(PDF)','2018-06-05 10:03:25.076941','2018-06-06 03:49:22.508910',1,1,2,1,1,0,NULL),(5,'{\r\n    \"text\": \"Here is a quick reply!\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        }\r\n    ]\r\n  }',5,'button','2018-06-06 04:15:29.621893','2018-06-06 04:19:52.601148',1,1,4,1,1,0,NULL),(6,'{\"text\": \"登録頂きありがとうございます！\"}',1,'はじめまして','2018-06-05 10:03:25.076941','2018-06-06 06:37:43.978641',0,1,1,1,1,0,NULL),(7,'{\r\n    \"text\": \"どうします？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"資料請求\",\r\n            \"payload\":\"GET_DOC\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"イベント予約\",\r\n            \"payload\":\"__event_GET_STARTED\"\r\n        }\r\n    ]\r\n  }',2,'どうします？','2018-06-05 10:03:25.076941','2018-06-08 07:09:38.668686',0,1,4,1,1,0,'hoge'),(8,'{\r\n    \"text\": \"受け取り方法は？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"このチャットで\",\r\n            \"payload\":\"GET_PDF\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"郵送\",\r\n            \"payload\":\"ASK_ADRESS\"\r\n        }\r\n    ]\r\n  }',1,'受け取り方法は？','2018-06-05 10:03:25.076941','2018-06-06 06:42:54.771332',0,1,4,1,3,0,NULL),(9,'{\r\n    \"text\": \"住所を入力してください\"\r\n}',1,'住所を入力してください','2018-06-05 10:03:25.076941','2018-06-06 14:39:30.562380',0,1,1,3,6,1,'郵送'),(10,'{\r\n    \"text\": \"ありがとうございます！\"\r\n}',2,'ありがとうございます（PDF）','2018-06-05 10:03:25.076941','2018-06-06 06:46:47.351443',0,1,1,1,5,0,NULL),(11,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',1,'(PDF送信)','2018-06-05 10:03:25.076941','2018-06-06 06:46:41.457373',0,1,2,1,5,0,NULL),(12,'{\"text\": \"ありがとうございます！　郵送しますねー\"}',1,'（住所入力後の返信）','2018-06-05 10:03:25.076941','2018-06-06 06:52:27.744298',0,3,1,1,2,0,NULL),(13,'{\r\n    \"elements\": [\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    },\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            },\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            }\r\n        ]\r\n}',1,NULL,'2018-07-02 12:59:50.680751','2018-07-02 12:59:50.680787',0,6,3,6,10,0,NULL),(14,'{\"text\": \"登録頂きありがとうございます！\"}',1,NULL,'2018-07-02 12:59:50.698630','2018-07-02 12:59:50.698667',0,6,1,6,10,0,NULL),(15,'{\r\n    \"text\": \"どうします？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"資料請求\",\r\n            \"payload\":\"GET_DOC\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"イベント予約\",\r\n            \"payload\":\"__event_GET_STARTED\"\r\n        }\r\n    ]\r\n  }',2,NULL,'2018-07-02 12:59:50.709365','2018-07-02 12:59:50.709404',0,6,4,6,10,0,'hoge'),(16,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',4,NULL,'2018-07-02 12:59:50.718484','2018-07-02 12:59:50.718521',0,6,2,6,10,0,NULL),(17,'{\r\n    \"text\": \"Here is a quick reply!\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        }\r\n    ]\r\n  }',5,NULL,'2018-07-02 12:59:50.727685','2018-07-02 12:59:50.727725',0,6,4,6,10,0,NULL),(18,'{\"text\": \"text\"}',1,NULL,'2018-07-02 12:59:50.742954','2018-07-02 12:59:50.743002',0,6,1,6,11,0,NULL),(19,'{\"text\": \"ありがとうございます！　郵送しますねー\"}',1,NULL,'2018-07-02 12:59:50.756417','2018-07-02 12:59:50.756495',0,7,1,6,11,0,NULL),(20,'{\r\n\"type\": \"image\",\r\n\"url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\"\r\n}',2,NULL,'2018-07-02 12:59:50.765038','2018-07-02 12:59:50.765075',0,6,2,6,11,0,NULL),(21,'{\r\n    \"text\": \"受け取り方法は？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"このチャットで\",\r\n            \"payload\":\"GET_PDF\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"郵送\",\r\n            \"payload\":\"ASK_ADRESS\"\r\n        }\r\n    ]\r\n  }',1,NULL,'2018-07-02 12:59:50.777912','2018-07-02 12:59:50.777963',0,6,4,6,12,0,NULL),(22,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',1,NULL,'2018-07-02 12:59:50.792310','2018-07-02 12:59:50.792351',0,6,2,6,13,0,NULL),(23,'{\r\n    \"text\": \"ありがとうございます！\"\r\n}',2,NULL,'2018-07-02 12:59:50.799638','2018-07-02 12:59:50.799678',0,6,1,6,13,0,NULL),(24,'{\r\n    \"text\": \"住所を入力してください\"\r\n}',1,NULL,'2018-07-02 12:59:50.811801','2018-07-02 12:59:50.811837',0,6,1,7,14,1,'郵送'),(25,'{\r\n    \"elements\": [\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    },\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            },\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            }\r\n        ]\r\n}',1,NULL,'2018-07-02 13:10:47.836561','2018-07-02 13:10:47.836614',0,8,3,8,15,0,NULL),(26,'{\"text\": \"登録頂きありがとうございます！\"}',1,NULL,'2018-07-02 13:10:47.846460','2018-07-02 13:10:47.846503',0,8,1,8,15,0,NULL),(27,'{\r\n    \"text\": \"どうします？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"資料請求\",\r\n            \"payload\":\"GET_DOC\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"イベント予約\",\r\n            \"payload\":\"__event_GET_STARTED\"\r\n        }\r\n    ]\r\n  }',2,NULL,'2018-07-02 13:10:47.854234','2018-07-02 13:10:47.854274',0,8,4,8,15,0,'hoge'),(28,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',4,NULL,'2018-07-02 13:10:47.870375','2018-07-02 13:10:47.870421',0,8,2,8,15,0,NULL),(29,'{\r\n    \"text\": \"Here is a quick reply!\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        }\r\n    ]\r\n  }',5,NULL,'2018-07-02 13:10:47.877949','2018-07-02 13:10:47.877988',0,8,4,8,15,0,NULL),(30,'{\"text\": \"text\"}',1,NULL,'2018-07-02 13:10:47.888869','2018-07-02 13:10:47.888915',0,8,1,8,16,0,NULL),(31,'{\"text\": \"ありがとうございます！　郵送しますねー\"}',1,NULL,'2018-07-02 13:10:47.903373','2018-07-02 13:10:47.903467',0,9,1,8,16,0,NULL),(32,'{\r\n\"type\": \"image\",\r\n\"url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\"\r\n}',2,NULL,'2018-07-02 13:10:47.910175','2018-07-02 13:10:47.910207',0,8,2,8,16,0,NULL),(33,'{\r\n    \"text\": \"受け取り方法は？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"このチャットで\",\r\n            \"payload\":\"GET_PDF\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"郵送\",\r\n            \"payload\":\"ASK_ADRESS\"\r\n        }\r\n    ]\r\n  }',1,NULL,'2018-07-02 13:10:47.922159','2018-07-02 13:10:47.922197',0,8,4,8,17,0,NULL),(34,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',1,NULL,'2018-07-02 13:10:47.932869','2018-07-02 13:10:47.932932',0,8,2,8,18,0,NULL),(35,'{\r\n    \"text\": \"ありがとうございます！\"\r\n}',2,NULL,'2018-07-02 13:10:47.940026','2018-07-02 13:10:47.940063',0,8,1,8,18,0,NULL),(36,'{\r\n    \"text\": \"住所を入力してください\"\r\n}',1,NULL,'2018-07-02 13:10:47.952286','2018-07-02 13:10:47.952329',0,8,1,9,19,1,'郵送'),(37,'{\r\n    \"elements\": [\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    },\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            },\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            }\r\n        ]\r\n}',1,NULL,'2018-07-02 13:12:46.404526','2018-07-02 13:12:46.404572',0,10,3,10,20,0,NULL),(38,'{\"text\": \"登録頂きありがとうございます！\"}',1,NULL,'2018-07-02 13:12:46.413431','2018-07-02 13:12:46.413491',0,10,1,10,20,0,NULL),(39,'{\r\n    \"text\": \"どうします？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"資料請求\",\r\n            \"payload\":\"GET_DOC\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"イベント予約\",\r\n            \"payload\":\"__event_GET_STARTED\"\r\n        }\r\n    ]\r\n  }',2,NULL,'2018-07-02 13:12:46.423072','2018-07-02 13:12:46.423114',0,10,4,10,20,0,'hoge'),(40,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',4,NULL,'2018-07-02 13:12:46.430240','2018-07-02 13:12:46.430273',0,10,2,10,20,0,NULL),(41,'{\r\n    \"text\": \"Here is a quick reply!\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        }\r\n    ]\r\n  }',5,NULL,'2018-07-02 13:12:46.439473','2018-07-02 13:12:46.439524',0,10,4,10,20,0,NULL),(42,'{\"text\": \"text\"}',1,NULL,'2018-07-02 13:12:46.451855','2018-07-02 13:12:46.451916',0,10,1,10,21,0,NULL),(43,'{\"text\": \"ありがとうございます！　郵送しますねー\"}',1,NULL,'2018-07-02 13:12:46.464573','2018-07-02 13:12:46.464614',0,11,1,10,21,0,NULL),(44,'{\r\n\"type\": \"image\",\r\n\"url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\"\r\n}',2,NULL,'2018-07-02 13:12:46.472886','2018-07-02 13:12:46.472921',0,10,2,10,21,0,NULL),(45,'{\r\n    \"text\": \"受け取り方法は？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"このチャットで\",\r\n            \"payload\":\"GET_PDF\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"郵送\",\r\n            \"payload\":\"ASK_ADRESS\"\r\n        }\r\n    ]\r\n  }',1,NULL,'2018-07-02 13:12:46.479576','2018-07-02 13:12:46.479606',0,10,4,10,22,0,NULL),(46,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',1,NULL,'2018-07-02 13:12:46.494199','2018-07-02 13:12:46.494259',0,10,2,10,23,0,NULL),(47,'{\r\n    \"text\": \"ありがとうございます！\"\r\n}',2,NULL,'2018-07-02 13:12:46.501244','2018-07-02 13:12:46.501292',0,10,1,10,23,0,NULL),(48,'{\r\n    \"text\": \"住所を入力してください\"\r\n}',1,NULL,'2018-07-02 13:12:46.507631','2018-07-02 13:12:46.507666',0,10,1,11,24,1,'郵送'),(49,'{\r\n    \"elements\": [\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    },\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            },\r\n            {\r\n                \"title\": \"titleMessage\",\r\n                \"url\":  \"https://sushitimes.co/\",\r\n                \"image_url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\",\r\n                \"subtitle\": \"some small message\",\r\n                \"buttons\": [\r\n                    {\r\n                        \"type\": \"url\",\r\n                        \"title\": \"button_title\",\r\n                        \"data\": \"https://sushitimes.co/\"\r\n                    }\r\n                ]\r\n            }\r\n        ]\r\n}',1,NULL,'2018-07-02 13:34:24.181289','2018-07-02 13:34:24.181328',0,12,3,12,25,0,NULL),(50,'{\"text\": \"登録頂きありがとうございます！\"}',1,NULL,'2018-07-02 13:34:24.203831','2018-07-02 13:34:24.203898',0,12,1,12,25,0,NULL),(51,'{\r\n    \"text\": \"どうします？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"資料請求\",\r\n            \"payload\":\"GET_DOC\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"イベント予約\",\r\n            \"payload\":\"__event_GET_STARTED\"\r\n        }\r\n    ]\r\n  }',2,NULL,'2018-07-02 13:34:24.211287','2018-07-02 13:34:24.211324',0,12,4,12,25,0,'hoge'),(52,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',4,NULL,'2018-07-02 13:34:24.216880','2018-07-02 13:34:24.216919',0,12,2,12,25,0,NULL),(53,'{\r\n    \"text\": \"Here is a quick reply!\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"Search\",\r\n            \"payload\":\"<POSTBACK_PAYLOAD>\"\r\n        }\r\n    ]\r\n  }',5,NULL,'2018-07-02 13:34:24.224671','2018-07-02 13:34:24.224705',0,12,4,12,25,0,NULL),(54,'{\"text\": \"text\"}',1,NULL,'2018-07-02 13:34:24.230202','2018-07-02 13:34:24.230243',0,12,1,12,26,0,NULL),(55,'{\"text\": \"ありがとうございます！　郵送しますねー\"}',1,NULL,'2018-07-02 13:34:24.237810','2018-07-02 13:34:24.237845',0,13,1,12,26,0,NULL),(56,'{\r\n\"type\": \"image\",\r\n\"url\": \"https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\"\r\n}',2,NULL,'2018-07-02 13:34:24.247311','2018-07-02 13:34:24.247365',0,12,2,12,26,0,NULL),(57,'{\r\n    \"text\": \"受け取り方法は？\",\r\n    \"quick_replies\":[\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"このチャットで\",\r\n            \"payload\":\"GET_PDF\"\r\n        },\r\n        {\r\n            \"content_type\":\"text\",\r\n            \"title\":\"郵送\",\r\n            \"payload\":\"ASK_ADRESS\"\r\n        }\r\n    ]\r\n  }',1,NULL,'2018-07-02 13:34:24.257077','2018-07-02 13:34:24.257111',0,12,4,12,27,0,NULL),(58,'{\r\n\"type\": \"file\",\r\n\"url\": \"https://s3-ap-northeast-1.amazonaws.com/gosa/data/CARRICULUM.pdf\"\r\n}',1,NULL,'2018-07-02 13:34:24.269847','2018-07-02 13:34:24.269882',0,12,2,12,28,0,NULL),(59,'{\r\n    \"text\": \"ありがとうございます！\"\r\n}',2,NULL,'2018-07-02 13:34:24.276632','2018-07-02 13:34:24.276670',0,12,1,12,28,0,NULL),(60,'{\r\n    \"text\": \"住所を入力してください\"\r\n}',1,NULL,'2018-07-02 13:34:24.284661','2018-07-02 13:34:24.284712',0,12,1,13,29,1,'郵送');
/*!40000 ALTER TABLE `core_enduserstory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserstoryhistory`
--

DROP TABLE IF EXISTS `core_enduserstoryhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserstoryhistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `is_todo` tinyint(1) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_id` int DEFAULT NULL,
  `end_user_story_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `end_user_reply` varchar(2048) DEFAULT NULL,
  `todo_action_status_id` int DEFAULT NULL,
  `memo` longtext,
  PRIMARY KEY (`id`),
  KEY `core_enduserstoryhistory_end_user_id_b246e557_fk_core_enduser_id` (`end_user_id`),
  KEY `core_enduserstoryhis_end_user_story_id_2e4a6163_fk_core_endu` (`end_user_story_id`),
  KEY `core_enduserstoryhis_vendor_branch_id_e4d0ea8d_fk_core_vend` (`vendor_branch_id`),
  KEY `core_enduserstoryhis_todo_action_status_i_eb5722ea_fk_core_todo` (`todo_action_status_id`),
  CONSTRAINT `core_enduserstoryhis_end_user_story_id_2e4a6163_fk_core_endu` FOREIGN KEY (`end_user_story_id`) REFERENCES `core_enduserstory` (`id`),
  CONSTRAINT `core_enduserstoryhis_todo_action_status_i_eb5722ea_fk_core_todo` FOREIGN KEY (`todo_action_status_id`) REFERENCES `core_todoactionstatus` (`id`),
  CONSTRAINT `core_enduserstoryhis_vendor_branch_id_e4d0ea8d_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`),
  CONSTRAINT `core_enduserstoryhistory_end_user_id_b246e557_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserstoryhistory`
--

LOCK TABLES `core_enduserstoryhistory` WRITE;
/*!40000 ALTER TABLE `core_enduserstoryhistory` DISABLE KEYS */;
INSERT INTO `core_enduserstoryhistory` VALUES (1,0,'2018-06-06 13:50:13.257281','2018-06-06 13:50:13.812615',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(2,0,'2018-06-06 13:50:13.816057','2018-06-06 13:50:28.625492',0,5,7,1,'GET_STARTED_PAYLOAD',1,NULL),(3,0,'2018-06-06 13:50:28.630869','2018-06-06 13:50:30.457879',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(4,0,'2018-06-06 13:50:30.462175','2018-06-06 13:51:17.498236',0,5,7,1,'GET_STARTED_PAYLOAD',1,NULL),(5,0,'2018-06-06 13:51:17.504004','2018-06-06 13:51:18.234313',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(6,0,'2018-06-06 13:51:18.242222','2018-06-06 13:53:21.461655',0,5,7,1,'GET_STARTED_PAYLOAD',1,NULL),(7,0,'2018-06-06 13:53:21.465626','2018-06-06 13:53:22.311049',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(8,0,'2018-06-06 13:53:22.315380','2018-06-06 13:54:35.703155',0,5,7,1,'GET_DOC',1,NULL),(9,0,'2018-06-06 13:54:35.708855','2018-06-06 13:56:23.170897',0,5,8,1,'GET_PDF',1,NULL),(10,0,'2018-06-06 13:56:23.181208','2018-06-06 13:56:23.737116',0,5,11,1,'GET_PDF',1,NULL),(11,0,'2018-06-06 13:56:23.742672','2018-06-06 14:27:03.424383',0,5,10,1,'GET_STARTED_PAYLOAD',1,NULL),(12,0,'2018-06-06 14:27:03.427957','2018-06-06 14:27:04.220014',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(13,0,'2018-06-06 14:27:04.226169','2018-06-06 14:27:35.912246',0,5,7,1,'GET_DOC',1,NULL),(14,0,'2018-06-06 14:27:35.922021','2018-06-06 14:28:57.274617',0,5,8,1,'ASK_ADRESS',1,NULL),(15,1,'2018-06-06 14:28:57.283916','2018-06-25 01:46:58.346115',0,5,9,1,'テストですー',5,''),(16,0,'2018-06-06 14:29:23.586311','2018-06-06 14:33:19.086574',0,5,12,1,'GET_STARTED_PAYLOAD',1,NULL),(17,0,'2018-06-06 14:33:19.092423','2018-06-06 14:33:19.517381',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(18,0,'2018-06-06 14:33:19.522864','2018-06-06 14:33:54.557052',0,5,7,1,'GET_DOC',1,NULL),(19,0,'2018-06-06 14:33:54.561957','2018-06-06 14:34:32.262378',0,5,8,1,'ASK_ADRESS',1,NULL),(20,1,'2018-06-06 14:34:32.265850','2018-06-16 14:55:06.245705',0,5,9,1,'なわなわなわ',4,'test'),(21,0,'2018-06-06 14:35:06.669312','2018-06-07 01:14:49.129427',0,5,12,1,'GET_STARTED_PAYLOAD',1,NULL),(22,0,'2018-06-07 01:14:49.146219','2018-06-07 01:14:49.548334',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(23,0,'2018-06-07 01:14:49.553336','2018-06-07 01:14:59.637072',0,5,7,1,'GET_DOC',1,NULL),(24,0,'2018-06-07 01:14:59.645991','2018-06-07 01:15:09.618994',0,5,8,1,'GET_PDF',1,NULL),(25,0,'2018-06-07 01:15:09.622323','2018-06-07 01:15:10.116864',0,5,11,1,'GET_PDF',1,NULL),(26,0,'2018-06-07 01:15:10.124126','2018-06-07 01:16:42.693897',0,5,10,1,'GET_STARTED_PAYLOAD',1,NULL),(27,0,'2018-06-07 01:16:42.699966','2018-06-07 01:16:43.112907',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(28,0,'2018-06-07 01:16:43.118841','2018-06-07 01:17:22.791502',0,5,7,1,'GET_DOC',1,NULL),(29,0,'2018-06-07 01:17:22.796515','2018-06-07 01:17:31.143001',0,5,8,1,'GET_PDF',1,NULL),(30,0,'2018-06-07 01:17:31.148137','2018-06-07 01:17:31.539514',0,5,11,1,'GET_PDF',1,NULL),(31,0,'2018-06-07 01:17:31.542910','2018-06-08 08:59:48.603013',0,5,10,1,'GET_STARTED_PAYLOAD',1,NULL),(32,0,'2018-06-08 08:59:48.606333','2018-06-08 08:59:48.952826',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(33,0,'2018-06-08 08:59:48.957542','2018-06-08 09:02:11.035531',0,5,7,1,'GET_STARTED_PAYLOAD',1,NULL),(34,0,'2018-06-08 09:02:11.041602','2018-06-08 09:02:15.480271',0,5,6,1,'GET_STARTED_PAYLOAD',1,NULL),(35,0,'2018-06-08 09:02:15.486037','2018-06-08 09:02:15.486106',0,5,7,1,NULL,1,NULL),(36,0,'2018-07-02 08:11:09.848128','2018-07-02 08:11:10.205650',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(37,0,'2018-07-02 08:11:10.210859','2018-07-02 08:11:34.728793',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(38,0,'2018-07-02 08:11:34.736052','2018-07-02 08:11:35.093844',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(39,0,'2018-07-02 08:11:35.098621','2018-07-02 08:12:06.024773',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(40,0,'2018-07-02 08:12:06.032789','2018-07-02 08:12:06.423331',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(41,0,'2018-07-02 08:12:06.431763','2018-07-04 01:47:57.853291',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(42,0,'2018-07-04 01:47:57.868652','2018-07-04 01:47:58.173125',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(43,0,'2018-07-04 01:47:58.181827','2018-07-04 02:36:43.240051',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(44,0,'2018-07-04 02:36:43.256409','2018-07-04 02:36:44.120289',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(45,0,'2018-07-04 02:36:44.127481','2018-07-04 02:38:00.776162',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(46,0,'2018-07-04 02:38:00.786707','2018-07-04 02:38:01.119184',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(47,0,'2018-07-04 02:38:01.125096','2018-07-04 02:45:38.501513',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(48,0,'2018-07-04 02:45:38.507250','2018-07-04 02:45:38.822333',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(49,0,'2018-07-04 02:45:38.829461','2018-07-04 02:53:50.038821',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(50,0,'2018-07-04 02:53:50.047008','2018-07-04 02:53:50.351307',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(51,0,'2018-07-04 02:53:50.357580','2018-07-04 02:53:54.636441',0,7,7,1,'GET_DOC',1,NULL),(52,0,'2018-07-04 02:53:54.644918','2018-07-04 02:54:03.561495',0,7,8,1,'GET_PDF',1,NULL),(53,0,'2018-07-04 02:54:03.566293','2018-07-04 02:54:03.907492',0,7,11,1,'GET_PDF',1,NULL),(54,0,'2018-07-04 02:54:03.912487','2018-07-18 02:37:40.906647',0,7,10,1,'GET_STARTED_PAYLOAD',1,NULL),(55,0,'2018-07-18 02:37:40.918007','2018-07-18 02:37:41.240475',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(56,0,'2018-07-18 02:37:41.246971','2018-07-18 02:38:05.624794',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(57,0,'2018-07-18 02:38:05.700845','2018-07-18 02:38:06.013846',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(58,0,'2018-07-18 02:38:06.019292','2018-07-19 04:44:23.507220',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(59,0,'2018-07-19 04:44:23.511850','2018-07-19 04:44:23.827867',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(60,0,'2018-07-19 04:44:23.834203','2018-07-19 04:44:57.981629',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(61,0,'2018-07-19 04:44:57.987451','2018-07-19 04:44:58.279644',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(62,0,'2018-07-19 04:44:58.285328','2018-07-19 04:45:34.494020',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(63,0,'2018-07-19 04:45:34.497029','2018-07-19 04:45:34.779322',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(64,0,'2018-07-19 04:45:34.787774','2018-07-19 04:46:30.708277',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(65,0,'2018-07-19 04:46:30.713065','2018-07-19 04:46:31.019865',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(66,0,'2018-07-19 04:46:31.025546','2018-07-19 04:46:55.207061',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(67,0,'2018-07-19 04:46:55.212026','2018-07-19 04:46:55.511477',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(68,0,'2018-07-19 04:46:55.517585','2018-07-19 04:47:49.371387',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(69,0,'2018-07-19 04:47:49.375181','2018-07-19 04:47:49.660278',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(70,0,'2018-07-19 04:47:49.668603','2018-07-19 04:54:45.685909',0,7,7,1,'GET_STARTED_PAYLOAD',1,NULL),(71,0,'2018-07-19 04:54:45.690870','2018-07-19 04:54:45.983751',0,7,6,1,'GET_STARTED_PAYLOAD',1,NULL),(72,0,'2018-07-19 04:54:45.988803','2018-07-19 04:54:45.988841',0,7,7,1,NULL,1,NULL),(73,1,'2018-07-25 04:15:21.255576','2018-07-25 04:15:21.255639',0,7,NULL,1,'TESTING 1234',5,'testing memo function 123'),(74,0,'2018-07-30 01:41:48.029780','2018-07-30 01:41:48.137404',0,8,6,1,'GET_STARTED_PAYLOAD',1,NULL),(75,0,'2018-07-30 01:41:48.142576','2018-07-30 02:56:09.087091',0,8,7,1,'GET_STARTED_PAYLOAD',1,NULL),(76,0,'2018-07-30 02:56:09.090966','2018-07-30 02:56:09.285284',0,8,6,1,'GET_STARTED_PAYLOAD',1,NULL),(77,0,'2018-07-30 02:56:09.290364','2018-07-30 02:56:48.138386',0,8,7,1,'GET_STARTED_PAYLOAD',1,NULL),(78,0,'2018-07-30 02:56:48.144943','2018-07-30 02:56:48.278659',0,8,6,1,'GET_STARTED_PAYLOAD',1,NULL),(79,0,'2018-07-30 02:56:48.284069','2018-07-30 02:58:01.833812',0,8,7,1,'GET_STARTED_PAYLOAD',1,NULL),(80,0,'2018-07-30 02:58:01.839220','2018-07-30 02:58:01.972225',0,8,6,1,'GET_STARTED_PAYLOAD',1,NULL),(81,0,'2018-07-30 02:58:01.977655','2018-07-30 02:58:01.977704',0,8,7,1,NULL,1,NULL);
/*!40000 ALTER TABLE `core_enduserstoryhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserstorytemplate`
--

DROP TABLE IF EXISTS `core_enduserstorytemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserstorytemplate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `payload` varchar(256) DEFAULT NULL,
  `next_end_user_state` varchar(256) DEFAULT NULL,
  `messaging_api_type` varchar(256) DEFAULT NULL,
  `messaging_api_param_json` longtext,
  `run_order_num` int DEFAULT NULL,
  `is_todo` tinyint(1) NOT NULL,
  `todo_title` varchar(128) DEFAULT NULL,
  `admin_text` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_story_template_category_id` int DEFAULT NULL,
  `end_user_state` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_enduserstorytem_end_user_story_templ_0fc5f0be_fk_core_endu` (`end_user_story_template_category_id`),
  CONSTRAINT `core_enduserstorytem_end_user_story_templ_0fc5f0be_fk_core_endu` FOREIGN KEY (`end_user_story_template_category_id`) REFERENCES `core_enduserstorytemplatecategory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserstorytemplate`
--

LOCK TABLES `core_enduserstorytemplate` WRITE;
/*!40000 ALTER TABLE `core_enduserstorytemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_enduserstorytemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_enduserstorytemplatecategory`
--

DROP TABLE IF EXISTS `core_enduserstorytemplatecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_enduserstorytemplatecategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `service_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_enduserstorytem_service_id_721dfd66_fk_core_serv` (`service_id`),
  CONSTRAINT `core_enduserstorytem_service_id_721dfd66_fk_core_serv` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_enduserstorytemplatecategory`
--

LOCK TABLES `core_enduserstorytemplatecategory` WRITE;
/*!40000 ALTER TABLE `core_enduserstorytemplatecategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_enduserstorytemplatecategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_event`
--

DROP TABLE IF EXISTS `core_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `description` longtext,
  `url` varchar(2048) DEFAULT NULL,
  `location` varchar(1024) DEFAULT NULL,
  `tel` varchar(64) DEFAULT NULL,
  `is_public` tinyint(1) NOT NULL,
  `capacity_num` int DEFAULT NULL,
  `is_gcal_set` tinyint(1) NOT NULL,
  `start_dt` datetime(6) DEFAULT NULL,
  `end_dt` datetime(6) DEFAULT NULL,
  `gcal_keyword` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `event_category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_event_event_category_id_dfa9e7e6_fk_core_eventcategory_id` (`event_category_id`),
  CONSTRAINT `core_event_event_category_id_dfa9e7e6_fk_core_eventcategory_id` FOREIGN KEY (`event_category_id`) REFERENCES `core_eventcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_event`
--

LOCK TABLES `core_event` WRITE;
/*!40000 ALTER TABLE `core_event` DISABLE KEYS */;
INSERT INTO `core_event` VALUES (1,'Event2','description2','web url2','location2','tel222',0,1,0,NULL,NULL,'test keyword','2018-06-09 07:44:07.624179','2018-06-09 13:49:58.644950',0,4),(2,'super special','Some very long explanation can be found here describing the most amazing fictional event ever held in the history of Tokyo super special fictional convention center.','https://www.example2.com','Tokyo','(070)111122223333',0,NULL,1,NULL,NULL,'test2','2018-06-09 13:48:31.421070','2018-06-18 05:59:51.083137',0,4),(3,'testing event','Charity event hosted by the Lorem Ipsum foundation where various esteemed members will read several passages of the popular manuscript.','https://www.example.com','Shibuya','(070)111122223333',0,NULL,1,NULL,NULL,'testing event','2018-06-09 13:50:28.443552','2018-08-07 04:24:26.114256',0,4),(14,'test2','test2','test2','test2','test2',1,NULL,0,NULL,NULL,'test2','2018-07-30 09:05:36.533854','2018-08-01 03:55:21.246705',1,4),(17,NULL,NULL,NULL,NULL,NULL,0,NULL,1,NULL,NULL,NULL,'2018-08-01 03:57:11.282620','2018-08-01 03:57:11.282660',0,4),(18,'past event','test','https://www.example.com','test','test',1,NULL,1,'2018-08-21 06:52:00.000000','2018-08-21 06:52:00.000000',NULL,'2018-08-01 03:58:14.619412','2018-08-21 08:30:07.910915',0,11),(19,'test','test','https://www.example.com','test','test',1,NULL,0,NULL,NULL,'','2018-08-09 05:09:54.289978','2018-08-23 08:19:20.109604',1,12),(20,NULL,NULL,NULL,NULL,NULL,0,NULL,1,NULL,NULL,NULL,'2018-08-21 05:00:04.575907','2018-08-21 05:10:42.931047',1,15),(21,'test','test','https://www.example.com','test','test',1,NULL,0,NULL,NULL,'test','2018-08-21 05:11:01.150362','2018-08-21 07:42:31.362498',1,15),(22,NULL,NULL,NULL,NULL,NULL,0,NULL,1,NULL,NULL,NULL,'2018-08-21 05:12:36.693817','2018-08-23 08:19:22.097629',1,12),(23,'test','test','https://www.example.com','TEST','test',1,NULL,1,'2018-08-21 08:28:00.000000','2018-08-21 08:28:00.000000',NULL,'2018-08-21 08:27:53.310960','2018-08-21 08:28:18.973764',0,16),(24,NULL,NULL,NULL,NULL,NULL,0,NULL,1,NULL,NULL,NULL,'2018-11-29 02:40:35.883563','2018-11-29 02:40:35.883601',0,19);
/*!40000 ALTER TABLE `core_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_eventcategory`
--

DROP TABLE IF EXISTS `core_eventcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_eventcategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `description` longtext,
  `display_order_num` int DEFAULT NULL,
  `is_public` tinyint(1) NOT NULL,
  `is_gcal_use` tinyint(1) NOT NULL,
  `is_gcal_available_time` tinyint(1) NOT NULL,
  `is_user_select_event_minutes` tinyint(1) NOT NULL,
  `event_minutes_csv` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_eventcategory_vendor_branch_id_dfb7514f_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_eventcategory_vendor_branch_id_dfb7514f_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_eventcategory`
--

LOCK TABLES `core_eventcategory` WRITE;
/*!40000 ALTER TABLE `core_eventcategory` DISABLE KEYS */;
INSERT INTO `core_eventcategory` VALUES (1,'Category 1-1','Event Category 1-1',1,1,0,1,0,NULL,'2018-06-09 01:45:48.588869','2018-08-01 03:54:22.548190',1,1),(2,'Category 2','Event Category 2',2,1,1,1,1,'30','2018-06-09 01:46:23.633731','2018-07-30 07:42:33.210344',1,1),(3,'Event Category 3','Event Category 3',3,1,1,1,1,'120','2018-06-09 01:46:42.454672','2018-07-30 07:42:30.327052',1,1),(4,'Name Here','test',NULL,1,1,0,0,'30,90','2018-06-09 07:31:36.220034','2018-06-22 08:57:30.119233',0,1),(5,NULL,NULL,NULL,0,1,0,0,NULL,'2018-06-22 09:14:15.585528','2018-06-22 09:18:37.106441',1,1),(6,'test new one','some description',NULL,0,1,0,0,NULL,'2018-06-22 09:14:46.832252','2018-06-22 09:18:33.077857',1,1),(7,'test1','test1',NULL,0,1,0,0,NULL,'2018-06-29 07:10:59.147682','2018-06-29 07:11:12.273365',0,2),(8,'test','test',NULL,0,0,0,0,NULL,'2018-07-27 08:25:51.586372','2018-08-01 03:54:17.915373',1,1),(9,NULL,NULL,NULL,0,0,0,0,NULL,'2018-07-31 02:05:25.921826','2018-07-31 02:05:53.584767',1,1),(10,'test5','test5',NULL,1,0,0,0,NULL,'2018-07-31 02:05:55.061667','2018-08-01 03:54:20.341348',1,1),(11,'public','test',NULL,1,0,0,0,NULL,'2018-08-01 03:54:23.727676','2018-08-01 03:58:09.618218',0,1),(12,'test','test',NULL,0,1,1,1,'30,90','2018-08-06 08:21:31.928921','2018-08-23 08:19:31.914657',1,1),(13,'test','test',NULL,0,0,0,1,'30','2018-08-21 04:41:00.105614','2018-08-21 04:49:06.831367',1,1),(14,NULL,NULL,NULL,0,0,0,0,NULL,'2018-08-21 04:49:08.275757','2018-08-21 04:59:31.654912',1,1),(15,'test','test',NULL,1,1,0,0,'30','2018-08-21 04:59:44.886884','2018-08-21 07:42:41.163964',1,1),(16,'test','test',NULL,1,0,0,0,NULL,'2018-08-21 07:42:42.658513','2018-08-21 08:27:42.770103',0,1),(17,'test','test',NULL,1,0,0,0,NULL,'2018-08-23 08:19:32.884196','2018-08-23 08:43:22.878721',1,1),(18,'test','test',NULL,1,0,0,0,NULL,'2018-08-23 08:43:25.296457','2018-08-23 08:44:07.666088',1,1),(19,'test','test',NULL,1,0,0,0,NULL,'2018-08-23 08:44:08.599205','2018-08-23 08:44:13.768279',0,1);
/*!40000 ALTER TABLE `core_eventcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_eventreservation`
--

DROP TABLE IF EXISTS `core_eventreservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_eventreservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reservation_date` date DEFAULT NULL,
  `reservation_start_time` time(6) DEFAULT NULL,
  `reservation_end_time` time(6) DEFAULT NULL,
  `gcal_url` varchar(1024) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_id` int DEFAULT NULL,
  `event_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `event_reservation_status_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_eventreservation_end_user_id_6749ef90_fk_core_enduser_id` (`end_user_id`),
  KEY `core_eventreservation_event_id_fc6d7119_fk_core_event_id` (`event_id`),
  KEY `core_eventreservatio_vendor_branch_id_47c88bf0_fk_core_vend` (`vendor_branch_id`),
  KEY `core_eventreservatio_event_reservation_st_e9456c63_fk_core_even` (`event_reservation_status_id`),
  CONSTRAINT `core_eventreservatio_event_reservation_st_e9456c63_fk_core_even` FOREIGN KEY (`event_reservation_status_id`) REFERENCES `core_eventreservationstatus` (`id`),
  CONSTRAINT `core_eventreservatio_vendor_branch_id_47c88bf0_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`),
  CONSTRAINT `core_eventreservation_end_user_id_6749ef90_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`),
  CONSTRAINT `core_eventreservation_event_id_fc6d7119_fk_core_event_id` FOREIGN KEY (`event_id`) REFERENCES `core_event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_eventreservation`
--

LOCK TABLES `core_eventreservation` WRITE;
/*!40000 ALTER TABLE `core_eventreservation` DISABLE KEYS */;
INSERT INTO `core_eventreservation` VALUES (1,'2018-06-13','15:28:02.000000','15:28:04.000000','https://www.example.com','2018-06-13 06:28:44.713373','2018-06-13 06:28:44.713461',0,5,2,1,1);
/*!40000 ALTER TABLE `core_eventreservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_eventreservationstatus`
--

DROP TABLE IF EXISTS `core_eventreservationstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_eventreservationstatus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_eventreservationstatus`
--

LOCK TABLES `core_eventreservationstatus` WRITE;
/*!40000 ALTER TABLE `core_eventreservationstatus` DISABLE KEYS */;
INSERT INTO `core_eventreservationstatus` VALUES (1,'OK12345',1,'2018-06-13 06:28:24.593521','2018-06-13 06:28:24.593563',0);
/*!40000 ALTER TABLE `core_eventreservationstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_file`
--

DROP TABLE IF EXISTS `core_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_file` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uploaded_at` datetime(6) NOT NULL,
  `upload` varchar(100) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `size` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_document_vendor_branch_id_9407118c_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `core_file_vendor_branch_id_6d36c1b9_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_file`
--

LOCK TABLES `core_file` WRITE;
/*!40000 ALTER TABLE `core_file` DISABLE KEYS */;
INSERT INTO `core_file` VALUES (6,'2019-11-07 02:25:54.572713','vendor_branch_1/this_person_does_not_exist_2.jpeg',1,NULL),(8,'2021-06-15 05:49:31.822042','vendor_branch_1/14-funny-miniature-photos-running-race-tatsuya-tanaka.jpg',1,NULL),(10,'2021-06-15 05:56:08.057068','vendor_branch_1/13-funny-miniature-photography-coke-basketball-tatsuya-tanaka.jpg',1,NULL),(11,'2021-06-15 05:56:16.954293','vendor_branch_1/38665d2edaea07c6afeda547fa1b4c15.jpg',1,NULL),(12,'2021-06-15 05:56:32.396711','vendor_branch_1/89418039da858df6dce21c9666d80889.jpg',1,NULL),(13,'2021-06-15 05:56:34.100956','vendor_branch_1/89418039da858df6dce21c9666d80889_QbigTc3.jpg',1,NULL),(14,'2021-06-15 05:56:42.780972','vendor_branch_1/993994116b9954ce244ec3f4169328d5.jpg',1,NULL),(15,'2021-06-15 05:56:57.846344','vendor_branch_1/ant_man.jpg',1,NULL),(16,'2021-06-15 05:57:06.722525','vendor_branch_1/apples-funny-miniature-star-wallpaper-preview.jpg',1,NULL),(17,'2021-06-15 05:57:19.404976','vendor_branch_1/banana.jpg',1,NULL),(18,'2021-06-15 05:57:30.680957','vendor_branch_1/breakfast.jpg',1,NULL),(19,'2021-06-15 05:57:42.584848','vendor_branch_1/brocolli-forest.jpg',1,NULL),(20,'2021-06-15 05:57:55.235423','vendor_branch_1/click.jpg',1,NULL),(21,'2021-06-15 05:58:12.956210','vendor_branch_1/da9cdcc99eee80c791627e526fe68e61.jpg',1,NULL),(22,'2021-06-15 05:58:40.559877','vendor_branch_1/dessert.jpg',1,NULL),(23,'2021-06-15 05:58:43.087412','vendor_branch_1/dessert_1aj6lxy.jpg',1,NULL),(24,'2021-06-17 11:52:18.081252','vendor_branch_1/14-funny-miniature-photos-running-race-tatsuya-tanaka_99YIRj9.jpg',1,62262),(25,'2021-06-17 11:54:45.814709','vendor_branch_1/38665d2edaea07c6afeda547fa1b4c15_GNe2wSQ.jpg',1,52063),(26,'2021-06-17 11:57:25.605545','vendor_branch_1/38665d2edaea07c6afeda547fa1b4c15_djcgtkI.jpg',1,52063),(27,'2021-06-17 12:05:41.879100','vendor_branch_1/14-funny-miniature-photos-running-race-tatsuya-tanaka_EOnM6nb.jpg',1,62262),(28,'2021-06-17 12:05:51.518138','vendor_branch_1/38665d2edaea07c6afeda547fa1b4c15_Xz9TxEw.jpg',1,52063),(29,'2021-06-17 12:06:03.931726','vendor_branch_1/13-funny-miniature-photography-coke-basketball-tatsuya-tanaka_XNtDecH.jpg',1,79984),(30,'2021-06-17 12:07:13.649647','vendor_branch_1/38665d2edaea07c6afeda547fa1b4c15_ZQNmMKs.jpg',1,52063),(31,'2021-06-17 12:08:11.453236','vendor_branch_1/13-funny-miniature-photography-coke-basketball-tatsuya-tanaka_ngQ9ZLL.jpg',1,79984),(32,'2021-06-17 15:44:15.215630','vendor_branch_1/ant_man_HLSVlnV.jpg',1,5206),(33,'2021-06-17 15:48:23.042186','vendor_branch_1/banana_f6qVn1e.jpg',1,22194),(34,'2021-06-18 06:26:57.094804','vendor_branch_1/apples-funny-miniature-star-wallpaper-preview_AuQT4z7.jpg',1,38639),(35,'2021-06-18 06:27:06.972987','vendor_branch_1/super_heroes.jpg',1,56257),(36,'2021-06-18 06:27:31.191879','vendor_branch_1/brocolli-forest_F3ZYJCb.jpg',1,6812),(37,'2021-06-18 07:40:55.947857','vendor_branch_1/993994116b9954ce244ec3f4169328d5_xpIEwYP.jpg',1,53325),(38,'2021-06-18 08:02:05.085864','vendor_branch_1/13-funny-miniature-photography-coke-basketball-tatsuya-tanaka_pNMyKs7.jpg',1,79984),(39,'2021-06-18 09:26:15.574075','vendor_branch_1/apples-funny-miniature-star-wallpaper-preview_5mXLaYR.jpg',1,38639),(40,'2021-06-23 04:52:43.633709','vendor_branch_1/ant_man_X1ZOjMm.jpg',1,5206);
/*!40000 ALTER TABLE `core_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_logshistory`
--

DROP TABLE IF EXISTS `core_logshistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_logshistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_start_dt` datetime(6) DEFAULT NULL,
  `event_end_dt` datetime(6) DEFAULT NULL,
  `is_athena_query` tinyint(1) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_logshistory`
--

LOCK TABLES `core_logshistory` WRITE;
/*!40000 ALTER TABLE `core_logshistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_logshistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_manualmessagecontroller`
--

DROP TABLE IF EXISTS `core_manualmessagecontroller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_manualmessagecontroller` (
  `id` int NOT NULL AUTO_INCREMENT,
  `messaging_api_param_json` longtext,
  `run_order_num` int DEFAULT NULL,
  `admin_text` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `manual_message_overview_id` int DEFAULT NULL,
  `messaging_api_type_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_manualmessageco_manual_message_overv_a940a353_fk_core_manu` (`manual_message_overview_id`),
  KEY `core_manualmessageco_messaging_api_type_i_91e0558a_fk_core_mess` (`messaging_api_type_id`),
  CONSTRAINT `core_manualmessageco_manual_message_overv_a940a353_fk_core_manu` FOREIGN KEY (`manual_message_overview_id`) REFERENCES `core_manualmessageoverview` (`id`),
  CONSTRAINT `core_manualmessageco_messaging_api_type_i_91e0558a_fk_core_mess` FOREIGN KEY (`messaging_api_type_id`) REFERENCES `core_messagingapitype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_manualmessagecontroller`
--

LOCK TABLES `core_manualmessagecontroller` WRITE;
/*!40000 ALTER TABLE `core_manualmessagecontroller` DISABLE KEYS */;
INSERT INTO `core_manualmessagecontroller` VALUES (86,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test123\'}',1,NULL,'2018-06-22 08:38:53.955967','2018-06-22 08:38:53.956015',0,21,1),(107,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test123123\'}',1,NULL,'2018-06-29 07:18:58.259907','2018-06-29 07:18:58.259966',0,22,1),(129,'{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'asda\', \'image_url\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\', \'subtitle\': \'asdasdsa\', \'actions\': \'https://derp.com\'}, {\'title\': \'asdasdsadsadsadsadsadsadsadsadsadsadsadsadsadsadasdadasdasdasdasdasdasdasdsadasda\', \'image_url\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\', \'subtitle\': \'asdasdsadsadsadsadsadsadsadsadsadsadsadsadsadsadasdadasdasdasdasdasdasdasdsadasda\', \'actions\': \'https://derp.com\'}, {\'title\': \'sadsadsadsadsadasda\', \'image_url\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\', \'subtitle\': \'asdsadsadsadsadsadsadadasd\', \'actions\': \'https://derp.com\'}]}',1,NULL,'2018-07-05 06:01:21.884280','2018-07-05 06:01:21.884353',0,4,3),(130,'{\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\'}',2,NULL,'2018-07-05 06:01:21.894181','2018-07-05 06:01:21.894241',0,4,5),(131,'{\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://onaliternote.files.wordpress.com/2016/11/wp-1480230666843.jpg\'}',3,NULL,'2018-07-05 06:01:21.905095','2018-07-05 06:01:21.905153',0,4,5),(132,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'hello\'}',1,NULL,'2018-07-09 05:02:42.567957','2018-07-09 05:02:42.568261',0,30,1),(136,'{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test messsage\'}',1,NULL,'2018-08-17 06:32:11.484335','2018-08-17 06:32:11.484360',0,1,1),(137,'{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'sushitimes\', \'image_url\': \'https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\', \'subtitle\': \'subtitle\', \'actions\': \'https://sushitimes.co\'}, {\'title\': \'sushitimes2\', \'image_url\': \'https://sushitimes.co/wp-content/uploads/2017/09/sushilogo-1.png\', \'subtitle\': \'subtitle2\', \'actions\': \'https://sushitimes.co\'}]}',2,NULL,'2018-08-17 06:32:11.485663','2018-08-17 06:32:11.485685',0,1,3),(138,'{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'asda\', \'image_url\': \'https://www.example.com\', \'subtitle\': \'asdasdasdsad\', \'actions\': \'https://www.example.com\'}, {\'title\': \'asdasd\', \'image_url\': \'https://www.example.com\', \'subtitle\': \'asdsadsadsa\', \'actions\': \'https://www.example.com\'}, {\'title\': \'asdasdadadsad\', \'image_url\': \'https://www.example.com\', \'subtitle\': \'sadasdsad\', \'actions\': \'https://www.example.com\'}]}',3,NULL,'2018-08-17 06:32:11.486955','2018-08-17 06:32:11.486977',0,1,3);
/*!40000 ALTER TABLE `core_manualmessagecontroller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_manualmessagehistory`
--

DROP TABLE IF EXISTS `core_manualmessagehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_manualmessagehistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_text` varchar(64) DEFAULT NULL,
  `send_dt` datetime(6) DEFAULT NULL,
  `send_user_count` int DEFAULT NULL,
  `send_user_id_csv` varchar(64) DEFAULT NULL,
  `selected_tag_csv` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `manual_message_overview_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_manualmessagehi_manual_message_overv_60c249f2_fk_core_manu` (`manual_message_overview_id`),
  KEY `core_manualmessagehi_vendor_branch_id_7d451808_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_manualmessagehi_manual_message_overv_60c249f2_fk_core_manu` FOREIGN KEY (`manual_message_overview_id`) REFERENCES `core_manualmessageoverview` (`id`),
  CONSTRAINT `core_manualmessagehi_vendor_branch_id_7d451808_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_manualmessagehistory`
--

LOCK TABLES `core_manualmessagehistory` WRITE;
/*!40000 ALTER TABLE `core_manualmessagehistory` DISABLE KEYS */;
INSERT INTO `core_manualmessagehistory` VALUES (1,NULL,'2018-06-15 14:16:57.906917',1,'5','1','2018-06-15 14:16:57.932361','2018-06-15 14:16:57.932402',0,1,1),(2,NULL,'2018-06-25 09:16:44.053426',1,'5','1,2','2018-06-25 09:16:44.058008','2018-06-25 09:16:44.058057',0,1,1),(3,NULL,'2018-07-03 02:45:05.784308',1,'5','1,2','2018-07-03 02:45:05.788003','2018-07-03 02:45:05.788040',0,1,1);
/*!40000 ALTER TABLE `core_manualmessagehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_manualmessageoverview`
--

DROP TABLE IF EXISTS `core_manualmessageoverview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_manualmessageoverview` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `is_share` tinyint(1) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `message_status_id` int DEFAULT NULL,
  `tags` longtext,
  `push_dt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_manualmessageov_vendor_branch_id_ba3ce2e5_fk_core_vend` (`vendor_branch_id`),
  KEY `core_manualmessageov_message_status_id_fa557ab9_fk_core_mess` (`message_status_id`),
  CONSTRAINT `core_manualmessageov_message_status_id_fa557ab9_fk_core_mess` FOREIGN KEY (`message_status_id`) REFERENCES `core_messagestatus` (`id`),
  CONSTRAINT `core_manualmessageov_vendor_branch_id_ba3ce2e5_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_manualmessageoverview`
--

LOCK TABLES `core_manualmessageoverview` WRITE;
/*!40000 ALTER TABLE `core_manualmessageoverview` DISABLE KEYS */;
INSERT INTO `core_manualmessageoverview` VALUES (1,'test000001',0,'2018-06-14 09:09:47.971475','2018-08-17 06:32:11.480506',0,1,3,'4,6',NULL),(2,'a',0,'2018-06-14 09:26:59.951449','2018-08-17 06:36:18.305431',0,1,3,'2',NULL),(3,'manual message test 001',0,'2018-06-15 05:49:54.891596','2018-08-17 06:35:32.483699',0,1,3,'2',NULL),(4,'b',0,'2018-06-15 06:00:39.838634','2018-07-05 06:01:21.862204',0,1,1,'2,3',NULL),(5,'test',0,'2018-06-15 06:02:17.383692','2018-06-18 03:28:20.753712',1,1,1,'1,2',NULL),(6,NULL,0,'2018-06-18 02:49:20.355159','2018-06-18 02:51:45.810863',1,1,1,NULL,NULL),(7,NULL,0,'2018-06-18 02:52:33.668906','2018-06-18 02:52:51.167295',1,1,1,NULL,NULL),(8,'Noneasdsa',0,'2018-06-18 02:55:17.793504','2018-06-18 03:11:48.017448',1,1,1,'',NULL),(9,'teasdt3e',0,'2018-06-18 02:55:43.457567','2018-06-18 03:08:09.999119',1,1,1,'',NULL),(10,'sadadsfds',0,'2018-06-18 03:12:20.825657','2018-06-18 03:21:10.496040',1,1,1,'',NULL),(11,'asdsad',0,'2018-06-18 03:21:13.142214','2018-06-18 03:28:13.351532',1,1,1,'',NULL),(12,'test123',0,'2018-06-18 03:28:24.350480','2018-06-18 03:29:13.894942',1,1,1,'',NULL),(13,'asdasda',0,'2018-06-18 07:44:35.645196','2018-06-18 07:44:39.158985',1,1,1,'',NULL),(14,'asdsadsad',0,'2018-06-18 07:44:56.730063','2018-06-18 07:45:00.753954',1,1,1,'',NULL),(15,'asdadasda',0,'2018-06-18 07:45:05.123260','2018-06-18 07:45:08.657741',0,1,1,'',NULL),(16,'dasfadfsa',0,'2018-06-18 07:45:11.065231','2018-06-18 07:45:14.189733',0,1,1,'',NULL),(17,'asdffdsasdfa',0,'2018-06-18 07:45:16.905345','2018-06-18 07:45:21.585762',0,1,1,'',NULL),(18,'dsfaadsfasd',0,'2018-06-18 07:45:34.304540','2018-06-19 05:00:53.804140',1,1,1,'2',NULL),(19,'sfdsadfasdf',0,'2018-06-18 07:45:39.565566','2018-06-18 07:45:43.626785',0,1,1,'',NULL),(20,'adsfasdfsa',0,'2018-06-18 07:45:46.651368','2018-06-18 07:45:49.812716',0,1,1,'',NULL),(21,'test123456',0,'2018-06-22 08:38:34.232120','2018-06-22 08:38:53.949476',0,1,1,'',NULL),(22,'test123123',0,'2018-06-29 07:18:44.381091','2018-06-29 07:18:58.221528',0,2,1,'',NULL),(23,NULL,0,'2018-07-09 02:54:00.886228','2018-07-09 02:54:00.886305',1,1,1,NULL,NULL),(24,NULL,0,'2018-07-09 02:56:04.578296','2018-07-09 02:56:04.578346',1,1,1,NULL,NULL),(25,NULL,0,'2018-07-09 02:56:11.253343','2018-07-09 02:56:11.253483',1,1,1,NULL,NULL),(26,NULL,0,'2018-07-09 02:56:32.773952','2018-07-09 02:56:32.774028',1,1,1,NULL,NULL),(27,NULL,0,'2018-07-09 03:20:14.871199','2018-07-09 03:20:14.871307',1,1,1,NULL,NULL),(28,NULL,0,'2018-07-09 03:23:34.711286','2018-07-09 03:23:34.711340',1,1,1,NULL,NULL),(29,NULL,0,'2018-07-09 03:24:43.838510','2018-07-09 03:24:43.838591',1,1,1,NULL,NULL),(30,'test1234',0,'2018-07-09 05:02:01.783077','2018-07-09 05:03:04.234212',1,1,1,'2',NULL),(31,NULL,0,'2018-07-13 07:21:40.482996','2018-07-13 07:21:40.483049',1,1,1,NULL,NULL),(32,'asdsa',0,'2018-11-29 02:44:03.031432','2018-11-29 02:45:35.048234',0,1,3,'',NULL),(33,'title',0,'2018-11-29 02:44:36.069574','2018-11-29 02:45:27.827055',0,1,5,'','1111-11-11 01:52:00.000000');
/*!40000 ALTER TABLE `core_manualmessageoverview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_messageblock`
--

DROP TABLE IF EXISTS `core_messageblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_messageblock` (
  `id` int NOT NULL AUTO_INCREMENT,
  `messaging_api_param_json` longtext,
  `admin_text` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_messageblock_vendor_branch_id_5f80f63b_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_messageblock_vendor_branch_id_5f80f63b_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_messageblock`
--

LOCK TABLES `core_messageblock` WRITE;
/*!40000 ALTER TABLE `core_messageblock` DISABLE KEYS */;
INSERT INTO `core_messageblock` VALUES (1,'[{\'type\': \'filesendmessage\', \'version\': \'1.0\', \'payload\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/ant_man_X1ZOjMm.jpg\'}, {\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/this_person_does_not_exist_2.jpeg\'}, {\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'qqw\', \'image_url\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/this_person_does_not_exist_2.jpeg\', \'subtitle\': \'erqw\', \'actions\': \'http://pain.ita\'}]}]','start','2018-07-13 04:14:35.493747','2021-06-23 05:39:50.199500',0,1),(2,'[{\'type\': \'tagsendmessage\', \'version\': \'1.0\', \'payload\': {\'mode\': \'add\', \'tag\': \'sushi\'}}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'You have been signed up for sushi mailing!\', \'payload\': [{\'title\': \'Take me back!\', \'payload\': \'1\'}, {\'title\': \'What did you say?\', \'payload\': \'2\'}]}]','sushi confirmation','2018-07-13 06:04:01.294045','2021-06-11 16:06:08.204139',0,1),(6,'[{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'dsasf\', \'image_url\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/this_person_does_not_exist_2.jpeg\', \'subtitle\': \'fad\', \'actions\': \'http://action.com/\'}, {\'title\': \'title\', \'image_url\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/this_person_does_not_exist_2.jpeg\', \'subtitle\': \'text\', \'actions\': \'http://action.com/\'}]}, {\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/this_person_does_not_exist_2.jpeg\'}]','file block','2018-07-18 09:52:29.399481','2021-06-18 11:22:44.597898',0,1),(7,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'sadness\'}]','Carousel Test','2018-07-20 06:03:02.050053','2021-06-08 03:51:28.183179',0,1),(8,'[]','Empty','2018-07-23 06:28:51.130484','2018-11-15 09:03:51.758587',1,1),(9,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'【ユーザーネーム】さん、はじめまして！ 【会社orプロジェクト名】にご興味をお持ち頂き、誠にありがとうございます！\'}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'本日はどういったご用件でしょうか？\', \'payload\': [{\'title\': \'資料請求\', \'payload\': \'10\'}, {\'title\': \'お問い合わせ\', \'payload\': \'14\'}]}]','LP01','2018-07-24 08:26:12.758172','2018-11-15 09:03:51.759116',0,1),(10,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'ありがとうございます！\'}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'どのように資料をお送りしたほうがよろしいでしょうか？\', \'payload\': [{\'title\': \'このチャットで送付\', \'payload\': \'11\'}, {\'title\': \'メールで送付\', \'payload\': \'none\'}, {\'title\': \'郵送\', \'payload\': \'none\'}]}]','LP01a','2018-07-24 08:28:39.230402','2018-11-15 09:03:51.763308',0,1),(11,'[{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'ドローン資料\', \'image_url\': \'https://www.instagram.com/static/images/homepage/screenshot1-2x.jpg/9144d6673849.jpg\', \'subtitle\': \'ver.1.2 ダウンロードする\', \'actions\': \'https://www.apple.com/privacy/parentaldisclosureconsent.pdf\'}]}]','LP01aa','2018-07-24 08:32:11.029285','2021-06-07 10:40:26.241497',1,1),(12,'[{\'type\': \'inputsendmessage\', \'version\': \'1.0\', \'payload\': {\'question\': \'What email can we use to contact you?\', \'attribute\': \'email\'}}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'ありがとうございます！\'}]','LP01ab','2018-07-24 08:46:06.925700','2018-11-15 09:03:51.765061',0,1),(13,'[{\'type\': \'inputsendmessage\', \'version\': \'1.0\', \'payload\': {\'question\': \'かしこまりました。 送付先の郵便番号と住所をお伝えください。\', \'attribute\': \'address1\'}}]','LP01ac','2018-07-24 09:05:38.501775','2018-11-15 09:03:51.765891',0,1),(14,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'ありがとうございます！\'}, {\'type\': \'formsendmessage\', \'version\': \'2.0\', \'title\': \'Question\', \'memo\': \'LP test 01b\', \'todo\': True, \'payload\': [{\'question\': \'お問い合わせ内容を打ち込み、送信ください。\', \'attribute\': \'answer\'}]}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'お問い合わせを受付いたしました。\\r\\n内容を確認し、担当者より折り返しご連絡いたします。\'}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'本日はお問い合わせいただきありがとうございました。\'}]','LP01b','2018-07-24 09:07:27.065597','2018-11-16 10:36:56.686094',0,1),(15,'[]','Test delete','2018-07-27 07:19:31.472837','2018-11-15 09:03:51.767313',1,1),(16,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test123\'}, {\'type\': \'tagsendmessage\', \'version\': \'1.0\', \'payload\': {\'mode\': \'add\', \'tag\': \'asdsad\'}}, {\'type\': \'inputsendmessage\', \'version\': \'1.0\', \'payload\': {\'question\': \'dasdsa\', \'attribute\': \'email\'}}, {\'type\': \'formsendmessage\', \'version\': \'2.0\', \'title\': \'asdsad\', \'memo\': \'asdasd\', \'todo\': True, \'payload\': [{\'question\': \'asdsad\', \'attribute\': \'answer\'}]}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'test\', \'payload\': [{\'title\': \'test\', \'payload\': \'none\'}, {\'title\': \'test2\', \'payload\': \'none\'}]}]','new test','2018-08-02 04:20:55.860531','2021-06-07 10:41:44.156376',1,1),(21,'[{\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'What test do you want to run?\', \'payload\': [{\'title\': \'Show me carousels!\', \'payload\': \'7\'}, {\'title\': \'Show me all!\', \'payload\': \'none\'}, {\'title\': \'Show me a file!\', \'payload\': \'6\'}, {\'title\': \'Event reservation\', \'payload\': \'__event_GET_STARTED\'}, {\'title\': \'event reservation\', \'payload\': \'__event_GET_STARTED\'}]}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \"Hey I will make you an offer you can\'t refuse.\"}, {\'type\': \'imagesendmessage\', \'version\': \'1.0\', \'payload\': \'https://media.giphy.com/media/l3V0GEwekqtkf5mWk/giphy.gif\'}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'Subscribe to my sushi news and I will take you out for an expensive dinner.\', \'payload\': [{\'title\': \'Yes! Sign me up!\', \'payload\': \'2\'}, {\'title\': \"No I don\'t like fish\", \'payload\': \'none\'}]}, {\'type\': \'tagsendmessage\', \'version\': \'1.0\', \'payload\': {\'mode\': \'add\', \'tag\': \'sushi\'}}, {\'type\': \'waitsendmessage\', \'version\': \'1.0\', \'payload\': \'167\'}, {\'type\': \'formsendmessage\', \'version\': \'2.0\', \'title\': \'Question\', \'memo\': \'any response will do\', \'todo\': True, \'payload\': [{\'question\': \'Anything we can do for you?\', \'attribute\': \'answer\'}]}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'Well do you want to sign up for an event then?\', \'payload\': [{\'title\': \'Sure!\', \'payload\': \'__event_GET_STARTED\'}, {\'title\': \"I don\'t understand\", \'payload\': \'6\'}]}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test lala\'}]','start','2018-08-20 08:40:21.403825','2018-11-15 09:03:51.768992',0,7),(22,'[{\'type\': \'tagsendmessage\', \'version\': \'1.0\', \'payload\': {\'mode\': \'add\', \'tag\': \'sushi\'}}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'You have been signed up for sushi mailing!\', \'payload\': [{\'title\': \'Take me back!\', \'payload\': \'1\'}, {\'title\': \'What did you say?\', \'payload\': \'2\'}]}]','sushi confirmation','2018-08-20 08:40:21.404164','2018-11-15 09:03:51.769736',0,7),(23,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'This is a newly created block, pretty cool huh?\'}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'We need to be sure you understand some stuff so be sure to read this file\'}, {\'type\': \'filesendmessage\', \'version\': \'1.0\', \'payload\': \'https://www.apple.com/privacy/parentaldisclosureconsent.pdf\'}]','file block','2018-08-20 08:40:21.404529','2018-11-15 09:03:51.770359',0,7),(24,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'sad\'}, {\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'https://www.example.com\', \'image_url\': \'https://media.giphy.com/media/l3V0GEwekqtkf5mWk/giphy.gif\', \'subtitle\': \'https://www.example.com\', \'actions\': \'https://www.google.com\'}, {\'title\': \'test\', \'image_url\': \'https://media.giphy.com/media/l3V0GEwekqtkf5mWk/giphy.gif\', \'subtitle\': \'test\', \'actions\': \'https://www.google.com\'}, {\'title\': \'test2\', \'image_url\': \'https://media.giphy.com/media/l3V0GEwekqtkf5mWk/giphy.gif\', \'subtitle\': \'test2\', \'actions\': \'https://www.google.com\'}]}]','Carousel Test','2018-08-20 08:40:21.405196','2018-11-15 09:03:51.771018',0,7),(25,'[]','Empty','2018-08-20 08:40:21.405512','2018-11-15 09:03:51.771627',1,7),(26,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'【ユーザーネーム】さん、はじめまして！ 【会社orプロジェクト名】にご興味をお持ち頂き、誠にありがとうございます！\'}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'本日はどういったご用件でしょうか？\', \'payload\': [{\'title\': \'資料請求\', \'payload\': \'10\'}, {\'title\': \'お問い合わせ\', \'payload\': \'14\'}]}]','LP01','2018-08-20 08:40:21.405814','2018-11-15 09:03:51.772165',0,7),(27,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'ありがとうございます！\'}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'どのように資料をお送りしたほうがよろしいでしょうか？\', \'payload\': [{\'title\': \'このチャットで送付\', \'payload\': \'11\'}, {\'title\': \'メールで送付\', \'payload\': \'none\'}, {\'title\': \'郵送\', \'payload\': \'none\'}]}]','LP01a','2018-08-20 08:40:21.406106','2018-11-15 09:03:51.772759',0,7),(28,'[{\'type\': \'carouselsendmessage\', \'version\': \'1.0\', \'payload\': [{\'title\': \'ドローン資料\', \'image_url\': \'https://s3.amazonaws.com/botsociety.prod.us/ba1ad30500531b16bef2_downloadjpg.jpg\', \'subtitle\': \'ver.1.2 ダウンロードする\', \'actions\': \'https://www.apple.com/privacy/parentaldisclosureconsent.pdf\'}]}]','LP01aa','2018-08-20 08:40:21.406433','2018-11-15 09:03:51.773300',0,7),(29,'[{\'type\': \'inputsendmessage\', \'version\': \'1.0\', \'payload\': {\'question\': \'What email can we use to contact you?\', \'attribute\': \'email\'}}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'ありがとうございます！\'}]','LP01ab','2018-08-20 08:40:21.406839','2018-11-15 09:03:51.773837',0,7),(30,'[{\'type\': \'inputsendmessage\', \'version\': \'1.0\', \'payload\': {\'question\': \'かしこまりました。 送付先の郵便番号と住所をお伝えください。\', \'attribute\': \'address1\'}}]','LP01ac','2018-08-20 08:40:21.407166','2018-11-15 09:03:51.774357',0,7),(31,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'ありがとうございます！\'}, {\'type\': \'formsendmessage\', \'version\': \'2.0\', \'title\': \'Question\', \'memo\': \'LP test 01b\', \'todo\': True, \'payload\': [{\'question\': \'お問い合わせ内容を打ち込み、送信ください。\', \'attribute\': \'answer\'}]}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'お問い合わせを受付いたしました。\\r\\n内容を確認し、担当者より折り返しご連絡いたします。\'}, {\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'本日はお問い合わせいただきありがとうございました。\'}]','LP01b','2018-08-20 08:40:21.407493','2018-11-15 09:03:51.774932',0,7),(32,'[]','Test delete','2018-08-20 08:40:21.407870','2018-11-15 09:03:51.775513',1,7),(33,'[{\'type\': \'textsendmessage\', \'version\': \'1.0\', \'payload\': \'test123\'}, {\'type\': \'tagsendmessage\', \'version\': \'1.0\', \'payload\': {\'mode\': \'add\', \'tag\': \'asdsad\'}}, {\'type\': \'inputsendmessage\', \'version\': \'1.0\', \'payload\': {\'question\': \'dasdsa\', \'attribute\': \'email\'}}, {\'type\': \'formsendmessage\', \'version\': \'2.0\', \'title\': \'asdsad\', \'memo\': \'asdasd\', \'todo\': True, \'payload\': [{\'question\': \'asdsad\', \'attribute\': \'answer\'}]}, {\'type\': \'quickreplysendmessage\', \'version\': \'1.0\', \'question\': \'test\', \'payload\': [{\'title\': \'test\', \'payload\': \'none\'}, {\'title\': \'test2\', \'payload\': \'none\'}]}]','new test','2018-08-20 08:40:21.408146','2018-11-15 09:03:51.776131',0,7),(34,'[]','None','2021-06-07 16:35:39.415346','2021-06-07 16:35:47.855907',0,1);
/*!40000 ALTER TABLE `core_messageblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_messagesequence`
--

DROP TABLE IF EXISTS `core_messagesequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_messagesequence` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_text` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `start_block_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_messagesequence_start_block_id_c22a45fa_fk_core_mess` (`start_block_id`),
  KEY `core_messagesequence_vendor_branch_id_ab27cc31_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_messagesequence_start_block_id_c22a45fa_fk_core_mess` FOREIGN KEY (`start_block_id`) REFERENCES `core_messageblock` (`id`),
  CONSTRAINT `core_messagesequence_vendor_branch_id_ab27cc31_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_messagesequence`
--

LOCK TABLES `core_messagesequence` WRITE;
/*!40000 ALTER TABLE `core_messagesequence` DISABLE KEYS */;
INSERT INTO `core_messagesequence` VALUES (1,'Get Started',NULL,NULL,0,1,1),(6,'Get Started','2018-08-20 08:40:21.409769','2018-08-20 08:40:21.409791',0,1,7);
/*!40000 ALTER TABLE `core_messagesequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_messagestatus`
--

DROP TABLE IF EXISTS `core_messagestatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_messagestatus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_messagestatus`
--

LOCK TABLES `core_messagestatus` WRITE;
/*!40000 ALTER TABLE `core_messagestatus` DISABLE KEYS */;
INSERT INTO `core_messagestatus` VALUES (1,'draft',NULL,NULL,0),(2,'template',NULL,NULL,0),(3,'pending',NULL,NULL,0),(4,'sent',NULL,NULL,0),(5,'scheduled',NULL,NULL,0);
/*!40000 ALTER TABLE `core_messagestatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_messagingapitype`
--

DROP TABLE IF EXISTS `core_messagingapitype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_messagingapitype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(64) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_messagingapitype`
--

LOCK TABLES `core_messagingapitype` WRITE;
/*!40000 ALTER TABLE `core_messagingapitype` DISABLE KEYS */;
INSERT INTO `core_messagingapitype` VALUES (1,'text','textsendmessage',NULL,NULL,0),(2,'file','filesendmessage',NULL,'2018-06-06 03:47:35.322030',0),(3,'carousel','carouselsendmessage',NULL,NULL,0),(4,'button_select','button_select','2018-06-06 04:14:50.497163','2018-06-06 04:14:50.497230',0),(5,'image','imagesendmessage',NULL,NULL,0);
/*!40000 ALTER TABLE `core_messagingapitype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_payload`
--

DROP TABLE IF EXISTS `core_payload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_payload` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `tag_category_name` varchar(64) DEFAULT NULL,
  `tag_name` varchar(64) DEFAULT NULL,
  `value_alt` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_payload_vendor_branch_id_c76418b1_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `core_payload_vendor_branch_id_c76418b1_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_payload`
--

LOCK TABLES `core_payload` WRITE;
/*!40000 ALTER TABLE `core_payload` DISABLE KEYS */;
INSERT INTO `core_payload` VALUES (1,'GET_STARTED_PAYLOAD','2018-06-05 10:03:00.459667','2018-06-05 10:03:00.459816',0,1,NULL,'すたーと',NULL),(2,'__text_input','2018-06-06 04:46:43.441002','2018-06-06 04:46:43.441072',0,1,NULL,NULL,NULL),(3,'GET_DOC',NULL,NULL,0,1,NULL,'','資料請求'),(4,'HOW_TO_GET',NULL,NULL,0,1,NULL,NULL,''),(5,'GET_PDF',NULL,NULL,0,1,NULL,'PDF','このチャットで'),(6,'ASK_ADRESS',NULL,NULL,0,1,NULL,NULL,'郵送'),(7,'THANKU',NULL,NULL,0,1,NULL,'',NULL),(10,'GET_STARTED_PAYLOAD','2018-07-02 12:59:50.664721','2018-07-02 12:59:50.664773',0,10,NULL,NULL,NULL),(11,'__text_input','2018-07-02 12:59:50.732822','2018-07-02 12:59:50.732869',0,10,NULL,NULL,NULL),(12,'GET_DOC','2018-07-02 12:59:50.769634','2018-07-02 12:59:50.769690',0,10,NULL,NULL,NULL),(13,'GET_PDF','2018-07-02 12:59:50.782905','2018-07-02 12:59:50.782965',0,10,NULL,NULL,NULL),(14,'ASK_ADRESS','2018-07-02 12:59:50.804299','2018-07-02 12:59:50.804362',0,10,NULL,NULL,NULL),(15,'GET_STARTED_PAYLOAD','2018-07-02 13:10:47.822598','2018-07-02 13:10:47.822658',0,11,NULL,NULL,NULL),(16,'__text_input','2018-07-02 13:10:47.881801','2018-07-02 13:10:47.881893',0,11,NULL,NULL,NULL),(17,'GET_DOC','2018-07-02 13:10:47.915755','2018-07-02 13:10:47.915826',0,11,NULL,NULL,NULL),(18,'GET_PDF','2018-07-02 13:10:47.925823','2018-07-02 13:10:47.925870',0,11,NULL,NULL,NULL),(19,'ASK_ADRESS','2018-07-02 13:10:47.943758','2018-07-02 13:10:47.943791',0,11,NULL,NULL,NULL),(20,'GET_STARTED_PAYLOAD','2018-07-02 13:12:46.397093','2018-07-02 13:12:46.397127',0,13,NULL,NULL,NULL),(21,'__text_input','2018-07-02 13:12:46.443869','2018-07-02 13:12:46.443926',0,13,NULL,NULL,NULL),(22,'GET_DOC','2018-07-02 13:12:46.474903','2018-07-02 13:12:46.474945',0,13,NULL,NULL,NULL),(23,'GET_PDF','2018-07-02 13:12:46.484711','2018-07-02 13:12:46.484765',0,13,NULL,NULL,NULL),(24,'ASK_ADRESS','2018-07-02 13:12:46.503459','2018-07-02 13:12:46.503490',0,13,NULL,NULL,NULL),(25,'GET_STARTED_PAYLOAD','2018-07-02 13:34:24.174591','2018-07-02 13:34:24.174635',0,17,NULL,NULL,NULL),(26,'__text_input','2018-07-02 13:34:24.226486','2018-07-02 13:34:24.226518',0,17,NULL,NULL,NULL),(27,'GET_DOC','2018-07-02 13:34:24.249893','2018-07-02 13:34:24.249921',0,17,NULL,NULL,NULL),(28,'GET_PDF','2018-07-02 13:34:24.262602','2018-07-02 13:34:24.262657',0,17,NULL,NULL,NULL),(29,'ASK_ADRESS','2018-07-02 13:34:24.278678','2018-07-02 13:34:24.278707',0,17,NULL,NULL,NULL);
/*!40000 ALTER TABLE `core_payload` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_service`
--

DROP TABLE IF EXISTS `core_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_service` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(64) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `fbms_access_url_part` varchar(2048) DEFAULT NULL,
  `fbms_access_token` varchar(2048) DEFAULT NULL,
  `fbms_verify_token` varchar(256) DEFAULT NULL,
  `line_access_url_part` varchar(2048) DEFAULT NULL,
  `line_access_token` varchar(2048) DEFAULT NULL,
  `line_verify_token` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_service`
--

LOCK TABLES `core_service` WRITE;
/*!40000 ALTER TABLE `core_service` DISABLE KEYS */;
INSERT INTO `core_service` VALUES (1,'00004','smartsec','hoge','hoge','hoge','hoge','hoge','hoge','2018-06-04 08:33:47.306753','2018-06-04 08:33:47.306819',0),(2,'00006','qa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `core_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_summarylogendusers`
--

DROP TABLE IF EXISTS `core_summarylogendusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_summarylogendusers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `end_user_id` int DEFAULT NULL,
  `device_type` int DEFAULT NULL,
  `device_family` varchar(64) DEFAULT NULL,
  `os_family` varchar(64) DEFAULT NULL,
  `os_version` varchar(64) DEFAULT NULL,
  `browser_family` varchar(64) DEFAULT NULL,
  `browser_version` varchar(64) DEFAULT NULL,
  `ip_address` varchar(64) DEFAULT NULL,
  `server_host` varchar(64) DEFAULT NULL,
  `status_code` varchar(64) DEFAULT NULL,
  `content_type` varchar(64) DEFAULT NULL,
  `http_referer` varchar(1024) DEFAULT NULL,
  `action_type` varchar(64) DEFAULT NULL,
  `params` varchar(1024) DEFAULT NULL,
  `endpoint` varchar(1024) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `service_id` int DEFAULT NULL,
  `vendor_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `level` varchar(64) DEFAULT NULL,
  `log_dt` datetime(6) DEFAULT NULL,
  `message_block_id` int DEFAULT NULL,
  `message_progress` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_summarylogendusers_service_id_ab0efbac_fk_core_service_id` (`service_id`),
  KEY `core_summarylogendusers_vendor_id_cfc1a9bb_fk_core_vendor_id` (`vendor_id`),
  KEY `core_summarylogendus_vendor_branch_id_3adc737f_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_summarylogendus_vendor_branch_id_3adc737f_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`),
  CONSTRAINT `core_summarylogendusers_service_id_ab0efbac_fk_core_service_id` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`),
  CONSTRAINT `core_summarylogendusers_vendor_id_cfc1a9bb_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_summarylogendusers`
--

LOCK TABLES `core_summarylogendusers` WRITE;
/*!40000 ALTER TABLE `core_summarylogendusers` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_summarylogendusers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_summarylogvendorusers`
--

DROP TABLE IF EXISTS `core_summarylogvendorusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_summarylogvendorusers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `device_type` int DEFAULT NULL,
  `device_family` varchar(64) DEFAULT NULL,
  `os_family` varchar(64) DEFAULT NULL,
  `os_version` varchar(64) DEFAULT NULL,
  `browser_family` varchar(64) DEFAULT NULL,
  `browser_version` varchar(64) DEFAULT NULL,
  `ip_address` varchar(64) DEFAULT NULL,
  `server_host` varchar(64) DEFAULT NULL,
  `status_code` varchar(64) DEFAULT NULL,
  `content_type` varchar(64) DEFAULT NULL,
  `http_referer` varchar(1024) DEFAULT NULL,
  `action_type` varchar(64) DEFAULT NULL,
  `params` varchar(1024) DEFAULT NULL,
  `endpoint` varchar(1024) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_user_id` int DEFAULT NULL,
  `level` varchar(64) DEFAULT NULL,
  `log_dt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_summarylogvendo_vendor_user_id_b3cec614_fk_core_vend` (`vendor_user_id`),
  CONSTRAINT `core_summarylogvendo_vendor_user_id_b3cec614_fk_core_vend` FOREIGN KEY (`vendor_user_id`) REFERENCES `core_vendoruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_summarylogvendorusers`
--

LOCK TABLES `core_summarylogvendorusers` WRITE;
/*!40000 ALTER TABLE `core_summarylogvendorusers` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_summarylogvendorusers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_tag`
--

DROP TABLE IF EXISTS `core_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(256) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `tag_category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_tag_tag_category_id_1f74a3c4_fk_core_tagcategory_id` (`tag_category_id`),
  CONSTRAINT `core_tag_tag_category_id_1f74a3c4_fk_core_tagcategory_id` FOREIGN KEY (`tag_category_id`) REFERENCES `core_tagcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_tag`
--

LOCK TABLES `core_tag` WRITE;
/*!40000 ALTER TABLE `core_tag` DISABLE KEYS */;
INSERT INTO `core_tag` VALUES (1,'1-1','testTag2',1,NULL,'2018-06-19 03:31:35.092710',1,1),(2,'TAG0001','admin',2,NULL,'2018-06-14 06:07:15.997685',0,1),(3,'TAG0002','testing',3,NULL,'2018-07-26 03:54:06.270126',1,1),(4,'1-4','すたーと',NULL,'2018-07-04 02:53:50.370433','2018-07-04 02:53:50.373405',0,1),(5,'1-5','PDF',NULL,'2018-07-04 02:54:03.927535','2018-07-04 02:54:03.929451',0,1),(6,'1-6','no sushi',NULL,'2018-07-23 05:49:34.043862','2018-07-23 05:49:34.052885',0,1),(7,'1-7','test1234',NULL,'2018-07-25 09:23:08.442744','2018-08-01 09:54:34.040477',1,1),(8,'1-8','sushi',NULL,'2018-07-25 09:27:24.009335','2018-07-25 09:27:24.012637',0,1),(9,'1-None','test1234',NULL,'2018-08-02 06:45:42.236749','2018-08-02 06:45:42.236790',0,NULL),(10,NULL,NULL,NULL,'2018-08-17 03:05:41.436381','2018-08-17 03:07:35.205019',1,1),(11,NULL,NULL,NULL,'2018-08-17 03:07:37.907616','2018-08-17 03:09:01.900680',1,1),(12,'1-12','test',NULL,'2018-08-17 03:08:52.206398','2018-08-17 03:08:59.011250',1,1),(13,'1-13','test123',NULL,'2018-08-17 03:09:03.443255','2018-08-17 03:09:10.538182',1,1),(14,'1-14','test123',NULL,'2018-08-17 03:09:14.995554','2018-08-17 03:09:25.848653',1,1),(15,'1-15','sadsad',NULL,'2018-08-17 03:10:14.219411','2018-08-17 03:10:19.458704',1,1);
/*!40000 ALTER TABLE `core_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_tagcategory`
--

DROP TABLE IF EXISTS `core_tagcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_tagcategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_tagcategory_vendor_branch_id_0b46f474_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_tagcategory_vendor_branch_id_0b46f474_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_tagcategory`
--

LOCK TABLES `core_tagcategory` WRITE;
/*!40000 ALTER TABLE `core_tagcategory` DISABLE KEYS */;
INSERT INTO `core_tagcategory` VALUES (1,'main',1,NULL,NULL,0,1),(6,'dummy',NULL,'2018-08-20 08:40:21.309225','2018-08-20 08:40:21.309249',0,7);
/*!40000 ALTER TABLE `core_tagcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_tmpentry`
--

DROP TABLE IF EXISTS `core_tmpentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_tmpentry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_agent` varchar(256) DEFAULT NULL,
  `x_forwarded_for` varchar(256) DEFAULT NULL,
  `branch_code` varchar(256) DEFAULT NULL,
  `access_dt` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `tag_name` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_tmpentry`
--

LOCK TABLES `core_tmpentry` WRITE;
/*!40000 ALTER TABLE `core_tmpentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_tmpentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_tmpregistrationentry`
--

DROP TABLE IF EXISTS `core_tmpregistrationentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_tmpregistrationentry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_agent` varchar(256) DEFAULT NULL,
  `x_forwarded_for` varchar(256) DEFAULT NULL,
  `code` varchar(256) DEFAULT NULL,
  `access_dt` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `affiliate_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_tmpregistration_affiliate_id_efdd7eba_fk_core_affi` (`affiliate_id`),
  CONSTRAINT `core_tmpregistration_affiliate_id_efdd7eba_fk_core_affi` FOREIGN KEY (`affiliate_id`) REFERENCES `core_affiliate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_tmpregistrationentry`
--

LOCK TABLES `core_tmpregistrationentry` WRITE;
/*!40000 ALTER TABLE `core_tmpregistrationentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_tmpregistrationentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_todo`
--

DROP TABLE IF EXISTS `core_todo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_todo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `end_user_reply` varchar(2048) DEFAULT NULL,
  `title` longtext,
  `memo` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `end_user_id` int DEFAULT NULL,
  `todo_action_status_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_todo_end_user_id_d4cce780_fk_core_enduser_id` (`end_user_id`),
  KEY `core_todo_todo_action_status_i_e2917b5e_fk_core_todo` (`todo_action_status_id`),
  KEY `core_todo_vendor_branch_id_c3e20939_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `core_todo_end_user_id_d4cce780_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`),
  CONSTRAINT `core_todo_todo_action_status_i_e2917b5e_fk_core_todo` FOREIGN KEY (`todo_action_status_id`) REFERENCES `core_todoactionstatus` (`id`),
  CONSTRAINT `core_todo_vendor_branch_id_c3e20939_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_todo`
--

LOCK TABLES `core_todo` WRITE;
/*!40000 ALTER TABLE `core_todo` DISABLE KEYS */;
INSERT INTO `core_todo` VALUES (10,'[{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'}]','test3','test memo','2018-07-25 09:32:08.903949','2018-07-25 09:32:08.903991',0,7,5,1),(11,'[{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'}]','test3','test memo','2018-07-25 09:32:31.942378','2018-07-25 09:32:31.942437',0,7,5,1),(15,'[{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'}]','test3','test memo','2018-07-26 08:07:20.131949','2018-07-26 08:07:20.132026',0,7,5,1),(16,'[{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'},{\'attribute\':\'test1\', \'value\':\'test2\'}]','Question','any response will do','2018-08-02 04:44:27.438990','2018-11-30 07:28:02.535888',0,7,4,1),(17,'no','Question','any response will do','2018-11-05 06:05:05.171118','2018-11-05 06:05:05.171262',0,12,5,1);
/*!40000 ALTER TABLE `core_todo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_todoactionstatus`
--

DROP TABLE IF EXISTS `core_todoactionstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_todoactionstatus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_todoactionstatus`
--

LOCK TABLES `core_todoactionstatus` WRITE;
/*!40000 ALTER TABLE `core_todoactionstatus` DISABLE KEYS */;
INSERT INTO `core_todoactionstatus` VALUES (1,'None',0,'2018-06-06 13:05:32.969306','2018-06-06 13:05:32.969350',1),(2,'NEW',1,'2018-06-06 13:05:41.823811','2018-06-06 13:05:41.823853',0),(3,'In-Progress',2,'2018-06-06 13:05:49.927493','2018-06-06 13:05:49.927535',0),(4,'DONE',3,'2018-06-06 13:05:57.762141','2018-06-06 13:05:57.762179',0),(5,'Pending',4,'2018-06-06 13:06:07.127259','2018-06-06 13:06:07.127299',0),(6,'Hidden',5,NULL,NULL,0);
/*!40000 ALTER TABLE `core_todoactionstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vendor`
--

DROP TABLE IF EXISTS `core_vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_vendor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(64) DEFAULT NULL,
  `company_name` varchar(256) DEFAULT NULL,
  `company_name_kana` varchar(256) DEFAULT NULL,
  `company_url` varchar(2048) DEFAULT NULL,
  `fbms_access_url_part` varchar(2048) DEFAULT NULL,
  `fbms_access_token` varchar(2048) DEFAULT NULL,
  `fbms_verify_token` varchar(256) DEFAULT NULL,
  `line_access_url_part` varchar(2048) DEFAULT NULL,
  `line_access_token` varchar(2048) DEFAULT NULL,
  `line_verify_token` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `service_id` int DEFAULT NULL,
  `picture_url` varchar(2024) DEFAULT NULL,
  `oem_service_url` varchar(256) DEFAULT NULL,
  `oem_service_namespace` varchar(256) DEFAULT NULL,
  `fbms_public_url` varchar(1024) DEFAULT NULL,
  `line_public_url` varchar(1024) DEFAULT NULL,
  `contactchat_access_token` varchar(2048) DEFAULT NULL,
  `contactchat_access_url_part` varchar(2048) DEFAULT NULL,
  `contactchat_verify_token` varchar(256) NOT NULL,
  `contactchat_css` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_vendor_service_id_4909dabc_fk_core_service_id` (`service_id`),
  CONSTRAINT `core_vendor_service_id_4909dabc_fk_core_service_id` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vendor`
--

LOCK TABLES `core_vendor` WRITE;
/*!40000 ALTER TABLE `core_vendor` DISABLE KEYS */;
INSERT INTO `core_vendor` VALUES (1,'000001','テストカンパニー','テストカンパニー','https://test.com','af3e42e240f8d996f4a24861804230f7af44b1056bd780e77d','EAACweYQolMgBABJWEME2JbDNw5ivYZCjWmxlZCsCWdZB8uWTQZAh0HnntNiVg54KY1cKuvCYSnkDUrTxvyFG7xZATCStTTbZA6KIBHpi55MshNH7HjfmfgQLZBsxg0oZB426TroGX4bNJIy15YlLfFlPr5DRLjOcx5OcJO9qPXtXAQZDZD','12346940','123412312321312','9wbaoRas04oUu9pRv2TXipSlCsB+hLmRLgUWF4YqKekKbHyWRFHvjhMd0FRgNLyLZKiWOcZWREudGfkSSIv9MPj+DVXxIT6C5LtgEEZtPcCwpLd2OC8IvLuyBK749StOWlw8s2FX+XKSiz9dCugu7AdB04t89/1O/w1cDnyilFU=','2669c0cbeed818e6ecacf01d273a8909','2018-06-04 08:34:54.247606','2021-06-02 05:59:45.555775',0,1,'vendor_1/avatar/Screen_Shot_2019-04-18_at_5.29.51_PM.png',NULL,NULL,'','','token00001','url00001','secretkeytest','{\"robottextcolor\": \"B8FF4E\", \"robotbubblecolor\": \"FF0000\", \"usertextcolor\": \"9B18FF\", \"userbubblecolor\": \"FF0000\", \"--robottextcolor\": \"#B8FF4E\", \"--robotbubblecolor\": \"#4A13FF\", \"--usertextcolor\": \"#9B18FF\", \"--userbubblecolor\": \"#FF0000\", \"chatbackgroundcolor\": \"55823A\", \"submitbuttoncolor\": \"FFFFFF\", \"windowcolor\": \"wedkhfslkh5D7096\", \"infotextcolor\": \"62739C\", \"usericon\": \"https://upload.wikimedia.org/wikipedia/commons/2/27/Emojione_1F464.svg\", \"roboticon\": \"https://upload.wikimedia.org/wikipedia/commons/b/b6/Emojione_1F916.svg\", \"fontsize\": \"10\", \"fontfamily\": \"Arial\", \"fontstyle\": \"normal\"}'),(2,'2','2','2','2','2','2','2','2','2','2','2018-06-29 06:53:59.389537','2018-06-29 06:53:59.389580',0,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'qwerty',NULL),(7,'0820-1701','testing template copy',NULL,NULL,'fbzXWJHdoe9viXpnwoKzXbUQjCdnVaJsmbQvFjiSRbGVjUGjbt','','PpavzMyNKR','lnzXWJHdoe9viXpnwoKzXbUQjCdnVaJsmbQvFjiSRbGVjUGjbt','','','2018-08-20 08:40:21.305728','2018-08-20 08:40:21.305758',0,1,NULL,NULL,NULL,'https://smartby.ai/fbzXWJHdoe9viXpnwoKzXbUQjCdnVaJsmbQvFjiSRbGVjUGjbt','https://smartby.ai/lnzXWJHdoe9viXpnwoKzXbUQjCdnVaJsmbQvFjiSRbGVjUGjbt',NULL,NULL,'qwerty',NULL),(10,'0307-1616','QA_TEST_VENDOR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-03-07 07:16:09.073205','2019-03-07 07:16:09.074250',0,2,NULL,NULL,NULL,NULL,NULL,'iA6ZMdzxMatCTbHWmc7e','cchD9UOogZMtYuOEjGmGp6','qwerty',NULL),(12,'0307-1713','QA_TEST_2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-03-07 08:13:13.200387','2019-03-07 08:13:13.200420',0,2,NULL,NULL,NULL,NULL,NULL,'mdPOYqmdk3owTz60ubGF','cccXqebnUXWiDXtY7PbDWw','qwerty',NULL),(15,'0307-1718','QA_TEST3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-03-07 08:18:15.448502','2019-03-07 08:18:15.448538',0,2,NULL,NULL,NULL,NULL,NULL,'NqPwGnml73ed9b0JdShX','ccGkjT5WvOusJun5djGNEn','qwerty',NULL),(16,'0508-1503','donvermo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-05-08 06:03:40.198017','2019-05-08 06:03:40.198072',0,2,NULL,NULL,NULL,NULL,NULL,'gwKRXKnAW0gxgkVXHn7B','ccGtVEZQTtUKuPPDSJDPrb','qwerty',NULL),(18,'0509-1107','test vendor',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-05-09 02:07:36.604372','2019-05-09 02:07:36.604571',0,2,NULL,NULL,NULL,NULL,NULL,'gjuEc1xHOw06FfIF4aka','cc5YxH4LcirqTc9QjPJN9G','qwerty',NULL),(19,'0509-1153','test vendor22',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-05-09 02:53:30.025908','2019-05-09 02:53:30.026109',0,2,NULL,NULL,NULL,NULL,NULL,'vvMELY379B3m9ijuJsyR','ccsNw93DYzsYZRtVSlcQJ3','qwerty',NULL),(20,'0710-1451','asdsada',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-10 05:51:32.385033','2019-07-10 05:51:32.385061',0,2,'',NULL,NULL,NULL,NULL,'bUwujyxxXw2bPSgKhsm9','ccgxwDiKCNVDo8K8CwmPxO','qwerty',NULL),(21,'0711-1615','vendor name test',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-11 07:15:06.877182','2019-07-11 07:15:06.877211',0,2,'',NULL,NULL,NULL,NULL,'6O8LltBhYK7BA8Zw4kdM','ccI7lYA0nWF2t8z4XM7XqP','qwerty',NULL);
/*!40000 ALTER TABLE `core_vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vendorbranch`
--

DROP TABLE IF EXISTS `core_vendorbranch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_vendorbranch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(128) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `cd_path` varchar(2024) DEFAULT NULL,
  `join_cd` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_id` int DEFAULT NULL,
  `google_credentials` longtext,
  `google_credentials_initial_code` longtext,
  `google_credentials_refresh_token` longtext,
  `is_google_calendar_ready` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_vendorbranch_vendor_id_afced2a5_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `core_vendorbranch_vendor_id_afced2a5_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vendorbranch`
--

LOCK TABLES `core_vendorbranch` WRITE;
/*!40000 ALTER TABLE `core_vendorbranch` DISABLE KEYS */;
INSERT INTO `core_vendorbranch` VALUES (1,'00001-01','test-hq','hoge','hoge','2018-06-04 08:35:32.815726','2019-03-07 07:01:42.184993',0,1,NULL,NULL,NULL,1),(2,'2','BRANCH 2','VENDOR2','2','2018-06-29 06:54:18.465266','2018-06-29 06:54:18.465309',0,2,'2','2','2',0),(7,'00001','branch_00001',NULL,NULL,'2018-08-20 08:40:21.306463','2018-08-20 08:40:21.306486',0,7,NULL,NULL,NULL,0),(8,'00001','branch_00001',NULL,NULL,'2019-03-07 07:04:23.643126','2019-03-07 07:04:23.643147',0,7,NULL,NULL,NULL,1),(10,'00001','branch_00001',NULL,NULL,'2019-03-07 07:16:09.074809','2019-03-07 07:16:09.074832',0,10,NULL,NULL,NULL,1),(12,'00001','branch_00001',NULL,NULL,'2019-03-07 08:13:13.200934','2019-03-07 08:13:13.200956',0,12,NULL,NULL,NULL,1),(13,'00001','branch_00001',NULL,NULL,'2019-03-07 08:18:15.449960','2019-03-07 08:18:15.449981',0,15,NULL,NULL,NULL,1),(14,'00001','branch_00001',NULL,NULL,'2019-05-08 06:03:40.204785','2019-05-08 06:03:40.204840',0,16,NULL,NULL,NULL,1),(16,'00001','branch_00001',NULL,NULL,'2019-05-09 02:07:36.607976','2019-05-09 02:07:36.608091',0,18,NULL,NULL,NULL,1),(17,'00001','branch_00001',NULL,NULL,'2019-05-09 02:53:30.028869','2019-05-09 02:53:30.028984',0,19,NULL,NULL,NULL,1),(18,'00001','branch_00001',NULL,NULL,'2019-07-10 05:51:32.395445','2019-07-10 05:51:32.395475',0,20,NULL,NULL,NULL,1),(19,'00001','branch_00001',NULL,NULL,'2019-07-11 07:15:06.880965','2019-07-11 07:15:06.880989',0,21,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `core_vendorbranch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vendoreventsettings`
--

DROP TABLE IF EXISTS `core_vendoreventsettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_vendoreventsettings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `work_start_time` time(6) DEFAULT NULL,
  `work_end_time` time(6) DEFAULT NULL,
  `day_off_csv` varchar(32) DEFAULT NULL,
  `buffer_period` int DEFAULT NULL,
  `is_google_calender_oauth` tinyint(1) NOT NULL,
  `admin_text` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_vendoreventsett_vendor_branch_id_e8278987_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_vendoreventsett_vendor_branch_id_e8278987_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vendoreventsettings`
--

LOCK TABLES `core_vendoreventsettings` WRITE;
/*!40000 ALTER TABLE `core_vendoreventsettings` DISABLE KEYS */;
INSERT INTO `core_vendoreventsettings` VALUES (1,'10:00:00.000000','20:00:00.000000','3,4,5,6',60,0,'memo','2018-06-09 02:09:28.902238','2018-08-06 07:34:55.698837',0,1),(2,'16:07:00.000000','16:07:00.000000','1',1,1,'12','2018-06-29 07:07:17.598004','2018-06-29 07:10:54.265699',0,2),(7,NULL,NULL,NULL,NULL,0,NULL,'2018-08-20 08:40:21.309871','2018-08-20 08:40:21.309893',0,7);
/*!40000 ALTER TABLE `core_vendoreventsettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vendoruser`
--

DROP TABLE IF EXISTS `core_vendoruser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_vendoruser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(64) DEFAULT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `last_name_kana` varchar(64) DEFAULT NULL,
  `first_name_kana` varchar(64) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `facebook_sender_id` varchar(256) DEFAULT NULL,
  `line_user_id` varchar(64) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auth_user_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_vendoruser_email_82d01640_uniq` (`email`),
  KEY `core_vendoruser_auth_user_id_3d0a49b5_fk_auth_user_id` (`auth_user_id`),
  KEY `core_vendoruser_vendor_branch_id_3db0c958_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `core_vendoruser_auth_user_id_3d0a49b5_fk_auth_user_id` FOREIGN KEY (`auth_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `core_vendoruser_vendor_branch_id_3db0c958_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vendoruser`
--

LOCK TABLES `core_vendoruser` WRITE;
/*!40000 ALTER TABLE `core_vendoruser` DISABLE KEYS */;
INSERT INTO `core_vendoruser` VALUES (1,'b','a','','','{\'last_name\': \'b\', \'first_name\': \'a\', \'last_name_kana\': \'\', \'first_name_kana\': \'\', \'email\': {...}}','2201067469910921','','2018-06-04 08:37:07.763429','2019-03-08 03:50:39.444005',0,7,1,1),(2,'test02a','test02','','','test02@test.com','','','2018-06-17 12:59:25.545308','2018-08-30 07:14:09.818356',0,8,1,1),(3,'NAME','NAME','name','name','email','dummy','dummy','2018-06-29 06:54:45.428211','2018-06-29 06:56:56.964583',0,9,2,1),(8,'','',NULL,NULL,'template@template.com',NULL,NULL,'2018-08-20 08:40:21.401841','2018-08-20 08:40:21.401866',0,16,7,1);
/*!40000 ALTER TABLE `core_vendoruser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_workersqsstatus`
--

DROP TABLE IF EXISTS `core_workersqsstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_workersqsstatus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message_id` varchar(512) DEFAULT NULL,
  `message` longtext,
  `status` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `error_text` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_workersqsstatus`
--

LOCK TABLES `core_workersqsstatus` WRITE;
/*!40000 ALTER TABLE `core_workersqsstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_workersqsstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-06-04 08:33:47.314112','1','00001',1,'[{\"added\": {}}]',11,1),(2,'2018-06-04 08:34:54.251080','1','000001',1,'[{\"added\": {}}]',8,1),(3,'2018-06-04 08:35:32.820438','1','00001-01',1,'[{\"added\": {}}]',10,1),(4,'2018-06-04 08:37:07.772478','1','テスト',1,'[{\"added\": {}}]',15,1),(5,'2018-06-04 12:46:41.366668','1','000001',2,'[{\"changed\": {\"fields\": [\"fbms_access_url_part\", \"fbms_access_token\", \"fbms_verify_token\"]}}]',8,1),(6,'2018-06-05 03:22:33.629071','1','INITIAL',1,'[{\"added\": {}}]',19,1),(7,'2018-06-05 04:00:04.669156','2','dxpUVd_Jun Kawajiri',3,'',4,1),(8,'2018-06-05 04:07:05.620756','3','Jun Kawajiri_ObrA7r',3,'',4,1),(9,'2018-06-05 04:12:27.692926','4','Jun Kawajiri_t0Fg2j',3,'',4,1),(10,'2018-06-05 04:16:25.329288','5','Jun Kawajiri_Rwp0qO',3,'',4,1),(11,'2018-06-05 10:03:00.466389','1','GET_STARTED_PAYLOAD',1,'[{\"added\": {}}]',18,1),(12,'2018-06-05 10:03:25.083750','1','hoge',1,'[{\"added\": {}}]',17,1),(13,'2018-06-05 10:41:26.485100','2','TEST',1,'[{\"added\": {}}]',19,1),(14,'2018-06-06 02:15:05.432278','2','hoge',2,'[{\"changed\": {\"fields\": [\"messaging_api_type\", \"messaging_api_param_json\"]}}]',17,1),(15,'2018-06-06 02:18:05.519541','2','hoge',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(16,'2018-06-06 02:19:10.142544','1','text',2,'[{\"changed\": {\"fields\": [\"admin_text\"]}}]',17,1),(17,'2018-06-06 02:19:15.983219','2','image',2,'[{\"changed\": {\"fields\": [\"admin_text\"]}}]',17,1),(18,'2018-06-06 02:19:22.777221','3','carousel',2,'[{\"changed\": {\"fields\": [\"admin_text\"]}}]',17,1),(19,'2018-06-06 02:26:59.691896','3','carousel',2,'[{\"changed\": {\"fields\": [\"messaging_api_type\"]}}]',17,1),(20,'2018-06-06 03:16:25.777632','3','carousel',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(21,'2018-06-06 03:20:08.308559','1','text',2,'[{\"changed\": {\"fields\": [\"run_order_num\"]}}]',17,1),(22,'2018-06-06 03:20:13.277695','3','carousel',2,'[{\"changed\": {\"fields\": [\"run_order_num\"]}}]',17,1),(23,'2018-06-06 03:21:05.478089','3','carousel',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(24,'2018-06-06 03:22:13.770331','3','carousel',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(25,'2018-06-06 03:23:13.453439','3','carousel',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(26,'2018-06-06 03:23:45.227629','3','carousel',2,'[]',17,1),(27,'2018-06-06 03:24:53.553991','3','carousel',2,'[]',17,1),(28,'2018-06-06 03:25:47.269791','3','carousel',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(29,'2018-06-06 03:45:35.059231','2','image',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(30,'2018-06-06 03:47:35.326171','2','file',2,'[{\"changed\": {\"fields\": [\"cd\", \"name\"]}}]',20,1),(31,'2018-06-06 03:49:22.512015','4','file(PDF)',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(32,'2018-06-06 04:14:50.509221','4','button_select',1,'[{\"added\": {}}]',20,1),(33,'2018-06-06 04:15:29.628924','5','button',1,'[{\"added\": {}}]',17,1),(34,'2018-06-06 04:19:52.604907','5','button',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(35,'2018-06-06 04:46:43.450424','2','__text_input',1,'[{\"added\": {}}]',18,1),(36,'2018-06-06 05:30:02.547111','2','image',2,'[{\"changed\": {\"fields\": [\"payload\"]}}]',17,1),(37,'2018-06-06 05:36:00.761313','2','image',2,'[{\"changed\": {\"fields\": [\"is_delete\"]}}]',17,1),(38,'2018-06-06 05:40:00.478803','1','text',2,'[{\"changed\": {\"fields\": [\"payload\", \"run_order_num\"]}}]',17,1),(39,'2018-06-06 05:40:27.399648','1','text',2,'[{\"changed\": {\"fields\": [\"is_delete\"]}}]',17,1),(40,'2018-06-06 06:37:43.987801','6','はじめまして',2,'[{\"changed\": {\"fields\": [\"payload\", \"messaging_api_param_json\"]}}]',17,1),(41,'2018-06-06 06:39:23.044557','7','どうします？',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\"]}}]',17,1),(42,'2018-06-06 06:39:53.714102','7','どうします？',2,'[{\"changed\": {\"fields\": [\"payload\", \"messaging_api_type\", \"run_order_num\"]}}]',17,1),(43,'2018-06-06 06:42:54.781013','8','受け取り方法は？',2,'[{\"changed\": {\"fields\": [\"payload\", \"messaging_api_type\", \"messaging_api_param_json\"]}}]',17,1),(44,'2018-06-06 06:44:49.929672','11','(PDF送信)',2,'[{\"changed\": {\"fields\": [\"payload\", \"admin_text\"]}}]',17,1),(45,'2018-06-06 06:46:17.392785','10','ありがとうございます',2,'[{\"changed\": {\"fields\": [\"payload\", \"messaging_api_param_json\", \"run_order_num\"]}}]',17,1),(46,'2018-06-06 06:46:26.192762','10','ありがとうございます（PDF）',2,'[{\"changed\": {\"fields\": [\"admin_text\"]}}]',17,1),(47,'2018-06-06 06:46:41.458772','11','(PDF送信)',2,'[{\"changed\": {\"fields\": [\"run_order_num\"]}}]',17,1),(48,'2018-06-06 06:46:47.352443','10','ありがとうございます（PDF）',2,'[]',17,1),(49,'2018-06-06 06:49:58.803813','9','住所を入力してください',2,'[{\"changed\": {\"fields\": [\"payload\", \"next_end_user_state\", \"messaging_api_param_json\"]}}]',17,1),(50,'2018-06-06 06:52:27.749948','12','（住所入力後の返信）',2,'[{\"changed\": {\"fields\": [\"end_user_state\", \"messaging_api_param_json\", \"admin_text\"]}}]',17,1),(51,'2018-06-06 12:16:04.728467','1','Register DATE',1,'[{\"added\": {}}]',27,1),(52,'2018-06-06 12:16:17.782237','2','RESEVATION DATA',1,'[{\"added\": {}}]',27,1),(53,'2018-06-06 12:16:21.100786','2','RESEVATION DATA',2,'[]',27,1),(54,'2018-06-06 12:16:37.151265','3','LAST VISIT',1,'[{\"added\": {}}]',27,1),(55,'2018-06-06 12:29:07.274367','1','REGIST',1,'[{\"added\": {}}]',23,1),(56,'2018-06-06 12:29:32.940019','2','RESERVE follow up',1,'[{\"added\": {}}]',23,1),(57,'2018-06-06 12:30:05.820168','3','follow up',1,'[{\"added\": {}}]',23,1),(58,'2018-06-06 12:30:21.854463','2','remind RESERVATION',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',23,1),(59,'2018-06-06 12:30:39.957831','1','step message from regist_dt',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',23,1),(60,'2018-06-06 13:05:32.971503','1','None',1,'[{\"added\": {}}]',35,1),(61,'2018-06-06 13:05:41.826380','2','NEW',1,'[{\"added\": {}}]',35,1),(62,'2018-06-06 13:05:49.928088','3','In-Progress',1,'[{\"added\": {}}]',35,1),(63,'2018-06-06 13:05:57.762843','4','DONE',1,'[{\"added\": {}}]',35,1),(64,'2018-06-06 13:06:07.129058','5','Pending',1,'[{\"added\": {}}]',35,1),(65,'2018-06-06 14:26:25.452558','9','住所を入力してください',2,'[{\"changed\": {\"fields\": [\"is_todo\"]}}]',17,1),(66,'2018-06-06 14:39:30.567927','9','住所を入力してください',2,'[{\"changed\": {\"fields\": [\"todo_title\"]}}]',17,1),(67,'2018-06-08 07:09:38.672484','7','どうします？',2,'[{\"changed\": {\"fields\": [\"messaging_api_param_json\", \"todo_title\"]}}]',17,1),(68,'2018-06-08 08:39:22.581155','1','TEST EVENT 01',1,'[{\"added\": {}}]',36,1),(69,'2018-06-08 08:39:24.612677','1','TEST EVENT 01',2,'[]',36,1),(70,'2018-06-08 08:39:58.344462','2','TEST EVENT 02',1,'[{\"added\": {}}]',36,1),(71,'2018-06-08 08:40:23.107619','3','TEST EVENT 03',1,'[{\"added\": {}}]',36,1),(72,'2018-06-08 09:17:27.405053','1','TEST RSV 01-01',1,'[{\"added\": {}}]',16,1),(73,'2018-06-09 01:45:48.659810','1','Event Category 1',1,'[{\"added\": {}}]',38,1),(74,'2018-06-09 01:46:23.640250','2','Event Category 2',1,'[{\"added\": {}}]',38,1),(75,'2018-06-09 01:46:42.455136','3','Event Category 3',1,'[{\"added\": {}}]',38,1),(76,'2018-06-09 02:09:28.903131','1','memo',1,'[{\"added\": {}}]',41,1),(77,'2018-06-09 02:09:32.948994','1','memo',2,'[]',41,1),(78,'2018-06-09 07:44:07.625667','1','Event',1,'[{\"added\": {}}]',37,1),(79,'2018-06-09 12:29:23.182078','1','Event',2,'[{\"changed\": {\"fields\": [\"description\", \"url\", \"location\", \"tel\"]}}]',37,1),(80,'2018-06-12 06:21:16.389346','1','registration date',2,'[{\"changed\": {\"fields\": [\"title_name\"]}}]',22,1),(81,'2018-06-12 06:21:54.217492','2','remind',2,'[{\"changed\": {\"fields\": [\"title_name\"]}}]',22,1),(82,'2018-06-12 06:22:24.354804','3','follow up',1,'[{\"added\": {}}]',22,1),(83,'2018-06-13 06:28:24.596070','1','OK',1,'[{\"added\": {}}]',40,1),(84,'2018-06-13 06:28:44.716955','1','https://www.example.com',1,'[{\"added\": {}}]',39,1),(85,'2018-06-14 06:07:15.999038','2','admin',2,'[{\"changed\": {\"fields\": [\"cd\"]}}]',42,1),(86,'2018-06-14 06:07:25.064980','1','testTag',2,'[{\"changed\": {\"fields\": [\"cd\"]}}]',42,1),(87,'2018-06-14 06:09:27.008490','5','Kawajiri',2,'[{\"changed\": {\"fields\": [\"last_name_kana\", \"first_name_kana\", \"age\", \"birth_date\", \"email\", \"address1\", \"address2\", \"tel1\", \"tel2\", \"admin_text\", \"last_login_dt\", \"reservation_data_json\", \"tag\"]}}]',12,1),(88,'2018-06-16 12:41:45.309005','3','hoge',1,'[{\"added\": {}}]',29,1),(89,'2018-06-16 12:42:01.328142','4','hoge',1,'[{\"added\": {}}]',29,1),(90,'2018-06-16 12:42:14.327224','5','hoge',1,'[{\"added\": {}}]',29,1),(91,'2018-06-17 12:57:30.437809','7','test01@test.com',1,'[{\"added\": {}}]',4,1),(92,'2018-06-17 12:58:08.430178','1','テスト',2,'[{\"changed\": {\"fields\": [\"auth_user\", \"email\"]}}]',15,1),(93,'2018-06-26 01:54:34.176271','2','TAG0002',2,'[{\"added\": {\"name\": \"Tagged Item\", \"object\": \"None tagged with TAG0002\"}}]',31,1),(94,'2018-06-26 01:54:56.181141','2','TAG0002',2,'[{\"changed\": {\"name\": \"Tagged Item\", \"object\": \"Jun Kawajiri_gId3ij tagged with TAG0002\", \"fields\": [\"object_id\"]}}]',31,1),(95,'2018-06-26 01:55:41.935089','2','TAG0002',2,'[{\"changed\": {\"name\": \"Tagged Item\", \"object\": \"test tagged with TAG0002\", \"fields\": [\"content_type\"]}}]',31,1),(96,'2018-06-29 06:53:10.719797','9','vendor2',1,'[{\"added\": {}}]',4,1),(97,'2018-06-29 06:53:59.398805','2','2',1,'[{\"added\": {}}]',8,1),(98,'2018-06-29 06:54:18.470951','2','2',1,'[{\"added\": {}}]',10,1),(99,'2018-06-29 06:54:45.433349','3','NAME',1,'[{\"added\": {}}]',15,1),(100,'2018-06-29 06:56:56.969622','3','NAME',2,'[]',15,1),(101,'2018-06-29 07:07:17.600652','2','12',1,'[{\"added\": {}}]',41,1),(102,'2018-08-20 06:13:23.990692','1','system',1,'[{\"added\": {}}]',3,1),(103,'2018-08-20 06:13:42.156933','7','test01@test.com',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(104,'2018-12-06 04:02:21.708659','8','test02@test.com',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(105,'2019-03-05 03:31:49.148998','3','3',1,'[{\"added\": {}}]',62,1),(106,'2019-03-05 03:36:15.372915','1','000001-Free',1,'[{\"added\": {}}]',60,1),(107,'2019-03-05 03:37:07.340976','1','test',1,'[{\"added\": {}}]',61,1),(108,'2019-03-05 05:32:17.638092','1','test',2,'[{\"changed\": {\"fields\": [\"vendor_branch\"]}}]',61,1),(109,'2019-05-08 06:57:20.949962','6','donvermo@gmail.com',3,'',61,1),(110,'2019-05-09 02:48:48.621548','8','donvermo@gmail.com',3,'',61,1),(111,'2019-05-09 07:22:46.980767','1','test message',1,'[{\"added\": {}}]',78,1),(112,'2019-07-11 09:35:35.151614','13','derp@derp.com',3,'',61,1),(113,'2019-07-11 09:35:50.453406','12','123132131test@test.com',3,'',61,1),(114,'2019-07-11 09:35:50.454730','11','donvermo@gmail.com',3,'',61,1),(115,'2019-07-11 09:35:50.455316','5','test97@test.com',3,'',61,1),(116,'2019-07-11 09:35:50.456305','4','test98@test.com',3,'',61,1),(117,'2019-08-27 03:06:27.605791','1','PeaceFactory',1,'[{\"added\": {}}]',90,1),(118,'2019-08-27 03:09:44.326643','1','test01@test.com',1,'[{\"added\": {}}]',92,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(52,'core','affiliate'),(23,'core','automessagecondition'),(21,'core','automessagecontroller'),(26,'core','automessagehistory'),(22,'core','automessagetrigger'),(27,'core','automessagetype'),(116,'core','document'),(12,'core','enduser'),(29,'core','enduserautomessage'),(55,'core','endusercontactchat'),(7,'core','enduserfacebook'),(9,'core','enduserline'),(47,'core','endusersequencestate'),(19,'core','enduserstate'),(17,'core','enduserstory'),(34,'core','enduserstoryhistory'),(44,'core','enduserstorytemplate'),(45,'core','enduserstorytemplatecategory'),(37,'core','event'),(38,'core','eventcategory'),(39,'core','eventreservation'),(40,'core','eventreservationstatus'),(59,'core','file'),(58,'core','logshistory'),(24,'core','manualmessagecontroller'),(28,'core','manualmessagehistory'),(25,'core','manualmessageoverview'),(49,'core','messageblock'),(48,'core','messagesequence'),(43,'core','messagestatus'),(20,'core','messagingapitype'),(18,'core','payload'),(16,'core','reservation'),(36,'core','reservationevent'),(14,'core','reservationhistory'),(11,'core','service'),(56,'core','summarylogendusers'),(57,'core','summarylogvendorusers'),(42,'core','tag'),(13,'core','tagcategory'),(51,'core','tmpentry'),(53,'core','tmpregistrationentry'),(50,'core','todo'),(35,'core','todoactionstatus'),(8,'core','vendor'),(10,'core','vendorbranch'),(41,'core','vendoreventsettings'),(30,'core','vendorreservationsettings'),(15,'core','vendoruser'),(46,'core','workersqsstatus'),(54,'db','testmodel'),(95,'mailroom','matrigger'),(97,'mailroom','matriggertype'),(96,'mailroom','message'),(98,'mailroom','messagehistory'),(102,'mailroom','messagetemplate'),(103,'mailroom','messagetemplatecategory'),(99,'messageflow','bot'),(100,'messageflow','botscenario'),(114,'messageflow','enduser'),(111,'messageflow','enduserbotscenario'),(113,'messageflow','logline'),(104,'messageflow','message'),(107,'messageflow','messageblock'),(105,'messageflow','messagetype'),(112,'messageflow','response'),(101,'messageflow','scenario'),(115,'messageflow','settings'),(90,'nchat','business'),(91,'nchat','businessplan'),(110,'nchat','enduser'),(109,'nchat','file'),(106,'nchat','paymenthistory'),(108,'nchat','settings'),(92,'nchat','vendoruser'),(68,'qa','coupon'),(81,'qa','couponclaim'),(67,'qa','coupontype'),(73,'qa','enduserquestionnaire'),(80,'qa','matrigger'),(79,'qa','matriggertype'),(78,'qa','message'),(94,'qa','notification'),(93,'qa','notificationhistory'),(66,'qa','notificationservice'),(65,'qa','notificationsetting'),(64,'qa','plan'),(82,'qa','product'),(83,'qa','productcategory'),(69,'qa','question'),(70,'qa','questionnaire'),(71,'qa','questionnairequestion'),(88,'qa','questionnairetemplate'),(89,'qa','questionnairetemplatequestion'),(72,'qa','questiontype'),(84,'qa','receivinghistory'),(74,'qa','response'),(75,'qa','senbayuser'),(63,'qa','service'),(85,'qa','shippinghistory'),(86,'qa','stock'),(87,'qa','stockspace'),(76,'qa','vendorbusinesspartner'),(77,'qa','vendorbusinesspartnertag'),(60,'qa','vendorplan'),(62,'qa','vendorservice'),(61,'qa','vendoruser'),(6,'sessions','session'),(31,'taggit','tag'),(32,'taggit','taggeditem'),(33,'taggit_templatetags','amodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=378 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-05-31 02:49:11.943975'),(2,'auth','0001_initial','2018-05-31 02:49:13.046988'),(3,'admin','0001_initial','2018-05-31 02:49:13.176912'),(4,'admin','0002_logentry_remove_auto_add','2018-05-31 02:49:13.192712'),(5,'contenttypes','0002_remove_content_type_name','2018-05-31 02:49:13.293805'),(6,'auth','0002_alter_permission_name_max_length','2018-05-31 02:49:13.331922'),(7,'auth','0003_alter_user_email_max_length','2018-05-31 02:49:13.375630'),(8,'auth','0004_alter_user_username_opts','2018-05-31 02:49:13.389462'),(9,'auth','0005_alter_user_last_login_null','2018-05-31 02:49:13.431117'),(10,'auth','0006_require_contenttypes_0002','2018-05-31 02:49:13.434410'),(11,'auth','0007_alter_validators_add_error_messages','2018-05-31 02:49:13.447711'),(12,'auth','0008_alter_user_username_max_length','2018-05-31 02:49:13.494526'),(13,'auth','0009_alter_user_last_name_max_length','2018-05-31 02:49:13.535995'),(14,'sessions','0001_initial','2018-05-31 02:49:13.580021'),(15,'core','0001_initial','2018-06-02 15:12:35.698010'),(16,'core','0002_reservation_reservationhistory_tagcategory_vendoruser','2018-06-02 15:40:42.482187'),(17,'core','0003_auto_20180603_1330','2018-06-03 04:30:16.368163'),(18,'core','0004_auto_20180603_1403','2018-06-03 05:03:45.034549'),(19,'core','0005_auto_20180603_1422','2018-06-03 05:22:23.749841'),(20,'core','0006_auto_20180603_1434','2018-06-03 05:34:32.843673'),(21,'core','0007_auto_20180603_1443','2018-06-03 05:43:18.380898'),(22,'core','0008_auto_20180603_1448','2018-06-03 05:49:15.967035'),(23,'core','0009_auto_20180603_1449','2018-06-03 05:49:16.576242'),(24,'core','0010_auto_20180603_1458','2018-06-03 05:59:34.367113'),(25,'core','0011_auto_20180603_1459','2018-06-03 05:59:34.943683'),(26,'taggit','0001_initial','2018-06-03 11:51:20.710183'),(27,'taggit','0002_auto_20150616_2121','2018-06-03 11:51:20.746947'),(28,'core','0012_auto_20180603_2051','2018-06-03 11:51:21.207565'),(29,'core','0013_auto_20180603_2245','2018-06-03 13:46:04.250879'),(30,'core','0014_auto_20180606_2147','2018-06-06 12:47:10.193181'),(31,'core','0015_auto_20180606_2149','2018-06-06 12:49:08.410716'),(32,'core','0016_auto_20180606_2156','2018-06-06 12:56:43.582368'),(33,'core','0017_auto_20180606_2202','2018-06-06 13:02:51.536450'),(34,'core','0018_auto_20180606_2204','2018-06-06 13:04:33.282973'),(35,'core','0019_auto_20180606_2338','2018-06-06 14:38:18.697631'),(36,'core','0020_auto_20180608_1539','2018-06-08 06:39:23.013501'),(37,'core','0021_auto_20180608_1616','2018-06-08 07:16:39.271393'),(38,'core','0022_auto_20180608_1738','2018-06-08 08:38:42.020229'),(39,'core','0023_auto_20180608_1747','2018-06-08 08:47:35.932989'),(40,'core','0024_auto_20180609_1023','2018-06-09 01:23:15.838275'),(41,'core','0025_auto_20180609_1030','2018-06-09 01:30:04.319296'),(42,'core','0026_auto_20180609_1038','2018-06-09 01:38:17.821179'),(43,'core','0027_auto_20180609_1100','2018-06-09 02:00:46.829635'),(44,'core','0028_auto_20180609_1122','2018-06-09 02:22:03.077626'),(45,'core','0029_auto_20180612_1632','2018-06-13 07:47:16.049548'),(46,'core','0030_auto_20180612_1639','2018-06-13 07:47:16.568796'),(47,'core','0031_auto_20180613_1647','2018-06-13 07:47:16.979533'),(48,'core','0032_auto_20180613_1831','2018-06-13 09:31:27.594416'),(49,'core','0033_auto_20180614_1504','2018-06-14 06:04:16.046853'),(50,'core','0034_auto_20180614_1806','2018-06-14 09:06:14.058009'),(51,'core','0031_auto_20180613_1454','2018-06-15 01:24:02.632999'),(52,'core','0034_merge_20180614_2222','2018-06-15 01:24:02.637623'),(53,'core','0035_merge_20180615_1023','2018-06-15 01:24:02.644240'),(54,'core','0036_auto_20180615_1040','2018-06-15 01:40:15.623932'),(55,'core','0037_auto_20180616_2140','2018-06-16 12:40:45.225986'),(56,'core','0038_auto_20180616_2141','2018-06-16 12:41:34.086264'),(57,'core','0039_auto_20180616_2244','2018-06-16 13:44:19.485050'),(58,'core','0040_auto_20180619_1731','2018-06-22 07:10:17.530623'),(59,'core','0041_auto_20180623_1312','2018-06-25 01:40:58.262254'),(60,'core','0042_auto_20180623_2038','2018-06-25 01:40:58.981732'),(61,'core','0043_auto_20180627_1704','2018-06-28 02:22:52.794283'),(62,'core','0044_auto_20180627_1749','2018-06-28 02:22:53.499412'),(63,'core','0045_auto_20180628_1122','2018-06-28 02:22:54.028801'),(64,'core','0046_auto_20180702_1611','2018-07-03 01:15:34.179266'),(65,'core','0047_auto_20180702_1612','2018-07-03 01:15:35.008866'),(66,'core','0048_auto_20180702_2142','2018-07-03 01:15:35.598686'),(67,'core','0049_auto_20180703_1651','2018-07-03 07:51:05.241378'),(68,'core','0050_auto_20180707_2113','2018-07-09 02:28:04.757905'),(69,'core','0051_auto_20180707_2124','2018-07-09 02:28:05.353032'),(70,'core','0052_auto_20180709_1127','2018-07-09 02:28:05.816674'),(71,'core','0053_auto_20180711_1433','2018-07-11 05:33:22.819584'),(72,'core','0054_auto_20180711_1726','2018-07-11 08:26:13.173047'),(73,'core','0055_auto_20180711_1727','2018-07-11 08:28:51.081607'),(74,'core','0056_auto_20180711_1728','2018-07-11 08:28:51.520726'),(75,'core','0057_auto_20180711_1743','2018-07-11 08:43:52.879586'),(76,'core','0058_auto_20180713_1150','2018-07-13 02:50:15.915641'),(77,'core','0052_auto_20180709_2123','2018-07-17 09:15:02.383502'),(78,'core','0053_merge_20180713_1511','2018-07-17 09:15:02.389008'),(79,'core','0059_merge_20180713_2203','2018-07-17 09:15:02.393965'),(80,'core','0060_auto_20180714_2320','2018-07-17 09:15:02.870832'),(81,'core','0061_auto_20180714_2321','2018-07-17 09:15:03.439889'),(82,'core','0062_auto_20180714_2328','2018-07-17 09:15:03.853149'),(83,'core','0063_auto_20180715_0101','2018-07-17 09:15:04.221702'),(84,'core','0064_auto_20180721_2259','2018-07-23 06:14:17.623267'),(85,'core','0065_auto_20180721_2304','2018-07-23 06:14:18.066941'),(86,'core','0066_auto_20180725_1537','2018-07-25 06:37:42.646841'),(87,'core','0067_auto_20180725_1607','2018-07-25 07:07:10.777869'),(88,'core','0066_auto_20180724_1611','2018-07-31 01:17:55.435926'),(89,'core','0067_auto_20180725_1814','2018-07-31 01:17:55.913774'),(90,'core','0068_merge_20180730_1355','2018-07-31 01:17:55.919369'),(91,'core','0069_auto_20180730_1355','2018-07-31 01:17:56.497171'),(92,'core','0070_auto_20180730_1546','2018-07-31 01:17:56.910914'),(93,'core','0071_auto_20180730_1722','2018-07-31 01:17:57.399965'),(94,'core','0072_auto_20180731_1017','2018-07-31 01:17:57.870590'),(95,'core','0072_auto_20180801_1703','2018-08-02 00:48:20.725634'),(96,'core','0073_merge_20180802_0948','2018-08-02 00:48:20.734684'),(97,'core','0073_merge_20180802_1133','2018-08-07 03:09:12.777413'),(98,'core','0074_auto_20180802_1654','2018-08-07 03:09:13.260138'),(99,'core','0075_merge_20180807_1209','2018-08-07 03:09:13.264916'),(100,'core','0076_auto_20180814_1501','2018-08-17 03:11:48.467875'),(101,'core','0077_auto_20180817_1211','2018-08-17 03:11:48.740846'),(102,'core','0078_auto_20180821_1803','2018-08-21 09:03:32.914896'),(103,'core','0079_auto_20180823_1258','2018-08-23 03:58:21.781743'),(104,'core','0080_auto_20180823_1717','2018-08-23 08:17:50.414735'),(105,'core','0081_auto_20180919_1448','2018-09-19 05:48:27.128983'),(106,'health_check_db','0001_initial','2018-09-19 05:48:27.158618'),(107,'db','0001_initial','2018-09-19 05:48:27.166582'),(108,'core','0082_auto_20181012_1654','2018-10-12 07:54:54.939457'),(109,'core','0083_auto_20181016_1652','2018-10-16 07:52:41.390059'),(110,'core','0082_auto_20181019_1038','2018-10-31 11:26:27.865532'),(111,'core','0083_auto_20181019_1102','2018-10-31 11:26:28.206417'),(112,'core','0084_auto_20181019_1107','2018-10-31 11:26:28.535324'),(113,'core','0085_auto_20181020_2349','2018-10-31 11:26:28.919198'),(114,'core','0086_auto_20181023_1101','2018-10-31 11:26:29.241661'),(115,'core','0087_auto_20181023_1158','2018-10-31 11:26:29.635663'),(116,'core','0088_auto_20181023_1201','2018-10-31 11:26:29.938969'),(117,'core','0089_auto_20181026_1843','2018-10-31 11:26:30.389279'),(118,'core','0090_auto_20181029_1842','2018-10-31 11:26:30.721912'),(119,'core','0091_merge_20181031_2026','2018-10-31 11:26:30.725828'),(120,'core','0092_auto_20181101_1240','2018-11-01 03:40:43.987853'),(121,'core','0093_auto_20181101_1329','2018-11-01 04:29:39.305413'),(122,'core','0091_merge_20181101_1436','2018-11-05 05:04:23.038637'),(123,'core','0092_auto_20181101_1436','2018-11-05 05:04:23.475123'),(124,'core','0094_merge_20181101_1720','2018-11-05 05:04:23.479548'),(125,'core','0095_auto_20181101_1720','2018-11-05 05:04:23.867971'),(126,'core','0096_auto_20181114_1207','2018-11-14 03:07:56.170552'),(127,'core','0097_auto_20181115_1733','2018-11-15 08:33:49.236881'),(130,'core','0098_todo_message_migration','2018-11-15 09:03:51.780078'),(131,'core','0099_auto_20181128_1021','2018-11-28 01:31:05.377399'),(132,'core','0100_vendor_user_rename_facebook_sender_id','2018-11-28 01:31:05.479208'),(133,'core','0101_auto_20181128_1259','2018-11-28 03:59:49.724031'),(134,'core','0102_vendor_default_token_value','2019-01-17 06:07:52.192126'),(135,'core','0103_auto_20190117_1523','2019-01-17 06:23:25.252387'),(136,'core','0104_auto_20190204_1433','2019-02-04 05:34:02.235326'),(137,'core','0105_auto_20190204_1612','2019-02-05 07:36:52.857269'),(138,'core','0106_auto_20190205_1545','2019-02-05 07:36:53.157296'),(139,'core','0107_auto_20190205_1638','2019-02-05 08:23:41.802065'),(140,'core','0108_auto_20190206_1121','2019-02-08 06:41:23.105085'),(141,'core','0109_auto_20190208_1541','2019-02-08 06:41:23.471012'),(142,'core','0110_auto_20190305_1100','2019-03-05 02:51:46.841970'),(143,'core','0111_auto_20190305_1123','2019-03-05 02:51:47.168151'),(144,'core','0112_auto_20190305_1130','2019-03-05 02:51:47.458030'),(145,'core','0113_auto_20190305_1131','2019-03-05 02:51:47.805825'),(146,'core','0114_auto_20190305_1131','2019-03-05 02:51:48.088866'),(147,'qa','0001_initial','2019-03-05 02:51:48.437949'),(148,'core','0115_auto_20190305_1313','2019-03-05 04:13:49.214679'),(149,'qa','0002_vendoruser_is_active','2019-03-05 04:13:49.315960'),(150,'core','0116_auto_20190308_1341','2019-03-08 04:41:46.758275'),(151,'qa','0003_vendoruser_tel','2019-03-08 04:41:46.865292'),(152,'core','0117_auto_20190312_1046','2019-03-12 01:46:51.509396'),(157,'core','0118_auto_20190312_1059','2019-03-12 02:03:43.688730'),(158,'core','0119_auto_20190312_1100','2019-03-12 02:03:43.956636'),(159,'core','0120_auto_20190312_1101','2019-03-12 02:03:44.233851'),(160,'qa','0004_notificationservice_notificationsetting','2019-03-12 02:04:51.740885'),(161,'core','0121_auto_20190312_1731','2019-03-12 08:34:49.500481'),(162,'core','0122_auto_20190312_1731','2019-03-12 08:34:49.810229'),(163,'qa','0005_auto_20190312_1732','2019-03-12 08:34:49.894119'),(164,'core','0123_auto_20190312_1736','2019-03-12 08:36:42.107499'),(165,'qa','0006_coupon_vendor_branch','2019-03-12 08:36:42.208341'),(166,'core','0124_auto_20190319_1344','2019-03-19 04:44:20.291161'),(167,'qa','0007_auto_20190319_1344','2019-03-19 04:44:20.514712'),(168,'core','0125_auto_20190325_1057','2019-03-25 02:00:28.665877'),(169,'core','0126_auto_20190325_1059','2019-03-25 02:00:28.997233'),(170,'qa','0008_auto_20190325_1057','2019-03-25 02:00:29.025074'),(171,'qa','0009_auto_20190325_1059','2019-03-25 02:00:29.457242'),(172,'core','0127_auto_20190325_1120','2019-03-25 02:20:52.551607'),(173,'qa','0010_question_question_options','2019-03-25 02:20:52.602884'),(174,'core','0128_auto_20190325_1121','2019-03-25 02:21:16.838741'),(175,'core','0129_auto_20190401_1448','2019-04-01 05:49:05.612056'),(176,'qa','0011_enduserquestionnaire_response','2019-04-01 05:49:05.872052'),(177,'core','0130_auto_20190422_1725','2019-04-22 08:25:11.119903'),(178,'qa','0012_auto_20190422_1725','2019-04-22 08:25:11.158268'),(179,'core','0130_auto_20190419_1352','2019-05-07 01:40:20.136903'),(180,'core','0131_auto_20190420_2153','2019-05-07 01:40:20.508934'),(181,'core','0132_auto_20190420_2213','2019-05-07 01:40:20.913033'),(182,'core','0133_merge_20190501_1138','2019-05-07 01:40:20.918005'),(183,'core','0134_auto_20190501_1138','2019-05-07 01:40:21.250817'),(184,'core','0135_auto_20190501_1606','2019-05-07 01:40:21.656445'),(185,'core','0136_auto_20190501_1807','2019-05-07 01:40:21.986694'),(186,'core','0137_auto_20190501_1812','2019-05-07 01:40:22.379906'),(187,'qa','0012_auto_20190419_1352','2019-05-07 01:40:22.415269'),(188,'qa','0013_senbayuser','2019-05-07 01:40:22.503463'),(189,'qa','0014_auto_20190420_2213','2019-05-07 01:40:22.526226'),(190,'qa','0015_merge_20190501_1138','2019-05-07 01:40:22.531080'),(191,'qa','0016_vendorbusinesspartner','2019-05-07 01:40:22.617455'),(192,'qa','0017_vendorbusinesspartnertag','2019-05-07 01:40:22.702601'),(193,'qa','0018_auto_20190501_1807','2019-05-07 01:40:22.745691'),(194,'qa','0019_vendorbusinesspartner_tag_csv','2019-05-07 01:40:22.775492'),(195,'core','0138_auto_20190507_1323','2019-05-07 04:23:12.963518'),(196,'qa','0020_auto_20190507_1323','2019-05-07 04:23:13.031507'),(197,'core','0139_auto_20190507_1344','2019-05-07 04:44:20.225932'),(198,'qa','0021_auto_20190507_1344','2019-05-07 04:44:20.289865'),(199,'core','0140_auto_20190509_1557','2019-05-09 06:57:53.590391'),(200,'core','0141_auto_20190509_1615','2019-05-09 07:15:17.426693'),(201,'qa','0022_message','2019-05-09 07:15:17.553322'),(202,'core','0142_auto_20190510_1511','2019-05-10 06:19:31.521811'),(203,'core','0143_auto_20190510_1513','2019-05-10 06:19:31.930964'),(204,'qa','0023_auto_20190510_1513','2019-05-10 06:19:32.254073'),(205,'core','0144_auto_20190510_1819','2019-05-10 09:19:40.891232'),(206,'qa','0024_auto_20190510_1819','2019-05-10 09:19:40.986921'),(207,'core','0145_auto_20190511_1838','2019-05-11 09:38:50.898902'),(208,'core','0146_auto_20190513_1306','2019-05-14 02:09:41.415216'),(209,'core','0147_auto_20190514_1109','2019-05-14 02:09:41.782379'),(210,'qa','0025_auto_20190514_1109','2019-05-14 02:09:41.834772'),(211,'core','0148_auto_20190516_1640','2019-05-16 07:40:48.666051'),(212,'qa','0026_auto_20190516_1640','2019-05-16 07:40:48.718939'),(213,'core','0149_auto_20190520_1622','2019-05-20 07:25:01.951631'),(214,'qa','0027_message_type','2019-05-20 07:30:38.330782'),(215,'core','0150_auto_20190521_1636','2019-05-21 07:36:19.181734'),(216,'qa','0028_couponclaim','2019-05-21 07:36:19.325938'),(217,'core','0151_auto_20190521_1739','2019-05-21 08:39:35.596483'),(218,'core','0152_auto_20190522_1756','2019-05-22 08:56:59.067983'),(219,'qa','0029_auto_20190522_1756','2019-05-22 08:56:59.164358'),(220,'core','0153_auto_20190531_1633','2019-05-31 07:33:29.094763'),(221,'core','0154_auto_20190603_0815','2019-06-04 05:33:05.873176'),(222,'core','0155_auto_20190604_1432','2019-06-04 05:33:06.307617'),(223,'qa','0030_auto_20190604_1432','2019-06-04 05:33:06.401976'),(224,'core','0156_auto_20190604_1527','2019-06-04 06:28:02.083107'),(225,'qa','0031_auto_20190604_1527','2019-06-04 06:28:02.182394'),(226,'core','0157_auto_20190609_1638','2019-06-12 06:46:38.429452'),(227,'core','0158_auto_20190609_1930','2019-06-12 06:46:38.847016'),(228,'core','0159_auto_20190609_1930','2019-06-12 06:46:39.208485'),(229,'core','0160_auto_20190610_1030','2019-06-12 06:46:39.635662'),(230,'core','0161_auto_20190611_1639','2019-06-12 06:46:39.995074'),(231,'core','0162_auto_20190611_1841','2019-06-12 06:46:40.410953'),(232,'core','0163_auto_20190611_1842','2019-06-12 06:46:40.822114'),(233,'core','0164_auto_20190611_1842','2019-06-12 06:46:41.168073'),(234,'qa','0032_auto_20190609_1638','2019-06-12 06:46:41.986334'),(235,'qa','0033_auto_20190609_1930','2019-06-12 06:46:42.037384'),(236,'qa','0034_auto_20190609_1930','2019-06-12 06:46:42.088856'),(237,'qa','0035_remove_question_question_options','2019-06-12 06:46:42.175042'),(238,'qa','0036_question_question_options','2019-06-12 06:46:42.268160'),(239,'qa','0037_default_charset','2019-06-12 06:58:05.158842'),(240,'core','0165_auto_20190618_1306','2019-06-18 07:09:23.904211'),(241,'core','0166_auto_20190618_1609','2019-06-18 07:09:24.379652'),(242,'core','0167_auto_20190619_1009','2019-06-19 01:09:13.604243'),(243,'core','0168_auto_20190619_1619','2019-06-19 07:20:01.739758'),(244,'qa','0038_questionnairetemplate','2019-06-19 07:20:01.871717'),(245,'core','0169_auto_20190619_1633','2019-06-19 07:33:29.231728'),(246,'qa','0039_remove_questionnairetemplate_questionnaire','2019-06-19 07:33:29.334470'),(247,'core','0170_auto_20190619_1642','2019-06-19 07:42:12.228723'),(248,'qa','0040_questionnairetemplatequestion','2019-06-19 07:42:12.358342'),(249,'core','0171_auto_20190619_1658','2019-06-19 07:58:14.835838'),(250,'qa','0041_auto_20190619_1658','2019-06-19 07:58:14.869730'),(251,'core','0172_auto_20190620_1527','2019-06-20 06:32:22.137066'),(252,'qa','0042_multi_option_type','2019-06-20 06:32:22.150820'),(253,'qa','0043_questionnaretype','2019-06-24 08:34:08.148340'),(254,'core','0173_auto_20190730_1609','2019-07-30 07:10:11.486506'),(255,'qa','0044_auto_20190730_1609','2019-07-30 07:10:11.547999'),(256,'core','0174_auto_20190730_1611','2019-07-30 07:11:38.055182'),(257,'core','0175_auto_20190730_1612','2019-07-30 07:12:38.668875'),(258,'core','0176_auto_20190801_1521','2019-08-26 08:32:17.434241'),(259,'core','0177_auto_20190826_1732','2019-08-26 08:32:17.886148'),(260,'core','0178_auto_20190827_1154','2019-08-27 02:58:48.428531'),(261,'core','0179_auto_20190827_1158','2019-08-27 02:58:48.891297'),(263,'core','0180_auto_20190827_1206','2019-08-27 03:06:09.788186'),(265,'core','0177_auto_20190906_1844','2019-09-06 09:49:43.667877'),(266,'core','0178_auto_20190906_1900','2019-09-09 05:49:00.156889'),(267,'core','0179_auto_20190909_1418','2019-09-09 05:49:00.903641'),(268,'qa','0045_notification_notificationhistory','2019-09-09 05:49:01.140431'),(269,'mailroom','0001_initial','2019-10-01 05:10:55.433301'),(270,'mailroom','0002_auto_20191001_1621','2019-10-01 07:22:04.255276'),(271,'mailroom','0003_auto_20191001_1633','2019-10-01 07:34:38.479698'),(272,'mailroom','0004_auto_20191001_1633','2019-10-01 07:34:38.913301'),(273,'mailroom','0005_auto_20191002_1546','2019-10-02 06:46:51.224271'),(274,'mailroom','0006_auto_20191003_1133','2019-10-03 02:36:11.863442'),(275,'core','0181_auto_20190903_1121','2019-10-08 05:40:03.715340'),(276,'core','0177_auto_20190925_1311','2019-10-08 05:40:04.481618'),(277,'core','0178_auto_20190925_1316','2019-10-08 05:40:05.353420'),(278,'core','0182_merge_20191003_1726','2019-10-08 05:40:05.361221'),(279,'core','0183_merge_20191008_1437','2019-10-08 05:40:05.369590'),(280,'mailroom','0007_auto_20191008_1430','2019-10-08 05:40:05.525312'),(281,'mailroom','0008_auto_20191008_1439','2019-10-08 05:40:05.560295'),(285,'mailroom','0009_auto_20191008_1501','2019-10-08 06:01:40.427852'),(286,'mailroom','0010_auto_20191009_1652','2019-10-09 07:53:31.671746'),(287,'mailroom','0011_messagehistory_status','2019-10-09 07:53:31.822525'),(288,'mailroom','0012_auto_20191009_1704','2019-10-09 08:04:49.806695'),(289,'mailroom','0013_auto_20191009_1800','2019-10-09 09:00:45.193769'),(290,'mailroom','0014_auto_20191010_1033','2019-10-10 01:33:19.187793'),(291,'mailroom','0015_remove_messagehistory_send_dt','2019-10-10 02:10:11.904170'),(292,'mailroom','0016_messagehistory_send_dt','2019-10-10 02:11:33.422386'),(294,'core','0184_auto_20191018_1808','2019-10-18 09:08:40.246316'),(297,'nchat','0001_initial','2019-10-21 02:41:58.191803'),(298,'nchat','0002_auto_20190903_1547','2019-10-21 02:41:58.398948'),(299,'nchat','0003_auto_20191018_1808','2019-10-21 02:41:58.419466'),(300,'core','0185_auto_20191021_1648','2019-10-21 08:11:28.949681'),(301,'core','0186_auto_20191021_1654','2019-10-21 08:11:29.727981'),(302,'core','0187_auto_20191021_1711','2019-10-21 08:11:30.639590'),(304,'nchat','0004_auto_20191021_1648','2019-10-21 08:11:31.206876'),(305,'nchat','0005_paymenthistory','2019-10-21 08:11:31.433597'),(306,'core','0188_auto_20191022_1539','2019-10-22 06:40:13.463370'),(307,'core','0189_auto_20191022_1540','2019-10-22 06:40:14.174659'),(308,'nchat','0006_businessplan_description','2019-10-22 06:40:14.337169'),(309,'core','0184_auto_20191011_1736','2019-10-30 09:08:24.786143'),(310,'core','0185_auto_20191011_1737','2019-10-30 09:08:25.500011'),(311,'core','0186_merge_20191030_1754','2019-10-30 09:08:25.507126'),(312,'core','0190_merge_20191030_1808','2019-10-30 09:08:25.514540'),(313,'messageflow','0001_initial','2019-10-30 09:08:26.090519'),(314,'nchat','0003_auto_20191011_1736','2019-10-30 09:08:26.111094'),(315,'nchat','0004_merge_20191030_1723','2019-10-30 09:08:26.118645'),(316,'nchat','0007_merge_20191030_1808','2019-10-30 09:08:26.126348'),(317,'core','0191_auto_20191101_1709','2019-11-01 08:10:20.620015'),(318,'nchat','0008_auto_20191101_1709','2019-11-01 08:10:20.640768'),(319,'core','0192_auto_20191101_1726','2019-11-01 08:26:22.479551'),(321,'core','0193_auto_20191101_1804','2019-11-01 09:04:21.034230'),(323,'core','0194_auto_20191101_1804','2019-11-01 09:05:34.536031'),(324,'core','0195_auto_20191101_1805','2019-11-01 09:06:59.373467'),(325,'core','0196_auto_20191101_1807','2019-11-01 09:50:44.302609'),(326,'core','0197_auto_20191105_1022','2019-11-05 01:23:09.698328'),(327,'core','0198_auto_20191105_1027','2019-11-05 01:28:30.562507'),(328,'core','0199_auto_20191105_1029','2019-11-05 01:34:03.742121'),(329,'core','0200_auto_20191105_1030','2019-11-05 01:34:04.655503'),(330,'core','0201_auto_20191105_1033','2019-11-05 01:34:05.403314'),(331,'core','0202_auto_20191105_1036','2019-11-05 01:36:55.135484'),(332,'nchat','0009_settings','2019-11-05 02:34:49.045864'),(333,'core','0203_auto_20191105_1100','2019-11-07 03:55:29.675790'),(334,'core','0204_auto_20191105_1125','2019-11-07 03:55:30.297786'),(335,'core','0205_auto_20191105_1128','2019-11-07 03:55:31.025146'),(336,'core','0206_auto_20191105_1134','2019-11-07 03:55:31.778800'),(337,'core','0207_auto_20191107_1255','2019-11-07 03:55:32.408819'),(338,'messageflow','0002_auto_20191107_1255','2019-11-07 03:55:32.427812'),(339,'nchat','0010_file','2019-11-07 03:55:32.479430'),(340,'core','0208_auto_20191112_1534','2019-11-12 06:36:17.934752'),(341,'mailroom','0017_trigger_type_seed','2019-11-12 06:36:17.951358'),(342,'messageflow','0003_message_type_seed','2019-11-12 06:36:17.967620'),(343,'core','0209_auto_20191112_1835','2019-11-12 09:36:30.313265'),(344,'core','0210_auto_20191112_1848','2019-11-12 09:48:48.873490'),(345,'core','0208_auto_20191111_1027','2019-11-13 06:24:49.892950'),(346,'core','0209_merge_20191113_0842','2019-11-13 06:24:49.901289'),(347,'core','0210_auto_20191113_1145','2019-11-13 06:24:50.550974'),(348,'core','0211_auto_20191113_1524','2019-11-13 06:24:51.400949'),(349,'messageflow','0004_enduserbotscenario_response','2019-11-13 06:24:51.641533'),(350,'nchat','0011_enduser','2019-11-13 06:24:51.812290'),(351,'nchat','0012_auto_20191113_1447','2019-11-13 06:24:51.957337'),(352,'messageflow','0005_auto_20191114_1227','2019-11-14 03:38:24.592264'),(353,'core','0212_auto_20191118_1654','2019-11-20 01:55:24.735792'),(354,'messageflow','0006_message_type_image_and_file_seed','2019-11-20 01:55:24.751724'),(355,'messageflow','0007_enduser','2019-11-20 01:55:24.978887'),(356,'messageflow','0008_auto_20191119_1939','2019-11-20 01:55:25.505122'),(357,'nchat','0013_auto_20191118_1654','2019-11-20 01:55:25.904524'),(358,'messageflow','0009_settings','2019-11-29 08:07:06.936443'),(359,'messageflow','0010_auto_20191203_1212','2019-12-03 03:12:37.992405'),(362,'messageflow','0011_target_message_seed','2019-12-05 04:19:38.077847'),(363,'messageflow','0012_merge_20191205_1315','2019-12-05 04:19:38.090588'),(364,'messageflow','0013_auto_20191212_1736','2019-12-12 08:37:03.405186'),(365,'messageflow','0014_auto_20191213_1537','2019-12-17 02:03:43.437230'),(366,'messageflow','0015_auto_20191213_1556','2019-12-17 02:03:43.462495'),(367,'messageflow','0016_auto_20191217_1113','2019-12-17 02:13:33.681413'),(368,'admin','0003_logentry_add_action_flag_choices','2021-06-01 11:54:41.008612'),(369,'auth','0010_alter_group_name_max_length','2021-06-01 11:54:41.227255'),(370,'auth','0011_update_proxy_permissions','2021-06-01 11:54:41.330037'),(371,'auth','0012_alter_user_first_name_max_length','2021-06-01 11:54:41.459312'),(372,'taggit','0003_taggeditem_add_unique_index','2021-06-01 11:54:41.575921'),(373,'core','0213_auto_20210610_1728','2021-06-10 08:28:27.688159'),(374,'core','0214_auto_20210617_0226','2021-06-16 17:27:39.625390'),(375,'core','0214_auto_20210617_1003','2021-06-17 07:42:09.701218'),(376,'core','0215_merge_20210617_1642','2021-06-17 07:42:09.704182'),(377,'core','0110_auto_20210720_1725','2021-07-20 08:26:18.062528');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1u40iy3xiw1mxd8lr3h8p457iaer3f7j','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2020-01-30 07:45:03.598419'),('3aabx0crjv1ts7xki3zhuhfu8bo01yay','ZmQ2ZmVhNDFkYjU2MmFiODAxMzYxODg0MDNkOTc4NDE0MWYzZWI0Yjp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2018-07-12 04:15:17.026977'),('4xx2hktzbct6vgxehmd05j46zixse4mz','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-08-14 00:09:18.725028'),('63misfq7vtvm32pfqnl1jc2n11vkun0v','YWY2YWQ3OTQ3YTgwNmU3MDY2ODNkMzhhNzZiMTgyYzVkZTM3YmJiNjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-10-15 03:11:24.786322'),('6pees7zjwxo0vibiwq1p6fm9j1l0h3y3','ZWFkYTE5ZGFiN2FiZGE3YzQ4OWJkMDVjMmI0NTUwOTAwODUwMmNjNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDBiYTcyZDFlZDk2ZDczNDc1YzU5NDU3MWNlZTBiMmI3ZmQ4OGY2In0=','2018-06-18 08:33:05.656389'),('75odj8mvgj7o9wk03ifoylexd8l34p40','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-09-03 07:11:50.861140'),('7d47p7d4oldvsxpkooxkanf79f9tpf1q','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-17 06:02:29.558616'),('7jtq0g44vci8aptherxwyw6n9chhpvwj','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-11-27 07:10:42.884707'),('8g4spfy75le30d8zt2v41vhsajil2jas','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-12-16 02:37:24.882190'),('8wsgjc6p3hxfgnq7u7c631987lix37xn','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-11-27 03:50:56.924828'),('8yk5oacadxr7q0mcuiiuin7akiyyo9qj','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-25 05:36:42.182801'),('bvo0n1denhokt4329c6avwp2kj5ntuqv','MDdhMzNhODY4YzIyYWJlYWE4ODM3MGM3ZWI4NjBmOWYyZmE3YjU4ZDp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNzFiMTNmYzZlOGI5YmQwNDU0ZDkzNTAyOTM1NjA1YjZkMGZhNzc2In0=','2018-11-13 05:15:05.394953'),('c2ufv0jxqe9du8z29133uvc13ygdhug9','MDhmOWFkYmE2YmIwMTZlZWFjODVmZDdmNTY4ZTYwYzdlMTIyYTBjZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDBiYTcyZDFlZDk2ZDczNDc1YzU5NDU3MWNlZTBiMmI3ZmQ4OGY2Iiwic3RhdGUiOiJaUnBmSTd4QXZmamliWmtxME5SdW93cDVpTGpxRVIiLCJjcmVkZW50aWFscyI6eyJ0b2tlbiI6InlhMjkuR2x2V0JmYkVzb0lKTkQyR2ZhYzM1V2dRaG9wV0V3cE92akplZ2JLYUl1XzI2QjFDN2Q5MVV4X2R5RFhNdFhOTzl5UDNXcElJNFRNbkpfZE1lYjZUd1RrVzRrY08tejVSNzRKbWhrSWhVb20tYVNpYkhjX1lkVDd2RmVqZSIsInJlZnJlc2hfdG9rZW4iOiIxL1otMFM4MktibXFuekswSFJGamRPRHAyZ0tQX3Bhb3BPZTZyNUg5a3prZW83YVlHaHROVjEwc3FZenpkQTFJZ2QiLCJ0b2tlbl91cmkiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvdG9rZW4iLCJjbGllbnRfaWQiOiI3MDYwMjY3Njc3NzMtcThmMnRxZjlkdTIzY2RqazZkaWtrbmZocWY0cTdzbDguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJjbGllbnRfc2VjcmV0IjoiMU9OMGM5R1RaUzFmdWR3SDdpZVgzYWhCIiwic2NvcGVzIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC9jYWxlbmRhciJ9fQ==','2018-06-24 13:28:43.055796'),('cf3cpetbnvnzk5enq1mfbjt6ij47itaa','YTdlMDI0Y2RiMTNiNTEwOTQ0MTVkYTBkYjcxMWE3NjlmYTA0ZGUwMTp7Il9hdXRoX3VzZXJfaWQiOiIyMzAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjAzZjdjMjk0Mjk1NzE0MWYwOGYwMWQ3YTQ2MmI0NDcwNWNjZDU1NGYiLCJfbGFuZ3VhZ2UiOiJlbiJ9','2019-12-31 02:21:33.856913'),('ct1h47jwxcg2z6p4dqm90slssrvms1bl','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-03-19 04:58:20.995204'),('d38l7w7i0mn5h45whiacalkngbyc02ep','ZWFkYTE5ZGFiN2FiZGE3YzQ4OWJkMDVjMmI0NTUwOTAwODUwMmNjNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDBiYTcyZDFlZDk2ZDczNDc1YzU5NDU3MWNlZTBiMmI3ZmQ4OGY2In0=','2018-06-14 02:50:00.215700'),('dx8ortu22iz1gwedjr2wubzi2erqkbop','NzcwZjc1MmE1YzI5OTViMmQwMzM0YjQ3NDkyYzY1NjZlYTJkMTQ1MTp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNzFiMTNmYzZlOGI5YmQwNDU0ZDkzNTAyOTM1NjA1YjZkMGZhNzc2IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2018-10-02 02:29:58.583033'),('e75a594w644ij0ulbwqx0sc7cuktst1x','ZTgwODJlYjI4NzYxZjgyMWJjNjg0NmQwNzliNDlmYjljM2FlYzU2ZTp7Il9sYW5ndWFnZSI6ImVuIn0=','2018-09-03 02:28:04.568484'),('fo7fkk4vh23ty9senxlg75m41benxi8o','YzVhMDM1YTM0YTRjNGYwM2JjNGFhZWFmMWRjYWZjOTBmMDM5MWY2ZTp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNmIyYTJiNWVhODkzNWRmODZmNmUwMzVjZDhlOTBmZDc4MGI2Zjc0IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2021-07-07 02:23:03.008086'),('fzfc3wbwctv43t183bprysb6mze7d68g','YWRhYjI5YTZjMTNhM2JjZTQ0MWYzZjRlMWU0Y2YxYzQ2MmIxY2EzYzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0IiwiX2xhbmd1YWdlIjoiamEifQ==','2019-09-04 03:51:26.346976'),('hdn1cm6aj84j7kmzxcdqb96a7riq46bh','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-09-13 05:39:11.887429'),('ivurmmpkrp1sbehbee7rd8ri426w3dfb','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-12 04:13:55.777071'),('jiytbnn16ias6w199xf25wx1ekey3xl7','YmRjY2Y4OWM0MzMyM2IxYmNjMjM5NjUzODQ4ODNjODI3YzczZmZkZTp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYzY4YzQ0ODBhNDhmN2JmYzIyYjc1Y2RkMWRlMWMwNTJkZWYxZDVkIn0=','2021-08-02 08:39:35.246427'),('kpjtgyxkzupwy3dk1g6c7id7vr1twtzz','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2018-12-24 01:13:57.503073'),('m5it4whkfemljk3uqfamjprwm2rg9ypo','YWY2YWQ3OTQ3YTgwNmU3MDY2ODNkMzhhNzZiMTgyYzVkZTM3YmJiNjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-05-06 05:05:20.084601'),('mbk1gkmn9jkzwe8jzjpyl4wg6e0ujwwf','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-13 04:20:57.939242'),('mn1qs5ozhwamvr44xifhn6iandxmuruw','YWY2YWQ3OTQ3YTgwNmU3MDY2ODNkMzhhNzZiMTgyYzVkZTM3YmJiNjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-09-25 06:59:44.859432'),('n0lmoklpkkd052hk5cx4bjnjlnoiaj99','YTkyMWEwZDE5ODJmOWM5NzVlY2JjNWQxNGI4ZTc2YTY0ODA1YzMwNjp7Il9sYW5ndWFnZSI6ImVuIiwiX2F1dGhfdXNlcl9pZCI6IjciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjE3MWIxM2ZjNmU4YjliZDA0NTRkOTM1MDI5MzU2MDViNmQwZmE3NzYifQ==','2018-09-17 02:53:47.563883'),('n1u4oxg9d5o6attzaixymtyg01x87ub2','MDdhMzNhODY4YzIyYWJlYWE4ODM3MGM3ZWI4NjBmOWYyZmE3YjU4ZDp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNzFiMTNmYzZlOGI5YmQwNDU0ZDkzNTAyOTM1NjA1YjZkMGZhNzc2In0=','2018-08-22 01:57:11.834670'),('njnu6a18nwf1krvirev4mbckzxh3skuz','N2RlNGJmMzg2M2YzYWFmYWMxNjY0MWU1OTYxNGZmZDdhODRjNjlhYjp7Il9sYW5ndWFnZSI6ImVuIiwiX2F1dGhfdXNlcl9pZCI6IjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjZkZjI2YTM0NjM0YjAzYjUwZmE3NzkyYTQzOWNlN2JjMmQxOWNjMzkifQ==','2018-08-21 01:34:46.999756'),('o7e1xljrqm4qkn7mdf265p2x0ybl44uj','ZDQyOTMzMWVhYWU0YWRkM2M2NWEyMDAxNzhmMjFmMDk2OTNmNjg0MTp7Il9hdXRoX3VzZXJfaWQiOiIxOTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMwM2NlYThiM2RlOTE3NWVjMWRmYTRlYjRkMTdlZWUzNzlkNWM1MjIiLCJfbGFuZ3VhZ2UiOiJlbiJ9','2020-02-11 02:56:42.973427'),('pqt72rk4etmcou8bjzjdlyizp945qn7u','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-04-24 05:28:23.229918'),('r4lrvorc0ej0e67wj9bmq1ic0swlkkl1','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-10-17 09:13:29.359381'),('skwhh0wvuk9q4dyhnh4jvhhsomyey5bw','YWY2YWQ3OTQ3YTgwNmU3MDY2ODNkMzhhNzZiMTgyYzVkZTM3YmJiNjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-05-31 03:23:51.033641'),('tl3h5zyenbbsni26yt9366qth8fk3opq','ZTI3NDBkYTVjYjAyZTA4YjQ1ODJlZGFiMzU1MWI1YThmYjk3NzI2Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDBiYTcyZDFlZDk2ZDczNDc1YzU5NDU3MWNlZTBiMmI3ZmQ4OGY2Iiwic3RhdGUiOiJyU3pIM2ZRSUVCZVB6Qlh6V1RmcTFvNnU5VmFzRzAifQ==','2018-06-24 13:23:23.303100'),('tm93xtryk5k1dtk0uxb4nps3vxrj9qsu','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2020-01-24 06:29:04.577535'),('uqxosspjbo6ch4anvwd5afzy3l14uecv','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-01 13:00:00.965734'),('vtb3mp3jmcjh9xaq5l8mm7i16nczbjvo','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-12 03:10:36.078201'),('w2f3uqoaoaslcclyild8fc6lako3ppf3','.eJxVjjsOgzAQRO_iOrIcg38p03MGy7veBRJkJAxVlLsHIoqknTfzNC8R07YOcau0xDGLm3Di8ptBwieVA-RHKv0scS7rMoI8KvKkVXZzpul-dv8EQ6rDvkYGFzBbA7oF12ijFRFBdmxZccgarVc-tCFZZzR6INsgY2BjNKvrVzrtB7bU066jIt4f8zo95Q:1lqXTH:dBdT7-Pod2JqgP5nMCacmeP9BDdm7XAeENknp_nyCWY','2021-06-22 08:52:27.416362'),('w5sz7q3vebem0tz8rclfo1kq30edcqhy','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2018-12-13 02:08:54.108535'),('wotlcrrnwg1bvbmrz5ay3hbafkje7t3j','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-04-24 05:26:46.739658'),('wx3smj5k53oempm07vs0mv1to0x7u3n0','ZWFkYTE5ZGFiN2FiZGE3YzQ4OWJkMDVjMmI0NTUwOTAwODUwMmNjNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDBiYTcyZDFlZDk2ZDczNDc1YzU5NDU3MWNlZTBiMmI3ZmQ4OGY2In0=','2018-06-17 11:55:17.360772'),('xppemz7vqh6b7uu7k5wwz4485fdpt5xk','YWY2YWQ3OTQ3YTgwNmU3MDY2ODNkMzhhNzZiMTgyYzVkZTM3YmJiNjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0IiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-04-01 06:57:30.692851'),('z1dkpehjc5pm4btt9trp2nxo596s0p2y','MjEwNThlZjMwNTdkZDljMmE2ZDdmNmUzYTA1ZTk2ODllZmVmN2Y2ZDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZGYyNmEzNDYzNGIwM2I1MGZhNzc5MmE0MzljZTdiYzJkMTljYzM5In0=','2018-07-17 03:35:03.494637'),('z5pekrv2jdkpt9rlkj3dy99gmvgxsdjg','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-11-12 08:20:00.890551'),('znb11r1d7z3lydj8v779tcx4vq3lkrib','Y2IyYzM1NDA3MjU4NzA5NzQ2MGViYTYwZWFhYWJmZDAzZGQ3ZGZmMzp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDljNjQ3OGY3N2M2NjEzN2Y2ZmI5ZmFiNjk4YmVlOGQ1Y2Q3NmI0In0=','2019-07-25 06:02:03.081011');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_check_db_testmodel`
--

DROP TABLE IF EXISTS `health_check_db_testmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `health_check_db_testmodel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_check_db_testmodel`
--

LOCK TABLES `health_check_db_testmodel` WRITE;
/*!40000 ALTER TABLE `health_check_db_testmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_check_db_testmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailroom_matrigger`
--

DROP TABLE IF EXISTS `mailroom_matrigger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mailroom_matrigger` (
  `id` int NOT NULL AUTO_INCREMENT,
  `days` int NOT NULL,
  `hours` int NOT NULL,
  `message_id` int NOT NULL,
  `trigger_type_id` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mailroom_matrigger_message_id_3df00522_fk_mailroom_message_id` (`message_id`),
  KEY `mailroom_matrigger_trigger_type_id_8f7c9d9c_fk_mailroom_` (`trigger_type_id`),
  CONSTRAINT `mailroom_matrigger_message_id_3df00522_fk_mailroom_message_id` FOREIGN KEY (`message_id`) REFERENCES `mailroom_message` (`id`),
  CONSTRAINT `mailroom_matrigger_trigger_type_id_8f7c9d9c_fk_mailroom_` FOREIGN KEY (`trigger_type_id`) REFERENCES `mailroom_matriggertype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailroom_matrigger`
--

LOCK TABLES `mailroom_matrigger` WRITE;
/*!40000 ALTER TABLE `mailroom_matrigger` DISABLE KEYS */;
INSERT INTO `mailroom_matrigger` VALUES (88,1,1,90,1,0),(89,0,0,91,1,1),(90,0,0,92,1,1),(91,0,0,93,1,1),(92,0,0,94,1,0),(93,0,0,95,1,0),(94,0,0,96,1,0),(96,0,0,98,1,0);
/*!40000 ALTER TABLE `mailroom_matrigger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailroom_matriggertype`
--

DROP TABLE IF EXISTS `mailroom_matriggertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mailroom_matriggertype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailroom_matriggertype`
--

LOCK TABLES `mailroom_matriggertype` WRITE;
/*!40000 ALTER TABLE `mailroom_matriggertype` DISABLE KEYS */;
INSERT INTO `mailroom_matriggertype` VALUES (1,'after joining'),(2,'after taking survey'),(3,'after using coupon'),(4,'after no activity'),(5,'after new survey goes live'),(6,'after new coupon goes live'),(7,'before coupon expires'),(8,'before survey expires'),(9,'before birthday');
/*!40000 ALTER TABLE `mailroom_matriggertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailroom_message`
--

DROP TABLE IF EXISTS `mailroom_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mailroom_message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(256) NOT NULL,
  `message_text` longtext NOT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailroom_message`
--

LOCK TABLES `mailroom_message` WRITE;
/*!40000 ALTER TABLE `mailroom_message` DISABLE KEYS */;
INSERT INTO `mailroom_message` VALUES (1,'first message','its good to be first',7,'nchat'),(2,'2nd message','deuxieme',7,'nchat'),(3,'third message','triumphant',7,'nchat'),(4,'fourth','',7,'nchat'),(5,'','',1,'123'),(6,'','',1,'123'),(7,'','',1,'123'),(8,'','',1,'123'),(9,'','',1,'123'),(10,'','',1,'123'),(11,'','',1,'123'),(12,'','',1,'123'),(13,'','',1,'123'),(14,'','',1,'123'),(15,'','',1,'123'),(16,'','',1,'123'),(20,'hello','<p>how are you?</p>',1,'123'),(31,'one','<p>1</p>',1,'123'),(32,'02    We should be able to delete!','<p>We should be able!</p>',1,'123'),(33,'boo','<p>help</p>',1,'123'),(38,'','',1,'123'),(39,'','',1,'123'),(40,'','',1,'123'),(41,'','',1,'123'),(43,'this saves','<p>saving</p>',1,'123'),(44,'','',1,'123'),(49,'foo template','foo you too',0,'mail_template'),(50,'bar template','you\'ve been barred',0,'mail_template'),(75,'','',147,'nchat'),(76,'This is a new trigger','<p>Text.</p>',147,'nchat'),(78,'','',147,'nchat'),(79,'','',147,'nchat'),(80,'','',147,'nchat'),(81,'','',147,'nchat'),(82,'','',147,'nchat'),(85,'','',7,'nchat'),(86,'','',7,'nchat'),(88,'','',7,'nchat'),(89,'','',7,'nchat'),(90,'hello','<p>hello</p>',7,'nchat'),(91,'rgefdx','<p>gfdsgf</p><p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat'),(92,'gfsddf','<p>fdshsdfh</p>',7,'nchat'),(93,'','',7,'nchat'),(94,'','',7,'nchat'),(95,'','',147,'nchat'),(96,'','',147,'nchat'),(98,'','',230,'nchat');
/*!40000 ALTER TABLE `mailroom_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailroom_messagehistory`
--

DROP TABLE IF EXISTS `mailroom_messagehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mailroom_messagehistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(256) NOT NULL,
  `recipients` longtext NOT NULL,
  `message_text` longtext NOT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `status` int NOT NULL,
  `send_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailroom_messagehistory`
--

LOCK TABLES `mailroom_messagehistory` WRITE;
/*!40000 ALTER TABLE `mailroom_messagehistory` DISABLE KEYS */;
INSERT INTO `mailroom_messagehistory` VALUES (3,'allo!','[\'booksmart@savoirvire.fr\']','<p>allo!</p>',7,'nchat',1,'2019-10-10 02:11:33.269714'),(4,'Work!','[\'booksmart@savoirvire.fr, arubaito@machtfrei.de\']','<p>Work!</p>',7,'nchat',1,'2019-10-10 02:11:33.269714'),(6,'good night!','[\'bonsoiree@greetings.com\']','<p>good night!</p>',7,'nchat',1,'2019-10-10 02:11:33.269714'),(8,'ahoy mate!','[\'chaz@b.com\']','<p>ahoy!</p>',7,'nchat',0,'2019-10-10 02:11:33.269714'),(12,'dsailufg','[\'hy\']','<p>dsfsagdgsd</p>',7,'nchat',0,'2019-10-10 06:21:04.295171'),(13,'dsailufg','[\'hy\']','<p>sgdfa</p>',7,'nchat',0,'2019-10-10 06:22:11.626032'),(14,'this is a test','[\'h\']','<p>testing</p>',7,'nchat',0,'2019-10-10 06:23:41.300161'),(15,'this is a test','[\'h\']','<p>fixed?</p>',7,'mailroom',0,'2019-10-10 06:24:34.888163'),(16,'dsg','[\'ghddd\']','<p>sgfgsr</p>',7,'nchat',0,'2019-10-10 08:57:48.102768'),(17,'good times','[\'entered\', [\'unentered\']]','<p>these are</p>',7,'nchat',0,'2019-10-10 09:11:59.666952'),(18,'boo','[\'enter\', \'the\', \'dragon\']','<p>hello</p>',7,'nchat',0,'2019-10-10 09:16:35.739544'),(19,'I\'m Pickle Rick!','[\'test@you.com\', \'chaz303@yahoo.com\']','<p><img src=\"https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/froala/pickle_rick.jpg\" style=\"width: 180px;\" class=\"fr-fic fr-dib\"></p>',7,'nchat',0,'2019-10-11 02:02:49.119338'),(20,'Mr. Poopybutthole Proposed!','[\'\', \'test@you.com\']','<p><img src=\"https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/vendor_branch_1/froala/Mr._Poopybutthole_Proposing.jpg\" style=\"width: 740px;\" class=\"fr-fic fr-dib\"></p>',7,'nchat',0,'2019-10-11 05:58:12.001072'),(21,'sdkfj','[\'chaz303@yahoo.com\', \'\']','<p>dfkjsdlrjk</p>',7,'nchat',0,'2019-10-15 04:25:39.835255'),(22,'hello','[\'\', \'c.wilson@peacefactory.co.jp\']','<p>hello&nbsp;</p>',7,'nchat',0,'2019-10-15 06:29:39.550834'),(23,'one recipient','[\'c.wilson@peacefactory.co.jp\']','<p>one&nbsp;</p>',7,'nchat',0,'2019-10-15 06:43:46.449398'),(24,'one more recipient','[\'c.wilson@peacefactory.co.jp\']','<p>&nbsp;sdffaf</p>',7,'nchat',0,'2019-10-15 06:44:07.453860'),(25,'hgjv','[\'chaz303@yahoo.com\', \'ym\']','<p>ghfsk</p><p><br></p>',7,'nchat',0,'2019-10-15 06:45:15.724335'),(26,'idhf','[\'ch\']','<p>dhk</p>',7,'nchat',0,'2019-10-15 06:54:02.441489'),(27,'dkf','[\'fdjh\']','<p>kdlsjd</p>',7,'nchat',0,'2019-10-15 07:52:57.091734'),(28,'dfadf','[\'fdf\']','<p>edfsdf</p>',7,'nchat',0,'2019-10-15 08:04:52.464878'),(29,'ddd','[\'gfsg\']','<p>dsdsfafd</p>',7,'nchat',0,'2019-10-15 08:21:16.259735'),(30,'asdfjlhfo;ashdf','[\'fsfd\']','<p>fsjlshaf;djh</p>',7,'nchat',0,'2019-10-15 08:39:51.808200'),(31,'sdfawdf','[\'test@you.com\']','<p>dsgfsdg</p>',7,'nchat',0,'2019-10-15 09:00:10.973145'),(32,'sdfawdf','[\'ch\', \'dfjd\', \'dfh\']','<p>fsdaasdf</p>',7,'nchat',0,'2019-10-15 09:00:31.902260'),(33,'sdfawdf','[\'fsfd\']','',7,'nchat',0,'2019-10-15 09:02:39.073924'),(34,'dbdb','[\'fdsfd\']','<p>&nbsp;</p>',7,'nchat',0,'2019-10-15 09:38:43.942803'),(35,'dbdb','[\'fdsfd\']','<p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>',7,'nchat',0,'2019-10-15 09:39:52.338967'),(36,'first send_mass_mail test','[\'boo\']','<p>hey</p>',7,'nchat',0,'2019-10-16 01:26:54.206838'),(37,'first send_mass_mail test','[\'real@address.com\']','<p>fjdjf</p>',7,'nchat',0,'2019-10-16 01:29:32.562817'),(38,'dbdb','[\'dshfkh\']','<p>kdsjfdkj</p>',7,'nchat',0,'2019-10-16 01:30:38.268577'),(39,'sdfj','[\'real@address.com\']','<p>dsf</p>',7,'nchat',0,'2019-10-16 01:31:24.533631'),(40,'sdfawdf','[\'test@you.com\', \'notyou@test.com\']','<p>hi</p>',7,'nchat',0,'2019-10-16 01:32:53.774477'),(41,'sdfawdf','[\'test@you.com\', \'notyou@test.com\', \'test\']','<p>jdsk</p>',7,'nchat',0,'2019-10-16 01:33:50.826604'),(42,'sdfawdf','[\'test@you.com\', \'m@m.com\']','<p>i need a message</p>',7,'nchat',0,'2019-10-16 01:35:17.138800'),(43,'sdfawdf','[\'m@m.com\', \'test\']','<p>i need a message</p>',7,'nchat',0,'2019-10-16 01:36:15.740852'),(44,'sdfawdf','[\'this@this.com\', \'y@o.com\']','<p>i need a message</p>',7,'nchat',0,'2019-10-16 01:38:15.032089'),(45,'test','[\'test@you.com\', \'booksmart@savoirvire.fr\']','<p>test</p>',7,'nchat',0,'2019-10-16 01:41:06.235138'),(46,'hi','[\'test@you.com\']','<p>hi</p><p><br></p>',7,'nchat',0,'2019-10-16 01:44:45.663990'),(47,'double','[\'hi\', \'y@o.com\']','<p>trouble</p>',7,'nchat',0,'2019-10-16 01:45:49.472555'),(48,'hello, there','[\'t\', \'test@you.com\']','<p>this is a message</p>',7,'nchat',0,'2019-10-16 01:47:41.693789'),(49,'hello','[\'this@you.com\', \'y@o.com\']','<p>how are you?</p>',7,'nchat',0,'2019-10-16 01:55:09.248972'),(50,'fdsaf','[\'chaz303@yahoo.com\']','<p>sfdg fhsdl ewhrh q &nbsp;qwqhewa w chaz303@yahoo.com</p>',7,'nchat',0,'2019-10-17 03:13:36.623137'),(51,'print(\"this is type: \", type(email_recipients))','[\'chaz303@yahoo.comhdh\']','<pre>print(&quot;this is type: &quot;, type(email_recipients))</pre>',7,'nchat',0,'2019-10-17 03:14:59.958911'),(52,'sdff chaz303@yahoo.com sfhq e weowi','[\'chaz303@yahoo.com\']','<p>aerwsgsvd</p>',7,'nchat',0,'2019-10-17 06:34:31.681750'),(53,'sdff chaz303@yahoo.com sfhq e weowi','[\'chaz303@yahoo.com\']','<p>sdff <a href=\"mailto:chaz303@yahoo.com\">chaz303@yahoo.com</a> sfhq e weowi</p>',7,'nchat',0,'2019-10-17 06:34:43.664994'),(54,'sdff chaz303@yahoo.com sfhq e weowi','[\'long@message.com\']','<p>yNGKBDlWt9nIDjYnWtf5OVdUBboRfGuFhNmXZj8meCp07gExFg3vL52KuGelwVDfzs7R1ugLbqWj2zSRDPLDIjk25ecy5QWZ0nxm6Essf43pCn3j1nl7MKn4t9oZrDG8pCRLCVtMRdxBkExlKeBotZGT31kbDT0QieiTeMuY3Yk6a0vEpIMrgStssMfI52za1PL77BdyraUuzQqtLDsPm6Pvk974nK7jHFqsiuZj2s7CZMdnXoX0SNPzJOz9dVkfJXYG47vsak47tQgjVR3xm56rFUDwlpKkfIC4wJOQowNLCD1OHOYw4wd15FbiHvZMh194coEL6QGfsxzSNyAZ10gsqHrvJIYLWDUb8Wg6r7gtkLP3xsrw2goambbzl3O3svUYeZANHFilGL6Hp0B328WriyTPrPN0nQ5X1UqXg9zfuFTiIOaBJ9OLHvnj4Du4Fyja1Yst2HUAJfv6Po5SIGgtW83lnYlxAaiaT3leoQlraHD8ojNxchqqqlul53Nd7zkFB1DMoPnMkNhg8vTCLwjOIIOq52kbFxeSp2mvH37q6Bxz6Z08D9ws3YN5PjWsvfiirzpi7p4hdyKFj6beX7KYnYQevqb6AiKMGhmXSChZllp8LfcDcM6d0UiFPXu950l5hI2fZB0cjKjHP43p77UA6iI2z31G4DYq8hCZTnYAd7Il6ViKlhK7abu6eYUCTw2pQEGjpdu7D7zC6RYsBnkTaWsslHtvtT7bSMjC5yuEgHYtk9vNpCHwi0GKZkrxUZtj1EDl2uWnCpIqVBR6VfXPNnRBGst32jYn2v2MOq3VAkWIbusFsu45VOhES6dnm4ovhfWPHMFr81gfm2l364CQdTflFgWrGtKGHtJwCHWyK9D5o8QYDtFjpyEFotcGsoX6yCp3ItkUHIMRTT6ba6eCOO691WBXX3aSALOz1oVlFlkaNxzpHcwuLM4uEaXNjEAnX8ja7K2T89bH9tL9r7DsIVZfG1zSyCxDifPpo2eDt5qnC66nakgHtqqH6DDCEBgjmN8TXEaX3IrslW1IzjNTTEW6PLWX8WrOhl0l8bsBYG6gmMeUM2mSQLCzVwuog3bUrMd6yyAqkqJgdQ70NCyRxjJdT23O7j3J7EWj6eGepIYI5cowvwLeGTVIbNaZSE2tWLm0NVFJ9vtHsM14Vd5V1e0ntDtZk7sxYeC1gfSDPAc9XXpJ5B3IN0e7xRoVzZfl2Y3YzTOy6qpWulHkfoe1uqd8PSOjnSQGgZkohtosbYvzpeOpdjCT4khnheic3fpL0CeyN5PTkYJ1MNWQ6KvtjaZCCYHzqlMmXoulr1qHU3Aih2fF3hj4ekzgJv2FbrLSVwecZ6w4napLamqYc6yiUDDWtM6SDIwpzQlMDrj9D6y0s1MlKCfCy16QRfqsm8btKaydrbzooZBWUANMFFOhtxfIolESg2Retbq4Toke2tzEi5M7yxEnMmGIqsTaPQtMSCiv5ziPvWgjlrHB7TtnCn5d6DcaraZ5NER8HoMYxUHISvPUSqJkrNvZMgAHI2GMjGIyjybxHkIYHDn9OA87ze9PifNrpVdBuokZCf4kcJzOvA7btjpNd0S6eYB8eU6GtaUKhNh4ByWPz1jEmZ4BSDHZdQKWEVR0r41Ns9xMOrLDX6fPdGpJ8Lji7J2G8V1oiLC4EcQrpKVzY5XSol8Q2YGZdDVWy9IJtifgoBLF6FUJO8xJRqjapKOxSM52rbd6qjmopZPpIuh5rrCzDsRTPUwjgskiglHngKt2rJpSgerEImX0fvSml79ZVEZUqokNu7qLmfpQ6B4JcELoT2VW50H7YpYEOtZ7rADcSbyo8I2SisBVfrELzGhbIVqEtc8yswDWKpBWEUiI4GRe4vyEcXzvYsx0ujr6YxMy6pFwWpGPM3FSyxPX4LYf9etGASV9cAjt9TW3oB5RGT7yKjx9tumLtJITzn0dXv2cgSy9n2gPTpswSOriRHNH93CAeMnj6NzCrtvPSu1GgXd3GzdoWLaDyYCKajAU2cUUKXQHj4iOe8IrDBCb8DczUeLItayGcqMBX7sY5oQVa28p3ZW5Y8Rp5Wq1rvcpRMZKmyFkyeqMs8gYURLzUYA7pqiKZBgEraYrqRdS89c8S9mVMxIXvHtB0AtympJUQ50rHZ11iSt59lf2kWU8HscanJJ9794NZYEntZ930o4pm6I6AUl7OSYcfri2MXHxWQIkh5nk7R0IwsiFzk9skv2NUnPRdybz2avLTfVIYOZjt8Twygmqj3fE9GpRbFU1zmDtXAZrl6RhIdlQLDZQX0GFbysfLxQfPr0GE1tENGyGHZYm574kxWnvm6wbw9jX08DtQjRS34AoH2drS64kEjK1g1DcIH66t84zPg9E0f7fhAzi3OBcRle5q6pjNkpOSOee3CsBG6Fodgj1SsD6PCpnYy9VgxiWV1JSNlJDpH5meAWUxIhM9IB6hhcxHdEaMDR4CtNcDEKHSaap0ieL8IJJogxQX3StM0zk3Ta88wP23ork5dX2LB290Du2Szpq1J3RdqIHX6nWs798OsB8K8XWvuMehkLN2uC6olz0AQ9cmB2V30bh84yA3DDcrfc7lKG8JY6ZRwsqKIe0AXMlpA7cSff4UEBHDZZn1sGFmz5vPiPq2485dNLIpHUaODz0TP2S47Q0NWpXzWlecUXm8j36qJanogWjdYkImcioinMqI26FYVJGjrXLNDr8e59c8YIdlNAMAYkB2s8g0XgLMVXWC3G8BcyVccTmQ7UuJ1vcc0VuOXJvS3JhvRLUnfYxp48UaIFDUBsYtKAGLqhbACE6EQv0Zv7nADjaU6dPrN70CUvy4RUlw7MzlUlNVcu0dYFsLv2O7W8yy32C5MB8GDbKFdNCfSxQMnkxncwTWhVe2TYc9pHyt2USoCd3DpEGGRsF9A7d4hbhwofJrxFRg5ZTP2WmczQtHdX4nZJlnW0YqxLBzybADQNyHFBtB9d7D8i3KAnIxOP2TsVGPil1hKLhkDgCHLVriB8dbYJTdIxDlNneoMFFB5ixtiibirHAiWM72XZm5FmQjw3sMyzzIkCa11eie2bPEw9LeVllg5kBwimAC5xJkoKDaSp7CZTUuJwIMb9jmDXx5P3IGgr3dFI1a6ufvIeQAhOVbxhEexJmFnwbXzoVjTpUXpIK1K98TRsf3Alp7R1DgrNkgjEG11hXD1KybSgPW0EW1arCPVHCJzgOO5FCp8xCEr9ZLzQYiOopbDjCyBGGBvTWzAIPzOLHzlI5GNOb3hya84s2XCnAwNhiv2g8srQvnKC9N8tlC4s39jMAUx05eI6IjTXJa3De8U6PkIF9Eww9x3zlYjPacA3pQOBFkxWN7R5Mz11qXbxZ8k0Bj87J0FyAptQwjxiALtQWlG0jKng8gkWWR9HrHn8PftXn2Nku4uNogsZv5GCju1jBhXkCB9RDmEsr2iMSDSUScC2VEOpE1RMY1bexVvjkNDl4nM9GjM8zVRVVOTo8xbDq5KgJSSIB51WnpVKJCxdlTx4Jxjk4F8JkYZNCvdSZNq7zyiJ5ECWS4aupRFRV7ZO7bEmVIV1gtOLXwJQGHlqSmY8zzNRaJSnEfC43rclelJMiJvZUS9nkhG02B445YM6Sth0Tw7lVJHsxotrJIWwcR8Wnv7vQwz0Eo912NRnxhzFvu5uIVsRcDYT3qiaF9Qopzqlub7GGxGmEzn8EA1eGORzEtpy9Q3DGfz1nuIA3FeWo6uBTy6XAgjaLF3YHqDbo85WGUqUGDTJgxsgXUOYgQoKm5Mw0NF9WrT8zuWEntYW6yRpR6Em6CbuaMEBsNYmvaO9W2jDUg9yfF6yf06XNzX5rURMRRWQVDZOtCQB82n00LU7aw3aR2fBkVKweBZ21kIxOz9hIUKiqGfvbifVY2q0iiwMEubRUVACzIIx9mlZKhObMDQLVbifaoOTSKar3sgIbxjayhX7ERREwPG2Nadtce1mxIqwnWbuh9d6RGyxUAWy0DyKtyiDCkQjJGHy7koFatRaeDOmT6BFYAdPHma0IaILvz60FxFz1WgCr4nRnY4k39TDlxix1d2FJqyBRvWAQx0Ecr1bd3FTpIu14m9UUPNUvpXNTqRdyYZk10dtgbbz4HZKZR6kmi8wUYshbOeEsi9cYbAdJFRruIZk3KmRpsvxfW3Tvhw0bxdehGlXvNUDUQLgHr5M7wzDpRD728WUnxdqtco4ehHyOCkIvPg9FGSiDIztF9nqg43pu1E8yZc2qxNfex07NaWzwrgmcYRMf0AK3Ew7qdFqZtIkmr3y1yABs0rfAJyAIp4UVNtNnu9sfN250tgTn3eACgW374pxnVuSbsjO08tcwW6lgrb68vaKBDCSsabfbPampltXMFeeQtdM8jD7IHPJHpmgo9YyOvCeSewF3saddxZktNEVas1DId2jkZ0Qtr9QJYUUe4XPBjtMFCNgtpP2uh2Y9P7S11AmncMVRGr7jBNIloEnYPegRGUc1IfBTCy8LxQEoQRp3cLPc4FHBPdrar7ZpFzn3bq1sekfP2t8HW5yZmxv4Ms5vXtnpNK6oSUnPLq5phFmr9L8aEhyvIijpZcjAo5mrgitFx0buimQKwwO5ghM5aH74drKqKf85rHoGWhk15N6hM4oCSGruw0roZJoNZC3y9Q3vDykyCw5OFyqX27ZYB6nhupKnCfOsGTYJA6Lq5GTgS9VDyHUnnP12Q8u0XqetvUmMF2Sgxj8kzh0rDfMMbCuniFa0fJksHJIxWtA6XxuhL7HA5qk6Pu7s6WDjqgrnQD9pLyVrSxTQ3tRL4I4PP7YzmoUkjSBH2TQdNLyzb0TJr3t9xUZazudrfh1EXHHsdOdTtrwv6HcbDIKdTN59YPcFEkS3XAqnqdUc7Nd73cMD5fS2PUfopYB5veqQ5KOvcDDAecXEPKOBVODtkDjk20Pi2x2jywdPPxjLM2EvGTqxfo8vLuIkSBiZAU7EOhZMsWzIXgwCPoAXjiyxUrJTN78pVkRasRDVabRWkv7c0rDrY3EZZhr1sYLaxMQVZfccUv4YgUm9VNVCcqyrEFQaTHmAXslNmVyM3fpfFaoOYZf97aS3Spt85ZyGGKgW77g4Hs0ssi0KvvreJFSk46tDGBWH2ulZV56poZAGC8sbs0TfRsys5U7zjOiCi9xVh2dMEPsYcTGzcvC7Bcx4bzrXA9kVou1k69LaHgmWTeUJXnjuUpCipOzbHNGsIWtCKBbucYZFIasPgEvibFELF08OgOe9atPi9znV8uZVnXPNYXp1fmMAMMIXOqrqOysHgauGpvR9nFOnv6eZwSlTupWJc3TNB1J7NJatDxAeh9czPZhHadAuTXDeJ0Otxad5Z5bELi9MUhBtaPuJBH1mzKlMCbCnxdLwcQPjOXUDPT8VfFy5uIU4FCF7AZb0IMytP9Tct1GG42Tn1DoDZ0zllat4w3Ildc9EBBuAwaumWq04kyfNWIWBbXooXwIhTlgaz66cySLjf2cthZs6zWIW76TzYRD76iIu9ht3NHSGs1Awcb6by6pbLc4z4N8TTEBFtu7YGQ3bsMmqG2bGngdIEGfowNeJOSlfgAA5J7li4S4cCRqyDYQXi8hNTrEXYhuzasoNNeBnLvDalv56lndn6BhA8jhO2yzaj4TvDHdRqo8TdsoW61kpl0CkJTNJ3MbtmRBlB8SdUAKTqw9vtK4WFGrzsKzTXrJtMVByFP5tNvSD2FFLK8yQnCQCXcNJmzsOKI8wMzQBXNgUrNJXQrUNKjbeqTOQ8KoqarLC5aba7ct2mZcrkadh45OlB2TnTOJhm2sGKlXuo6bwC06T7viG7TTMF2dsWva3Ylc5XVuitbGY7W3wWx5wZ1wgjEc6YyC9A2r6WDKrZiIOE9dRTl4TvCxQVHNzLtl59eYRVb1jTO2rEZyMIQ7aUxap9nJbr6ooGiNNr1Kh8UAL5oNxhCw9fOkSdIUq6NzT18iW00oGvvOqjUvpmtnV0ZIOHPUHouSB0TJhhRt8ump91Ma5T7ETpaOjPUTThwWBSQgGQxv8DV8nunjTmB62n00mbqJqfuW8rlSJnG9UZwdoZVZH6JzEapDVIgqD8yrjNk0UETLQHK6l4SN4LFCMvscMvf6vqPAesj1ncYCF4tljZLteCzQOwSh3di9p1GPxgipy5ZPTBfdjB4AaSNwIzIkncN5Cln2TT016iKAK1GHuwxlAdPQqtqCTgFV81mEDBnJ9JGFaQaDh9MZeWozo7ifSQFKjWIJc8J2JYzO3eBA6c3cRYfF2V6zBtpEZsheMBbS1QTxB2wAZTROItRRZl6XDJNbaFr2JbvswLLuBxssEpEuVYufUTspbcea4f6kKArgMlNX60RbEvALG3mcleDxfFvYwZABVHwoHcYt14GTTyQntmMw9YV3xC8Kyqta9naxB1cqixeSiEQbxZ1dlKiEny9SKrkbpFi0ZnXDQLXphO0EovJpkixANbkt2Jl0rhWJgZVrUhMV2Iz7WI8zJjy3m0QiahlxZT6s5OmjJSS1q7fCHk0fkXzfTdr3fI5QjbzXSsVmzAaBhIN5DvRW1MOyxt2bq7ZaPiDL4q3Q7bqyP0fH5Qq37Vd1cA7xjsvzbIWiB8IDx36uwzMhy20j6aMH9vIB9C5ybRqkAr3O41qYufzYLks8jbQtL3bojSxwgQGb0R64FNFX3tlnldIgkXHBi7fTaAPxyRlukFGndlhB3Z94vtKTr5Bh5MKp6uY008pJ67mjwlvNNyNzoUXOKICkEhm3wOxNOHizm8CjmDdLZvh01o2XdhciLeYjbh3J3w4JaBbSNuEWER08epN6fEyj8XIvovgtvY6alUpruO35VJQEsQ4nnud6iOFaCbdpH5Sznmju3AiB0kLWyrSItGuJlTJ2hXCHWRakzQ1cgSKLSS7CgCrCetjnuq48sg4MLERJ09ryGZy09B3q5ricOku8kUaUwnjY3rTnwvcbuoJOg7FwPeoC4hGXEg2ZXcfFzj5ZengjVKqvbVbXcU10ccv0rHcnk2qURolO5qu5BMPil8oilF0t8HXx85N9f8IwnzKzFNtnAORDQn03FSa3VPAkAjgL0eHrCtmxi9ftfuTmzL5Fe2wdzKSzSyrjNvZx8Um7RyCtdFR4M3zx7VNS4knKCktnyGQTd7Lb5Ct3oLn1O4sDfVHvVdPzEDHz4IeFgCs33A1ukOXNhHMBDAbqgM8oIGsZu28eLQSOW5Jqp7zsTDutdiLCPL0RBP0ChY4Cbdw3s9gsmEm0cTkm1bMZpfpX7G2fgFshnrdxoptbPuT5MI0IcsMPqNdZDVasmHlvQLWy8DOpOg9hTQShDr2UU4WRfKNvGZrbZ3hGBPTXzdWQy6vqXVmpqj8NuEnQusKVcVqwO3AUEHCOlAsXUvJ1LxnFagapo5bbIb7lC7bdHqJaa7dlhEF7xhfePiBcastKk7WcMCjPiXcZPkTzFrOqJDD0fsSpXhIiu3MHmXgkRJVitKp9AzB6di8loMOkfGKK4fcTs4JnM2bnuLS9DjRDCcp1miHMOc6MqoXuFJNCIyYLHYS6r6v0423zPdsNBuN2wj9q67gzk2oduPOwkLCUo237zWuySDvYwMbscMaOO450JX1o4F9zuPjkAOZWU1uyDOUjTxb2S60KDKLE47ZUXCVbXxaSUz6K2JVSlplMKjk6VRzKyPirltB5fwAR2HRIFr0MRKnGvHQCGzDQK3OZwQSoi4bmGXziAvIElkoMkPq15LnMT6hvRVNFwAvuIoDfYYnoegsyJy19zRJwQPs7jDSIXxG2gFFPkCVZgfuXRRCgDkFrmv9X7vot7mLapkWWqHKgWaoMlgfRMFYyJyh95tTVoRLZqwVHvGHYkvVr176wKEupvtLc0OmrSt33KGkzU1WzO8M8XDbq2bEfSdvpw4WLwTs4zsroI2BsyeMGRzkDnXS6O7V4kCGy9bYklqdmVOd8fgt14Dc7HsVLwTwdgT0WUsm0n0edx0nCZu</p>',7,'nchat',0,'2019-10-17 06:38:04.930496'),(55,'sakfjd','[\'dsjfak@hd.com\']','<p>sladjf</p>',7,'nchat',0,'2019-10-17 08:45:43.681790'),(56,'boob','[\'glad@yahoo.com\']','<p>boob</p>',7,'nchat',0,'2019-10-17 09:03:56.822479'),(57,'ghost','[\'chaz303@yahoo.com\']','<p>ghost</p>',7,'nchat',0,'2019-10-17 09:06:09.055402'),(58,'this','[\'chaz@a.bo\']','<p>this</p>',7,'nchat',0,'2019-10-18 01:24:10.140862'),(59,'this','[\'chaz@a.bo\', \'chaz303@yahoo.com\']','<p>this</p>',7,'nchat',0,'2019-10-18 01:24:58.041155'),(60,'this','[\'chaz@a.bo\', \'chaz303@yahoo.com\']','<p>this</p>',7,'nchat',0,'2019-10-18 03:49:56.820304'),(61,'this','[\'chaz@a.bo\']','<p>this</p>',7,'nchat',0,'2019-10-18 03:50:34.292083'),(62,'this','[\'chaz@a.bo.com\']','<p>this</p>',7,'nchat',0,'2019-10-18 08:17:17.675958'),(64,'testing','[\'chaz303@yahoo.com\']','<p>testing</p><p><br></p><p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat',0,'2019-11-08 07:22:57.474119'),(65,'test','[\'chaz303@yahoo.com\']','<p>test</p><p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat',0,'2019-11-11 04:46:11.577255'),(66,'test2','[\'chaz303@yahoo.com\']','<p>test2</p><p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat',0,'2019-11-11 04:50:00.602877'),(67,'test','[\'chaz303@yahoo.com\']','<p>test</p><p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat',0,'2019-11-11 05:00:22.745602'),(68,'ghost','[\'chaz303@yahoo.com\']','<p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat',0,'2019-11-11 07:32:45.500120'),(69,'airhead','[\'chaz303@yahoo.com\']','<p>hello</p><p data-f-id=\"pbf\" style=\"text-align: center; font-size: 14px; margin-top: 30px; opacity: 0.65; font-family: sans-serif;\">Powered by <a href=\"https://www.froala.com/wysiwyg-editor?pb=1\" title=\"Froala Editor\">Froala Editor</a></p>',147,'nchat',0,'2019-11-11 07:37:07.901306'),(70,'should be in history','[\'test@test.com\']','<p>hello</p>',7,'nchat',0,'2019-11-11 07:42:00.059677'),(71,'dghsd','[\'hghdsh@a.com\']','<p>sdhgsdgh</p>',7,'nchat',0,'2019-11-12 04:25:16.705666');
/*!40000 ALTER TABLE `mailroom_messagehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailroom_messagetemplate`
--

DROP TABLE IF EXISTS `mailroom_messagetemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mailroom_messagetemplate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `message_id` int NOT NULL,
  `template_category_id` int NOT NULL,
  `language_code` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mailroom_messagetemp_message_id_0ce079e6_fk_mailroom_` (`message_id`),
  KEY `mailroom_messagetemp_template_category_id_4506cf32_fk_mailroom_` (`template_category_id`),
  CONSTRAINT `mailroom_messagetemp_message_id_0ce079e6_fk_mailroom_` FOREIGN KEY (`message_id`) REFERENCES `mailroom_message` (`id`),
  CONSTRAINT `mailroom_messagetemp_template_category_id_4506cf32_fk_mailroom_` FOREIGN KEY (`template_category_id`) REFERENCES `mailroom_messagetemplatecategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailroom_messagetemplate`
--

LOCK TABLES `mailroom_messagetemplate` WRITE;
/*!40000 ALTER TABLE `mailroom_messagetemplate` DISABLE KEYS */;
INSERT INTO `mailroom_messagetemplate` VALUES (1,'foo template',49,1,'en'),(2,'bar template',50,2,'en'),(3,'two bar',50,2,'en'),(4,'to wong foo',49,1,'en'),(5,'three foo',49,1,'en');
/*!40000 ALTER TABLE `mailroom_messagetemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailroom_messagetemplatecategory`
--

DROP TABLE IF EXISTS `mailroom_messagetemplatecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mailroom_messagetemplatecategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `language_code` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailroom_messagetemplatecategory`
--

LOCK TABLES `mailroom_messagetemplatecategory` WRITE;
/*!40000 ALTER TABLE `mailroom_messagetemplatecategory` DISABLE KEYS */;
INSERT INTO `mailroom_messagetemplatecategory` VALUES (1,'foo','en'),(2,'bar','en');
/*!40000 ALTER TABLE `mailroom_messagetemplatecategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_bot`
--

DROP TABLE IF EXISTS `messageflow_bot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_bot` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `regist_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_bot`
--

LOCK TABLES `messageflow_bot` WRITE;
/*!40000 ALTER TABLE `messageflow_bot` DISABLE KEYS */;
INSERT INTO `messageflow_bot` VALUES (1,'Chaz Bot',0,907896,'nchat','1970-01-10 00:00:00.000000'),(2,'PDP Bot',0,147,'nchat','1971-01-01 00:00:00.000000'),(3,'Active Bot',0,147,'nchat','1971-01-01 00:00:00.000000'),(4,'Inactive Bot',0,147,'nchat','1980-01-01 00:00:00.000000'),(5,'line bot 1',0,147,'nchat','2019-11-14 01:54:19.503832'),(6,'test1',0,7,'nchat','2019-11-29 08:40:40.618438'),(7,'Test',0,7,'nchat','2019-12-02 03:22:42.784924'),(8,'Fun Bot',1,7,'nchat','2019-12-02 05:12:07.558262'),(9,'nullbot',0,7,'nchat','2019-12-05 08:26:52.509192'),(10,'dfaf',0,180,'nchat','2019-12-11 03:37:44.685082'),(11,'Hello',0,192,'nchat','2019-12-11 08:51:55.976321'),(12,'Stained Glass Bot',1,192,'nchat','2019-12-12 03:48:33.536080'),(13,'first bot',0,202,'nchat','2019-12-13 03:09:12.969417'),(14,'Bot 2',0,202,'nchat','2019-12-13 03:37:02.262914'),(15,'Bot1',0,222,'nchat','2019-12-16 03:17:39.408567'),(16,'Bot1',0,223,'nchat','2019-12-16 03:22:00.952004'),(17,'Bot1',0,224,'nchat','2019-12-16 03:23:39.900319'),(18,'Bot1',0,225,'nchat','2019-12-16 03:25:18.151394'),(19,'Bot1',0,226,'nchat','2019-12-16 03:26:27.380104'),(20,'Bot1',0,227,'nchat','2019-12-16 03:28:15.446665'),(21,'Bot1',0,228,'nchat','2019-12-16 03:34:21.594528'),(22,'Bot1',0,229,'nchat','2019-12-16 03:35:46.302258'),(24,'No back and forth',1,230,'nchat','2019-12-17 02:39:24.281013');
/*!40000 ALTER TABLE `messageflow_bot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_botscenario`
--

DROP TABLE IF EXISTS `messageflow_botscenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_botscenario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `weight` int unsigned NOT NULL,
  `bot_id` int NOT NULL,
  `scenario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messageflow_botscenario_bot_id_51087cdd_fk_messageflow_bot_id` (`bot_id`),
  KEY `messageflow_botscena_scenario_id_3a5ac117_fk_messagefl` (`scenario_id`),
  CONSTRAINT `messageflow_botscena_scenario_id_3a5ac117_fk_messagefl` FOREIGN KEY (`scenario_id`) REFERENCES `messageflow_scenario` (`id`),
  CONSTRAINT `messageflow_botscenario_bot_id_51087cdd_fk_messageflow_bot_id` FOREIGN KEY (`bot_id`) REFERENCES `messageflow_bot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_botscenario`
--

LOCK TABLES `messageflow_botscenario` WRITE;
/*!40000 ALTER TABLE `messageflow_botscenario` DISABLE KEYS */;
INSERT INTO `messageflow_botscenario` VALUES (8,100,6,12),(9,100,7,13),(10,100,8,14),(11,100,10,22),(12,100,12,31),(13,100,13,32),(14,100,14,32),(15,100,18,37),(16,100,19,38),(17,100,20,39),(18,100,21,40),(19,100,22,41),(29,100,24,42);
/*!40000 ALTER TABLE `messageflow_botscenario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_enduser`
--

DROP TABLE IF EXISTS `messageflow_enduser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_enduser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(64) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `tel` varchar(32) DEFAULT NULL,
  `attribute_json` longtext,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `last_login_dt` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `subscribed` tinyint(1) NOT NULL,
  `auth_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `messageflow_enduser_auth_user_id_88cc4236_fk_auth_user_id` (`auth_user_id`),
  CONSTRAINT `messageflow_enduser_auth_user_id_88cc4236_fk_auth_user_id` FOREIGN KEY (`auth_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_enduser`
--

LOCK TABLES `messageflow_enduser` WRITE;
/*!40000 ALTER TABLE `messageflow_enduser` DISABLE KEYS */;
INSERT INTO `messageflow_enduser` VALUES (18,'','Chaz Wilson','Male',NULL,'sdfakjdhf',NULL,'{\"line_user_id\": \"U2b4e9711cf674a1f3108125d31c46ed6\", \"picture_url\": \"https://profile.line-scdn.net/0ha91mH9ybPhYMFBLG3DBBQTBRMHt7OjhedHEkcX5EYSQoJyoVMyYjcSBEMnEjIX0TNidyc3odNS51\", \"line_postback_payload\": \"None\"}',7,'nchat',NULL,'2019-12-02 02:45:49.248015','2019-12-04 08:49:05.524125',0,1,168),(19,'','Chaz Wilson',NULL,NULL,'',NULL,'{\"line_user_id\": \"U2b4e9711cf674a1f3108125d31c46ed6\", \"picture_url\": \"https://profile.line-scdn.net/0ha91mH9ybPhYMFBLG3DBBQTBRMHt7OjhedHEkcX5EYSQoJyoVMyYjcSBEMnEjIX0TNidyc3odNS51\"}',7,'nchat',NULL,'2019-12-03 02:12:25.044393','2019-12-03 02:12:25.095792',0,1,169),(48,'','Chaz Wilson',NULL,NULL,'',NULL,'{\"line_user_id\": \"U2b4e9711cf674a1f3108125d31c46ed6\", \"picture_url\": \"https://profile.line-scdn.net/0ha91mH9ybPhYMFBLG3DBBQTBRMHt7OjhedHEkcX5EYSQoJyoVMyYjcSBEMnEjIX0TNidyc3odNS51\", \"line_postback_payload\": \"None\"}',202,'nchat',NULL,'2019-12-13 07:03:31.998669','2019-12-13 09:06:23.192915',0,1,220),(49,'','Chaz Wilson',NULL,NULL,'',NULL,'{\"line_user_id\": \"U2b4e9711cf674a1f3108125d31c46ed6\", \"picture_url\": \"https://profile.line-scdn.net/0ha91mH9ybPhYMFBLG3DBBQTBRMHt7OjhedHEkcX5EYSQoJyoVMyYjcSBEMnEjIX0TNidyc3odNS51\", \"line_postback_payload\": \"None\"}',230,'nchat',NULL,'2019-12-16 04:35:08.680334','2019-12-16 04:40:04.878044',0,1,231);
/*!40000 ALTER TABLE `messageflow_enduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_enduserbotscenario`
--

DROP TABLE IF EXISTS `messageflow_enduserbotscenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_enduserbotscenario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `regist_dt` datetime(6) NOT NULL,
  `bot_id` int NOT NULL,
  `current_message_id` int DEFAULT NULL,
  `scenario_id` int NOT NULL,
  `state` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messageflow_enduserb_bot_id_6fd57974_fk_messagefl` (`bot_id`),
  KEY `messageflow_enduserb_current_message_id_338d873c_fk_messagefl` (`current_message_id`),
  KEY `messageflow_enduserb_scenario_id_25b949c7_fk_messagefl` (`scenario_id`),
  CONSTRAINT `messageflow_enduserb_bot_id_6fd57974_fk_messagefl` FOREIGN KEY (`bot_id`) REFERENCES `messageflow_bot` (`id`),
  CONSTRAINT `messageflow_enduserb_current_message_id_338d873c_fk_messagefl` FOREIGN KEY (`current_message_id`) REFERENCES `messageflow_message` (`id`),
  CONSTRAINT `messageflow_enduserb_scenario_id_25b949c7_fk_messagefl` FOREIGN KEY (`scenario_id`) REFERENCES `messageflow_scenario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_enduserbotscenario`
--

LOCK TABLES `messageflow_enduserbotscenario` WRITE;
/*!40000 ALTER TABLE `messageflow_enduserbotscenario` DISABLE KEYS */;
INSERT INTO `messageflow_enduserbotscenario` VALUES (7,17,7,'nchat','2019-12-02 02:45:49.312800',6,4,12,'WAITING'),(8,17,7,'nchat','2019-12-02 02:45:49.312800',6,1,13,'INITIAL'),(9,17,7,'nchat','2019-12-02 02:45:49.312800',8,24,14,'WAITING'),(10,19,7,'nchat','2019-12-03 02:12:25.107042',8,24,14,'WAITING'),(11,18,7,'nchat','2019-12-03 03:12:45.338675',8,24,14,'INITIAL'),(12,30,192,'nchat','2019-12-12 09:14:55.647176',12,31,31,'WAITING'),(13,31,202,'nchat','2019-12-13 03:40:30.302486',13,33,32,'INITIAL'),(14,32,202,'nchat','2019-12-13 04:19:48.407523',13,33,32,'INITIAL'),(15,33,202,'nchat','2019-12-13 04:38:48.048008',13,33,32,'INITIAL'),(16,34,202,'nchat','2019-12-13 04:41:52.147533',13,33,32,'INITIAL'),(17,35,202,'nchat','2019-12-13 04:43:08.834114',13,33,32,'INITIAL'),(18,36,202,'nchat','2019-12-13 04:49:06.087266',13,33,32,'INITIAL'),(19,37,202,'nchat','2019-12-13 04:55:17.399074',13,33,32,'INITIAL'),(20,38,202,'nchat','2019-12-13 04:56:54.479483',13,33,32,'INITIAL'),(21,39,202,'nchat','2019-12-13 05:03:22.676813',13,34,32,'WAITING'),(22,40,202,'nchat','2019-12-13 05:04:59.073723',13,34,32,'WAITING'),(23,41,202,'nchat','2019-12-13 05:09:22.462047',13,34,32,'WAITING'),(24,42,202,'nchat','2019-12-13 05:22:28.836818',13,34,32,'WAITING'),(25,43,202,'nchat','2019-12-13 06:28:31.481259',13,34,32,'WAITING'),(26,44,202,'nchat','2019-12-13 06:37:58.710011',13,34,32,'WAITING'),(27,45,202,'nchat','2019-12-13 06:40:43.727745',13,34,32,'WAITING'),(28,46,202,'nchat','2019-12-13 06:43:32.601175',13,34,32,'WAITING'),(29,47,202,'nchat','2019-12-13 06:58:55.985043',13,34,32,'WAITING'),(30,48,202,'nchat','2019-12-13 07:03:32.073447',13,34,32,'WAITING');
/*!40000 ALTER TABLE `messageflow_enduserbotscenario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_logline`
--

DROP TABLE IF EXISTS `messageflow_logline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_logline` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` longtext,
  `user_id` int NOT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `is_user_message` tinyint(1) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `end_user_bot_scenario_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `messageflow_logline_end_user_bot_scenari_2e6abadc_fk_messagefl` (`end_user_bot_scenario_id`),
  CONSTRAINT `messageflow_logline_end_user_bot_scenari_2e6abadc_fk_messagefl` FOREIGN KEY (`end_user_bot_scenario_id`) REFERENCES `messageflow_enduserbotscenario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=718 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_logline`
--

LOCK TABLES `messageflow_logline` WRITE;
/*!40000 ALTER TABLE `messageflow_logline` DISABLE KEYS */;
INSERT INTO `messageflow_logline` VALUES (434,'H',17,7,'nchat',1,'2019-12-02 03:42:42.795375',7),(435,'test message 2',17,7,'nchat',0,'2019-12-02 03:42:42.802209',7),(436,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist.jpeg',17,7,'nchat',0,'2019-12-02 03:42:42.978920',7),(437,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg',17,7,'nchat',0,'2019-12-02 03:42:43.165848',7),(438,'this is an option message',17,7,'nchat',0,'2019-12-02 03:42:43.289183',7),(439,'H\n',17,7,'nchat',1,'2019-12-02 03:43:52.455989',7),(440,'Y',17,7,'nchat',1,'2019-12-02 03:44:35.833533',7),(441,'H',17,7,'nchat',1,'2019-12-02 03:44:49.451427',7),(442,'Hi',17,7,'nchat',1,'2019-12-02 03:51:49.832777',7),(443,'test message 2',17,7,'nchat',0,'2019-12-02 03:51:49.840031',7),(444,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist.jpeg',17,7,'nchat',0,'2019-12-02 03:51:49.928615',7),(445,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg',17,7,'nchat',0,'2019-12-02 03:51:50.015174',7),(446,'this is an option message',17,7,'nchat',0,'2019-12-02 03:51:50.097983',7),(447,' Hi',17,7,'nchat',1,'2019-12-02 05:13:23.585026',7),(448,'H',17,7,'nchat',1,'2019-12-02 05:16:43.989793',7),(449,'Hi',17,7,'nchat',1,'2019-12-02 05:17:35.864461',7),(450,'Hi',17,7,'nchat',1,'2019-12-02 05:20:22.022562',7),(451,'H',17,7,'nchat',1,'2019-12-02 05:25:39.936314',7),(452,'H',17,7,'nchat',1,'2019-12-02 05:26:04.803844',7),(453,'I\n',17,7,'nchat',1,'2019-12-02 05:42:25.368011',9),(454,'test message 2',17,7,'nchat',0,'2019-12-02 05:42:25.377357',9),(455,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist.jpeg',17,7,'nchat',0,'2019-12-02 05:42:25.476758',9),(456,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg',17,7,'nchat',0,'2019-12-02 05:42:25.587695',9),(457,'this is an option message',17,7,'nchat',0,'2019-12-02 05:42:25.699101',9),(458,'Hi',17,7,'nchat',1,'2019-12-02 05:55:01.005137',9),(459,'this is an option message',17,7,'nchat',0,'2019-12-02 05:55:03.559911',9),(460,'this is an option message',17,7,'nchat',0,'2019-12-02 05:55:04.831095',9),(461,'this is an option message',17,7,'nchat',0,'2019-12-02 05:55:06.748906',9),(462,'this is an option message',17,7,'nchat',0,'2019-12-02 05:55:08.079876',9),(463,'this is an option message',17,7,'nchat',0,'2019-12-02 05:55:09.422022',9),(464,'G',17,7,'nchat',1,'2019-12-02 05:58:14.895725',9),(465,'test message 2',17,7,'nchat',0,'2019-12-02 05:58:14.912299',9),(466,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist.jpeg',17,7,'nchat',0,'2019-12-02 05:58:16.079519',9),(467,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg',17,7,'nchat',0,'2019-12-02 05:58:17.205440',9),(468,'this is an option message',17,7,'nchat',0,'2019-12-02 05:58:18.381324',9),(469,'G',17,7,'nchat',1,'2019-12-02 05:58:20.600848',9),(470,'H',17,7,'nchat',1,'2019-12-02 06:02:22.492231',9),(471,'test message 2',17,7,'nchat',0,'2019-12-02 06:02:22.507279',9),(472,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist.jpeg',17,7,'nchat',0,'2019-12-02 06:02:22.611779',9),(473,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg',17,7,'nchat',0,'2019-12-02 06:02:22.726870',9),(474,'this is an option message',17,7,'nchat',0,'2019-12-02 06:02:22.863363',9),(475,'H',17,7,'nchat',1,'2019-12-02 06:06:52.845617',9),(476,'Woo!',17,7,'nchat',0,'2019-12-02 06:06:52.860848',9),(477,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:06:58.905596',9),(478,'Woo!',17,7,'nchat',0,'2019-12-02 06:06:59.001802',9),(479,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:07:00.259806',9),(480,'Woo!',17,7,'nchat',0,'2019-12-02 06:07:00.350370',9),(481,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:07:27.598589',9),(482,'Woo!',17,7,'nchat',0,'2019-12-02 06:07:27.693577',9),(483,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:08:01.316723',9),(484,'Woo!',17,7,'nchat',0,'2019-12-02 06:08:01.527845',9),(485,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:12:23.669322',9),(486,'Woo!',17,7,'nchat',0,'2019-12-02 06:12:23.763675',9),(487,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:12:51.044140',9),(488,'Woo!',17,7,'nchat',0,'2019-12-02 06:12:51.156260',9),(489,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:16:17.859172',9),(490,'Woo!',17,7,'nchat',0,'2019-12-02 06:16:17.985067',9),(491,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:18:29.187762',9),(492,'Woo!',17,7,'nchat',0,'2019-12-02 06:18:29.305548',9),(493,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:18:30.333855',9),(494,'Woo!',17,7,'nchat',0,'2019-12-02 06:18:30.422256',9),(495,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:18:31.666698',9),(496,'Woo!',17,7,'nchat',0,'2019-12-02 06:18:31.752201',9),(497,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:19:08.809958',9),(498,'Woo!',17,7,'nchat',0,'2019-12-02 06:19:08.937492',9),(499,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:22:19.644141',9),(500,'Woo!',17,7,'nchat',0,'2019-12-02 06:22:19.716567',9),(501,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:31:52.167191',9),(502,'Woo!',17,7,'nchat',0,'2019-12-02 06:31:52.258666',9),(503,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:36:59.828035',9),(504,'Woo!',17,7,'nchat',0,'2019-12-02 06:36:59.947189',9),(505,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:37:14.705128',9),(506,'Woo!',17,7,'nchat',0,'2019-12-02 06:37:14.802634',9),(507,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:38:58.108728',9),(508,'Woo!',17,7,'nchat',0,'2019-12-02 06:38:58.247609',9),(509,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:43:04.539351',9),(510,'Woo!',17,7,'nchat',0,'2019-12-02 06:43:04.636808',9),(511,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:45:57.525868',9),(512,'Woo!',17,7,'nchat',0,'2019-12-02 06:45:57.629148',9),(513,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:47:36.896153',9),(514,'Woo!',17,7,'nchat',0,'2019-12-02 06:47:37.018039',9),(515,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:48:30.205892',9),(516,'Woo!',17,7,'nchat',0,'2019-12-02 06:48:30.319899',9),(517,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:48:53.221948',9),(518,'Woo!',17,7,'nchat',0,'2019-12-02 06:48:53.314107',9),(519,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:49:24.842229',9),(520,'Woo!',17,7,'nchat',0,'2019-12-02 06:49:24.959792',9),(521,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:49:51.517057',9),(522,'Woo!',17,7,'nchat',0,'2019-12-02 06:49:51.608972',9),(523,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:49:57.419995',9),(524,'Woo!',17,7,'nchat',0,'2019-12-02 06:49:57.540465',9),(525,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:51:44.410921',9),(526,'Woo!',17,7,'nchat',0,'2019-12-02 06:51:44.505933',9),(527,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:52:08.458720',9),(528,'Woo!',17,7,'nchat',0,'2019-12-02 06:52:08.582263',9),(529,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:53:46.045821',9),(530,'Woo!',17,7,'nchat',0,'2019-12-02 06:53:46.144890',9),(531,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:54:16.988294',9),(532,'Woo!',17,7,'nchat',0,'2019-12-02 06:54:17.108740',9),(533,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:55:13.427611',9),(534,'Woo!',17,7,'nchat',0,'2019-12-02 06:55:13.613372',9),(535,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:58:07.550200',9),(536,'Woo!',17,7,'nchat',0,'2019-12-02 06:58:07.673578',9),(537,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 06:58:57.365488',9),(538,'Woo!',17,7,'nchat',0,'2019-12-02 06:58:57.459406',9),(539,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 07:24:27.447810',9),(540,'Woo!',17,7,'nchat',0,'2019-12-02 07:24:27.542811',9),(541,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 07:26:48.731546',9),(542,'Woo!',17,7,'nchat',0,'2019-12-02 07:26:48.820864',9),(543,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 07:29:56.288599',9),(544,'Woo!',17,7,'nchat',0,'2019-12-02 07:29:56.384166',9),(545,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 07:39:21.052849',9),(546,'Woo!',17,7,'nchat',0,'2019-12-02 07:39:21.161342',9),(547,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:13:50.818241',9),(548,'Woo!',17,7,'nchat',0,'2019-12-02 08:13:50.913093',9),(549,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:17:11.459050',9),(550,'Woo!',17,7,'nchat',0,'2019-12-02 08:17:11.587337',9),(551,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:30:30.977962',9),(552,'Woo!',17,7,'nchat',0,'2019-12-02 08:30:31.075182',9),(553,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:31:06.174267',9),(554,'Woo!',17,7,'nchat',0,'2019-12-02 08:31:06.269545',9),(555,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:31:47.854389',9),(556,'Woo!',17,7,'nchat',0,'2019-12-02 08:31:47.954143',9),(557,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:32:21.071514',9),(558,'Woo!',17,7,'nchat',0,'2019-12-02 08:32:21.181246',9),(559,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:32:42.536375',9),(560,'Woo!',17,7,'nchat',0,'2019-12-02 08:32:42.630918',9),(561,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:34:02.618034',9),(562,'Woo!',17,7,'nchat',0,'2019-12-02 08:34:02.719024',9),(563,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:44:09.470511',9),(564,'Woo!',17,7,'nchat',0,'2019-12-02 08:44:09.623578',9),(565,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:46:40.799912',9),(566,'Woo!',17,7,'nchat',0,'2019-12-02 08:46:40.899087',9),(567,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:51:46.864107',9),(568,'Woo!',17,7,'nchat',0,'2019-12-02 08:51:46.987032',9),(569,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:53:44.367059',9),(570,'Woo!',17,7,'nchat',0,'2019-12-02 08:53:44.464439',9),(571,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:55:25.718908',9),(572,'Woo!',17,7,'nchat',0,'2019-12-02 08:55:25.827298',9),(573,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 08:55:44.327070',9),(574,'Woo!',17,7,'nchat',0,'2019-12-02 08:55:44.427695',9),(575,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:01:01.050908',9),(576,'Woo!',17,7,'nchat',0,'2019-12-02 09:01:01.209405',9),(577,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:01:25.319212',9),(578,'Woo!',17,7,'nchat',0,'2019-12-02 09:01:25.426623',9),(579,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:05:12.867194',9),(580,'Woo!',17,7,'nchat',0,'2019-12-02 09:05:13.027353',9),(581,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:05:43.727117',9),(582,'Woo!',17,7,'nchat',0,'2019-12-02 09:05:43.832775',9),(583,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:06:21.475618',9),(584,'Woo!',17,7,'nchat',0,'2019-12-02 09:06:21.575815',9),(585,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:07:35.253363',9),(586,'Woo!',17,7,'nchat',0,'2019-12-02 09:07:35.362565',9),(587,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:08:03.060041',9),(588,'Woo!',17,7,'nchat',0,'2019-12-02 09:08:03.286072',9),(589,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:08:22.985197',9),(590,'Woo!',17,7,'nchat',0,'2019-12-02 09:08:23.082822',9),(591,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:09:30.490210',9),(592,'Woo!',17,7,'nchat',0,'2019-12-02 09:09:30.598724',9),(593,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-02 09:10:34.408434',9),(594,'Woo!',17,7,'nchat',0,'2019-12-02 09:10:34.517294',9),(595,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',17,7,'nchat',0,'2019-12-03 01:38:40.000647',9),(596,'Woo!',17,7,'nchat',0,'2019-12-03 01:38:40.123871',9),(597,'this is a text message',19,7,'nchat',0,'2019-12-03 02:12:25.110207',10),(598,'Woo!',19,7,'nchat',0,'2019-12-03 02:12:25.204278',10),(599,'this is a text message',18,7,'nchat',0,'2019-12-03 03:12:45.342073',11),(600,'Woo!',18,7,'nchat',0,'2019-12-03 03:12:45.456939',11),(601,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/afro_panda_school_girl.png',18,7,'nchat',0,'2019-12-03 03:12:55.941039',11),(602,'this is a text message',18,7,'nchat',0,'2019-12-03 03:12:56.129534',11),(603,'Woo!',18,7,'nchat',0,'2019-12-03 03:12:56.277996',11),(604,'this is a text message',18,7,'nchat',0,'2019-12-03 04:48:29.077045',11),(605,'Woo!',18,7,'nchat',0,'2019-12-03 04:48:29.165514',11),(606,'this is a text message',18,7,'nchat',0,'2019-12-03 04:48:30.004743',11),(607,'Woo!',18,7,'nchat',0,'2019-12-03 04:48:30.085431',11),(608,'this is a text message',18,7,'nchat',0,'2019-12-03 06:06:47.587103',11),(609,'Woo!',18,7,'nchat',0,'2019-12-03 06:06:47.687945',11),(610,'this is a text message',18,7,'nchat',0,'2019-12-03 06:06:48.641878',11),(611,'Woo!',18,7,'nchat',0,'2019-12-03 06:06:48.743964',11),(612,'this is a text message',18,7,'nchat',0,'2019-12-03 06:06:48.929373',11),(613,'Woo!',18,7,'nchat',0,'2019-12-03 06:06:49.025767',11),(614,'this is a text message',18,7,'nchat',0,'2019-12-03 06:06:49.206166',11),(615,'Woo!',18,7,'nchat',0,'2019-12-03 06:06:49.302948',11),(616,'this is a text message',18,7,'nchat',0,'2019-12-03 06:08:57.168268',11),(617,'Woo!',18,7,'nchat',0,'2019-12-03 06:08:57.253118',11),(618,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/grinning_afro_panda.jpg',18,7,'nchat',0,'2019-12-03 06:09:42.422041',11),(619,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/DiscoAfroPanda.jpg',18,7,'nchat',0,'2019-12-03 06:09:42.515605',11),(620,'Woo!',18,7,'nchat',0,'2019-12-03 06:09:42.621781',11),(621,'Hey',18,7,'nchat',1,'2019-12-04 08:48:58.441054',11),(622,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/grinning_afro_panda.jpg',18,7,'nchat',0,'2019-12-04 08:49:05.545515',11),(623,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/DiscoAfroPanda.jpg',18,7,'nchat',0,'2019-12-04 08:49:05.683934',11),(624,'Woo!',18,7,'nchat',0,'2019-12-04 08:49:05.774766',11),(625,'Yo',30,192,'nchat',1,'2019-12-12 09:14:55.656830',12),(626,'go to the start',30,192,'nchat',0,'2019-12-12 09:14:55.671494',12),(627,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/192/stained-glass-51982.jpg',30,192,'nchat',0,'2019-12-12 09:15:14.998958',12),(628,'go to the start',30,192,'nchat',0,'2019-12-12 09:15:15.103235',12),(629,'Hi',31,202,'nchat',1,'2019-12-13 03:40:30.304639',13),(630,'text2',31,202,'nchat',0,'2019-12-13 03:40:30.307935',13),(631,'Hi',32,202,'nchat',1,'2019-12-13 04:19:48.414842',14),(632,'text2',32,202,'nchat',0,'2019-12-13 04:19:48.426960',14),(633,'H',32,202,'nchat',1,'2019-12-13 04:28:06.547366',14),(634,'text2',32,202,'nchat',0,'2019-12-13 04:28:06.558152',14),(635,'H',32,202,'nchat',1,'2019-12-13 04:28:23.565794',14),(636,'H',32,202,'nchat',1,'2019-12-13 04:29:10.880003',14),(637,'I',33,202,'nchat',1,'2019-12-13 04:38:48.050288',15),(638,'text2',33,202,'nchat',0,'2019-12-13 04:38:48.056149',15),(639,'J',33,202,'nchat',1,'2019-12-13 04:39:49.553473',15),(640,'K',33,202,'nchat',1,'2019-12-13 04:40:03.320912',15),(641,'L',33,202,'nchat',1,'2019-12-13 04:40:32.493072',15),(642,'M',34,202,'nchat',1,'2019-12-13 04:41:52.150456',16),(643,'text2',34,202,'nchat',0,'2019-12-13 04:41:52.153268',16),(644,'N',35,202,'nchat',1,'2019-12-13 04:43:08.836519',17),(645,'text2',35,202,'nchat',0,'2019-12-13 04:43:08.842234',17),(646,'H',36,202,'nchat',1,'2019-12-13 04:49:06.090212',18),(647,'text2',36,202,'nchat',0,'2019-12-13 04:49:06.093274',18),(648,'I',37,202,'nchat',1,'2019-12-13 04:55:17.401590',19),(649,'text2',37,202,'nchat',0,'2019-12-13 04:55:17.407333',19),(650,'J',38,202,'nchat',1,'2019-12-13 04:56:54.480919',20),(651,'text2',38,202,'nchat',0,'2019-12-13 04:56:54.485697',20),(652,'K',39,202,'nchat',1,'2019-12-13 05:03:22.678891',21),(653,'text2',39,202,'nchat',0,'2019-12-13 05:03:22.684146',21),(654,'Go to start!',39,202,'nchat',0,'2019-12-13 05:03:22.836974',21),(655,'text1',39,202,'nchat',0,'2019-12-13 05:04:28.296528',21),(656,'text2',39,202,'nchat',0,'2019-12-13 05:04:28.393303',21),(657,'Go to start!',39,202,'nchat',0,'2019-12-13 05:04:28.500847',21),(658,'L',40,202,'nchat',1,'2019-12-13 05:04:59.075456',22),(659,'text2',40,202,'nchat',0,'2019-12-13 05:04:59.080940',22),(660,'Go to start!',40,202,'nchat',0,'2019-12-13 05:04:59.194726',22),(661,'Y',41,202,'nchat',1,'2019-12-13 05:09:22.464113',23),(662,'text2',41,202,'nchat',0,'2019-12-13 05:09:22.467286',23),(663,'Go to start!',41,202,'nchat',0,'2019-12-13 05:09:22.557009',23),(664,'text2',42,202,'nchat',0,'2019-12-13 05:22:28.844677',24),(665,'Go to start!',42,202,'nchat',0,'2019-12-13 05:22:28.955842',24),(666,'text1',42,202,'nchat',0,'2019-12-13 05:22:29.542405',24),(667,'text2',42,202,'nchat',0,'2019-12-13 05:22:29.644600',24),(668,'Go to start!',42,202,'nchat',0,'2019-12-13 05:22:29.774186',24),(669,'Hi',43,202,'nchat',1,'2019-12-13 06:28:31.486724',25),(670,'text2',43,202,'nchat',0,'2019-12-13 06:28:31.489934',25),(671,'Go to start!',43,202,'nchat',0,'2019-12-13 06:28:31.596693',25),(672,'Hi',43,202,'nchat',1,'2019-12-13 06:28:35.960224',25),(673,'M',44,202,'nchat',1,'2019-12-13 06:37:58.711458',26),(674,'text2',44,202,'nchat',0,'2019-12-13 06:37:58.714389',26),(675,'Go to start!',44,202,'nchat',0,'2019-12-13 06:37:58.813017',26),(676,'N',45,202,'nchat',1,'2019-12-13 06:40:43.729328',27),(677,'text2',45,202,'nchat',0,'2019-12-13 06:40:43.736686',27),(678,'Go to start!',45,202,'nchat',0,'2019-12-13 06:40:43.825162',27),(679,'I',46,202,'nchat',1,'2019-12-13 06:43:32.603576',28),(680,'text1',46,202,'nchat',0,'2019-12-13 06:43:32.609208',28),(681,'text2',46,202,'nchat',0,'2019-12-13 06:43:32.829129',28),(682,'Go to start!',46,202,'nchat',0,'2019-12-13 06:43:33.178037',28),(683,'text1',46,202,'nchat',0,'2019-12-13 06:43:59.344940',28),(684,'text2',46,202,'nchat',0,'2019-12-13 06:43:59.435029',28),(685,'Go to start!',46,202,'nchat',0,'2019-12-13 06:43:59.525286',28),(686,'Hi',47,202,'nchat',1,'2019-12-13 06:58:55.986639',29),(687,'text1',47,202,'nchat',0,'2019-12-13 06:58:55.989458',29),(688,'text2',47,202,'nchat',0,'2019-12-13 06:58:56.085123',29),(689,'Go to start!',47,202,'nchat',0,'2019-12-13 06:58:56.188419',29),(690,'text1',47,202,'nchat',0,'2019-12-13 06:59:04.273085',29),(691,'text2',47,202,'nchat',0,'2019-12-13 06:59:04.362359',29),(692,'Go to start!',47,202,'nchat',0,'2019-12-13 06:59:04.451730',29),(693,'Hi',48,202,'nchat',1,'2019-12-13 07:03:32.079738',30),(694,'text1',48,202,'nchat',0,'2019-12-13 07:03:32.092139',30),(695,'text2',48,202,'nchat',0,'2019-12-13 07:03:32.200934',30),(696,'Go to start!',48,202,'nchat',0,'2019-12-13 07:03:32.307142',30),(697,'text1',48,202,'nchat',0,'2019-12-13 07:03:35.536831',30),(698,'text2',48,202,'nchat',0,'2019-12-13 07:03:35.828932',30),(699,'Go to start!',48,202,'nchat',0,'2019-12-13 07:03:36.004515',30),(700,'text1',48,202,'nchat',0,'2019-12-13 07:03:44.245387',30),(701,'text2',48,202,'nchat',0,'2019-12-13 07:03:44.367758',30),(702,'Go to start!',48,202,'nchat',0,'2019-12-13 07:03:44.459718',30),(703,'text1',48,202,'nchat',0,'2019-12-13 07:06:17.472824',30),(704,'text2',48,202,'nchat',0,'2019-12-13 07:06:17.577193',30),(705,'Go to start!',48,202,'nchat',0,'2019-12-13 07:06:17.683824',30),(706,'text1',48,202,'nchat',0,'2019-12-13 09:06:23.206587',30),(707,'Go to start!',48,202,'nchat',0,'2019-12-13 09:06:23.307993',30),(708,'Yo',49,230,'nchat',1,'2019-12-16 04:35:08.770020',NULL),(709,'howdie ho!',49,230,'nchat',0,'2019-12-16 04:35:08.779318',NULL),(710,'repeat',49,230,'nchat',0,'2019-12-16 04:35:08.909673',NULL),(711,'Hi',49,230,'nchat',1,'2019-12-16 04:38:15.702649',NULL),(712,'howdie ho!',49,230,'nchat',0,'2019-12-16 04:38:25.002894',NULL),(713,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/230/file_icon.png',49,230,'nchat',0,'2019-12-16 04:38:25.170680',NULL),(714,'repeat',49,230,'nchat',0,'2019-12-16 04:38:25.341456',NULL),(715,'howdie ho!',49,230,'nchat',0,'2019-12-16 04:40:04.891647',NULL),(716,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/230/afropanda.jpg',49,230,'nchat',0,'2019-12-16 04:40:04.988847',NULL),(717,'repeat',49,230,'nchat',0,'2019-12-16 04:40:05.092094',NULL);
/*!40000 ALTER TABLE `messageflow_logline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_message`
--

DROP TABLE IF EXISTS `messageflow_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `json_content` longtext,
  `options` varchar(2048) DEFAULT NULL,
  `display_order` int DEFAULT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `message_block_id` int NOT NULL,
  `type_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messageflow_message_message_block_id_5288a2eb_fk_messagefl` (`message_block_id`),
  KEY `messageflow_message_type_id_c2fce034_fk_messagefl` (`type_id`),
  CONSTRAINT `messageflow_message_message_block_id_5288a2eb_fk_messagefl` FOREIGN KEY (`message_block_id`) REFERENCES `messageflow_messageblock` (`id`),
  CONSTRAINT `messageflow_message_type_id_c2fce034_fk_messagefl` FOREIGN KEY (`type_id`) REFERENCES `messageflow_messagetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_message`
--

LOCK TABLES `messageflow_message` WRITE;
/*!40000 ALTER TABLE `messageflow_message` DISABLE KEYS */;
INSERT INTO `messageflow_message` VALUES (1,'Welcome to Line test bot.','None',0,147,'nchat','2019-11-14 01:54:50.344812','2019-11-28 09:46:38.325243',25,1),(2,'test message 2','None',1,147,'nchat','2019-11-14 03:40:42.938510','2019-11-28 09:46:38.326076',25,1),(4,'this is an option message','[{\'title\': \'option 1\', \'payload\': \'continue\'}, {\'title\': \'restart\', \'payload\': \'25\'}, {\'title\': \'tell me a joke!\', \'payload\': \'27\'}]',4,147,'nchat','2019-11-14 04:50:00.295120','2019-11-28 09:46:38.328599',25,2),(6,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist.jpeg','None',2,147,'nchat','2019-11-15 03:21:03.979369','2019-11-28 09:46:38.326894',25,3),(7,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg','None',5,147,'nchat','2019-11-15 03:21:48.609118','2019-11-28 09:46:38.329445',25,3),(9,'Knock, knock','[{\'title\': \"Who\'s there?\", \'payload\': \'continue\'}, {\'title\': \'Fuck off\', \'payload\': \'25\'}]',0,147,'nchat','2019-11-15 07:05:22.037911','2019-11-21 02:22:10.175565',27,2),(10,'Boo.','[{\'title\': \'Boo, who?\', \'payload\': \'continue\'}, {\'title\': \'Fuck off.\', \'payload\': \'25\'}]',1,147,'nchat','2019-11-15 07:06:39.573376','2019-11-21 02:22:10.176613',27,2),(11,'Why are you crying?','None',2,147,'nchat','2019-11-15 07:06:39.574343','2019-11-21 02:22:10.177538',27,1),(12,'Want to hear it again?','[{\'title\': \'YES!\', \'payload\': \'27\'}]',3,147,'nchat','2019-11-15 07:20:25.922616','2019-11-21 02:22:10.178399',27,2),(13,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/afro_panda_comb.jpg','None',6,147,'nchat','2019-11-28 01:25:19.387508','2019-11-28 09:46:38.330225',25,4),(14,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/this_person_does_not_exist_2.jpeg','None',3,147,'nchat','2019-11-28 02:08:15.533089','2019-11-28 09:46:38.327683',25,4),(21,'Hello.','None',0,7,'nchat','2019-12-02 03:23:36.602191','2019-12-02 03:37:28.290908',41,1),(22,'hug','None',0,7,'nchat','2019-12-02 04:10:50.627675','2019-12-02 04:10:50.627730',39,1),(24,'Woo!','[{\'title\': \'Go to Beginning\', \'payload\': \'42\'}]',2,7,'nchat','2019-12-02 05:12:57.454299','2019-12-03 06:09:32.544701',42,2),(27,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/grinning_afro_panda.jpg','None',0,7,'nchat','2019-12-03 06:09:32.547449','2019-12-03 06:09:32.547538',42,3),(28,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/7/DiscoAfroPanda.jpg','None',1,7,'nchat','2019-12-03 06:09:32.549187','2019-12-03 06:09:32.549268',42,4),(29,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/192/stained-glass-51982.jpg','None',0,192,'nchat','2019-12-12 03:47:39.223041','2019-12-12 03:47:39.223136',67,3),(30,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/192/stained-glass-51982.jpg','None',0,192,'nchat','2019-12-12 03:48:55.169520','2019-12-12 09:02:11.803804',68,3),(31,'go to the start','[{\'title\': \'go!\', \'payload\': \'68\'}]',1,192,'nchat','2019-12-12 09:02:11.807495','2019-12-12 09:02:11.807552',68,2),(33,'text1','None',0,202,'nchat','2019-12-13 03:39:58.549818','2019-12-13 09:05:46.379525',69,1),(34,'Go to start!','[{\'title\': \'back to start\', \'payload\': \'69\'}]',1,202,'nchat','2019-12-13 05:03:12.857885','2019-12-13 09:05:46.381510',69,2),(35,'howdie ho!','None',0,230,'nchat','2019-12-16 04:34:39.936041','2019-12-16 04:39:52.911202',73,1),(36,'repeat','[{\'title\': \'repeat\', \'payload\': \'73\'}]',2,230,'nchat','2019-12-16 04:34:39.943637','2019-12-16 04:39:52.914407',73,2),(38,'https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/230/afropanda.jpg','None',1,230,'nchat','2019-12-16 04:39:07.493516','2019-12-16 04:39:52.913392',73,3),(39,'test','None',0,230,'nchat','2019-12-17 02:09:22.032724','2019-12-17 02:09:22.032793',75,1);
/*!40000 ALTER TABLE `messageflow_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_messageblock`
--

DROP TABLE IF EXISTS `messageflow_messageblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_messageblock` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `display_order` int DEFAULT NULL,
  `regist_dt` datetime(6) NOT NULL,
  `scenario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messageflow_messageb_scenario_id_c586deeb_fk_messagefl` (`scenario_id`),
  CONSTRAINT `messageflow_messageb_scenario_id_c586deeb_fk_messagefl` FOREIGN KEY (`scenario_id`) REFERENCES `messageflow_scenario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_messageblock`
--

LOCK TABLES `messageflow_messageblock` WRITE;
/*!40000 ALTER TABLE `messageflow_messageblock` DISABLE KEYS */;
INSERT INTO `messageflow_messageblock` VALUES (1,'',1,'2019-11-08 01:39:40.932455',4),(2,'',1,'2019-11-08 02:02:34.218023',4),(13,'',2,'2019-11-08 03:45:04.458486',4),(14,'',3,'2019-11-08 04:56:22.511408',4),(15,'',4,'2019-11-08 06:38:27.653194',4),(16,'',5,'2019-11-08 06:49:12.944431',4),(17,'',1,'2019-11-08 07:11:36.893568',5),(18,'',1,'2019-11-08 07:11:42.450077',5),(19,'',0,'2019-11-08 08:39:41.495466',3),(20,'',1,'2019-11-08 08:39:47.879479',3),(21,'',1,'2019-11-08 08:41:30.886898',6),(22,'',1,'2019-11-08 09:33:58.262430',7),(23,'',1,'2019-11-08 09:40:29.528054',7),(24,'',2,'2019-11-08 09:44:00.253045',7),(25,'Home',0,'2019-11-11 01:30:22.539075',8),(26,'',1,'2019-11-14 04:49:04.723862',9),(27,'Joke',1,'2019-11-14 09:20:04.287018',8),(28,'',2,'2019-11-15 07:06:46.134591',8),(29,'',3,'2019-11-15 07:18:28.743369',8),(30,'',1,'2019-11-20 04:59:19.010585',10),(31,'',4,'2019-11-21 06:57:32.223562',8),(32,'',5,'2019-11-21 07:00:01.803607',8),(33,'',6,'2019-11-21 07:00:04.319946',8),(34,'',-1,'2019-11-21 07:55:56.957221',11),(37,'',7,'2019-11-26 06:39:01.292518',8),(38,'',1,'2019-11-29 08:40:42.357739',4),(39,'',1,'2019-11-29 08:40:49.974463',12),(40,'',2,'2019-12-02 03:20:48.413324',12),(41,'',1,'2019-12-02 03:23:05.502066',13),(42,'',1,'2019-12-02 05:12:10.884550',14),(43,'',1,'2019-12-05 05:40:50.035585',17),(44,'',1,'2019-12-05 05:45:25.343662',18),(45,'',1,'2019-12-05 05:45:45.186868',19),(46,'',1,'2019-12-05 05:45:47.282416',19),(47,'',1,'2019-12-05 08:27:07.623583',20),(48,'',2,'2019-12-06 08:23:54.703866',12),(49,'',1,'2019-12-06 10:11:50.870638',21),(50,'',1,'2019-12-06 10:12:00.882637',21),(51,'',1,'2019-12-11 03:37:46.720690',22),(52,'',1,'2019-12-11 03:37:55.309265',22),(53,'',2,'2019-12-11 03:43:01.857235',22),(54,'',1,'2019-12-11 06:20:52.677761',23),(55,'',1,'2019-12-11 06:51:19.917288',24),(56,'',1,'2019-12-11 06:51:33.657774',24),(57,'',2,'2019-12-11 06:53:05.819845',24),(58,'',1,'2019-12-11 08:51:40.142685',25),(59,'',1,'2019-12-11 08:53:47.347979',26),(60,'',1,'2019-12-11 08:58:49.834930',26),(61,'',1,'2019-12-12 01:19:35.350572',27),(62,'',1,'2019-12-12 01:29:26.921060',27),(63,'',2,'2019-12-12 01:38:10.197217',27),(64,'',1,'2019-12-12 01:45:37.523361',28),(65,'',1,'2019-12-12 02:31:19.819336',28),(66,'',1,'2019-12-12 03:46:37.981040',29),(67,'',1,'2019-12-12 03:47:23.105616',30),(68,'',1,'2019-12-12 03:48:37.928519',31),(69,'',1,'2019-12-13 03:07:44.965264',32),(70,'',1,'2019-12-13 03:39:29.110220',32),(71,'',1,'2019-12-13 08:18:24.240786',33),(72,'',1,'2019-12-13 08:19:18.460991',33),(73,'',0,'2019-12-16 04:31:56.010156',42),(74,'',1,'2019-12-17 02:08:44.885563',43),(75,'',1,'2019-12-17 02:09:05.152659',44),(76,'',1,'2019-12-17 02:09:08.060194',44);
/*!40000 ALTER TABLE `messageflow_messageblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_messagetype`
--

DROP TABLE IF EXISTS `messageflow_messagetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_messagetype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_messagetype`
--

LOCK TABLES `messageflow_messagetype` WRITE;
/*!40000 ALTER TABLE `messageflow_messagetype` DISABLE KEYS */;
INSERT INTO `messageflow_messagetype` VALUES (1,'text',NULL,NULL),(2,'option',NULL,NULL),(3,'image',NULL,NULL),(4,'file',NULL,NULL);
/*!40000 ALTER TABLE `messageflow_messagetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_scenario`
--

DROP TABLE IF EXISTS `messageflow_scenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_scenario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `regist_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_scenario`
--

LOCK TABLES `messageflow_scenario` WRITE;
/*!40000 ALTER TABLE `messageflow_scenario` DISABLE KEYS */;
INSERT INTO `messageflow_scenario` VALUES (1,'fun',147,'nchat','1980-09-06 00:00:00.000000'),(2,'time',147,'nchat','1990-01-01 00:00:00.000000'),(3,'scenario three',147,'nchat','1991-01-01 00:00:00.000000'),(4,'new',147,'nchat','2019-11-08 01:39:40.890002'),(5,'new',147,'nchat','2019-11-08 07:11:36.849410'),(6,'new',147,'nchat','2019-11-08 08:41:30.884001'),(7,'new',147,'nchat','2019-11-08 09:33:58.219260'),(8,'new',147,'nchat','2019-11-11 01:30:22.512072'),(9,'new',7,'nchat','2019-11-14 04:49:04.706054'),(10,'new',147,'nchat','2019-11-20 04:59:18.968093'),(11,' ',-1,'nchat','2019-11-20 04:59:18.968093'),(12,'new plan test',7,'nchat','2019-11-29 08:40:42.326318'),(13,'December 2nd Scenario',7,'nchat','2019-12-02 03:23:05.500267'),(14,'fun bot 1',7,'nchat','2019-12-02 05:12:10.841541'),(16,'',-1,'nchat','2019-12-05 04:19:38.064165'),(17,'new',7,'nchat','2019-12-05 05:40:49.987306'),(18,'new',7,'nchat','2019-12-05 05:45:25.298636'),(19,'new',7,'nchat','2019-12-05 05:45:45.183530'),(20,'new',7,'nchat','2019-12-05 08:27:07.581844'),(21,'new',7,'nchat','2019-12-06 10:11:50.825389'),(22,'new',180,'nchat','2019-12-11 03:37:46.674042'),(23,'new',191,'nchat','2019-12-11 06:20:52.588335'),(24,'new',191,'nchat','2019-12-11 06:51:19.867075'),(25,'new',192,'nchat','2019-12-11 08:51:40.096512'),(26,'new',192,'nchat','2019-12-11 08:53:47.300766'),(27,'new',192,'nchat','2019-12-12 01:19:35.303481'),(28,'new',192,'nchat','2019-12-12 01:45:37.479276'),(29,'new',192,'nchat','2019-12-12 03:46:37.937348'),(30,'Stained Glass',192,'nchat','2019-12-12 03:47:23.061347'),(31,'Stained Glass 2',192,'nchat','2019-12-12 03:48:37.885022'),(32,'new',202,'nchat','2019-12-13 03:07:44.864798'),(33,'My First Bot',202,'nchat','2019-12-13 08:18:24.195141'),(34,'Scenario1',222,'nchat','2019-12-16 03:17:39.416233'),(35,'Scenario1',223,'nchat','2019-12-16 03:22:00.960810'),(36,'Scenario1',224,'nchat','2019-12-16 03:23:39.911686'),(37,'Scenario1',225,'nchat','2019-12-16 03:25:18.156459'),(38,'Scenario1',226,'nchat','2019-12-16 03:26:27.388046'),(39,'Scenario1',227,'nchat','2019-12-16 03:28:15.455898'),(40,'Scenario1',228,'nchat','2019-12-16 03:34:21.599708'),(41,'Scenario1',229,'nchat','2019-12-16 03:35:46.305771'),(42,'シナリオ1',230,'nchat','2019-12-16 03:51:04.031966'),(43,'new',230,'nchat','2019-12-17 02:08:44.837977'),(44,'scenario 2',230,'nchat','2019-12-17 02:09:05.111378');
/*!40000 ALTER TABLE `messageflow_scenario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messageflow_settings`
--

DROP TABLE IF EXISTS `messageflow_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messageflow_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `line_access_url_part` varchar(2048) DEFAULT NULL,
  `line_channel_access_token` varchar(2048) DEFAULT NULL,
  `line_channel_secret` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messageflow_settings`
--

LOCK TABLES `messageflow_settings` WRITE;
/*!40000 ALTER TABLE `messageflow_settings` DISABLE KEYS */;
INSERT INTO `messageflow_settings` VALUES (2,7,'nchat','1','iC3NlT/U0I+AxF3Oz1nvyZRO2eh2Nrf6lJ+bg8qbpwky/9yHSWkdgPEOfdqxLZNuCwWsvqpi3TKjKBO4BcnbQgIgPu/dFeGllRDOMVHNl3UOWn0npf02Hlwev13hbEDA0kOjkYlHWP3zfFjYKWrzsQdB04t89/1O/w1cDnyilFU=','1adf87f26ad333d66e3cc36d6526ffc5'),(3,192,'nchat','37','iC3NlT/U0I+AxF3Oz1nvyZRO2eh2Nrf6lJ+bg8qbpwky/9yHSWkdgPEOfdqxLZNuCwWsvqpi3TKjKBO4BcnbQgIgPu/dFeGllRDOMVHNl3UOWn0npf02Hlwev13hbEDA0kOjkYlHWP3zfFjYKWrzsQdB04t89/1O/w1cDnyilFU=','1adf87f26ad333d66e3cc36d6526ffc5'),(4,194,'nchat',NULL,'','a'),(5,194,'nchat','random_umber',NULL,NULL),(6,194,'nchat','72513026919594127942',NULL,NULL),(7,194,'nchat','80400376020307821126',NULL,NULL),(8,194,'nchat','34743108532444934339',NULL,NULL),(9,202,'nchat','50965036801636735428','iC3NlT/U0I+AxF3Oz1nvyZRO2eh2Nrf6lJ+bg8qbpwky/9yHSWkdgPEOfdqxLZNuCwWsvqpi3TKjKBO4BcnbQgIgPu/dFeGllRDOMVHNl3UOWn0npf02Hlwev13hbEDA0kOjkYlHWP3zfFjYKWrzsQdB04t89/1O/w1cDnyilFU=','1adf87f26ad333d66e3cc36d6526ffc5'),(10,221,'nchat','47928140338428158479',NULL,NULL),(11,222,'nchat','30177176519163846469',NULL,NULL),(12,223,'nchat','93671458861227468938',NULL,NULL),(13,224,'nchat','96613331611174412257',NULL,NULL),(14,225,'nchat','85075494612762506483',NULL,NULL),(15,226,'nchat','62540574916429254520',NULL,NULL),(16,227,'nchat','99023640834011415311',NULL,NULL),(17,228,'nchat','30407774614687874266',NULL,NULL),(18,229,'nchat','59519974056110405231',NULL,NULL),(19,230,'nchat','86949439417269847469','iC3NlT/U0I+AxF3Oz1nvyZRO2eh2Nrf6lJ+bg8qbpwky/9yHSWkdgPEOfdqxLZNuCwWsvqpi3TKjKBO4BcnbQgIgPu/dFeGllRDOMVHNl3UOWn0npf02Hlwev13hbEDA0kOjkYlHWP3zfFjYKWrzsQdB04t89/1O/w1cDnyilFU=','1adf87f26ad333d66e3cc36d6526ffc5');
/*!40000 ALTER TABLE `messageflow_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nchat_business`
--

DROP TABLE IF EXISTS `nchat_business`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nchat_business` (
  `id` int NOT NULL AUTO_INCREMENT,
  `business_name` varchar(255) NOT NULL,
  `service_name` varchar(255) NOT NULL,
  `logo` varchar(2024) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_super_oem` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `lft` int unsigned NOT NULL,
  `rght` int unsigned NOT NULL,
  `tree_id` int unsigned NOT NULL,
  `level` int unsigned NOT NULL,
  `parent_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `business_name` (`business_name`),
  KEY `nchat_business_tree_id_2d000371` (`tree_id`),
  KEY `nchat_business_parent_business_id_66ddad61` (`parent_id`),
  CONSTRAINT `nchat_business_parent_id_e9d95435_fk_nchat_business_id` FOREIGN KEY (`parent_id`) REFERENCES `nchat_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nchat_business`
--

LOCK TABLES `nchat_business` WRITE;
/*!40000 ALTER TABLE `nchat_business` DISABLE KEYS */;
INSERT INTO `nchat_business` VALUES (1,'PeaceFactory','nchat',NULL,'2019-09-03 06:47:37.021310','2019-09-03 06:47:37.021310',1,0,1,66,1,0,NULL),(17,'test child 1','dummyChat1',NULL,'2019-09-03 06:47:37.021310','2019-09-03 06:47:37.021310',0,0,2,3,1,1,1),(18,'test child 2','dummyChat2',NULL,'2019-09-03 06:47:37.021310','2019-09-03 06:47:37.021310',1,0,4,7,1,1,1),(19,'test child 3','dummyChat3',NULL,'2019-09-03 06:47:37.021310','2019-09-03 06:47:37.021310',0,0,5,6,1,2,1),(20,'Test 02','Test 02','','2019-10-28 09:19:15.197301','2019-10-28 09:19:15.197351',0,0,1,2,2,0,1),(21,'Test 0222222','Test 0222222','','2019-10-28 09:21:06.614903','2019-10-28 09:21:06.614965',0,0,1,2,3,0,NULL),(22,'Good bye','hello','business_22/avatar/this_person_does_not_exist_2.jpeg','2019-10-28 09:29:15.804422','2019-11-08 08:46:17.554024',0,0,1,2,1,1,1),(23,'No Business','No Business','','2019-11-07 07:09:01.916856','2019-11-07 07:09:01.916905',0,0,1,2,4,0,NULL),(24,'none','none','','2019-11-07 07:10:46.300863','2019-11-07 07:10:46.300955',0,0,1,2,5,0,NULL),(25,'Child Account','Child Account','','2019-12-10 06:20:07.026189','2019-12-10 06:20:07.026277',0,0,1,2,6,1,1),(26,'parenttest1','parenttest1','','2019-12-11 02:10:52.955876','2019-12-11 02:10:52.955976',0,0,1,2,7,0,NULL),(27,'parenttest2','parenttest2','','2019-12-11 02:24:16.257007','2019-12-11 02:24:16.257087',0,0,8,9,1,1,1),(28,'parenttest3','parenttest3','','2019-12-11 02:29:50.304382','2019-12-11 02:29:50.304434',0,0,10,11,1,1,1),(29,'parenttest4','parenttest4','','2019-12-11 02:36:49.382192','2019-12-11 02:36:49.382241',0,0,12,13,1,1,1),(30,'parenttest6','parenttest6','','2019-12-11 02:57:56.864860','2019-12-11 02:57:56.864914',0,0,14,15,1,1,1),(31,'parenttest8','parenttest8','','2019-12-11 03:01:00.109440','2019-12-11 03:01:00.109528',0,0,16,17,1,1,1),(32,'parenttest9','parenttest9','','2019-12-11 03:02:41.075244','2019-12-11 03:02:41.075301',0,0,18,19,1,1,1),(33,'parenttest12','parenttest12','','2019-12-11 03:19:47.027338','2019-12-11 03:19:47.027397',0,0,1,2,8,0,NULL),(34,'parenttest13','parenttest13','','2019-12-11 03:22:37.089072','2019-12-11 03:22:37.089128',0,0,20,21,1,1,1),(35,'parenttest14','parenttest14','','2019-12-11 03:26:14.796989','2019-12-11 03:26:14.797115',0,0,22,23,1,1,1),(36,'hasparent3','hasparent3','','2019-12-11 06:11:28.349397','2019-12-11 06:11:28.349472',0,0,24,25,1,1,1),(37,'test2','test2','','2019-12-11 08:38:22.090906','2019-12-11 08:38:22.090979',0,0,26,27,1,1,1),(38,'access','access','','2019-12-13 02:22:32.067285','2019-12-13 02:22:32.067345',0,0,28,29,1,1,1),(39,'access2','access2','','2019-12-13 02:30:03.268713','2019-12-13 02:30:03.268987',0,0,30,31,1,1,1),(40,'access3','access3','','2019-12-13 02:39:15.968245','2019-12-13 02:39:15.968299',0,0,32,33,1,1,1),(41,'access4','access4','','2019-12-13 02:42:20.709501','2019-12-13 02:42:20.709656',0,0,34,35,1,1,1),(42,'access5','access5','','2019-12-13 02:50:58.203233','2019-12-13 02:50:58.203350',0,0,36,37,1,1,1),(43,'access6','access6','','2019-12-13 02:53:33.709074','2019-12-13 02:53:33.709167',0,0,38,39,1,1,1),(44,'access7','access7','','2019-12-13 02:58:34.960378','2019-12-13 02:58:34.960531',0,0,40,41,1,1,1),(45,'access8','access8','','2019-12-13 02:59:41.315589','2019-12-13 02:59:41.315673',0,0,42,43,1,1,1),(46,'access9','access9','','2019-12-13 03:00:16.280208','2019-12-13 03:00:16.280260',0,0,44,45,1,1,1),(47,'Bot','Bot','','2019-12-16 03:15:20.002009','2019-12-16 03:15:20.002073',0,0,46,47,1,1,1),(48,'Bot2','Bot2','','2019-12-16 03:17:39.085729','2019-12-16 03:17:39.085781',0,0,48,49,1,1,1),(49,'Test3','Test3','','2019-12-16 03:22:00.475559','2019-12-16 03:22:00.475618',0,0,50,51,1,1,1),(50,'Test4','Test4','','2019-12-16 03:23:39.505016','2019-12-16 03:23:39.505119',0,0,52,53,1,1,1),(51,'Test5','Test5','','2019-12-16 03:25:17.761456','2019-12-16 03:25:17.761541',0,0,54,55,1,1,1),(52,'Test6','Test6','','2019-12-16 03:26:27.071272','2019-12-16 03:26:27.071322',0,0,56,57,1,1,1),(53,'test7','test7','','2019-12-16 03:28:15.163377','2019-12-16 03:28:15.163424',0,0,58,59,1,1,1),(54,'test8','test8','','2019-12-16 03:34:21.308577','2019-12-16 03:34:21.308630',0,0,60,61,1,1,1),(55,'test9','test9','','2019-12-16 03:35:46.008420','2019-12-16 03:35:46.008471',0,0,62,63,1,1,1),(56,'test10','test10','','2019-12-16 03:51:03.709066','2019-12-16 03:51:03.709117',0,0,64,65,1,1,1);
/*!40000 ALTER TABLE `nchat_business` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nchat_businessplan`
--

DROP TABLE IF EXISTS `nchat_businessplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nchat_businessplan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `price` bigint NOT NULL,
  `regist_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `business_id` int NOT NULL,
  `duration` int NOT NULL,
  `recurring` tinyint(1) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `nchat_businessplan_business_id_f6648a40_fk_nchat_business_id` (`business_id`),
  CONSTRAINT `nchat_businessplan_business_id_f6648a40_fk_nchat_business_id` FOREIGN KEY (`business_id`) REFERENCES `nchat_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nchat_businessplan`
--

LOCK TABLES `nchat_businessplan` WRITE;
/*!40000 ALTER TABLE `nchat_businessplan` DISABLE KEYS */;
INSERT INTO `nchat_businessplan` VALUES (1,'1 Month',3000,'2019-09-03 06:48:11.651483','2019-10-29 05:59:50.432344',0,1,1,1,'<p>Paragraph!</p><p>Another Paragraph!</p>'),(14,'Plan 18',18000,'2019-10-28 08:35:16.284845','2019-10-29 08:35:10.312445',0,1,4,1,'<p>this is easy</p>'),(15,'No Month Plan',0,'2019-10-28 08:56:11.103145','2019-10-28 09:03:49.203838',1,1,0,1,'<p>the no month plan!</p>'),(16,'Delete This Plan',0,'2019-10-28 08:57:32.732059','2019-10-28 09:01:13.842882',1,1,0,1,'<p>This plan should not appear.</p>'),(17,'Funky New Plan',10000000,'2019-10-29 08:22:10.844196','2019-10-29 08:22:37.355674',0,1,1,1,'<p>Elite Package</p>'),(18,'Cheap Package',1000,'2019-10-29 08:26:05.400126','2019-10-29 08:30:21.695770',1,1,3,1,'<p>1000 Yen!!!</p><p>What a bargain!</p>'),(19,'New Plan',0,'2019-10-29 09:01:57.336120','2019-10-29 09:01:57.336160',0,1,0,1,''),(20,'New Plan',0,'2019-12-10 04:03:56.657976','2019-12-10 04:03:56.658030',0,1,0,1,'');
/*!40000 ALTER TABLE `nchat_businessplan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nchat_file`
--

DROP TABLE IF EXISTS `nchat_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nchat_file` (
  `id` int NOT NULL AUTO_INCREMENT,
  `owner_id` int NOT NULL,
  `app_id` varchar(256) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `upload` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nchat_file`
--

LOCK TABLES `nchat_file` WRITE;
/*!40000 ALTER TABLE `nchat_file` DISABLE KEYS */;
INSERT INTO `nchat_file` VALUES (6,7,'nchat','2019-11-15 03:20:30.581155','nchat/7/afropanda.jpg'),(7,7,'nchat','2019-11-15 06:13:08.953296','nchat/7/grinning_afro_panda.jpg'),(8,7,'nchat','2019-11-15 06:13:43.832933','nchat/7/DiscoAfroPanda.jpg'),(9,7,'nchat','2019-11-15 06:13:56.242399','nchat/7/afro_plus_panda.jpeg'),(10,7,'nchat','2019-11-15 06:14:04.456985','nchat/7/afro_panda_school_girl.png'),(11,7,'nchat','2019-11-15 06:14:14.680790','nchat/7/afro_panda_comb.jpg'),(12,147,'nchat','2019-11-22 03:20:21.295533','nchat/147/this_person_does_not_exist.jpeg'),(13,147,'nchat','2019-11-22 09:50:01.564495','nchat/147/this_person_does_not_exist_2.jpeg'),(14,147,'nchat','2019-11-22 09:57:00.121360','nchat/147/afro_panda_comb.jpg'),(15,147,'nchat','2019-11-22 09:57:06.838347','nchat/147/grinning_afro_panda.jpg'),(16,147,'nchat','2019-11-22 09:57:15.257131','nchat/147/DiscoAfroPanda.jpg'),(17,147,'nchat','2019-11-22 09:57:22.915699','nchat/147/afro_plus_panda.jpeg'),(18,147,'nchat','2019-11-22 09:57:31.330388','nchat/147/afro_panda_school_girl.png'),(19,147,'nchat','2019-11-22 09:57:52.624224','nchat/147/afropanda.jpg'),(20,147,'nchat','2019-11-27 01:51:22.709636','nchat/147/test.js'),(21,147,'nchat','2019-11-28 04:08:13.154064','nchat/147/file_icon.svg'),(22,147,'nchat','2019-11-28 04:12:46.216711','nchat/147/file_icon.png'),(23,192,'nchat','2019-12-12 03:47:03.240775','nchat/192/stained-glass-51982.jpg'),(24,192,'nchat','2019-12-12 09:01:13.097163','nchat/192/Screen_Shot_2019-12-02_at_11.52.42.png'),(25,230,'nchat','2019-12-16 04:37:31.747671','nchat/230/file_icon.png'),(26,230,'nchat','2019-12-16 04:39:32.428964','nchat/230/afropanda.jpg');
/*!40000 ALTER TABLE `nchat_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nchat_paymenthistory`
--

DROP TABLE IF EXISTS `nchat_paymenthistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nchat_paymenthistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plan_name` varchar(256) NOT NULL,
  `amount` bigint NOT NULL,
  `expiration_dt` datetime(6) NOT NULL,
  `regist_dt` datetime(6) NOT NULL,
  `status` int NOT NULL,
  `from_business_id` int NOT NULL,
  `to_business_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `nchat_paymenthistory_from_business_id_44a1da69_fk_nchat_bus` (`from_business_id`),
  KEY `nchat_paymenthistory_to_business_id_d7390a9c_fk_nchat_bus` (`to_business_id`),
  CONSTRAINT `nchat_paymenthistory_from_business_id_44a1da69_fk_nchat_bus` FOREIGN KEY (`from_business_id`) REFERENCES `nchat_business` (`id`),
  CONSTRAINT `nchat_paymenthistory_to_business_id_d7390a9c_fk_nchat_bus` FOREIGN KEY (`to_business_id`) REFERENCES `nchat_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nchat_paymenthistory`
--

LOCK TABLES `nchat_paymenthistory` WRITE;
/*!40000 ALTER TABLE `nchat_paymenthistory` DISABLE KEYS */;
INSERT INTO `nchat_paymenthistory` VALUES (10,'1Month',2000,'2019-09-03 06:48:11.651483','2019-09-03 06:48:11.651483',1,17,1),(11,'1Month',1500,'2019-10-03 06:48:11.651483','2019-09-03 06:48:11.651483',1,17,1),(12,'1Month',1500,'2019-11-03 06:48:11.651483','2019-09-03 06:48:11.651483',1,17,1),(13,'1Month',2000,'2019-11-03 06:48:11.651483','2019-09-03 06:48:11.651483',1,1,18),(14,'1Month',2000,'2019-10-03 06:48:11.651483','2019-09-03 06:48:11.651483',1,1,18),(15,'1Month',2000,'2019-09-03 06:48:11.651483','2019-09-03 06:48:11.651483',1,1,18),(16,'1 Month',3000,'2019-12-03 06:48:11.651483','2019-10-24 05:44:49.139166',0,1,1),(17,'1 Month',3000,'2020-01-03 06:48:11.651483','2019-10-24 05:58:04.634833',0,1,1),(18,'3 Month',7000,'2020-04-03 06:48:11.651483','2019-10-24 06:00:51.488642',0,1,1),(19,'1 Month',3000,'2020-05-03 06:48:11.651483','2019-10-24 06:12:02.695287',0,1,1),(20,'1 Month',3000,'2020-06-03 06:48:11.651483','2019-10-24 06:32:33.140072',0,1,1),(21,'1 Month',3000,'2020-07-03 06:48:11.651483','2019-10-24 08:45:07.876679',0,1,1),(22,'1 Month',3000,'2020-08-03 06:48:11.651483','2019-10-24 08:47:16.584605',0,1,1),(23,'1 Month',3000,'2020-09-03 06:48:11.651483','2019-10-24 08:47:42.649815',0,1,1),(24,'6 Month',12000,'2021-03-03 06:48:11.651483','2019-10-24 08:50:20.114704',0,1,1),(25,'1 Year',20000,'2022-03-03 06:48:11.651483','2019-10-24 09:22:06.241768',0,1,1),(26,'1 Month',3000,'2022-04-03 06:48:11.651483','2019-10-24 09:51:10.816484',0,1,1),(27,'1 Month',3000,'2022-05-03 06:48:11.651483','2019-10-24 09:52:06.351660',0,1,1),(28,'1 Month',3000,'2022-06-03 06:48:11.651483','2019-10-24 09:53:35.729520',3,1,1),(29,'6 Month',12000,'2022-12-03 06:48:11.651483','2019-10-24 10:20:08.268153',0,1,1),(30,'1 Month',3000,'2023-01-03 06:48:11.651483','2019-10-24 10:21:58.104450',0,1,1),(31,'1 Month',3000,'2023-02-03 06:48:11.651483','2019-10-24 10:23:11.818988',2,1,1),(32,'Plan 18',18000,'2023-11-03 06:48:11.651483','2019-10-28 09:07:53.264397',2,1,1),(33,'1 Month',3000,'2023-12-03 06:48:11.651483','2019-10-29 05:24:08.086974',2,1,1),(34,'Plan 18',18000,'2024-09-03 06:48:11.651483','2019-10-29 05:38:46.477779',2,1,1),(40,'New Plan',0,'2019-10-30 06:09:25.791844','2019-10-30 06:09:25.799545',0,22,1),(41,'Funky New Plan',10000000,'2019-09-30 06:09:25.791844','2019-10-30 06:11:43.656234',2,22,1),(42,'1 Month',3000,'2019-10-30 06:09:25.791844','2019-11-01 05:24:03.277188',2,22,1),(43,'1 Month',3000,'2019-11-30 06:09:25.791844','2019-11-01 05:47:49.599627',2,22,1),(44,'1 Month',3000,'2020-01-10 08:15:04.117018','2019-12-10 08:15:04.132427',0,25,1),(45,'1 Month',3000,'2020-02-10 08:15:04.117018','2019-12-10 08:17:41.452974',0,25,1),(46,'1 Month',3000,'2020-03-10 08:15:04.117018','2019-12-10 08:20:38.159142',0,25,1),(47,'1 Month',3000,'2020-02-28 03:02:39.064619','2020-01-28 03:02:39.067407',0,37,1),(48,'1 Month',3000,'2020-03-28 03:02:39.064619','2020-01-28 04:49:19.350188',0,37,1);
/*!40000 ALTER TABLE `nchat_paymenthistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nchat_settings`
--

DROP TABLE IF EXISTS `nchat_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nchat_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content_json` longtext,
  `business_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `nchat_settings_business_id_d2e4c569_fk_nchat_business_id` (`business_id`),
  CONSTRAINT `nchat_settings_business_id_d2e4c569_fk_nchat_business_id` FOREIGN KEY (`business_id`) REFERENCES `nchat_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nchat_settings`
--

LOCK TABLES `nchat_settings` WRITE;
/*!40000 ALTER TABLE `nchat_settings` DISABLE KEYS */;
INSERT INTO `nchat_settings` VALUES (2,'{\"line_channel_id\": 524398723598, \"line_channel_secret\": \"hlkjashgf;kjshfdgkljhslj\", \"line_channel_access_token\": \"hsdfgljkhfasgjhsdfgkljahd\"}',22),(3,'{\"line_access_url_part\": \"1\", \"widget_theme\": \"Maximus Martinus\", \"widget_font_family\": \"Arial\", \"widget_font_style\": \"normal\", \"widget_text_color\": \"FFFFFF\", \"widget_bot_icon\": \"https://upload.wikimedia.org/wikipedia/commons/b/b6/Emojione_1F916.svg\", \"widget_user_icon\": \"https://upload.wikimedia.org/wikipedia/commons/2/27/Emojione_1F464.svg\", \"widget_font_size\": 12, \"line_channel_secret\": \"1adf87f26ad333d66e3cc36d6526ffc5\", \"line_channel_access_token\": \"iC3NlT/U0I+AxF3Oz1nvyZRO2eh2Nrf6lJ+bg8qbpwky/9yHSWkdgPEOfdqxLZNuCwWsvqpi3TKjKBO4BcnbQgIgPu/dFeGllRDOMVHNl3UOWn0npf02Hlwev13hbEDA0kOjkYlHWP3zfFjYKWrzsQdB04t89/1O/w1cDnyilFU=\"}',1);
/*!40000 ALTER TABLE `nchat_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nchat_vendoruser`
--

DROP TABLE IF EXISTS `nchat_vendoruser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nchat_vendoruser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(64) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `email` varchar(255) NOT NULL,
  `tel` varchar(32) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_oem_admin` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auth_user_id` int DEFAULT NULL,
  `business_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `nchat_vendoruser_auth_user_id_16e7f6e7_fk_auth_user_id` (`auth_user_id`),
  KEY `nchat_vendoruser_business_id_47075974_fk_nchat_business_id` (`business_id`),
  CONSTRAINT `nchat_vendoruser_auth_user_id_16e7f6e7_fk_auth_user_id` FOREIGN KEY (`auth_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `nchat_vendoruser_business_id_47075974_fk_nchat_business_id` FOREIGN KEY (`business_id`) REFERENCES `nchat_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nchat_vendoruser`
--

LOCK TABLES `nchat_vendoruser` WRITE;
/*!40000 ALTER TABLE `nchat_vendoruser` DISABLE KEYS */;
INSERT INTO `nchat_vendoruser` VALUES (1,'Lastname','Test','test01@test.com','123456789','2019-09-03 06:48:11.651483','2019-09-03 06:48:11.651513',1,1,0,7,1),(3,'Lastname','Test900','test900@test.com','9483092923','2019-10-28 09:29:16.079982','2019-10-28 09:29:16.080031',1,1,0,147,22),(6,'','','test03@test.com','578473984','2019-11-07 07:09:02.199389','2019-11-07 07:09:02.199430',1,0,0,148,23),(7,'','','new@user.com','4737282','2019-11-07 07:10:46.622221','2019-11-07 07:10:46.622269',1,0,0,149,24),(8,'','','childaccount@test.com','911','2019-12-10 06:20:07.365918','2019-12-10 06:20:07.365971',1,1,0,180,25),(9,'','','account@hasparent.com','384729847','2019-12-11 02:10:53.410073','2019-12-11 02:10:53.410156',1,0,0,181,26),(10,'','','account2@hasparent.com','384729847','2019-12-11 02:24:16.715270','2019-12-11 02:24:16.715347',1,0,0,182,27),(11,'','','account3@hasparent.com','384729847','2019-12-11 02:29:50.586619','2019-12-11 02:29:50.586671',1,0,0,183,28),(12,'','','account4@hasparent.com','384729847','2019-12-11 02:36:49.764422','2019-12-11 02:36:49.764471',1,0,0,184,29),(13,'','','account6@hasparent.com','384729847','2019-12-11 02:57:57.146307','2019-12-11 02:57:57.146352',1,0,0,185,30),(14,'','','account8@hasparent.com','384729847','2019-12-11 03:01:00.544253','2019-12-11 03:01:00.544335',1,0,0,186,31),(15,'','','account9@hasparent.com','384729847','2019-12-11 03:02:41.367265','2019-12-11 03:02:41.367316',1,0,0,187,32),(16,'','','account12@hasparent.com','384729847','2019-12-11 03:19:47.342090','2019-12-11 03:19:47.342132',1,0,0,188,33),(17,'','','account13@hasparent.com','384729847','2019-12-11 03:22:37.366041','2019-12-11 03:22:37.366083',1,0,0,189,34),(18,'','','account14@hasparent.com','384729847','2019-12-11 03:26:15.086582','2019-12-11 03:26:15.086629',1,0,0,190,35),(19,'','','hasparent3@test.com','564738','2019-12-11 06:11:28.680013','2019-12-11 06:11:28.680063',1,1,0,191,36),(20,'','','test2@test.com','34273857','2019-12-11 08:38:22.412032','2019-12-11 08:38:22.412087',1,1,0,192,37),(21,'','','access1@test.com','6','2019-12-13 02:22:32.347258','2019-12-13 02:22:32.347308',1,1,0,194,38),(22,'','','access2@test.com','6','2019-12-13 02:30:03.574388','2019-12-13 02:30:03.574434',1,0,0,195,39),(23,'','','access3@test.com','6','2019-12-13 02:39:16.269949','2019-12-13 02:39:16.270008',1,0,0,196,40),(24,'','','access5@test.com','6','2019-12-13 02:50:58.653814','2019-12-13 02:50:58.653895',1,0,0,198,42),(25,'','','access6@test.com','6','2019-12-13 02:53:33.988768','2019-12-13 02:53:33.988820',1,0,0,199,43),(26,'','','access7@test.com','6','2019-12-13 02:58:35.377335','2019-12-13 02:58:35.377422',1,0,0,200,44),(27,'','','access8@test.com','6','2019-12-13 02:59:41.751341','2019-12-13 02:59:41.751447',1,0,0,201,45),(28,'','','access9@test.com','6','2019-12-13 03:00:16.551181','2019-12-13 03:00:16.551338',1,1,0,202,46),(29,'','','bot@test.com','6','2019-12-16 03:15:20.289494','2019-12-16 03:15:20.289546',1,0,0,221,47),(30,'','','bot2@test.com','6','2019-12-16 03:17:39.396209','2019-12-16 03:17:39.396341',1,0,0,222,48),(31,'','','Bot3@test.com','6','2019-12-16 03:22:00.939489','2019-12-16 03:22:00.939566',1,0,0,223,49),(32,'','','Bot4@test.com','6','2019-12-16 03:23:39.888987','2019-12-16 03:23:39.889038',1,0,0,224,50),(33,'','','Bot5@test.com','6','2019-12-16 03:25:18.146384','2019-12-16 03:25:18.146426',1,0,0,225,51),(34,'','','Bot6@test.com','6','2019-12-16 03:26:27.364759','2019-12-16 03:26:27.364897',1,0,0,226,52),(35,'','','test7@yahoo.com','6','2019-12-16 03:28:15.435171','2019-12-16 03:28:15.435224',1,1,0,227,53),(36,'','','test8@yahoo.com','6','2019-12-16 03:34:21.589895','2019-12-16 03:34:21.589950',1,0,0,228,54),(37,'','','test9@test.com','6','2019-12-16 03:35:46.297551','2019-12-16 03:35:46.297597',1,1,0,229,55),(38,'','','test10@test.com','6','2019-12-16 03:51:03.982750','2019-12-16 03:51:03.982798',1,1,0,230,56);
/*!40000 ALTER TABLE `nchat_vendoruser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_coupon`
--

DROP TABLE IF EXISTS `qa_coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_coupon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `data` varchar(256) DEFAULT NULL,
  `style` varchar(256) DEFAULT NULL,
  `valid_from` datetime(6) NOT NULL,
  `valid_until` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `type_id` int NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `qrcode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_coupon_type_id_f480878f_fk_qa_coupontype_id` (`type_id`),
  KEY `qa_coupon_vendor_branch_id_3338d722_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `qa_coupon_type_id_f480878f_fk_qa_coupontype_id` FOREIGN KEY (`type_id`) REFERENCES `qa_coupontype` (`id`),
  CONSTRAINT `qa_coupon_vendor_branch_id_3338d722_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_coupon`
--

LOCK TABLES `qa_coupon` WRITE;
/*!40000 ALTER TABLE `qa_coupon` DISABLE KEYS */;
INSERT INTO `qa_coupon` VALUES (1,'testname','tester.com','','2019-03-18 03:00:00.000000','2019-03-20 07:12:00.000000','2019-03-18 01:50:30.249262','2019-03-19 00:58:21.402831',1,2,1,NULL),(6,'test expired coupon','test text','','2019-02-18 06:37:00.000000','2019-02-20 06:37:00.000000','2019-03-18 06:37:42.456870','2019-03-19 08:23:54.676391',0,1,1,'qrcodes/qrcode-6.png'),(7,'',NULL,NULL,'2019-03-18 07:29:39.155361',NULL,'2019-03-18 07:29:39.156232','2019-06-25 04:45:45.225234',1,1,1,'qrcodes/qrcode-7.png'),(8,'test coupon name','empty','','2019-03-19 00:58:00.000000','2019-04-19 00:58:00.000000','2019-03-19 00:58:49.644428','2019-08-20 07:12:03.756855',0,1,1,'qrcodes/qrcode-8_xs3VtRK.png'),(9,'',NULL,NULL,'2019-03-19 01:33:22.701113',NULL,'2019-03-19 01:33:22.701729','2019-06-25 04:45:40.737059',1,1,1,'qrcodes/qrcode-9.png'),(10,'',NULL,NULL,'2019-05-14 05:13:16.952456',NULL,'2019-05-14 05:13:18.003675','2019-05-14 05:13:20.886211',1,1,1,'qrcodes/qrcode-None_cIbPdMY.png'),(11,'test coupon new print','test','','3019-06-24 04:37:23.000000','3019-06-24 04:37:23.000000','2019-06-24 04:37:22.057884','2019-06-25 04:45:48.611406',1,1,1,'qrcodes/qrcode-None_y1x1fgT.png'),(12,'',NULL,NULL,'2019-06-25 04:44:46.000000',NULL,'2019-06-25 04:44:46.600243','2019-06-25 04:45:35.106848',1,1,1,'qrcodes/qrcode-12.png'),(13,'new testing','empty','','3019-06-25 04:45:49.000000','3019-06-25 04:45:49.000000','2019-06-25 04:45:49.989013','2019-06-25 04:46:06.295379',0,3,1,'qrcodes/qrcode-13.png'),(14,'',NULL,NULL,'2019-07-31 01:34:00.000000',NULL,'2019-07-31 01:34:07.950965','2019-08-01 05:50:41.096017',1,1,1,'qrcodes/qrcode-14.png'),(15,'',NULL,NULL,'2019-08-01 05:50:00.000000',NULL,'2019-08-01 05:50:22.387650','2019-08-01 05:50:35.381625',1,1,1,'qrcodes/qrcode-15.png'),(16,'test new coupon thing','1','','2029-08-01 08:41:00.000000','2039-08-01 08:41:00.000000','2019-08-01 08:41:26.242099','2019-08-22 03:27:49.559185',0,3,1,'qrcodes/qrcode-16.png'),(17,'',NULL,NULL,'2019-09-11 06:59:00.000000',NULL,'2019-09-11 06:59:32.621190','2019-09-11 06:59:32.621222',0,1,1,'');
/*!40000 ALTER TABLE `qa_coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_couponclaim`
--

DROP TABLE IF EXISTS `qa_couponclaim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_couponclaim` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `coupon_id` int NOT NULL,
  `end_user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_couponclaim_coupon_id_f8a22270_fk_qa_coupon_id` (`coupon_id`),
  KEY `qa_couponclaim_end_user_id_8c734d09_fk_core_enduser_id` (`end_user_id`),
  CONSTRAINT `qa_couponclaim_coupon_id_f8a22270_fk_qa_coupon_id` FOREIGN KEY (`coupon_id`) REFERENCES `qa_coupon` (`id`),
  CONSTRAINT `qa_couponclaim_end_user_id_8c734d09_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_couponclaim`
--

LOCK TABLES `qa_couponclaim` WRITE;
/*!40000 ALTER TABLE `qa_couponclaim` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_couponclaim` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_coupontype`
--

DROP TABLE IF EXISTS `qa_coupontype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_coupontype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_coupontype`
--

LOCK TABLES `qa_coupontype` WRITE;
/*!40000 ALTER TABLE `qa_coupontype` DISABLE KEYS */;
INSERT INTO `qa_coupontype` VALUES (1,'text','2019-03-12 08:34:49.875496','2019-03-12 08:34:49.875537'),(2,'url','2019-03-12 08:34:49.876095','2019-03-12 08:34:49.876122'),(3,'questionnaire','2019-06-24 08:34:08.139636','2019-06-24 08:34:08.139682');
/*!40000 ALTER TABLE `qa_coupontype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_enduserquestionnaire`
--

DROP TABLE IF EXISTS `qa_enduserquestionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_enduserquestionnaire` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regist_dt` datetime(6) DEFAULT NULL,
  `end_user_id` int NOT NULL,
  `questionnaire_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_enduserquestionnaire_end_user_id_16941ed4_fk_core_enduser_id` (`end_user_id`),
  KEY `qa_enduserquestionna_questionnaire_id_fbf473aa_fk_qa_questi` (`questionnaire_id`),
  CONSTRAINT `qa_enduserquestionna_questionnaire_id_fbf473aa_fk_qa_questi` FOREIGN KEY (`questionnaire_id`) REFERENCES `qa_questionnaire` (`id`),
  CONSTRAINT `qa_enduserquestionnaire_end_user_id_16941ed4_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_enduserquestionnaire`
--

LOCK TABLES `qa_enduserquestionnaire` WRITE;
/*!40000 ALTER TABLE `qa_enduserquestionnaire` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_enduserquestionnaire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_matrigger`
--

DROP TABLE IF EXISTS `qa_matrigger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_matrigger` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message_id` int NOT NULL,
  `trigger_type_id` int NOT NULL,
  `days` int NOT NULL,
  `hours` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_matrigger_message_id_7439b9a6_fk_qa_message_id` (`message_id`),
  KEY `qa_matrigger_trigger_type_id_9c623f8a_fk_qa_matriggertype_id` (`trigger_type_id`),
  CONSTRAINT `qa_matrigger_message_id_7439b9a6_fk_qa_message_id` FOREIGN KEY (`message_id`) REFERENCES `qa_message` (`id`),
  CONSTRAINT `qa_matrigger_trigger_type_id_9c623f8a_fk_qa_matriggertype_id` FOREIGN KEY (`trigger_type_id`) REFERENCES `qa_matriggertype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_matrigger`
--

LOCK TABLES `qa_matrigger` WRITE;
/*!40000 ALTER TABLE `qa_matrigger` DISABLE KEYS */;
INSERT INTO `qa_matrigger` VALUES (1,3,1,1,1),(7,9,1,0,0),(8,10,1,0,1),(9,11,1,0,3),(10,12,1,0,4),(11,13,1,0,5),(12,14,1,0,5),(13,15,1,0,0),(14,16,1,0,0),(15,17,1,0,0),(16,18,1,0,0),(17,19,1,0,0),(18,20,1,0,0),(19,21,1,0,0),(20,22,1,0,0),(21,23,1,0,0),(22,24,1,0,0),(23,25,1,0,0),(24,26,1,0,0),(25,27,1,0,0),(26,28,1,0,0),(27,29,1,0,0),(28,30,1,0,0),(29,31,1,0,0),(30,32,1,0,0),(31,33,1,0,0),(32,34,1,0,0),(33,35,1,0,0),(34,36,1,0,0);
/*!40000 ALTER TABLE `qa_matrigger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_matriggertype`
--

DROP TABLE IF EXISTS `qa_matriggertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_matriggertype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_matriggertype`
--

LOCK TABLES `qa_matriggertype` WRITE;
/*!40000 ALTER TABLE `qa_matriggertype` DISABLE KEYS */;
INSERT INTO `qa_matriggertype` VALUES (1,'after joining'),(2,'after taking survey'),(3,'after using coupon'),(4,'after no activity'),(5,'after new survey goes live'),(6,'after new coupon goes live'),(7,'before coupon expires'),(8,'before survey expires'),(9,'before birthday');
/*!40000 ALTER TABLE `qa_matriggertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_message`
--

DROP TABLE IF EXISTS `qa_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(256) NOT NULL,
  `message_text` longtext NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_message_vendor_branch_id_96f7e132_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `qa_message_vendor_branch_id_96f7e132_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_message`
--

LOCK TABLES `qa_message` WRITE;
/*!40000 ALTER TABLE `qa_message` DISABLE KEYS */;
INSERT INTO `qa_message` VALUES (1,'test message','test message contents',1),(2,'','',1),(3,'test subject2','test contents',1),(9,'very long message subject name that we want to try out here','contents',1),(10,'test 2','<p>test 2</p>',1),(11,'test 3','<p>test 3</p>',1),(12,'test 4','<p>test 4</p>',1),(13,'very long message name to test something in the system.','<p>very long message name to test something in the system right now so lets see how this fits</p>',1),(14,'test 5','<p>test 5</p>',1),(15,'','',1),(16,'','',1),(17,'fdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdassddddddddddddddddfdas','<p style=\"text-align: center;\">dfdf</p>',1),(18,'','',1),(19,'','',1),(20,'','',1),(21,'','',1),(22,'','',1),(23,'','',1),(24,'','',1),(25,'','',1),(26,'','',1),(27,'','',1),(28,'','',1),(29,'','',1),(30,'','',1),(31,'','',1),(32,'','',1),(33,'','',1),(34,'','',1),(35,'','',1),(36,'','',1);
/*!40000 ALTER TABLE `qa_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_notification`
--

DROP TABLE IF EXISTS `qa_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_notification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(512) NOT NULL,
  `body` longtext NOT NULL,
  `priority` int NOT NULL,
  `schedule_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_notification`
--

LOCK TABLES `qa_notification` WRITE;
/*!40000 ALTER TABLE `qa_notification` DISABLE KEYS */;
INSERT INTO `qa_notification` VALUES (1,'The Database Works 1','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',1,'2020-12-31 00:00:00.000000'),(2,'The Database Works 2','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',2,'2021-01-01 00:00:00.000000'),(3,'The Database Works 3','This is number 3.',2,'1999-01-01 00:00:00.000000');
/*!40000 ALTER TABLE `qa_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_notificationhistory`
--

DROP TABLE IF EXISTS `qa_notificationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_notificationhistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `seen` tinyint(1) NOT NULL,
  `seen_dt` datetime(6) DEFAULT NULL,
  `notification_id` int NOT NULL,
  `vendor_user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_notificationhisto_notification_id_c8ce617a_fk_qa_notifi` (`notification_id`),
  KEY `qa_notificationhisto_vendor_user_id_44062632_fk_qa_vendor` (`vendor_user_id`),
  CONSTRAINT `qa_notificationhisto_notification_id_c8ce617a_fk_qa_notifi` FOREIGN KEY (`notification_id`) REFERENCES `qa_notification` (`id`),
  CONSTRAINT `qa_notificationhisto_vendor_user_id_44062632_fk_qa_vendor` FOREIGN KEY (`vendor_user_id`) REFERENCES `qa_vendoruser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_notificationhistory`
--

LOCK TABLES `qa_notificationhistory` WRITE;
/*!40000 ALTER TABLE `qa_notificationhistory` DISABLE KEYS */;
INSERT INTO `qa_notificationhistory` VALUES (100,0,NULL,1,1),(200,1,NULL,2,1),(300,0,NULL,3,1);
/*!40000 ALTER TABLE `qa_notificationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_notificationservice`
--

DROP TABLE IF EXISTS `qa_notificationservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_notificationservice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `icon` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_notificationservice`
--

LOCK TABLES `qa_notificationservice` WRITE;
/*!40000 ALTER TABLE `qa_notificationservice` DISABLE KEYS */;
INSERT INTO `qa_notificationservice` VALUES (1,'Email','fa fa-2x fa-envelope','2019-03-12 02:04:51.713591','2019-03-12 02:04:51.713633',0),(2,'Slack','fa fa-2x fa-slack','2019-03-12 02:04:51.714152','2019-03-12 02:04:51.714171',0);
/*!40000 ALTER TABLE `qa_notificationservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_notificationsetting`
--

DROP TABLE IF EXISTS `qa_notificationsetting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_notificationsetting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `setting_value` int NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `notification_service_id` int NOT NULL,
  `vendor_user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_notificationsetti_notification_service_f22c6d26_fk_qa_notifi` (`notification_service_id`),
  KEY `qa_notificationsetti_vendor_user_id_0675b0ad_fk_qa_vendor` (`vendor_user_id`),
  CONSTRAINT `qa_notificationsetti_notification_service_f22c6d26_fk_qa_notifi` FOREIGN KEY (`notification_service_id`) REFERENCES `qa_notificationservice` (`id`),
  CONSTRAINT `qa_notificationsetti_vendor_user_id_0675b0ad_fk_qa_vendor` FOREIGN KEY (`vendor_user_id`) REFERENCES `qa_vendoruser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_notificationsetting`
--

LOCK TABLES `qa_notificationsetting` WRITE;
/*!40000 ALTER TABLE `qa_notificationsetting` DISABLE KEYS */;
INSERT INTO `qa_notificationsetting` VALUES (1,2,'2019-03-12 02:17:31.296557','2019-03-12 06:13:50.080127',0,1,1),(2,0,'2019-03-12 02:17:31.296557','2019-03-12 02:18:06.431546',0,2,1);
/*!40000 ALTER TABLE `qa_notificationsetting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_plan`
--

DROP TABLE IF EXISTS `qa_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_plan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_plan`
--

LOCK TABLES `qa_plan` WRITE;
/*!40000 ALTER TABLE `qa_plan` DISABLE KEYS */;
INSERT INTO `qa_plan` VALUES (1,'Free','2019-03-05 02:51:48.311560','2019-03-05 02:51:48.311605',0);
/*!40000 ALTER TABLE `qa_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_product`
--

DROP TABLE IF EXISTS `qa_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `code` varchar(256) DEFAULT NULL,
  `memo` longtext,
  `sales_price` int DEFAULT NULL,
  `receiving_price` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `product_category_id` int DEFAULT NULL,
  `stock_space_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_product_product_category_id_e4012147_fk_qa_productcategory_id` (`product_category_id`),
  KEY `qa_product_stock_space_id_8125c440_fk_qa_stockspace_id` (`stock_space_id`),
  CONSTRAINT `qa_product_product_category_id_e4012147_fk_qa_productcategory_id` FOREIGN KEY (`product_category_id`) REFERENCES `qa_productcategory` (`id`),
  CONSTRAINT `qa_product_stock_space_id_8125c440_fk_qa_stockspace_id` FOREIGN KEY (`stock_space_id`) REFERENCES `qa_stockspace` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_product`
--

LOCK TABLES `qa_product` WRITE;
/*!40000 ALTER TABLE `qa_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_productcategory`
--

DROP TABLE IF EXISTS `qa_productcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_productcategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `code` varchar(256) DEFAULT NULL,
  `memo` longtext,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_productcategory_vendor_id_0ca2a029_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `qa_productcategory_vendor_id_0ca2a029_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_productcategory`
--

LOCK TABLES `qa_productcategory` WRITE;
/*!40000 ALTER TABLE `qa_productcategory` DISABLE KEYS */;
INSERT INTO `qa_productcategory` VALUES (1,'test',NULL,'',NULL,'2019-06-26 05:37:52.275187','2019-06-26 05:39:26.768105',0,1);
/*!40000 ALTER TABLE `qa_productcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_question`
--

DROP TABLE IF EXISTS `qa_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `question_text` varchar(2048) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `type_id` int NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `question_options` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_question_type_id_07437bc8_fk_qa_questiontype_id` (`type_id`),
  KEY `qa_question_vendor_branch_id_fccfaa96_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `qa_question_type_id_07437bc8_fk_qa_questiontype_id` FOREIGN KEY (`type_id`) REFERENCES `qa_questiontype` (`id`),
  CONSTRAINT `qa_question_vendor_branch_id_fccfaa96_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_question`
--

LOCK TABLES `qa_question` WRITE;
/*!40000 ALTER TABLE `qa_question` DISABLE KEYS */;
INSERT INTO `qa_question` VALUES (1,'test question','are you prepared?2','2019-03-25 07:42:44.041165','2019-06-03 01:08:24.283981',1,1,NULL),(2,'test q 2','do you like this?','2019-03-25 07:42:44.041165','2019-06-03 01:08:24.294593',2,1,NULL),(25,'','test456','2019-04-23 07:27:38.196508','2019-05-07 08:41:46.220865',1,1,NULL),(26,'','test456','2019-04-23 08:32:15.237366','2019-04-23 08:32:15.237405',1,1,NULL),(27,'','tet123','2019-04-25 02:07:06.423214','2019-05-07 08:41:46.210863',2,1,NULL),(28,'','third question?','2019-05-07 08:41:25.195112','2019-05-07 08:41:25.195141',1,1,NULL),(29,'','third question as an option?','2019-05-07 08:41:46.229678','2019-05-07 08:41:46.229704',2,1,NULL),(30,'','test question 3','2019-05-17 09:16:45.335307','2019-06-03 01:08:24.304786',3,1,NULL),(31,'','testing first name?','2019-06-03 01:07:41.014670','2019-06-03 01:08:24.314255',3,1,NULL),(32,'','thank you, now please write red','2019-06-03 01:08:24.322610','2019-06-03 01:08:24.322636',1,1,NULL),(33,'','test question 3','2019-06-06 07:14:30.909906','2019-06-07 07:43:35.471060',2,1,NULL);
/*!40000 ALTER TABLE `qa_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_questionnaire`
--

DROP TABLE IF EXISTS `qa_questionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_questionnaire` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `intro` varchar(2048) NOT NULL,
  `outro` varchar(2048) NOT NULL,
  `valid_from` datetime(6) NOT NULL,
  `valid_until` datetime(6) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_questionnaire_vendor_branch_id_0480f1a8_fk_core_vend` (`vendor_branch_id`),
  CONSTRAINT `qa_questionnaire_vendor_branch_id_0480f1a8_fk_core_vend` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_questionnaire`
--

LOCK TABLES `qa_questionnaire` WRITE;
/*!40000 ALTER TABLE `qa_questionnaire` DISABLE KEYS */;
INSERT INTO `qa_questionnaire` VALUES (1,'Test questionnaire','test message','test','2020-03-25 07:42:00.000000','2021-03-25 07:42:44.000000','2019-03-25 07:42:44.041165','2019-06-03 01:08:24.273320',0,1),(2,'Test 2','testing message','testing closing','2019-04-22 05:05:00.000000','2119-04-22 05:05:00.000000','2019-04-22 05:05:52.325810','2019-05-07 08:41:46.201951',0,1),(3,'','','','2019-05-07 04:22:09.000000',NULL,'2019-05-07 04:26:53.593698','2019-05-07 07:15:59.733073',1,1),(4,'','','','2019-05-07 04:22:09.000000',NULL,'2019-05-07 04:27:07.641341','2019-05-07 07:16:03.806902',1,1),(5,'','','','2019-05-06 19:42:55.000000',NULL,'2019-05-07 04:42:56.029270','2019-05-07 07:16:07.612701',1,1),(6,'','','','2019-05-06 19:43:11.000000',NULL,'2019-05-07 04:43:11.669075','2019-05-07 07:16:11.511855',1,1),(7,'','','','2019-05-07 04:43:44.000000',NULL,'2019-05-07 04:43:44.277595','2019-05-07 07:16:15.142369',1,1),(8,'asdsadsadsadasdsadsadasdsadasdsadasdsadasdveeeeeeeeerrrrrhyyyyyy','hi','bye','2019-05-17 01:48:08.000000','2019-05-17 01:48:08.000000','2019-05-17 01:48:08.771697','2019-05-17 01:48:31.974745',0,1),(9,'test3','test3','test3','2029-06-06 07:13:55.000000','2029-06-06 07:13:55.000000','2019-06-06 07:13:55.626414','2019-06-07 07:43:35.459456',0,1),(10,'old draft title','2019-08-29 15:28','2019-08-29 15:28','2019-06-20 04:45:00.000000','2019-08-29 06:28:00.000000','2019-06-20 04:45:39.195992','2019-08-29 06:29:45.215573',0,1),(11,'test234','test','and','2019-08-29 06:28:00.000000','2019-08-29 06:28:00.000000','2019-08-29 06:28:49.018385','2019-08-29 06:28:59.216953',0,1),(12,'sadsadsad','asdsadsa','ads','2019-08-29 06:29:00.000000','2019-08-29 06:28:00.000000','2019-08-29 06:29:04.342324','2019-08-29 06:29:10.747232',0,1),(13,'newest draft','bye','bye','2019-08-29 06:29:00.000000','2019-08-29 06:28:00.000000','2019-08-29 06:29:17.409537','2019-08-29 06:29:31.508714',0,1),(14,'new blank','new blank','and','2029-08-29 06:29:00.000000','2029-08-29 06:29:00.000000','2019-08-29 06:29:51.239654','2019-08-29 06:30:04.699575',0,1),(15,'newer blank','2029-08-29 15:29','and','2029-08-29 06:29:00.000000','2029-08-29 06:29:00.000000','2019-08-29 06:30:18.340687','2019-08-29 06:30:35.675643',0,1),(16,'newsiest bank','2029-08-29 15:29','asdsadasda','2029-08-29 06:29:00.000000','2029-08-29 06:29:00.000000','2019-08-29 06:30:40.646253','2019-08-29 06:30:51.998121',0,1),(17,'newestetst blank 1','3019-08-29 15:45','3019-08-29 15:45','3019-08-29 06:45:00.000000','3019-08-29 06:45:00.000000','2019-08-29 06:45:30.998649','2019-08-29 06:45:46.096565',0,1),(18,'2','and','3019-08-29 15:45','3019-08-29 06:45:00.000000','3019-08-29 06:45:00.000000','2019-08-29 06:47:40.874365','2019-08-29 06:47:50.018334',0,1),(19,'3','3019-08-29 15:45','3019-08-29 15:45','2019-08-29 06:47:00.000000','3019-08-29 06:45:00.000000','2019-08-29 06:47:54.080786','2019-08-29 06:47:59.095014',0,1),(20,'4','3019-08-29 15:45','3019-08-29 15:45','3019-08-29 06:45:00.000000','3019-08-29 06:45:00.000000','2019-08-29 06:48:03.377200','2019-08-29 06:48:16.924643',0,1),(21,'5','3019-08-29 15:45','3019-08-29 15:45','3019-08-29 06:45:00.000000','3019-08-29 06:45:00.000000','2019-08-29 06:48:22.232102','2019-08-29 06:48:30.037999',0,1),(22,'','','','2019-09-11 07:52:00.000000',NULL,'2019-09-11 07:52:06.454946','2019-09-11 07:52:06.454974',0,1),(23,'','','','2020-01-10 06:29:00.000000',NULL,'2020-01-10 06:29:32.144755','2020-01-10 06:29:32.144782',0,1),(24,'','','','2020-01-10 06:30:00.000000',NULL,'2020-01-10 06:30:42.291724','2020-01-10 06:30:42.291776',0,1),(25,'','','','2020-01-10 06:32:00.000000',NULL,'2020-01-10 06:32:32.284811','2020-01-10 06:32:32.284879',0,1),(26,'','','','2020-01-10 06:32:00.000000',NULL,'2020-01-10 06:32:44.762081','2020-01-10 06:32:44.762112',0,1),(27,'','','','2020-01-10 06:32:00.000000',NULL,'2020-01-10 06:32:56.850111','2020-01-10 06:32:56.850163',0,1);
/*!40000 ALTER TABLE `qa_questionnaire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_questionnairequestion`
--

DROP TABLE IF EXISTS `qa_questionnairequestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_questionnairequestion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `display_order` int NOT NULL,
  `required` tinyint(1) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `question_id` int NOT NULL,
  `questionnaire_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_questionnairequestion_question_id_fac2ee19_fk_qa_question_id` (`question_id`),
  KEY `qa_questionnaireques_questionnaire_id_5935de9f_fk_qa_questi` (`questionnaire_id`),
  CONSTRAINT `qa_questionnaireques_questionnaire_id_5935de9f_fk_qa_questi` FOREIGN KEY (`questionnaire_id`) REFERENCES `qa_questionnaire` (`id`),
  CONSTRAINT `qa_questionnairequestion_question_id_fac2ee19_fk_qa_question_id` FOREIGN KEY (`question_id`) REFERENCES `qa_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_questionnairequestion`
--

LOCK TABLES `qa_questionnairequestion` WRITE;
/*!40000 ALTER TABLE `qa_questionnairequestion` DISABLE KEYS */;
INSERT INTO `qa_questionnairequestion` VALUES (1,1,1,'2019-03-25 07:42:44.041165',1,1),(2,2,1,'2019-03-25 07:42:44.041165',2,1),(25,2,1,'2019-04-23 07:27:38.198013',25,2),(26,1,1,'2019-04-23 08:32:15.240219',27,2),(27,3,1,'2019-05-07 08:41:25.196645',29,2),(28,3,1,'2019-05-17 09:16:45.337737',30,1),(29,4,1,'2019-06-03 01:07:41.020991',31,1),(30,5,1,'2019-06-03 01:08:24.323320',32,1),(31,1,1,'2019-06-06 07:14:30.911466',33,9);
/*!40000 ALTER TABLE `qa_questionnairequestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_questionnairetemplate`
--

DROP TABLE IF EXISTS `qa_questionnairetemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_questionnairetemplate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_questionnairetemplate`
--

LOCK TABLES `qa_questionnairetemplate` WRITE;
/*!40000 ALTER TABLE `qa_questionnairetemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_questionnairetemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_questionnairetemplatequestion`
--

DROP TABLE IF EXISTS `qa_questionnairetemplatequestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_questionnairetemplatequestion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `display_order` int NOT NULL,
  `required` tinyint(1) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `question_id` int NOT NULL,
  `questionnaire_template_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_questionnairetemp_question_id_3808736e_fk_qa_questi` (`question_id`),
  KEY `qa_questionnairetemp_questionnaire_templa_46b0b8c9_fk_qa_questi` (`questionnaire_template_id`),
  CONSTRAINT `qa_questionnairetemp_question_id_3808736e_fk_qa_questi` FOREIGN KEY (`question_id`) REFERENCES `qa_question` (`id`),
  CONSTRAINT `qa_questionnairetemp_questionnaire_templa_46b0b8c9_fk_qa_questi` FOREIGN KEY (`questionnaire_template_id`) REFERENCES `qa_questionnairetemplate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_questionnairetemplatequestion`
--

LOCK TABLES `qa_questionnairetemplatequestion` WRITE;
/*!40000 ALTER TABLE `qa_questionnairetemplatequestion` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_questionnairetemplatequestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_questiontype`
--

DROP TABLE IF EXISTS `qa_questiontype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_questiontype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_questiontype`
--

LOCK TABLES `qa_questiontype` WRITE;
/*!40000 ALTER TABLE `qa_questiontype` DISABLE KEYS */;
INSERT INTO `qa_questiontype` VALUES (1,'text','2019-03-05 03:36:15.372277','2019-03-05 03:36:15.372277'),(2,'option','2019-03-05 03:36:15.372277','2019-03-05 03:36:15.372277'),(3,'registration','2019-05-20 07:30:38.322057','2019-05-20 07:30:38.322111'),(4,'multioption','2019-06-20 06:32:22.142500','2019-06-20 06:32:22.142531');
/*!40000 ALTER TABLE `qa_questiontype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_receivinghistory`
--

DROP TABLE IF EXISTS `qa_receivinghistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_receivinghistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `issue_number` varchar(256) DEFAULT NULL,
  `track_number` varchar(256) DEFAULT NULL,
  `scheduled_dt` datetime(6) DEFAULT NULL,
  `stats` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `business_partner_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `memo` longtext,
  PRIMARY KEY (`id`),
  KEY `qa_receivinghistory_business_partner_id_e47030b5_fk_qa_vendor` (`business_partner_id`),
  KEY `qa_receivinghistory_product_id_6d1c54f0_fk_qa_product_id` (`product_id`),
  CONSTRAINT `qa_receivinghistory_business_partner_id_e47030b5_fk_qa_vendor` FOREIGN KEY (`business_partner_id`) REFERENCES `qa_vendorbusinesspartner` (`id`),
  CONSTRAINT `qa_receivinghistory_product_id_6d1c54f0_fk_qa_product_id` FOREIGN KEY (`product_id`) REFERENCES `qa_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_receivinghistory`
--

LOCK TABLES `qa_receivinghistory` WRITE;
/*!40000 ALTER TABLE `qa_receivinghistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_receivinghistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_response`
--

DROP TABLE IF EXISTS `qa_response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_response` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(2048) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `end_user_id` int NOT NULL,
  `end_user_questionnaire_id` int NOT NULL,
  `questionnaire_question_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_response_end_user_id_b7fbba97_fk_core_enduser_id` (`end_user_id`),
  KEY `qa_response_questionnaire_questi_92be0ecc_fk_qa_questi` (`questionnaire_question_id`),
  KEY `qa_response_end_user_questionnai_c1078f5d_fk_qa_enduse` (`end_user_questionnaire_id`),
  CONSTRAINT `qa_response_end_user_id_b7fbba97_fk_core_enduser_id` FOREIGN KEY (`end_user_id`) REFERENCES `core_enduser` (`id`),
  CONSTRAINT `qa_response_end_user_questionnai_c1078f5d_fk_qa_enduse` FOREIGN KEY (`end_user_questionnaire_id`) REFERENCES `qa_enduserquestionnaire` (`id`),
  CONSTRAINT `qa_response_questionnaire_questi_92be0ecc_fk_qa_questi` FOREIGN KEY (`questionnaire_question_id`) REFERENCES `qa_questionnairequestion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_response`
--

LOCK TABLES `qa_response` WRITE;
/*!40000 ALTER TABLE `qa_response` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_senbayuser`
--

DROP TABLE IF EXISTS `qa_senbayuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_senbayuser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jwt_token` varchar(1024) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_senbayuser_vendor_user_id_f43cf5e7_fk_qa_vendoruser_id` (`vendor_user_id`),
  CONSTRAINT `qa_senbayuser_vendor_user_id_f43cf5e7_fk_qa_vendoruser_id` FOREIGN KEY (`vendor_user_id`) REFERENCES `qa_vendoruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_senbayuser`
--

LOCK TABLES `qa_senbayuser` WRITE;
/*!40000 ALTER TABLE `qa_senbayuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_senbayuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_service`
--

DROP TABLE IF EXISTS `qa_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_service` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cd` varchar(64) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_service`
--

LOCK TABLES `qa_service` WRITE;
/*!40000 ALTER TABLE `qa_service` DISABLE KEYS */;
INSERT INTO `qa_service` VALUES (1,'00001','QA','2019-03-05 02:51:48.312286','2019-03-05 02:51:48.312316',0);
/*!40000 ALTER TABLE `qa_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_shippinghistory`
--

DROP TABLE IF EXISTS `qa_shippinghistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_shippinghistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `issue_number` varchar(256) DEFAULT NULL,
  `track_number` varchar(256) DEFAULT NULL,
  `scheduled_dt` datetime(6) DEFAULT NULL,
  `stats` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `business_partner_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `memo` longtext,
  PRIMARY KEY (`id`),
  KEY `qa_shippinghistory_business_partner_id_b709b60a_fk_qa_vendor` (`business_partner_id`),
  KEY `qa_shippinghistory_product_id_81d8f2dc_fk_qa_product_id` (`product_id`),
  CONSTRAINT `qa_shippinghistory_business_partner_id_b709b60a_fk_qa_vendor` FOREIGN KEY (`business_partner_id`) REFERENCES `qa_vendorbusinesspartner` (`id`),
  CONSTRAINT `qa_shippinghistory_product_id_81d8f2dc_fk_qa_product_id` FOREIGN KEY (`product_id`) REFERENCES `qa_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_shippinghistory`
--

LOCK TABLES `qa_shippinghistory` WRITE;
/*!40000 ALTER TABLE `qa_shippinghistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_shippinghistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_stock`
--

DROP TABLE IF EXISTS `qa_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_stock` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int DEFAULT NULL,
  `memo` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_stock_product_id_207cbacb_fk_qa_product_id` (`product_id`),
  CONSTRAINT `qa_stock_product_id_207cbacb_fk_qa_product_id` FOREIGN KEY (`product_id`) REFERENCES `qa_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_stock`
--

LOCK TABLES `qa_stock` WRITE;
/*!40000 ALTER TABLE `qa_stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_stockspace`
--

DROP TABLE IF EXISTS `qa_stockspace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_stockspace` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `code` varchar(256) DEFAULT NULL,
  `memo` longtext,
  `display_order_num` int DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_stockspace_vendor_id_5dd9767c_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `qa_stockspace_vendor_id_5dd9767c_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_stockspace`
--

LOCK TABLES `qa_stockspace` WRITE;
/*!40000 ALTER TABLE `qa_stockspace` DISABLE KEYS */;
INSERT INTO `qa_stockspace` VALUES (1,'space 1',NULL,'',NULL,'2019-06-26 05:41:40.330481','2019-06-26 05:41:40.330511',0,1);
/*!40000 ALTER TABLE `qa_stockspace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_vendorbusinesspartner`
--

DROP TABLE IF EXISTS `qa_vendorbusinesspartner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_vendorbusinesspartner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `short_name` varchar(256) DEFAULT NULL,
  `name_kana` varchar(256) DEFAULT NULL,
  `email` varchar(2048) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  `prefecture` varchar(32) DEFAULT NULL,
  `address1` varchar(256) DEFAULT NULL,
  `address2` varchar(256) DEFAULT NULL,
  `tel1` varchar(32) DEFAULT NULL,
  `tel2` varchar(32) DEFAULT NULL,
  `fax` varchar(32) DEFAULT NULL,
  `memo` longtext,
  `attribute_json` longtext,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_id` int DEFAULT NULL,
  `tag_csv` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_vendorbusinesspartner_vendor_id_ba76aa06_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `qa_vendorbusinesspartner_vendor_id_ba76aa06_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_vendorbusinesspartner`
--

LOCK TABLES `qa_vendorbusinesspartner` WRITE;
/*!40000 ALTER TABLE `qa_vendorbusinesspartner` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_vendorbusinesspartner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_vendorbusinesspartnertag`
--

DROP TABLE IF EXISTS `qa_vendorbusinesspartnertag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_vendorbusinesspartnertag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `vendor_id` int DEFAULT NULL,
  `cd` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_vendorbusinesspartnertag_vendor_id_aec7e6a8_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `qa_vendorbusinesspartnertag_vendor_id_aec7e6a8_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_vendorbusinesspartnertag`
--

LOCK TABLES `qa_vendorbusinesspartnertag` WRITE;
/*!40000 ALTER TABLE `qa_vendorbusinesspartnertag` DISABLE KEYS */;
/*!40000 ALTER TABLE `qa_vendorbusinesspartnertag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_vendorplan`
--

DROP TABLE IF EXISTS `qa_vendorplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_vendorplan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `plan_id` int DEFAULT NULL,
  `vendor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_vendorplan_plan_id_66c26865_fk_qa_plan_id` (`plan_id`),
  KEY `qa_vendorplan_vendor_id_40f6c420_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `qa_vendorplan_plan_id_66c26865_fk_qa_plan_id` FOREIGN KEY (`plan_id`) REFERENCES `qa_plan` (`id`),
  CONSTRAINT `qa_vendorplan_vendor_id_40f6c420_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_vendorplan`
--

LOCK TABLES `qa_vendorplan` WRITE;
/*!40000 ALTER TABLE `qa_vendorplan` DISABLE KEYS */;
INSERT INTO `qa_vendorplan` VALUES (1,'2019-03-05 03:36:15.372248','2019-03-05 03:36:15.372277',0,1,1),(2,NULL,NULL,0,1,10),(4,'2019-03-07 08:13:13.205915','2019-03-07 08:13:13.205935',0,1,12),(6,'2019-03-07 08:18:15.454255','2019-03-07 08:18:15.454277',0,1,15),(7,'2019-05-08 06:03:40.221277','2019-05-08 06:03:40.221312',0,1,16),(9,'2019-05-09 02:07:36.630801','2019-05-09 02:07:36.630893',0,1,18),(10,'2019-05-09 02:53:30.051308','2019-05-09 02:53:30.051401',0,1,19),(11,'2019-07-10 05:51:32.419359','2019-07-10 05:51:32.419390',0,1,20),(12,'2019-07-11 07:15:06.902461','2019-07-11 07:15:06.902491',0,1,21);
/*!40000 ALTER TABLE `qa_vendorplan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_vendorservice`
--

DROP TABLE IF EXISTS `qa_vendorservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_vendorservice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `service_id` int DEFAULT NULL,
  `vendor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qa_vendorservice_service_id_671ac1ff_fk_qa_service_id` (`service_id`),
  KEY `qa_vendorservice_vendor_id_d205510f_fk_core_vendor_id` (`vendor_id`),
  CONSTRAINT `qa_vendorservice_service_id_671ac1ff_fk_qa_service_id` FOREIGN KEY (`service_id`) REFERENCES `qa_service` (`id`),
  CONSTRAINT `qa_vendorservice_vendor_id_d205510f_fk_core_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `core_vendor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_vendorservice`
--

LOCK TABLES `qa_vendorservice` WRITE;
/*!40000 ALTER TABLE `qa_vendorservice` DISABLE KEYS */;
INSERT INTO `qa_vendorservice` VALUES (3,'2019-03-05 03:31:49.147883','2019-03-05 03:31:49.147914',0,1,1),(4,NULL,NULL,0,1,10),(6,'2019-03-07 08:13:13.204034','2019-03-07 08:13:13.204055',0,1,12),(8,'2019-03-07 08:18:15.452322','2019-03-07 08:18:15.452344',0,1,15),(9,'2019-05-08 06:03:40.212391','2019-05-08 06:03:40.212422',0,1,16),(11,'2019-05-09 02:07:36.621531','2019-05-09 02:07:36.621636',0,1,18),(12,'2019-05-09 02:53:30.040812','2019-05-09 02:53:30.040901',0,1,19),(13,'2019-07-10 05:51:32.404261','2019-07-10 05:51:32.404299',0,1,20),(14,'2019-07-11 07:15:06.888838','2019-07-11 07:15:06.888865',0,1,21);
/*!40000 ALTER TABLE `qa_vendorservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qa_vendoruser`
--

DROP TABLE IF EXISTS `qa_vendoruser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qa_vendoruser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(64) DEFAULT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `last_name_kana` varchar(64) DEFAULT NULL,
  `first_name_kana` varchar(64) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `regist_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `auth_user_id` int DEFAULT NULL,
  `vendor_branch_id` int DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `tel` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `qa_vendoruser_auth_user_id_8c1867ea_fk_auth_user_id` (`auth_user_id`),
  KEY `qa_vendoruser_vendor_branch_id_3453f08d_fk_core_vendorbranch_id` (`vendor_branch_id`),
  CONSTRAINT `qa_vendoruser_auth_user_id_8c1867ea_fk_auth_user_id` FOREIGN KEY (`auth_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `qa_vendoruser_vendor_branch_id_3453f08d_fk_core_vendorbranch_id` FOREIGN KEY (`vendor_branch_id`) REFERENCES `core_vendorbranch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qa_vendoruser`
--

LOCK TABLES `qa_vendoruser` WRITE;
/*!40000 ALTER TABLE `qa_vendoruser` DISABLE KEYS */;
INSERT INTO `qa_vendoruser` VALUES (1,'test','tester','','','test01@test.com','2019-03-05 03:37:07.340416','2019-06-26 03:32:17.110540',0,7,1,1,''),(2,NULL,NULL,NULL,NULL,'test02@test.com','2019-03-07 07:01:42.269198','2019-03-07 07:01:42.269225',0,8,1,1,NULL),(3,NULL,NULL,NULL,NULL,'test99@test.com','2019-03-07 07:16:09.277468','2019-03-07 07:16:09.277500',0,139,10,1,NULL);
/*!40000 ALTER TABLE `qa_vendoruser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggit_tag`
--

DROP TABLE IF EXISTS `taggit_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggit_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggit_tag`
--

LOCK TABLES `taggit_tag` WRITE;
/*!40000 ALTER TABLE `taggit_tag` DISABLE KEYS */;
INSERT INTO `taggit_tag` VALUES (1,'TAG0001','tag0001'),(2,'TAG0002','tag0002'),(3,'1-1','1-1'),(4,'1-4','1-4'),(5,'1-5','1-5'),(6,'1-6','1-6'),(7,'1-7','1-7'),(8,'1-8','1-8');
/*!40000 ALTER TABLE `taggit_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggit_taggeditem`
--

DROP TABLE IF EXISTS `taggit_taggeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggit_taggeditem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `object_id` int NOT NULL,
  `content_type_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uniq` (`content_type_id`,`object_id`,`tag_id`),
  KEY `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` (`tag_id`),
  KEY `taggit_taggeditem_object_id_e2d7d1df` (`object_id`),
  KEY `taggit_taggeditem_content_type_id_object_id_196cc965_idx` (`content_type_id`,`object_id`),
  CONSTRAINT `taggit_taggeditem_content_type_id_9957a03c_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggit_taggeditem`
--

LOCK TABLES `taggit_taggeditem` WRITE;
/*!40000 ALTER TABLE `taggit_taggeditem` DISABLE KEYS */;
INSERT INTO `taggit_taggeditem` VALUES (80,5,12,1),(79,5,12,8),(22,6,12,2),(35,7,12,1),(36,7,12,2),(37,7,12,4),(38,7,12,5),(39,7,12,7),(40,7,12,8),(77,8,12,4),(78,8,12,8),(81,12,12,8);
/*!40000 ALTER TABLE `taggit_taggeditem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-21 14:07:10
