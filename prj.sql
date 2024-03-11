create database sms;
use sms;
show tables;

select * from tots;
create table purchase(
pid varchar(50),
cid varchar(50),
item varchar(50),
p_qty int,
purch_p int,
tot int,
pdate varchar(50),
billid int 
);
drop table purchase;
drop table sold;
create table sold(
sid varchar(50),
cid varchar(50),
item varchar(50),
s_qty int,
sold_p int,
tot int,
sdate varchar(50),
billid int not null
);
drop table tots;

create table billp(
bill int,
billid varchar(50),
pdate varchar(50)
);
show tables;
drop table billp;
create table bills(
bill int,
billid varchar(50),
sdate varchar(50)
);
drop table bills;
use sms;
create table bs(
cid varchar(50),
bstock int
);
show tables;
drop table bs;
select * from purchase;
select * from bs;
select * from totp;
select * from purchase;

drop table bs;
create table totp(
cid varchar(50),
totp int
);
drop table totp;
create table tots(
cid varchar(50),
tots int
);
use sms;
show tables;
select * from ptotqty;
select * from sold;
drop table tots;
show tables;
drop table mainbill;
select * from mainbill;
select * from bills;
select * from sold;
create table mainbill(
sno int auto_increment primary key,
itemname varchar(50),
qty int,
price float,
tot float,
billid int
);
drop table mainbill;
select * from mainbill;
show tables;
create table display(
type varchar(50),
itemid varchar(50),
itemname varchar(50),
qty varchar(50),
price varchar(50),
tot varchar(50),
date varchar(50),
billid varchar(50)
);
show tables;
drop table display;
create table totalbill(
billid int,
tot float
);
select * from sold;
drop table sold;
select * from ptotqty;