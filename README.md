## Websocket Kis API TEST
---

**스펙**  
- Python:3.9  
- visual studio code  

**IDE 세팅**  

<u>**Step1.**</u> `root dir` > `venv` 생성  
```shell
$ python -m venv env
``` 

<u>**Step2.**</u> app dir에서 visual studio code 실행  
> 프로젝트의 모든 구동 위치는 app dir이 될 것이다.  
> \-  



<u>**Step3.**</u> Debug탭(*vscode 왼쪽 위에서 4번째*)> `launch.json` 만들기 클릭  
- "**Python: Current File**" 설정은 test.py 파일을 구동할 때 사용
- "**Python: FastAPI**" 설정은 fastapi로 restapi를 사용할 때 사용
- Debug탭에서 (초록색 세모)를 클릭하면 위 설정 변경 가능
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name":"Python: Current File",
            "type":"python",
            "request":"launch",
            "program":"${file}",
            "console":"integratedTerminal"
        },
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args":[
                "app:app"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

<u>**Step4.**</u> [위 launch.json을 만들면 `.vscode` dir이 생성됨] `.vscode` > `setting.json`
```json
{   // mac
    "python.analysis.extraPaths": ["../env/lib/python3.9/site-packages"],
    "python.defaultInterpreterPath": "../env/bin/python"
}

{   // windows
    "python.analysis.extraPaths": ["../env/Lib/site-packages"],
    "python.defaultInterpreterPath": "..\\env\\Scripts\\python.exe"
}
```
- terminal을 생성하면 자동으로 env 환경에 접속됩니다.
- F5로 env 환경의 python 인터프리터가 실행할 수 있습니다.


## Env 파일로 민감정보를 관리하세요
---

`.env.example`(아래)를 보고 자신의 민감정보를 root dir에 `.env`파일에 등록하세요
```text
KIS_VIRTUAL_DOMAIN=[KIS_모의투자_도메인]
KIS_VIRTUAL_PORT=[KIS_모의투자_포트번호]
KIS_WS_VIRTUAL_DOMAIN=[KIS_모의투자_웹소켓_도메인]
KIS_WS_VIRTUAL_PORT=[KIS_모의투자_웹소켓_포트번호]

KIS_DOMAIN=[KIS_실전투자_도메인]
KIS_PORT=[KIS_실전투자_포트번호]
KIS_WS_DOMAIN=[KIS_실전투자_웹소켓_도메인]
KIS_WS_PORT=[KIS_실전투자_웹소켓_포트번호]

MY_APPKEY=[KIS_API_PUBLIC_KEY]
MY_SECKEY=[KIS_API_PRIVATE_KEY]

MY_CANO=[실전투자용_계좌번호]
MY_VIRTUAL_CANO=[모의투자용_계좌번호]

```

## REST API와 Websocket 테스트하는 방법
--- 
**한투(KIS) API의 Rest API를 확인하는 방법**   

<u>**Step1.**</u> Debug 탭에서 "Python: FastApi" 설정을 고르고, `F5`로 실행

<u>**Step2.**</u> web browser에서 **FastAPI swagger**로 api 테스트 가능
- url: `http://localhost:8000/docs`


**한투(KIS) API의 실시간 데이터를 Websocket client로 확인하는 방법**  

<u>**Step1.**</u> Debug 탭에서 "Python: FastApi" 설정을 고르고, `root dir` > `F5`로 실행실행

<u>**Step2.**</u> `test.py`의 주석처리된 코드 확인
- `test.py`의 주석처리한 코드들을 확인하시면 됩니다.
- 테스트 가능 기능
  - 콘솔모드
  - 다중종목 실시간 체결가 조회
  - 실시간 체결가 to excel
  - 실시간 호가 to excel 
> 주의: 마지막 코드는 **실시간 체결가 to excel**와 **실시간 호가 to excel**을 동시에 테스트하는 코드입니다. "실시간1.xlsx"와 "실시간2.xlsx"을 root 디렉토리에 위치시키고 실행하시면 실시간으로 데이터를 확인가능합니다.


