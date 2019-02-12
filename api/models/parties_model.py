from api.utils.validator import generate_id
#party class for data structure model
PARTIES = []
class Party(object):
    """Party model to store party data in data structures"""

    def add_party(self, name, hq_address, logo_url):
        """create a party."""
        party = {
            "id" : generate_id(PARTIES),
            "name" : name,
            "hq_address" : hq_address,
            "logo_url" : logo_url,
        }
        PARTIES.append(party)
        return party


    def get_parties(self):
        """get all parties"""
        return PARTIES

    def get_party(self, party_id):
        """get one political party"""
        return [party for party in PARTIES if party["id"] == party_id]

    def update_party(self, party_id, name):
        for party in PARTIES:
            if(party["id"] == party_id):
                party["name"] = name
                return party
            return party

