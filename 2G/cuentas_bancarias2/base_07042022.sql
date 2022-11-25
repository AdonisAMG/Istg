-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.5.32 - MySQL Community Server (GPL)
-- SO del servidor:              Win32
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para cajero_electronico
CREATE DATABASE IF NOT EXISTS `cajero_electronico` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cajero_electronico`;

-- Volcando estructura para tabla cajero_electronico.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `cli_id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(20) NOT NULL,
  `clave` int(11) NOT NULL DEFAULT '0',
  `cli_correo` varchar(50) NOT NULL,
  `cli_cedula` varchar(12) NOT NULL,
  `cli_celular` varchar(12) NOT NULL,
  `cli_apellidos` varchar(50) NOT NULL,
  `cli_nombres` varchar(50) NOT NULL,
  `cli_fecha_nac` datetime NOT NULL,
  `cli_estado_civil` varchar(20) NOT NULL,
  `cli_direccion` varchar(200) NOT NULL,
  `cli_nombres_cont` varchar(100) NOT NULL,
  `cli_tlf_cont` varchar(30) NOT NULL,
  `cli_parentesco_cont` varchar(30) NOT NULL,
  `cli_calle_princ` varchar(100) NOT NULL,
  `cli_calle_secn` varchar(100) NOT NULL,
  `cli_num_dom` varchar(5) NOT NULL,
  `cli_tlf_dom` varchar(30) NOT NULL,
  `cli_referencia_dom` varchar(200) NOT NULL,
  `cli_estado` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`cli_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla cajero_electronico.clientes: ~24 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`cli_id`, `usuario`, `clave`, `cli_correo`, `cli_cedula`, `cli_celular`, `cli_apellidos`, `cli_nombres`, `cli_fecha_nac`, `cli_estado_civil`, `cli_direccion`, `cli_nombres_cont`, `cli_tlf_cont`, `cli_parentesco_cont`, `cli_calle_princ`, `cli_calle_secn`, `cli_num_dom`, `cli_tlf_dom`, `cli_referencia_dom`, `cli_estado`) VALUES
	(5, 'juan', 1234, 'juan@ccc.com', '09129', '09754548', 'salazar', 'juan', '0000-00-00 00:00:00', '', 'xxxx', '', '0990', '', '', '', '', '', '', b'1'),
	(6, '', 0, 'juan123@gmail.com.ec', '09121212', '093231212', 'jimenez flores', 'juan fernando', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(7, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(8, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(9, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(10, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(11, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(12, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(13, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 01:45:59', '', '', '', '', '', '', '', '', '', '', b'0'),
	(14, '', 0, 'juan1@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(15, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(16, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(17, '', 0, 'qwqw', 'qwqw', 'qwqw', 'wewe', 'wewe', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(18, '', 0, 'qwqw', 'qwqw', 'qwqw', 'wewe', 'wewe', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(19, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(20, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(21, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(22, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(23, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(24, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(25, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(26, '', 0, 'juan12345@gmail.com.ec', '0919653532', '0990154547', 'jimenez calderon', 'juan fernando', '2022-04-05 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(27, '', 0, 'juan', '2323', 'ew23223', '21334', 'jaime', '1977-07-16 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0'),
	(28, '', 0, 'juanga', '0954545', '09445454', 'mendez', 'wewewewe', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', '', '', b'0');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla cajero_electronico.cuentas_bancarias
CREATE TABLE IF NOT EXISTS `cuentas_bancarias` (
  `cta_id` int(11) NOT NULL AUTO_INCREMENT,
  `cli_id` int(11) DEFAULT NULL,
  `cta_numero` varchar(10) DEFAULT NULL,
  `cta_saldo` float DEFAULT NULL,
  `cta_tipo` varchar(2) DEFAULT NULL,
  `cta_clave` varchar(6) DEFAULT NULL,
  `cta_estado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`cta_id`) USING BTREE,
  KEY `FK_cuentas_bancarias_clientes` (`cli_id`),
  CONSTRAINT `FK_cuentas_bancarias_clientes` FOREIGN KEY (`cli_id`) REFERENCES `clientes` (`cli_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla cajero_electronico.cuentas_bancarias: ~18 rows (aproximadamente)
/*!40000 ALTER TABLE `cuentas_bancarias` DISABLE KEYS */;
INSERT INTO `cuentas_bancarias` (`cta_id`, `cli_id`, `cta_numero`, `cta_saldo`, `cta_tipo`, `cta_clave`, `cta_estado`) VALUES
	(1, 5, '0902', 0, 'A', '1234', b'1'),
	(2, 5, '0902', 0, 'A', '1234', b'1'),
	(3, 5, '0902', 0, 'A', '1234', b'1'),
	(4, 5, '0902', 0, 'A', '1234', b'1'),
	(5, 5, '0902', 0, 'A', '1234', b'1'),
	(6, 5, '0902', 0, 'A', '1234', b'1'),
	(7, 5, '0902', 0, 'A', '1234', b'1'),
	(8, 5, '0902', 0, 'A', '1234', b'1'),
	(9, 5, '0902', 0, 'A', '1234', b'1'),
	(10, 5, '0902', 0, 'A', '1234', b'1'),
	(11, 5, '0902', 0, 'A', '1234', b'1'),
	(12, 5, '0902', 0, 'A', '1234', b'1'),
	(13, 5, '0902', 0, 'A', '1234', b'1'),
	(14, 5, '0902', 0, 'A', '1234', b'1'),
	(15, 5, '090009', 0, 'A', '1234', b'1'),
	(16, 5, '090010', 0, 'A', '1234', b'1'),
	(17, 5, '0902', 0, 'A', '1234', b'1'),
	(18, 5, '0902', 0, 'A', '1234', b'1');
/*!40000 ALTER TABLE `cuentas_bancarias` ENABLE KEYS */;

-- Volcando estructura para tabla cajero_electronico.movimientos
CREATE TABLE IF NOT EXISTS `movimientos` (
  `mov_id` int(11) NOT NULL,
  `cta_id` int(11) DEFAULT NULL,
  `mov_fecha` datetime DEFAULT NULL,
  `mov_monto` float DEFAULT NULL,
  `mov_saldo` float DEFAULT NULL,
  `mov_estado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`mov_id`),
  KEY `FK_movimientos_cuentas_bancarias` (`cta_id`),
  CONSTRAINT `FK_movimientos_cuentas_bancarias` FOREIGN KEY (`cta_id`) REFERENCES `cuentas_bancarias` (`cta_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

SELECT * from cuentas_bancarias;
ALTER TABLE DROP FOREIGN KEY FK_movimientos_cuentas_bancarias;

ALTER TABLE movimientos ADD COLUMN cta_id int(11) FOREIGN KEY (`cta_id`) REFERENCES `cuentas_bancarias` (`cta_id`)
        
		
		
 -- ALTER TABLE movimientos  DROP FOREIGN KEY FK_movimientos_cuentas_bancarias;
 -- TRUNCATE TABLE cuentas_bancarias;
 
 
ALTER TABLE movimientos ADD COLUMN cta_id int(11);
ALTER TABLE movimientos ADD constraint FK_movimientos_cuentas_bancarias FOREIGN KEY (cta_id) REFERENCES cuentas_bancarias(cta_id);

-- Volcando datos para la tabla cajero_electronico.movimientos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `movimientos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

https://www.google.com/settings/security/lesssecureapps