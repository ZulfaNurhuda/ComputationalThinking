def parseDocumentData(dokumen):
    jenis_dokumen = ""
    string_index = "0"
    found_separator = False

    for i in dokumen:
        if i == "-":
            found_separator = True
        else:
            if found_separator:
                string_index += i
            else:
                jenis_dokumen += i

    return {"jenis_dokumen": str(jenis_dokumen), "index": int(string_index)}

def input_tipe_dokumen(jumlah):
    return [str(input(f"Masukkan tipe dokumen ke-{i+1}: ")) for i in range(jumlah)]

def input_rak_arsip(jumlah_rak, tipe_dokumen):
    rak = ["" for _ in range(jumlah_rak)]
    i = 0
    while i < jumlah_rak:
        dokumen = str(input(f"Slot {i+1}: "))
        if dokumen == "":
            i += 1
        else:
            data_dokumen = parseDocumentData(dokumen)
            if data_dokumen["jenis_dokumen"] in tipe_dokumen:
                rak[i] = dokumen
                i += 1
            else:
                print(f'Tipe dokumen {data_dokumen["jenis_dokumen"]} tidak valid!')
    return rak

def cari_max_index(terindex):
    max_index = 0
    for index in terindex:
        if index > max_index:
            max_index = index
    return max_index

def tambah_dokumen_baru(rak, jumlah_rak, tipe_dokumen):
    selesai = False
    i = 0
    while not selesai and "" in rak:
        if rak[i] == "":
            dokumen_baru = str(input("Masukkan dokumen baru: "))
            if dokumen_baru == "selesai":
                selesai = True
            elif dokumen_baru not in tipe_dokumen:
                print(f"Tipe dokumen {dokumen_baru} tidak valid!")
            else:
                terindex = []
                for j in range(jumlah_rak):
                    if rak[j] != "":
                        dokumen_sekarang = parseDocumentData(rak[j])
                        if dokumen_sekarang["jenis_dokumen"] == dokumen_baru:
                            terindex += [dokumen_sekarang["index"]]

                max_index = cari_max_index(terindex)
                new_index = max_index + 1
                rak[i] = f"{dokumen_baru}-{new_index}"
                i += 1
        else:
            i += 1

    if not selesai:
        print("Rak arsip sudah penuh!")
    return rak

def cari_dokumen(rak, jumlah_rak, tipe_dokumen):
    selesai = False
    while not selesai:
        search = str(input("Masukkan tipe dokumen yang ingin dicari: "))
        if search == "selesai":
            selesai = True
        elif search not in tipe_dokumen:
            print(f"Tipe dokumen {search} tidak valid!")
        else:
            terindex = []
            for j in range(jumlah_rak):
                if rak[j] != "":
                    dokumen_sekarang = parseDocumentData(rak[j])
                    if dokumen_sekarang["jenis_dokumen"] == search:
                        terindex += [
                            {"index_dokumen": dokumen_sekarang["index"], "letak_rak": j}
                        ]

            panjang_terindex = 0
            for _ in terindex:
                panjang_terindex += 1

            for m in range(1, panjang_terindex):
                for n in range(0, panjang_terindex - 1):
                    if terindex[n]["index_dokumen"] > terindex[n + 1]["index_dokumen"]:
                        terindex[n], terindex[n + 1] = terindex[n + 1], terindex[n]

            for data in terindex:
                print(
                    f'Dokumen {search}-{data["index_dokumen"]} ditemukan pada slot {data["letak_rak"] + 1}'
                )

        print()

""" MAIN PROGRAM"""
jumlah_tipe_dokumen = int(input("Masukkan jumlah tipe dokumen: "))
tipe_dokumen = input_tipe_dokumen(jumlah_tipe_dokumen)

print()

jumlah_rak_arsip = int(input("Masukkan jumlah slot rak arsip: "))
print("Masukkan isi rak arsip saat ini")
rak = input_rak_arsip(jumlah_rak_arsip, tipe_dokumen)

print()

rak = tambah_dokumen_baru(rak, jumlah_rak_arsip, tipe_dokumen)

print()

cari_dokumen(rak, jumlah_rak_arsip, tipe_dokumen)