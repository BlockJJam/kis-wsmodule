#웹소켓 실시간 WEBSOCKET 주식현재가_실시간주식호가[실시간-004] 엑셀연동 샘플
#Method : POST
#실전 Domain : https://openapi.koreainvestment.com:9443
#모의 Domain : https://openapivts.koreainvestment.com:29443
#URL: /tryitout/H0STCNT0
#Content-Type : text/plain
#엑셀파일 실시간.xlsx 띄우고 프로그램 실행하세요
import os
import json
import pandas as pd
import xlwings as xw
import websocket
from ws.config.parser import dotenv_parser

appkey = dotenv_parser.get_env('MY_APPKEY')
seckey = dotenv_parser.get_env('MY_SECKEY')

h = {
    "appkey": appkey,
    "appsecret": seckey
}
b = {
    "header": {
        "appkey": appkey,
        "appsecret": seckey,
        "custtype": "P",
        "tr_type": "1",
        "content-type": "utf-8"
    },
    "body":
        {
            "input": {
                "tr_id": "H0STCNT0", #API명
                "tr_key": "005930"   #종목번호
            }
    }
}

wb = xw.Book('실시간1.xlsx')
wsheet = wb.sheets[0]

# Pandas DataFrame 이용
def pdbind(result):

    df = pd.DataFrame([
        ['유가증권 단축 종목코드', result[0]],
        ['주식 체결 시간', result[1]],
        ['주식 현재가', result[2]],
        ['전일 대비 부호', result[3]],
        ['전일 대비', result[4]],
        ['전일 대비율', result[5]],
        ['가중 평균 주식 가격', result[6]],
        ['주식 시가', result[7]],
        ['주식 최고가', result[8]],
        ['주식 최저가', result[9]],
        ['매도호가1', result[10]],
        ['매수호가1', result[11]],
        ['체결 거래량', result[12]],
        ['누적 거래량', result[13]],
        ['누적 거래 대금', result[14]],
        ['매도 체결 건수', result[15]],
        ['매수 체결 건수', result[16]],
        ['순매수 체결 건수', result[17]],
        ['체결강도', result[18]],
        ['총 매도 수량', result[19]],
        ['총 매수 수량', result[20]],
        ['체결구분', result[21]],
        ['매수비율', result[22]],
        ['전일 거래량 대비 등락율', result[23]],
        ['시가 시간', result[24]],
        ['시가대비구분', result[25]],
        ['시가대비', result[26]],
        ['최고가 시간', result[27]],
        ['고가대비구분', result[28]],
        ['고가대비', result[29]],
        ['최저가 시간', result[30]],
        ['저가대비구분', result[31]],
        ['저가대비', result[32]],
        ['영업 일자', result[33]],
        ['신 장운영 구분 코드', result[34]],
        ['거래정지 여부', result[35]],
        ['매도호가 잔량1', result[36]],
        ['매수호가 잔량1', result[37]],
        ['총 매도호가 잔량', result[38]],
        ['총 매수호가 잔량', result[39]],
        ['거래량 회전율', result[40]],
        ['전일 동시간 누적 거래량', result[41]],
        ['전일 동시간 누적 거래량 비율', result[42]],
        ['시간 구분 코드', result[43]],
        ['임의종료구분코드', result[44]],
        ['정적VI발동기준가', result[45]]
    ]
    )

    wsheet.range('A1').value = df

def on_message(ws, data):
    #print('type=', type(data), '\ndata=', data)

    if data[0] in ['0', '1']:  # 시세데이터가 아닌경우
        d1 = data.split("|")
        if len(d1) >= 4:
            isEncrypt = d1[0]
            tr_id = d1[1]
            tr_cnt = d1[2]
            recvData = d1[3]
            result = recvData.split("^")
            #print("start time=", result[1])
            pdbind(result)  # pandas dataframe 이용 변경


        else:
            print('Data Size Error=', len(d1))
    else:
        recv_dic = json.loads(data)
        tr_id = recv_dic['header']['tr_id']
        # xls 바인딩
        wsheet.range('A4').value = tr_id

        if tr_id == 'PINGPONG':
            send_ping = recv_dic
            ws.send(data, websocket.ABNF.OPCODE_PING)
        else:  # parser data
            print('tr_id=', tr_id, '\nmsg=', data)


def on_error(ws, error):
    print('error=', error)


def on_close(ws, status_code, close_msg):
    print('on_close close_status_code=', status_code, " close_msg=", close_msg)


def on_open(ws):
    print('on_open send data=', json.dumps(b))
    ws.send(json.dumps(b), websocket.ABNF.OPCODE_TEXT)


# websocket.enableTrace(True)

ws = websocket.WebSocketApp("ws://ops.koreainvestment.com:21000/tryitout/H0STCNT0",
                            on_open=on_open, on_message=on_message, on_error=on_error)

def run_ws():
    ws.run_forever()