class Train():
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.noOfSeats = seats
        self.seatsTotal = {seat_num: '*' for seat_num in range(1, seats+1)}

    def BookTicket(self, numberOfSeats):
        for seat in numberOfSeats:
            if self.seatsTotal[seat] == '*':
                self.seatsTotal[seat] ='Booked'
                print("Ticket Booked!!")
            else:
                print("This Ticket is not available ,Check Info")



    def cancelTicket(self,cancellist):
        for seat in cancellist:
            if self.seatsTotal[seat] == 'Booked':
                self.seatsTotal[seat] = '*'
                print('Ticket Cancelled')
            else:
                print("This ticket is not booked!!")


    def getInfo(self):
        print(f'''Name : {self.name}
Seats : {self.noOfSeats}
''')

    def FareInfoOfMyRailways(self):
        if "Metro" in self.name:
            print(f"Fare : {self.fare} \n")
        else:
            print("Fare : 20")


def test():

    train1 = Train("Metro", 15, 100)
    train1.getInfo()
    train1.FareInfoOfMyRailways()
    train1.BookTicket([1, 2, 3, 9])
    train1.getInfo()
    train1.BookTicket([1])
    train1.getInfo()
    train1.cancelTicket([1])
    train1.BookTicket([1])
    train1.getInfo()
    
    print(train1.seatsTotal)



test()
