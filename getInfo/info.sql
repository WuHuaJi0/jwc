CREATE database allinfo;

use allinfo;

CREATE table info(
	id int(12) unsigned NOT NULL AUTO_INCREMENT primary key,
	username varchar(30),
	name varchar(30),
	birth varchar(30),
	minzu varchar(20),
	idNum varchar(30),
	xueyuan varchar(30),
	major varchar(30),
	kaoshenghao varchar(30),
	kaoshengleibie varchar(30),
	shengao varchar(30),
	tizhong varchar(30),
	dizhi varchar(30),
	jiatingdianhua varchar(30),
	benrendianhua varchar(30),
	jinji varchar(30),
	jinjidianhua varchar(30),
	qq varchar(30),
	youjian varchar(30),
	wechat varchar(30),
	nhCard varchar(30),
	brothNum varchar(30),
	familyNum varchar(30),
	allYearEarn varchar(30),
	address varchar(30),
	hukouAttr varchar(30)
);