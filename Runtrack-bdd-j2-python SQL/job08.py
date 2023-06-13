import mysql.connector

class ZooManager:
    def __init__(self, config):
        self.config = config
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def add_animal(self, id, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (id, nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id, nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print("Nouvel animal ajouté avec succès.")

    def remove_animal(self, id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print("Animal supprimé avec succès.")

    def update_animal(self, id, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print("Animal mis à jour avec succès.")

    def add_cage(self, id, superficie, capacite_max):
        query = "INSERT INTO cage (id, superficie, capacite_max) VALUES (%s, %s, %s)"
        values = (id, superficie, capacite_max)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print("Nouvelle cage ajoutée avec succès.")

    def remove_cage(self, id):
        query = "DELETE FROM cage WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print("Cage supprimée avec succès.")

    def update_cage(self, id, superficie, capacite_max):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
        values = (superficie, capacite_max, id)
        self.cursor.execute(query, values)
        self.cnx.commit()
        print("Cage mise à jour avec succès.")


    def get_all_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animals = self.cursor.fetchall()
        for animal in animals:
            print(animal)

    
    def calculate_total_cage_area(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        total_area = self.cursor.fetchone()[0]
        print(f"La superficie totale de toutes les cages est de : {total_area} m².")

    def close_connection(self):
        self.cursor.close()
        self.cnx.close()
        print("Connexion à la base de données fermée.")
        

    config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Azerty06!',
    'database': 'zoo'
    }

    
