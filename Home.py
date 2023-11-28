import streamlit as st

from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="HofeliT",
    page_icon="logo.png"
)
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
        st.write()
        st.header("Apa itu HofeliT ?")
        st.markdown('<div style="text-align: justify;">Hofelit dibuat untuk mengetahui rate tentang suasana hati. Hadirnya Hofelit diharapkan membantu teman-teman untuk memeriksa bagaimana, kesehatan mental yang selama ini teman-teman rasakan.</div>', unsafe_allow_html=True)
        st.header("Bagaimana Kerja Hofelit ?")
        st.markdown('<div style="text-align: justify;">Hofelit dibuat untuk mencari rate tentang suansana hati, maka dari itu kami mengembangkan sistem untuk mengetahui sejauh mana mental health teman-teman yang akan diukur. Dengan begitu poin yang telah dikumpulkan setelah menjawab pertanyaan, akan menjadi acuan untuk teman-teman mengambil keputusan terhadap mental health teman-teman.</div>', unsafe_allow_html=True)
        st.write(""" """)
        st.markdown("""
                    
                    Selain itu Hofelit juga memiliki hal unik di dalamnya, seperti 
                    1. Bergabung dengan diskusi komunitas

                    2. Membuat Memo dimana teman-teman dapat menuliskan apa saja yang teman-teman resahkan selama ini.
                    """)
        st.header("Noted")
        st.write("Untuk menjawab pertanyaan bagaimana keadaan mental health teman-teman, kami sarankan untuk login (🪪 Login Page )terlebih dahulu. Setelah itu dapat melanjutkan menjawab pertanyaan melalui quiz yang sudah disediakan.")
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
        st.image("rey.jpg", width=300, caption="rey/wir")
        st.markdown(""" 
                    Sebagai : Editor

                    Fun Fact : Suka vlog masak

                    Motto Hidup : do it like you dream it

                    """)
        st.write(" ")
        st.write(" ")
        st.subheader("Khaalishah Zuhrah Alyaa Vanefi")
        # Khaalishah
        st.image("alya.jpg", width=300, caption="al/panepoy")
        st.markdown("""
                    Sebagai : Desainer

                    Fun fact : Cantik

                    Motto Hidup : it will pass

                    """)
        st.write(" ")
        st.write(" ")
        # Tessa
        st.subheader("Tessa Kania Sagala")
        st.image("tessa.jpg", width=300, caption="tes")
        st.markdown(""" 
                    Sebagai : Writer

                    Funfact : Menghindari tontonan dan bacaan yang sad ending

                    Motto Hidup : think before you act

                    """)
    about_page()


elif menu == "How To Use":
    def How_to_Use():
        st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
        st.markdown("<h1 class='centered-title'>Cara Menggunakan HofeliT</h1>", unsafe_allow_html=True)

        st.markdown('<div style="text-align: justify;">1. Klik tombol Login Page pada sisi kiri Halaman.</div>', unsafe_allow_html=True)
        st.image("no1.jpg",caption='Step 1')
        st.write("")

        st.markdown('<div style="text-align: justify;">2. Apabila belum mempunyai akun, buat akun terlebih dahulu. Pilih menu Registrasi jika belum memiliki akun. Isi data yang diperlukan.</div>', unsafe_allow_html=True)
        st.image("no2.jpg",caption='Step 2')
        st.write("")
        
        st.markdown('<div style="text-align: justify;">3. Ketika selesai mengisi data tekan tombol registrasi untuk membuat akun. Tunggu Nontifikasi hijau muncul.</div>', unsafe_allow_html=True)
        st.image("no3.jpg",caption='Step 3')
        st.write("")
        
        st.markdown('<div style="text-align: justify;">4. Pilih menu Masuk,  kemudian masukkan Username dan Password yang telah dibuat.</div>', unsafe_allow_html=True)
        st.image("no4.jpg",caption='Step 4')
        st.write("")

        st.markdown('<div style="text-align: justify;">5. Setelah tampilan User Page muncul,Quiz Page, Comunnity Page, dan Memo Page dapat digunakan. Ingat! ketiga page tersebut dapat diakses setelah berhasil masuk ke User Page .</div>', unsafe_allow_html=True)
        st.image("no5.jpg",caption='Step 5')
        st.write("")

        st.markdown('<div style="text-align: justify;">6. Tekan tombol Quiz Page pada sisi kiri untuk memulai quiz.</div>', unsafe_allow_html=True)
        st.image("no6.jpg",caption='Step 6')
        st.write("")

        st.markdown('<div style="text-align: justify;">7. Setelah mengisi jawaban dari soal yang diberikan, tekan tombol submit untuk melihat hasil akhir. Hasil akhir bisa dilihat dengan 2 output, yaitu Paramter dan saran. Untuk mengganti output tekan output yang diinginkan. Ketika berganti output, pastikan tombol submit ditekan kembali untuk melihat hasilnya.</div>', unsafe_allow_html=True)
        st.image("no71.jpg")
        st.image("no72.jpg",caption='Step 7')
        st.write("")

        st.markdown('<div style="text-align: justify;">8. Ketika sudah selesai menggunakan Hofelit, kembali ke Login Page lalu tekan tombol Keluar untuk keluar dari akun yang digunakan.</div>', unsafe_allow_html=True)
        st.image("no8.jpg",caption='Step 8')
        st.write("")
    How_to_Use()
        