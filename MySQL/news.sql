-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1:3308
-- Generation Time: 2017-12-28 09:33:53
-- 服务器版本： 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wangyinews`
--

-- --------------------------------------------------------

--
-- 表的结构 `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(20) NOT NULL,
  `content` varchar(200) NOT NULL,
  `tips` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL,
  `image` varchar(200) DEFAULT NULL,
  `author` varchar(10) DEFAULT NULL,
  `in_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `news`
--

INSERT INTO `news` (`id`, `title`, `content`, `tips`, `image`, `author`, `in_time`) VALUES
(1, '中共十九届二中全会明年1月召开 讨论研究', '新华社北京12月27日电中共中央政治局12月27日召开会议，决定明年1月在北京召开中国共产党第十九届中央委员会第二次全体会议，主要议程是，讨论研究修改宪法部分内容的建议。会议听取中央纪律检查委员会工作汇报，研究部署2018年党风廉政建设和反腐败工作。中共中央总书记习近平主持会议。', 'polotical', NULL, 'LUCY', '2017-12-01 00:00:00'),
(2, '新疆克拉玛依遇10级狂风 塑胶场地被掀翻', '12月27日，新疆克拉玛依，狂风裹着雪花弥漫了整个城市。克拉玛依大学城的塑胶篮球场地被掀，路人被大风推倒。据天气预报，局地风力达9-10级。', 'winds', NULL, 'wanghu', '2017-12-03 00:00:00'),
(3, '男子在上海地铁站跳入轨道 被列车冲撞身亡', '澎湃新闻记者从上海轨交公安了解到，12月28日12时18分，一男性乘客从地铁2号线娄山关路站上行方向站台跳入轨道，被后续列车冲撞身亡。此事未对线路运营造成影响，事件正在进一步处理中。', 'subway', 'http://cms-bucket.nosdn.127.net/catchpic/4/41/41c93714da0037196165d899de690682.jpg?imageView&thumbnail=550x0', 'SHARY', '2017-12-05 00:00:00'),
(4, '美国一乘客起飞4小时后发现登错机 航班掉', '报道说，26号，这架载有226名乘客的客机预计飞行11个小时后抵达东京；然而，当飞机飞行了4小时时，乘客突然听到机组广播称，机组人员发现有一名乘客的机票信息不属于本航班，因此需要返航。这一消息让机上的乘客们十分无奈。', 'airline', NULL, 'JHON', '2017-12-10 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
