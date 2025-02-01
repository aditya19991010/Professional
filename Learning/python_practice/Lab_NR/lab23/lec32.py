#Dictionary
from traceback import print_tb


def dictops():
    dictplayers = {
        "Rohit": 78,
        "Gill": 33,
        "Kohli": 45,
    }
    dictplayers["Ishan"] = 90
    dictplayers["Gill"] = 120
    dictplayers["Gill"] = 130

    dictnew = {
        "bumrah" : 30 ,
        "siraj" : 20
    }

    dictplayers.update(dictnew)

    del dictplayers["siraj"]

    "Rohit" in dictplayers

    dictplayers["Gill"]
    #dictplayers["shyam"]
    dictplayers.get("Gill")
    dictplayers.get("shyam", 'Not present')

    dictplayers.keys()
    print(list(dictplayers.keys()))
    print(list(dictplayers.values()))
    print(list(dictplayers.items()))
    print(dictplayers.keys())
    print(dictplayers.items())


# def main():
#     dictops()
#
# if __name__=="__main__":
#     main()


#Sets

def setops():
    print('set operation')
    # sets are like dict with its values thrown away, leaving on
    #sets are unordered

    new_set =  set("letters")
    print(new_set)

    lset = set(["Virat" , "Rohit", "Shubham"])
    print(lset)

    print(type(lset))

    #set from tuple
    tset = set(("Virat" , "Rohit", "Shubham"))
    print(tset)

    dset = set({"Virat" : 80, "Gill" : 88, "Rohit":100})
    print(dset)


    #test for a value using in -values are set most common use
    playerscores = {
        "Rohit" : {5,27,28},
        "Kohli" : {123,44,87},
        "Gill"  : {21,85}
    }


    for name, scores in playerscores.items():
        if 123 in scores: #find score = 123 in the keys
            print(name)

    # combinations and operatots
    for name, scores in playerscores.items():
        if scores & {21 ,85 }:
            print(name)

    a = {1,2}
    b = {2,3}
    print(a & b)
    print(a.intersection(b))
    print(a | b) #union
    print(a - b)
    print(a.difference(b))
    print(a ^ b) # inverse of intersection or symmetric difference
    print(a.symmetric_difference(b))
    print(a <= b) # is a subset of b
    print(a < b)
    print(a > b)
    print(a >= b) #To find if a is subset of b
    print(a.issubset(b))

    #Bigger DS
    batsmen = ['Roh', 'Koh', 'Ash']
    bowlers = ['Bum' , 'Sha', 'Ash']
    keepers = ['Dho', 'Isha']

    tuple_x_list = batsmen, bowlers, keepers
    list_x_list = [batsmen, bowlers, keepers]
    dict_x_list = {"bat":batsmen, "bow":bowlers, "keep":keepers}

    print(type(dict_x_list["bat"]))

#
#
# def main():
#     setops()
#
# if __name__=="__main__":
#     main()


A = set((range(1,31) ))

low = list()
mid = list()
high = list()
dict_scores = {"Low": low, "Mid": mid, "High": high}

for num in range(1,len(A)):
    if num <= 10:
        low.append(num)
    elif 10 < num <= 20:
        mid.append(num)
    elif 20 < num <= 30:
        high.append(num)



def main():
    setops()

if __name__=="__main__":
    main()
