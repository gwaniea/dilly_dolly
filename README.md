# dilly_dolly

PWS : http://fakhriyah-ghania-dillydolly.pbp.cs.ui.ac.id/

Pertanyaan :
# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab : 
1) Membuat sebuah proyek Django baru
- Langkah pertama adalah melakukan inisiasi repositori di Github yang saya namakan dilly_dolly dan mengatur repo menjadi public serta menambahkan berkas README.md saat ingin membuat repo sebagai tempat untuk menjawab pertanyaan.
- Setelah itu, saya melakukan cloning ke komputer lokal dengan cara menggunakan command prompt pada direktori lokal yang nantinya akan menjadi direktori utama proyek ini. Saya menjalankan perintah git clone https://github.com/gwaniea/dilly_dolly.git untuk menduplikasi seluruh repo ke komputer lokal.
- Selanjutnya, saya membuka command prompt pada direktori dilly_dolly yang sudah saya clone dari Github dan membuat virtual environment dengan perintah python -m venv env lalu mengaktifkannya dengan perintah env\Scripts\activate. Tujuan dari virtual environment ini untuk mengisolasi package dan dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada di komputer lokal. Mengaktifkan virtual environment berarti membuat ruang kerja terpisah di mana saya dapat menginstal package dan dependencies tanpa memengaruhi proyek lainnya yang ada di komputer saya.
- Kemudian, saya membuat file requirements.txt di dalam direktori tersebut dan menambahkan beberapa dependencies (seperti yang ada di tutorial 0). Saya melakukan instalasi terhadap dependencies dengan perintah pip install -r requirements.txt.
- Selanjutnya, saya membuat proyek Django bernama dilly_dolly dengan perintah django-admin startproject dilly_dolly . (setelah perintah ini, akan terdapat direktori baru bernama dilly_dolly di dalam direktori utama)
- Setelah itu, saya menambahkan "localhost" dan "127.0.0.1" pada ALLOWED_HOSTS di settings.py (settings.py ada di dalam direktori proyek dilly_dolly) untuk memberikan izin akses dari host lokal. Untuk menandakan berhasil atau tidaknya aplikasi Django dibuat, saya menjalankan perintah python manage.py runserver dan membuka http://localhost:8000/ dan melihat animasi roket (aplikasi Django berhasil dibuat)
- Selanjutnya, saya menambahkan berkas .gitignore pada direktori utama yang isinya adalah berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git.
- Terakhir, saya melakukan add, commit, dan push dari direktori repo lokal.
2) Membuat aplikasi dengan nama main pada proyek tersebut.
- Sebelum membuat aplikasi main, saya memastikan bahwa virtual environment dalam keadaan aktif terlebih dahulu. Selanjutnya, saya menjalankan perintah python manage.py startapp main untuk membuat aplikasi main (setelah ini, direktori baru bernama main yang isinya adalah struktur awal aplikasi Django akan terbentuk)
- Kemudian, saya menambahkan aplikasi main ke dalam daftar aplikasi INSTALLED_APPS di settings.py (settings.py ada di dalam direktori proyek dilly_dolly)
3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Pertama, saya menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan aplikasi main. Dalam file urls.py pada direktori proyek dilly_dolly, saya mengimpor fungsi include dari django.urls dan menambahkan rute URL, yaitu path('', include('main.urls')), untuk mengarahkan ke tampilan main. Fungsi include digunakan untuk impor rute URL dari aplikasi lain ke dalam file urls.py proyek.
4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, dan description.
- Pertama, saya membuka berkas models.py pada direktori aplikasi main.
- Saya mengisi model dengan kode berikut :

from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255) 
    price = models.IntegerField()             
    description = models.TextField()
    category = models.CharField(max_length=255,  default='Uncategorized')
    stock = models.IntegerField(default=0)

Kode ini merepresentasikan tabel di database. Setiap atribut dalam kelas ini akan menjadi kolom di tabel database yang sesuai dan masing-masing baris di tabel akan mewakili satu entri produk. Berikut detailnya :
- name: Nama produk dengan panjang maksimal 255 karakter.
- price: Harga produk yang disimpan sebagai bilangan bulat.
- description: Deskripsi produk yang panjangnya tidak terbatas.
- category: Kategori produk dengan nilai default "Uncategorized" jika tidak diisi. (atribut tambahan)
- stock: Jumlah stok produk dengan nilai default 0 jika tidak diisi. (atribut tambahan)

- Selanjutnya, saya melakukan migrasi model dengan menjalankan perintah python manage.py makemigrations untuk membuat berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam database. Kemudian, saya menjalankan perintah python manage.py migrate untuk menerapkan perubahan model.
5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
- Pertama, saya membuka berkas views.py pada direktori aplikasi main.

- Kemudian, saya menambahkan fungsi berikut :

def show_main(request):
    context = {
        'app': 'Dilly Dolly',  
        'nama': 'Fakhriyah Ghania Putri',  
        'kelas': 'PBP B' 
    }

    return render(request, "main.html", context)

Kode ini untuk mendefinisikan fungsi show_main yang menerima parameter request. Fungsi ini akan memproses request yang masuk dari pengguna, lalu mengirimkan data ke template untuk ditampilkan. Data ini memuat informasi app, nama, dan kelas.
6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Pertama, saya membuat berkas urls.py di dalam direktori main untuk mengatur rute URL terkait aplikasi main. Saya mengimpor path dari django.urls untuk menentukan pola URL dan mengaitkannya dengan tampilan fungsi show_main dari main.views. Ketika URL diakses, maka web akan menampilkan fungsi show_main pada views.py yang sudah didefinisikan sebelumnya. Selain itu, saya juga mendefinisikan variabel app_name (isinya 'main') untuk menentukan nama unik untuk pola URL yang ada di aplikasi tersebut supaya tidak bertabrakan dengan aplikasi lain yang memiliki pola URL yang sama.
7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Saya membuat proyek baru dengan menekan tombol Create New Project. Kemudian, saya mengisi Project Name dengan dillydolly dan menekan tombol Create New Project.
- Selanjutnya, pada settings.py di proyek Django, saya menambahkan URL Deployment PWS pada ALLOWED_HOST. Sekarang ALLOWED_HOST saya terlihat seperti ini:

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "fakhriyah-ghania-dillydolly.pbp.cs.ui.ac.id"]

- Setelah itu, saya melakukan git add, commit, dan push.
- Selanjutnya, saya menjalankan perintah yang terdapat pada informasi Project Command PWS. Kemudian, saya menjalankan perintah git branch -M main untuk mengubah nama branch utama menjadi main kembali. Setiap ada perubahan, seperti menambahkan atribut pada model, saya melakukan migrasi (khusus perubahan pada model) dan push ke PWS dengan perintah git push pws main:master.
8) Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
- Saya telah membuat berkas README.md saat membuat repositori baru. Isinya adalah jawaban dari pertanyaan beserta link PWS.

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
![alt text](bagan.jpg)

# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawab:
Fungsi Git adalah untuk melacak perubahan dalam kode selama pengembangan proyek. Git dapat melacak setiap perubahan dalam kode dari waktu ke waktu sehingga pengguna dapat melihat riwayat semua perubahan yang terjadi pada kode. Selain itu, Git juga mendukung kolaborasi tim tanpa mengganggu pekerjaan masing-masing. Setiap anggota tim dapat mengerjakan bagiannya masing-masing, lalu menggabungkannya. Git juga dapat menjadi backup karena sistemnya yang terdistribusi. Ini berarti developer memiliki salinan dari seluruh riwayat proyeknya. Selain itu, Git berfungsi untuk memudahkan proses pengembangan dan maintenance perangkat lunak akibat adanya tools CI/CD untuk melakukan build, test, integrate, deliver, dan deploy secara otomatis.

# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab:
Menurut saya, Django praktis karena pengguna tidak perlu membangun semuanya dari awal. Banyak tools yang disediakan dari framework ini, seperti routing dan lainnya, sehingga memudahkan pengguna dalam membangun web. Struktur Django juga cukup beginner-friendly sehingga saya bisa memahami bagaimana aplikasi web dibangun secara terpisah (models, views, templates). 

# 5. Mengapa model pada Django disebut sebagai ORM?
Jawab: 
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django memetakan objek-objek dalam models ke dalam tabel-tabel database. Misalnya, dalam models.py, terdapat atribut name, price, description, category, dan stock, kemudian ORM akan menerjemahkan model tersebut ke dalam tabel database dengan kolom dan baris yang sesuai. 