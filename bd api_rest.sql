create database api_test;
USE api_test;
create table tabla_api(
	id_vehiculo int not null auto_increment,
    placa varchar(255),
    pos_ini varchar(255),
    pos_fin varchar(255),
    primary key(id_vehiculo));
select * from tabla_api;
INSERT INTO TABLA_API(id_vehiculo,placa,pos_ini,pos_fin) VALUE ('1', 'AB12CD34', '15', '55');
delete from tabla_api where id_vehiculo=3 ;