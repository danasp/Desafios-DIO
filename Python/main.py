import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://danasp:210989@cluster0.wjfgx56.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.aula

albuns = db.albuns.find()

file = open("/Users/danielsouza/Documents/albuns.txt", "a")

for item in albuns:
    nome = item["nome"]
    file.write(nome + '\n')

file.close()
