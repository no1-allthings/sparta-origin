from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.uebefva.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']

all = list(db.movies.find({'star':star},{'_id':False}))
for m in all:
    print(m['title'])