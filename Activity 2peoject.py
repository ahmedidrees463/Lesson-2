passenger_name="Syed Idrees Ahmed"
destination= "Hong Kong"
ticket_price= 1200.0
number_of_tickets= 3
is_available= True

print("Passenger name:",passenger_name)
print("destionation:",destination)
print("Ticket Price:",ticket_price)
print("Number Of Tickets:",number_of_tickets)
print("Tickets Available?:",is_available)

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

total_cost=ticket_price*number_of_tickets
discount= 150
final_cost=total_cost-discount
print("\Total cost:",total_cost)
print("Discount:",discount)
print("Final Cost:",final_cost)

print("Double Ticket Price:",ticket_price * 2)
print("Ticket Price After 70 Increase:",ticket_price + 70)
print("Half Ticket Price:",ticket_price / 2)

print("Is ticket price under 1200?:",ticket_price<1200)
print("Are more then 1 tickets booked?:",number_of_tickets>1)
print("Is destionation Hong Kong?:",destination=="Hong Kong")
print("Is Final cost more then 3000?:",final_cost>3000)

travel_message= passenger_name + " Is traveling to " + destination + "."
print("\nTravel Message:", travel_message)
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name)) 

Evening_ticket_price= 850
Midnight_ticket_price= 1000

print("\nAfter Swapping:")
print("Evening Ticket Price:", Evening_ticket_price)
print("Midnight Ticket Price:", Midnight_ticket_price)