import requests
URL = 'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:%s~date:gte:%s~date:lte:%s&size=100000'
def DICT_FILTER(x, y): return dict([(i, x[i]) for i in x if i in set(y)])


KEYS = ['date', 'ceilingPrice', 'floorPrice', 'open',
        'high', 'low', 'close', 'average', 'change']


def getAllHistoryPrices(code, start, end):
    try:
        r = requests.get(URL % (code, start, end))
        res = r.json()
    except Exception as e:
        return {'status': 'Error', 'message': e, 'data': []}
    if 'data' in res and len(res['data']) > 0:
        res = list(map(lambda x: DICT_FILTER(x, KEYS), res['data']))
        return {'status': 'OK', 'message': 'Success', 'data': res}
    return {'status': 'Not Found', 'message': 'No Data', 'data': []}
