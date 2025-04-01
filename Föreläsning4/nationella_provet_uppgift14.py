"""Lösning till uppgift 14 i nationella provet i matematik.
"""
import random
import matplotlib.pyplot as plt

N_LJUS = 8
N_MÖRK = 7
N_VIT = 6

ANTALET_SIMULERINGAR = 100000

def skapa_påse():

    påse = []

    for x in range(N_LJUS):
        påse.append('ljus')

    for x in range(N_MÖRK):
        påse.append('mörk')

    for x in range(N_VIT):
        påse.append('vit')

    return påse

def uppgift_a():
    påse = skapa_påse()

    teoretiska_sannolikheten = N_VIT / (N_VIT + N_MÖRK + N_LJUS)

    antal_vit = 0
    andel_vit = []

    for f in range(ANTALET_SIMULERINGAR):

        if random.choice(påse) == 'vit':
            antal_vit +=1

        andel_vit.append(antal_vit/(f+1))

    uppskattade_sannolikhet = antal_vit / ANTALET_SIMULERINGAR

    print('Teoretisk sannolikhet:', teoretiska_sannolikheten)
    print('Uppskattad sannolikhet:', uppskattade_sannolikhet)

    plt.plot(andel_vit, label='Uppskattad sannolikhet')
    plt.hlines(uppskattade_sannolikhet, 0, ANTALET_SIMULERINGAR, colors='red', label='Uppmätt')
    plt.hlines(teoretiska_sannolikheten, 0, ANTALET_SIMULERINGAR, colors='green', label='Teoretisk')
    plt.xlabel('Antalet försök')
    plt.ylabel('Andelen vit')
    plt.legend()
    #plt.show()

def uppgift_b():
    påse = skapa_påse()

    teoretiska_sannolikheten = (N_LJUS / (N_VIT + N_MÖRK + N_LJUS)) * ((N_LJUS - 1) / (N_VIT + N_MÖRK + N_LJUS - 1))

    antal2_ljusa = 0
    andel2_ljusa = []

    for f in range(ANTALET_SIMULERINGAR):

        if random.sample(påse, 2) == ['ljus', 'ljus']:
            antal2_ljusa +=1

        andel2_ljusa.append(antal2_ljusa /(f+1))

    uppskattade_sannolikhet = antal2_ljusa / ANTALET_SIMULERINGAR

    print('Teoretisk sannolikhet:', teoretiska_sannolikheten)
    print('Uppskattad sannolikhet:', uppskattade_sannolikhet)

    plt.plot(andel2_ljusa, label='Uppskattad sannolikhet')
    plt.hlines(uppskattade_sannolikhet, 0, ANTALET_SIMULERINGAR, colors='red', label='Uppmätt')
    plt.hlines(teoretiska_sannolikheten, 0, ANTALET_SIMULERINGAR, colors='green', label='Teoretisk')
    plt.xlabel('Antalet försök')
    plt.ylabel('Andelen 2 ljusa')
    plt.legend()
    #plt.show()


if __name__ == '__main__':
    plt.figure(figsize=(10,6))
    plt.subplot(121)
    plt.title("Uppgift A")
    uppgift_a()
    plt.subplot(122)
    plt.title("Uppgift B")
    uppgift_b()
    plt.show()
