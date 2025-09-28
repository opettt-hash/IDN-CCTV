# Coded By Rolandino
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
from __future__ import annotations
import os
import sys
import time
import webbrowser
import shutil
import subprocess
from typing import List, Tuple
H = "\033[92m"
R = "\033[0m"
# -----------------------------
# This Is Roland !
DAFTAR_CCTV: List[Tuple[str, str]] = [
    ("CCTV_PariDermagaUtama", "https://emtv.tachyon.co.id/CCTV_PariDermagaUtama/embed.html"),
    ("CCTV_UJDermagaTengah", "https://emtv.tachyon.co.id/CCTV_UJDermagaTengah/embed.html"),
    ("CCTV_KelapaDermagaPantura", "https://emtv.tachyon.co.id/CCTV_KelapaDermagaPantura/embed.html"),
    ("CCTV_PanggangDermagaUtama", "https://emtv.tachyon.co.id/CCTV_KelapaDermagaPantura/embed.html"),
    ("CCTV_BidaraCina88", "https://emtv.tachyon.co.id/CCTV_BidaraCina88/embed.html"),
    ("CCTV_Susukan45", "https://emtv.tachyon.co.id/CCTV_Susukan45/embed.html"),
    ("CCTV_DurenTiga51", "https://emtv.tachyon.co.id/CCTV_DurenTiga51/embed.html"),
    ("CCTV_Kamal37", "https://emtv.tachyon.co.id/CCTV_Kamal37/embed.html"),
    ("CCTV_PondokPinang53", "https://emtv.tachyon.co.id/CCTV_PondokPinang53/embed.html"),
    ("Tebet-Timur", "https://cctv-jsc.balitower.co.id:8011/Tebet-Timur-006-705568_2/embed.html?proto=hls"),
    ("CCTV_CilandakBarat14", "https://emtv.tachyon.co.id/CCTV_CilandakBarat14/embed.html"),
    ("Pondok-Kopi", "https://cctv-jsc.balitower.co.id:8011/Pondok-Kopi-009-704444_2/embed.html?proto=hls"),
    ("CCTV_Petogogan311", "https://emtv.tachyon.co.id/CCTV_Petogogan311/embed.html"),
    ("CCTV_CilandakBarat14", "https://emtv.tachyon.co.id/CCTV_CilandakBarat14/embed.html"),
    ("CCTV_Keb.Manggis48", "https://emtv.tachyon.co.id/CCTV_Keb.Manggis48/embed.html"),
    ("CCTV_Taman_Bintaro", "https://vms2.jsclab.id/vsaas/embed/taman.bintaro-3b54ccdf88?dvr=false&token=358c4ZKTwxe2ipQoSRrbpuuZ"),
    (" CCTV_Taman_Green_Garden", "https://vms2.jsclab.id/vsaas/embed/taman.green.garden-37cd48cab9?dvr=false&token=P51yXEdcubhpxXWsygNOvbG1"),
    ("CCTV_Taman_Rawa_Badak_Utara", "https://vms2.jsclab.id/vsaas/embed/taman.rawa.badak.utara-2d12a09186?dvr=false&token=rjeMFX4sRznzK4WbWZ59NQsA"),
    ("CCTV_Rumah_Pabrik_Pompa", "https://vms2.jsclab.id/vsaas/embed/phb..mujair-a0b1fd49d9?dvr=false&token=3FERB3HNXxaU0KFv7id6qjWJ"),
    ("CCTV_Taman_Gunung_Balong", "https://vms2.jsclab.id/vsaas/embed/taman.gunung.balong-fa306044e5?dvr=false&token=5igu0Fck6ZPDeMi18o8PT9B3"),
    ("CCTV_Taman_Wijaya_Kusuma", "https://vms2.jsclab.id/vsaas/embed/taman.wijaya.kusuma-f9bae23767?dvr=false&token=nKdgoaGasmPfuT06P1yULRG5"),
    ("CCTV_Taman_Gorontalo", "https://vms2.jsclab.id/vsaas/embed/taman.gorontalo-4e77ab1045?dvr=false&token=zxBl5I6wm1SH3S5RPVOaRhz7"),
    ("CCTV_Taman_Bahariwan", "https://vms2.jsclab.id/vsaas/embed/taman.bahariwan-b33a42e799?dvr=false&token=CcG4l98NpunX5tJOgGBkzTuG"),
    ("CCTV_Taman_Palem", "https://vms2.jsclab.id/vsaas/embed/taman.palem-755da5c6df?dvr=false&token=wGuu8Woy8pNHh6JLGW2CvxGY"),
    ("CCTV_Taman_Warung_Sila", "https://vms2.jsclab.id/vsaas/embed/taman.warung.sila-e86bd4741b?dvr=false&token=EfsvdQjreQ9VTdnYCRGmar76"),
    ("CCTV_Rumah_Pompa_Junction", "https://vms1.jsclab.id/vsaas/embed/rumah.pompa.junction-1dd7cd2430?token=2.07jrdus2AA0ABitBcrUw3wmsLYalJoJrau-aGjJnr20UPPss"),
    ("CCTV_Sunter_Timur_Rawa_Badak", "https://vms2.jsclab.id/vsaas/embed/sunter.timur.3.rawa.badak-c3ff6c55d0?dvr=false&token=vONGGQGKTNan48wk4uG7nQR9"),
    ("CCTV_Dishubjl_Menteng_Raya", "https://vms1.jsclab.id/vsaas/embed/dishub.jl..menteng.raya.-.jl..ridwan.rais.(tugu.tani)-8cf9d78d45?token=2.07jrdus2AA0ABitBcrUw33E7JQdddftZPD2bYl9llLBSTe5S"),
    ("CCTV_LubangBuaya42", "https://emtv.tachyon.co.id/CCTV_LubangBuaya42/embed.html"),
    ("CCTV_Jelambar_Borobudur", "https://vms2.jsclab.id/vsaas/embed/jelambar.borobudur-f3a3c773ee?dvr=false&token=OEI8NdXNhq9Pp0Y6hbbHZ5jj"),
    ("CCTV_Cawang_Wika_Cipinang_Cempedak", "https://vms2.jsclab.id/vsaas/embed/cawang.wika.cipinang.cempedak-f403a81f7a?dvr=false&token=Rkz8Ls4iJsgzQBKb0X7hC1IM"),
    ("CCTV_Tugu_Utara", "https://cctv-jsc.balitower.co.id:8011/Tugu-Utara-008-701515_2/embed.html?proto=hls"),
    ("CCTV_Dishubjlraya_Bogor_Cijantung", "https://vms1.jsclab.id/vsaas/embed/dishub.jl..raya.bogor.-.jl..cijantung-f29c1e8f46?token=2.07jrdus2AA0ABitBcrUw3z6DdfKWU75LZxAZ1bH64DJr7Qkg"),
    ("CCTV_Pondok_Indah_Kartini", "https://vms1.jsclab.id/vsaas/embed/gambir-7eee8dcbb4?token=2.07jrdus2AA0ABitBcrUw3wevOIbxlqZFhO-Md5ueHtP_AcDU"),
    ("CCTV_Pondok_Indah_Margadua", "https://vms1.jsclab.id/vsaas/embed/jl..pondok.indah.-.jl..marga.dua.-.jl..kartika.utama-06d66d7421?token=2.07jrdus2AA0ABitBcrUw38fcbIKzzUeUXLDmLa2-HVoaxz2B"),
    ("CCTV_Galur", "https://cctv-jsc.balitower.co.id:8011/Galur-001-700035_2/embed.html?proto=hls"),
    ("CCTV_Ciracas", "https://cctv-jsc.balitower.co.id:8011/Ciracas-017-704737_2/embed.html?proto=hls"),
    ("CCTV_Serdang", "https://cctv-jsc.balitower.co.id:8011/Serdang-005-700288_2/embed.html?proto=hls"),
    ("CCTV_Sumur-Batu", "https://cctv-jsc.balitower.co.id:8011/Sumur-Batu-005-700179_2/embed.html?proto=hls"),
    ("CCTV_Klingkit_Cengkareng", "https://vms2.jsclab.id/vsaas/embed/klingkit.cengkareng-5892e2843f?dvr=false&token=MgyidEBlarFZER1XmVfGG558"),
    ("CCTV_Melawai", "https://cctv-jsc.balitower.co.id:8011/Melawai-007-705367_1/embed.html?proto=hls"),
    ("CCTV_Cempaka_Putih_Timur", "https://cctv-jsc.balitower.co.id:8011/Cempaka-Putih-Timur-022-700479_2/embed.html?proto=hls"),
    ("CCTV_Ceger", "https://cctv-jsc.balitower.co.id:8011/Ceger-005-704097_2/embed.html?proto=hls"),
    ("CCTV_Duren_Sawit", "https://cctv-jsc.balitower.co.id:8011/Duren-Sawit-008-704174_3/embed.html?proto=hls"),
    ("CCTV_Cilandak_Barat", "https://cctv-jsc.balitower.co.id:8011/Cilandak-Barat-001-705009_2/embed.html?proto=hls"),
    ("CCTV_Gunung_Sahari_Utara", ""),
    ("CCTV_Petogogan311", "https://emtv.tachyon.co.id/CCTV_Petogogan311/embed.html"),
    ("CCTV_Ulujami319", "https://emtv.tachyon.co.id/CCTV_Ulujami319/embed.html"),
    ("CCTV_Cijantung", "https://cctv-jsc.balitower.co.id:8011/Cijantung-001-704103_2/embed.html?proto=hls"),
    ("CCTV_Kebayoran_Lama_Utara", "https://cctv-jsc.balitower.co.id:8011/Kebayoran-Lama-Utara-004-705315_2/embed.html?proto=hls"),
]
# -----------------------------

APP_TITLE = "Realtime Indonesua CCTV Scraper By ( Rolandino )"

# This Is Roland !
def clear():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception:
        pass

# This Is Roland !
def ukuran_terminal():
    try:
        t = shutil.get_terminal_size(fallback=(80, 24))
        return t.columns, t.lines
    except Exception:
        return 80, 24

# This Is Roland !
def _hapus_ansi(s: str) -> str:
    import re
    ansi = re.compile(r"\x1b\[[0-9;]*m")
    return ansi.sub("", s)

# This Is Roland ! 
def cetak_tengah(baris: List[str]):
    cols, lines = ukuran_terminal()
    tinggi = len(baris)
    top_pad = max((lines - tinggi) // 2, 0)
    clear()
    for _ in range(top_pad):
        print()
    for b in baris:
        visible = _hapus_ansi(b)
        pad = max((cols - len(visible)) // 2, 0)
        print(" " * pad + b)

# This Is Roland !
def tampilkan_banner():
    if os.path.exists("banner.txt"):
        try:
            with open("banner.txt", "r", encoding="utf-8", errors="ignore") as f:
                lines = [line.rstrip("\n") for line in f]
            
            for ln in lines:
                cetak_tengah([H + ln + R])
                
            print()
        except Exception:
            pass

# This Is Roland !
def tampilkan_menu_tengah():
    baris: List[str] = []
    baris.append("")
    baris.append(H + APP_TITLE + R)
    baris.append("")
    baris.append(H + "Total 50 Entry ( jakcctv.jakarta.go.id )" + R)
    baris.append("")
    baris.append(H + "" + R)
    for i, (label, _) in enumerate(DAFTAR_CCTV, start=1):
        baris.append(H + f"{i}. {label}" + R)
    baris.append(H + "0. Keluar" + R)
    baris.append("")
    cetak_tengah(baris)

# This Is Roland !
def buka_browser_fallback(url: str) -> bool:
    url = url.strip()
    if not url:
        return False
    if shutil.which("termux-open"):
        try:
            subprocess.Popen(["termux-open", url])
            return True
        except Exception:
            pass
    if shutil.which("am"):
        try:
            
            rc = subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if rc.returncode == 0:
                return True
        except Exception:
            pass
    
    if shutil.which("xdg-open"):
        try:
            rc = subprocess.Popen(["xdg-open", url])
            return True
        except Exception:
            pass
    
    try:
        opened = webbrowser.open_new_tab(url)
        if opened:
            return True
    except Exception:
        pass
    return False

# This Is Roland !
def animasi_buka(url: str):
    clear()
    teks_status = [
        "Inisialisasi Koneksi ✓",
        "Membuka Protokol Streaming ✓",
        "Autentikasi Server ✓",
        "Menjalin Koneksi ✓",
        "Mempersiapkan Browser ✓"
    ]
    
    for s in teks_status:
        cetak_tengah([H + s + R])
        time.sleep(0.45)

    
    sukses = buka_browser_fallback(url)

    
    if sukses:
        cetak_tengah([H + "Browser Berhasil Dibuka Harap Tunggu !" + R])
    else:
        cetak_tengah([H + "Gagal Membuka Browser,Silakan Buka Manual : " + R, H + url + R])
    time.sleep(1.5)

# This Is Roland
def main():
    while True:
        clear()
        tampilkan_banner()
        tampilkan_menu_tengah()
        try:
            jawaban = input(H + "\nPilih Nomor : " + R).strip()
        except (EOFError, KeyboardInterrupt):
            clear()
            cetak_tengah([H + "Berhasil Keluar" + R])
            sys.exit(0)

        if not jawaban:
            continue

        if jawaban.lower() in ("q", "quit", "exit"):
            clear()
            cetak_tengah([H + "Berhasil Keluar" + R])
            sys.exit(0)

        if not jawaban.isdigit():
            cetak_tengah([H + "Pilih Yang Benar !" + R])
            time.sleep(1.0)
            continue

        pilih = int(jawaban)
        if pilih == 0:
            clear()
            cetak_tengah([H + "Terimakasih Telah Menggunakan Program Script Ini :)" + R])
            time.sleep(1.0)
            sys.exit(0)

        if 1 <= pilih <= len(DAFTAR_CCTV):
            label, url = DAFTAR_CCTV[pilih - 1]
            cetak_tengah([H + f"Membuka CCTV : {label}" + R])
            time.sleep(0.6)
            animasi_buka(url)
            
            try:
                input(H + "\nEnter Untuk Kembali Ke Menu" + R)
            except (EOFError, KeyboardInterrupt):
                pass
        else:
            cetak_tengah([H + "Pilih Yang Benar !" + R])
            time.sleep(1.0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        cetak_tengah([H + "\nDihentikan Oleh Pengguna !" + R])
        sys.exit(0)
