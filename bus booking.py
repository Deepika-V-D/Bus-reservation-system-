# BUS RESERVATION SYSTEM
# Using Dictionary, Conditions and Loops

buses = {
    101: {
        "from": "Thanjavur",
        "to": "Chennai",
        "total_seats": 40,
        "available": 5,
        "fare": 450
    },
    102: {
        "from": "Madurai",
        "to": "Chennai",
        "total_seats": 40,
        "available": 3,
        "fare": 500
    },
    103: {
        "from": "Trichy",
        "to": "Coimbatore",
        "total_seats": 40,
        "available": 8,
        "fare": 400
    },
    104: {
        "from": "Thanjavur",
        "to": "Madurai",
        "total_seats": 40,
        "available": 10,
        "fare": 350
    }
}

bookings = []

while True:

    print("\n========================================")
    print("       BUS RESERVATION SYSTEM")
    print("========================================")
    print("1. View Available Buses")
    print("2. View Bus Details")
    print("3. Book Ticket")
    print("4. View Booked Tickets")
    print("5. Search Booking")
    print("6. Update Booking")
    print("7. Cancel Ticket")
    print("8. Check Seat Availability")
    print("9. View Passenger Details")
    print("10. Exit")

    choice = int(input("\nEnter your choice: "))

    # 1. View Available Buses
    if choice == 1:
        print("\n========== AVAILABLE BUSES ==========")
        print("Bus No.     Route                  Seats")
        print("------------------------------------------")

        for bus_no, bus in buses.items():
            route = bus["from"] + " -> " + bus["to"]
            print(bus_no, "       ", route, "     ", bus["available"])

    # 2. View Bus Details
    elif choice == 2:
        print("\n========== BUS DETAILS ==========")

        bus_no = int(input("Enter Bus Number: "))

        if bus_no in buses:
            bus = buses[bus_no]

            print("\nBus Number :", bus_no)
            print("From       :", bus["from"])
            print("To         :", bus["to"])
            print("Total Seats:", bus["total_seats"])
            print("Available  :", bus["available"])
            print("Fare       : ₹", bus["fare"])
        else:
            print("Invalid Bus Number!")

    # 3. Book Ticket
    elif choice == 3:
        print("\n========== BOOK TICKET ==========")

        bus_no = int(input("Enter Bus Number: "))

        if bus_no in buses:

            name = input("Enter Passenger Name: ")
            age = int(input("Enter Age: "))
            seat = int(input("Enter Seat Number: "))

            bus = buses[bus_no]

            if bus["available"] > 0:
                booking = {
                    "name": name,
                    "age": age,
                    "bus_no": bus_no,
                    "seat": seat,
                    "fare": bus["fare"]
                }

                bookings.append(booking)
                bus["available"] -= 1

                print("\nTicket booked successfully!")
                print("\nPassenger :", name)
                print("Age       :", age)
                print("Bus No.   :", bus_no)
                print("Seat No.  :", seat)
                print("Fare      : ₹", bus["fare"])

            else:
                print("No seats available!")

        else:
            print("Invalid Bus Number!")

    # 4. View Booked Tickets
    elif choice == 4:
        print("\n========== BOOKED TICKETS ==========")

        if len(bookings) == 0:
            print("No bookings found.")

        else:
            print("Passenger      Bus No.     Seat No.     Fare")
            print("------------------------------------------------")

            for booking in bookings:
                print(
                    booking["name"],
                    "       ",
                    booking["bus_no"],
                    "         ",
                    booking["seat"],
                    "          ₹",
                    booking["fare"]
                )

    # 5. Search Booking
    elif choice == 5:
        print("\n========== SEARCH BOOKING ==========")

        name = input("Enter Passenger Name: ")
        found = False

        for booking in bookings:

            if booking["name"].lower() == name.lower():

                print("\nBooking Found!")
                print("\nPassenger :", booking["name"])
                print("Age       :", booking["age"])
                print("Bus No.   :", booking["bus_no"])
                print("Seat No.  :", booking["seat"])
                print("Fare      : ₹", booking["fare"])

                found = True

        if found == False:
            print("Booking not found!")

    # 6. Update Booking
    elif choice == 6:
        print("\n========== UPDATE BOOKING ==========")

        name = input("Enter Passenger Name: ")
        found = False

        for booking in bookings:

            if booking["name"].lower() == name.lower():

                print("\nCurrent Seat Number:", booking["seat"])

                new_seat = int(input("Enter New Seat Number: "))

                booking["seat"] = new_seat

                print("\nBooking updated successfully!")
                print("\nPassenger :", booking["name"])
                print("New Seat  :", booking["seat"])

                found = True
                break

        if found == False:
            print("Booking not found!")

    # 7. Cancel Ticket
    elif choice == 7:
        print("\n========== CANCEL TICKET ==========")

        name = input("Enter Passenger Name: ")
        found = False

        for booking in bookings:

            if booking["name"].lower() == name.lower():

                print("\nBooking found.")

                confirm = input(
                    "Are you sure you want to cancel? (yes/no): "
                )

                if confirm.lower() == "yes":

                    bus_no = booking["bus_no"]

                    buses[bus_no]["available"] += 1
                    bookings.remove(booking)

                    print("\nTicket cancelled successfully!")

                else:
                    print("Cancellation stopped.")

                found = True
                break

        if found == False:
            print("Booking not found!")

    # 8. Check Seat Availability
    elif choice == 8:
        print("\n========== SEAT AVAILABILITY ==========")

        bus_no = int(input("Enter Bus Number: "))

        if bus_no in buses:

            booked_seats = []

            for booking in bookings:
                if booking["bus_no"] == bus_no:
                    booked_seats.append(booking["seat"])

            print("\nAvailable Seats:")

            for seat in range(1, buses[bus_no]["total_seats"] + 1):

                if seat not in booked_seats:
                    print(seat, end=" ")

            print("\n\nAvailable Seats:",
                  buses[bus_no]["available"])

            print("Booked Seats   :",
                  len(booked_seats))

        else:
            print("Invalid Bus Number!")

    # 9. View Passenger Details
    elif choice == 9:
        print("\n========== PASSENGER DETAILS ==========")

        bus_no = int(input("Enter Bus Number: "))

        found = False

        for booking in bookings:

            if booking["bus_no"] == bus_no:

                print("\nPassenger Name :", booking["name"])
                print("Age            :", booking["age"])
                print("Seat Number    :", booking["seat"])

                found = True

        if found == False:
            print("No passenger details found!")

    # 10. Exit
    elif choice == 10:

        print("\n========================================")
        print("       THANK YOU FOR USING")
        print("       BUS RESERVATION SYSTEM")
        print("========================================")

        break

    else:
        print("\nInvalid choice! Please try again.")