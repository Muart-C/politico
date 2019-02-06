#office class for data structure model
offices = []
class Office(object):
    """office model to store office data in data structures"""
    def __init__(self):
        """#instatiate an empty list of political offices."""
        self.political_offices = offices

    #create a office.
    def add_office(self, office_type, name):
        office = {
            "Id" : len(self.political_offices)+1,
            "office_type" : office_type,
            "name" : name,
        }
        self.political_offices.append(office)
        return office
    
    #get all offices
    def get_offices(self):
        return self.political_offices

    #get one political office
    def get_office(self, Id):
        return [office for office in self.political_offices if office.get("Id") == Id]
        

    