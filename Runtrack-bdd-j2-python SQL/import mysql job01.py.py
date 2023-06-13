import mysql.connector


# creation d'une connexion a la base de donnée
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Azerty06!",
    database="LaPlateforme"
)

# créer un curseur de base de donnée pour effectuer des operations SQL
mycursor=mydb.cursor()

#executer le curseur avec la methode execute()et transmis la requete SQL
mycursor.execute("SELECT * FROM etudiants")

# Rcuperer toutes les lignes de la derniere instruction executée
res = mycursor.fetchall()

for x in res:
    print(x)

mycursor.execute("select nom,capacite From salles")

res=mycursor.fetchall()

for x in res:
    print(x)


mycursor.execute("SELECT SUM(superficie) From etage ")

res=mycursor.fetchall()

for x in res:
    print("la superficie de la Plateforme est de " , (x),"m2" )


mycursor.execute("SELECT SUM(capacite) FROM salles")

res=mycursor.fetchall()

for x in res:
    print("La capacité de toute les salles est de : ", x)

mycursor.execute("SELECT *  FROM employes WHERE salaire >3000")

res=mycursor.fetchall()

for x in res:
    print(x)


