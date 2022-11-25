create database borrar;
#select * from borrar;

create table borrar.usuarios (
  nombre varchar(30),
  apellido varchar(10)
 );

insert into borrar.usuarios (nombre, apellido) values ('Leonardo','Reyes');
insert into borrar.usuarios (nombre, apellido) values ('MarioPerez','Muñoz'); 
insert into borrar.usuarios (nombre, apellido) values ('MarioPerez','Martinez'); 
insert into borrar.usuarios (nombre, apellido) values ('Marcelo','Rivera');
insert into borrar.usuarios (nombre, apellido) values ('Gustavo','Rivera');

select * from borrar.usuarios;

delete from borrar.usuarios where nombre='Marcelo';

delete from borrar.usuarios where apellido='River';

insert into borrar.usuarios (nombre) values ('Adonis');

delete from borrar.usuarios where nombre='Leonardo';

update borrar.usuarios set apellido=null
 where apellido='Rivera';