# Proje: Veri Analizi (best_veri_analizi)

```bash
Github Link: https://github.com/hakanozer/best_veri_analizi

Ortam Oluşturma: python -m venv venv
Aktif Etme (Mac): source venv/bin/activate
Aktif Etme (Windows): venv\Scripts\activate
Proje kütüphanelerini kurma: pip install -r requirements.txt

Tek dosya Çalıştırma: python src/utils.py

Jupyter ile çalştırma (Hızlı - Öğrenme):jupyter notebook
# Tarayıcı otomatik açılır: http://localhost:8888
```

Bu proje veri analizi çalışmaları için bir başlangıç şablonudur.

Proje dizin yapısı:
```
├── venv/                  # Sanal ortam (git'e ekleme!)
├── data/
│   ├── raw/               # Ham veriler (değiştirme)
│   └── processed/         # İşlenmiş veriler
├── notebooks/             # Jupyter Notebook dosyaları
│   └── 01_giris.ipynb
├── src/                   # Python modülleri
│   └── utils.py
├── outputs/               # Grafikler ve raporlar
├── requirements.txt       # Bağımlılıklar
└── README.md
```

Hızlı başlangıç:

1. Sanal ortam oluşturun ve aktifleştirin:

```bash
python -m venv venv
source venv/bin/activate
```

2. Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

3. Notebooks klasöründeki `01_giris.ipynb` ile başlayın.

**Çalıştırma ve Geliştirme**

- **Sanal ortam oluşturma ve aktifleştirme:**

```bash
python -m venv venv
source venv/bin/activate
```

- **Bağımlılıkları yükleme:**

```bash
pip install -r requirements.txt
```

- **Python betiği çalıştırma (örnek):**

```bash
python path/to/script.py
# veya modül olarak çalıştırma
python -m path.to.module
```

- **Arka planda çalıştırma ve durdurma:**

```bash
# Arka planda çalıştır
nohup python path/to/script.py &

# Foreground süreci durdurmak için: Ctrl+C

# PID ile durdurma (örnek):
ps aux | grep path/to/script.py
kill <PID>

# veya isimle kapatma
pkill -f path/to/script.py
```

- **Jupyter Notebook / Lab çalıştırma:**

```bash
# Notebooks klasöründe belirli bir dosyayı açmak
jupyter notebook notebooks/01_giris.ipynb
# veya genel arayüz
jupyter lab
```

- **Notebook'u komut satırından çalıştırma (otomatik):**

```bash
jupyter nbconvert --to notebook --execute notebooks/01_giris.ipynb --output executed.ipynb
```

- **Test, biçimlendirme ve kalite kontrol:**

```bash
# Testler
pytest
# Kod formatlama
black .
# Lint
flake8 .
```
