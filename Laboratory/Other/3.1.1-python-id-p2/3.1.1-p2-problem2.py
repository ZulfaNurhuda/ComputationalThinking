""" PROGRAM DESCRIPTION """
# +-------------------------------------------------+
# | PROGRAM <Tidy Up Invoice>                       |
# +-------------------------------------------------+
# | Identify data on an invoice (sending department |
# | number, receiver, and invoice serial number)    |
# | and arrange it in the correct format.           |
# +-------------------------------------------------+

# +----------------------------+----------------------+
# | PROGRAM DICTIONARY         | DATA TYPE            |
# +----------------------------+----------------------+
# | sending_department         | list[string]         |
# | sending_department_data    | dict[string, string] |
# | invoice_number             | string               |
# | invoice_data               | list[string]         |
# | index                      | integer              |
# | separator                  | boolean              |
# | sending_department_invoice | string               |
# | receiving_department_invoice| string              |
# | serial_number_invoice      | string               |
# +----------------------------+----------------------+

""" PROGRAM ALGORITHM """
# INITIALIZE DEPARTMENT NUMBERS THAT CAN SEND
sending_department: list[str] = ["1", "9", "14"]

# INPUT INVOICE DATA GENERATED FROM EACH SENDING DEPARTMENT
sending_department_data: dict[str, str] = {
    department_number: str(input(f"Masukkan jumalah invoice yang telah dikeluarkan oleh departemen {department_number}: "))
    for department_number in sending_department
}

# INPUT THE INVOICE NUMBER TO BE CHECKED
invoice_number: str = str(input("Masukkan nomor invoice yang akan dicek: "))

# INITIALIZE INVOICE DATA TO HOLD THE NUMBERS SEPARATED BY THE SEPARATOR (/)
invoice_data: list[str] = ["" for _ in range(3)]

# CREATE INDEX AND SEPARATOR TO SUPPORT THE LOOP
index: int = 0
separator: bool = False

# LOOP TO FIND THE NUMBERS SEPARATED BY THE SEPARATOR (/)
for i in invoice_number:
    if ('0' <= i <= '9'):
        if (not separator):
            invoice_data[index] += i
        else:
            invoice_data[index] = i
            separator = False
    else:
        index += 1
        separator = True

# INITIALIZE SENDING DEPARTMENT NUMBER, RECEIVER, AND INVOICE SERIAL NUMBER
sending_department_invoice: str = None
receiving_department_invoice: str = None
serial_number_invoice: str = None

# SELECT THE NUMBERS IN THE INVOICE DATA TO BE MANAGED
for i in invoice_data:
    digit: int = 0
    for _ in i:
        digit += 1

    if digit == 3:
        serial_number_invoice = i
    else:
        if i in sending_department:
            sending_department_invoice = i
        else:
            receiving_department_invoice = i

# CONDITIONAL TO FILTER THE CONDITIONS THAT OCCUR
if (sending_department_invoice and receiving_department_invoice and serial_number_invoice):
    if (int(serial_number_invoice) <= int(sending_department_data[sending_department_invoice])):
        print(f"Nomor invoice yang valid: {sending_department_invoice}/{serial_number_invoice}/{receiving_department_invoice}")
    else:
        print("Nomor invoice tersebut tidak valid.")
else:
    print("Nomor invoice tersebut tidak valid.")
