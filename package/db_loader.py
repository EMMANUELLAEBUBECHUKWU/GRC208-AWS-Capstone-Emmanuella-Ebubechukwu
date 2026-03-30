import json
import boto3
import pymysql

def lambda_handler(event, context):
    try:
        conn = pymysql.connect(
            host='grc-capstone-db.cnok20k42m82.us-east-1.rds.amazonaws.com',
            user='grcadmin',
            password='GrcPass2026!',
            db='grcdb',
            connect_timeout=30
        )
        cursor = conn.cursor()
        
        with open('sample_data.sql', 'r') as f:
            sql_content = f.read()
        
        statements = [s.strip() for s in sql_content.split(';') if s.strip()]
        
        executed = 0
        errors = []
        for statement in statements:
            try:
                cursor.execute(statement)
                executed += 1
            except Exception as e:
                errors.append(str(e))
        
        conn.commit()
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Database loaded successfully',
                'executed': executed,
                'errors': errors[:5]
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
