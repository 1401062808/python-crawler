TABLES = {}
TABLES['urls'] = (
    "CREATE TABLE `urls` ("
    "  `index` int(11) NOT NULL AUTO_INCREMENT," # index of queue
    "  `url` varchar(512) NOT NULL,"
    "  `md5` varchar(32) NOT NULL,"
    "  `status` varchar(11) NOT NULL DEFAULT 'new'," # could be new, downloading and finish
    "  `depth` int(11) NOT NULL,"
    "  `queue_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "  `done_time` timestamp NOT NULL DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`index`),"
    "  UNIQUE KEY `md5` (`md5`)"
    ") ENGINE=InnoDB")
for name, ddl in TABLES.iteritems():
    print('name:', name, '\n')
    print('ddl:', ddl, '\n')
