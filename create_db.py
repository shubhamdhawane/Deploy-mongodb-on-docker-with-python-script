import pymongo
import logging

myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

#adding new database
db = myclient["customersdb"]
customers = db["customers"]


dblist = myclient.list_database_names()
print("list database {}".format(dblist))

#checking if it is already added to the database
if "customersdb" in dblist:
    print("The database exists.")
else : 
    print("none")

#adding many data to the db
customers_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = customers.insert_many(customers_list)

#adding one data to the db
x = customers.insert_one({ "name": "Peter", "address": "Lowstreet 27" })

#find all item 
search_all = db["customers"].find()
for x in search_all : 
    print(x)

print()
#find random and only one
search_one = db["customers"].find_one()
print("result of search one")
print(search_one,"\n")


#find specific item 
search_specific = db["customers"].find({"address":"Main Road 989"})
print("result of search many")
for item in search_specific : 
    print(item,"\n")

#find with advance query
find_regex = db["customers"].find({"address":{"$gt":"S"}})
print("find with regex 1")
for item in find_regex : 
    print(item)

print()
find_regex_2 = db["customers"].find({"address":{"$regex":"^O"}})
print("find with regex 2")
for item in find_regex_2 : 
    print(item)

print()
#sort the result
#based on name
sort_result = db["customers"].find().sort("name")
print("sorting result based on name")
for item in sort_result : 
    print(item)

print()
#sort descending 
sort_result_2 = db["customers"].find().sort("name",-1)
print("sorting result descending based on name")
for item in sort_result_2 : 
    print(item)

#limit result
print()
limit_result = db["customers"].find().limit(5)
print("limit result")
for i in limit_result : 
    print(i)


print()
#update one item 
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
db["customers"].update_one(myquery, newvalues)
print("update result")
for x in db["customers"].find() : 
    print(x)

print()
#update many item 
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
db["customers"].update_many(myquery, newvalues)
print("many update result")
for x in db["customers"].find() : 
    print(x)

# delete has similar syntax with insert
# insert_one -> delete_one
# insert_many -> delete_many

print()
#delete all item 
x = customers.delete_many({})
print(x.deleted_count, " documents deleted.") 
