import boto3
import json

def lambda_handler(event, context):
    import pymysql
    import os
    
    conn = pymysql.connect(
        host='grc-capstone-db.cnok20k42m82.us-east-1.rds.amazonaws.com',
        user='grcadmin',
        password='GrcPass2026!',
        database='grcdb'
    )
    
    return {"statusCode": 200, "body": "Data loaded successfully"}
