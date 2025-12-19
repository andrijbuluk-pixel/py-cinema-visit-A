from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number_cinema):
        self.number_cinema = number_cinema



    def movie_session(self, customers, cleaning_staff):
        print(f"Start watch {customers}")
        print(f"The end watch {customers}")
        print(f"Start cleaning {cleaning_staff}")
