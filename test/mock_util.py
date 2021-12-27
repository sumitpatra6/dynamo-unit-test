class MockDynamo:
    def Table(self, table_name):
        pass


class BaseMockTable:
    def __init__(self, table_name):
        pass


class MockUserTable(BaseMockTable):
    def query(self, KeyConditionExpression=None):
        return {
            'Items': [{'id': '56b72315513547d688849c2a858ef9cd',
                       'name': 'Sweta'}]

        }
