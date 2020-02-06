# coding: utf-8

from model.conferenceModel import conferenceModel
from model.entities.conference import Conference

class conferenceView():
    """View or controller taking care of all the logic related to conference in the app.
        Vue ou contrôleur prenant en charge toute la logique liée à la conférence dans l'application."""
    model = conferenceModel()

    def __init__(self):
        pass

    def show_conferences(self):
        """Display all the conferences from database to the screen"""
        # retrieve conferences from the database
        # récupérer les conférences de la base de données
        conferences = conferenceView.model.get_conferences()
        # if we have conferences we show them in a loop
        # si nous avons des conférences, nous les montrons en boucle
        if conferences:
            for conference in conferences:
                print(conference)
        # otherwise we print a message
        # sinon nous imprimons un message
        else:
            print("Nous n'avons aucune conférence de prévue pour l'instant")
        input("Appuyez sur une touche pour continuer")

    def new_conference(self):
        """Displays inputs to register a new conference in the database"""
        # start an empty dictionnary to hold conference's information
        # démarrer un dictionnaire vide pour organiser des informations sur les conférences
        data = {}
        data["title"] = input("Titre : ")
        data["summary"] = input("Résumé : ")
        data["event_date"] = input("Date (jj/mm/aaaa): ")
        data["event_time"] = input("Heure (hh:mm): ")
        data["speaker"] = input("Id de l'intervenant : ")
        # instanciate a conferance with the info
        # instancier une conférence avec l'info
        conference = Conference(data)
        # if the registering is succesfull print a success message
        # si l'enregistrement est réussi, imprimer un message de réussite
        if conferenceView.model.add_conference(conference):
            print("la conférence a bien été enregistrée")

    def delete_conference(self):
        """Display an input to delete a conference from database by his ID"""
        id = input("L'id de la conférence à annuler : ")
        # if the delete is succesfull print a success message
        # si la suppression est réussie, imprimer un message de réussite
        if conferenceView.model.delete_conference(id):
            print("La conférence a bien été supprimée")
