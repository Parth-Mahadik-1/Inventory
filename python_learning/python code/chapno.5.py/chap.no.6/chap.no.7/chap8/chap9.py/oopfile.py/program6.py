class train:
    def __init__(slv,S,F,N):
        slv.S=S
        slv.F=F
        slv.N=N
    def bookticket(slv):
        if (slv.S>0):
            print("*********************")
            print(f"your seat is booked your seat number is: {slv.S}")
            slv.S=slv.S-1
        else:
            print("your seat is not book plz try in tatkal")
            print("*********************")
    def seats(slv):
        print("*********************")
        print(f"The number of seats in train are: {slv.S}")
        print("*********************")
    def fare(slv):
        print("*********************")   
        print(f"The number of fare is in RS: {slv.F}\- ")
        print("*********************")
    def name(slv):
        print("*********************")
        print(f"tha train name: {slv.N}")
        print("*********************")
P=train(2,2500,"/***vande bharat express***/")
P.name()
P.fare()
P.bookticket()
P.seats()
P.bookticket()
P.seats()

