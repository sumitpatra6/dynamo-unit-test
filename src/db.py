import boto3
from boto3.dynamodb.conditions import Key
from pprint import pprint
class DB:
    def __init__(self) -> None:
        self.dynamo = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    

    def save_date(self, rows):
        table = self.dynamo.Table("User")
        with table.batch_writer() as writer:
            for item in rows:
                writer.put_item(Item=item)

    def get_items(self):
        table = self.dynamo.Table('User')
        data = table.scan()
        pprint(data)

    def query(self, id):
        table = self.dynamo.Table('User')
        data = table.query(KeyConditionExpression=Key("id").eq(id))
        pprint(data['Items'])
        return data['Items']