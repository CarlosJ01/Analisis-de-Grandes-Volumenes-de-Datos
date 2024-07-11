/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 10.5.4-MariaDB : Database - macave
*********************************************************************
*/
DROP DATABASE IF EXISTS `macave`;

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`macave` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `macave`;

/*Table structure for table `equipos` */

DROP TABLE IF EXISTS `equipos`;

CREATE TABLE `equipos` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `grupo` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `logo` text COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Table structure for table `partidos` */

DROP TABLE IF EXISTS `partidos`;

CREATE TABLE `partidos` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `id_equipo_1` bigint(20) unsigned NOT NULL,
  `goles_1` smallint(6) DEFAULT NULL,
  `id_equipo_2` bigint(20) unsigned NOT NULL,
  `goles_2` smallint(6) DEFAULT NULL,
  `tipo` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dia` date NOT NULL,
  `jugado` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `partidos_id_equipo_1_foreign` (`id_equipo_1`),
  KEY `partidos_id_equipo_2_foreign` (`id_equipo_2`),
  CONSTRAINT `partidos_id_equipo_1_foreign` FOREIGN KEY (`id_equipo_1`) REFERENCES `equipos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `partidos_id_equipo_2_foreign` FOREIGN KEY (`id_equipo_2`) REFERENCES `equipos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
