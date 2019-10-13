create database juego;
use juego;

create table jugadores 
(
id int auto_increment not null primary key,nombre varchar(20)not null
);

create table destino
(
id int auto_increment not null primary key, palabra varchar(20) not null
);

create table origen
(
id int auto_increment not null primary key, palabra varchar(20) not null
);