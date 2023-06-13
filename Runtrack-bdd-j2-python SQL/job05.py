#À l’aide d’un requête calculer la superficie de l’ensemble des étages et afficher “La superficie de La Plateforme est de X m2”, X étant le résultat de la requête.

mycursor.execute("SELECT SUM(superficie) From etage ")

res=mycursor.fetchall()

for x in res:
    print("la superficie de la Plateforme est de " , (x),"m2" )