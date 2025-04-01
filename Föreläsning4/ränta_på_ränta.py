"""Detta programmet simulerar ränta-på-ränta effekten.

"""

def beräkna_ränta(princip, ränta, tid):

    # A = princip*(1 + ränta/100)**tid

    belopp = princip*(1 + ränta/100)**tid
    sammansatt_ränta = belopp - princip

    return sammansatt_ränta

if __name__ =='__main__':

    princip = float(input('Ange startbeloppet i kronor: '))

    ränta = float(input('Ange uppskattad avkastning i procent: '))

    tid = float(input('Ange tid i år: '))

    resultat = beräkna_ränta(princip, ränta, tid)

    print('----------------------------')
    print(f"princip: {princip}, ränta: {ränta}, tid: {tid}")
    print(f"Totalbeloppet efter {tid} år är {princip + resultat}")
    print(f"Sammansatta räntan efter {tid} år är {resultat}")
    print(f"Den procentuella ökningen efter {tid} år är {resultat/princip*100}")
    print('----------------------------')
