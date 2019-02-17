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
party_with_wrong_name_type = {
    "name" : 54654,
    "hqAddress" : "Machakos",
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}

party_with_wrong_name_input = {
    "name" : "sasa  ",
    "hqAddress" : "Machakos",
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}
party_with_wrong_address_input = {
    "name" : "name",
    "hqAddress" : "  ",
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}

#a party with an address of wrong data type
party_with_wrong_address_type = {
    "name" : "name",
    "hqAddress" : 123423,
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}


#a party with a wrong logo url
party_with_wrong_logo_url = {
    "name" : "name",
    "hqAddress" : "Hello",
    "logoUrl" : "/images/3RKgQ6",
}

#an office with a name of wrong data type
party_with_name_of_wrong_data_type = {
    "name" : 4564,
    "hqAddress" : "Machakos",
}

party_with_name_of_wrong_data_type = {
    "name" : 4564,
    "hqAddress" : "Machakos",
}
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
    "hqdress" : "Machakos",
}


office_with_correct_data = {
    "name" : "Presidency",
    "office_type" : "legislative",
}
office_with_wrong_office_type_data = {
    "name" : "president",
    "office_type" : "hello"
}

office_with_wrong_office_name_data = {
    "name" : 213,
    "office_type" : "hello"
}

office_with_wrong_office_type_type_input = {
    "name" : "president",
    "office_type" : 12
}

office_with_invalid_key_name = {
    "namesada" : "name",
    "office_type" : "Machakos",
}
office_with_invalid_key_office_type = {
    "name" : "name",
    "office" : "legislative",
}
#an office with empty fields
office_with_empty_fields = {
    "name" : "",
    "office_type" : "",
 }

# #an empty offices list for testing
# empty_offices_list = []

# test data for new user
new_user={
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"edede@email.com",
    "phone_number":"+213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}

create_user_missing_data = {
    "firstname":"",
    "lastname":"",
    "othername":"",
    "email":"",
    "phone_number":"",
    "passport_url":"",
    "password":"secretpass",
}

create_user_wrong_email_input = {
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"mail",
    "phone_number":"+213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}

create_user_wrong_firstname_input = {
    "firstname":" ",
    "lastname":"lastname",
    "othername":"othername",
    "email":"mail",
    "phone_number":"+213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}
create_user_wrong_othername_input = {
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":3454,
    "email":"e@email.com",
    "phone_number":"+213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}
create_user_wrong_lastname_input = {
    "firstname":"firstname",
    "lastname":123,
    "othername":"othername",
    "email":"e@email.com",
    "phone_number":"+213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}
create_user_wrong_othername_input = {
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":3454,
    "email":"e@email.com",
    "phone_number":"+213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}
create_user_wrong_phone_number_input = {
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"e@email.com",
    "phone_number":2|3,
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}


create_user_wrong_passport_url_input = {
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"e@email.com",
    "phone_number":2|3,
    "passport_url":"oo.g/images/B9U4PK",
    "password":"secretpass",
}