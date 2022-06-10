-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: learnopedia
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

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
-- Table structure for table `Article`
--

DROP TABLE IF EXISTS `Article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Article` (
  `articleId` int NOT NULL AUTO_INCREMENT,
  `previewPic` varchar(100) DEFAULT NULL,
  `title` varchar(25) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `isValidated` int NOT NULL,
  `textContent` longtext NOT NULL,
  `textContentRaw` longtext NOT NULL,
  `previewPicture` longtext,
  `numOfLikes` int NOT NULL,
  `korisnikId` bigint NOT NULL,
  PRIMARY KEY (`articleId`),
  UNIQUE KEY `slug` (`slug`),
  KEY `Article_korisnikId_61b8687d_fk_Korisnik_id` (`korisnikId`),
  CONSTRAINT `Article_korisnikId_61b8687d_fk_Korisnik_id` FOREIGN KEY (`korisnikId`) REFERENCES `Korisnik` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Article`
--

LOCK TABLES `Article` WRITE;
/*!40000 ALTER TABLE `Article` DISABLE KEYS */;
INSERT INTO `Article` VALUES (1,'imgs/tenisvijetnam_9BueKDk.jpg','Yvon Petra','Yvon Petra','2022-05-30 16:04:30.425621',0,'<p><font face=\"Amiko, Helvetica, Arial, sans-serif\" color=\"#3984c6\"><span style=\"font-size: 18px; background-color: rgb(244, 244, 241);\">With an HPI of 57.89, Yvon Petra is the most famous Vietnamese Tennis Player.&nbsp; His biography has been translated into 16 different languages on wikipedia. Yvon Petra (French pronunciation: ​[ivɔ̃ petʁa]; 8 March 1916 – 12 September 1984) was a French male tennis player. He was born in Cholon, French Indochina. Petra is best remembered as the last Frenchman to win the Wimbledon Championships men\'s singles title (in 1946), beating Geoff Brown in five sets in the final. In doubles, he won the French Championships twice, in 1938 with Bernard Destremau, defeating the best pair in the world Budge-Mako, and in 1946 with Marcel Bernard. In 1938, he won the singles and doubles title at the French Covered Court Championships. He was a prisoner of war in World War II and after his release won three Tournoi de France singles titles from 1943 through 1945.</span></font><br></p>','With an HPI of&nbsp;57.89,&nbsp;Yvon Petra&nbsp;is the most famous&nbsp;Vietnamese&nbsp;Tennis Player. &nbsp;His&nbsp;biography has been translated into&nbsp;16&nbsp;different languages on wikipedia.Yvon Petra (French pronunciation: ​[ivɔ̃ petʁa]; 8 March 1916 – 12 September 1984) was a French male tennis player. He was born in Cholon, French Indochina. Petra is best remembered as the last Frenchman to win the Wimbledon Championships men\'s singles title (in 1946), beating Geoff Brown in five sets in the final. In doubles, he won the French Championships twice, in 1938 with Bernard Destremau, defeating the best pair in the world Budge-Mako, and in 1946 with Marcel Bernard. In 1938, he won the singles and doubles title at the French Covered Court Championships. He was a prisoner of war in World War II and after his release won three Tournoi&nbsp;de France singles titles from 1943 through 1945.',NULL,1,3),(2,'imgs/vietnamwar_Ml0HyOx.jpg','Vietnam War','Vietnam War','2022-05-30 16:04:30.425621',0,'<p style=\"margin-top: 30px; margin-bottom: 30px; padding: 0px; max-width: 100%;\"><font face=\"open-sans, sans-serif\" color=\"#cee7f7\"><span style=\"font-size: 18px; letter-spacing: 0.8px;\">The Vietnam War was a long, costly and divisive conflict that pitted the communist government of North Vietnam against South Vietnam and its principal ally, the United States. The conflict was intensified by the ongoing Cold War between the United States and the Soviet Union. More than 3 million people (including over 58,000 Americans) were killed in the Vietnam War, and more than half of the dead were Vietnamese civilians.</span></font><br></p><p style=\"box-sizing: border-box; margin: 30px 0px; padding: 0px; max-width: 100%; color: rgb(24, 24, 24); font-family: open-sans, sans-serif; font-size: 18px; letter-spacing: 0.8px;\"><br style=\"box-sizing: border-box; color: rgb(24, 24, 24); font-family: open-sans, sans-serif; font-size: 18px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: 0.8px; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;\"></p><p style=\"margin-top: 30px; margin-bottom: 30px; padding: 0px; max-width: 100%; color: rgb(24, 24, 24); font-family: open-sans, sans-serif; font-size: 18px; letter-spacing: 0.8px;\"><br></p><div><br></div>','The Vietnam War was a long, costly and divisive conflict that pitted the communist government of North Vietnam against South Vietnam and its principal ally, the United States. The conflict was intensified by the ongoing Cold War between the United States and the Soviet Union. More than 3 million people (including over 58,000 Americans) were killed in the Vietnam War, and more than half of the dead were Vietnamese civilians.&nbsp;',NULL,3,3),(3,'imgs/elon_IFka4V3.jpg','Elon and Twitter','Elon Musk','2022-05-30 16:04:30.425621',0,'<p><span style=\"font-family: nyt-imperial, georgia, &quot;times new roman&quot;, times, serif; font-size: 20px;\"><font color=\"#cee7f7\"><span style=\"font-family: Arial;\">Twitter agreed to sell itself to Mr. Musk for $54.20 a share, a 38 percent premium over the company’s share price this month before he revealed he was the firm’s single largest shareholder. It would be the largest deal to take a company private — something Mr. Musk has said he will do with Twitter — in at least two decades, according to data compiled by Dealogic</span>.</font></span><span style=\"font-family: Arial;\">﻿</span><br></p>','Elon Reeve Musk&nbsp;FRS&nbsp;(/ˈiːlɒn/&nbsp;EE-lon; born June 28, 1971) is a&nbsp;business magnate&nbsp;and investor. He is the founder, CEO, and&nbsp;Chief Engineer&nbsp;at&nbsp;SpaceX;&nbsp;angel investor, CEO, and Product Architect of&nbsp;Tesla, Inc.; founder of&nbsp;The Boring Company; and co-founder of&nbsp;Neuralink&nbsp;and&nbsp;OpenAI. With an estimated net worth of around US$265&nbsp;billion as of May 2022,[4]&nbsp;Musk is the wealthiest person in the world according to both the&nbsp;Bloomberg Billionaires Index&nbsp;and the&nbsp;Forbes&nbsp;real-time billionaires list.',NULL,3,3),(4,'imgs/lol_muOSHq3.jpeg','LeagueOfLegends','LeagueOfLegends','2022-05-30 16:04:30.425621',0,'<p><font face=\"sans-serif\" color=\"#cee7f7\">In the game, two teams of five players battle in player-versus-player combat, each team occupying and defending their half of the map. Each of the ten players controls a character, known as a \"champion\", with unique abilities and differing styles of play. During a match, champions become more powerful by collecting experience points, earning gold, and purchasing items to defeat the opposing team. In League\'s main mode, Summoner\'s Rift, a team wins by pushing through to the enemy base and destroying their \"Nexus\", a large structure located within.</font><br></p>','In the game, two teams of five players battle in player-versus-player combat, each team occupying and defending their half of the map. Each of the ten players controls a character, known as a \"champion\", with unique abilities and differing styles of play. During a match, champions become more powerful by collecting experience points, earning gold, and purchasing items to defeat the opposing team. In League\'s main mode, Summoner\'s Rift, a team wins by pushing through to the enemy base and destroying their \"Nexus\", a large structure located within.',NULL,1,4),(5,'','Summernote IS BAD','Summernote IS BAD','2022-05-30 16:04:30.425621',0,'<p dir=\"auto\" style=\"margin-bottom: 16px;\"><font color=\"#cee7f7\"><font face=\"-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji\">In summernote-bs3.css you\'re overriding the bootstrap styling of .hidden-xs, .hidden-sm, .hidden-md, .hidden-lg, etc. This is a bad practice for multiple reasons: You\'re using !important (instead: increase specificity of your selector, e.g. .note-editor .hidden-xs) You\'re overriding this style throughout the entire page layout, instead of scoping it to summernote, which means that if any other parts of the design make use of these styles and depend on their default behavior, they no longer work as intended.</font><br></font></p><p dir=\"auto\" style=\"margin-bottom: 16px; color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;\"><br></p><ol dir=\"auto\" style=\"padding-left: 2em; color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; margin-bottom: 0px !important;\"></ol>','In summernote-bs3.css you\'re overriding the bootstrap styling of .hidden-xs, .hidden-sm, .hidden-md, .hidden-lg, etc. This is a bad practice for multiple reasons: You\'re using !important (instead: increase specificity of your selector, e.g. .note-editor .hidden-xs) You\'re overriding this style throughout the entire page layout, instead of scoping it to summernote, which means that if any other parts of the design make use of these styles and depend on their default behavior, they no longer work as intended.',NULL,2,4),(6,'imgs/billgates.jpg','Bill Gates','Bill Gates','2022-05-30 16:04:30.425621',0,'<p>William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, author, and philanthropist. He is a co-founder of Microsoft, along with his late childhood friend Paul Allen. During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO), president and chief software architect, while also being the largest individual shareholder until May 2014. He was a major entrepreneur of the microcomputer revolution of the 1970s and 1980s.<br></p>','William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, author, and philanthropist. He is a co-founder of Microsoft, along with his late childhood friend Paul Allen. During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO), president and chief software architect, while also being the largest individual shareholder until May 2014. He was a major entrepreneur of the microcomputer revolution of the 1970s and 1980s.',NULL,1,4),(7,'imgs/magic.jpg','Magic Johnson','Magic Johnson','2022-05-30 16:04:30.425621',0,'<p>Earvin \"Magic\" Johnson Jr. (born August 14, 1959) is an American former professional basketball player and former president of basketball operations of the Los Angeles Lakers of the National Basketball Association (NBA). Often regarded as the greatest point guard of all time,[3][4] Johnson played 13 seasons for the Lakers and was honored as one of the 50 Greatest Players in NBA History in 1996 and selected to the NBA 75th Anniversary Team in 2021. After winning championships in high school and college, Johnson was selected first overall in the 1979 NBA draft by the Lakers. He won a championship and an NBA Finals Most Valuable Player Award in his rookie season, and won four more championships with the Lakers during the 1980s. Johnson retired abruptly in 1991 after announcing that he had contracted HIV, but returned to play in the 1992 All-Star Game, winning the All-Star MVP Award. After protests from his fellow players, he retired again for four years, but returned in 1996, at age 36, to play 32 games for the Lakers before retiring for the third and final time.<br></p>','Earvin \"Magic\" Johnson Jr. (born August 14, 1959) is an American former professional basketball player and former president of basketball operations of the Los Angeles Lakers of the National Basketball Association (NBA). Often regarded as the greatest point guard of all time,[3][4] Johnson played 13 seasons for the Lakers and was honored as one of the 50 Greatest Players in NBA History in 1996 and selected to the NBA 75th Anniversary Team in 2021. After winning championships in high school and college, Johnson was selected first overall in the 1979 NBA draft by the Lakers. He won a championship and an NBA Finals Most Valuable Player Award in his rookie season, and won four more championships with the Lakers during the 1980s. Johnson retired abruptly in 1991 after announcing that he had contracted HIV, but returned to play in the 1992 All-Star Game, winning the All-Star MVP Award. After protests from his fellow players, he retired again for four years, but returned in 1996, at age 36, to play 32 games for the Lakers before retiring for the third and final time.',NULL,1,2),(8,'imgs/carmelo.jpg','Carmelo','Carmelo','2022-05-30 16:04:30.425621',0,'<p><font face=\"sans-serif\" color=\"#9cc6ef\"><b style=\"\">Carmelo Kyam Anthony (born May 29, 1984) is an American professional basketball player for the Los Angeles Lakers. He has been named an NBA All-Star ten times and an All-NBA Team member six times. He played college basketball for the Syracuse Orange, winning a national championship as a freshman in 2003 while being named the NCAA Tournament\'s Most Outstanding Player. During the NBA\'s 75th anniversary, he was named one of the 75 Greatest Players in NBA History, and is regarded as one of the greatest scorers and players in the history of basketball.</b></font><br></p>','Carmelo Kyam Anthony (born May 29, 1984) is an American professional basketball player for the Los Angeles Lakers. He has been named an NBA All-Star ten times and an All-NBA Team member six times. He played college basketball for the Syracuse Orange, winning a national championship as a freshman in 2003 while being named the NCAA Tournament\'s Most Outstanding Player. During the NBA\'s 75th anniversary, he was named one of the 75 Greatest Players in NBA History, and is regarded as one of the greatest scorers and players in the history of basketball.',NULL,1,2),(9,'imgs/270px-Messi_vs_Nigeria_2018.jpg','Lionel Messi','Lionel Messi','2022-05-30 16:04:30.425621',0,'<p>Lionel Andrés Messi(Spanish pronunciation: [ljoˈnel anˈdɾes ˈmesi] (listen); born 24 June 1987), also known as Leo Messi, is an Argentine professional footballer who plays as a forward for Ligue 1 club Paris Saint-Germain and captains the Argentina national team. Often considered the best player in the world and widely regarded as one of the greatest players of all time, Messi has won a record seven Ballon d\'Or awards, a record six European Golden Shoes, and in 2020 was named to the Ballon d\'Or Dream Team. Until leaving the club in 2021, he had spent his entire professional career with Barcelona, where he won a club-record 35 trophies, including ten La Liga titles, seven Copa del Rey titles and four UEFA Champions Leagues. A prolific goalscorer and creative playmaker, Messi holds the records for most goals in La Liga (474), a La Liga and European league season (50), most hat-tricks in La Liga (36) and the UEFA Champions League (8), and most assists in La Liga (192), a La Liga season (21) and the Copa América (17). He also holds the record for most international goals by a South American male (81). Messi has scored over 750 senior career goals for club and country, and has the most goals by a player for a single club.<br></p>','Lionel Andrés Messi(Spanish pronunciation: [ljoˈnel anˈdɾes ˈmesi] (listen); born 24 June 1987), also known as Leo Messi, is an Argentine professional footballer who plays as a forward for Ligue 1 club Paris Saint-Germain and captains the Argentina national team. Often considered the best player in the world and widely regarded as one of the greatest players of all time, Messi has won a record seven Ballon d\'Or awards, a record six European Golden Shoes, and in 2020 was named to the Ballon d\'Or Dream Team. Until leaving the club in 2021, he had spent his entire professional career with Barcelona, where he won a club-record 35 trophies, including ten La Liga titles, seven Copa del Rey titles and four UEFA Champions Leagues. A prolific goalscorer and creative playmaker, Messi holds the records for most goals in La Liga (474), a La Liga and European league season (50), most hat-tricks in La Liga (36) and the UEFA Champions League (8), and most assists in La Liga (192), a La Liga season (21) and the Copa América (17). He also holds the record for most international goals by a South American male (81). Messi has scored over 750 senior career goals for club and country, and has the most goals by a player for a single club.',NULL,0,5),(10,'imgs/roman.jpg','Roman','Roman','2022-05-30 16:04:30.425621',0,'<p><font color=\"#9cc6ef\">Roman Arkadyevich Abramovich (Russian: Роман Аркадьевич Абрамович, pronounced [rɐˈman ɐrˈkadʲjɪvʲɪtɕ ɐbrɐˈmovʲɪtɕ]; Hebrew: רומן ארקדיביץ\' אברמוביץ\'; born 24 October 1966) is a Russian oligarch, businessman, philanthropist and politician. He is best known outside Russia as the former owner of Chelsea, a Premier League football club in London, England, and is the primary owner of the private investment company Millhouse LLC. He was formerly Governor of Chukotka Autonomous Okrug from 2000 to 2008. According to Forbes, Abramovich\'s net worth was US$14.5 billion in 2021, making him the second-richest person in Israel, the eleventh-richest in Russia and the richest person in Portugal. Abramovich enriched himself in the years following the collapse of the Soviet Union in the 1990s, obtaining Russian state-owned assets at prices far below market value in Russia\'s controversial loans-for-shares privatisation program. Abramovich is considered to have a good relationship with Russian president Vladimir Putin.[6] Besides Russian, he also holds Israeli and Portuguese citizenship.</font><br></p>','Roman Arkadyevich Abramovich (Russian: Роман Аркадьевич Абрамович, pronounced [rɐˈman ɐrˈkadʲjɪvʲɪtɕ ɐbrɐˈmovʲɪtɕ]; Hebrew: רומן ארקדיביץ\' אברמוביץ\'; born 24 October 1966) is a Russian oligarch, businessman, philanthropist and politician. He is best known outside Russia as the former owner of Chelsea, a Premier League football club in London, England, and is the primary owner of the private investment company Millhouse LLC. He was formerly Governor of Chukotka Autonomous Okrug from 2000 to 2008. According to Forbes, Abramovich\'s net worth was US$14.5 billion in 2021, making him the second-richest person in Israel, the eleventh-richest in Russia and the richest person in Portugal. Abramovich enriched himself in the years following the collapse of the Soviet Union in the 1990s, obtaining Russian state-owned assets at prices far below market value in Russia\'s controversial loans-for-shares privatisation program. Abramovich is considered to have a good relationship with Russian president Vladimir Putin.[6] Besides Russian, he also holds Israeli and Portuguese citizenship.',NULL,1,5),(11,'imgs/hotshot.jpg','George Georgallidis','George Georgallidis','2022-05-30 16:04:30.425621',0,'<p><font color=\"#9cc6ef\">George Georgallidis (born June 23, 1990), better known by his in-game name HotshotGG, is the founder, owner of, and a former player for Counter Logic Gaming, a professional esports organization.</font></p><p><font color=\"#9cc6ef\">George Georgallidis founded Counter Logic Gaming in April 2010. Georgallidis has since led the organization\'s teams to success across multiple esports titles, including League of Legends, Counter-Strike: Global Offensive, Halo, and Super Smash Bros.. Following the 2013 NA LCS Spring Split, George stepped down as a player to take a managerial role in the team. He was replaced with Nientonsoh on May 26, 2013.</font><br></p>','George Georgallidis (born June 23, 1990), better known by his in-game name HotshotGG, is the founder, owner of, and a former player for Counter Logic Gaming, a professional esports organization.George Georgallidis founded Counter Logic Gaming in April 2010. Georgallidis has since led the organization\'s teams to success across multiple esports titles, including League of Legends, Counter-Strike: Global Offensive, Halo, and Super Smash Bros.. Following the 2013 NA LCS Spring Split, George stepped down as a player to take a managerial role in the team. He was replaced with Nientonsoh on May 26, 2013.',NULL,0,5),(12,'imgs/iluminati.png','Illuminati','Illuminati','2022-05-30 16:04:30.425621',0,'<p><span style=\"font-size: 24px;\"><b>Forbidden Dorito</b></span><br></p><p><br></p><p><br></p><p>The Illuminati (plural of Latin illuminatus, \'enlightened\') is a name given to several groups, both real and fictitious. Historically, the name usually refers to the Bavarian Illuminati, an Enlightenment-era secret society founded on 1 May 1776 in Bavaria, today part of Germany. The society\'s goals were to oppose superstition, obscurantism, religious influence over public life, and abuses of state power. \"The order of the day,\" they wrote in their general statutes, \"is to put an end to the machinations of the purveyors of injustice, to control them without dominating them.\" The Illuminati—along with Freemasonry and other secret societies—were outlawed through edict by Charles Theodore, Elector of Bavaria, with the encouragement of the Catholic Church, in 1784, 1785, 1787, and 1790. During subsequent years, the group was generally vilified by conservative and religious critics who claimed that the Illuminati continued underground and were responsible for the French Revolution.<br></p>','Forbidden DoritoThe Illuminati (plural of Latin illuminatus, \'enlightened\') is a name given to several groups, both real and fictitious. Historically, the name usually refers to the Bavarian Illuminati, an Enlightenment-era secret society founded on 1 May 1776 in Bavaria, today part of Germany. The society\'s goals were to oppose superstition, obscurantism, religious influence over public life, and abuses of state power. \"The order of the day,\" they wrote in their general statutes, \"is to put an end to the machinations of the purveyors of injustice, to control them without dominating them.\" The Illuminati—along with Freemasonry and other secret societies—were outlawed through edict by Charles Theodore, Elector of Bavaria, with the encouragement of the Catholic Church, in 1784, 1785, 1787, and 1790. During subsequent years, the group was generally vilified by conservative and religious critics who claimed that the Illuminati continued underground and were responsible for the French Revolution.',NULL,0,1);
/*!40000 ALTER TABLE `Article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ArticleCategory`
--

DROP TABLE IF EXISTS `ArticleCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ArticleCategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `articleId` int NOT NULL,
  `categoryId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ArticleCategory_articleId_categoryId_c5e97936_uniq` (`articleId`,`categoryId`),
  KEY `ArticleCategory_categoryId_93ec2689_fk_Category_categoryId` (`categoryId`),
  CONSTRAINT `ArticleCategory_articleId_8570d812_fk_Article_articleId` FOREIGN KEY (`articleId`) REFERENCES `Article` (`articleId`),
  CONSTRAINT `ArticleCategory_categoryId_93ec2689_fk_Category_categoryId` FOREIGN KEY (`categoryId`) REFERENCES `Category` (`categoryId`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ArticleCategory`
--

LOCK TABLES `ArticleCategory` WRITE;
/*!40000 ALTER TABLE `ArticleCategory` DISABLE KEYS */;
INSERT INTO `ArticleCategory` VALUES (26,1,1),(27,1,3),(21,2,2),(22,2,3),(23,3,4),(28,4,5),(29,5,6),(15,6,4),(16,7,4),(17,7,7),(18,8,7),(30,9,8),(31,10,4),(32,10,8),(33,11,4),(34,11,5),(35,12,1),(36,12,2),(37,12,3),(38,12,4),(39,12,5),(40,12,6),(41,12,7),(42,12,8),(43,12,9);
/*!40000 ALTER TABLE `ArticleCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category` (
  `categoryId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`categoryId`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (1,'Tennis','Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Each player uses a tennis racket that is strung with cord to strike a hollow rubber ball covered with felt over or around a net and into the opponent\'s court. The object of the game is to manoeuvre the ball in such a way that the opponent is not able to play a valid return. The player who is unable to return the ball validly will not gain a point, while the opposite player will.'),(2,'War','War is an intense armed conflict between states, governments, societies, or paramilitary groups such as mercenaries, insurgents, and militias. It is generally characterized by extreme violence, aggression, destruction, and mortality, using regular or irregular military forces. Warfare refers to the common activities and characteristics of types of war, or of wars in general.[2] Total war is warfare that is not restricted to purely legitimate military targets, and can result in massive civilian or other non-combatant suffering and casualties.'),(3,'Vietnam','Vietnam is a Southeast Asian country known for its beaches, rivers, Buddhist pagodas and bustling cities.'),(4,'Business','A business is defined as an organization or enterprising entity engaged in commercial, industrial, or professional activities'),(5,'Games','Video-games'),(6,'Programming','Programming is the process of creating a set of instructions that tell a computer how to perform a task.'),(7,'Basketball','Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball (approximately 9.4 inches (24 cm) in diameter) through the defender\'s hoop (a basket 18 inches (46 cm) in diameter mounted 10 feet (3.048 m) high to a backboard at each end of the court, while preventing the opposing team from shooting through their own hoop.'),(8,'Football','Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. Unqualified, the word football normally means the form of football that is the most popular where the word is used. Sports commonly called football include association football (known as soccer in North America and Oceania); gridiron football (specifically American football or Canadian football); Australian rules football; rugby union and rugby league; and Gaelic football.'),(9,'Mistery','????');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comment`
--

DROP TABLE IF EXISTS `Comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comment` (
  `commentId` int NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `articleId` int NOT NULL,
  `korisnikId` bigint NOT NULL,
  PRIMARY KEY (`commentId`),
  KEY `Comment_articleId_628d264e_fk_Article_articleId` (`articleId`),
  KEY `Comment_korisnikId_e3932624_fk_Korisnik_id` (`korisnikId`),
  CONSTRAINT `Comment_articleId_628d264e_fk_Article_articleId` FOREIGN KEY (`articleId`) REFERENCES `Article` (`articleId`),
  CONSTRAINT `Comment_korisnikId_e3932624_fk_Korisnik_id` FOREIGN KEY (`korisnikId`) REFERENCES `Korisnik` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment`
--

LOCK TABLES `Comment` WRITE;
/*!40000 ALTER TABLE `Comment` DISABLE KEYS */;
INSERT INTO `Comment` VALUES (2,'We all know that he will buy Twitter eventually.','2022-05-30 16:04:30.426481',3,4),(3,'He was really one of the best.','2022-05-30 16:04:30.426481',1,4),(4,'When u measure war casualties US won that war. LOL git gud.','2022-05-30 16:04:30.426481',2,2),(5,'Yeah, people using summernote are just really annoying.','2022-05-30 16:04:30.426481',5,2),(6,'No, summernote is the Best.','2022-05-30 16:04:30.426481',5,3),(7,'Summernote is pure ****.','2022-05-30 16:04:30.426481',5,5),(8,'Worst game ever.','2022-05-30 16:04:30.426481',4,5),(9,'He is trying to poison us with vaccines XD','2022-05-30 16:04:30.426481',6,5),(10,'Better than Jordan.','2022-05-30 16:04:30.426481',7,5),(11,'Lol 0 rings.','2022-05-30 16:04:30.426481',8,5);
/*!40000 ALTER TABLE `Comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Korisnik`
--

DROP TABLE IF EXISTS `Korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Korisnik` (
  `id` bigint NOT NULL AUTO_INCREMENT,
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
  `isModerator` int NOT NULL,
  `isAdministrator` int NOT NULL,
  `profilePic` varchar(100) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Korisnik`
--

LOCK TABLES `Korisnik` WRITE;
/*!40000 ALTER TABLE `Korisnik` DISABLE KEYS */;
INSERT INTO `Korisnik` VALUES (1,'pbkdf2_sha256$320000$Gc3sKdPpsCWfGZTDRH8k0g$xH4AdEmsb0XSYXikTOUNjg9SwBFxMmAzVwWRt1FgiXk=','2022-05-30 17:28:31.000000',1,'rasa','Rasa','Stojanovic','',1,1,'2022-05-30 16:04:07.000000',0,1,'imgs/mistery.png','Head Admin'),(2,'pbkdf2_sha256$320000$mRkACNbHIzMgbWF5AHDFcp$376rRt+lfY9gW4m2LHBReWD4CNPVt0S57mAGRBpnP1c=','2022-05-30 16:54:37.878412',0,'Dejan13','Dejan','Draskovic','',0,1,'2022-05-30 16:08:05.384314',0,0,'imgs/dejan.jpg','Godine : 22\r\nStudent Elektrotehnickog fakulteta u Beogradu\r\nIma psa Limu \r\nHobiji : Anime , Lav Tolstoj, i grcki kino.'),(3,'pbkdf2_sha256$320000$uEYnkLUYPkn5r8bBq35dP1$unvxnzA72zL0IvvAWvGf/7fdt1hMnhXeyWSRakw83FM=','2022-05-30 17:09:44.000000',0,'IlijaM','Ilija','Markovic','',0,1,'2022-05-30 16:13:00.000000',0,1,'imgs/vijetnam.jpg','Godine: 21\r\nHobiji : Tenis, Gluma, kao i davanje glasova ratnim filmovima Vijetnama'),(4,'pbkdf2_sha256$320000$SnhmdJMH5F3wLO6Excwwrr$4PyScuIAVwdCuADIQfgYp36j9wVGsM/eWxBQP8iRJUs=','2022-05-30 17:12:52.000000',0,'Brka','Marko','Brkic','',0,1,'2022-05-30 16:45:53.000000',0,1,'imgs/brka.jpg','Godine : 21\r\nZanimanje : Student Elektrotehnickog fakulteta u Beogradu\r\nHobiji: U slobodno vreme igra LeagueOfLegends i kninji korisnika IlijuM zato sto koristi summernote.'),(5,'pbkdf2_sha256$320000$vGZmDM1hjCmaCztjyyQYSr$2JikG8lq4y8h3wDTpIrb6UMRi4EFII9k5IApJO1jUvo=','2022-05-30 17:15:30.000000',0,'RixRasa','Rasa','Stojanovic','',0,1,'2022-05-30 17:15:29.000000',1,0,'imgs/281842549_337527631664948_7933331147465596433_n.jpg','Godine :21\r\nHobiji: operacije prednjih ukrstenih ligamenata\r\nStvari koje ne volim : SUMMERNOTE');
/*!40000 ALTER TABLE `Korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KorisnikArticleGrade`
--

DROP TABLE IF EXISTS `KorisnikArticleGrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `KorisnikArticleGrade` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `grade` int NOT NULL,
  `articleId` int NOT NULL,
  `korisnikId` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `KorisnikArticleGrade_articleId_korisnikId_10c9268e_uniq` (`articleId`,`korisnikId`),
  KEY `KorisnikArticleGrade_korisnikId_09629abd_fk_Korisnik_id` (`korisnikId`),
  CONSTRAINT `KorisnikArticleGrade_articleId_b4e2da6e_fk_Article_articleId` FOREIGN KEY (`articleId`) REFERENCES `Article` (`articleId`),
  CONSTRAINT `KorisnikArticleGrade_korisnikId_09629abd_fk_Korisnik_id` FOREIGN KEY (`korisnikId`) REFERENCES `Korisnik` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KorisnikArticleGrade`
--

LOCK TABLES `KorisnikArticleGrade` WRITE;
/*!40000 ALTER TABLE `KorisnikArticleGrade` DISABLE KEYS */;
/*!40000 ALTER TABLE `KorisnikArticleGrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KorisnikLikedArticle`
--

DROP TABLE IF EXISTS `KorisnikLikedArticle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `KorisnikLikedArticle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `articleId` int NOT NULL,
  `korisnikId` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `KorisnikLikedArticle_korisnikId_articleId_74a8335b_uniq` (`korisnikId`,`articleId`),
  KEY `KorisnikLikedArticle_articleId_164e601f_fk_Article_articleId` (`articleId`),
  CONSTRAINT `KorisnikLikedArticle_articleId_164e601f_fk_Article_articleId` FOREIGN KEY (`articleId`) REFERENCES `Article` (`articleId`),
  CONSTRAINT `KorisnikLikedArticle_korisnikId_48fadbec_fk_Korisnik_id` FOREIGN KEY (`korisnikId`) REFERENCES `Korisnik` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KorisnikLikedArticle`
--

LOCK TABLES `KorisnikLikedArticle` WRITE;
/*!40000 ALTER TABLE `KorisnikLikedArticle` DISABLE KEYS */;
INSERT INTO `KorisnikLikedArticle` VALUES (11,3,2),(9,5,2),(10,6,2),(12,8,2),(1,2,3),(3,1,4),(2,2,4),(8,3,4),(7,4,4),(14,2,5),(15,3,5),(13,5,5),(16,7,5),(18,10,5);
/*!40000 ALTER TABLE `KorisnikLikedArticle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Korisnik_groups`
--

DROP TABLE IF EXISTS `Korisnik_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Korisnik_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnik_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Korisnik_groups_korisnik_id_group_id_db032ddd_uniq` (`korisnik_id`,`group_id`),
  KEY `Korisnik_groups_group_id_980cdc2e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Korisnik_groups_group_id_980cdc2e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `Korisnik_groups_korisnik_id_a52b6905_fk_Korisnik_id` FOREIGN KEY (`korisnik_id`) REFERENCES `Korisnik` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Korisnik_groups`
--

LOCK TABLES `Korisnik_groups` WRITE;
/*!40000 ALTER TABLE `Korisnik_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `Korisnik_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Korisnik_user_permissions`
--

DROP TABLE IF EXISTS `Korisnik_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Korisnik_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnik_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Korisnik_user_permission_korisnik_id_permission_i_6d3ef4bb_uniq` (`korisnik_id`,`permission_id`),
  KEY `Korisnik_user_permis_permission_id_c771180b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Korisnik_user_permis_permission_id_c771180b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `Korisnik_user_permissions_korisnik_id_1478424b_fk_Korisnik_id` FOREIGN KEY (`korisnik_id`) REFERENCES `Korisnik` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Korisnik_user_permissions`
--

LOCK TABLES `Korisnik_user_permissions` WRITE;
/*!40000 ALTER TABLE `Korisnik_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Korisnik_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Question`
--

DROP TABLE IF EXISTS `Question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Question` (
  `questionId` int NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `answer1` varchar(50) DEFAULT NULL,
  `answer2` varchar(50) DEFAULT NULL,
  `answer3` varchar(50) DEFAULT NULL,
  `answer4` varchar(50) DEFAULT NULL,
  `points` int NOT NULL,
  `correct` int NOT NULL,
  `articleId` int NOT NULL,
  PRIMARY KEY (`questionId`),
  KEY `Question_articleId_f9718030_fk_Article_articleId` (`articleId`),
  CONSTRAINT `Question_articleId_f9718030_fk_Article_articleId` FOREIGN KEY (`articleId`) REFERENCES `Article` (`articleId`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Question`
--

LOCK TABLES `Question` WRITE;
/*!40000 ALTER TABLE `Question` DISABLE KEYS */;
INSERT INTO `Question` VALUES (1,'At what age did Yvon died?','68','62','70','66',10,1,1),(2,'Where was he born?','Cholon','Chicago','Belgrade','Stepojevac',5,1,1),(3,'Who lost the Vietnam War?','USA','Vietnam','France','Montenegro',4,1,2),(4,'When did vietnam war started','November 1, 1955','November 10, 1954','December 15, 1953','December 1, 1956',8,1,2),(5,'How many civilians died in vietnam war','2,000,000 civilians on both sides','2,500,000 civilians on both sides','2,800,000 civilians on both sides','2,200,000 civilians on both sides',8,1,2),(6,'What company does Elon own?','SpaceX','Microsoft','Maxi','Swisslion',10,1,3),(7,'How rich is bill gates?','$133.8 billion','$123.5 billion','$134.9 billion','$143.7 billion',10,1,6),(8,'How rich is magic?','700 million $','750 million $','605 million $','600 million $',8,4,7),(9,'Where was Magic Johnson born','Michigan, United States','Michigan, Romania','Texas, United States','Florida, United States',8,1,7),(10,'Magic Johnson last team?','Los Angeles Lakers','New York Knicks','KK Radnicki','BC Olympiacos',8,1,7),(11,'Messi age?','34','35','33','32',8,1,9),(12,'Messi hometown?','Rosario, Argentina','Buenos Aires, Argentina','Madrid, Spain','Sombor, Serbia',12,1,9),(13,'George ingame nickname?','HotShot','ColdShot','DoubleLift','Faker',10,1,11),(14,'???','WE','ARE','WATCHING','YOU',10000,4,12);
/*!40000 ALTER TABLE `Question` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add korisnik',6,'add_korisnik'),(22,'Can change korisnik',6,'change_korisnik'),(23,'Can delete korisnik',6,'delete_korisnik'),(24,'Can view korisnik',6,'view_korisnik'),(25,'Can add article',7,'add_article'),(26,'Can change article',7,'change_article'),(27,'Can delete article',7,'delete_article'),(28,'Can view article',7,'view_article'),(29,'Can add category',8,'add_category'),(30,'Can change category',8,'change_category'),(31,'Can delete category',8,'delete_category'),(32,'Can view category',8,'view_category'),(33,'Can add question',9,'add_question'),(34,'Can change question',9,'change_question'),(35,'Can delete question',9,'delete_question'),(36,'Can view question',9,'view_question'),(37,'Can add comment',10,'add_comment'),(38,'Can change comment',10,'change_comment'),(39,'Can delete comment',10,'delete_comment'),(40,'Can view comment',10,'view_comment'),(41,'Can add korisnik liked article',11,'add_korisniklikedarticle'),(42,'Can change korisnik liked article',11,'change_korisniklikedarticle'),(43,'Can delete korisnik liked article',11,'delete_korisniklikedarticle'),(44,'Can view korisnik liked article',11,'view_korisniklikedarticle'),(45,'Can add korisnik article grade',12,'add_korisnikarticlegrade'),(46,'Can change korisnik article grade',12,'change_korisnikarticlegrade'),(47,'Can delete korisnik article grade',12,'delete_korisnikarticlegrade'),(48,'Can view korisnik article grade',12,'view_korisnikarticlegrade'),(49,'Can add article category',13,'add_articlecategory'),(50,'Can change article category',13,'change_articlecategory'),(51,'Can delete article category',13,'delete_articlecategory'),(52,'Can view article category',13,'view_articlecategory'),(53,'Can add attachment',14,'add_attachment'),(54,'Can change attachment',14,'change_attachment'),(55,'Can delete attachment',14,'delete_attachment'),(56,'Can view attachment',14,'view_attachment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Korisnik_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Korisnik_id` FOREIGN KEY (`user_id`) REFERENCES `Korisnik` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-05-30 17:28:45.430440','4','Brka',2,'[{\"changed\": {\"fields\": [\"IsAdministrator\"]}}]',6,1),(2,'2022-05-30 17:29:00.519399','3','IlijaM',2,'[{\"changed\": {\"fields\": [\"IsAdministrator\"]}}]',6,1),(3,'2022-05-30 17:29:07.943443','5','RixRasa',2,'[{\"changed\": {\"fields\": [\"IsModerator\"]}}]',6,1),(4,'2022-05-30 17:29:54.062521','1','rasa',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"IsAdministrator\", \"ProfilePic\", \"Description\"]}}]',6,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(14,'django_summernote','attachment'),(7,'learnopedia','article'),(13,'learnopedia','articlecategory'),(8,'learnopedia','category'),(10,'learnopedia','comment'),(6,'learnopedia','korisnik'),(12,'learnopedia','korisnikarticlegrade'),(11,'learnopedia','korisniklikedarticle'),(9,'learnopedia','question'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-05-30 16:03:23.745846'),(2,'contenttypes','0002_remove_content_type_name','2022-05-30 16:03:23.817435'),(3,'auth','0001_initial','2022-05-30 16:03:24.230920'),(4,'auth','0002_alter_permission_name_max_length','2022-05-30 16:03:24.324792'),(5,'auth','0003_alter_user_email_max_length','2022-05-30 16:03:24.340705'),(6,'auth','0004_alter_user_username_opts','2022-05-30 16:03:24.352913'),(7,'auth','0005_alter_user_last_login_null','2022-05-30 16:03:24.366996'),(8,'auth','0006_require_contenttypes_0002','2022-05-30 16:03:24.376784'),(9,'auth','0007_alter_validators_add_error_messages','2022-05-30 16:03:24.389529'),(10,'auth','0008_alter_user_username_max_length','2022-05-30 16:03:24.401046'),(11,'auth','0009_alter_user_last_name_max_length','2022-05-30 16:03:24.412207'),(12,'auth','0010_alter_group_name_max_length','2022-05-30 16:03:24.434379'),(13,'auth','0011_update_proxy_permissions','2022-05-30 16:03:24.445554'),(14,'auth','0012_alter_user_first_name_max_length','2022-05-30 16:03:24.456628'),(15,'learnopedia','0001_initial','2022-05-30 16:03:25.751555'),(16,'admin','0001_initial','2022-05-30 16:03:25.946676'),(17,'admin','0002_logentry_remove_auto_add','2022-05-30 16:03:25.963402'),(18,'admin','0003_logentry_add_action_flag_choices','2022-05-30 16:03:25.983757'),(19,'django_summernote','0001_initial','2022-05-30 16:03:26.021549'),(20,'django_summernote','0002_update-help_text','2022-05-30 16:03:26.030447'),(21,'django_summernote','0003_alter_attachment_id','2022-05-30 16:03:26.088933'),(22,'sessions','0001_initial','2022-05-30 16:03:26.150132');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ghfg5glvs7goziizd44q2889jz8svoe0','.eJxVjEEOwiAQRe_C2pABSgGX7j0DmYFBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4ZXEWSpx-N8L04LaDfMd2m2Wa27pMJHdFHrTL65z5eTncv4OKvX5riwg5BRgUqDJ4lYrXoJJnCyb4YsDpoC1TsYnI2BHIjU6x1mQKArB4fwDLHDdU:1nvjBv:rc1W5Syu2OzlD7hn1FLgXdxAEloMQvcZSKYprmUNpSc','2022-06-13 17:28:31.202404');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_summernote_attachment`
--

DROP TABLE IF EXISTS `django_summernote_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_summernote_attachment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_summernote_attachment`
--

LOCK TABLES `django_summernote_attachment` WRITE;
/*!40000 ALTER TABLE `django_summernote_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_summernote_attachment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-30 19:42:30
