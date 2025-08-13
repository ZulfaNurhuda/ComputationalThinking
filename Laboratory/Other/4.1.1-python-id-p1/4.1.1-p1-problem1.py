""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Item Purchase>                |
# +----------------------------------------+
# | DETERMINES IF MR. LEO CAN BUY THE      |
# | DESIRED ITEM.                          |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | purchase_price     | integer   |
# | selling_price      | integer   |
# | new_item_price     | integer   |
# | savings            | integer   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# GET THE PURCHASE PRICE OF THE ITEM TO BE SOLD FROM THE USER.
purchase_price: int = int(input("Masukkan harga beli barang yang akan dijual: "))
# GET THE SELLING PRICE OF THE ITEM TO BE SOLD FROM THE USER.
selling_price: int = int(input("Masukkan harga jual barang yang akan dijual: "))
# GET THE PRICE OF THE NEW ITEM MR. LEO WANTS TO BUY FROM THE USER.
new_item_price: int = int(input("Masukkan harga barang yang ingin dibeli: "))
# GET MR. LEO'S CURRENT SAVINGS FROM THE USER.
savings: int = int(input("Masukkan tabungan Tuan Leo: "))

# CHECK IF THE SELLING PRICE IS GREATER THAN OR EQUAL TO THE PURCHASE PRICE.
if selling_price >= purchase_price:
    # IF TRUE, CHECK IF MR. LEO'S SAVINGS PLUS THE SELLING PRICE ARE ENOUGH TO BUY THE NEW ITEM.
    if savings + selling_price >= new_item_price:
        print("Tuan Leo dapat membeli barang yang diinginkan.")
    else:
        print("Tuan Leo tidak dapat membeli barang yang diinginkan.")
else:
    # IF THE SELLING PRICE IS LESS THAN THE PURCHASE PRICE, CHECK IF MR. LEO'S SAVINGS ALONE ARE ENOUGH TO BUY THE NEW ITEM.
    if savings >= new_item_price:
        print("Tuan Leo dapat membeli barang yang diinginkan.")
    else:
        print("Tuan Leo tidak dapat membeli barang yang diinginkan.")