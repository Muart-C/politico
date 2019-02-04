#party class for data structure model

#instatiate an empty list of political parties
political_parties = []

class Party(object):
    """Party model to store party data in data structures"""
    def __init__(self, Id, name, hqAddress, logoUrl):
        self.Id = Id
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    #create a party.
    def add_party(self):
        political_parties.append(self)


    