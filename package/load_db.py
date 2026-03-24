import json
import boto3
import pymysql

DB_HOST = 'grc-capstone-db.cnok20k42m82.us-east-1.rds.amazonaws.com'
DB_USER = 'grcadmin'
DB_PASS = 'GrcPass2026!'
DB_NAME = 'grcdb'

def lambda_handler(event, context):
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            connect_timeout=10
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        conn.close()
        return {
            "statusCode": 200,
            "body": json.dumps({"tables": [t[0] for t in tables]})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
