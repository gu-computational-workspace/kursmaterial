import random
import time

def hamta_anvandarens_val():
    anvandarens_val = input("Välj sten, sax eller påse: ").lower()
    while anvandarens_val not in ['sten', 'sax', 'påse']:
        print("Ogiltigt val. Försök igen.")
        anvandarens_val = input("Välj sten, sax eller påse: ").lower()
    return anvandarens_val

def hamta_datorns_val():
    valmöjligheter = ['sten', 'sax', 'påse']
    return random.choice(valmöjligheter)

def avgora_vinnare(anvandarens_val, datorns_val):
    if anvandarens_val == datorns_val:
        return "Det är oavgjort!"
    elif (
        (anvandarens_val == 'sten' and datorns_val == 'sax') or
        (anvandarens_val == 'sax' and datorns_val == 'påse') or
        (anvandarens_val == 'påse' and datorns_val == 'sten')
    ):
        return "Du vinner!"
    else:
        return "Datorn vinner!"

def spela_spelet():
    print("Välkommen till sten-sax-påse-spelet!")
    
    while True:
        anvandarens_val = hamta_anvandarens_val()
        datorns_val = hamta_datorns_val()

        print(f"Du valde: {anvandarens_val}")
        print(f"Datorn valde: {datorns_val}")

        time.sleep(0.5)
        resultat = avgora_vinnare(anvandarens_val, datorns_val)
        print(resultat)

        spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
        if spela_igen != 'ja':
            print("Tack för att du spelade. Hej då!")
            break

if __name__ == "__main__":
    spela_spelet()
