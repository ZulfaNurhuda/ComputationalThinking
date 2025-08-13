""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Document Archiving System>    |
# +----------------------------------------+
# | Manages document archives with         |
# | functionalities to add and search      |
# | documents.                             |
# +----------------------------------------+

# +-----------------------+-----------------+
# | PROGRAM DICTIONARY    | DATA TYPE       |
# +-----------------------+-----------------+
# | num_document_types    | integer         |
# | document_types        | array of string |
# | num_archive_shelves   | integer         |
# | shelf                 | array of string |
# +-----------------------+-----------------+

def parseDocumentData(document: str) -> dict:
    """ Description: `[FUNCTION] parseDocumentData` """
    # +------------------------------------------------+
    # | FUNCTION <Parse Document Data>                 |
    # +------------------------------------------------+
    # | Parses a document string to extract its type   |
    # | and index.                                     |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | document           | string    |
    # | document_type      | string    |
    # | string_index       | string    |
    # | found_separator    | boolean   |
    # | i                  | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE VARIABLES
    document_type: str = ""
    string_index: str = "0"
    found_separator: bool = False

    # ITERATE THROUGH EACH CHARACTER IN THE DOCUMENT STRING
    for i in document:
        # CHECK FOR SEPARATOR
        if i == "-":
            found_separator = True
        else:
            # APPEND CHARACTERS TO DOCUMENT TYPE OR INDEX BASED ON SEPARATOR
            if found_separator:
                string_index += i
            else:
                document_type += i

    # RETURN PARSED DOCUMENT DATA
    return {"document_type": str(document_type), "index": int(string_index)}

def inputDocumentTypes(count: int) -> list[str]:
    """ Description: `[FUNCTION] inputDocumentTypes` """
    # +------------------------------------------------+
    # | FUNCTION <Input Document Types>                |
    # +------------------------------------------------+
    # | Prompts the user to input document types based |
    # | on a given count.                              |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | count              | integer   |
    # | i                  | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # PROMPT USER FOR EACH DOCUMENT TYPE AND RETURN AS A LIST
    return [str(input(f"Masukkan tipe dokumen ke-{i+1}: ")) for i in range(count)]

def inputArchiveShelves(num_shelves: int, document_types: list[str]) -> list[str]:
    """ Description: `[FUNCTION] inputArchiveArchiveShelves` """
    # +------------------------------------------------+
    # | FUNCTION <Input Archive Shelves>               |
    # +------------------------------------------------+
    # | Prompts the user to input documents for archive|
    # | shelves, validating document types.            |
    # +------------------------------------------------+

    # +--------------------+-----------------+
    # | LOCAL DICTIONARY   | DATA TYPE       |
    # +--------------------+-----------------+
    # | num_shelves        | integer         |
    # | document_types     | list of string  |
    # | shelf              | list of string  |
    # | i                  | integer         |
    # | document           | string          |
    # | document_data      | dictionary      |
    # +--------------------+-----------------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE SHELF WITH EMPTY SLOTS
    shelf: list[str] = ["" for _ in range(num_shelves)]
    i: int = 0
    # LOOP TO FILL EACH SHELF SLOT
    while i < num_shelves:
        # PROMPT FOR DOCUMENT INPUT
        document: str = str(input(f"Slot {i+1}: "))
        # IF INPUT IS EMPTY, MOVE TO NEXT SLOT
        if document == "":
            i += 1
        else:
            # PARSE DOCUMENT DATA
            document_data: dict = parseDocumentData(document)
            # VALIDATE DOCUMENT TYPE
            if document_data["document_type"] in document_types:
                # ADD DOCUMENT TO SHELF IF VALID
                shelf[i] = document
                i += 1
            else:
                # PRINT ERROR FOR INVALID DOCUMENT TYPE
                print(f'Tipe dokumen {document_data["document_type"]} tidak valid!')
    # RETURN THE FILLED SHELF
    return shelf

def findMaxIndex(indexed_items: list) -> int:
    """ Description: `[FUNCTION] findMaxIndex` """
    # +------------------------------------------------+
    # | FUNCTION <Find Maximum Index>                  |
    # +------------------------------------------------+
    # | Finds the maximum index from a list of indexed |
    # | items.                                         |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | indexed_items      | list      |
    # | max_index          | integer   |
    # | index              | any       |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE MAX_INDEX
    max_index: int = 0
    # ITERATE THROUGH EACH INDEX IN THE LIST
    for index in indexed_items:
        # UPDATE MAX_INDEX IF CURRENT INDEX IS GREATER
        if index > max_index:
            max_index = index
    # RETURN THE MAXIMUM INDEX FOUND
    return max_index

def addNewDocument(shelf: list[str], num_shelves: int, document_types: list[str]) -> list[str]:
    """ Description: `[FUNCTION] addNewDocument` """
    # +------------------------------------------------+
    # | FUNCTION <Add New Document>                    |
    # +------------------------------------------------+
    # | Adds a new document to the archive shelf,      |
    # | assigning it a new index based on existing     |
    # | documents of the same type.                    |
    # +------------------------------------------------+

    # +--------------------+-----------------+
    # | LOCAL DICTIONARY   | DATA TYPE       |
    # +--------------------+-----------------+
    # | shelf              | list of string  |
    # | num_shelves        | integer         |
    # | document_types     | list of string  |
    # | done               | boolean         |
    # | i                  | integer         |
    # | new_document       | string          |
    # | indexed_items      | list            |
    # | j                  | integer         |
    # | current_document   | dictionary      |
    # | max_index          | integer         |
    # | new_index          | integer         |
    # +--------------------+-----------------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE VARIABLES
    done: bool = False
    i: int = 0
    # LOOP WHILE NOT DONE AND THERE ARE EMPTY SLOTS IN THE SHELF
    while not done and "" in shelf:
        # CHECK IF CURRENT SHELF SLOT IS EMPTY
        if shelf[i] == "":
            # PROMPT FOR NEW DOCUMENT INPUT
            new_document: str = str(input("Masukkan dokumen baru: "))
            # CHECK IF USER WANTS TO FINISH
            if new_document == "selesai":
                done = True
            # VALIDATE NEW DOCUMENT TYPE
            elif new_document not in document_types:
                print(f"Tipe dokumen {new_document} tidak valid!")
            else:
                # FIND EXISTING INDICES FOR THE NEW DOCUMENT TYPE
                indexed_items: list = []
                for j in range(num_shelves):
                    if shelf[j] != "":
                        current_document: dict = parseDocumentData(shelf[j])
                        if current_document["document_type"] == new_document:
                            indexed_items += [current_document["index"]]

                # DETERMINE NEW INDEX
                max_index: int = findMaxIndex(indexed_items)
                new_index: int = max_index + 1
                # ADD NEW DOCUMENT TO SHELF
                shelf[i] = f"{new_document}-{new_index}"
                i += 1
        else:
            # MOVE TO NEXT SLOT IF CURRENT IS NOT EMPTY
            i += 1

    # CHECK IF SHELF IS FULL
    if not done:
        print("Rak arsip sudah penuh!")
    # RETURN UPDATED SHELF
    return shelf

def searchDocument(shelf: list[str], num_shelves: int, document_types: list[str]) -> None:
    """ Description: `[PROCEDURE] searchDocument` """
    # +------------------------------------------------+
    # | PROCEDURE <Search Document>                    |
    # +------------------------------------------------+
    # | Searches for documents of a specific type in   |
    # | the archive shelf and prints their locations.  |
    # +------------------------------------------------+

    # +--------------------+-----------------+
    # | LOCAL DICTIONARY   | DATA TYPE       |
    # +--------------------+-----------------+
    # | shelf              | list of string  |
    # | num_shelves        | integer         |
    # | document_types     | list of string  |
    # | done               | boolean         |
    # | search_query       | string          |
    # | indexed_items      | list            |
    # | j                  | integer         |
    # | current_document   | dictionary      |
    # | len_indexed_items  | integer         |
    # | m                  | integer         |
    # | n                  | integer         |
    # | data               | dictionary      |
    # +--------------------+-----------------+

    """ PROCEDURE ALGORITHM """
    # INITIALIZE FLAG FOR LOOP CONTROL
    done: bool = False
    # LOOP UNTIL USER ENTERS "selesai"
    while not done:
        # PROMPT FOR SEARCH QUERY
        search_query: str = str(input("Masukkan tipe dokumen yang ingin dicari: "))
        # CHECK IF USER WANTS TO FINISH
        if search_query == "selesai":
            done = True
        # VALIDATE SEARCH QUERY TYPE
        elif search_query not in document_types:
            print(f"Tipe dokumen {search_query} tidak valid!")
        else:
            # FIND MATCHING DOCUMENTS AND THEIR LOCATIONS
            indexed_items: list = []
            for j in range(num_shelves):
                if shelf[j] != "":
                    current_document: dict = parseDocumentData(shelf[j])
                    if current_document["document_type"] == search_query:
                        indexed_items += [
                            {"document_index": current_document["index"], "shelf_location": j}
                        ]

            # GET LENGTH OF FOUND ITEMS
            len_indexed_items: int = 0
            for _ in indexed_items:
                len_indexed_items += 1

            # SORT FOUND ITEMS BY DOCUMENT INDEX (BUBBLE SORT)
            for m in range(1, len_indexed_items):
                for n in range(0, len_indexed_items - 1):
                    if indexed_items[n]["document_index"] > indexed_items[n + 1]["document_index"]:
                        indexed_items[n], indexed_items[n + 1] = indexed_items[n + 1], indexed_items[n]

            # PRINT LOCATIONS OF FOUND DOCUMENTS
            for data in indexed_items:
                print(
                    f'Dokumen {search_query}-{data["document_index"]} ditemukan pada slot {data["shelf_location"] + 1}'
                )

        # PRINT EMPTY LINE FOR BETTER READABILITY IF NOT DONE
        if (not done): print("")

""" PROGRAM ALGORITHM """
# INPUT NUMBER OF DOCUMENT TYPES
num_document_types: int = int(input("Masukkan jumlah tipe dokumen: "))
# INPUT DOCUMENT TYPES
document_types: list[str] = inputDocumentTypes(num_document_types)

# PRINT EMPTY LINE FOR READABILITY
print("")

# INPUT NUMBER OF ARCHIVE SHELVES
num_archive_shelves: int = int(input("Masukkan jumlah slot rak arsip: "))
print("Masukkan isi rak arsip saat ini")
# INPUT ARCHIVE SHELVES
shelf: list[str] = inputArchiveShelves(num_archive_shelves, document_types)

# PRINT EMPTY LINE FOR READABILITY
print("")

# ADD NEW DOCUMENT TO ARCHIVE
shelf = addNewDocument(shelf, num_archive_shelves, document_types)

# PRINT EMPTY LINE FOR READABILITY
print("")

# SEARCH FOR DOCUMENTS IN ARCHIVE
searchDocument(shelf, num_archive_shelves, document_types)