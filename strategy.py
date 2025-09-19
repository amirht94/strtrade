def sample_strategy(ohlcv):
    """
    نمونه ساده استراتژی: اگر قیمت بسته شدن آخرین کندل > قیمت بسته شدن قبل، BUY، در غیر اینصورت SELL
    """
    if len(ohlcv) < 2:
        return "NO DATA"
    
    last_close = ohlcv[-1][4]
    prev_close = ohlcv[-2][4]
    
    if last_close > prev_close:
        return "BUY"
    else:
        return "SELL"
