"""A simple stock portfolio tracker using manually defined example prices."""

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00,
}


def main():
    print("\n=== Stock Portfolio Tracker ===")
    print("Example prices are hardcoded for practice; they are not live market prices.")
    print("\nAvailable symbols and example prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f}")

    portfolio = {}
    while True:
        symbol = input("\nEnter a stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Symbol not found. Choose one from the list above.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a whole number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("No stocks entered.")
        return

    total = 0.0
    print("\n--- Portfolio Summary ---")
    lines = ["Stock Portfolio Summary", "Symbol,Quantity,Unit Price,Total Value"]
    for symbol, quantity in portfolio.items():
        unit_price = STOCK_PRICES[symbol]
        value = quantity * unit_price
        total += value
        print(f"{symbol}: {quantity} shares x ${unit_price:.2f} = ${value:.2f}")
        lines.append(f"{symbol},{quantity},{unit_price:.2f},{value:.2f}")

    print(f"\nTotal investment value: ${total:.2f}")
    lines.append(f"TOTAL,,,{total:.2f}")

    save = input("Save this report to portfolio_report.csv? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio_report.csv", "w", encoding="utf-8", newline="") as file:
            file.write("\n".join(lines) + "\n")
        print("Saved portfolio_report.csv")


if __name__ == "__main__":
    main()
