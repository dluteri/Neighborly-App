import json
import logging

import azure.functions as func


# def main(event: func.EventGridEvent):
#     result = json.dumps({
#         'id': event.id,
#         'data': event.get_json(),
#         'topic': event.topic,
#         'subject': event.subject,
#         'event_type': event.event_type,
#     })

#     logging.info('Python EventGrid trigger processed an event: %s', result)

import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Sending message from my Azure Functions HTTP Trigger"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "luterifake@gmail.com"
            }]}],
        "subject": "[AZURE FUNCTIONS SENDGRID] email",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    return func.HttpResponse("Message successfully sent.")