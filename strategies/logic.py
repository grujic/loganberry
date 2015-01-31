# Imports
from strategies.quotes_class import Quote, Quotes

# Functions

def refresh_quotes(conn):
    # Checks wether quotes are in place, updates them if needed

    ALPHA_TOLERANCE = 2
    ALPHA_INDEX = - 0.3
    BETA_TOLERANCE = 2
    BETA_INDEX = -0.1
    GAMMA_TOLERANCE = 10
    GAMMA_INDEX = 0.0

    tickets = ['FOO','BAR','BAZ','QUUX','CORGE']
    for ticket in tickets:

        # BUY
        lead = conn.book.nth_buy_price(ticket, 0)
        mid = conn.book.nth_buy_price(ticket, 5)
        tail = conn.book.nth_buy_price(ticket, 10)

        mean_volume = conn.book.mean_buy_volume(ticket)
        position = conn.bank.positions[ticket]

        # ALPHA
        q_id = conn.quotes.getID( ticker, 'BUY', 'Alpha' )
        q_val = conn.quotes.getValue( q_id ) 
        if ( q_id == -1 or q_val <= lead - ALPHA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancel(q_id)

            # Set new quote
            price = lead + 1
            volume = int ( mean_volume + position * ALPHA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, 0, "BUY", price, volume )
                new_quote = Quote( ticker, "BUY", "Alpha", volume, price, new_id )
                conn.quotes.addQuote( newQuote )

        # BETA
        q_id = conn.quotes.getID( ticker, 'BUY', 'Beta' )
        q_val = conn.quotes.getValue( q_id ) 
        if ( q_id == -1 or q_val >= lead + BETA_TOLERANCE or q_val <= mid - BETA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancel(q_id)

            # Set new quote
            price = int( 0.5 * (lead + mid) )
            volume = int ( mean_volume + position * BETA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, 0, "BUY", price, volume )
                new_quote = Quote( ticker, "BUY", "Beta", volume, price, new_id )
                conn.quotes.addQuote( newQuote )

        # GAMMA
        q_id = conn.quotes.getID( ticker, 'BUY', 'Gamma' )
        q_val = conn.quotes.getValue( q_id ) 
        if ( q_id == -1 or q_val >= mid + GAMMA_TOLERANCE or q_val <= tail - GAMMA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancel(q_id)

            # Set new quote
            price = int( 0.5 * (tail + mid) )
            volume = int ( mean_volume + position * GAMMA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, 0, "BUY", price, volume )
                new_quote = Quote( ticker, "BUY", "Gamma", volume, price, new_id )
                conn.quotes.addQuote( newQuote )

        # SELL
        
        lead = conn.book.nth_sell_price(ticket, 0)
        mid = conn.book.nth_sell_price(ticket, 5)
        tail = conn.book.nth_sell_price(ticket, 10)

        mean_volume = conn.book.mean_sell_volume(ticket)
        position = -conn.bank.positions[ticket]

        # ALPHA
        q_id = conn.quotes.getID( ticker, 'SELL', 'Alpha' )
        q_val = conn.quotes.getValue( q_id ) 
        if ( q_id == -1 or q_val >= lead + ALPHA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancel(q_id)

            # Set new quote
            price = lead - 1
            volume = int ( mean_volume + position * ALPHA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, 0, "SELL", price, volume )
                new_quote = Quote( ticker, "SELL", "Alpha", volume, price, new_id )
                conn.quotes.addQuote( newQuote )

        # BETA
        q_id = conn.quotes.getID( ticker, 'SELL', 'Beta' )
        q_val = conn.quotes.getValue( q_id ) 
        if ( q_id == -1 or q_val <= lead + BETA_TOLERANCE or q_val >= mid - BETA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancel(q_id)

            # Set new quote
            price = int( 0.5 * (lead + mid) )
            volume = int ( mean_volume + position * BETA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, 0, "SELL", price, volume )
                new_quote = Quote( ticker, "SELL", "Beta", volume, price, new_id )
                conn.quotes.addQuote( newQuote )

        # GAMMA
        q_id = conn.quotes.getID( ticker, 'SELL', 'Gamma' )
        q_val = conn.quotes.getValue( q_id ) 
        if ( q_id == -1 or q_val <= mid + GAMMA_TOLERANCE or q_val >= tail - GAMMA_TOLERANCE ):
            if ( q_id > 0 ):
                # Cancel quote
                conn.quotes.removeQuote( q_id )
                conn.cancel(q_id)

            # Set new quote
            price = int( 0.5 * (tail + mid) )
            volume = int ( mean_volume + position * GAMMA_INDEX )
            if ( volume > 0 ):
                new_id = conn.addOrder( ticker, 0, "SELL", price, volume )
                new_quote = Quote( ticker, "SELL", "Gamma", volume, price, new_id )
                conn.quotes.addQuote( newQuote )