 #def washingMachin(weight):
 #   if weight<=2000:
 #       print("low level water ")
 #   elif weight >=2000 and weight<=4000:
 #       print("the water is in medium level")
 #   elif weight>=4000 and weight<7000:
 #       print("weight is high level")
 # #  elif weight ==7000:
 #       print("OVERLOAD")
 #   else:
 #       print("invalid")

#washingMachin(int(input())) 

#selection of traineees
#round_1 =int(input("entr the oxygen level at frist round")) 
#round_2  =int(input("enter thre oxygen level at round 2"))
#round_3  =int(input("enter thre oxygen level at round 3"))
#round_4  =int(input("enter thre oxygen level at round 4"))
#round_5   =int(input("enter thre oxygen level at round 5"))
#round_6 =int(input("enter thre oxygen level at round 6"))
#round_7  =int(input("enter thre oxygen level at round 7"))
#round_8  =int(input("enter thre oxygen level at round 8"))
#round_9  =int(input("enter thre oxygen level at round 9"))

#average1 =(round_1+round_2+round_3)/3
#average2 =(round_4+round_5+round_6)/3
#average3 =(round_7+round_8+round_9)/3

#if  average1 or average2 or average3 <=70:
#    print("you are unfit")

#if average1>average2 and average1>average3:
 #   print("trainee1 is fit ",+average1)

#elif average1<average2 and average2>average3:
 #   print("trainee 2 is fit",+ average2)

#elif  average1<average3 and average2<average3:
#    print("trainee3 is fit",+average3)

#elif average1==average2==average3:
#    print("all are eligible")
#else:
#    print("you are unfit")

trainee =[[],[],[],[]]
for i in range(3):
    for j in range(3):
        trainee[i].append(int(input()))
        if (trainee[i][j] not in range (1,101)):
            print("invalid input")
    for i in range (3):
        trainee[3].append((trainee[2][i]+trainee[1][i]+trainee[0][i])//3)
    maximum = max(trainee[3])
    for i in range(3):
        if trainee[3][i]<70:
            print("trainee {0} is unfit".format(i+1))
        elif trainee[3][i] == maximum:
            print("trainee number:",i+1)



def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

