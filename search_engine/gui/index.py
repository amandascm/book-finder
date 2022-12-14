import os
from flask import Flask, render_template, request, url_for, redirect
from search_engine.gui.controller import *

app = Flask(__name__)

results = {
    "field_results": [],
    "text_results": [],
    "field_recommend": {}
}

query = {
    "current": [],
    "total_results": None
}

@app.route('/', methods=['GET'])
def home():
    results['field_results'] = []
    results['text_results'] = []
    query['current'] = []
    results['field_recommend'] = {}
    return render_template(os.path.join('home.html'), field_results=results['field_results'], text_results=results['text_results'], required_field=False, current_query=query['current'], recommend=results['field_recommend'], total_results=query['total_results'])

@app.route('/result', methods=['GET'])
def home_result():
    return render_template(os.path.join('home.html'), field_results=results['field_results'], text_results=results['text_results'], required_field=False, current_query=query['current'], recommend=results['field_recommend'], total_results=query['total_results'])

@app.route('/search/text/', methods=['POST'])
def text_search():
    content = request.form['content']
    if not content:
        results['field_results'] = []
        results['text_results'] = []
        query['current'] = []
        query['total_results'] = None
        results['field_recommend'] = {}
        return render_template(os.path.join('home.html'), field_results=[], text_results=[], required_field=True, current_query=False, recommend={}, total_results=None)
    else:
        results['text_results'] = text_query(content)
        query['current'] = [i for i in [content] if i]
        query['total_results'] = len(results['text_results'])
        results['field_results'] = []
        results['field_recommend'] = {}
        return redirect(url_for('home_result'))

@app.route('/search/field/', methods=['POST'])
def field_search():
    title = request.form['title']
    publisher = request.form['publisher']
    authors = request.form['author']
    isbn = request.form['isbn']
    description = request.form['description']
    # Check if some field is filled
    if not (title or publisher or authors or isbn or description):
        results['field_results'] = []
        results['text_results'] = []
        query['current'] = []
        query['total_results'] = None
        results['field_recommend'] = {}
        return render_template(os.path.join('home.html'), field_results=[], text_results=[], required_field=True, current_query=False, recommend={}, total_results=None)
    else:
        # Submit query and receive results
        (results['field_results'], results['field_recommend']) = field_query(request.form)
        query['total_results'] = len(results['field_results'])
        query['current'] = [i for i in [title, publisher, authors, isbn, description] if i]
        results['text_results'] = []
        return redirect(url_for('home_result'))

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=5000,debug=True)