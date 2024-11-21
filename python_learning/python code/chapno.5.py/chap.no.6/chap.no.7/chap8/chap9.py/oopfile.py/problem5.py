class train:
    def __init__(self,T,S,F):
        self.T=T
        self.S=S
        self.F=F
    def bookticket(self):
        print(f"the tickets is availble for booking{self.T}")

    def seats(self):
        print(f"The number of seats in train are {self.S}")

    def fare(self):
        print(f"The number of seats in train {self.F}")

P=train("/***vande bharat express***/",300,2500)

P.bookticket()
P.seats()
P.fare()