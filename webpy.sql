-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 20, 2026 at 02:53 AM
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
(1, 'https://starlika.cc', '2026-10-13 13:08:00');

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
  `masa_akhir` time NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id`, `username`, `password`, `trades`, `status`, `statranfer`, `runtrans`, `masa_akhir`, `date`) VALUES
(2, 'farishdanial', 'waksaker1', 2, 1, 0, 0, '11:15:48', '2026-10-20'),
(3, 'farishdanial01', 'waksaker1', 2, 1, 1, 1, '11:22:51', '2026-10-20'),
(4, 'farishdanial02', 'waksaker1', 2, 1, 1, 1, '11:29:47', '2026-10-20'),
(5, 'farishdanial03', 'waksaker1', 2, 1, 1, 1, '11:36:50', '2026-10-20'),
(6, 'farishdanial04', 'waksaker1', 2, 1, 1, 1, '11:43:55', '2026-10-20'),
(7, 'nisa08', 'Dsnisya86@', 2, 1, 1, 1, '11:50:54', '2026-10-20'),
(8, 'nisa09', 'Dsnisya86@', 2, 1, 1, 1, '11:56:23', '2026-10-20'),
(9, 'nisa10', 'Dsnisya86@', 2, 1, 1, 1, '11:59:16', '2026-10-20'),
(10, 'nisa11', 'Dsnisya86@', 2, 1, 1, 1, '12:02:18', '2026-10-20'),
(11, 'cantik08', 'Dsnisya86@', 2, 1, 1, 1, '12:05:18', '2026-10-20'),
(12, 'cantik09', 'Dsnisya86@', 2, 1, 1, 1, '12:08:22', '2026-10-20'),
(13, 'mantoba', 'waksaker1', 2, 1, 0, 0, '12:11:21', '2026-10-20'),
(14, 'sharipah', 'waksaker1', 2, 1, 0, 0, '12:14:28', '2026-10-20'),
(18, 'cantik02', 'Dsnisya86@', 2, 1, 1, 1, '12:17:21', '2026-10-20'),
(19, 'cantik03', 'Dsnisya86@', 2, 1, 1, 1, '12:20:33', '2026-10-20'),
(20, 'cantik04', 'Dsnisya86@', 2, 1, 1, 1, '12:23:23', '2026-10-20'),
(21, 'cantik05', 'Dsnisya86@', 2, 1, 1, 1, '12:26:22', '2026-10-20'),
(22, 'cantik06', 'Dsnisya86@', 2, 1, 1, 1, '12:29:26', '2026-10-20'),
(23, 'cantik07', 'Dsnisya86@', 2, 1, 1, 1, '12:32:23', '2026-10-20'),
(24, 'nisa04', 'Dsnisya86@', 2, 1, 1, 1, '12:35:34', '2026-10-20'),
(25, 'nisa05', 'Dsnisya86@', 2, 1, 1, 1, '12:38:28', '2026-10-20'),
(26, 'nisa06', 'Dsnisya86@', 2, 1, 1, 1, '12:41:21', '2026-10-20'),
(27, 'nisa07', 'Dsnisya86@', 2, 1, 1, 1, '12:44:29', '2026-10-20'),
(28, 'richarissa', 'Dsnisya86@', 2, 1, 0, 0, '12:47:27', '2026-10-20'),
(29, 'richarissa1', 'Dsnisya86@', 2, 1, 1, 1, '12:50:26', '2026-10-20');

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
