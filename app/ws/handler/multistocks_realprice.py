import os
import json
import pandas as pd
import websocket
from ws.config.parser import dotenv_parser

i_stock = ["005930","011700","000270"]
i_appkey    = dotenv_parser.get_env('MY_APPKEY')
i_appsecret = dotenv_parser.get_env('MY_SECKEY')

b = {
    "header": {"appkey": i_appkey, "appsecret": i_appkey, "custtype": "P", "tr_type": "1", "content-type": "utf-8"},
    "body": { "input": {"tr_id": "H0STCNT0",  # API명
                        "tr_key": i_stock[0]  # 종목번호
                       }
            }
}
b2 = {
    "header": {"appkey": i_appkey, "appsecret": i_appkey, "custtype": "P", "tr_type": "1", "content-type": "utf-8"},
    "body": { "input": {"tr_id": "H0STCNT0",  # API명
                        "tr_key": i_stock[1]  # 종목번호
                       }
            }
}
b3 = {
    "header": {"appkey": i_appkey, "appsecret": i_appkey, "custtype": "P", "tr_type": "1", "content-type": "utf-8"},
    "body": { "input": {"tr_id": "H0STCNT0",  # API명
                        "tr_key": i_stock[2]  # 종목번호
                       }
            }
}

# Pandas DataFrame 이용
def pdbind(result):

     if i_stock[0] == result[0]:
        print("종목코드1:",result[0], " 체결시간:", result[1], " 현재가:", result[2])
     if i_stock[1] == result[0]:
        print("종목코드2:",result[0], " 체결시간:", result[1], " 현재가:", result[2])
     if i_stock[2] == result[0]:
        print("종목코드3:",result[0], " 체결시간:", result[1], " 현재가:", result[2])

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
    ws.send(json.dumps(b), websocket.ABNF.OPCODE_TEXT) #종목코드 1
    ws.send(json.dumps(b2), websocket.ABNF.OPCODE_TEXT) #종목코드 2
    ws.send(json.dumps(b3), websocket.ABNF.OPCODE_TEXT)  # 종목코드 3

ws = websocket.WebSocketApp("ws://ops.koreainvestment.com:21000/tryitout/H0STCNT0",
                            on_open=on_open, on_message=on_message, on_error=on_error)

def run_ws():
    ws.run_forever()