import dataclasses
import os
from typing import List
from typing import Optional

import boto3
from tqdm import tqdm

os.environ["AWS_DEFAULT_REGION"] = "ap-northeast-1"


@dataclasses.dataclass
class DynamoDBClient:
    table_name: str

    def __post_init__(self) -> None:
        self.table = boto3.resource("dynamodb").Table(self.table_name)

    def get_item(self, key_name: str, key_value: str) -> Optional[dict]:
        try:
            response = self.table.get_item(Key={key_name: key_value})
        except Exception as e:
            print(e)
        else:
            return response

    def put_item(self, item: dict) -> None:
        return self.table.put_item(Item=item)

    def batch_writer(self, items: List[dict]) -> None:
        max_count = len(items)
        with self.table.batch_writer() as batch:
            for item in tqdm(items, desc=f"insert {self.table_name}"):
                try:
                    batch.put_item(Item=item)
                except ValidationException as e:
                    print(f"error[{item['id']}], reason[{e}]")

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
