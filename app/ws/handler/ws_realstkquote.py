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
                "tr_id": "H0STASP0",
                "tr_key": "005930"
            }
    }
}

wb = xw.Book('실시간2.xlsx')
wsheet = wb.sheets[0]

# Pandas DataFrame 이용
def pdbind(result):

    df = pd.DataFrame([
        ['', result[1], ''],
        [result[32], result[12], ''],
        [result[31], result[11], ''],
        [result[30], result[10], ''],
        [result[29], result[9], ''],
        [result[28], result[8], ''],
        [result[27], result[7], ''],
        [result[26], result[6], ''],
        [result[25], result[5], ''],
        [result[24], result[4], ''],
        [result[23], result[3], ''],
        ['', result[13], result[33]],
        ['', result[14], result[34]],
        ['', result[15], result[35]],
        ['', result[16], result[36]],
        ['', result[17], result[37]],
        ['', result[18], result[38]],
        ['', result[19], result[39]],
        ['', result[20], result[40]],
        ['', result[21], result[41]],
        ['', result[22], result[42]],
        [result[43], '', result[44]]  # 총매도호가, 총매수호가
    ]
    )
    wsheet.range('A4').value = df

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
            # xlsvalue(result)

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

ws = websocket.WebSocketApp("ws://ops.koreainvestment.com:31000/tryitout/H0STCNT0",
                            on_open=on_open, on_message=on_message, on_error=on_error)

def run_ws():
    ws.run_forever()