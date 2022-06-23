from typing import Literal
from ws.kis.types import UrlType
import dotenv
from ws.config.parser import dotenv_parser as dp

class AddressBuilder:
    @staticmethod
    def get_address(urlType:Literal) -> str:
        # print( dp.get_env('KIS_DOMAIN')+ ':' + dp.get_env('KIS_PORT')+ dp.get_env(urlType.value[0]))
        return dp.get_env('KIS_DOMAIN') + ':' + dp.get_env('KIS_PORT') + dp.get_env(urlType.value[0])
    
    @staticmethod
    def get_virtual_address(urlType:Literal) -> str:
        print(dp.get_env('KIS_VIRTUAL_DOMAIN') + ':' + dp.get_env('KIS_VIRTUAL_PORT') + dp.get_env(urlType.value[0]))
        return dp.get_env('KIS_VIRTUAL_DOMAIN') + ':' + dp.get_env('KIS_VIRTUAL_PORT') + dp.get_env(urlType.value[0])


        
    
    
        