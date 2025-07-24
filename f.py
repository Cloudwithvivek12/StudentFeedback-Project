#!/usr/bin/env python3

import cgi
import boto3
import uuid

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
name = form.getvalue("name")
course = form.getvalue("course")
feedback = form.getvalue("feedback")

try:
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')  # example: 'us-east-1'
    table = dynamodb.Table('CloudWithVivekFeedback')

    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'name': name,
        'course': course,
        'feedback': feedback
    })

    print("<h2>Thank you for your feedback!</h2>")

except Exception as e:
    print("<h2>Error occurred:</h2>")
    print(f"<pre>{str(e)}</pre>")