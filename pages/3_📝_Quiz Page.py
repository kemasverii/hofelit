import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

class Quiz:
    def __init__(self, pertanyaan,username):
        self.pertanyaan = pertanyaan
        self.username = username
        self.jawaban = []
        self.submitted = False
        # Display the questions and get the user's answers
    def lihat_jawaban(self):
        respon_user = pd.read_csv("jawaban_user.csv")
        return respon_user
    
    def waktu(self):
        waktu_sekarang = datetime.now()
        return waktu_sekarang
    
    def jawaban_user(self,username,jawaban):
        try:
            data_jawaban = pd.read_csv("jawaban_user.csv")
        except FileNotFoundError:
            data_jawaban = pd.DataFrame(columns=['username',
                            'pertanyaan 1',
                            'pertanyaan 2',
                            'pertanyaan 3',
                            'pertanyaan 4',
                            'pertanyaan 5',
                            'pertanyaan 6',
                            'pertanyaan 7',
                            'pertanyaan 8',
                            'pertanyaan 9',
                            'pertanyaan 10',
                            'tanggal_waktu'])
        df_jawaban = pd.DataFrame({
                            'username':[username],
                            'pertanyaan 1': [jawaban[0]],
                            'pertanyaan 2': [jawaban[1]],
                            'pertanyaan 3': [jawaban[2]],
                            'pertanyaan 4': [jawaban[3]],
                            'pertanyaan 5': [jawaban[4]],
                            'pertanyaan 6': [jawaban[5]],
                            'pertanyaan 7': [jawaban[6]],
                            'pertanyaan 8': [jawaban[7]],
                            'pertanyaan 9': [jawaban[8]],
                            'pertanyaan 10': [jawaban[9]],
                            'tanggal_waktu': [self.waktu()]})
        if self.username in data_jawaban['username'].values:

            data_jawaban = pd.concat([data_jawaban,df_jawaban], ignore_index=True)
        else:
        
            data_jawaban = pd.concat([data_jawaban, df_jawaban], ignore_index=True)
        data_jawaban.to_csv("jawaban_user.csv",index=False)

    def soal(self):
        for i, pertanyaan_item in enumerate(self.pertanyaan):
            # Display "Yes" and "No" options
            user_choice = st.radio(
                f"Pertanyaan {i + 1}: {pertanyaan_item} (1 = Rendah, 10 = Tinggi) ",
                ["Ya", "Tidak"],
            )
            if user_choice == "Ya":
                hasil = st.slider("Pilih angka:", 1, 10, key=f"slider_{i}")
                st.write("Anda memilih angka:", hasil)
                self.jawaban.append(hasil)
            elif user_choice == "Tidak":
                hasil = 0
                self.jawaban.append(hasil)
        self.submit_button()

    def submit_button(self):
        klik = st.button("Submit")
        if klik:
            if sum(self.jawaban) <= 0.9 and sum(self.jawaban) >= 0:
                st.success("Kondisi anda sangat baik!")
            elif len(self.jawaban) == len(self.pertanyaan):
                st.session_state.issubmit = True
                self.submitted = True
                self.jawaban_user(self.username,self.jawaban)
            else:
                st.warning("Isi Jawaban dengan Benar!")
            if "issubmit" in st.session_state and st.session_state.issubmit:
                st.success("Jawaban Anda telah disubmit!")
            # Menampilkan respon hanya setelah tombol "Submit" ditekan

    def hasil(self):
        rata_rata = sum(self.jawaban) / len(self.pertanyaan)
        return rata_rata


    def chart(self, poin):
        if poin >= 1:
            fig = go.Figure(
                go.Indicator(
                    domain={"x": [0, 1], "y": [0, 1]},
                    value=poin,
                    mode="gauge+number",
                    title={"text": "Mental Health Poin"},
                    gauge={
                        "axis": {"range": [0, 10]},
                        "steps": [
                            {"range": [0, 3.9], "color": "green"},
                            {"range": [4, 6.9], "color": "yellow"},
                            {"range": [7, 10], "color": "red"},
                        ],
                        "threshold": {
                            "line": {"color": "white", "width": 4},
                            "thickness": 0.75,
                            "value": poin,
                        },
                    },
                )
            )
            st.plotly_chart(fig, use_container_width=True, height=50)

    def saran(self, poin):
        if poin >= 1:
            if poin >= 1 and poin <= 3.9:
                st.title("Saran")
                st.markdown(
                    """
                        Normal : Menjaga pola hidup sehat, tidur cukup.
                            
                        Kegiatan yang dapat dilakukan:
                            
                        1. Katakan Hal Positif pada Diri Sendiri
                            
                        3. Fokus pada Satu Hal pada Satu Waktu
                        
                        4. Olahraga
                            
                        5. Makanlah Makanan yang Enak
                            
                        6. Makan coklat!
                            
                        7.  Istirahat
                        """
                )
            elif poin >= 4 and poin <= 6.9:
                st.title("Saran")
                st.markdown(
                    """
                        Jenuh : istirahat, mencari kesibukan, bertemu teman, jalan jalan

                        Kegiatan yang dapat dilakukan:
                        
                        1. Memaknai Kembali Pekerjaan yang Dilakukan.
                        
                        2. Mendengarkan Musik.
                        
                        3. Menata Ruang Kerja.
                        
                        4. Menjaga Work-Life Balance. 
                        
                        """
                )
            elif poin >= 7 and poin <= 10:
                st.title("Saran")
                st.markdown(
                    """
                        Stress : istirahat, makan cukup, konsultasi pada pihak profesional (psikiater, halo-dok)
                        
                        Kegiatan yang dapat dilakukan:
                            
                        1. Bicarakan keluhan dengan seseorang yang dapat dipercaya.
                            
                        2. Melakukan kegiatan yang sesuai dengan minat dan kemampuan.
                            
                        3. Kembangkan hobi yang bermanfaat.
                            
                        4. Meningkatkan ibadah dan mendekatkan diri pada Tuhan.
                            
                        5. Berpikir positif.
                            
                        6. Tenangkan pikiran dengan relaksasi.
                            
                        """
                )

    
    def pilihan(self, poin):
        hasil = st.selectbox("Menu",("Parameter","Saran"))
        if self.submitted:
            st.title("Hasil Quiz:")
            st.header(f"Poin Anda: {poin: .1f}")
            if poin >= 1 and poin <= 3.9:
                st.markdown(
                    """<style>.centered-title {text-align: center;}</style>""",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<h1 class='centered-title'>Anda sedang baik-baik saja</h1>",
                    unsafe_allow_html=True,
                )
            elif poin >= 4 and poin <= 6.9:
                st.markdown(
                    """<style>.centered-title {text-align: center;}</style>""",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<h1 class='centered-title'>Anda sedang jenuh</h1>",
                    unsafe_allow_html=True,
                )
            elif poin >= 7 and poin <= 10:
                st.markdown(
                    """<style>.centered-title {text-align: center;}</style>""",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<h1 class='centered-title'>Anda sedang stress</h1>",
                    unsafe_allow_html=True,
                )

            
            if hasil== "Parameter":
                self.chart(poin)
            elif hasil == "Saran":
                self.saran(poin)
                if poin > 7:
                    st.markdown(
                        '<div style="text-align: justify;">Jika anda merasa perlu penangan lebih terkait kesehatan mental anda, kami sarankan klik link dibawah ini untuk melihat Psikiater terdekat</div>',
                        unsafe_allow_html=True,
                    )
                    st.subheader("Link Psikiater Terdekat")
                    st.link_button(
                        "Psikiater Terdekat", "https://bit.ly/PsikiaterTerdekat"
                    )




pertanyaan = [
    "Apakah anda merasa tidak baik-baik saja selama ini?",
    "Apa kamu merasa percaya diri dengan semua kondisimu sekarang?",
    "Pernahkah Anda merasa dipengaruhi oleh perasaan gelisah, cemas, atau gugup?",
    "Seberapa sering Anda merasa terganggu karena tidak bisa berhenti khawatir?",
    "Apakah kamu hobi bepergian dengan teman?",
    "Apakah kamu lebih suka menyendiri daripada bermain bareng teman-teman?",
    "Apakah perasaan cemas atau tidak nyaman di sekitar orang lain mengganggu Anda?",
    "Pernahkah Anda mengalami penurunan minat terhadap aktivitas yang biasanya Anda nikmati selama seminggu atau lebih? Contohnya mungkin termasuk pekerjaan, olahraga, atau hobi.",
    "Apakah kamu merasa sangat lelah dan tidak ingin bersosialisasi?",
    "Apakah kamu sering berdiam diri karena merasa stress dan penat?",
]
st.markdown(
    """<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True
)


if "isverif" not in st.session_state or st.session_state.isverif == False:
    st.title("SILAHKAN MASUK TERLEBIH DAHULU UNTUK MEMULAI QUIZ!")
    multi = """ 
    Setelah itu pastikan:

    1. Menjawab soal dengan jujur dan kemauan sendiri.

    2. Jangan cemas ya gaiss, karena apapun yang kamu dapatkan hasilnya, dapat membantu diri menjadi lebih baik.

    3. Jangan terburu-buru ngerjainnya.

    4. Jawaban harus diisi terlebih dahulu dan jangan lupa untuk submit yaa.

    5. Semangat, kamu pasti orang hebat dan kuat yang bisa bertahan selama ini !!!
    """
    st.markdown(multi)
else:
    st.markdown(
        """<style>.centered-title {text-align: center;}</style>""",
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='centered-title'>Hofelit</h1>", unsafe_allow_html=True)
    username = st.session_state.username
    quiz = Quiz(pertanyaan,username)
    quiz.soal()
    poin = quiz.hasil()
    quiz.pilihan(poin)