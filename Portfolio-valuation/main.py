import requests as r
from bs4 import BeautifulSoup


def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    return {
        "ticker": ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency
    }


if __name__ == "__main__":
    print(get_price_information("MSFT", "NASDAQ"))
