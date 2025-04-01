import time

def nedrakning(sekunder):
    print("Nedräkningen börjar!")
    while sekunder > 0:
        print(sekunder)
        time.sleep(1)  # Vänta i 1 sekund
        sekunder -= 1
    print("Nedräkningen är klar! Nu händer det grejer!")

if __name__ == "__main__":
    try:
        antal_sekunder = int(input("Ange antal sekunder för nedräkningen: "))
        nedrakning(antal_sekunder)
    except ValueError:
        print("Felaktig inmatning. Ange ett heltal som antal sekunder.")