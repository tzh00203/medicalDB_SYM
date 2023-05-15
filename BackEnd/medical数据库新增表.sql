use medicaldb;
CREATE TABLE departments_consist
(
dep_name varchar(255) NOT NULL,
doc_name varchar(255) NOT NULL,
level int NOT NULL,
join_date varchar(255) NOT NULL,
PRIMARY KEY (dep_name, doc_name)
);
DESC departments_consist; -- 建表后查看数据结构

CREATE TABLE patients_med_disease
(
pt_name varchar(255) NOT NULL ,
med_id int  NOT NULL  ,

dis_date varchar(255) NOT NULL,
dis_type varchar(255) NOT NULL ,
doc_name varchar(255) NOT NULL ,
PRIMARY KEY (pt_name, med_id,dis_date),
FOREIGN KEY (pt_name) references patients(pt_name),
FOREIGN KEY (dis_type) references disease_records(dis_type),
FOREIGN KEY (doc_name)  references doctors(doc_name)
);
DESC patients_med_disease; -- 建表后查看数据结构


