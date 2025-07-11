-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Lug 11, 2025 alle 23:22
-- Versione del server: 10.6.21-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ristomensa`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add dipendente', 7, 'add_dipendente'),
(26, 'Can change dipendente', 7, 'change_dipendente'),
(27, 'Can delete dipendente', 7, 'delete_dipendente'),
(28, 'Can view dipendente', 7, 'view_dipendente'),
(29, 'Can add responsabile', 8, 'add_responsabile'),
(30, 'Can change responsabile', 8, 'change_responsabile'),
(31, 'Can delete responsabile', 8, 'delete_responsabile'),
(32, 'Can view responsabile', 8, 'view_responsabile'),
(33, 'Can add azienda', 9, 'add_azienda'),
(34, 'Can change azienda', 9, 'change_azienda'),
(35, 'Can delete azienda', 9, 'delete_azienda'),
(36, 'Can view azienda', 9, 'view_azienda'),
(37, 'Can add struttura', 10, 'add_struttura'),
(38, 'Can change struttura', 10, 'change_struttura'),
(39, 'Can delete struttura', 10, 'delete_struttura'),
(40, 'Can view struttura', 10, 'view_struttura'),
(41, 'Can add tavolo', 11, 'add_tavolo'),
(42, 'Can change tavolo', 11, 'change_tavolo'),
(43, 'Can delete tavolo', 11, 'delete_tavolo'),
(44, 'Can view tavolo', 11, 'view_tavolo'),
(45, 'Can add amministratore', 12, 'add_amministratore'),
(46, 'Can change amministratore', 12, 'change_amministratore'),
(47, 'Can delete amministratore', 12, 'delete_amministratore'),
(48, 'Can view amministratore', 12, 'view_amministratore'),
(49, 'Can add associazione', 13, 'add_associazione'),
(50, 'Can change associazione', 13, 'change_associazione'),
(51, 'Can delete associazione', 13, 'delete_associazione'),
(52, 'Can view associazione', 13, 'view_associazione'),
(53, 'Can add prenotazione', 14, 'add_prenotazione'),
(54, 'Can change prenotazione', 14, 'change_prenotazione'),
(55, 'Can delete prenotazione', 14, 'delete_prenotazione'),
(56, 'Can view prenotazione', 14, 'view_prenotazione'),
(57, 'Can add piatto', 15, 'add_piatto'),
(58, 'Can change piatto', 15, 'change_piatto'),
(59, 'Can delete piatto', 15, 'delete_piatto'),
(60, 'Can view piatto', 15, 'view_piatto');

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(12, 'mensa', 'amministratore'),
(13, 'mensa', 'associazione'),
(9, 'mensa', 'azienda'),
(7, 'mensa', 'dipendente'),
(15, 'mensa', 'piatto'),
(14, 'mensa', 'prenotazione'),
(8, 'mensa', 'responsabile'),
(10, 'mensa', 'struttura'),
(11, 'mensa', 'tavolo'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-07-11 21:21:09.913278'),
(2, 'auth', '0001_initial', '2025-07-11 21:21:10.096891'),
(3, 'admin', '0001_initial', '2025-07-11 21:21:10.145011'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-07-11 21:21:10.149741'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-07-11 21:21:10.154470'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-07-11 21:21:10.183932'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-07-11 21:21:10.203527'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-07-11 21:21:10.215888'),
(9, 'auth', '0004_alter_user_username_opts', '2025-07-11 21:21:10.220746'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-07-11 21:21:10.238790'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-07-11 21:21:10.240175'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-07-11 21:21:10.245265'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-07-11 21:21:10.257780'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-07-11 21:21:10.269457'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-07-11 21:21:10.285412'),
(16, 'auth', '0011_update_proxy_permissions', '2025-07-11 21:21:10.291454'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-07-11 21:21:10.308205'),
(18, 'sessions', '0001_initial', '2025-07-11 21:21:10.326406'),
(19, 'mensa', '0001_initial', '2025-07-11 21:21:59.562081');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('egag0w94f4z64s8qmpckwjgueezn0ae9', 'eyJ1c2VyX2VtYWlsIjoiZmVkZXJpY28uc3RydXR0dXJhMkBleGFtcGxlLmNvbSIsInJ1b2xvIjoiRGlwZW5kZW50ZSIsImlkX3N0cnV0dHVyYSI6Mn0:1uaLCf:hw-Hywc3QkqCTP9Lv2TZ-dxLlLhUOZE2hlMAfDuguhw', '2025-07-11 21:32:45.190665');

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_amministratore`
--

CREATE TABLE `mensa_amministratore` (
  `id_amministratore` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` longtext NOT NULL,
  `id_azienda_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_associazione`
--

CREATE TABLE `mensa_associazione` (
  `id` bigint(20) NOT NULL,
  `quantita` int(10) UNSIGNED NOT NULL CHECK (`quantita` >= 0),
  `piatto_id` int(11) NOT NULL,
  `prenotazione_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_azienda`
--

CREATE TABLE `mensa_azienda` (
  `id_azienda` int(11) NOT NULL,
  `ragione_sociale` longtext NOT NULL,
  `partita_iva` longtext NOT NULL,
  `indirizzo` longtext NOT NULL,
  `id_struttura_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa_azienda`
--

INSERT INTO `mensa_azienda` (`id_azienda`, `ragione_sociale`, `partita_iva`, `indirizzo`, `id_struttura_id`) VALUES
(1, 'Tech Solutions S.p.A.', 'IT12345678901', 'Via Roma 12, Milano', 1),
(2, 'Green Energy S.r.l.', 'IT98765432109', 'Corso Torino 45, Torino', 2),
(3, 'Food & Co.', 'IT56789012345', 'Viale Europa 88, Firenze', 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_dipendente`
--

CREATE TABLE `mensa_dipendente` (
  `id_dipendente` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cognome` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(32) NOT NULL,
  `id_azienda_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa_dipendente`
--

INSERT INTO `mensa_dipendente` (`id_dipendente`, `nome`, `cognome`, `email`, `password`, `id_azienda_id`) VALUES
(1, 'Alice', 'Rossi', 'alice.struttura1@example.com', '3ce98305181b1bac59d024a49b0ffd73', 1),
(2, 'Bob', 'Verdi', 'bob.struttura1@example.com', '3ce98305181b1bac59d024a49b0ffd73', 1),
(3, 'Carla', 'Neri', 'carla.struttura1@example.com', '3ce98305181b1bac59d024a49b0ffd73', 1),
(4, 'Davide', 'Bianchi', 'davide.struttura1@example.com', '3ce98305181b1bac59d024a49b0ffd73', 1),
(5, 'Elena', 'Gialli', 'elena.struttura1@example.com', '3ce98305181b1bac59d024a49b0ffd73', 1),
(6, 'Federico', 'Blu', 'federico.struttura2@example.com', '3ce98305181b1bac59d024a49b0ffd73', 2),
(7, 'Giulia', 'Rosa', 'giulia.struttura2@example.com', '3ce98305181b1bac59d024a49b0ffd73', 2),
(8, 'Henry', 'Moro', 'henry.struttura2@example.com', '3ce98305181b1bac59d024a49b0ffd73', 2),
(9, 'Irene', 'Azzurri', 'irene.struttura2@example.com', '3ce98305181b1bac59d024a49b0ffd73', 2),
(10, 'Luca', 'Celeste', 'luca.struttura2@example.com', '3ce98305181b1bac59d024a49b0ffd73', 2),
(11, 'Mario', 'Viola', 'mario.struttura3@example.com', '3ce98305181b1bac59d024a49b0ffd73', 3),
(12, 'Nadia', 'Argento', 'nadia.struttura3@example.com', '3ce98305181b1bac59d024a49b0ffd73', 3),
(13, 'Oscar', 'Bronzo', 'oscar.struttura3@example.com', '3ce98305181b1bac59d024a49b0ffd73', 3),
(14, 'Paola', 'Corallo', 'paola.struttura3@example.com', '3ce98305181b1bac59d024a49b0ffd73', 3),
(15, 'Quinto', 'Sabbia', 'quinto.struttura3@example.com', '3ce98305181b1bac59d024a49b0ffd73', 3);

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_piatto`
--

CREATE TABLE `mensa_piatto` (
  `id_piatto` int(11) NOT NULL,
  `nome` varchar(80) NOT NULL,
  `descrizione` varchar(255) DEFAULT NULL,
  `prezzo` decimal(10,2) NOT NULL,
  `tipo_cottura` enum('breve','medio','lungo') DEFAULT NULL,
  `tipo_piatto` enum('primo piatto','secondo piatto','frutta','dessert','bevande') NOT NULL,
  `contorno` enum('patate al forno','verdure grigliate','insalata mista') DEFAULT NULL,
  `origine_frutta` enum('locale','esterna','biologica','convenzionale') DEFAULT NULL,
  `tipo_dessert` enum('gelato','torta','budino','semifreddo') DEFAULT NULL,
  `alcolica` tinyint(1) NOT NULL,
  `id_responsabile_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa_piatto`
--

INSERT INTO `mensa_piatto` (`id_piatto`, `nome`, `descrizione`, `prezzo`, `tipo_cottura`, `tipo_piatto`, `contorno`, `origine_frutta`, `tipo_dessert`, `alcolica`, `id_responsabile_id`) VALUES
(1, 'Spaghetti R1A', 'Pasta con pomodoro fresco', 4.50, 'breve', 'primo piatto', 'patate al forno', NULL, NULL, 0, 1),
(2, 'Risotto R1B', 'Riso con funghi porcini', 5.20, 'lungo', 'primo piatto', 'verdure grigliate', NULL, NULL, 0, 1),
(3, 'Penne R1C', 'Pasta piccante all’arrabbiata', 4.80, 'medio', 'primo piatto', 'insalata mista', NULL, NULL, 0, 1),
(4, 'Pollo R1A', 'Coscia di pollo arrosto', 6.00, 'lungo', 'secondo piatto', 'patate al forno', NULL, NULL, 0, 1),
(5, 'Merluzzo R1B', 'Merluzzo con limone', 6.30, 'medio', 'secondo piatto', 'insalata mista', NULL, NULL, 0, 1),
(6, 'Tofu R1C', 'Tofu saltato con verdure', 5.00, 'breve', 'secondo piatto', 'verdure grigliate', NULL, NULL, 0, 1),
(7, 'Mela R1A', 'Mela biologica locale', 1.00, NULL, 'frutta', NULL, 'biologica', NULL, 0, 1),
(8, 'Banana R1B', 'Banana estera', 1.20, NULL, 'frutta', NULL, 'esterna', NULL, 0, 1),
(9, 'Pera R1C', 'Pera dolce', 1.10, NULL, 'frutta', NULL, 'locale', NULL, 0, 1),
(10, 'Tiramisù R1A', 'Dolce al caffè', 2.80, NULL, 'dessert', NULL, NULL, 'torta', 0, 1),
(11, 'Budino R1B', 'Budino al cioccolato', 2.40, NULL, 'dessert', NULL, NULL, 'budino', 0, 1),
(12, 'Gelato R1C', 'Gelato alla fragola', 2.20, NULL, 'dessert', NULL, NULL, 'gelato', 0, 1),
(13, 'Acqua R1A', 'Bottiglia naturale 0.5L', 0.50, NULL, 'bevande', NULL, NULL, NULL, 0, 1),
(14, 'Vino R1B', 'Bicchiere di vino rosso', 2.00, NULL, 'bevande', NULL, NULL, NULL, 1, 1),
(15, 'Succo R1C', 'Succo ACE', 1.60, NULL, 'bevande', NULL, NULL, NULL, 0, 1),
(16, 'Spaghetti R2A', 'Pasta con basilico', 4.60, 'breve', 'primo piatto', 'patate al forno', NULL, NULL, 0, 2),
(17, 'Risotto R2B', 'Risotto agli asparagi', 5.40, 'lungo', 'primo piatto', 'verdure grigliate', NULL, NULL, 0, 2),
(18, 'Penne R2C', 'Pasta al pesto', 4.70, 'medio', 'primo piatto', 'insalata mista', NULL, NULL, 0, 2),
(19, 'Pollo R2A', 'Pollo alla griglia', 6.10, 'lungo', 'secondo piatto', 'patate al forno', NULL, NULL, 0, 2),
(20, 'Trota R2B', 'Trota salmonata', 6.40, 'medio', 'secondo piatto', 'insalata mista', NULL, NULL, 0, 2),
(21, 'Tempeh R2C', 'Tempeh speziato', 5.10, 'breve', 'secondo piatto', 'verdure grigliate', NULL, NULL, 0, 2),
(22, 'Mela R2A', 'Mela Fuji', 1.00, NULL, 'frutta', NULL, 'convenzionale', NULL, 0, 2),
(23, 'Banana R2B', 'Banana biologica', 1.30, NULL, 'frutta', NULL, 'biologica', NULL, 0, 2),
(24, 'Pera R2C', 'Pera estera', 1.15, NULL, 'frutta', NULL, 'esterna', NULL, 0, 2),
(25, 'Tiramisù R2A', 'Tiramisù alla fragola', 2.90, NULL, 'dessert', NULL, NULL, 'torta', 0, 2),
(26, 'Budino R2B', 'Budino vaniglia', 2.50, NULL, 'dessert', NULL, NULL, 'budino', 0, 2),
(27, 'Gelato R2C', 'Gelato al pistacchio', 2.30, NULL, 'dessert', NULL, NULL, 'gelato', 0, 2),
(28, 'Acqua R2A', 'Bottiglia frizzante', 0.60, NULL, 'bevande', NULL, NULL, NULL, 0, 2),
(29, 'Vino R2B', 'Vino bianco secco', 2.10, NULL, 'bevande', NULL, NULL, NULL, 1, 2),
(30, 'Succo R2C', 'Succo mela', 1.50, NULL, 'bevande', NULL, NULL, NULL, 0, 2),
(31, 'Spaghetti R2A', 'Pasta con basilico', 4.60, 'breve', 'primo piatto', 'patate al forno', NULL, NULL, 0, 3),
(32, 'Risotto R2B', 'Risotto agli asparagi', 5.40, 'lungo', 'primo piatto', 'verdure grigliate', NULL, NULL, 0, 3),
(33, 'Penne R2C', 'Pasta al pesto', 4.70, 'medio', 'primo piatto', 'insalata mista', NULL, NULL, 0, 3),
(34, 'Pollo R2A', 'Pollo alla griglia', 6.10, 'lungo', 'secondo piatto', 'patate al forno', NULL, NULL, 0, 3),
(35, 'Trota R2B', 'Trota salmonata', 6.40, 'medio', 'secondo piatto', 'insalata mista', NULL, NULL, 0, 3),
(36, 'Tempeh R2C', 'Tempeh speziato', 5.10, 'breve', 'secondo piatto', 'verdure grigliate', NULL, NULL, 0, 3),
(37, 'Mela R2A', 'Mela Fuji', 1.00, NULL, 'frutta', NULL, 'convenzionale', NULL, 0, 3),
(38, 'Banana R2B', 'Banana biologica', 1.30, NULL, 'frutta', NULL, 'biologica', NULL, 0, 3),
(39, 'Pera R2C', 'Pera estera', 1.15, NULL, 'frutta', NULL, 'esterna', NULL, 0, 3),
(40, 'Tiramisù R2A', 'Tiramisù alla fragola', 2.90, NULL, 'dessert', NULL, NULL, 'torta', 0, 3),
(41, 'Budino R2B', 'Budino vaniglia', 2.50, NULL, 'dessert', NULL, NULL, 'budino', 0, 3),
(42, 'Gelato R2C', 'Gelato al pistacchio', 2.30, NULL, 'dessert', NULL, NULL, 'gelato', 0, 3),
(43, 'Acqua R2A', 'Bottiglia frizzante', 0.60, NULL, 'bevande', NULL, NULL, NULL, 0, 3),
(44, 'Vino R2B', 'Vino bianco secco', 2.10, NULL, 'bevande', NULL, NULL, NULL, 1, 3),
(45, 'Succo R2C', 'Succo mela', 1.50, NULL, 'bevande', NULL, NULL, NULL, 0, 3);

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_prenotazione`
--

CREATE TABLE `mensa_prenotazione` (
  `id_prenotazione` int(11) NOT NULL,
  `data_prenotazione` date NOT NULL,
  `fascia_oraria` varchar(20) NOT NULL,
  `stato` enum('in attesa','annullata','confermata') NOT NULL,
  `totale_prezzo` decimal(4,2) DEFAULT NULL,
  `id_dipendente_id` int(11) NOT NULL,
  `id_tavolo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_responsabile`
--

CREATE TABLE `mensa_responsabile` (
  `id_responsabile` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(32) NOT NULL,
  `id_struttura_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa_responsabile`
--

INSERT INTO `mensa_responsabile` (`id_responsabile`, `email`, `password`, `id_struttura_id`) VALUES
(1, 'responsabile.1a@struttura1.it', '21232f297a57a5a743894a0e4a801fc3', 1),
(2, 'responsabile.2a@struttura2.it', '21232f297a57a5a743894a0e4a801fc3', 2),
(3, 'responsabile.3a@struttura3.it', '21232f297a57a5a743894a0e4a801fc3', 3);

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_struttura`
--

CREATE TABLE `mensa_struttura` (
  `id_struttura` int(11) NOT NULL,
  `nome` longtext NOT NULL,
  `indirizzo` longtext NOT NULL,
  `numero_tavoli_disponibili` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa_struttura`
--

INSERT INTO `mensa_struttura` (`id_struttura`, `nome`, `indirizzo`, `numero_tavoli_disponibili`) VALUES
(1, 'Mensa Centrale Milano', 'Via Roma 12, Milano', 10),
(2, 'Mensa Torino Nord', 'Corso Torino 45, Torino', 8),
(3, 'Mensa Firenze Sud', 'Viale Europa 88, Firenze', 6);

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa_tavolo`
--

CREATE TABLE `mensa_tavolo` (
  `id_tavolo` int(11) NOT NULL,
  `numero_posti_disponibili` int(11) NOT NULL,
  `disponibilità` tinyint(1) NOT NULL,
  `struttura_associata_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa_tavolo`
--

INSERT INTO `mensa_tavolo` (`id_tavolo`, `numero_posti_disponibili`, `disponibilità`, `struttura_associata_id`) VALUES
(1, 4, 1, 1),
(2, 6, 1, 1),
(3, 2, 1, 1),
(4, 8, 1, 1),
(5, 4, 1, 1),
(6, 6, 1, 1),
(7, 2, 1, 1),
(8, 4, 1, 1),
(9, 6, 1, 1),
(10, 4, 1, 1),
(11, 4, 1, 2),
(12, 6, 1, 2),
(13, 2, 1, 2),
(14, 8, 1, 2),
(15, 4, 1, 2),
(16, 6, 1, 2),
(17, 2, 1, 2),
(18, 4, 1, 2),
(19, 6, 1, 2),
(20, 4, 1, 2),
(21, 4, 1, 3),
(22, 6, 1, 3),
(23, 2, 1, 3),
(24, 8, 1, 3),
(25, 4, 1, 3),
(26, 6, 1, 3),
(27, 2, 1, 3),
(28, 4, 1, 3),
(29, 6, 1, 3),
(30, 4, 1, 3);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indici per le tabelle `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indici per le tabelle `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indici per le tabelle `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indici per le tabelle `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indici per le tabelle `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indici per le tabelle `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indici per le tabelle `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indici per le tabelle `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indici per le tabelle `mensa_amministratore`
--
ALTER TABLE `mensa_amministratore`
  ADD PRIMARY KEY (`id_amministratore`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `mensa_amministratore_id_azienda_id_b6dd8066_fk_mensa_azi` (`id_azienda_id`);

--
-- Indici per le tabelle `mensa_associazione`
--
ALTER TABLE `mensa_associazione`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mensa_associazione_prenotazione_id_1c4661a7_fk_mensa_pre` (`prenotazione_id`),
  ADD KEY `mensa_associazione_piatto_id_c1006dcf_fk_mensa_piatto_id_piatto` (`piatto_id`);

--
-- Indici per le tabelle `mensa_azienda`
--
ALTER TABLE `mensa_azienda`
  ADD PRIMARY KEY (`id_azienda`),
  ADD KEY `mensa_azienda_id_struttura_id_93585478_fk_mensa_str` (`id_struttura_id`);

--
-- Indici per le tabelle `mensa_dipendente`
--
ALTER TABLE `mensa_dipendente`
  ADD PRIMARY KEY (`id_dipendente`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `mensa_dipendente_id_azienda_id_9e3b6266_fk_mensa_azi` (`id_azienda_id`);

--
-- Indici per le tabelle `mensa_piatto`
--
ALTER TABLE `mensa_piatto`
  ADD PRIMARY KEY (`id_piatto`),
  ADD KEY `mensa_piatto_id_responsabile_id_61a9a5d1_fk_mensa_res` (`id_responsabile_id`);

--
-- Indici per le tabelle `mensa_prenotazione`
--
ALTER TABLE `mensa_prenotazione`
  ADD PRIMARY KEY (`id_prenotazione`),
  ADD KEY `mensa_prenotazione_id_tavolo_id_88c13cfb_fk_mensa_tav` (`id_tavolo_id`),
  ADD KEY `mensa_prenotazione_id_dipendente_id_28835e86_fk_mensa_dip` (`id_dipendente_id`);

--
-- Indici per le tabelle `mensa_responsabile`
--
ALTER TABLE `mensa_responsabile`
  ADD PRIMARY KEY (`id_responsabile`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `mensa_responsabile_id_struttura_id_dc41de8a_fk_mensa_str` (`id_struttura_id`);

--
-- Indici per le tabelle `mensa_struttura`
--
ALTER TABLE `mensa_struttura`
  ADD PRIMARY KEY (`id_struttura`);

--
-- Indici per le tabelle `mensa_tavolo`
--
ALTER TABLE `mensa_tavolo`
  ADD PRIMARY KEY (`id_tavolo`),
  ADD KEY `mensa_tavolo_struttura_associata__37b0c49f_fk_mensa_str` (`struttura_associata_id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT per la tabella `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT per la tabella `mensa_associazione`
--
ALTER TABLE `mensa_associazione`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `mensa_piatto`
--
ALTER TABLE `mensa_piatto`
  MODIFY `id_piatto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT per la tabella `mensa_prenotazione`
--
ALTER TABLE `mensa_prenotazione`
  MODIFY `id_prenotazione` int(11) NOT NULL AUTO_INCREMENT;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Limiti per la tabella `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Limiti per la tabella `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limiti per la tabella `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limiti per la tabella `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limiti per la tabella `mensa_amministratore`
--
ALTER TABLE `mensa_amministratore`
  ADD CONSTRAINT `mensa_amministratore_id_azienda_id_b6dd8066_fk_mensa_azi` FOREIGN KEY (`id_azienda_id`) REFERENCES `mensa_azienda` (`id_azienda`);

--
-- Limiti per la tabella `mensa_associazione`
--
ALTER TABLE `mensa_associazione`
  ADD CONSTRAINT `mensa_associazione_piatto_id_c1006dcf_fk_mensa_piatto_id_piatto` FOREIGN KEY (`piatto_id`) REFERENCES `mensa_piatto` (`id_piatto`),
  ADD CONSTRAINT `mensa_associazione_prenotazione_id_1c4661a7_fk_mensa_pre` FOREIGN KEY (`prenotazione_id`) REFERENCES `mensa_prenotazione` (`id_prenotazione`);

--
-- Limiti per la tabella `mensa_azienda`
--
ALTER TABLE `mensa_azienda`
  ADD CONSTRAINT `mensa_azienda_id_struttura_id_93585478_fk_mensa_str` FOREIGN KEY (`id_struttura_id`) REFERENCES `mensa_struttura` (`id_struttura`);

--
-- Limiti per la tabella `mensa_dipendente`
--
ALTER TABLE `mensa_dipendente`
  ADD CONSTRAINT `mensa_dipendente_id_azienda_id_9e3b6266_fk_mensa_azi` FOREIGN KEY (`id_azienda_id`) REFERENCES `mensa_azienda` (`id_azienda`);

--
-- Limiti per la tabella `mensa_piatto`
--
ALTER TABLE `mensa_piatto`
  ADD CONSTRAINT `mensa_piatto_id_responsabile_id_61a9a5d1_fk_mensa_res` FOREIGN KEY (`id_responsabile_id`) REFERENCES `mensa_responsabile` (`id_responsabile`);

--
-- Limiti per la tabella `mensa_prenotazione`
--
ALTER TABLE `mensa_prenotazione`
  ADD CONSTRAINT `mensa_prenotazione_id_dipendente_id_28835e86_fk_mensa_dip` FOREIGN KEY (`id_dipendente_id`) REFERENCES `mensa_dipendente` (`id_dipendente`),
  ADD CONSTRAINT `mensa_prenotazione_id_tavolo_id_88c13cfb_fk_mensa_tav` FOREIGN KEY (`id_tavolo_id`) REFERENCES `mensa_tavolo` (`id_tavolo`);

--
-- Limiti per la tabella `mensa_responsabile`
--
ALTER TABLE `mensa_responsabile`
  ADD CONSTRAINT `mensa_responsabile_id_struttura_id_dc41de8a_fk_mensa_str` FOREIGN KEY (`id_struttura_id`) REFERENCES `mensa_struttura` (`id_struttura`);

--
-- Limiti per la tabella `mensa_tavolo`
--
ALTER TABLE `mensa_tavolo`
  ADD CONSTRAINT `mensa_tavolo_struttura_associata__37b0c49f_fk_mensa_str` FOREIGN KEY (`struttura_associata_id`) REFERENCES `mensa_struttura` (`id_struttura`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
