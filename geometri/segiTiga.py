class SegiTiga():
    def __init__(self,a,t):
        self.a = a
        self.t = t

    def info(self):
        return f'Luas segitiga dengan alas {self.a} dan {self.t} adalah'

    def hitung_luas(self):
        return 0.5 * self.a * self.t