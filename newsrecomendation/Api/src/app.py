from flask import Flask, request, jsonify
from flask_cors import CORS
from newsrecomendation.Api.src.articleService import ArticleService

app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    return jsonify({'name': 'News recommendation API', 'version': '1.0.0'})


@app.route('/articles', methods=['GET'])
def get_articles():
    category = request.args.get('category')
    service = ArticleService()
    response = service.get_articles(category)
    return jsonify(response)


@app.route('/categories', methods=['GET'])
def get_categories():
    service = ArticleService()
    return service.get_categories()


if __name__ == '__main__':
    app.run(debug=True)
