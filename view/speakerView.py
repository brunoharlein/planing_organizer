from model.speakerModel import speakerModel
from model.entities.speaker import Speaker

class speakerView():
    """View or controller taking care of all the logic related to speaker in the app.
        Vue ou contrôleur prenant en charge toute la logique liée au speaker dans l'application."""
    model = speakerModel()

    def __init__(self):
        pass

    def show_speakers(self):
        """Display all the speakers from database to the screen
            Afficher tous les speaker de la base de données à l'écran"""
        # retrieve speakers from database
        # récupérer les intervenants de la base de données
        speakers = speakerView.model.get_speakers()
        # if we have speakers we show them in a loop
        # si nous avons des speakers, nous les montrons en boucle
        if speakers:
            for speaker in speakers:
                print(speaker)
        # otherwise we print a message
        # sinon nous imprimons un message
        else:
            print("pas d'intervenants")
        input("Appuyez sur une touche pour continuer")

    def new_speaker(self):
        """Displays inputs to register a new speaker in the database
            Affiche les entrées pour enregistrer un nouveau speaker dans la base de données"""
        # start an empty dictionnary to hold speaker's information
        # démarrer un dictionnaire vide pour contenir les informations sur les speakers
        data = {}
        data["firstname"] = input("Prénom : ")
        data["lastname"] = input("Nom : ")
        data["job"] = input("Profession : ")
        data["description"] = input("Présentation : ")
        # instanciate a speaker with the info
        speaker = Speaker(data)
        # if the registering is succesfull print a success message
        if speakerView.model.add_speaker(speaker):
            print("Le nouvel intervenant a bien été enregistré")

    def delete_speaker(self):
        """Display an input to delete a speaker from database by his ID
            Afficher une entrée pour supprimer un speaker de la base de données par son ID"""
        id = input("L'id de l'intervenant à supprimer : ")
        # if the delete is succesfull print a success message
        # si la suppression est réussie, imprimer un message de réussite
        if speakerView.model.delete_speaker(id):
            print("L'intervenant a bien été supprimé")
