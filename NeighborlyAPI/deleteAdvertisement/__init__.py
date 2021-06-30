import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://lutericosmosdb:sX5FlaMo4NsW3k8dP32EJWGeb8MMCw4JKmJFKm9TIyih4Yf5PApFVVe7U20XxN1x2C22P943JPv0PGgqzwyZ5g==@lutericosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lutericosmosdb@" # TODO: Update with appropriate MongoDB connection information
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
