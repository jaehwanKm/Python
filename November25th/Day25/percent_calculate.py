import time

now = time.localtime()
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(timestamp)

FILE_PRICE = "D:/Project/PythonGit/Python/November25th/Day25/crypto_price.txt"

#with open(FILE_PRICE,"r", encoding="utf-8") as f:
#    data= f.read()
#    print(data)

def Calculate():
    total_price = float(input("total price :"))
    buy_price = float(input("price of buy :"))
    sell_price = float(input("price of sell :"))
    print('==============================')
    
    variance_price = (sell_price - buy_price)
    percent = (variance_price / buy_price) * 100
    margin_percent = (percent / 100)
    total_margin = (total_price + (total_price * margin_percent))

    print(f"buy_price = {buy_price :.4f} \nsell_price = {sell_price :.4f} \npercent = {percent :.4f}, \nmargin = {total_margin :.4f}")
    return buy_price, sell_price, percent, total_margin

buy_price, sell_price, percent, total_margin = Calculate()     

with open(FILE_PRICE,"a",encoding="utf-8") as f:
    f.write(f"\n{timestamp} \nbuy_price = {buy_price:.4f}, sell_price = {sell_price:.4f}, percent = {percent:.4f}, margin = {total_margin:.4f}")
    f.write("\n=============================================================================================")