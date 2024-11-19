
import tkinter as tk
import requests

def get_trade_decision(symbol):
    url = f'http://127.0.0.1:5000/calculate'
    try:
        # Example data structure expected by the Flask server
        data = {
            'close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        }
        response = requests.post(url, json=data)
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
root.title("Trade Decision App")

tk.Label(root, text="Enter Symbol:").pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

tk.Button(root, text="Get Trade Decision", command=update_decision).pack()
decision_label = tk.Label(root, text="")
decision_label.pack()

root.mainloop()
