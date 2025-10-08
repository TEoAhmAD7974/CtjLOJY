# 代码生成时间: 2025-10-08 23:34:40
from bottle import Bottle, run, request, response, static_file

# 初始化Bottle应用
app = Bottle()

# 假设的社交媒体帖子存储
posts = []

# 路由：获取所有帖子
@app.route('/posts', method='GET')
def get_posts():
    """
    获取所有社交媒体帖子
    :return: JSON格式的帖子列表
    """
    return {'posts': posts}

# 路由：创建新帖子
@app.route('/posts', method='POST')
def create_post():
    """
    创建一个新的社交媒体帖子
    :return: JSON格式的创建结果
    """
    data = request.json
    if not data or 'content' not in data:
        response.status = 400  # 错误请求
        return {'error': 'Bad Request'}
    post = {'content': data['content'], 'id': len(posts) + 1}
    posts.append(post)
    return {'message': 'Post created', 'post': post}

# 路由：获取单个帖子
@app.route('/posts/<post_id:int>', method='GET')
def get_post(post_id):
    """
    根据ID获取单个社交媒体帖子
    :param post_id: 帖子的ID
    :return: JSON格式的帖子详情
    """
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        response.status = 404  # 未找到
        return {'error': 'Post not found'}
    return post

# 路由：更新帖子
@app.route('/posts/<post_id:int>', method='PUT')
def update_post(post_id):
    """
    更新一个社交媒体帖子
    :param post_id: 帖子的ID
    :return: JSON格式的更新结果
    """
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        response.status = 404  # 未找到
        return {'error': 'Post not found'}
    data = request.json
    if not data or 'content' not in data:
        response.status = 400  # 错误请求
        return {'error': 'Bad Request'}
    post['content'] = data['content']
    return {'message': 'Post updated', 'post': post}

# 路由：删除帖子
@app.route('/posts/<post_id:int>', method='DELETE')
def delete_post(post_id):
    """
    删除一个社交媒体帖子
    :param post_id: 帖子的ID
    :return: JSON格式的删除结果
    """
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        response.status = 404  # 未找到
        return {'error': 'Post not found'}
    posts.remove(post)
    return {'message': 'Post deleted'}

# 启动应用
if __name__ == '__main__':
    run(app, host='localhost', port=8080)