#party class for data structure model
parties = []
class Party(object):
    """Party model to store party data in data structures"""
    def __init__(self):
        """#instatiate an empty list of political parties."""
        self.political_parties = parties

    #create a party.
    def add_party(self, name, hqAddress, logoUrl):
        party = {
            "Id" : len(self.political_parties)+1,
            "name" : name,
            "hqAddress" : hqAddress,
            "logoUrl" : logoUrl,
        }
        self.political_parties.append(party)
        return party
    
    #get all parties
    def get_parties(self):
        return self.political_parties

    #get one political party
    def get_party(self, Id):
        return [party for party in self.political_parties if party.get("Id") == Id]
        

    