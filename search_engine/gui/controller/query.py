import json
import os
from search_engine.inverted_index import *
from search_engine.query import get_Query_Index_Rank, get_Query_Rank
from .mutual_info import *
import tldextract
from urllib.parse import urlparse

CURR_FILE_DIR = os.path.dirname(os.path.realpath(__file__))

query_response_mock = {
    13: 0.9,
    5000: 0.1321,
    3200: 0.02
}

def get_val_field_pairs(field, value):
    return [f'{val}.{field}' for val in tokenize_text(value)]

docname_docid_map = {}
with open(os.path.join(CURR_FILE_DIR, '..', '..', '..', 'data', 'inverted-index', 'docIDs.json'), 'r', encoding='utf-8') as file:
    docname_docid_map = json.load(file)
def get_docid_name(docid):
    return list(docname_docid_map.keys())[list(docname_docid_map.values()).index(docid)]

docname_docurl_map = {}
with open(os.path.join(CURR_FILE_DIR, '..', 'static', 'data', 'doc_name_to_url.json'), 'r', encoding='utf-8') as file:
    docname_docurl_map = json.load(file)
def get_docname_url(docname):
    return docname_docurl_map[docname]

def get_docmetadata(docname):
    base_path = os.path.join(CURR_FILE_DIR, '..', '..', '..', 'data', 'wrapped')
    ends_with = '.html.json'
    filename = f"{docname}{ends_with}"
    path_list = [os.path.join(root, filename) for root, _, files in os.walk(base_path) if filename in files]
    docmetadata_path = path_list.pop()
    with open(docmetadata_path, encoding='utf-8') as file:
        return json.load(file)

def field_query(input):
    query = []
    fields = []
    # Generate value.field strings from input
    for (field, value) in input.items():
        if value:
            query += get_val_field_pairs(field, value)
            fields += [field]
    # Get top K terms with largest mutual information for each input field
    top_k_mutualinfo = {}
    for field in list(set(fields)): # Iterate over input present fields
        field_values = list(set(filter(lambda t: t.split('.')[1] == field, query))) # List all unique values
        top_k_mutualinfo[field] = get_top_k_mutualinfo(field_values, field)
    return search(query, field=True), top_k_mutualinfo

def text_query(input):
    query = list(filter(lambda t: t, tokenize_text(input)))
    return search(query, field=False)

def search(query, field):
    if query:
        docid_score_result = get_Query_Index_Rank(query) if field else get_Query_Rank(query)
        results = []
        for docid, score in docid_score_result.items():
            docname = get_docid_name(docid)
            docurl = get_docname_url(docname)
            docmetadata = get_docmetadata(docname)
            docmetadata['url'] = docurl
            docmetadata['domain'] = get_url_domain(docurl)
            results.append(docmetadata)
        return results
    return []

def get_url_netloc(url):
        try:
            return urlparse(url).netloc
        except Exception:
            return None

def get_url_domain(url):
    try:
        url_netloc = get_url_netloc(url)
        return tldextract.extract(url_netloc).domain
    except Exception:
        return None