import random
from numpy import True_, append
from instagrapi import Client
import json

def exit():
    global c
    c=1
c=0
# session_id=[]
ACCOUNT_USERNAME = input('usernamr_1')
# ACCOUNT_PASSWORD = input('pass_1')
# cl = Client()
# print("done")
# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
# print("valid login")
# data=cl.get_settings()
# print(data)
# session_id.append(data)
# print(session_id)
#########################################################
def read_file(filename):
    fh = open(filename, "r")
    return json.load(fh)
IG_CREDENTIAL = ACCOUNT_USERNAME
cl = Client(read_file(IG_CREDENTIAL))


hastag = input("Enter hastag")
medias = cl.location_medias_top("delhi",10)
usernamee=[]
for aap in medias:
    if c==1:
        break
    else:
        data=aap.json()
        data=json.loads(data)
        print()
        print()
        print()
        print(data)
        print()
        print()
        print()
        print()
        try:
            usernamee.append(data["user"]["username"])
        except:
            pass
    

# user_id=[]
# for user_detail in usernamee:
#     if c==1:
#         break
#     else:
#         data=cl.user_id_from_username(user_detail)
#         id=cl.user_info(data).json()
#         json_data=json.loads(id)
#         print()
#         print()
#         print()
#         print(json_data)
#         print()
#         print()
#         print()
#         user_id.append(json_data["pk"])



# for posts in user_id:
#     if c==1:
#         break
#     else:
#         data=cl.user_medias(posts,6)
#         for i in data:
#             item=i.json()
#             item=json.loads(item)
#             print()
#             print()
#             print()
#             print(item)
#             print()
#             print()
#             print()


