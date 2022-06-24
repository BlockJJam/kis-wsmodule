
from ws.kis.types import UrlType
from ws.kis.address import AddressBuilder
import httpx
from httpx import Response
from logger.config import logger

class AuthHandler():
    basic_headers= {
        'content-type': 'application/json; charset=utf-8',
        'appkey' : 'PS6CscEq1d10XrDcIIfxSMsq1g25SEFh1Far',
        'appsecret' :'P4R8zN5rQFGdnNoTp8YVqmBTJDHHxs1cA/sXHj5ykQKRIWYl1GYy9Oi0AAIvzpjkVcYkvDmAQgYs7s0cjKQyJcf+r/w9PjNmAr2VC+d6nsmsMl55uZ+9HxIi2JYe68F9sFGsFbw069nmr5OnUjzIC+7yHfEhwlH5eKwloFgTDfHpRBocWzA='
    }

    @classmethod
    def test_hashkey_request(self):
        headers = self.basic_headers

        data={
            'CANO':'50067192'
        }
        response:Response = httpx.post(AddressBuilder.get_virtual_address(UrlType.HASHKEY),headers=headers, json=data)
        logger.debug(f'\n[status code] >>> {response.status_code} \n\n[response header] >>> {response.headers}\n\n[response data] >>> {response.json()}\n')
        
    @classmethod
    def test_get_access_token(self):
        headers = self.basic_headers
        
        data = {
            'grant_type': 'client_credentials',
            'appkey' : 'PS6CscEq1d10XrDcIIfxSMsq1g25SEFh1Far',
            'appsecret' :'P4R8zN5rQFGdnNoTp8YVqmBTJDHHxs1cA/sXHj5ykQKRIWYl1GYy9Oi0AAIvzpjkVcYkvDmAQgYs7s0cjKQyJcf+r/w9PjNmAr2VC+d6nsmsMl55uZ+9HxIi2JYe68F9sFGsFbw069nmr5OnUjzIC+7yHfEhwlH5eKwloFgTDfHpRBocWzA='
        }

        response:Response = httpx.post(AddressBuilder.get_virtual_address(UrlType.ACCESSKEY), headers = headers, json=data)
        logger.debug(f'\n[status code] >>> {response.status_code} \n\n[response header] >>> {response.headers}\n\n[response data] >>> {response.json()}\n')

        
class StockHandler():
    '''
    appkey, appsecret: 이 두가지는 개인 정보로
    authorization: access token 값으로 채워야 함 <- AuthHandler.test_get_access_token()
    '''
    basic_headers = {
        'content-type': 'application/json; charset=utf-8',
        'appkey' : 'PS6CscEq1d10XrDcIIfxSMsq1g25SEFh1Far',
        'appsecret' :'P4R8zN5rQFGdnNoTp8YVqmBTJDHHxs1cA/sXHj5ykQKRIWYl1GYy9Oi0AAIvzpjkVcYkvDmAQgYs7s0cjKQyJcf+r/w9PjNmAr2VC+d6nsmsMl55uZ+9HxIi2JYe68F9sFGsFbw069nmr5OnUjzIC+7yHfEhwlH5eKwloFgTDfHpRBocWzA=',
        'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6Ijk2ZWIyODBkLWZhMGYtNGRjOC05ZDBjLWY4MzgwZWFkYzM5YiIsImlzcyI6InVub2d3IiwiZXhwIjoxNjU2MTE3ODI1LCJpYXQiOjE2NTYwMzE0MjUsImp0aSI6IlBTNkNzY0VxMWQxMFhyRGNJSWZ4U01zcTFnMjVTRUZoMUZhciJ9.3hL8UH9zCd6WMoK-3JgxIu0FHa1D44DbKHG6McMrhqm_o1CJNOBuuKEPGwQUt3KlhkBWH-ts6Khj_4MEDvuv-g'
    }

    @classmethod
    def test_get_marketprice(self, type: str, code: str) -> str:
        headers = self.basic_headers
        headers['tr_id'] = 'FHKST01010100'
        data = {
            'FID_COND_MRKT_DIV_CODE' : type,
            'FID_INPUT_ISCD' : code
        }

        response:Response = httpx.get(AddressBuilder.get_virtual_address(UrlType.STOCK_MARKETPRICE), headers = headers, params = data)
        # logger.debug(f'\n[status code] >>> {response.status_code} \n\n[response header] >>> {response.headers}\n\n[response data] >>> {response.json()}\n')
        logger.debug(f'{response.text}')
        
        return response.text

    @classmethod
    def test_get_executions(self, type: str, code: str) -> str:
        headers = self.basic_headers
        headers['tr_id'] = 'FHKST01010300'
        data = {
            'FID_COND_MRKT_DIV_CODE' : type,
            'FID_INPUT_ISCD' : code
        }

        response:Response = httpx.get(AddressBuilder.get_virtual_address(UrlType.STOCK_EXECUTIONS), headers = headers, params = data)
        logger.debug(f'{response.text}')

        return response.text

    @classmethod
    def test_get_price_by_data(self, type: str, code: str) -> str:
        headers = self.basic_headers
        headers['tr_id'] = 'FHKST01010400'
        data = {
            'FID_COND_MRKT_DIV_CODE' : type,
            'FID_INPUT_ISCD' : code,
            'FID_PERIOD_DIV_CODE' : 'D', # D: 최근30거래일, W: 30주, M: 30개월
            'FID_ORG_ADJ_PRC' : '0', # 0: 수정주가 반영, 1: 미반영
        }

        response:Response = httpx.get(AddressBuilder.get_virtual_address(UrlType.STOCK_EXECUTIONS), headers = headers, params = data)
        logger.debug(f'{response.text}')

        return response.text

    @classmethod
    def test_get_asking_price_excepted_executions(self, type: str, code: str) -> str:
        headers = self.basic_headers
        headers['tr_id'] = 'FHKST01010200'
        data = {
            'FID_COND_MRKT_DIV_CODE' : type,
            'FID_INPUT_ISCD' : code
        }

        response:Response = httpx.get(AddressBuilder.get_virtual_address(UrlType.STOCK_EXECUTIONS), headers = headers, params = data)
        logger.debug(f'{response.text}')

        return response.text

        
    @classmethod
    def test_get_elw_marketprice(self, type: str, code: str) -> str:
        headers = self.basic_headers
        headers['tr_id'] = 'FHKEW15010000' # elw용
        data = {
            'FID_COND_MRKT_DIV_CODE' : type,
            'FID_INPUT_ISCD' : code
        }

        response:Response = httpx.get(AddressBuilder.get_virtual_address(UrlType.ELK_MARKETPRICE), headers = headers, params = data)
        logger.debug(f'{response.text}')

        return response.text

    @classmethod
    def test_get_stock_price_by_period(self, type: str, code: str, div_code: str) -> str:
        '''
        제한 사항
        - 데이터 100개가 제한(이어서 못 가져옴) 즉, 시작 일자 ~ 종료 일자를 지정해서 100개씩 끊어서 가져오던지 해야함
        - 분봉 없음
        '''
        headers = self.basic_headers
        headers['tr_id'] = 'FHKST03010100' # 실전투자용, 모의투자 제공안됨!
        headers['custtype'] = 'P'

        data = {
            'FID_COND_MRKT_DIV_CODE' : type,
            'FID_INPUT_ISCD' : code,
            'FID_INPUT_DATE_1' : '20200501',
            'FID_INPUT_DATE_2' : '20220501',
            'FID_PERIOD_DIV_CODE' : div_code,
            'FID_ORG_ADJ_PRC': '0' #0: 수정주가, 1: 원주가
        }

        response:Response = httpx.get(AddressBuilder.get_virtual_address(UrlType.ELK_MARKETPRICE), headers = headers, params = data)
        logger.debug(f'{response.text}')

        return response.text
        

    
        
        




        
        
