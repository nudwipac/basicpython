def ticket(passenger_type):
    if passenger_type == "A":
        fare = 50
    elif passenger_type == "S":
        fare = 30
    elif passenger_type == "C" or passenger_type == "E":
        fare = 10
    return fare


p = input("Passenger type [A]dult, [S]tudent, [C]hild, [E]lder :")
print(ticket(p.upper()))
