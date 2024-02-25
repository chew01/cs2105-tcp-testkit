from enum import Enum

from pydantic import BaseModel

class MethodEnum(str, Enum):
    post = 'POST'
    get = 'GET'
    delete = 'DELETE'

class DestEnum(str, Enum):
    key = '/key/'
    counter = '/counter/'

class Query(BaseModel):
    method: MethodEnum
    dest: DestEnum
    path: str
    content: str = ""
    force_content_length: bool = False

    def to_bytes(self) -> bytes:
        content_length = len(self.content)
        if content_length > 0 or self.force_content_length:
            string = f"{self.method.value} {self.dest.value}{self.path} Content-Length {content_length}  {self.content}"
        else:
            string = f"{self.method.value} {self.dest.value}{self.path}  {self.content}"
        return string.encode()