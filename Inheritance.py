class Constantinopole:
    def Empire(self):
        print('Bizentine, Roman, Ottoman empire.')
    def Culture(self):
        print('Byzentine, Greek, Turkish.')

class Eskisehir(Constantinopole):
    def location(self):
        print('NorthWestern Turkey.')
    def previous_name(self):
        print('In Byzantine era it was Dorylaeum.')

class Ankara(Constantinopole):
    pass

eskesehir = Eskisehir()
eskesehir.Culture()
eskesehir.Empire()
eskesehir.location()
eskesehir.previous_name()
ankara = Ankara()
ankara.Empire()
ankara.Culture()