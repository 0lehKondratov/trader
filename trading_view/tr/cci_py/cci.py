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


//@version=5
indicator(title="Commodity Channel Index", shorttitle="CCI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
length = input.int(20, minval=1)
src = input(hlc3, title="Source")
ma = ta.sma(src, length)
cci = (src - ma) / (0.015 * ta.dev(src, length))
plot(cci, "CCI", color=#2962FF)
band1 = hline(100, "Upper Band", color=#787B86, linestyle=hline.style_dashed)
hline(0, "Middle Band", color=color.new(#787B86, 50))
band0 = hline(-100, "Lower Band", color=#787B86, linestyle=hline.style_dashed)
fill(band1, band0, color=color.rgb(33, 150, 243, 90), title="Background")

ma(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

typeMA = input.string(title = "Method", defval = "SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="Smoothing")
smoothingLength = input.int(title = "Length", defval = 5, minval = 1, maxval = 100, group="Smoothing")

smoothingLine = ma(cci, smoothingLength, typeMA)
plot(smoothingLine, title="Smoothing Line", color=#f37f20, display=display.none)
