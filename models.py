class Destination:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

class Itinerary:
    def __init__(self, destination_id, activity):
        self.destination_id = destination_id
        self.activity = activity

class Expense:
    def __init__(self, destination_id, description, amount):
        self.destination_id = destination_id
        self.description = description
        self.amount = amount

