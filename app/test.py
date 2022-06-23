from turtle import dot
from ws.kis.types import UrlType
from ws.config.parser import dotenv_parser
from ws.kis.address import AddressBuilder
from ws.handler.rest import AuthHandler

# env test
# print(dotenv_parser.get_env('URL'))

# Custom Http Address test
# print(AddressBuilder.get_address(UrlType.ACCESSKEY))
# print(AddressBuilder.get_virtual_address(UrlType.HASHKEY))

# KIS의 Hashkey API 테스트
auth = AuthHandler()
auth.test_hashkey_request()