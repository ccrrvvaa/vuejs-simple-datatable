import os
import json
import math
from flask import Flask, request, render_template, jsonify

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/list", methods=["GET"])
def list():
    response = {
        'data': [],
        'pages': 1,
        'page': 1
    }

    search = request.args.get('search', '')
    sort_by = request.args.get("sort_by", '')
    sort_order = request.args.get("sort", '')
    page = request.args.get("page", '')

    filename = os.path.join(app.static_folder, 'data/es.1.clubs.json')
    with open(filename, 'r') as my_file:
        data = json.loads(my_file.read())
        params = {
            "search": search,
            "sort_by": sort_by,
            "sort_order": sort_order,
            "page": page
        }

        response = search_clubs(data['clubs'], params)

    return jsonify(response)

def search_clubs(items, params):
    data = []
    for item in items:
        if params['search']:
            if params['search'].lower() in item['name'].lower():
                data.append(item)
        else:
            data.append(item)

    if params['sort_by'] and params['sort_order']:
        if params['sort_by'] in ['key', 'code', 'name'] and params['sort_order'] in ['asc', 'desc']:
            reverse = False
            if params['sort_order'] == 'desc':
                reverse = True

            data.sort(key=lambda r: (r[params['sort_by']] is None, r[params['sort_by']] == "", r[params['sort_by']]), reverse=reverse)

    offset = 0
    per_page = 10
    if params['page']:
        offset = (int(params['page']) - 1) * per_page

    limit = offset + per_page
    count = math.ceil(len(data) / per_page)
    print(len(data))
    response = {
        'data': data[offset:limit],
        'pages': count,
        'page': params['page']
    }

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
