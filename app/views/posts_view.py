from flask import Flask, json, jsonify, request
from pymongo import results
from pymongo.message import query
from app.models.posts_model import Posts

def init_app(app: Flask):
  @app.post('/posts')
  def create_post():
    try:
      data = request.json
      post = Posts(title=data['title'], author=data['author'], tags=data['tags'], content=data['content'])
      result = post.save()
      print("RESULT", result)
      return result, 201
    
    except Exception as e:
      return f"Missing key: {e}", 405



  @app.get('/posts')
  def read_posts():
    posts_list = Posts.get_all_posts()
    return jsonify(posts_list), 200

  @app.delete('/posts/<int:id>')
  def delete_post(id: int):
    try:
      deleted_post = Posts.deleting_post(id)
      return deleted_post, 200
    except TypeError:
      return "Post does not exist", 404

  @app.get('/posts/<int:id>')
  def get_specific_post(id: int):
    try:
      get_post = Posts.getting_post(id)
      return get_post
    except TypeError:
      return "Post does not exist", 404
    
  @app.patch('/posts/<int:id>')
  def patch_specific_post(id: int):
    try:
      keys_list = ["title", "author", "tags", "content"]
      data = request.json
      for key in data:
        if key not in keys_list:
          return "Key does not exist", 400
      patch_post = Posts.patching_post(id, data)
      print(data)
      return patch_post
    except TypeError:
      return 'Post does not exist', 400
