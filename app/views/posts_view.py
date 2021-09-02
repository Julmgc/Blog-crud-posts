from flask import Flask, jsonify, request
from pymongo import results
from app.controllers.post_controllers import deleting_post, getting_all_posts, adding_post, deleting_post, getting_specific_post, updating_post

def init_app(app: Flask):
  @app.post('/posts')
  def create_post():
    try:
      data = request.json
      result = adding_post(data)
      return result, 201
    
    except Exception as e:
      return f"Missing key: {e}", 405

  @app.get('/posts')
  def read_posts():
    posts_list = getting_all_posts()
    return jsonify(posts_list), 200

  @app.delete('/posts/<int:id>')
  def delete_post(id: int):
    try:
      deleted_post = deleting_post(id)
      return deleted_post, 200
    except TypeError:
      return "Post does not exist", 404

  @app.get('/posts/<int:id>')
  def get_specific_post(id: int):
    try:
      get_post = getting_specific_post(id)
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
      patch_post = updating_post(id, data)
      return patch_post
    except TypeError:
      return 'Post does not exist', 400
