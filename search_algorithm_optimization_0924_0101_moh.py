# 代码生成时间: 2025-09-24 01:01:44
from bottle import route, run, request, response

# 定义全局变量，用于存储数据
DATA = []

# 定义一个函数，用于添加数据
def add_data(data):
    global DATA
    DATA.append(data)
    return {"status": "success", "message": "Data added successfully"}

# 定义一个函数，用于搜索数据
def search_data(query):
    global DATA
    results = [item for item in DATA if query.lower() in item['name'].lower()]
    if not results:
        return {"status": "error", "message": "No results found"}
    return {"status": "success", "message": "Results found", "results": results}

# 定义一个Bottle路由，用于添加数据
@route('/add', method='POST')
def add_data_route():
    try:
        data = request.json
        if not data:
            response.status = 400
            return {"status": "error", "message": "Invalid data format"}
        result = add_data(data)
        return result
    except Exception as e:
        response.status = 500
        return {"status": "error", "message": str(e)}

# 定义一个Bottle路由，用于搜索数据
@route('/search', method='GET')
def search_data_route():
    try:
        query = request.query.q
        if not query:
            response.status = 400
            return {"status": "error", "message": "Query parameter is required"}
        result = search_data(query)
        return result
    except Exception as e:
        response.status = 500
        return {"status": "error", "message": str(e)}

# 运行Bottle服务
if __name__ == '__main__':
    run(host='localhost', port=8080)
