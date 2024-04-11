# hotel_rooms = {
#     "101": {"status": "available", "customer": ""},
#     "102": {"status": "booked", "customer": "John Doe"}
# }






# def book_room(customer_name, room_number):
#     if room_number in hotel_rooms:
#         hotel_rooms[room_number]["status"] = "booked"
#         hotel_rooms[room_number]["customer"] = customer_name



# def check_out_customer(customer_name, room_number):
#     if room_number in hotel_rooms:
#         if customer_name == hotel_rooms[room_number]["customer"]:
#             hotel_rooms[room_number]["status"] = "available"
#             hotel_rooms[room_number]["customer"] = ""
            
# def display_room_status():
#     print("Room Status:")
#     for room_number, details in self.hotel_rooms.items():
#         print(f"Room {room_number}: Status - {details['status']}, Customer - {details['customer']}")
            
            




# def booking_room():
#     while True:
#         booked_room = input("Would you like to book or check-out or display a room?")
#         if booked_room == "book":
#             customer_name = input("What is the customer name?")
#             room_number = input("What is the room number?")
#             book_room(customer_name, room_number)
#             print("Room booked")
#         elif booked_room == "check-out":
#             customer_name = input("What is the customer name?")
#             room_number = input("What is the room number?")
#             check_out_customer(customer_name, room_number)
#             print("Checkout completed")
#         elif booked_room == "display":
#             print("")
            
        
# booking_room()



class HotelManager:
    def __init__(self, rooms):
        self.hotel_rooms = rooms
    
    def book_room(self, room_number, customer_name):
        if room_number in self.hotel_rooms:
            if self.hotel_rooms[room_number]["status"] == "available":
                self.hotel_rooms[room_number]["status"] = "booked"
                self.hotel_rooms[room_number]["customer"] = customer_name
                print(f"Room {room_number} booked successfully for {customer_name}.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print("Invalid room number.")

    def checkout_customer(self, room_number):
        if room_number in self.hotel_rooms:
            if self.hotel_rooms[room_number]["status"] == "booked":
                customer_name = self.hotel_rooms[room_number]["customer"]
                self.hotel_rooms[room_number]["status"] = "available"
                self.hotel_rooms[room_number]["customer"] = ""
                print(f"{customer_name} has checked out from Room {room_number}.")
            else:
                print(f"Room {room_number} is already available.")
        else:
            print("Invalid room number.")
    
    def display_room_status(self):
        print("Room Status:")
        for room_number, details in self.hotel_rooms.items():
            print(f"Room {room_number}: Status - {details['status']}, Customer - {details['customer']}")

# Initial hotel room structure
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

hotel_manager = HotelManager(hotel_rooms)

# Example usage:
hotel_manager.display_room_status()
hotel_manager.book_room("103", "Alice")
hotel_manager.book_room("102", "Bob")  # This room is already booked
hotel_manager.checkout_customer("101")
hotel_manager.checkout_customer("104")  # Invalid room number
hotel_manager.display_room_status()







def search_product(products, search_query):
    search_results = []
    search_query_lower = search_query.lower()  # Convert search query to lowercase for case-insensitive search
    for product_id, product_details in products.items():
        if search_query_lower in product_details['name'].lower():
            search_results.append(product_details)
    return search_results

def display_search_results(search_results):
    if search_results:
        print("Search Results:")
        for idx, product in enumerate(search_results, start=1):
            print(f"{idx}. Name: {product['name']}, Category: {product['category']}, Price: ${product['price']}")
    else:
        print("No matching products found.")

# Example product dictionary
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

# Example usage:
search_query = "shirt"
results = search_product(products, search_query)
display_search_results(results)

search_query = "phone"
results = search_product(products, search_query)
display_search_results(results)









