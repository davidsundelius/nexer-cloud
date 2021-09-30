from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
posts = [
    {
      "message": "Hello world",
      "user": "David"
    },
    {
      "message": "Hello world2",
      "user": "Daniel"
    }
    ];

@app.route("/posts", methods = ['GET', 'POST'])
def handlePosts():
  if request.method == 'GET':
    return jsonify(posts)
  else:
    data = request.get_json(force=True)
    posts.append( {
      "message": data["message"],
      "user": data["user"]
    })
    return "{\"status\": true}"

if __name__ == "__main__":
    app.run()
