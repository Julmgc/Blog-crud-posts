from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('DATABASE_URL'), os.getenv('DATABSE_PORT'))
db = client.kenzie

db.posts
db.idsequences
db.idsequences.insert_one({
    "id" : "posts",
    "value" : 0
})
def get_sequence(name):
    collection = db.idsequences
    document = collection.find_one_and_update({"id": name}, {"$inc": {"value": 1}}, return_document=True)
    return document["value"]

class Posts():

  def __init__(self, title: str, author: str, tags, content: str):
    self.title: str = title
    self.author: str = author
    self.tags = tags
    self.content: str = content
    self.id = get_sequence("posts")
    self.created_at = datetime.utcnow()
   
  def save(self):
    post = db.posts.insert_one(self.__dict__)
    del self.__dict__['_id']
    return self.__dict__

  def patching_post( id, data):
    data["updated_at"] = str(datetime.utcnow())
    update = {"$set": data}
    post_to_update = db.posts.find_one({"id": id})
    del post_to_update['_id']
    db.posts.update_one(post_to_update, update)
    return post_to_update

  @staticmethod
  def get_all_posts():
    posts_list = list(db.posts.find())
    for post in posts_list:
      del post['_id']
    return posts_list

  @staticmethod
  def deleting_post(id):
    del_post = db.posts.find_one({"id":id})
    del del_post['_id']
    return del_post
  
  @staticmethod
  def getting_post(id):
    specific_post = db.posts.find_one({"id": id})
    del specific_post['_id']
    return specific_post



