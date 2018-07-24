L = []

def middle(L):
    midden = len(L) / 2

    if ".5" not in str(midden):
        print("Geen middelste waarde")
        exit()
    print(type(midden))

    midden = midden - 0.5
    midden = int(midden)

    print(L[midden])


middle([1,2,3,4,5,6])
