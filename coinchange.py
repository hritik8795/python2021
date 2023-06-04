def coinChange(totalNumber,coin):
    N =totalNumber
    coins.sort()
    index =len(coin)-1
    while True:
        coinValue =coin[index]
        if N>=coinValue:
            print(coinValue)
            N =N-coinValue

        if N<coinValue:
            index -=1
        if N ==0:
            break
coins= [1,2,5,20,50,100]
coinChange(201,coins)