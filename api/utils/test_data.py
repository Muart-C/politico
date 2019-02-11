party_with_data = {
    "name" : "ANC",
    "hqAddress" : "Kakamega",
    "logoUrl" : "https://goo.gl/images/B9U4PK",
}

party_with_data = {
    "name" : "ANC",
    "hqAddress" : "Kakamega",
    "logoUrl" : "https://goo.gl/images/B9U4PK",
}


#a party with empty fields
party_with_empty_fields = {
    "name" : "",
    "hqAddress" : "",
}

#a party with a name of wrong data type
create_party_with_wrong_name_type = {
    "name" : 4564,
    "hqAddress" : "Machakos",
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}

#a party with an address of wrong data type
create_party_with_wrong_address_type = {
    "name" : "name",
    "hqAddress" : "`234324)!`",
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}


#a party with a wrong logo url
create_party_with_wrong_logo_url = {
    "name" : "name",
    "hqAddress" : "Hello",
    "logoUrl" : "/images/3RKgQ6",
}

#an office with a name of wrong data type
party_with_name_of_wrong_data_type = {
    "name" : 4564,
    "hqAddress" : "Machakos",
}


party_with_invalid_key_name = {
    "namesada" : "name",
    "hqAddress" : "Machakos",
}
party_with_invalid_key_address = {
    "name" : "name",
    "hqAddrs" : "Machakos",
}

#a dictionary containing an office
office_with_data = {
    "name" : "Presidency",
    "office_type" : "Office of the President",
}

#an office with empty fields
office_with_empty_fields = {
    "name" : "",
    "office_type" : "",
 }

#an empty offices list for testing
empty_offices_list = []