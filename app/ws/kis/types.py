from enum import Enum

class UrlType(Enum):
    HASHKEY='/uapi/hashkey'
    ACCESSKEY='/oauth2/tokenP'
    ACCESSKEY_REMOVE='/oauth2/revokeP'
    STOCK_MARKETPRICE='/uapi/domestic-stock/v1/quotations/inquire-price'
    STOCK_EXECUTIONS='/uapi/domestic-stock/v1/quotations/inquire-ccnl'
    STOCK_BY_DATE='/uapi/domestic-stock/v1/quotations/inquire-daily-price'
    STOCK_ASKING_PRICE_EXPECTED_EXECUTIONS='/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn'
    ELK_MARKETPRICE='/uapi/domestic-stock/v1/quotations/inquire-elw-price'

