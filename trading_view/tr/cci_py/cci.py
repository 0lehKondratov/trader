import pandas as pd
import numpy as np

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_cci(data, length=20):
    TP = (data['High'] + data['Low'] + data['Close']) / 3
    sma = calculate_sma(TP, length)
    mean_dev = lambda x: np.mean(np.abs(x - np.mean(x)))
    d = TP.rolling(window=length).apply(mean_dev, raw=True)
    cci = (TP - sma) / (0.015 * d)
    return cci

def apply_smoothing(cci, length=5, method='SMA'):
    if method == 'SMA':
        return calculate_sma(cci, length)
    else:
        # Implement other methods as needed
        return cci

# Example usage with a sample DataFrame
if __name__ == "__main__":
    # Create a sample DataFrame
    data = pd.DataFrame({
        'High': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'Low': [5, 6, 7, 8, 9, 8, 7, 6, 5, 4],
        'Close': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    })

    cci = calculate_cci(data)
    smoothed_cci = apply_smoothing(cci)

    print(smoothed_cci)


