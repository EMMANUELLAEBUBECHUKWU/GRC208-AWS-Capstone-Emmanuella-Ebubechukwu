import boto3
import json
import pymysql
import os

def lambda_handler(event, context):
    conn = pymysql.connect(
        host=event['host'],
        user=event['user'],
        password=event['password'],
        db=event['db']
    )
    cursor = conn.cursor()
    with open('sample_data.sql', 'r') as f:
        sql = f.read()
    for statement in sql.split(';'):
        if statement.strip():
            cursor.execute(statement)
    conn.commit()
    conn.close()
    return {'statusCode': 200, 'body': 'Data loaded successfully'}
