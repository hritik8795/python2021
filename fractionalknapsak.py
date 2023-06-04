class Item:
    def __init__(self,weight,value):
        self.weight =weight
        self.value =value
        self.ratio =value/weight
def KnapsackMethod(items,capacity):
    items.sort(key =lambda x:x.ratio,reverse =True)
    usedCapacity =0
    totalValue =0

    for i in items:
        if usedCapacity+i.weight<=capacity:
            usedCapacity +=i.weight
            totalValue += i.value

        else:
            unusedweight =capacity-usedCapacity
            value =i.ratio*unusedweight
            usedCapacity +=unusedweight
            totalValue +=value
        if usedCapacity==capacity:
            break
    print("total value obtan:"+str(totalValue))
item1 =Item(20,100)
item2 =Item(30,120)
item3 =Item(10,60)
clist =[item1,item2,item3]
KnapsackMethod(clist,50)
