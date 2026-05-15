import pandas as pd
import json

# 위키피디아에서 S&P500 목록 가져오기
table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]

tickers = {}
for i, row in enumerate(df.itertuples(), start=1):
    tickers[str(i)] = {
        "name": row.Security,
        "ticker": row.Symbol,
        "sector": row.GICS_Sector
    }

# JSON 파일로 저장
with open('tickers.json', 'w', encoding='utf-8') as f:
    json.dump(tickers, f, ensure_ascii=False, indent=2)

print(f"총 {len(tickers)}개 종목 저장 완료!")