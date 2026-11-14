
from langchain_core.tools import tool

# Sample IT tickets for our demonstration
TICKETS = {
    "INC-101": {
        "status": "Open",
        "issue": "Application server is unavailable",
        "priority": "High",
        "assigned_to": "IT Support Team",
    },
    "INC-102": {
        "status": "Resolved",
        "issue": "Employee unable to access email",
        "priority": "Medium",
        "assigned_to": "Service Desk",
    },
}


@tool
def lookup_ticket(ticket_id: str) -> str:
    """Look up an existing IT incident using its ticket ID."""
    ticket = TICKETS.get(ticket_id.strip().upper())

    if not ticket:
        return f"No ticket found with ID {ticket_id}."

    return (
        f"Ticket ID: {ticket_id.upper()}\n"
        f"Issue: {ticket['issue']}\n"
        f"Status: {ticket['status']}\n"
        f"Priority: {ticket['priority']}\n"
        f"Assigned team: {ticket['assigned_to']}"
    )
