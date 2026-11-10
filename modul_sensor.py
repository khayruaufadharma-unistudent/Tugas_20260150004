# modul_sensor.py
# Pustaka logika Sistem Monitoring Presisi IoT - Kampung Anggur Plumbungan

# Konstanta bertipe Tuple (nilainya tidak bisa diubah)
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)  # (Suhu Max dalam C, Kelembaban Min dalam %)


def hitung_tren(data_slice):
    """Menerima list berisi tuple (suhu, kelembaban).
    Mengembalikan (rata-rata suhu, rata-rata kelembaban)."""
    jumlah = len(data_slice)
    if jumlah == 0:  # pengaman agar tidak terjadi pembagian dengan nol
        return 0.0, 0.0

    total_suhu = 0
    total_lembab = 0
    for suhu, lembab in data_slice:  # tuple di-unpack langsung
        total_suhu += suhu
        total_lembab += lembab

    return total_suhu / jumlah, total_lembab / jumlah


def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """Menentukan status pompa berdasarkan rata-rata dan ambang kritis."""
    suhu_max, lembab_min = tuple_kritis  # unpacking tuple ambang

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    return "NORMAL: Pompa Mati."
