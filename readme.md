# ANGGOTA KELOMPOK <BR> PUJHA SURETNO G1F022051<BR> MUHAMMAD RAFLY ALFARIZY G1F022067 <BR> FARHAN NERO PRATAMA G1F022063
# Laporan UAS PBO
# BAB I
## Landasan Teori


### **1.1. Python**

<p align="justify">
&emsp;Python merupakan bahasa pemrograman komputer yang biasa dipakai untuk membangun situs, software/aplikasi, mengotomatiskan tugas dan melakukan analisis data. Bahasa pemrograman ini termasuk bahasa tujuan umum. Artinya, ia bisa digunakan untuk membuat berbagai program berbeda, bukan khusus untuk masalah tertentu saja.Karena sifatnya yang serba guna dan mudah digunakan, ia menjadi bahasa pemrograman yang paling banyak digunakan. Terutama untuk mereka yang masih pemula.Berdasarkan survei pengembang Stack Overflow tahun 2022, Python menjadi bahasa pemrograman terpopuler keempat. Sebanyak hampir 50% dari responden mengatakan bahwa mereka menggunakan hampir setengah dari waktu kerja mereka dengan menggunakan bahasa pemrograman ini.Nama Python sendiri berasal dari Monty Python. Ketika Guido van Rossum membuatnya, dia juga sedang membaca skrip Sirkus Terbang Monty Python BBC. Menurutnya nama itu singkat dan sedikit misterius. Karena itulah, sang kreator memilih menggunakan nama tersebut untuk bahasa pemrograman yang dibuatnya itu. Python telah menjadi andalan dalam ilmu data. Bahasa pemrograman ini memungkinkan analisis data untuk melakukan perhitungan statistik yang rumit, membuat visualisasi data serta algoritma machine learning. Ia juga bisa digunakan untuk memanipulasi, menganalisis data, dan menyelesaikan berbagai tugas lain terkait data. Dan dapat dikatakan Python adalah bahasa pemrograman yang sangat serbaguna. Bahasa ini dapat digunakan dalam berbagai bidang seperti data science, machine learning, web development, dan banyak lagi. Python juga memiliki banyak pustaka dan framework yang memudahkan dalam mengembangkan aplikasi.
</p>

**- Kelebihan Python**
1.	Mudah dipelajari, sintaksnya cukup sederhana dan mudah dimengerti
2.	Mudah diaplikasikan dalam mengembangkan produk
3.	Mendukung IoT (Internet of Things)
4.	Fleksibel, dapat diintegrasikan dengan aplikasi yang ditulis dalam bahasa pemrograman lain
5.	Meningkatkan produktivitas dikarenakan memiliki banyak library dan desain berorientasi objek yang bersih
6.	Bersifat open source dan free sehingga dapat diunduh secara gratis dan tidak perlu membeli lisensi


**- Kekurang Python**

1.	Kurangnya dukungan multiprosesor sehingga dapat membatasi penulisan kode
2.	Lebih sedikit developers yang berpengalaman melakukan pekerjaan menggunakan bahasa python
3.	Tidak ideal untuk memory intensive task dikarenakan menghasilkan konsumsi memori yang cukup tinggi
4.	Kurang populer untuk mobile app development
5.	Memiliki banyak batasan desain dikarenakan python diketik secara dinamis
6.	Kecepatan yang lebih lambat dibandingkan dengan bahasa pemrograman lainnya

### **1.2. Object Oriented Programming (OOP)**

<p align="justify">
&emsp;Pemrograman berorientasi objek atau object oriented programming adalah suatu cara baru dalam berpikir serta berlogika dalam menghadapi masalah- masalah yang akan dicoba mengatasi dengan bantuan komputer. Filosofi OOP menciptakan sinergi luar biasa sepanjang siklus pengembangan perangkat lunak (perencanaan, analisis, perancangan, serta implementasi) sehingga dapat diterapkan pada perancangan sistem secara umum menyangkut perangkat lunak, perangkat keras, serta sistem informasi secara keseluruhan. Berorientasi objek atau object oriented merupakan paradigma baru dalam rekayasa perangkat lunak yang memandang sistem sebagai kumpulan objek-objek diskrit yang saling berinteraksi. Yang dimaksud dengan berorientasi objek adalah bahwa mengorganisasikan perangkat lunak sebagai kumpulan objek-objek diskrit yang bekerja sama antara informasi atau struktur data dan perilakau (behavior) yang mengaturnya. Konsep OOP bertujuan untuk meningkatkan efisiensi dan keberlanjutan dalam pengembangan perangkat lunak melalui modularitas, memecah program menjadi objek dan kelas yang dapat dikelola secara terpisah. Dengan memberikan kemampuan reusabilitas, OOP memungkinkan penggunaan kembali kelas atau objek yang sudah ada, mengurangi kerja ulang dan mempercepat pengembangan perangkat lunak baru. Fleksibilitas dicapai dengan menggunakan pewarisan dan polimorfisme, memungkinkan penyesuaian dan perubahan dengan mudah. Konsep enkapsulasi membantu dalam memudahkan pemeliharaan dengan menyembunyikan detail implementasi dan fokus pada antarmuka yang terdefinisi dengan jelas. Dengan mendukung pengembangan yang cepat, OOP memfasilitasi kerja tim pengembang yang dapat bekerja secara terpisah pada bagian-bagian yang berbeda dari program. Selain itu, OOP membantu memodelkan struktur dunia nyata dengan lebih baik, mencerminkan hubungan dan sifat objek-objek dalam program. Tingkat keamanan ditingkatkan melalui enkapsulasi, dan landasan untuk skala besar terwujud melalui kemudahan pengelolaan kompleksitas dengan prinsip OOP.
</p>

# BAB II
## Soal dan Pembahasan

### **2.1. Soal**
1. Untuk memburamkan gambar menggunakan Python: Dengan bantuan kernel filter low pass yang berbeda, ini membuat gambar menjadi kurang jelas atau berbeda dan membuat gambar halus.

### **2.2. Pembahasan**

**Source Code :**
```
import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        self.blurred_img = None

    def apply_gaussian_blur(self, kernel_size=(15, 15)):
        self.blurred_img = cv2.GaussianBlur(self.img, kernel_size, 0)

    def show_image(self, window_name='Blurred Image'):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, self.img.shape[1], self.img.shape[0])

        if self.blurred_img is not None:
            cv2.imshow(window_name, self.blurred_img)
        else:
            print("Error: Gaussian blur not applied. Call apply_gaussian_blur() first.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Contoh penggunaan
if __name__ == "__main__":
    image_processor = ImageProcessor('Tailung.png')
    image_processor.apply_gaussian_blur()

    # Menampilkan citra yang telah di-blur
    image_processor.show_image('Blurred Image')
```

**Luaran Yang Dihasilkan :**

- Gambar Sebelum Dilakukan Blur :

![alt text](GoYoonJung.jpeg?raw=true)

- Gambar Sesudah Dilakukan Blur :

![alt text](GoYoonJungBlur.png?raw=true)

**Penjelasan Kode :**

**1. Import Library**
```
import cv2 import 
numpy as npm
```
<p align="justify">
&emsp;Kode mengimport dua library, yaitu OpenCV (cv2) untuk pemrosesan gambar dan NumPy (np) untuk manipulasi array.
</p>

**2. Constructor (__init__) :**
```
def __init__(self, image_path):
    self.image_path = image_path
    self.img = cv2.imread(image_path)
    self.blurred_img = None
```
<p align="justify">
&emsp;Konstruktor inisialisasi objek ImageProcessor dengan path gambar (image_path), membaca gambar menggunakan OpenCV, dan menginisialisasi atribut blurred_img menjadi None.
</p>

**3. Method apply_gaussian_blur :**
```
def apply_gaussian_blur(self, kernel_size=(15, 15), resize_factor=0.5):
    resized_img = cv2.resize(self.img, None, fx=resize_factor, fy=resize_factor)
    self.blurred_img = cv2.GaussianBlur(resized_img, kernel_size, 0)
```
<p align="justify">
&emsp;Method ini mengaplikasikan Gaussian Blur ke gambar. Prosesnya melibatkan pengubahan resolusi gambar dengan faktor tertentu (resize_factor) dan kemudian mengaplikasikan Gaussian Blur dengan ukuran kernel yang diberikan (kernel_size).
</p>

**4. Method show_image :**
```
def show_image(self, window_name='Blurred Image'):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, self.blurred_img.shape[1], self.blurred_img.shape[0])

    if self.blurred_img is not None:
        cv2.imshow(window_name, self.blurred_img)
    else:
        print("Error: Gaussian blur not applied. Call apply_gaussian_blur() first.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
<p align="justify">
&emsp;Method ini menampilkan gambar yang telah diproses dengan Gaussian Blur. Menciptakan jendela dengan nama tertentu (window_name), menyesuaikan ukuran jendela sesuai dengan gambar, dan menampilkan gambar.
</p>

**5. Contoh Penggunaan :**
```
if __name__ == "__main__":
    image_processor = ImageProcessor('GoYoonJung.jpeg')
    image_processor.apply_gaussian_blur(resize_factor=0.5)
    image_processor.show_image('Blurred Image')
```
<p align="justify">
&emsp;Di blok ini, objek ImageProcessor dibuat dengan path gambar 'GoYoonJung.jpeg'. Kemudian, Gaussian Blur diterapkan dengan faktor resize 0.5, dan hasilnya ditampilkan menggunakan show_image.
</p>

# BAB III
## Kesimpulan Dan Saran

### 3.1. Kesimpulan
<p align="justify"> 
&emsp;Python merupakan bahasa pemrograman komputer yang biasa dipakai untuk membangun situs, software/aplikasi, mengotomatiskan tugas dan melakukan analisis data. Bahasa pemrograman ini termasuk bahasa tujuan umum. Dan pada program memburamkan gambar menggunakan phyton: Dengan bantuan kernel filter low pass yang berbeda, ini membuat gambar menjadi kurang jelas atau berbeda dan membuat gambar halus. Teknik ini sering digunakan dalam berbagai aplikasi seperti pengolahan gambar medis, pengolahan citra untuk keperluan grafika komputer, atau untuk meningkatkan kinerja algoritma pengenalan objek dengan menghilangkan noise atau detail yang tidak diinginkan.
</p>

### 3.2. Saran
<p align="justify"> 
&emsp;Untuk meningkatkan program memburamkan gambar menggunakan phyton: Dengan bantuan kernel filter low pass yang berbeda, ini membuat gambar menjadi kurang jelas atau berbeda dan membuat gambar halus. Adalah dengan cara menciptakan fungsi atau loop yang memungkinkan untuk secara interaktif memilih atau mengganti kernel filter low-pass, sehingga program dapat memberikan fleksibilitas yang lebih besar dalam eksplorasi efek pengaburan dengan berbagai jenis kernel, meningkatkan interaktivitas, dan memudahkan eksperimen dengan berbagai tingkat pengaburan dan estetika visual. Namun di balik itu semua perlunya pengerjaan yang matang agar hasilnya sempurna
</p>

# DAFTAR PUSTAKA
<p align="justify"> 
[1] Agnes (2021) “ kelebihan dan kekurangan pada phyton” Dqlab.id. https://dqlab.id/belajar-python-kenali-kelebihan-kekurangan.Diakses pada 16 desember 2023
</p>

<p align="justify"> 
[2] Muhammad Romzi, Kurniawan B.(2020”Pengertian phyton” https://journal.unmaha.ac.id/index.php/jtim/article/view/6 Diakses pada 16 desember 2023
</p>

<p align="justify"> 
[3] MS Hasibuan(2020) “Sejarah Bahasa Pemrograman Python”. https://www.researchgate.net/publication/340536143_Belajar_Phyton_dengan_Singkat. Diakses pada 16 desember 2023
</p>

<p align="justify"> 
[4] Redaksi Jagoan Hosting(2023) “ Pengertian OOP (Object Oriented Programming”. https://www.jagoanhosting.com/blog/oop-adalah/. Diakses pada 16 desember 2023
</p>
