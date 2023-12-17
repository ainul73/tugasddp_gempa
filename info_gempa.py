from gempa import info_gempa

# Membuat 5 objek Gempa
gempa_banten = info_gempa("banten", 1.2)
gempa_palu = info_gempa("palu", 6.1)
gempa_cianjur = info_gempa("cianjur", 5.6)
gempa_jayapura = info_gempa("jayapura", 3.3)
gempa_garut = info_gempa("garut", 4.0)

# Memanggil fungsi dampak() untuk masing-masing objek Gempa
gempa_banten.dampak()
gempa_palu.dampak()