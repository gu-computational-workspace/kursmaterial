import math
import numpy as np
import matplotlib.pyplot as plt

def kaströrelse(initial_hastighet, vinkel, tid, antal_steg):
    """Simulerar kaströrelse för ett objekt."""
    vinkel_radianer = math.radians(vinkel)  # Omvandla grader till radianer

    # Beräkna startkomponenterna för hastighet
    initial_hastighet_x = initial_hastighet * math.cos(vinkel_radianer)
    initial_hastighet_y = initial_hastighet * math.sin(vinkel_radianer)

    tider = np.linspace(0, tid, antal_steg)  # Skapa jämnt fördelade tidssteg
    x_positions = []
    y_positions = []

    for t in tider:
        x_position = initial_hastighet_x * t
        y_position = initial_hastighet_y * t - 0.5 * 9.81 * t**2  # Formel för y-position

        if y_position < 0:  # Stanna när objektet når marken
            break

        x_positions.append(x_position)
        y_positions.append(y_position)

    return x_positions, y_positions

def main():
    initial_hastighet = float(input("Ange den initiala hastigheten (m/s): "))
    vinkel = float(input("Ange vinkeln för kastet (grader): "))
    tid = 10  # Lång simuleringstid för att få hela rörelsen
    antal_steg = 200  # Fler steg för bättre upplösning

    x_positions, y_positions = kaströrelse(initial_hastighet, vinkel, tid, antal_steg)

    # Plotta hela banan
    plt.plot(x_positions, y_positions, label="Bana", linestyle='dashed')

    # Plotta start- och slutpunkt
    plt.plot(x_positions[0], y_positions[0], 'bo', markersize=10, label="Start")
    plt.plot(x_positions[-1], y_positions[-1], 'ro', markersize=10, label="Slut")

    # Diagram-inställningar
    plt.xlabel("Horisontell position (m)")
    plt.ylabel("Vertikal position (m)")
    plt.title("Kaströrelse för ett objekt")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
