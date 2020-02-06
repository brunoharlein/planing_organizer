from .entity import Entity

class Conference(Entity):
    """Class inheriting from entity representing the conferences stored in database
        Classe héritant de l'entité représentant les conférences stockées dans la base de données"""

    def __init__(self, data=False):
        # call the mother class constructor
        # appeler le constructeur de la classe mère
        super().__init__()
        self.title = None
        self.summary = None
        self.event_date = None
        self.registering_date = None
        self.event_time = None
        self.speaker = None
        # if there is a dictionnary the hydrate the object
        # s'il y a un dictionnaire, hydrate l'objet
        if data:
            self.hydrate(data)

    def __str__(self):
        """Define the way the object is printed
            Définissez la façon dont l'objet est "printé"""
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\ntitle: {}\nsummary: {}\ndate: {}\nhour: {}\nspeaker: {}\n".format(
            self.id,
            self.title,
            self.summary,
            self.event_date.strftime("%d/%m/%Y"),
            self.event_time.strftime("%H:%M"),
            self.speaker.firstname + " " + self.speaker.lastname
        )


