import random
from numpy import append
from instagrapi import Client
import json

import csv
import pandas as pd


print("Login in..")


def write_file(data, filename):
    fh = open(filename, "w")
    try:
        fh.write(json.dumps(data))
    finally:
        fh.close()
def read_file(filename):
    fh = open(filename, "r")
    return json.load(fh)

ACCOUNT_USERNAME = 'dheeraj009joshi'
ACCOUNT_PASSWORD = '12345678900'


IG_CREDENTIAL = ACCOUNT_USERNAME

print(IG_CREDENTIAL)
cl = None

try:
    cl = Client(read_file(IG_CREDENTIAL))
    print("valid credentials.json")

except:
    print("invalid credentials.json")

    cl = Client()
    print("done")
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    print("valid login")
    write_file(cl.get_settings(), IG_CREDENTIAL)



# # usernamee=["buzzfeedtasty",
# # "houseofhighlights",
# # "amandaeliselee",
# # "foodnetwork",
# # "love_food",
# # "twisted",
# # "tipsybartender",
# # "paigehathaway",
# # "andreybatt",
# # "laurendrainfit",
# # "foodandwine",
# # "foodyfetish",
# # "healthyfitnessmeals",
# # "ronniecoleman8",
# # "how2mealprep",
# # "wholefoods",
# # "whitneyysimmons",
# # "foodyeating",]
# # # loc=cl.location_search(34.0223519,-118.285117)
# # # # print(loc[0])
# # # medias = cl.location_medias_top(4612,50)
# # # print(type(medias))
# # # print(medias)
# # # for data in medias:
# # #     item=data.json()
# # #     print(type(item))
# # #     i=json.loads(item)
# # #     print(type(i))
# # #     usernamee.append(i["user"]["username"])

# # c=0
# # user_id=[]
# # for user_detail in usernamee:
# #     if c==1:
# #         break
# #     else:
# #         data=cl.user_id_from_username(user_detail)
# #         id=cl.user_info(data).json()
# #         json_data=json.loads(id)
# #         print()
# #         print()
# #         print()
# #         print(json_data)
# #         print()
# #         print()
# #         print()
# #         user_id.append(json_data["pk"])



# # for posts in user_id:
# #     if c==1:
# #         break
# #     else:
# #         data=cl.user_medias(posts,6)
# #         for i in data:
# #             item=i.json()
# #             item=json.loads(item)
# #             print()
# #             print()
# #             print()
# #             print(item)
# #             print()
# #             print()
# #             print()

    


data=cl.media_pk_from_code('CRC57cpjDtn')
med=cl.media_info(data)
print(med.json())


name=cl.user_id_from_username('selenagomez')
info=cl.user_info(name)
print(info.json())