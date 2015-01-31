# Imports
from strategies.quotes_class import Quote, Quotes
import math

# Functions

def refresh_quotes(conn):
    # Checks wether quotes are in place, updates them if needed

    ALPHA_TOLERANCE = 2
    ALPHA_INDEX = - 0.3
    BETA_TOLERANCE = 2
    BETA_INDEX = -0.1
    GAMMA_TOLERANCE = 10
    GAMMA_INDEX = 0.0

    tickers = ['FOO','BAR','BAZ','QUUX','CORGE']
    for ticker in tickers:

        # BUY
        n = conn.book.how_many_buys(ticker)
        
        if n == 0:
            continue

        lead = conn.book.nth_buy_price(ticker, 0)
        mid = conn.book.nth_buy_price(ticker, int(math.floor(1./3*n)))
        tail = conn.book.nth_buy_price(ticker, int(math.floor(2./3*n)))

        mean_volume = conn.book.mean_buy_volume(ticker)
        position = conn.bank.positions[ticker]

        # ALPHA
        q_id = conn.quotes.getID( ticker, 'BUY', 'Alpha' )
        q_val = conn.quotes.getPrice( q_id ) 
        if ( q_id == -1 or q_val <= lead - ALPHA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancelOrder(q_id)

            # Set new quote
            price = lead + 1
            volume = int ( mean_volume + position * ALPHA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, "BUY", price, volume )
                new_quote = Quote( ticker, "BUY", "Alpha", volume, price, new_id )
                conn.quotes.addQuote( new_quote )

        # BETA
        q_id = conn.quotes.getID( ticker, 'BUY', 'Beta' )
        q_val = conn.quotes.getPrice( q_id ) 
        if ( q_id == -1 or q_val >= lead + BETA_TOLERANCE or q_val <= mid - BETA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancelOrder(q_id)

            # Set new quote
            price = int( 0.5 * (lead + mid) )
            volume = int ( mean_volume + position * BETA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, "BUY", price, volume )
                new_quote = Quote( ticker, "BUY", "Beta", volume, price, new_id )
                conn.quotes.addQuote( new_quote )

        # GAMMA
        q_id = conn.quotes.getID( ticker, 'BUY', 'Gamma' )
        q_val = conn.quotes.getPrice( q_id ) 
        if ( q_id == -1 or q_val >= mid + GAMMA_TOLERANCE or q_val <= tail - GAMMA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancelOrder(q_id)

            # Set new quote
            price = int( 0.5 * (tail + mid) )
            volume = int ( mean_volume + position * GAMMA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, "BUY", price, volume )
                new_quote = Quote( ticker, "BUY", "Gamma", volume, price, new_id )
                conn.quotes.addQuote( new_quote )

        # SELL
        n = conn.book.how_many_sells(ticker)
        
        if n == 0:
            continue

        lead = conn.book.nth_sell_price(ticker, 0)
        mid = conn.book.nth_sell_price(ticker, int(math.floor(1./3*n)))
        tail = conn.book.nth_sell_price(ticker, int(math.floor(2./3*n)))

        mean_volume = conn.book.mean_sell_volume(ticker)
        position = -conn.bank.positions[ticker]

        # ALPHA
        q_id = conn.quotes.getID( ticker, 'SELL', 'Alpha' )
        q_val = conn.quotes.getPrice( q_id ) 
        if ( q_id == -1 or q_val >= lead + ALPHA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancelOrder(q_id)

            # Set new quote
            price = lead - 1
            volume = int ( mean_volume + position * ALPHA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, "SELL", price, volume )
                new_quote = Quote( ticker, "SELL", "Alpha", volume, price, new_id )
                conn.quotes.addQuote( new_quote )

        # BETA
        q_id = conn.quotes.getID( ticker, 'SELL', 'Beta' )
        q_val = conn.quotes.getPrice( q_id ) 
        if ( q_id == -1 or q_val <= lead + BETA_TOLERANCE or q_val >= mid - BETA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancelOrder(q_id)

            # Set new quote
            price = int( 0.5 * (lead + mid) )
            volume = int ( mean_volume + position * BETA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, "SELL", price, volume )
                new_quote = Quote( ticker, "SELL", "Beta", volume, price, new_id )
                conn.quotes.addQuote( new_quote )

        # GAMMA
        q_id = conn.quotes.getID( ticker, 'SELL', 'Gamma' )
        q_val = conn.quotes.getPrice( q_id ) 
        if ( q_id == -1 or q_val <= mid + GAMMA_TOLERANCE or q_val >= tail - GAMMA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.Order(q_id)

            # Set new quote
            price = int( 0.5 * (tail + mid) )
            volume = int ( mean_volume + position * GAMMA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, "SELL", price, volume )
                new_quote = Quote( ticker, "SELL", "Gamma", volume, price, new_id )
                conn.quotes.addQuote( new_quote )