create database if not exists TP1;

use TP1;

create table if not exists citations (
    id int auto_increment primary key,
    auteur varchar(255),
    citation varchar(255),
);