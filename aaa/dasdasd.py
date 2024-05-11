number = [0,1,2,3,4,5]
letter = ["a","b","d", "e", "f", "g"]

combine = [["PACKAGE 1","PACKAGE 2", "PACKAGE 3"],
           ["Menudo","Kaldereta","Asado"]]

for i in combine:
    print("|", i[0], " "*(9-len(i[0])), "|", i[1], " "*(9-len(i[1])), i[2])
