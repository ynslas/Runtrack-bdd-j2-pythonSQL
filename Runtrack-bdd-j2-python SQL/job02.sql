À l'aide de votre terminal SQL, créez les tables suivantes :
- “etage” ayant comme champs :

● id, int, clé primaire et Auto Incrément
● nom, varchar de taille 255
● numero, int
● superficie, int
- “salles” ayant comme champs :

● id, int, clé primaire et Auto Incrément
● nom, varchar de taille 255
● id_etage, int
● capacite, int


 CREATE table etage (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,Nom VARCHAR(255) , numero INT , superficie INT)