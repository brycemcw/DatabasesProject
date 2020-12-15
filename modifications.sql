DROP TABLE IF EXISTS `user`;
SET character_set_client = utf8mb4;
CREATE TABLE `user` (
    `ID` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL,
		`password_hash` varchar(128) NOT NULL,
    `favoriteTeam` varchar(50) DEFAULT NULL,
		`favoriteYear` int(11) DEFAULT NULL,
    PRIMARY KEY (`ID`),
    UNIQUE KEY `ID` (`username`,`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


ALTER TABLE batting
ADD COLUMN PA smallint(6) DEFAULT NULL AFTER GIDP;

ALTER TABLE batting
ADD COLUMN BA double DEFAULT NULL AFTER PA;

ALTER TABLE batting
ADD COLUMN OBpercent double DEFAULT NULL AFTER BA;

ALTER TABLE batting
ADD COLUMN SLUGpercent double DEFAULT NULL AFTER OBpercent;

ALTER TABLE pitching
ADD COLUMN IP double DEFAULT NULL AFTER SV;

alter table batting rename column 3b to b3;
alter table batting rename column 2b to b2;
alter table teams rename column 2b to b2;
alter table teams rename column 3b to b3;


--Web User Permissions
grant select on baseball.* to web@localhost;
grant update on baseball.batting to web@localhost;
grant update on baseball.pitching to web@localhost;
grant update on baseball.user to web@localhost;
