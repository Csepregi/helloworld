from dakar import Dakar

class Motor(Dakar):

    speed_limit = 80

    def __init__(self, speed, benzin):
        super().__init__()