create database juego;
use juego;

create table destino
(
id int auto_increment not null primary key, palabra varchar(20) not null
);

create table origen
(
id int auto_increment not null primary key, palabra varchar(20) not null
);

create table score
(
	id int auto_increment primary key not null, nombre text, ahorcado int, gato int,puntos int 
);