import asyncio
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

# ws client test - 단일 종목 콘솔 모드
# import asyncio 
# from ws.handler.ws_client import *
# try:
#     asyncio.get_event_loop().run_until_complete(connect())
#     asyncio.get_event_loop().close()    
# except KeyboardInterrupt as e:
#     print(e)

# ws client test - 다중 종목 실시세
# from ws.handler import multistocks_realprice
# multistocks_realprice.run_ws()

# ws client test - 단일 종목 실시세 excel
from ws.handler import ws_realstkprice

# ws client test - 단일 종목 호가창 excel
from ws.handler import ws_realstkquote

async def test_ws_realdata():
    await asyncio.gather(
        asyncio.to_thread( ws_realstkprice.run_ws ),
        asyncio.to_thread( ws_realstkquote.run_ws )
    )
    # print('test 종료:',test_list)

asyncio.run(test_ws_realdata())
