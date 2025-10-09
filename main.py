# Lista tzv. "stop riječi" (eng. stop words). To su česte riječi koje se 
# u analizi teksta često zanemaruju jer ne nose puno specifičnog značenja
# (npr. prijedlozi, veznici, članovi). Iako je ova lista definirana, 
# važno je napomenuti da se u ostatku koda ona zapravo ne koristi.
# Da bi se koristila, trebalo bi je uključiti u funkciju `ocisti_tekst`.
STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'su', 'joj', 'ih']

# Definicija funkcije za učitavanje teksta iz datoteke.
# Funkcija prima jedan argument: `filepath`, što je putanja do datoteke.
def ucitaj_tekst(filepath):
    # `try...except` blok služi za obradu mogućih grešaka.
    # U ovom slučaju, hvata grešku `FileNotFoundError` ako datoteka ne postoji.
    try:
        # `with open(...)` je siguran način za otvaranje datoteke.
        # Automatski zatvara datoteku nakon što se završi s radom, čak i ako dođe do greške.
        # 'r' označava da se datoteka otvara za čitanje (read).
        # 'encoding='utf-8'' osigurava ispravno čitanje znakova specifičnih za hrvatski jezik (č, ć, š, đ, ž).
        with open (filepath,'r',encoding='utf-8') as file:
            # `file.read()` čita cjelokupan sadržaj datoteke kao jedan string (tekst).
            sadrzaj = file.read()
        # Funkcija vraća pročitani sadržaj.
        return sadrzaj
    # Ako se dogodi greška `FileNotFoundError` (datoteka nije pronađena)...
    except FileNotFoundError:
        # ...ispisuje se poruka o grešci korisniku.
        print(f'greška: Datoteka na putanji {filepath} ne postoji.')
        # Funkcija vraća `None`, što je specijalna vrijednost u Pythonu koja označava "ništa".
        # To je koristan signal da operacija nije uspjela.
        return None

# Definicija funkcije koja pročišćava tekst.
# Prima jedan argument: `tekst` (string koji treba očistiti).
def ocisti_tekst(tekst):
    # `tekst.lower()` pretvara sva slova u tekstu u mala slova.
    # To je važno kako se ista riječ napisana različitim velikim i malim slovima
    # (npr. "Riječ" i "riječ") ne bi brojala kao dvije različite riječi.
    tekst = tekst.lower()
    
    # Lista interpunkcijskih znakova koje želimo ukloniti iz teksta.
    interpunkcija = ['.', ',', ':', ';', '?', '!', '"', "'", '(', ')']
    
    # `for` petlja prolazi kroz svaki znak u listi `interpunkcija`.
    for znak in interpunkcija:
        # `tekst.replace(znak, '')` zamjenjuje svaki interpunkcijski znak praznim stringom,
        # čime ga efektivno briše iz teksta.
        tekst = tekst.replace(znak, '')
        
    # `tekst.split()` razdvaja string u listu pojedinačnih riječi.
    # Razdvajanje se vrši na mjestima gdje su razmaci ili prijelomi redaka.
    lista_riječi = tekst.split()

    # Funkcija vraća pročišćeni tekst u obliku liste riječi.
    return lista_riječi

# Definicija funkcije koja broji koliko se puta svaka riječ ponavlja.
# Prima jedan argument: `lista_rijeci` (lista riječi dobivena iz funkcije `ocisti_tekst`).
def broji_frekvenciju(lista_rijeci):
    # Kreiramo prazan rječnik (dictionary). Rječnik će služiti za pohranu rezultata,
    # gdje će ključ biti riječ, a vrijednost (value) broj njezinih ponavljanja.
    rjecnik_frekvencija = {}

    # `for` petlja prolazi kroz svaku riječ u primljenoj listi.
    for rijec in lista_rijeci:
        # Provjeravamo postoji li trenutna `rijec` već kao ključ u našem rječniku.
        if rijec in rjecnik_frekvencija:
            # Ako postoji, povećavamo njezinu vrijednost (brojač) za 1.
            rjecnik_frekvencija[rijec] += 1
        else:
            # Ako riječ još ne postoji u rječniku, dodajemo je kao novi ključ
            # i postavljamo njezinu početnu vrijednost (brojač) na 1.
            rjecnik_frekvencija[rijec] = 1
            
    # Funkcija vraća rječnik koji sadrži frekvenciju svake riječi.
    return rjecnik_frekvencija
    # Funkcija prima rječnik frekvencija i uklanja iz njega sve riječi koje se nalaze u listi STOP_WORDS.
def ocisti_stop_words(lista_rijeci):
    for rijec in STOP_WORDS:
        if rijec in lista_rijeci:
            lista_rijeci.remove(rijec)
    return lista_rijeci



# Glavni dio programa.
# `if __name__ == '__main__':` je standardna Python konstrukcija koja osigurava
# da se kod unutar ovog bloka izvršava samo kada se skripta pokreće direktno,
# a ne kada se uvozi kao modul u neku drugu skriptu.
if __name__ == '__main__':
    # Definiramo putanju do datoteke koju želimo analizirati.
    filepath = 'tekst.txt'
    print(f'učitavam tekst iz datoteke :{filepath}')

    # Pozivamo funkciju `ucitaj_tekst` da učita sadržaj iz datoteke.
    # Rezultat (sadržaj ili `None` ako je došlo do greške) spremamo u varijablu `ucitani_tekst`.
    ucitani_tekst = ucitaj_tekst(filepath)

    # Provjeravamo je li tekst uspješno učitan.
    # `if ucitani_tekst:` je isto što i `if ucitani_tekst is not None:`.
    if ucitani_tekst:
        # Ako je tekst učitan, ispisujemo ga na ekran radi provjere.
        print('\ntekst uspješno učitan. slijedi ispis sadržaja:')
        print('-' * 40) # Ispisuje liniju radi bolje čitljivosti.
        print(ucitani_tekst)
        print('-' * 40)
        
        # Pozivamo funkciju `ocisti_tekst` na učitanom sadržaju.
        procisceni_tekst = ocisti_tekst(ucitani_tekst)

        # Ispisujemo pročišćenu listu riječi.
        print("\nProcisceni tekst je: ")
        print('-' * 40)
        print(procisceni_tekst)
        print('-' * 40)

        skroz_cisti_tekst = ocisti_stop_words(procisceni_tekst)

        print("\nSkroz Čisti tekst je: ")
        print('-' * 40)
        print(skroz_cisti_tekst)
        print('-' * 40)
        
        # Ispisujemo 15 najčešćih riječi iz rječnika frekvencija.

        if skroz_cisti_tekst:
            sortiran_rjecnik = sorted(skroz_cisti_tekst.items(), key=lambda item: item[1], reverse=True)
            print('-' * 50)
            print("---Prvih 15 najčešćih riječi---")
            print(sortiran_rjecnik[:15])
            print('-' * 50)
        else:
            print("neka greška se desila")
        
        # `procisceni_tekst.__len__()` ispisuje ukupan broj riječi u tekstu.
        # To je isto kao i `len(procisceni_tekst)`.
        print(f"Ukupan broj riječi: {procisceni_tekst.__len__()}")

        # Pozivamo funkciju `broji_frekvenciju` na pročišćenoj listi riječi.
        print("\nBrojim frekvenciju riječi...")
        broj_rijeci = broji_frekvenciju(procisceni_tekst)
        print("Brojanje završeno!")

        # Ispisujemo konačni rezultat – rječnik s frekvencijama riječi.
        print("\n---Rjecnik frekvencije---")
        print(broj_rijeci)
        print("-" * 40)

    # Ako tekst nije uspješno učitan (funkcija `ucitaj_tekst` je vratila `None`)...
    else:
        # ...ispisujemo poruku i program završava s radom jer nema podataka za obradu.
        print('program se prekida jer tekst nije učitan.')

    
# Napomena: U kodu postoji dupli blok za provjeru `if procisceni_tekst:`, 
# što nije nužno, ali ne uzrokuje grešku. Logika je mogla biti smještena
# unutar jednog `if ucitani_tekst:` bloka.
