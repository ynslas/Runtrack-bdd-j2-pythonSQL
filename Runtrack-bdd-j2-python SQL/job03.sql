Ajouter les données suivantes a la table “etage” :
- RDC, 0, 500
- R+1, 1, 500


 insert into etage (nom,numero,superficie) values ("RDC",0,500),("R+1",1,500);

Ajouter les données suivantes a la table “salles” :
- Lounge, 1, 100
- Studio Son, 1, 5
- Broadcasting, 2, 50
- Bocal Peda, 2, 4
- Coworking, 2, 80
- Studio Video, 2, 5

 insert into salles (nom,id_etage,capacite) values ("Lounge",1,100),("Studio son",1,5),("Broadcasting",2,50),("Bocal Peda",2,4),("Coworking",2,80),("Studio Video",2,5);

Exporter votre base de données.

mysqldump -u root -p LaPlateforme > Laplateforme1.sql;

