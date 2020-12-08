"""
todo:   Daten einlesen
        Mailtext generieren
        Mail senden
"""


class Paar:
    def __init__(self, Partner1, Partner2, Host):
        self.Partner1 = Partner1
        self.Partner2 = Partner2
        self.Vorspeise = None #Paar5
        self.Hauptgang = None
        self.Nachspeise = None
        self.Host = Host    # 0->Vorspeise 1->Hauptgang 2->Nachspeise
        self.Adresse = 'Blaweg 5, 00111 Bla'
        self.Klingel = 'Klingel'
        self.Ernaehrung = None
        self.Stadtteil = None
        self.Email = 'bla@bla.de'
        self.Mailtext =''

        if self.Host == 0:
            self.Vorspeise = self
        if self.Host == 1:
            self.Hauptgang = self
        if self.Host == 2:
            self.Nachspeise = self

    def generate_Mailtext(self):
        pass

    def send_Mail(self):
        pass

    def set_Vorspeise(self,VorspeisenListe):
        for tisch in VorspeisenListe:
            if self in tisch:
                if self.Host == 0:
                    break
                else:
                    for paar in tisch:
                        if paar.Host == 0 and (paar != self):
                            self.Vorspeise = paar

    def set_Nachspeise(self, NachspeisenListe):
        for tisch in NachspeisenListe:
            if self in tisch:
                if self.Host == 2:
                    break
                else:
                    for paar in tisch:
                        if paar.Host == 2 and (paar != self):
                            self.Nachspeise = paar

    def set_Hauptgang(self, HauptgangListe):
        for tisch in HauptgangListe:
            if self in tisch:
                if self.Host == 1:
                    break
                else:
                    for paar in tisch:
                        if paar.Host == 1 and (paar != self):
                            self.Hauptgang = paar



def main():
    Paar1 = Paar(Partner1='Gerda', Partner2='Anna', Host=0)
    Paar2 = Paar(Partner1='Alex',Partner2= 'Freundin', Host=1)
    Paar3 = Paar(Partner1='Julia', Partner2='Tom', Host=1)
    Paar4 = Paar(Partner1='Paula', Partner2='Freund', Host=1)
    Paar5 = Paar(Partner1='Lioba', Partner2='Sophie', Host=2)
    Paar6 = Paar(Partner1='Hannes', Partner2='SCHAWNÜ', Host=0)
    Paar7 = Paar(Partner1='Klara', Partner2='Anna', Host=2)
    Paar8 = Paar(Partner1='Sascha', Partner2='Kumpel', Host=2)
    Paar9 = Paar(Partner1='Madelaine', Partner2='Lolo', Host=0)

    PaarListe = [Paar1, Paar2, Paar3, Paar4, Paar5, Paar6, Paar7, Paar8, Paar9]

    """
    für vorspeise, hauptgang und nachspeise paare nach tabelle sortieren
    """

    Vorspeise = [[Paar1, Paar2, Paar3],[Paar4, Paar5, Paar6],[Paar7, Paar8, Paar9]]
    Hauptgang = [[Paar1, Paar4, Paar7],[Paar2, Paar5, Paar8],[Paar3, Paar6, Paar9]]
    Nachspeise = [[Paar1, Paar5, Paar9],[Paar3, Paar4, Paar8],[Paar2, Paar6, Paar7]]

    for paar in PaarListe:
        paar.set_Vorspeise(VorspeisenListe=Vorspeise)
        paar.set_Hauptgang(HauptgangListe=Hauptgang)
        paar.set_Nachspeise(NachspeisenListe=Nachspeise)

    for paar in PaarListe:
        print('Hey {} und {}, \n'
              'eure Vorspeise bekommt ihr bei {} ({}), eure Hauptspeise dann bei {}'.format(paar.Partner1,
                                                                                            paar.Partner2,
                                                                                            paar.Vorspeise.Partner1,
                                                                                            paar.Vorspeise.Adresse,
                                                                                            paar.Hauptgang.Partner1))
        print('_______________________________________')



    

    """
    Hey Tom und Julia,
    ihr seit zur Vorspeise bei ? und beim Hauptgang bei ? ...
    """

if __name__ == '__main__':
    main()

