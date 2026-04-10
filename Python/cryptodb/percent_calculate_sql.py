import sqlite3
import time

DB_NAME = "crypto.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        buy_price REAL,
        sell_price REAL,
        percent REAL,
        margin REAL
    )
    """)

    conn.commit()
    conn.close()


def get_timestamp():
    now = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", now)


def calculate():
    total_price = float(input("total price : "))
    buy_price = float(input("price of buy : "))
    sell_price = float(input("price of sell : "))

    variance_price = (sell_price - buy_price)
    percent = (variance_price / buy_price) * 100
    margin_percent = percent / 100
    total_margin = total_price + (total_price * margin_percent)

    print('==============================')
    print(f"buy_price = {buy_price:.4f}")
    print(f"sell_price = {sell_price:.4f}")
    print(f"percent = {percent:.4f}")
    print(f"margin = {total_margin:.4f}")

    return buy_price, sell_price, percent, total_margin


def save_to_db(timestamp, buy_price, sell_price, percent, margin):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO trades (timestamp, buy_price, sell_price, percent, margin)
    VALUES (?, ?, ?, ?, ?)
    """, (timestamp, buy_price, sell_price, percent, margin))

    conn.commit()
    conn.close()


def show_history():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM trades ORDER BY id DESC LIMIT 5")
    rows = cur.fetchall()

    print("\n최근 거래 기록")
    print("====================================")
    for row in rows:
        print(row)

    conn.close()


init_db()

timestamp = get_timestamp()
buy_price, sell_price, percent, total_margin = calculate()

save_to_db(timestamp, buy_price, sell_price, percent, total_margin)
show_history()