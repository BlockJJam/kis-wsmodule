
from ws.kis.types import UrlType
from ws.kis.address import AddressBuilder
import httpx
from httpx import Response

class AuthHandler():
    @classmethod
    def test_hashkey_request(cls):
        headers= {
            'content-type': 'application/json; charset=utf-8',
            'appkey' : 'PS6CscEq1d10XrDcIIfxSMsq1g25SEFh1Far',
            'appsecret' :'P4R8zN5rQFGdnNoTp8YVqmBTJDHHxs1cA/sXHj5ykQKRIWYl1GYy9Oi0AAIvzpjkVcYkvDmAQgYs7s0cjKQyJcf+r/w9PjNmAr2VC+d6nsmsMl55uZ+9HxIi2JYe68F9sFGsFbw069nmr5OnUjzIC+7yHfEhwlH5eKwloFgTDfHpRBocWzA='
        }

        data={
            'CANO':'50067192'
        }
        response:Response = httpx.post(AddressBuilder.get_virtual_address(UrlType.HASHKEY),headers=headers, json=data);
        print(response.status_code)
        print(response.headers)
        print(response.json())
        
