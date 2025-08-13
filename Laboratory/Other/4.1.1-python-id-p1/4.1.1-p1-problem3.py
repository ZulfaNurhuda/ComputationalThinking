""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Antique Auction>              |
# +----------------------------------------+
# | CALCULATES THE TOTAL COST TO BE PAID   |
# | BY MR. LEO AFTER PARTICIPATING IN AN   |
# | AUCTION.                               |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | initial_price      | integer   |
# | bid_count          | integer   |
# +--------------------+-----------+

def calculateAuctionCost(initial_price: int, bid_count: int) -> int:
    """ Description: `[FUNCTION] calculateAuctionCost` """
    # +------------------------------------------------+
    # | FUNCTION <Calculate Auction Cost>              |
    # +------------------------------------------------+
    # | CALCULATES THE TOTAL COST OF AN ITEM AFTER     |
    # | AN AUCTION, CONSIDERING PRICE ADJUSTMENTS BASED|
    # | ON BID COUNT AND TOTAL COST THRESHOLDS.        |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | initial_price      | integer   |
    # | bid_count          | integer   |
    # | total_cost         | float     |
    # | i                  | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE TOTAL COST WITH THE INITIAL PRICE.
    total_cost: float = initial_price
    # IF THERE ARE NO BIDS, THE COST IS 0.
    if bid_count == 0:
        return 0

    # INITIALIZE A FLAG TO TRACK IF THE VOUCHER HAS BEEN APPLIED.
    voucher_applied: bool = False
    # ITERATE THROUGH EACH BID, UP TO A MAXIMUM OF (BID_COUNT - 1) APPLICATIONS OF THE 10% INCREASE.
    for i in range(max(0, bid_count - 1)):
        # INCREASE TOTAL COST BY 10% FOR EACH BID.
        total_cost *= 1.1
        # IF TOTAL COST EXCEEDS 100,000,000 AND VOUCHER HAS NOT BEEN APPLIED YET, DEDUCT 5,000,000.
        if total_cost > 100000000 and not voucher_applied:
            total_cost -= 5000000
            # SET THE FLAG TO TRUE AS THE VOUCHER HAS BEEN APPLIED.
            voucher_applied = True

    # IF FINAL TOTAL COST EXCEEDS 50,000,000, APPLY A 20% DISCOUNT.
    if total_cost > 50000000:
        total_cost *= 0.8

    # RETURN THE FINAL TOTAL COST AS AN INTEGER.
    return int(total_cost)

""" PROGRAM ALGORITHM """
# GET THE INITIAL PRICE OF THE ITEM FROM THE USER.
initial_price: int = int(input("Masukkan harga awal barang: "))
# GET THE NUMBER OF BIDS FROM THE USER.
bid_count: int = int(input("Masukkan jumlah penawaran: "))

# CALCULATE THE TOTAL AUCTION COST.
result: int = calculateAuctionCost(initial_price, bid_count)
# PRINT THE TOTAL COST TO BE PAID.
print(f"Total biaya yang harus dibayar adalah {result}")
