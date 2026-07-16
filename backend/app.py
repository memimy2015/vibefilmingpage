from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 允许前端跨域访问
CORS(app)

# 测试GET接口
@app.route('/api/hello', methods=["GET"])
def hello():
    return jsonify({"msg": "后端接口正常", "data": "来自Render服务端"})

# 接收前端POST请求
@app.route('/api/submit', methods=["POST"])
def submit():
    data = request.get_json()
    return jsonify({"status": "ok", "receive": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
