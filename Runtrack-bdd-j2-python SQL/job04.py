#Écrire un programme qui récupère tous les noms et les capacités de la table “salles” et afficher le résultat en console.

mycursor.execute("select nom,capacite From salles")

res=mycursor.fetchall()

for x in res:
    print(x)