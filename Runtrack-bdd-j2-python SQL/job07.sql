#Créer une base de données SQL avec une table nommée “employes” contenant les
champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar
- prenom, varchar
- salaire, decimal
- id_service, int


 CREATE TABLE employes (
    ->   id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ->   Nom VARCHAR(255),
    ->   Prenom VARCHAR(255),
    ->   Salaire DECIMAL(6,2),
    ->   id_service INT
    -> );

#Insérer des employées dans la table “employes”.

insert into employes (nom,prenom,salaire,id_service) values ("visor","tom",2800.58,1),("Lebroc","thomas",3200,2),("valduc","lisa",3600.48,3),("gabin","cedric",2458.36,2),("duty","melanie",2789.36,3),("Castel","Jordan",3154.87,4);


#Écrire une requête SQL pour récupérer tout les employées dont le salaire est supérieur à
3 000 €. Exécuter la requête et afficher le résultat.


select * from employes where salaire >3000 ;


#Ajouter la table “services” contenant les champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar

CREATE TABLE SERVICE (
    -> id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    -> nom VARCHAR(255)
    -> );
	
	
#Insérer des services dans votre table.

insert into service ( nom) values ( "secretaire"),("informaticien"),("electricien"),("devellopeur");


#Récupérer tous les employés et leur service respectif. Afficher le résultat en console.

 select * from employes;