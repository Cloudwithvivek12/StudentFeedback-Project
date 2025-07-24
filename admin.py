#!/usr/bin/env python3

import boto3
import cgi

print("Content-Type: text/html\n")

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')  # ✅ apni region daalo
table = dynamodb.Table('CloudWithVivekFeedback')

# Fetch all records
response = table.scan()
items = response.get('Items', [])

# HTML output
print("""
<html>
<head>
    <title>Admin Dashboard - Feedbacks</title>
    <style>
        table { border-collapse: collapse; width: 80%; margin: 20px auto; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        h2 { text-align: center; }
    </style>
</head>
<body>
<h2>Feedback Dashboard - CloudWithVivek</h2>
<table>
<tr><th>Name</th><th>Course</th><th>Feedback</th><th>ID</th></tr>
""")

for item in items:
    print(f"<tr><td>{item.get('name')}</td><td>{item.get('course')}</td><td>{item.get('feedback')}</td><td>{item.get('id')}</td></tr>")

print("""
</table>
</body>
</html>
""")
