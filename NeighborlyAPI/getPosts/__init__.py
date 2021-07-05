import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://lutericosmosdb1:C0JmDhDGvQ7TJqshlGgFODtQfHVpIBQzdn6UhN9qYPX8GQlVAoXZL0Hz2SzJL5AKRvZHHYfy09m0kothz45Vfw==@lutericosmosdb1.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lutericosmosdb1@"   # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['luteridb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)