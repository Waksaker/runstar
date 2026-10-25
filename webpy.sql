-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 25, 2026 at 03:21 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webpy`
--

-- --------------------------------------------------------

--
-- Table structure for table `link`
--

CREATE TABLE `link` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `updated` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `link`
--

INSERT INTO `link` (`id`, `name`, `updated`) VALUES
(1, 'https://starlika.net', '2026-10-13 13:08:00');

-- --------------------------------------------------------

--
-- Table structure for table `log_percent`
--

CREATE TABLE `log_percent` (
  `id` int NOT NULL,
  `percent` text NOT NULL,
  `date` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `log_percent`
--

INSERT INTO `log_percent` (`id`, `percent`, `date`) VALUES
(32, '0.34%', '2026-10-16'),
(33, '0.22%', '2026-10-17'),
(34, '0.24%', '2026-10-18'),
(35, '0.22%', '2026-10-19'),
(36, '0.28%', '2026-10-20');

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id` int NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `trades` int NOT NULL,
  `status` int NOT NULL,
  `statranfer` int NOT NULL,
  `runtrans` int NOT NULL,
  `masa_akhir` text NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id`, `username`, `password`, `trades`, `status`, `statranfer`, `runtrans`, `masa_akhir`, `date`) VALUES
(2, 'farishdanial', 'waksaker1', 0, 1, 0, 0, '00:12:35', '2026-10-20'),
(3, 'farishdanial01', 'waksaker1', 0, 1, 1, 0, '00:14:53', '2026-10-20'),
(4, 'farishdanial02', 'waksaker1', 0, 1, 1, 0, '00:17:14', '2026-10-20'),
(5, 'farishdanial03', 'waksaker1', 0, 1, 1, 0, '00:19:34', '2026-10-20'),
(6, 'farishdanial04', 'waksaker1', 0, 1, 1, 0, '00:21:55', '2026-10-20'),
(7, 'nisa08', 'Dsnisya86@', 0, 1, 1, 0, '00:24:15', '2026-10-20'),
(8, 'nisa09', 'Dsnisya86@', 0, 1, 1, 0, '00:26:41', '2026-10-20'),
(9, 'nisa10', 'Dsnisya86@', 0, 1, 1, 0, '00:29:03', '2026-10-20'),
(10, 'nisa11', 'Dsnisya86@', 0, 1, 1, 0, '00:31:35', '2026-10-20'),
(11, 'cantik08', 'Dsnisya86@', 0, 1, 1, 0, '00:33:56', '2026-10-20'),
(12, 'cantik09', 'Dsnisya86@', 0, 1, 1, 0, '00:36:32', '2026-10-20'),
(13, 'mantoba', 'waksaker1', 0, 1, 0, 0, '00:39:09', '2026-10-20'),
(14, 'sharipah', 'waksaker1', 0, 1, 0, 0, '00:43:05', '2026-10-20'),
(18, 'cantik02', 'Dsnisya86@', 0, 1, 1, 0, '00:45:23', '2026-10-20'),
(19, 'cantik03', 'Dsnisya86@', 0, 1, 1, 0, '00:47:52', '2026-10-20'),
(20, 'cantik04', 'Dsnisya86@', 0, 1, 1, 0, '00:50:12', '2026-10-20'),
(21, 'cantik05', 'Dsnisya86@', 0, 1, 1, 0, '00:52:35', '2026-10-20'),
(22, 'cantik06', 'Dsnisya86@', 0, 1, 1, 0, '00:57:04', '2026-10-20'),
(23, 'cantik07', 'Dsnisya86@', 0, 1, 1, 0, '00:59:27', '2026-10-20'),
(24, 'nisa04', 'Dsnisya86@', 0, 1, 1, 0, '01:01:48', '2026-10-20'),
(25, 'nisa05', 'Dsnisya86@', 0, 1, 1, 0, '01:04:26', '2026-10-20'),
(26, 'nisa06', 'Dsnisya86@', 0, 1, 1, 0, '01:06:48', '2026-10-20'),
(27, 'nisa07', 'Dsnisya86@', 0, 1, 1, 0, '01:09:12', '2026-10-20'),
(28, 'richarissa', 'Dsnisya86@', 0, 1, 0, 0, '01:11:31', '2026-10-20'),
(29, 'richarissa1', 'Dsnisya86@', 0, 1, 1, 0, '01:14:02', '2026-10-20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `link`
--
ALTER TABLE `link`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `log_percent`
--
ALTER TABLE `log_percent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `link`
--
ALTER TABLE `link`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `log_percent`
--
ALTER TABLE `log_percent`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
