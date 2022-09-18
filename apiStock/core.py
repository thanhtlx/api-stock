import requests
import random
from datetime import datetime
from .const import USER_AGENTS


URL = 'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:%s~date:gte:%s~date:lte:%s&size=100000'
URL_SSI_STOCK_HISTORY = "https://iboard.ssi.com.vn/dchart/api/history?resolution=D&symbol=%s&from=%s&to=%s" 
URL_SSI_STOCK_INFO = "https://finfo-iboard.ssi.com.vn/graphql"
def DICT_FILTER(x, y): return dict([(i, x[i]) for i in x if i in set(y)])


KEYS = ['date', 'ceilingPrice', 'floorPrice', 'open',
        'high', 'low', 'close', 'average', 'change',
        "nmVolume"]



def getStockHistoryV2(code,start_date,end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    end_time = int(end_date.timestamp())
    start_time = int(start_date.timestamp())
    try:
        r = requests.get(URL_SSI_STOCK_HISTORY % (code, start_time, end_time),
                         headers={"USER-AGENT": USER_AGENTS[random.randint(0, len(USER_AGENTS)-1)]})
        res = r.json()
    except Exception as e:
        return []
    result = dict()
    for k,v in res.copy().items():
        if isinstance(v, list):
            v.reverse()
            result[k] = v
    return result

def getStockHistory(code, start_date, end_date):
    try:
        r = requests.get(URL % (code, start_date, end_date),
                         headers={"USER-AGENT": USER_AGENTS[random.randint(0, len(USER_AGENTS)-1)]})
        res = r.json()
    except Exception as e:
        return []
    if 'data' in res and len(res['data']) > 0:
        res = list(map(lambda x: DICT_FILTER(x, KEYS), res['data']))
        res.reverse()
        return res
    return []

def getStockInfo(code):
    body = {
        "operationName": "financialIndicator",
        "variables": {
            "symbol": code,
            "size": 10
        },
        "query": "query financialIndicator($symbol: String!, $yearReport: String, $lengthReport: String, $size: Int, $offset: Int) {  financialIndicator(symbol: $symbol  yearReport: $yearReport  lengthReport: $lengthReport size: $size offset: $offset)}"
    }
    try:
        r = requests.post(URL_SSI_STOCK_INFO, json = body,
                         headers={"USER-AGENT": USER_AGENTS[random.randint(0, len(USER_AGENTS)-1)]})
        res = r.json()
    except Exception as e:
        print(e)
        return []
    if "errors" in res:
        return []
    res  = res["data"]["financialIndicator"]["dataList"]
    i = 0
    for i in range(len(res)):
        hit = res[i]
        if hit["revenue"] != "N" and  hit['profit'] != "N":
            break
    return res[i]

