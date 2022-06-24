from fastapi import APIRouter
from ws.handler.rest import StockHandler
import json


router = APIRouter()


'''/ws/test-stock-marketprice'''
@router.get('/test-stock-marketprice')
async def get_stock_marketprice():
    return json.loads(StockHandler.test_get_marketprice('J', '005930'))

'''/ws/test-stock-executions'''
@router.get('/test-stock-executions')
async def get_stock_executions():
    return json.loads(StockHandler.test_get_executions('J', '005930'))

'''/ws/test-stock-price-by-date'''
@router.get('/test-stock-price-by-date')
async def get_stock_by_date():
    return json.loads(StockHandler.test_get_price_by_data('J', '005930'))

'''/ws/test-stock-asking-price'''
@router.get('/test-stock-asking-price')
async def get_stock_asking_price_expected_executions():
    return json.loads(StockHandler.test_get_asking_price_excepted_executions('J', '005930'))

'''/ws/test-elw-marketprice'''
@router.get('/test-elw-marketprice')
async def get_elw_marketprice():
    return json.loads(StockHandler.test_get_elw_marketprice('W', '57HB90'))

'''/ws/test-stock-price-by-period'''
@router.get('/test-stock-price-by-period')
async def get_stock_price_by_period():
    return json.loads(StockHandler.test_get_stock_price_by_period('J', '005930', 'D')) # D: 일봉, W:주봉, M: 월봉, Y: 년봉


