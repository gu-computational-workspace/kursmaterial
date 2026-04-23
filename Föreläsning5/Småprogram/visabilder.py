import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class BildVisare:
    def __init__(self, bildmapp):
        self.bildmapp = bildmapp
        self.bildfiler = self.hamta_bildfiler()
        self.kolla_om_bildfilerna_fungerar()
        self.aktuell_index = np.random.randint(0, len(self.bildfiler))

        # Skapa figur och axel
        self.fig, self.ax = plt.subplots()
        self.visa_bild()

        # Anpassa knappstorleken för "Föregående"
        self.prev_button = Button(plt.axes([0.3, 0.01, 0.2, 0.05]), 'Föregående')
        
        # Anpassa storlek för "Nästa"
        self.next_button = Button(plt.axes([0.5, 0.01, 0.2, 0.05]), 'Nästa')
        
        # Anslut till knapptryckshändelser, uppdatera och visa ny bild beroende på vilken knapp som tryckts
        self.prev_button.on_clicked(lambda event: self.uppdatera_och_visa(event, 'prev'))
        self.next_button.on_clicked(lambda event: self.uppdatera_och_visa(event, 'next'))

        # Göm x- och y-axlar
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)

        # Anslut till tangentbordshändelser
        self.fig.canvas.mpl_connect('key_press_event', self.tangentbords_hantering)

        plt.show()

    def hamta_bildfiler(self):
        files = [f for f in os.listdir(self.bildmapp) if os.path.isfile(os.path.join(self.bildmapp, f))]
        bildfiler = [f for f in files if f.lower().endswith(('.png'))]
        return bildfiler

    def kolla_om_bildfilerna_fungerar(self):
        print("Kontrollerar om bilderna fungerar... kan ta en stund.")
        ok_bildfiler = []
        for bildfil in self.bildfiler:
            bildsokvag = os.path.join(self.bildmapp, bildfil)
            try:
                bild = plt.imread(bildsokvag)
                ok_bildfiler.append(bildfil)
            except:
                pass
        
        # Uppdatera bildfiler
        self.bildfiler = ok_bildfiler


    def visa_bild(self):
        if self.bildfiler:
            bildsokvag = os.path.join(self.bildmapp, self.bildfiler[self.aktuell_index])

            #Läs in bild
            bild = plt.imread(bildsokvag)

            # Rensa tidigare bild
            self.ax.cla()

            # Visa ny bild
            self.ax.imshow(bild)
            plt.title(f"Bild {self.aktuell_index + 1}/{len(self.bildfiler)}", loc= 'center')
            plt.draw()

    def uppdatera_och_visa(self, event, action):
        # Uppdatera aktuell index och visa ny bild, action kan vara 'prev' eller 'next'. Event är inte i bruk.
        if action == 'prev':
            self.aktuell_index = (self.aktuell_index - 1) % len(self.bildfiler)
        elif action == 'next':
            self.aktuell_index = (self.aktuell_index + 1) % len(self.bildfiler)

        #Visa ny bild
        self.visa_bild()

    def tangentbords_hantering(self, event):
        if event.key == 'left':
            self.uppdatera_och_visa(event, 'prev')
        elif event.key == 'right':
            self.uppdatera_och_visa(event, 'next')

if __name__ == "__main__":
    bildmapp = input("Ange sökvägen till mappen med bilder: ")

    if os.path.isdir(bildmapp):
        bildvisare = BildVisare(bildmapp)
    else:
        print("Ogiltig sökväg till mappen.")