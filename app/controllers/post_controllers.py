from app.models.posts_model import Posts

def getting_all_posts():
  posts_list = Posts.get_all_posts()
  return posts_list, 200

def adding_post(data):
  post = Posts(title=data['title'], author=data['author'], tags=data['tags'], content=data['content'])
  result = post.save()
  return result

def deleting_post(id):
  deleted_post = Posts.deleting_post(id)
  return deleted_post

def getting_specific_post(id):
  get_post = Posts.getting_post(id)
  return get_post

def updating_post(id, data):
  patch_post = Posts.patching_post(id, data)
  return patch_post

