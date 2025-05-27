# PDF'den PNG'ye Dönüştürücü

Bu Python betiği, bir PDF dosyasını seçmenize ve her sayfasını ayrı PNG dosyaları olarak kaydetmenize olanak tanır.

## 📜 Açıklama

Betik, kullanıcıdan bir PDF dosyası seçmesini isteyen bir grafik arayüz (GUI) penceresi açar. Seçilen PDF dosyasının her sayfası, orijinal PDF dosyasının bulunduğu dizine `sayfa_XXXX.png` formatında (örneğin, `sayfa_0001.png`, `sayfa_0002.png`) PNG dosyaları olarak kaydedilir.

## ⚙️ Gereksinimler

Bu betiğin çalışması için aşağıdaki Python kütüphanelerine ve harici bir araca ihtiyacınız vardır:

* **Python 3.x**
* **pdf2image**: PDF dosyalarını resim formatlarına dönüştürmek için kullanılır.
* **Pillow**: `pdf2image` kütüphanesinin bir bağımlılığıdır ve resim işleme için kullanılır.
* **Tkinter**: Python'un standart GUI kütüphanesidir. Genellikle Python ile birlikte gelir, ancak bazı sistemlerde ayrıca kurulması gerekebilir (örneğin, Linux'ta `python3-tk` paketi).
* **Poppler**: `pdf2image` kütüphanesinin PDF dosyalarını işleyebilmesi için gereklidir. Sisteminizde kurulu olmalıdır.

## 🛠️ Kurulum

1.  **Python 3.x Sürümünü Edinin:**
    Eğer sisteminizde Python 3 yüklü değilse, [python.org](https://www.python.org/downloads/) adresinden indirip kurun.

2.  **Poppler Kurulumu:**
    * **Windows:**
        1.  [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/) adresinden en son sürümü indirin.
        2.  Arşivi bir klasöre (örneğin, `C:\Program Files\poppler-23.08.0`) çıkarın.
        3.  Poppler'ın `bin` klasörünü (örneğin, `C:\Program Files\poppler-23.08.0\bin`) sisteminizin PATH ortam değişkenine ekleyin.
    * **macOS (Homebrew ile):**
        ```bash
        brew install poppler
        ```
    * **Linux (apt ile - Debian/Ubuntu tabanlı sistemler):**
        ```bash
        sudo apt-get update
        sudo apt-get install poppler-utils
        ```
    * **Linux (yum ile - Fedora/CentOS tabanlı sistemler):**
        ```bash
        sudo yum install poppler-utils
        ```

3.  **Gerekli Python Kütüphanelerini Kurun:**
    Terminal veya komut istemcisini açın ve aşağıdaki komutu çalıştırın:
    ```bash
    pip install pdf2image Pillow
    ```
    Eğer sisteminizde `tkinter` eksikse (genellikle Linux'ta karşılaşılır):
    ```bash
    sudo apt-get install python3-tk # Debian/Ubuntu için
    # Diğer dağıtımlar için uygun paket yöneticisi komutunu kullanın.
    ```

## 🚀 Kullanım

1.  Betiği (`.py` uzantılı dosya) bilgisayarınıza kaydedin.
2.  Terminal veya komut istemcisini açın ve betiğin bulunduğu dizine gidin.
3.  Aşağıdaki komutu çalıştırarak betiği başlatın:
    ```bash
    python dosya_adiniz.py
    ```
    (Burada `dosya_adiniz.py`, betiği kaydettiğiniz dosyanın adıdır.)
4.  Bir dosya seçme penceresi açılacaktır. Dönüştürmek istediğiniz PDF dosyasını seçin ve "Aç" düğmesine tıklayın.
5.  Betik, PDF dosyasını işlemeye başlayacak ve her sayfayı PNG formatında kaydedecektir. İşlem tamamlandığında konsolda bilgi mesajları görüntülenecektir.

## 🖼️ Çıktı

Dönüştürülen PNG dosyaları, orijinal PDF dosyasının bulunduğu klasöre aşağıdaki gibi bir isimlendirme şemasıyla kaydedilecektir:
* `sayfa_0001.png`
* `sayfa_0002.png`
* ...ve benzeri.
