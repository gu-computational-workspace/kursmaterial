import random
import time

def hämta_användarens_val():
    användarens_val = input('Välj sten, sax eller påse: ').lower()

    while(användarens_val) not in ['sten', 'sax', 'påse']:
        print('Ogiltigt val, input ska vara sten, sax eller påse.')
        användarens_val = input('Välj sten, sax eller påse: ').lower()

    return användarens_val

def hämta_datorns_val():
    val = ['sten', 'sax', 'påse']
    return random.choice(val)

def avgöra_vinnare(användarens_val, datorns_val):

    if användarens_val == datorns_val:
        return 'Det är oavgjort!'
    elif (
        (användarens_val =='sten' and datorns_val=='sax') or
        (användarens_val=='sax' and datorns_val=='påse') or
        (användarens_val=='påse' and datorns_val=='sten')
        ):
        return 'Du vinner spelet!'
    else:
        return 'Datorn vinner spelet!'

def spela_spelet():

    print('Välkommen till sten, sax och påse, lycka till!')
    while True:
        användarens_val = hämta_användarens_val()
        datorns_val = hämta_datorns_val()

        print('Jag valde', användarens_val)
        print('Datorn valde', datorns_val)

        time.sleep(0.7)
        resultat = avgöra_vinnare(användarens_val, datorns_val)
        print(resultat)

        spela_igen = input('Spela igen? (ja/nej): ').lower()

        if spela_igen == 'nej':
            print('Tack för en bra match! Hej då!')
            break


if __name__ == '__main__':
    spela_spelet()
    
