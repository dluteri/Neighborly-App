import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://lutericosmosdb1:C0JmDhDGvQ7TJqshlGgFODtQfHVpIBQzdn6UhN9qYPX8GQlVAoXZL0Hz2SzJL5AKRvZHHYfy09m0kothz45Vfw==@lutericosmosdb1.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lutericosmosdb1@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['luteridb']
            collection = database['posts']

            query = {'_id': str(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)