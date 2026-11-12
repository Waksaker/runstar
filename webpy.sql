-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 12, 2026 at 04:42 PM
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
-- Table structure for table `func`
--

CREATE TABLE `func` (
  `id` int NOT NULL,
  `func` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `func`
--

INSERT INTO `func` (`id`, `func`) VALUES
(1, 0);

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
(37, '0.22%', '2026-10-26'),
(38, '0.23%', '2026-10-27'),
(39, '0.20%', '2026-10-28');

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
  `staprofit` int NOT NULL,
  `statrade` int NOT NULL,
  `statranfer` int NOT NULL,
  `runtrans` int NOT NULL,
  `masa_akhir` text NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id`, `username`, `password`, `trades`, `status`, `staprofit`, `statrade`, `statranfer`, `runtrans`, `masa_akhir`, `date`) VALUES
(2, 'farishdanial', 'waksaker1', 0, 0, 0, 1, 0, 0, '0000-00-00 00:00:00', '2026-10-20'),
(3, 'farishdanial01', 'waksaker1', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(4, 'farishdanial02', 'waksaker1', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(5, 'farishdanial03', 'waksaker1', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(6, 'farishdanial04', 'waksaker1', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(7, 'nisa08', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(8, 'nisa09', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(9, 'nisa10', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(10, 'nisa11', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(11, 'cantik08', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(12, 'cantik09', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(13, 'mantoba', 'waksaker1', 0, 0, 0, 1, 0, 0, '0000-00-00 00:00:00', '2026-10-20'),
(14, 'sharipah', 'waksaker1', 0, 0, 0, 1, 0, 0, '0000-00-00 00:00:00', '2026-10-20'),
(18, 'cantik02', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(19, 'cantik03', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(20, 'cantik04', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(21, 'cantik05', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(22, 'cantik06', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(23, 'cantik07', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(24, 'nisa04', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(25, 'nisa05', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(26, 'nisa06', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(27, 'nisa07', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20'),
(28, 'richarissa', 'Dsnisya86@', 0, 0, 0, 1, 0, 0, '0000-00-00 00:00:00', '2026-10-20'),
(29, 'richarissa1', 'Dsnisya86@', 0, 0, 0, 1, 1, 0, '0000-00-00 00:00:00', '2026-10-20');

-- --------------------------------------------------------

--
-- Table structure for table `profitlock`
--

CREATE TABLE `profitlock` (
  `id` int NOT NULL,
  `iduser` int NOT NULL,
  `date` text NOT NULL,
  `profit` text NOT NULL,
  `lock` text NOT NULL,
  `updated` timestamp NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `profitlock`
--

INSERT INTO `profitlock` (`id`, `iduser`, `date`, `profit`, `lock`, `updated`) VALUES
(1, 2, '2026-11-08', '64.85', '301.02', '2026-11-08 15:44:45'),
(2, 3, '2026-11-08', '2.52', '183.04', '2026-11-08 15:49:28'),
(3, 4, '2026-11-08', '2.53', '183.26', '2026-11-08 15:51:54'),
(4, 5, '2026-11-08', '2.52', '182.59', '2026-11-08 15:54:22'),
(5, 6, '2026-11-08', '2.52', '182.56', '2026-11-08 15:56:41'),
(6, 7, '2026-11-08', '1.14', '281.22', '2026-11-08 15:59:01'),
(7, 8, '2026-11-09', '1.49', '177.61', '2026-11-08 16:01:16'),
(8, 2, '2026-11-10', '97.25', '301.02', '2026-11-10 07:39:00'),
(9, 3, '2026-11-10', '2.41', '185.56', '2026-11-09 17:18:02'),
(10, 2, '2026-11-12', '146.74', '301.02', '2026-11-12 14:05:08'),
(11, 3, '2026-11-12', '0.0', '176.97', '2026-11-12 15:25:58'),
(12, 4, '2026-11-12', '0.0', '177.22', '2026-11-12 15:29:52');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `func`
--
ALTER TABLE `func`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `profitlock`
--
ALTER TABLE `profitlock`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `func`
--
ALTER TABLE `func`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `link`
--
ALTER TABLE `link`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `log_percent`
--
ALTER TABLE `log_percent`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `profitlock`
--
ALTER TABLE `profitlock`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
