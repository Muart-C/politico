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

update_party_name_without_request_object = {}

update_party_name = {
    "name" : "ODM",
}

update_blank_party_name = {
    "name" : " ",
}

update_party_name_not_string = {
    "name" : 13243,
}

cast_vote = {
    "candidate_id" : 1,
    "user_id" : 1,
    "office_id" : 1,
}


party_with_empty_fields = {
    "name" : "",
    "hqAddress" : "",
}

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

party_with_wrong_address_type = {
    "name" : "name",
    "hqAddress" : 123423,
    "logoUrl" : "https://goo.gl/images/3RKgQ6",
}

party_with_wrong_logo_url = {
    "name" : "name",
    "hqAddress" : "Hello",
    "logoUrl" : "/images/3RKgQ6",
}

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

office_with_empty_name = {
    "name" : "",
    "office_type" : "legislative",
 }

office_with_empty_office_type = {
    "name" : "senate",
    "office_type" : "",
 }
office_with_wrong_office_type = {
    "name" : "senate",
    "office_type" : "wrong",
 }

new_user={
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"user@email.com",
    "phone_number":"2134254435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"1232AONon45",
}
new_user_2={
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"ndirangu@email.com",
    "phone_number":"4213425435",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"bAse730onGG23",
}
user_login={
    "email":"user@email.com",
    "password":"1232AONon45",
}

user_login_wrong_email={
    "email":"me@email.com",
    "password":"secretpass",
}

user_login_wrong_password={
    "email":"you@email.com",
    "password":"secretpassing",
}

user_login_empty_email={
    "email":"",
    "password":"secretpassing",
}

user_login_wrong_email_format={
    "email":"you@emailcom",
    "password":"secretpassing",
}

user_login_blank_password={
    "email":"you@emailcom",
    "password":"",
}

user_login_password_less_than_six_characters={
    "email":"you@emailcom",
    "password":"you",
}

admin_login={
    "email":"muathe.ndirangu@gmail.com",
    "password":"bAse730onE",
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
    "phone_number":"76676",
    "passport_url":"https://goo.gl/images/B9U4PK",
    "password":"secretpass",
}


create_user_wrong_passport_url_input = {
    "firstname":"firstname",
    "lastname":"lastname",
    "othername":"othername",
    "email":"e@email.com",
    "phone_number":"2453",
    "passport_url":"images/B9U4PK",
    "password":"secretpass",
}

create_candidate_user_does_not_exist = {
    "candidate_id":123,
    "party_id":1
}
create_candidate_party_does_not_exist = {
    "candidate_id":1,
    "party_id":12132
}

cast_vote={
	"office_id":1,
	"candidate_id":1
}

cast_vote_wrong_candidate={
	"office_id":1,
	"candidate_id":"candid"
}

cast_vote_wrong_office={
	"office_id":"office",
	"candidate_id":1
}


cast_vote_no_office={
	"candidate_id": 1
}

cast_vote_no_user={
	"office_id": 1
}

register_candidate={
	"party_id":1,
	"candidate_id": 1
}

register_candidate_no_party={
	"candidate_id": 1
}

register_candidate_no_user={
	"party_id": 1
}