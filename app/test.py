from turtle import dot
from ws.kis.types import UrlType
from ws.config.parser import dotenv_parser
from ws.kis.address import AddressBuilder
from ws.handler.rest import AuthHandler, StockHandler

# env test
# print(dotenv_parser.get_env('URL'))

# Custom Http Address test
# print(AddressBuilder.get_address(UrlType.ACCESSKEY))
# print(AddressBuilder.get_virtual_address(UrlType.HASHKEY))

# KIS의 Hashkey API 테스트
# auth = AuthHandler()
# auth.test_hashkey_request()
# auth.test_get_access_token()

# stock = StockHandler()
# stock.test_get_marketprice()


import asyncio 
from ws.handler.ws_client import *
try:
    asyncio.get_event_loop().run_until_complete(connect())
    asyncio.get_event_loop().close()    
except KeyboardInterrupt as e:
    print(e)


