import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://lutericosmosdb:P4pvBHNfSK4U35hFF9nkbCM1qMINWgzO5a690N5WsfZMfimQO2vvZNW5EgIqiowybZZsxb7WjT0nnPNLrofi3A==@lutericosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lutericosmosdb@" # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['luteridb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

