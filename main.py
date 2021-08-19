from os import error
from instagrapi import Client
from flask import Flask,jsonify
import json
import random

print('Login in..')

def write_file(data, filename):
    fh = open(filename, "w")
    try:
        fh.write(json.dumps(data))
    finally:
        fh.close()

def read_file(filename):
    fh = open(filename, "r")
    return json.load(fh)


# ACCOUNT_USERNAME = 'digital_solution_673'
# ACCOUNT_PASSWORD = 'Digitalsolution@1234'
# ACCOUNT_USERNAME = 'datusers'
# ACCOUNT_PASSWORD = 'datusers##'
# ACCOUNT_USERNAME = 'tester.dp'
# ACCOUNT_PASSWORD = 'dimpesh@123'
# ACCOUNT_USERNAME = 'instatracker001'
# ACCOUNT_PASSWORD = 'dat123@@'
# ACCOUNT_USERNAME = 'instatracker003'
# ACCOUNT_PASSWORD = 'instatracker'
# ACCOUNT_USERNAME = 'techdigi_788'
# ACCOUNT_PASSWORD = 'Techdigi788@1234'
# ACCOUNT_USERNAME = 'dimpesh.tester'
# ACCOUNT_PASSWORD = 'dimpesh@123'
# ACCOUNT_USERNAME = 'digitech_799'
# ACCOUNT_PASSWORD = 'Digitech@1234'
# ACCOUNT_USERNAME = 'instatracker002'
# ACCOUNT_PASSWORD = 'instatracker'
# ACCOUNT_USERNAME = 'ka.vyasharma__'
# ACCOUNT_PASSWORD = 'wn+{?R656sdty6s0,(}fY[+'
# ACCOUNT_USERNAME = 'dheeraj009joshi'
# ACCOUNT_PASSWORD = '12345678900'
ACCOUNT_USERNAME = 'hiteshgehlot2019'
ACCOUNT_PASSWORD = 'instatracker3'
# ACCOUNT_USERNAME = 'hydra123schol'
# ACCOUNT_PASSWORD = 'hydra@123'
# ACCOUNT_USERNAMES=['dheeraj009joshi','hiteshgehlot2019','ka.vyasharma__','instatracker002','instatracker003']
IG_CREDENTIAL = ACCOUNT_USERNAME
# # IG_CREDENTIAL = random.choice(ACCOUNT_USERNAMES)
print(IG_CREDENTIAL)
cl = None

try:
    cl = Client(read_file(IG_CREDENTIAL))
    print("valid credentials.json")

except:
    print("invalid credentials.json")

    cl = Client()
    print('done')
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    print("valid login")
    write_file(cl.get_settings(), IG_CREDENTIAL)
app = Flask(__name__)


@app.route("/")
def index():
    try:
        return "Hello World!"
    except:
        return 'Please Connect to internet'
@app.route("/favicon.ico")
def index2():
    try:
        print('faviconn')
        return "favicon.ico"
    except:
        return 'Please Connect to internet'
@app.route("/user/<username>")
def user(username):
    
    
    user_id = cl.user_id_from_username(username)
    medias = cl.user_info(user_id).dict()
    print(type(medias))
    return medias



@app.route('/followers/<username>')
def followers(username):  
   
    
    user_id = cl.user_id_from_username(username)
    medias = cl.user_followers(user_id)
    medias=str(medias)
    list=medias.replace("), 'media_type'","', 'media_type'")
    list=list.replace('HttpUrl(','')
    list=list.replace("='",":'")
    list=list.replace(",'username'","','username'")
    list=list.replace("UserShort(pk","UserShort{pk")
    list=list.replace("pk=","pk:")
    list=list.replace(",username","',username")
    list=list.replace("stories=[])","stories=[]}")
    list=list.replace("UserShort","")
    list=list.replace(")","")
    list=list.replace(", stories=[]","")
    list=list.replace("full_name=","full_name:")
    list=list.replace("'",'"')
    list=list.replace(",",', "')
    list=list.replace(":",'" :')
    list=list.replace('"https" :','"https:')
    list=list.replace('{','{"')
    list=list.replace('_ ','_')
 
    
    print(list)
    data=json.loads(list)
    temp = []
    for t in data:
        data[t].pop(" full_name",None)
        data[t].pop(' scheme',None)
        data[t].pop(' host',None)
        data[t].pop(' tld',None)
        data[t].pop(' host_type',None)
        data[t].pop(' path',None)
        data[t].pop(' query',None)
        print(data[t])
        print(type(data[t]))
        print(type(data[t]))
        temp.append(data[t])
    return jsonify(temp) 



@app.route('/following/<username>')
def following(username): 
    
    
    user_id = cl.user_id_from_username(username)
    medias = cl.user_following(user_id)
    medias=str(medias)
    list=medias.replace("), 'media_type'","', 'media_type'")
    list=list.replace('HttpUrl(','')
    list=list.replace("='",":'")
    list=list.replace(",'username'","','username'")
    list=list.replace("UserShort(pk","UserShort{pk")
    list=list.replace("pk=","pk:")
    list=list.replace(",username","',username")
    list=list.replace("stories=[])","stories=[]}")
    list=list.replace("UserShort","")
    list=list.replace(")","")
    list=list.replace(", stories=[]","")
    list=list.replace("full_name=","full_name:")
    list=list.replace("{","{'")
    list=list.replace(":","':")
    list=list.replace('" ','" ')
    json.dumps(list)
    return list    

@app.route("/hastag/top/<hastag>")
def hastag_top(hastag):
    
    medias = cl.hashtag_medias_top(str(hastag),50)
    hastag=[]
    for aap in medias:
        data=aap.dict()
        data.pop("caption_text",None)
        print(data)
        hastag.append(data)
    list=str(hastag)
    list=list.replace("), 'media_type'","', 'media_type'")
    list=list.replace('HttpUrl(','')
    
    
   
    
    json.dumps(hastag)
    return hastag

@app.route("/hastag/recent/<hastag>")
def hastag_recent(hastag):
    
    medias = cl.hashtag_medias_recent(str(hastag),50)
    hastag=[]
    for aap in medias:
        data=aap.json()
        print(data)
        hastag.append(data)
    hastag=str(hastag)
    json.dumps(hastag)
    return hastag


@app.route("/stories/<username>")
def user_stories(username):
    
    user_id = cl.user_id_from_username(username)
    data= cl.user_stories(user_id)
    story=[]
    for media in data:
        media=media.json()
        story.append(media)
    list=str(story)
    list=list.replace("'","")
    list=list.replace("']","]")
    json.dumps(list)

    return list

@app.route("/posts/<username>")
def user_posts(username):
   
    
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id)
    list=[]
    for medis in medias:
        # print(type(medias))
        # print(type(medis))
        data=medis.json()
        # print(type(data))
        dictiy=json.loads(data)
        # print(type(dictiy))
        dictiy.pop("caption_text", None)
        data=json.dumps(dictiy)

        list.append(data)
        
        
    list=str(list)
    
    list=list.replace("'","")
    list=list.replace("']","]")
    json.dumps(list)
    return list


@app.route("/media-comments/<media_id>")
def media_comment(media_id):
    
    medias = cl.media_comments(str(media_id))
    list=[]
    for i in medias:
        comments=i.json()
        print(comments)
        list.append(comments)
    list=str(list)
    list=list.replace("'","")
    list=list.replace("']","]")
    json.dumps(list)
    return list

@app.route("/media-likes/<media_id>")
def media_like(media_id):
    
    medias = cl.media_likers(str(media_id))
    list=[]
    for i in medias:
        comments=i.json()
        print(comments)
        list.append(comments)
    list=str(list)
    list=list.replace("\\", '')
    list=list.replace("'","")
    list=list.replace("']","]")
    json.dumps(list)
    return list
@app.route('/me-not-following-back/<username>')
def me_not_following_back(username):
   
    user_id = cl.user_id_from_username(username)
    followers=cl.user_followers(user_id)
    following=cl.user_following(user_id)
    data=[]
    for items in followers:
     if items not in following:
        users=cl.user_info(items).json()
        data.append(users)
        print(users)
    data=str(data)
    list=data.replace("'","")
    # list=list.replace("']","]")
    json.dumps(list)  
    return list

@app.route('/they-not-following-back/<username>')
def they_not_following_back(username):
    
    user_id = cl.user_id_from_username(username)
    followers=cl.user_followers(user_id)
    following=cl.user_following(user_id)
    data=[]
    for items in following:
     if items not in followers:
        users=cl.user_info(items)
        data.append(users)
        print(users)
    data=str(data)
    list=data.replace("'","")
    list=list.replace("']","]")
    json.dumps(data)  
    return data


if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0',port=8080)
