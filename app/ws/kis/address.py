from typing import Literal
from ws.kis.types import UrlType
import dotenv
from ws.config.parser import dotenv_parser as dp

class AddressBuilder:
    @staticmethod
    def get_address(urlType:Literal) -> str:
        # print( dp.get_env('KIS_DOMAIN')+ ':' + dp.get_env('KIS_PORT')+ dp.get_env(urlType.value[0]))
        return dp.get_env('KIS_DOMAIN') + ':' + dp.get_env('KIS_PORT') + urlType.value
    
    @staticmethod
    def get_virtual_address(urlType:Literal) -> str:
        # print(dp.get_env('KIS_VIRTUAL_DOMAIN') + ':' + dp.get_env('KIS_VIRTUAL_PORT') + urlType.value)
        return dp.get_env('KIS_VIRTUAL_DOMAIN') + ':' + dp.get_env('KIS_VIRTUAL_PORT') + urlType.value

    @staticmethod
    def get_ws_address() -> str:
        # print( dp.get_env('KIS_DOMAIN')+ ':' + dp.get_env('KIS_PORT')+ dp.get_env(urlType.value[0]))
        return dp.get_env('KIS_WS_DOMAIN') + ':' + dp.get_env('KIS_WS_PORT')

    @staticmethod
    def get_ws_virtual_address() -> str:
        # print( dp.get_env('KIS_DOMAIN')+ ':' + dp.get_env('KIS_PORT')+ dp.get_env(urlType.value[0]))
        return dp.get_env('KIS_WS_VIRTUAL_DOMAIN') + ':' + dp.get_env('KIS_WS_VIRTUAL_PORT')




        
    
    
        