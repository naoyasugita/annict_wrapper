import boto3


class DynamoDBClient:
    table_name: str
    table = boto3.resource("dynamodb").Table(self.table_name())

    def get_item(self, key_name: str, key_value: str) -> Optional[dict]:
        try:
            response = self.table.get_item(Key={key_name: key_value})
        except ClientError as e:
            raise (e.response["Error"]["Message"])
        else:
            # return default_proc(response)
            return response

    def put_item(self, item: dict) -> None:
        return self.table.put_item(Item=item)

    def batch_weiter(self, items: List[dict]) -> None:
        with dynamo_table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

    def delete_item(self, key_name: str, key_value: str) -> None:
        self.table.delete_item(Key={key_name: key_value})

    def default_proc(obj) -> object:
        if isinstance(obj, Decimal):
            if int(obj) == obj:
                return int(obj)
            else:
                return float(obj)
        elif isinstance(obj, Binary):
            return obj.value
        elif isinstance(obj, bytes):
            return obj.decode(encoding="default")
        elif isinstance(obj, set):
            return list(obj)
        try:
            return str(obj)
        except Exception:
            return None
