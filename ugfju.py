class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number


class Flight:
    def __init__(self, flight_number, departure, arrival, departure_date, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time


class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number


class FirstClass(Seat):
    def __init__(self, seat_number, additional_services):
        super().__init__(seat_number)
        self.class_type = "First Class"
        self.additional_services = additional_services


class BusinessClass(Seat):
    def __init__(self, seat_number, additional_services):
        super().__init__(seat_number)
        self.class_type = "Business Class"
        self.additional_services = additional_services


class EconomyClass(Seat):
    def __init__(self, seat_number, additional_services):
        super().__init__(seat_number)
        self.class_type = "Economy Class"
        self.additional_services = additional_services


class BoardingPass:
    def __init__(self, passenger, flight, seat, gate, boarding_time, electronic_ticket_number):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.gate = gate
        self.boarding_time = boarding_time
        self.electronic_ticket_number = electronic_ticket_number

    def print_details(self):
        print("NATIONAL AIRLINES BOARDING PASS")
        print(f"Passenger: {self.passenger.name}")
        print(f"Flight: {self.flight.flight_number}")
        print(f"From: {self.flight.departure} To: {self.flight.arrival}")
        print(f"Departure: {self.flight.departure_date} {self.flight.departure_time}")
        print(f"Arrival Time: {self.flight.arrival_time}")
        print(f"Seat: {self.seat.seat_number} ({self.seat.class_type})")
        print(f"Gate: {self.gate}")
        print(f"Boarding Time: {self.boarding_time}")
        print(f"Electronic Ticket Number: {self.electronic_ticket_number}")


# Creating objects with the provided boarding pass details
passenger = Passenger("JAMES SMITH", "XYZ123456")
flight = Flight("NA4321", "CHICAGO ORD", "NEW YORK JFK", "06 DEC 20", "11:40", "13:30")
seat = FirstClass("09A", ["Priority boarding", "Extra luggage allowance"])
boarding_pass = BoardingPass(passenger, flight, seat, "03", "11:20", "629")

# Printing the boarding pass details
boarding_pass.print_details()
