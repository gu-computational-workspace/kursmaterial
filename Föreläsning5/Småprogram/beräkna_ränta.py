#Kort beskrivning: Ett program som beräknar sammansatt ränta. Dvs. ränta på ränta effekten.

def beräkna_ränta(princip, ränta, tid):
    # Beräknar sammansatt ränta
    # A = P * (1 + r/100)^n
    belopp = princip * (pow((1 + ränta / 100), tid))
    sammansatt_ränta = belopp - princip
    return sammansatt_ränta

# Körkod
if __name__=='__main__':
    # Tar inmatning från användaren

    try:
        princip = float(input("Ange huvudbeloppet: "))
    except Exception as e:
        print("Felaktig inmatning. Ange ett tal som huvudbelopp.")
        print(e)

    try:
        ränta = float(input("Ange räntesatsen: "))
    except Exception as e:
        print("Felaktig inmatning. Ange ett tal som räntesats.")
        print(e)

    try: 
        tid = int(input("Ange tiden i år: "))
    except Exception as e:
        print("Felaktig inmatning. Ange ett heltal som antal år.")
        
    assert princip > 0, "Startbeloppet måste vara större än 0"
    assert 0 < ränta < 100, "Räntan måste vara mellan 0 och 100"
    assert isinstance(tid, int) and tid < 100, "Tiden måste vara ett heltal, samt mindre än 100år"

    # Funktionsanrop och utskrift av resultat
    resultat = beräkna_ränta(princip, ränta, tid)
    print("------------------------------")
    print("Totalbeloppet är:", round(resultat + princip, 2))
    print("Sammansatt ränta är:", round(resultat))
    print("Procentuell ökning är:", round(resultat / princip * 100, 2), "%")
    print("------------------------------")

    