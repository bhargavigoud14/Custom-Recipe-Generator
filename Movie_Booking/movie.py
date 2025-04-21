class Theatre:
    movie_name="Devara"
    seats={
        'silver':[30,250],
        'gold':[35,300],
        'diamond':[40,500]
    }
    def __init__(self,name,email):
        self.name=name
        self.email=email
    
    @classmethod
    def display(cls):
        print("Movie",cls.movie_name)
        for i in cls.seats:
            print("Seat type:",i)
            print("No of seats available seats:",cls.seats[i][0])
            print("price",cls.seats[i][1])

    def book_ticket(self):
        Theatre.display()
        seat_type=input("enter the seat type:")
        tickets=int(input("enter no of tickets:"))
        if seat_type in Theatre.seats:
            if tickets<=Theatre.seats[seat_type][0]:
                price=self.total_amount(seat_type,tickets)
                print("total amount:",price)
                if self.payment(price):
                    Theatre.seats[seat_type][0] -= tickets 
                    print(f"Payment done for tickets {tickets}")
                    print(f"Go and enjoy {Theatre.movie_name}")
                else:
                    print("payment failed ")
            else:
                print('seats are not available')
        else:
            print("seat type is not available")

    @staticmethod
    def total_amount(seat_type,tickets):
        return tickets*(Theatre.seats[seat_type][1])
    @staticmethod
    def payment(price):
        print(f"please pay{price}")
        pay=int(input("enter amount:"))
        if pay==price:
            return True
        else:
            return False
# obj=Theatre("na","sd")

        