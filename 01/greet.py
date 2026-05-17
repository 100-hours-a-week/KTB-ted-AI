import argparse
import yfinance as yf


# 한국주식은 종목코드 ex) 삼성전자 = 005930.KS, SK하이닉스 = 000660.KS 등
# 미국주식은 티커 TSLA , AAPL 등
parser = argparse.ArgumentParser(description='주식 현재가 조회')
parser.add_argument('ticker', help='종목 티커 ')
args = parser.parse_args()

stock = yf.Ticker(args.ticker)
price = stock.info['currentPrice']
print(f"현재가: ${price}") # 현재가격 출력
