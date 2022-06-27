import dotenv
import websockets
import json
import os
import asyncio
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

key_bytes = 32

# AES256 Decode
def aes_cbc_base64_dec(key: str, iv: str, cipher_text: str):
    '''
    :param key: AES256 secret key value
    :param iv: AES256 Initialize Vector
    :param cipher_text: Base64
    :return: Base64-AES256 decodec
    '''
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    return bytes.decode(unpad(cipher.decrypt(b64decode(cipher_text)), AES.block_size))

# 주식체결 출력 기능
def stockhoka(data):
    '''
    - verify that the data received is normal
    print('stockhoka[%s]' %(data)) 
    '''
    recv_value = data.split('^')

    print("유가증권 단축 종목코드 [" + recv_value[0] + "]")
    print("영업시간 [" + recv_value[1] + "]" + "시간구분코드 [" + recv_value[2] + "]")
    print("======================================")
    print("매도호가10 [%s]    잔량10 [%s]" % (recv_value[12], recv_value[32]))
    print("매도호가09 [%s]    잔량09 [%s]" % (recv_value[11], recv_value[31]))
    print("매도호가08 [%s]    잔량08 [%s]" % (recv_value[10], recv_value[30]))
    print("매도호가07 [%s]    잔량07 [%s]" % (recv_value[9], recv_value[29]))
    print("매도호가06 [%s]    잔량06 [%s]" % (recv_value[8], recv_value[28]))
    print("매도호가05 [%s]    잔량05 [%s]" % (recv_value[7], recv_value[27]))
    print("매도호가04 [%s]    잔량04 [%s]" % (recv_value[6], recv_value[26]))
    print("매도호가03 [%s]    잔량03 [%s]" % (recv_value[5], recv_value[25]))
    print("매도호가02 [%s]    잔량02 [%s]" % (recv_value[4], recv_value[24]))
    print("매도호가01 [%s]    잔량01 [%s]" % (recv_value[3], recv_value[23]))
    print("--------------------------------------")
    print("매수호가01 [%s]    잔량01 [%s]" % (recv_value[13], recv_value[33]))
    print("매수호가02 [%s]    잔량02 [%s]" % (recv_value[14], recv_value[34]))
    print("매수호가03 [%s]    잔량03 [%s]" % (recv_value[15], recv_value[35]))
    print("매수호가04 [%s]    잔량04 [%s]" % (recv_value[16], recv_value[36]))
    print("매수호가05 [%s]    잔량05 [%s]" % (recv_value[17], recv_value[37]))
    print("매수호가06 [%s]    잔량06 [%s]" % (recv_value[18], recv_value[38]))
    print("매수호가07 [%s]    잔량07 [%s]" % (recv_value[19], recv_value[39]))
    print("매수호가08 [%s]    잔량08 [%s]" % (recv_value[20], recv_value[40]))
    print("매수호가09 [%s]    잔량09 [%s]" % (recv_value[21], recv_value[41]))
    print("매수호가10 [%s]    잔량10 [%s]" % (recv_value[22], recv_value[42]))
    print("======================================")
    print("총매도호가 잔량        [%s]" % (recv_value[43]))
    print("총매도호가 잔량 증감   [%s]" % (recv_value[54]))
    print("총매수호가 잔량        [%s]" % (recv_value[44]))
    print("총매수호가 잔량 증감   [%s]" % (recv_value[55]))
    print("시간외 총매도호가 잔량 [%s]" % (recv_value[45]))
    print("시간외 총매수호가 증감 [%s]" % (recv_value[46]))
    print("시간외 총매도호가 잔량 [%s]" % (recv_value[56]))
    print("시간외 총매수호가 증감 [%s]" % (recv_value[57]))
    print("예상 체결가            [%s]" % (recv_value[47]))
    print("예상 체결량            [%s]" % (recv_value[48]))
    print("예상 거래량            [%s]" % (recv_value[49]))
    print("예상체결 대비          [%s]" % (recv_value[50]))
    print("부호                   [%s]" % (recv_value[51]))
    print("예상체결 전일대비율    [%s]" % (recv_value[52]))
    print("누적거래량             [%s]" % (recv_value[53]))
    print("주식매매 구분코드      [%s]" % (recv_value[58]))


def stocks_purchase(data_cnt: int, data: str):
    print("============================================")
    menu_list = "유가증권단축종목코드|주식체결시간|주식현재가|전일대비부호|전일대비|전일대비율|가중평균주식가격|주식시가|주식최고가|주식최저가|매도호가1|매수호가1|체결거래량|누적거래량|누적거래대금|매도체결건수|매수체결건수|순매수체결건수|체결강도|총매도수량|총매수수량|체결구분|매수비율|전일거래량대비등락율|시가시간|시가대비구분|시가대비|최고가시간|고가대비구분|고가대비|최저가시간|저가대비구분|저가대비|영업일자|신장운영구분코드|거래정지여부|매도호가잔량|매수호가잔량|총매도호가잔량|총매수호가잔량|거래량회전율|전일동시간누적거래량|전일동시간누적거래량비율|시간구분코드|임의종료구분코드|정적VI발동기준가"
    menu_str = menu_list.split('|')
    pValue = data.split('^')

    i=0
    for cnt in range(data_cnt):
        print('### [%d / %d]' %(cnt+1, data_cnt))
        for menu in menu_str:
            print('%-13s[%s]' %(menu, pValue[i]))
            i += 1

# 주식체결통보 출력 기능
def stock_signing_notice(data, key, iv):
    menu_list = "고객ID|계좌번호|주문번호|원주문번호|매도매수구분|정정구분|주문종류|주문조건|주식단축종목코드|체결수량|체결단가|주식체결시간|거부여부|체결여부|접수여부|지점번호|주문수량|계좌명|체결종목명|신용구분|신용대출일자|체결종목명40|주문가격"
    menu_str = menu_list.split('|')

    # AES256 처리 단계
    aes_dec_str = aes_cbc_base64_dec(key, iv, data)
    pValue = aes_dec_str.split('|')
    
    i=0 
    for menu in menu_str:
        print("%s   [%s]" %(menu, pValue[i]))
        i += 1
    

from ws.config.parser import dotenv_parser
from ws.kis.address import AddressBuilder
async def connect():
    appkey = dotenv_parser.get_env('MY_APPKEY')
    appsecret = dotenv_parser.get_env('MY_SECKEY')

    stockcode = '005930'    # 테스트용 임시 종목 설정, 삼성전자
    htsid = '101334'    # 체결통보용 htsid 입력
    custtype = 'P'      # customer type, 개인:'P' 법인 'B'
    url = AddressBuilder.get_ws_address()
    async with websockets.connect(url, ping_interval=None) as ws:
        
        while True:
            print("1.주식호가, 2.주식호가해제, 3.주식체결, 4.주식체결해제, 5.주식체결통보(고객), 6.주식체결통보해제(고객), 7.주식체결통보(모의), 8.주식체결통보해제(모의)")
            print("Input Command :")
            cmd = input()

            if cmd < '0' or cmd > '9':
                print('> Wrong Input Data', cmd)
                continue
            elif cmd == '0':
                print('Exit!')
                break

            # 입력값에 따라 전송 데이터셋 구분 처리
            if cmd == '1':
                tr_id = 'H0STASP0'
                tr_type='1'
            elif cmd == '2':
                tr_id = 'H0STASP0'
                tr_type = '2'
            elif cmd == '3':  # 주식체결 등록
                tr_id = 'H0STCNT0'
                tr_type = '1'
            elif cmd == '4':  # 주식체결 등록해제
                tr_id = 'H0STCNT0'
                tr_type = '2'
            elif cmd == '5':  # 주식체결통보 등록(고객용)
                tr_id = 'H0STCNI0' # 고객체결통보
                tr_type = '1'
            elif cmd == '6':  # 주식체결통보 등록해제(고객용)
                tr_id = 'H0STCNI0' # 고객체결통보
                tr_type = '2'
            elif cmd == '7':  # 주식체결통보 등록(모의)
                tr_id = 'H0STCNI9'  #테스트용 직원체결통보
                tr_type = '1'
            elif cmd == '8':  # 주식체결통보 등록해제(모의)
                tr_id = 'H0STCNI9'  # 테스트용 직원체결통보
                tr_type = '2'
            else:
                send_data = 'wrong inert data'

            
            # send json, 체결통보는 tr_key 입력하옥이 상이하므로 분리
            if cmd == '5' or cmd == '6' or cmd == '7' or cmd == '8':
                send_data = '{"header":{"appkey":"'+ appkey + '","appsecret":"' + appsecret + '","custtype":"'+custtype+'","tr_type":"' + tr_type + '","content-type":"utf-8"},"body":{"input":{"tr_id":"' + tr_id + '","tr_key":"' + htsid + '"}}}'
            else:
                send_data = '{"header":{"appkey":"' + appkey + '","appsecret":"' + appsecret + '","custtype":"'+custtype+'","tr_type":"' + tr_type + '","content-type":"utf-8"},"body":{"input":{"tr_id":"' + tr_id + '","tr_key":"' + stockcode + '"}}}'

            print('Input Command is :', send_data)

            await ws.send(send_data)

            while True:
                data = await ws.recv()
                print('Recv Command is : ', data)
                if data[0] == '0' or data[0] == '1': # 실시간 데이터일 경우
                    trid = jsonObject['header']['tr_id']
                    
                    if data[0] == '0':
                        recv_str = data.split('|') # 수신데이터가 실데이터 이전은 '|'로 나뉘어져 있어 split
                        trid0 =  recv_str[1]
                        
                        if trid0 == 'H0STASP0': # 주식호가 tr일 경우의 처리 단계
                            print("#### 주식호가 ####")
                            stockhoka(recv_str[3])
                            time.sleep(1)
                        elif trid0 == 'H0STCNT0': # 주식체결 데이터 처리
                            print("#### 주식체결 ####")
                            data_cnt = int(recv_str[2])	# 체결데이터 개수
                            stocks_purchase(data_cnt, recv_str[3])
                    elif data[0] == '1':
                        recv_str = data.split('|')
                        trid0 = recv_str[1]
                        if trid0 == "K0STCNI0" or trid0 == "K0STCNI9" or trid0 == "H0STCNI0" or trid0 == "H0STCNI9":  # 주실체결 통보 처리
                            print("#### 주식체결통보 ####")
                            stock_signing_notice(recv_str[3], aes_key, aes_iv)
                            await ws.send(send_data)
                else:
                    jsonObject = json.loads(data)
                    trid = jsonObject['header']['tr_id']

                    if trid != 'PINGPONG':
                        rt_cd = jsonObject['body']['rt_cd']
                        if rt_cd == '1': # 에러일 경우 처리
                            print("### ERROR RETURN CODE [ %s ] MSG [ %s ]" % (rt_cd, jsonObject["body"]["msg1"]))
                            break
                        elif rt_cd == '0': # 정상일 경우 처리
                            print("### RETURN CODE [ %s ] MSG [ %s ]" % (rt_cd, jsonObject["body"]["msg1"]))
                            if trid == 'K0STCNI0' or trid == 'K0STCNI9' or trid == 'H0STCNI0' or trid == 'H0STCNI9':
                                aes_key = jsonObject['body']['output']['key']
                                aes_iv = jsonObject['body']['output']['iv']
                                print("### TRID [%s] KEY[%s] IV[%s]" % (trid, aes_key, aes_iv))

                    elif trid == "PINGPONG":
                        print("### RECV [PINGPONG] [%s]" % (data))
                        await ws.send(data)
                        print("### SEND [PINGPONG] [%s]" % (data))

# asyncio.get_event_loop().run_until_complete(connect())
# asyncio.get_event_loop().close()