from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.legal_analyzer
docs = db.documents

def save_doc(content, summary, clauses):
    return docs.insert_one({
        "content": content,
        "summary": summary,
        "clauses": clauses
    })

def get_all_docs():
    return list(docs.find())
