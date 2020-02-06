import psycopg2
import psycopg2.extras

class Connection():
    """Class to manage the connection, the cursor and the requests to a database
        Classe pour gérer la connexion, le curseur et les requêtes vers une base de données"""
    # Store the username, the port and the database name as class attributs
    # In this case no host name and password because of my own configuration
    # Stockez le nom d'utilisateur, le port et le nom de la base de données en tant qu'attributs de classe
    # Dans ce cas, pas de nom d'hôte et de mot de passe en raison de ma propre configuration
    USER = "brunoharlein"
    PORT = "5432"
    DATABASE = "planning"

    def __init__(self):
        # The class stores an instance of pyscopg2 connection and cursor classes
        # La classe stocke une instance de connexion pyscopg2 et des classes de curseur
        self.connection = None
        self.cursor = None

    def initialize_connection(self):
        """Instanciate a connection and a cursor and store them in the related attributs
            Instancier une connexion et un curseur et les stocker dans les attributs associés"""
        try:
            self.connection = psycopg2.connect(user=Connection.USER,
                                               port=Connection.PORT,
                                               database=Connection.DATABASE)
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def close_connection(self):
        """Close both connection and cursor
            Fermer la connexion et le curseur"""
        if(self.connection):
            self.cursor.close()
            self.connection.close()

    def make_request(self, sql, arguments=False, message=False):
        """General method to handle a sql request with arguments and an error message
            Méthode générale pour gérer une requête SQL avec des arguments et un message d'erreur"""
        try:
            self.initialize_connection()
            # execute the given SQL query with arguments if there are
            # exécuter la requête SQL donnée avec des arguments s'il y a
            self.cursor.execute(sql, arguments)
            # if the request is of type SELECT we return a fetch with all results
            # si la demande est de type SELECT, nous renvoyons une recherche avec tous les résultats
            if sql.lower().startswith("select", 0):
                return self.cursor.fetchall()
            # if it is not a select then we have to commit whatever happens
            # si ce n'est pas un SELECT, nous devons engager(enregistrer) quoi qu'il arrive
            self.connection.commit()
            # if the request is of type DELETE we have to know if something has been deleted
            # si la requête est de type DELETE nous devons savoir si quelque chose a été supprimé
            if sql.lower().startswith("delete", 0):
                # if nothing has been deleted
                # si rien n'a été effacer
                if self.cursor.rowcount == 0:
                    raise Exception("Nothing found")
                return self.cursor.rowcount
            # if the request was of type INSERT INTO and was a success then return True
            # si la requête était de type INSERT INTO et a été un succès, retournez True
            return True
        except Exception as e:
            # If a specefic message has been given print it otherwise print the exception
            # Si un message spécifique a été donné, imprimez-le sinon imprimez l'exception
            if message:
                print(message)
            else:
                print(e)
            return False
        finally:
            self.close_connection()

