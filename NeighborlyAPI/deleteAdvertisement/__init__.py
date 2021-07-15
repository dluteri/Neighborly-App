import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://lutericosmosdb:9O1xVMVgvREXVTYinyiuRwntynyDz0kAH1FWh9m0l9uPI3joyuYpAjsxT0u7C6N95i6dVZKzUnIFaB9qET11xQ==@lutericosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lutericosmosdb@"
            client = pymongo.MongoClient(url)
            database = client['luteridb']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
