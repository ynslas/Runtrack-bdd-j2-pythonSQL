# À l’aide d’une requête, calculer la somme des capacités des salles et afficher le résultat en console.


mycursor.execute("SELECT SUM(capacite) FROM salles")

res=mycursor.fetchall()

for x in res:
    print("La capacité de toute les salles est de : ", x)