show databases;
create database medicaldb;   -- 创建医疗系统数据库medicaldb
show databases;
use medicaldb;


-- 0.1-SQL 在 "users_personal" 表创建时在 "id" 列创建 PRIMARY KEY 约束, 而且这个users表是独立于医疗信息之外的, 用户信息和医疗平台数据信息互相独立
CREATE TABLE users_personal
(
name varchar(255) NOT NULL PRIMARY KEY,
tel varchar(255) NOT NULL,
email_address varchar(255) NOT NULL,
gender varchar(255) NOT NULL,
birthdate varchar(255) NOT NULL,
job varchar(255) NOT NULL
);
DESC users_personal; -- 建表后查看数据结构

-- 0-SQL 在 "users" 表创建时在 "id" 列创建 PRIMARY KEY 约束, 而且这个users表是独立于医疗信息之外的
CREATE TABLE users
(
id int auto_increment UNIQUE KEY,
username varchar(255) NOT NULL PRIMARY KEY,
password varchar(255) NOT NULL,
name varchar(255) NOT NULL,
creation_date varchar(255) NOT NULL,
FOREIGN KEY (name) REFERENCES users_personal(name)
);
DESC users; -- 建表后查看数据结构

-- 分割线...


-- ①SQL 在 "patients" 表创建时在 "pt_id" 列创建 PRIMARY KEY 约束.......................................................................................
CREATE TABLE patients
(
pt_name varchar(255) NOT NULL PRIMARY KEY,
age int NOT NULL,
gender varchar(255) NOT NULL,
tel varchar(255) NOT NULL,
address varchar(255)，
creation_date varchar(255) NOT NULL
);
DESC patients; -- 建表后查看数据结构


-- ②SQL 在 "medical_records" 表创建时在 "med_id" 列创建 PRIMARY KEY 约束..............................................................................
CREATE TABLE medical_records
(
med_id int NOT NULL PRIMARY KEY,
creation_date varchar(255) NOT NULL,
allergic_history varchar(255) ,
drug_history varchar(255) 
);
DESC medical_records; -- 建表后查看数据结构

-- ③SQL 在 "disease_records" 表创建时在 "dis_id" 列创建 PRIMARY KEY 约束.................................................................
CREATE TABLE disease_records
(
dis_type  varchar(255)  NOT NULL PRIMARY KEY,
level int NOT NULL,
cure_methods varchar(255) 
);
DESC disease_records; -- 建表后查看数据结构

-- ④SQL 在 "doctors" 表创建时在 "doc_id" 列创建 PRIMARY KEY 约束
CREATE TABLE doctors
(
doc_name varchar(255) NOT NULL PRIMARY KEY,
age int  NOT NULL,
tel varchar(255) NULL,
gender varchar(255) NOT NULL,
introduction varchar(255) 
);
DESC doctors; -- 建表后查看数据结构

-- ⑤SQL 在 "departments" 表创建时在 "dep_id" 列创建 PRIMARY KEY 约束
CREATE TABLE departments
(
dep_name varchar(255) NOT NULL PRIMARY KEY,
location varchar(255) NOT NULL,
introduction varchar(255) 
);
DESC departments; -- 建表后查看数据结构

show tables;
