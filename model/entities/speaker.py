from .entity import Entity

class Speaker(Entity):
    """Class inheriting from entity representiong the speakers stored in database"""

    def __init__(self, data=False):
        # call the mother class constructor
        # appeler le constructeur de la classe mère
        super().__init__()
        self.firstname = None
        self.lastname = None
        self.job = None
        self.description = None
        self.is_active = None
        # if there is a dictionnary the hydrate the object
        # s'il y a un dictionnaire, hydrate l'objet
        if data:
            self.hydrate(data)


    def __str__(self):
        """Define the way the object is printed
            Définissez la façon dont l'objet est "printé"""
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\nfirstname: {}\nlastname: {}\njob: {}\ndescription: {}\n".format(
        self.id, self.firstname, self.lastname, self.job, self.description)
