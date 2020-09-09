from geometri.bangunRuang import BangunRuang


class SegiTiga(BangunRuang):
    def __init__(self,a,t):
        self.a = a
        self.t = t
    def test(self):
        return 'test segitiga'

    def info(self):
        return f'Menghitung rumus segitiga dengan alas {self.a} dan {self.t} adalah'

    def hitung_luas(self):
        return 0.5 * self.a * self.t