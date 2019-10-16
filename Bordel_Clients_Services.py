class Client:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget

    def __str__(self):
        return f"Je m'appèle {self.name} et je possède {self.budget}€"


class Service:

    def __init__(self, duree, type, femelle, client):
        """

        :param duree: en minutes
        :param type:
        :param femelle:
        :param client:
        """
        self.duree = duree
        self.type = type
        self.femelle = femelle
        self.client = client

    def __str__(self):
        return f"La {self.type} pour {self.client} avec les femelle n°{self.femelle} durera {self.duree}."

