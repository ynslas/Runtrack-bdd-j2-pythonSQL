#À l’aide du SQL et python, développer un programme permettant la gestion d’un zoo.

Chaque animal possède un identifiant qui l’identifie de façon unique, un nom , une race,
l’id du type de cage, une date de naissance et un pays d’origine.

Une cage peut contenir un ou plusieurs animaux, mais peu être aussi vide. Chaque cage
a un identifiant unique, une superficie et une capacité maximum.

À l’aide des informations ci-dessus, créer une base de données nommée zoo et créer la
table animal et la table cage.

 create database ZOO ;
 
  CREATE TABLE animal (
    ->   id INT PRIMARY KEY,
    ->   nom VARCHAR(255),
    ->   race VARCHAR(255),
    ->   id_cage INT,
    ->   date_naissance DATE,
    ->   pays_origine VARCHAR(255)
    -> );
	
	
	CREATE TABLE cage (
    ->   id INT PRIMARY KEY,
    ->   superficie DECIMAL(8,2),
    ->   capacite_max INT
    -> );
	
	