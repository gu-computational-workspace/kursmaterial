"""Detta programmet löser uppgift 9 i Nationella provet i matematik år 2014/2015.

Uppgiften är att hitta de tre primtalen som vid multiplikation av varandra blir 105.

"""

def is_prime(n):
    """
    Funktion för att avgöra om talet n är ett primtal eller inte.
    """

    for tal in range(2, n):
        if n % tal == 0:
            return False
    return True


def main():
    """
    Hittar de tre primtalen med produkten 105
    """
    n = 105

    primtal = []
    for tal in range(2, n):
        if is_prime(tal):
            primtal.append(tal)

    # Loopa igenom tal1, tal2, tal3 och avgör om tal1*tal2*tal3=105
    for tal1 in primtal:
        for tal2 in primtal:
            for tal3 in primtal:

                if tal1 * tal2 * tal3 == n:
                    print(tal1, tal2, tal3)



if __name__ =='__main__':
    main()
