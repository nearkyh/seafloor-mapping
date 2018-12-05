
show databases;

show tables;

create database seafloor_mapping;

use seafloor_mapping;

create table `data`(
`_id` int(10) not null auto_increment,
`latitude` int(10) default null comment 'latitude',
`longitude` int(10) default null comment 'longitude',
`depth` int(10) default null comment 'depth',
`timestamp` varchar(500) default null comment 'time stamp',
key `_id` (`_id`)
) engine=InnoDB default charset=utf8;

create table `data2`(
`_id` int(10) not null auto_increment,
`latitude` char(10) default null comment 'latitude',
`longitude` char(10) default null comment 'longitude',
`depth` char(10) default null comment 'depth',
`timestamp` varchar(500) default null comment 'time stamp',
key `_id` (`_id`)
) engine=InnoDB default charset=utf8;

INSERT INTO `seafloor_mapping`.`data` (
`_id`, `latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
'1', '0', '1', '-6', '154017038.7213247'
);

select * from data;

drop table data;


INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
35.153056,129.131650,51.0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
35.153055,129.131761,52.0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
35.153054,129.131872,51.0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`_id`, `latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,3,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,4,8.9,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,5,8.2,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,6,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,7,7.2,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,8,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,9,6.7,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,10,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,11,5.4,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,12,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,13,3.2,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,14,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,15,2.7,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,16,2.4,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,17,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,18,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,19,1,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,20,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,21,0.8,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,22,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,23,-2.7,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,24,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,25,-3.8,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,26,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,27,4.5,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,28,0,0
);

INSERT INTO `seafloor_mapping`.`data` (
`latitude`, `longitude`, `depth`, `timestamp`
) VALUES (
0,29,0,0
);
