
from flask import Flask, request, jsonify
import pandas as pd
import pandas_ta as ta

app = Flask(__name__)

def calculate_indicators(data):
    df = pd.DataFrame(data)
    
    # Calculate RSI
    df['RSI'] = df['close'].ta.rsi(length=14)
    
    # Calculate SMA
    df['SMA'] = df['close'].ta.sma(length=30)
    
    # Calculate MACD
    macd = df['close'].ta.macd()
    df['MACD'] = macd['MACD_12_26_9']
    df['MACD_signal'] = macd['MACDs_12_26_9']
    df['MACD_hist'] = macd['MACDh_12_26_9']
    
    return df

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    df = pd.DataFrame(data)
    df = calculate_indicators(df)
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
