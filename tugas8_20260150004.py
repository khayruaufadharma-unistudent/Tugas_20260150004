# tugas8_NIM.py  (ganti "NIM" pada nama file dengan NIM Anda)
# Program utama Sistem Monitoring Presisi IoT

import modul_sensor

# List kosong untuk menyimpan data bertipe tuple: (suhu, kelembaban)
log_kebun = []


def input_float_valid(pesan, minimum, maksimum):
    """Meminta angka desimal dalam rentang tertentu sampai valid."""
    while True:
        try:
            nilai = float(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"  Nilai harus di antara {minimum} dan {maksimum}!")
        except ValueError:
            print("  Input harus berupa angka, bukan huruf!")


def input_sensor():
    """Mengembalikan tuple (suhu, kelembaban) yang sudah tervalidasi."""
    suhu = input_float_valid("Masukkan Suhu Udara (C) [0-100]: ", 0, 100)
    lembab = input_float_valid("Masukkan Kelembaban Tanah (%) [0-100]: ", 0, 100)
    return (suhu, lembab)


def rekam_data():
    data = input_sensor()
    log_kebun.append(data)
    print(f"Data {data} berhasil direkam. Total data: {len(log_kebun)}")


def analisis_tren():
    if len(log_kebun) == 0:
        print("Belum ada data. Rekam data terlebih dahulu (menu 1).")
        return

    # Slicing: ambil maksimal 3 data terakhir
    tiga_terakhir = log_kebun[-3:]

    print(f"\nLokasi: {modul_sensor.LOKASI[0]}")
    print(f"Menganalisis {len(tiga_terakhir)} data terakhir:")
    for nomor, (suhu, lembab) in enumerate(tiga_terakhir, start=1):
        print(f"  Data {nomor}: Suhu = {suhu} C | Kelembaban = {lembab} %")

    rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
    print(f"Rata-rata Suhu       : {rata_suhu:.2f} C")
    print(f"Rata-rata Kelembaban : {rata_lembab:.2f} %")

    status = modul_sensor.evaluasi_irigasi(
        rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS
    )
    print(f"Status: {status}")


def main():
    while True:
        print("\n=== MONITORING IoT KAMPUNG ANGGUR PLUMBUNGAN ===")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            rekam_data()
        elif pilihan == "2":
            analisis_tren()
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid, masukkan 1, 2, atau 3.")


if __name__ == "__main__":
    main()
