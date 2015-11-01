USERS = [
    {
        "firstname": "sonu",
        "lastname": "nigam",
        "city": "mumbai",
        "country": "india",
        "profession": ["singer", "composer"],
        "genre": ["music", "film", "bollywood"]
    },
    {
        "firstname": "amitabh",
        "lastname": "bachan",
        "city": "mumbai",
        "country": "india",
        "profession": ["actor", "producer"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "hrithik",
        "lastname": "roshan",
        "city": "mumbai",
        "country": "india",
        "profession": ["actor"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "katrina",
        "lastname": "kaif",
        "city": "mumbai",
        "country": "india",
        "profession": ["actor"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "ranbir",
        "lastname": "kapoor",
        "city": "mumbai",
        "country": "india",
        "profession": ["actor"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "amir",
        "lastname": "khan",
        "city": "mumbai",
        "country": "india",
        "profession": ["actor", "producer", "director"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "kumar",
        "lastname": "sanu",
        "city": "kolkata",
        "country": "india",
        "profession": ["singer", "music director", "actor", "producer"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "kj",
        "lastname": "yesudas",
        "city": "cochin",
        "country": "india",
        "profession": ["singer", "composer"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "shantanu",
        "lastname": "mukherjee",
        "city": "mumbai",
        "country": "india",
        "profession": ["singer"],
        "genre": ["film", "bollywood"]
    },
    {
        "firstname": "tom",
        "lastname": "cruise",
        "city": "newyork",
        "country": "usa",
        "profession": ["actor", "producer"],
        "genre": ["film", "hollywood"]
    },
    {
        "firstname": "dwayne",
        "lastname": "johnson",
        "city": "california",
        "country": "usa",
        "profession": ["actor", "producer"],
        "genre": ["film", "hollywood"]
    },
    {
        "firstname": "leonardo",
        "lastname": "dicaprio",
        "city": "california",
        "country": "usa",
        "profession": ["actor", "producer"],
        "genre": ["film", "hollywood"]
    },
    {
        "firstname": "jennifer",
        "lastname": "lawrence",
        "city": "california",
        "country": "usa",
        "profession": ["actor"],
        "genre": ["film", "hollywood"]
    },
    {
        "firstname": "vin",
        "lastname": "diesel",
        "city": "california",
        "country": "usa",
        "profession": ["actor", "producer", "director", "screenwriter"],
        "genre": ["film", "hollywood"]
    },
    {
        "firstname": "matt",
        "lastname": "damon",
        "city": "massachusetts",
        "country": "usa",
        "profession": ["actor", "producer"],
        "genre": ["film", "hollywood"]
    }
]


# def abc1():
#     for i in USERS:
#         if i['city'] == 'Mumbai' and 'Actor' in i['profession']:
#             print i


# def abc():
#     for i in USERS:
#         if i['city'] == 'Mumbai':
#             print i


# def abc2():
#     filter = u'profession=actor'
#     key, value = filter.split('=')
#     key = str(key.lower())
#     value = str(value.lower())
#     # others = request.matchdict['other']
#     users = []
#     for i in USERS:
#         if key == 'profession' or key == 'genre':
#             for j in i[key]:
#                 if value == j.lower():
#                     users.append(i.copy())
#         else:
#             if i[key].lower() == value:
#                 users.append(i.copy())
#     print users


# def abc3():
#     filter = u'city=mumbai'
#     key, value = filter.split('=')
#     key = str(key.lower())
#     value = str(value.lower())
#     # others = request.matchdict['other']
#     users = []
#     for i in USERS:
#         if i[key].lower() == value.lower():
#             users.append(i.copy())

#     print users

# if __name__ == '__main__':
#     abc2()
