from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    text_1 = "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak "
    nieuwe_prijs = prijs - (korting * prijs)
    uitvoer = text_1 + f"{smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    totaal_btw = totaal * btw
    text_1 = "Het totaal van alle inkomsten van deze week is "
    text_2 = "euro btw betaald dient te worden."
    uitvoer = text_1 + f"{totaal} euro, waarover {totaal_btw}" + text_2
    return uitvoer

def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
