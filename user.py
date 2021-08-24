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

ACCOUNT_USERNAME = 'Maidenchai2020'
ACCOUNT_PASSWORD = 'Hyderabad123'
# ACCOUNT_USERNAME = 'miamiheatmapp'
# ACCOUNT_PASSWORD = 'Hyderabad123'
# ACCOUNT_USERNAME = 'dheerajjoshi750'
# ACCOUNT_PASSWORD = 'dheeraj12'
# ACCOUNT_USERNAME = 'dheerajjoshi3932'
# ACCOUNT_PASSWORD = 'dheeraj12'
# ACCOUNT_USERNAME = 'dheerajjoshi2160'
# ACCOUNT_PASSWORD = 'dheeraj12'
# ACCOUNT_USERNAME = 'dheerajjoshi773'
# ACCOUNT_PASSWORD = 'dheeraj12'
# ACCOUNT_USERNAME2 = 'dheeraj009joshi'
# ACCOUNT_PASSWORD = 'dheerajig'
#ACCOUNT_USERNAME = 'ig11124'
#ACCOUNT_PASSWORD = 'dheeraj12'

IG_CREDENTIAL = ACCOUNT_USERNAME
ACCOUNT_USERNAMES=['miamiheatmapp']
# IG_CREDENTIALS = random.choice(ACCOUNT_USERNAMES)
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



datas=cl.location_medias_recent(4612,50)
hastags=[]
for aap in datas:
    data=aap.json()
    hastags.append(data)

print(len(hastags))
pk = []
taken_at = []
media_type=[]
thumbnail_url = []
product_type = []
latitude = []
longitude = []
address = []
comment_count = []
view_count = []
like_count = []
caption_text = []
video_url = []
video_duration = []
usernamee=[]
pk_user=[]
full_name=[]
profile_pic_url=[]
print(hastags)
for item in hastags:
    
    
        
    item = json.loads(item)
    print(item)
    try:
        usernamee.append(item["user"]["username"])
        
    except:
        pass
    try:
        pk_user.append(item["user"]["pk"])
        
    except:
        pass
    try:
        full_name.append(item["user"]["full_name"])
        
    except:
        pass
    try:
        profile_pic_url.append(item["user"]["profile_pic_url"])
        
    except:
        pass
   
    try:
        pk.append(item["pk"])
    except:
        pk.append('null')
    
    try:
        taken_at.append(item["taken_at"])
    except:
        taken_at.append('null')

    try:
        if item["taken_at"]==8:
            thumbnail_url.append(item["resources"][1]["thumbnail_url"])
        else:   

            thumbnail_url.append(item["thumbnail_url"])
    except:
        thumbnail_url.append("null")
    try:

        media_type.append(item["media_type"])
    except:
        media_type.append('nll')
    try:

        product_type.append(item["product_type"])
    except:
        product_type.append('null')
    try:
        latitude.append(item["location"]["lat"])
    except:
        latitude.append('null')
    try:
        longitude.append(item["location"]["lng"])
    except:
        longitude.append('null')
    try:
        address.append(item["location"]["address"])
    except:
        address.append('address')
    try:
        view_count.append(item["view_count"])
    except:
        view_count.append('null')
    try:

        like_count.append(item["like_count"])
    except:
        like_count.append('null')
    try:
        caption_text.append(item["caption_text"])
    except:
        caption_text.append('null')
    try:

        video_url.append(item["video_url"])
    except:
        video_url.append('null')
    try:

        video_duration.append(item["video_duration"])
    except:
        video_duration.append("null")
    try:

        comment_count.append(item["comment_count"])
    except:
        comment_count.append('null')

print(usernamee)  



user_pk=[]
user_name=[]
full_name=[]
is_private=[]
profile_pic_url=[]
profile_pic_url_hd=[]
is_verified=[]
media_count=[]
follower_count=[]
following_count=[]
biography=[]
native_place=[]
external_url=[]
is_business=[]
public_email=[]




userrr=[]
for users in usernamee:
    print()
    print()
    print(users)

    # try:
    #     cl = Client(read_file(IG_CREDENTIALS))
    #     print("valid credentials.json")

    # except:
    #     print("invalid credentials.json")

    #     cl = Client()
    #     print("done")
    #     cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    #     print("valid login")
    #     write_file(cl.get_settings(), IG_CREDENTIAL)

    data=cl.user_id_from_username(users)
    id=cl.user_info(data).json()
    json_data=json.loads(id)
    print("..................................", type(json_data))
    print(id)
    userrr.append(json_data)


    

# for count,i in enumerate(userrr):
    
#     print("..........................", "type of userrr:   " , type(userrr))
#     print("........................", "type of i  ", type(i))
    
#     print()
#     print()
#     print()

#     print(i)

#     print()
#     print()
#     print()
#     try:
#         user_pk.append(i["pk"])
#         print()
#         print('this')
#         print(i["pk"])
#         print()
#     except Exception as e:
#         print('in exception')
#         print(e)
#         user_pk.append('null')
#     try:
#         user_name.append(i["username"])
#         print()
#         print('this')
#         print(i["pk"])
#         print()
#     except Exception as e:
#         print('in exception')
#         print(e)
#         user_name.append('null')
#     try:
#         full_name.append(i["full_name"])
#     except:
#         full_name.append('null')
#     try:
#         is_private.append(i["is_private"])
#     except:
#         is_private.append('null')
#     try:
#         profile_pic_url.append(i["profile_pic_url"])
#     except:
#         profile_pic_url.append('null')
#     try:
#         profile_pic_url_hd.append(i["profile_pic_url_hd"])
#     except:
#         profile_pic_url_hd.append('null')
#     try:
#         is_verified.append(i["is_verified"])
#     except:
#         is_verified.append('null')
#     try:
#         media_count.append(i["media_count"])
#     except:
#         media_count.append('null')
#     try:
#         follower_count.append(i["follower_count"])
#     except:
#         follower_count.append('null')
#     try:
#         following_count.append(i["following_count"])
#     except:
#         following_count.append('null')
#     try:
#         biography.append(i["biography"])
#     except:
#         biography.append('null')
#     try:
#         data=str(i["biography"]).split(" ")
#         print(data)
#         data1=data.index("📍")
#         item=data[data1+1]
#         item2=data[data1]
#         print(data1)
#         print()
#         print()
#         print(item)
#         print()
#         print(item2)
#         native_place.append(item)
#     except:
#         native_place.append('null')
#     try:
#         external_url.append(i["external_url"])
#     except:
#         external_url.append('null')
#     try:
#         is_business.append(i["is_business"])
#     except:
#         is_business.append('null')
#     try:
#         public_email.append(i["public_email"])
#     except:
#         public_email.append('null')


post_user_pk=[]
post_user_username=[]
post_pk=[]
post_taken_at=[]
post_thumbnail_url=[]
post_media_type=[]
post_product_type=[]
post_view_count=[]
post_like_count=[]
post_caption_text=[]
post_video_url=[]
post_video_duration=[]
post_comment_count=[]


for post in user_pk:
    print(type(post))

    data=cl.user_medias(post,6)

    for i in data:
        item=i.json()
        item=json.loads(item)
        print(type(item))
        
        # user_pk.append(item)
        try:
            post_user_pk.append(item["user"]["pk"])
        except:
            post_user_pk.append('null')
        try:
            post_user_username.append(item["user"]["username"])
        except:
            post_user_username.append('null')
        try:
            post_pk.append(item["pk"])
        except:
            post_pk.append('null')
        
        try:
            post_taken_at.append(item["taken_at"])
        except:
            post_taken_at.append('null')

        try:
            if item["taken_at"]==8:
                post_thumbnail_url.append(item["resources"][1]["thumbnail_url"])
            else:   

                post_thumbnail_url.append(item["thumbnail_url"])
        except:
            thumbnail_url.append("null")
        try:

            post_media_type.append(item["media_type"])
        except:
            post_media_type.append('nll')
        try:

            post_product_type.append(item["product_type"])
        except:
            post_product_type.append('null')
     
        try:
            post_view_count.append(item["view_count"])
        except:
            post_view_count.append('null')
        try:

            post_like_count.append(item["like_count"])
        except:
            post_like_count.append('null')
        try:
            post_caption_text.append(item["caption_text"])
        except:
            post_caption_text.append('null')
        try:

            post_video_url.append(item["video_url"])
        except:
            post_video_url.append('null')
        try:

            post_video_duration.append(item["video_duration"])
        except:
            post_video_duration.append("null")
        try:

            post_comment_count.append(item["comment_count"])
        except:
            post_comment_count.append('null')


df_user_post = pd.DataFrame({

'user_it':post_user_pk,
'username':post_user_username,
'post_id':post_pk,
'taken_at':post_taken_at,
'media_type':post_media_type,
'thumbnail_url':post_thumbnail_url,
'product_type':post_product_type,
'comment_count':post_comment_count,
'view_count':post_view_count,
'like_count':post_like_count,
'caption_text':post_caption_text,
'video_url':post_video_url,
'video_duration':post_video_duration,

})
print(df_user_post)
filename_user = 'hastag' + "_user_posts.csv"

df_user_post.to_csv(filename_user)




# # # # # # # # # # # # # # # # # # # user  detail  csv ####################################


# df_user=pd.DataFrame({'pk':user_pk,
# 'username':user_name,
# 'full_name':full_name,
# 'profile_pic_url':profile_pic_url,
# 'profile_pic_url_hd':profile_pic_url_hd,
# 'is_verified':is_verified,
# 'media_count':media_count,
# 'follower_count':follower_count,
# 'following_count':following_count,
# 'biography':biography,
# 'native_place':native_place,
# 'external_url':external_url,
# 'is_business':is_business,
# 'public_email':public_email,


# })


# print(df_user)
# filename_user = hastag + "_user.csv"

# df_user.to_csv(filename_user)

# # # # # # # # # # # # # # # # # # #   hastag  csv    #   # # # # # ## # # # # # # # ##  # 


df_hastag = pd.DataFrame({'pk':pk,
'taken_at':taken_at,
'media_type':media_type,
'thumbnail_url':thumbnail_url,
'product_type':product_type,
'latitude':latitude,
'longitude':longitude,
'address':address,
'comment_count':comment_count,
'view_count':view_count,
'like_count':like_count,
'caption_text':caption_text,
'video_url':video_url,
'video_duration':video_duration,
'username':usernamee,
'user_pk':pk_user,
'full_name':full_name,
'profile_pic_url':profile_pic_url,


})
filename = 'location' + ".csv"

df_hastag.to_csv(filename)





df_location= pd.DataFrame({

'latitude':latitude,
'longitude':longitude,
'address':address,
'username':usernamee,
'user_pk':pk_user,
})
filename = 'hastag' + "location.csv"

df_hastag.to_csv(filename)



