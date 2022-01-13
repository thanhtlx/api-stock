from core import getStockHistory

if __name__ == "__main__":
    s = getStockHistory("BID", "2022-01-11", "2022-02-12")
    print(s)
