# Business Class
# Import franchise store information to add to the 2 different businesses owned
from franchise import flagship_store, new_installment, arepas_place


class Business:
    # Constructor method for business, that shows the business name and their franchise location
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        locations = [franchise.address for franchise in self.franchises]
        return f"Business Name: {self.name!r} \n" f"Located at: {locations!r}"


# The 2 class variables for the 2 businesses owned
business_one = Business(
    "Basta Fazoolin' with my Heart", [flagship_store, new_installment]
)
business_two = Business("Take a' Arepa", [arepas_place])
