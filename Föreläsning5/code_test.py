#import pdb

f = open("data.txt", "r")
rader = f.readlines()

for rad in rader:
    try:
        tal = int(rad)
    except:
        print(rad)
        #pdb.set_trace()
