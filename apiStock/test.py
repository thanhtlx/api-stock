from core import getStockHistoryV2,getStockHistory

if __name__ == "__main__":
    s = getStockHistory("PAN", "2000-01-11", "2022-02-12")
    s1 = getStockHistoryV2("PAN", "2000-01-11", "2022-02-12")
    print(len(s))
    print(len(s1["v"]))
