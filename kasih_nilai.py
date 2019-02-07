with open("references/positive.txt") as pos1:
    for i in pos1:
        with open("references/pos_n.txt","a") as pos2:
            pos2.write(i.replace("\n",":1\n"))

with open("references/negative.txt") as pos1:
    for i in pos1:
        with open("references/neg_n.txt","a") as pos2:
            pos2.write(i.replace("\n",":-1\n"))