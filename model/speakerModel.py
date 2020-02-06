from .connection import Connection
from .entities.speaker import Speaker

class speakerModel():
    """Class to perform all queries related to the speaker table in the database
        Classe pour effectuer toutes les requêtes liées à la table des speaker dans la base de données"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        # Creation d'une instance de la class connection pour acceder à la BDD
        self.db = Connection()

    def get_speakers(self):
        # the query to execute
        sql = """SELECT id, firstname, lastname, job, description from speaker
                 WHERE is_active = true"""
        speakers = self.db.make_request(sql)
        # turn the list of lists returned by the database into a list of objects
        # transformer la liste des listes renvoyées par la base de données en une liste d'objets
        # For each list representing a speaker
        # Pour chaque liste représentant un speaker
        for key, speaker in enumerate(speakers):
            # instanciate a speaker object and store it in the list
            # instancier un objet speaker et le stocker dans la liste
            speakers[key] = Speaker(speaker)
        return speakers

    def add_speaker(self, speaker):
        # the query to execute
        sql = """INSERT INTO speaker (firstname, lastname, job, description)
                 VALUES(%s, %s, %s, %s)"""
        message = "Nous n'avons pas pu réaliser l'enregistrement"
        arguments = (speaker.firstname, speaker.lastname, speaker.job, speaker.description)
        return self.db.make_request(sql, message=message, arguments=arguments)

    def delete_speaker(self, id):
        # the query to execute
        sql = """delete from speaker
                 where id = %s"""
        arguments = (id,)
        message = "Un problème est survenu, nous n'arrivons pas à supprimer l'intervenant d'id {}".format(id)
        return self.db.make_request(sql, arguments=arguments, message=message)
