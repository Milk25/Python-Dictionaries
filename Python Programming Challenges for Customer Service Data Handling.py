class TicketManager:
    def __init__(self, tickets):
        self.service_tickets = tickets
    
    def open_ticket(self, ticket_id, customer_name, issue_description):
        if ticket_id not in self.service_tickets:
            self.service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
            print(f"Ticket {ticket_id} opened successfully for {customer_name}.")
        else:
            print(f"Ticket {ticket_id} already exists.")

    def update_ticket_status(self, ticket_id, new_status):
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = new_status
            print(f"Status of Ticket {ticket_id} updated to {new_status}.")
        else:
            print(f"Ticket {ticket_id} does not exist.")

    def display_tickets(self, status=None):
        print("Service Tickets:")
        for ticket_id, ticket_details in self.service_tickets.items():
            if status is None or ticket_details["Status"].lower() == status.lower():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_details['Customer']}, Issue: {ticket_details['Issue']}, Status: {ticket_details['Status']}")

# Sample ticket data
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

ticket_manager = TicketManager(service_tickets)

# Example usage:
ticket_manager.display_tickets()

ticket_manager.open_ticket("Ticket003", "Charlie", "Website loading slow")
ticket_manager.display_tickets()

ticket_manager.update_ticket_status("Ticket002", "open")
ticket_manager.display_tickets("open")







