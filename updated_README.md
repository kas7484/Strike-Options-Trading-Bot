
# Strike Options Trading Bot

This project includes a basic trading bot for Strike Options on Crypto.com, built with Python. It consists of two main components:
- A Flask backend for data collection, technical analysis, and trade prediction
- A Tkinter frontend for a simple user interface

## Requirements

Make sure you have Python installed. You'll also need to install the following libraries:

```
pip install pandas requests scikit-learn pandas_ta flask tk
```

## Files

- `app.py`: The Flask backend script
- `frontend.py`: The Tkinter frontend script

## Instructions

### Step 1: Start the Flask Backend

1. Open a terminal or command prompt.
2. Navigate to the directory containing `app.py`.
3. Run the Flask server with the following command:

```
python app.py
```

You should see output indicating that the Flask server is running on `http://127.0.0.1:5000/`.

### Step 2: Run the Tkinter Frontend

1. Open another terminal or command prompt.
2. Navigate to the directory containing `frontend.py`.
3. Run the Tkinter application with the following command:

```
python frontend.py
```

### Usage

1. In the Tkinter GUI, enter the cryptocurrency symbol you want to get a trade decision for (e.g., `bitcoin`).
2. Click the "Get Trade Decision" button.
3. The trade decision (Buy or Sell) will be displayed in the application window.

## Notes

- The current implementation only supports the `bitcoin` symbol for demonstration purposes. You can extend the backend to support more symbols by modifying the `trade_decision` function in `app.py`.
- The machine learning model is trained on historical data using simple technical indicators. For production use, consider using more sophisticated models and including additional data sources.

## Disclaimer

This project is for educational purposes only. Trading cryptocurrencies involves significant risk, and you should conduct your own research before making any trading decisions.
