
import tkinter as tk
import requests

def get_trade_decision(symbol):
    url = f'http://127.0.0.1:5000/calculate'
    try:
        response = requests.post(url, json={'symbol': symbol})
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()       # Attempt to decode the JSON response
        print("Server response:", data)  # Debug print to see the server response
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # HTTP error
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Other request errors
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")  # JSON decode error
    return None

def update_decision():
    symbol = symbol_entry.get()
    decision = get_trade_decision(symbol)
    if decision is not None:
        decision_label.config(text=f"Trade Decision: {decision}")
    else:
        decision_label.config(text="Failed to get trade decision")

# Setup the Tkinter GUI
root = tk.Tk()
root.title("Crypto Trade Decision Bot")

tk.Label(root, text="Enter Symbol:").grid(row=0)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1)

tk.Button(root, text="Get Trade Decision", command=update_decision).grid(row=1, columnspan=2)

decision_label = tk.Label(root, text="Trade Decision: ")
decision_label.grid(row=2, columnspan=2)

root.mainloop()
