class Figura:
    """klasa figura zawiera metodę przesuń"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def przesun(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Kwadrat(Figura):
    """Klasa kwadrat dziedziczy po figura"""

    def __init__(self, bok=1, x=0, y=0):
        Figura.__init__(self, x, y)
        self.bok = bok


class Kolo(Figura):
    pi = 3.14159

    def __init__(self, r=1, x=0, y=0):
        Figura.__init__(self, x, y)
        self.promień = r

    def pole(self):
        return self.promień*self.promień*self.pi

    def __str__(self):
        return "Koło o promieniu %s i położeniu (%d , %d)" \
            % (self.promień, self.x, self.y)
