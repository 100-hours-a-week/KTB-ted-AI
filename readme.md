
# Stock_CLI

주식 티커를 입력하면 현재 주식 가격을 조회할 수 있는 CLI 프로그램입니다.  
`argparse`를 사용하여 터미널 명령어 형태로 동작하며, `yfinance` 라이브러리를 통해 실시간 주가 정보를 가져옵니다.

---

# How to use

## 실행 방법

```bash
python main.py TSLA
```

```bash
python main.py AAPL
```

```bash
python main.py 005930.KS
```

---

# 사용 예시

## 미국 주식 조회

```bash
python main.py TSLA
```

출력 예시

```bash
현재가: $321.55
```

---

## 한국 주식 조회

```bash
python main.py 005930.KS
```

출력 예시

```bash
현재가: $82.14
```

---

# 지원 종목

## 미국 주식
- TSLA
- AAPL
- NVDA
- MSFT

등 티커 사용

---

## 한국 주식
- 삼성전자 → 005930.KS
- SK하이닉스 → 000660.KS

등 종목코드 사용

---

# 설치 방법

## yfinance 설치

```bash
pip install yfinance
```

---


# 코드 설명

## argparse

사용자가 터미널에서 종목 티커를 입력할 수 있도록 구현했습니다.

예시:

```bash
python main.py TSLA
```

---

## yfinance

Yahoo Finance 데이터를 이용하여 실시간 주식 현재가를 조회했습니다.

---

# 회고

처음에는 CLI 프로그램이 단순히 터미널에서 실행되는 프로그램 정도로만 생각했습니다.  
하지만 이번 과제를 진행하면서 강의에서 배운 기능인 argparse를 사용해 명령어 기반 입력을 처리하고, 외부 라이브러리를 통해 실제 데이터를 가져오는 과정까지 경험할 수 있었습니다.

또한 yfinance를 사용하면서 API 형태의 데이터 활용 방식도 처음 접하였고 터미널 환경에서 프로그램을 실행하는 흐름도 익힐 수 있었습니다.

아직은 기능이 단순하지만 이후에는:

- 여러 종목 동시 조회
- 주가 변동률 출력
- 관심 종목 저장 기능
- 그래프 출력

등의 기능을 추가해보고 싶습니다.

이번 과제를 통해 간단한 코드로 이루어진 CLI 프로그램이지만 argparse 사용과 yfinance를 사용해보며 이론에 대한 이해도가 높아졌습니다.