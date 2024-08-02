import streamlit as st

from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="HofeliT",
    page_icon="logo.png"
)
st.header("Welcome Home Gais")

logo = "logo.png"  
st.image(logo,use_column_width="auto",width=200)
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options =["Home","How To Use","About Us"],
        icons=['house-door','hand-index','people-fill'],
        default_index =0,
        orientation = "horizontal",
        styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "19px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#3FBAD8"},
            },
        )
    return selected

menu = streamlit_menu()

if menu == "Home":
    def home_page ():
        st.header("Apa itu Mental Health ?")
        st.markdown("""<div style="text-align: justify;">Mental Health adalah keadaan dimana individu memiliki kemampuan untuk berkembang secara fisik, 
                    mental, spiritual, dan sosial sehingga dapat mengetahui kemampuan diri, dapat menghadapi tantangan hidup, 
                    dapat belajar dan melakukan pekerjaan dengan baik, dan dapat memberikan kontribusi bagi masyarakat sekitar.</div>""", unsafe_allow_html=True)
        st.write(""" """)
        st.markdown("""<div style="text-align: justify;">Perlu Anda ketahui bahwa peristiwa dalam hidup yang berdampak besar pada kepribadian 
                    dan perilaku seseorang bisa berpengaruh pada kesehatan mentalnya. Akan tetapi, masalah kesehatan mental bisa mengubah cara seseorang dalam mengatasi stres,
                    berhubungan dengan orang lain, membuat pilihan, dan memicu hasrat untuk menyakiti diri sendiri.</div>""", unsafe_allow_html=True)
        st.write(""" """)
        st.header("Gangguan Mental Health")
        st.markdown(""" 
                    Beberapa jenis gangguan mental yang umum terjadi antara lain:

                    1. Depresi.
                    
                    2. Gangguan bipolar.
                    
                    3. Kecemasan. 
                    
                    4. Gangguan stres pasca trauma (PTSD)
                    
                    5. Gangguan obsesif kompulsif (OCD)
                    
                    6. Psikosis.

        """)
        st.write(""" """)
        st.header("Penyebab dan Gejala Gangguan Mental Health")
        st.subheader("A. Penyebab")
        st.markdown(""" 
                    Ada beberapa kondisi yang bisa menjadi penyebab seseorang mengalami gangguan mental health, antara lain:
                    
                    1. Faktor genetik atau terdapat riwayat pengidap gangguan kesehatan jiwa dalam keluarga.
                        
                    2. Kekerasan dalam rumah tangga atau bentuk pelecehan lainnya.
                        
                    3. Adanya riwayat kekerasan saat kanak-kanak.
                        
                    4.  Mengalami diskriminasi dan stigma.
                        
                    5. Kehilangan atau kematian seseorang yang sangat dekat.
                        
                    DLL
        """)
        st.subheader("B. Gejala")
        st.markdown("""
                    Gejala umum dari kelainan kesehatan ini yang bisa kamu kenali antara lain:

                    1. Berteriak atau berkelahi dengan keluarga dan teman-teman.

                    2. Delusi, paranoia, atau halusinasi.

                    3. Kehilangan kemampuan untuk berkonsentrasi.

                    4. Ketakutan, kekhawatiran, atau perasaan bersalah yang selalu menghantui.

                    5. Ketidakmampuan untuk mengatasi stres atau masalah sehari-hari.

                    6. Marah berlebihan dan rentan melakukan kekerasan.

                    7. Memiliki pengalaman dan kenangan buruk yang tidak dapat dilupakan.

                    8. Adanya pikiran untuk menyakiti diri sendiri atau orang lain.

                    9. Menarik diri dari orang-orang dan kegiatan sehari-hari.
                    
                    10. Menunjukkan perubahan suasana hati secara mendadak yang menyebabkan masalah dalam hubungan dengan orang lain.

                    11. Merasa bingung, pelupa, marah, tersinggung, cemas, kesal, khawatir, dan takut yang tidak biasa.

                    12. Perasaan sedih, tidak berarti, tidak berdaya, putus asa, atau tanpa harapan.
        """)
        st.write(""" """)
        st.header("Penanganan Gangguan Mental Health dan Tips Menjaga Mental Health")
        st.markdown(""" 
                    1. Psikoterapi
                    
        Penanganan dengan psikoterapi merupakan jenis terapi dengan media yang aman untuk mengungkapkan perasaan dan memberikan saran yang sesuai.
        Dalam situasi ini, psikiater akan memberi bantuan dengan membimbing pengidap dalam mengontrol perasaan.

    2. Perawatan Intensif di Rumah Sakit
                        
        Dokter dan ahli kejiwaan akan menyarankan rawat inap jika pengidap membutuhkan pemantauan ketat terhadap gejala masalah kesehatan jiwa yang dialami.

    3. Supporting group
                        
        Support group umumnya memiliki anggota pengidap penyakit kesehatan mental yang sejenis atau mereka yang sudah dapat mengendalikan emosinya dengan baik.
    4. Perhatikan Kesehatan Fisik & Pola Makan
                        
        Kesehatan fisik dan kesehatan mental saling terkait. Pastikan Anda menjaga pola makan seimbang, berolahraga secara teratur, dan tidur cukup. Tubuh yang sehat akan membantu Anda menghadapi stres dengan lebih baik.

    5.	Jangan Takut Mencari Bantuan
                        
        Jika Anda merasa kesulitan atau merasa terlalu cemas, jangan ragu untuk mencari bantuan dari konselor kampus atau profesional kesehatan mental. Banyak perguruan tinggi menawarkan layanan kesehatan mental gratis atau dengan biaya yang terjangkau.

    6.	Atur Batas Diri dan Harapan Yang Realistis

        Ingatlah bahwa tidak ada yang sempurna. Atur harapan yang realistis untuk diri sendiri dalam hal akademik, sosial, dan emosional. Jangan terlalu keras pada diri sendiri jika terjadi hambatan atau kegagalan. Jalani aktivitas sesuai kemampuan Anda !

    7.	Luangkan Me Time Agar Lebih Rileks
                        
        Meluangkan me time secara teratur supaya lebih rileks dan terhindar dari stres. Anda bisa melakukan hobi atau aktivitas yang santai seperti meditasi, yoga, seni, hangout atau aktivitas lain. Waktu untuk merilekskan diri adalah investasi untuk menjaga kesehatan mental lho!

    8.	Bersosialisasi & Menjalin Relasi
                        
        Berinteraksilah dengan orang-orang di sekitar Anda. Temukan kesempatan untuk bergabung dengan klub, organisasi mahasiswa, atau acara kampus. Bersosialisasi dapat membantumu merasa lebih terhubung dengan lingkungan kampus, menjalin relasi dengan banyak kenalan baru, serta mewujudkan ide dengan cara yang positif.
""")
    home_page()


elif menu == "About Us":
    def about_page():
        st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        # Kemas
        st.subheader("Kemas Veriandra Ramadhan")
        st.image("kemas.jpg", width=300, caption="Kemsky")
        st.markdown(""" 
                    Sebagai : Lead Project

                    Fun Fact : Makannya cepet, kayak dikejar hutang

                    Motto Hidup : do it like you dream it

                    """)
        st.write(" ")
        st.write(" ")
        # Reynaldi
        st.subheader("Reynaldi Rahmad")
        st.image("Rey.jpg", width=300, caption="rey/wir")
        st.markdown(""" 
                    Sebagai : Editor

                    Fun Fact : Suka vlog masak

                    Motto Hidup : Makin gede makin yaudah

                    """)
        st.write(" ")
        st.write(" ")
        st.subheader("Khaalishah Zuhrah Alyaa Vanefi")
        st.image("Alya.jpg", width=300, caption="al/panepoy")
        st.markdown("""
                    Sebagai : Desainer

                    Fun fact : Cantik

                    Motto Hidup : it will pass

                    """)
        st.write(" ")
        st.write(" ")
        # Tessa
        st.subheader("Tessa Kania Sagala")
        st.image("Tessa.jpg", width=300, caption="tes")
        st.markdown(""" 
                    Sebagai : Writer

                    Funfact : Menghindari tontonan dan bacaan yang sad ending

                    Motto Hidup : think before you act

                    """)
    about_page()


elif menu == "How To Use":
    def How_to_Use():
        st.write(""" """)
        st.write()
        st.header("Apa itu HofeliT ?")
        st.markdown("""<div style="text-align: justify;">Apakah Anda tahu? 1 dari 5 anak-anak dan remaja di dunia mengidap gangguan jiwa? 
                    dan apakah anda tahu bahwa 1 dari 9 orang yang tinggal di lingkugan penuh akan konflik memilki 
                    gangguan kejiwaan sedang hingga berat? dengan pernyataan yang telah disebutkan, 
                    membuat pertanyaa apakah hal tersebut dapat dikurangi atau bahkan dapat dihindari, 
                    sehingga kejadian seperti pernyataan diatas tidak terjadi pada Anda. Dengan itu hadirlah Hofelit untuk membantu mengatasi seputar kesehatan mental yang Anda alami.</div>""", unsafe_allow_html=True)
        st.write(""" """)
        st.markdown("""<div style="text-align: justify;">Hofelit dibuat untuk mengetahui rate tentang keadaan mental health Anda. 
                    Hadirnya Hofelit diharapkan membantu Anda untuk memeriksa bagaimana, kesehatan mental yang selama ini teman-teman rasakan.</div>""", unsafe_allow_html=True)
        st.write(""" """)
        st.markdown("""<div style="text-align: justify;">Maka dari itu kami mengembangkan sistem untuk mengetahui sejauh mana keadaan mental health Anda. 
                    Dengan begitu poin yang telah dikumpulkan setelah menjawab pertanyaan, akan menjadi acuan untuk mengambil 
                    keputusan terhadap keadaan mental health Anda.</div>""", unsafe_allow_html=True)
        st.write(""" """)
        st.markdown("""
                    
                    Selain itu Hofelit juga memiliki hal unik di dalamnya, seperti 
                    1. Bergabung dengan diskusi komunitas

                    2. Membuat Memo dimana teman-teman dapat menuliskan apa saja yang teman-teman resahkan selama ini.
                    """)
        st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
        st.markdown("<h1 class='centered-title'>Cara Menggunakan HofeliT</h1>", unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify;">1. Klik tombol panah pada bagian kiri atas, kemudian tekan Login Page untuk masuk.</div>', unsafe_allow_html=True)
        st.image("o11.jpg")
        st.image("o1.jpg", caption="Step 1")
        st.write("")

        st.markdown('<div style="text-align: justify;">2. Apabila belum mempunyai akun, buat akun terlebih dahulu. Pilih menu Registrasi jika belum memiliki akun. Isi data yang diperlukan.</div>', unsafe_allow_html=True)
        st.image("o1.jpg", caption="Step 2")
        st.write("")

        st.markdown('<div style="text-align: justify;">3. Ketika selesai mengisi data tekan tombol registrasi untuk membuat akun. Tunggu Nontifikasi hijau muncul.</div>', unsafe_allow_html=True)
        st.image("o3.jpg", caption="Step 3")
        st.write("")
        
        st.markdown('<div style="text-align: justify;">4. Pilih menu Masuk,  kemudian masukkan Username dan Password yang telah dibuat.</div>', unsafe_allow_html=True)
        st.image("o4.jpg", caption="Step 4")
        st.write("")

        st.markdown('<div style="text-align: justify;">5. Setelah tampilan User Page muncul Quiz Page, Comunnity Page, dan Memo Page dapat digunakan. Ingat! ketiga page tersebut dapat diakses setelah berhasil masuk ke User Page .</div>', unsafe_allow_html=True)
        st.image("o5.jpg", caption="Step 5")
        st.write("")

        st.markdown('<div style="text-align: justify;">6. Tekan tombol Quiz Page pada sisi kiri untuk memulai quiz.</div>', unsafe_allow_html=True)
        st.image("o6.jpg", caption="Step 6")
        st.write("")

        st.markdown('<div style="text-align: justify;">7. Setelah mengisi jawaban dari soal yang diberikan, tekan tombol submit untuk melihat hasil akhir. Hasil akhir bisa dilihat dengan 2 output, yaitu Paramter dan saran. Untuk mengganti output tekan output yang diinginkan. Ketika berganti output, pastikan tombol submit ditekan kembali untuk melihat hasilnya.</div>', unsafe_allow_html=True)
        st.image("o71.jpg")
        st.image("o72.jpg",caption='Step 7')
        st.write("")

        st.markdown('<div style="text-align: justify;">8. Ketika sudah selesai menggunakan Hofelit, kembali ke Login Page lalu tekan tombol Keluar untuk keluar dari akun yang digunakan.</div>', unsafe_allow_html=True)
        st.image("o8.jpg", caption="Step3")
        st.write("")
    How_to_Use()
        