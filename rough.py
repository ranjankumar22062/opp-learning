from opps_project import chatbook

user1=chatbook()
print(user1.id)
#using static method direct from class not from object
chatbook.set_id(10)
user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)