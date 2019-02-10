"""!api/admin/offices/model.py"""
from api.utils.validator import generate_id
#office class for data structure model
OFFICES = []
class Office():
    """office model to store office data in data structures"""
    def __init__(self):
        """#instantiate an empty list of political offices."""
        self.offices = OFFICES

    def add_office(self, name, office_type):
        """create a office."""
        office = {
            "id" : generate_id(OFFICES),
            "name" : name,
            "office_type" : office_type,
        }
        OFFICES.append(office)
        return office

    def get_offices(self):
        """get all offices"""
        return OFFICES

    def get_office(self, office_id):
        """get one political office"""
        for office in OFFICES:
            if(office["id"] == office_id):
                return office
            return office
