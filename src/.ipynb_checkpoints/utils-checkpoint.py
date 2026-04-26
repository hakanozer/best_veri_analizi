from pathlib import Path
import pandas as pd
import sys

# Hücre 1 — Kütüphaneleri kontrol et
print(f"Python versiyonu: {sys.version}")

# Hücre 2 — Basit hesap
fiyat = 150.0
adet = 3
toplam = fiyat * adet
print(f"Toplam tutar: {toplam} TL")