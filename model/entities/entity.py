class Entity():
    """Class representing the mother entity class
        Classe représentant la classe d'entité mère"""

    def __init__(self, data=False):
        # every entity must have an ID
        # chaque entité doit avoir un ID
        self.id = None

    def hydrate(self, data):
        """Set object's attributs value if they exists from a dictionnary
            Définir la valeur des attributs de l'objet s'ils existent dans un dictionnaire"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
