import streamlit as st
import pandas as pd
from datetime import datetime
class LoginUser:

    def __init__(self):
        self.username = None
        
    def baca_data(self):
        try:
            data_user = pd.read_csv("User.csv")
        except FileNotFoundError:
            data_user = pd.DataFrame(columns=["Username", "Password","Nama_Lengkap","Tanggal_Lahir",'Waktu_Tanggal'])
        return data_user

    def regist_data(self,name,password,full_name,date):
        data_user = self.baca_data()
        if name.strip() == '' or password.strip() == '' or full_name.strip() == '' or date.strip() == ' ': #jika inputan kosong, harus diisi
            st.error('Masukkan data yang valid')
            return
        if name in data_user["Username"].tolist():
            st.error("Username sudah terdaftar!, silakan ganti dengan Username lain")
        else:
            new_data = pd.DataFrame({"Username": [name], "Password": [password],"Nama_Lengkap": [full_name],"Tanggal_Lahir": [date],"Waktu_Tanggal":[datetime.now()]})
            data_user = pd.concat([data_user, new_data], ignore_index=True)
            data_user.to_csv("User.csv", index=False) # Corrected line
            st.success("Registrasi berhasil ! silakan Login")

    def cek_data(self,name,password):
        data_user = self.baca_data()
        user = (data_user[(data_user["Username"] == name) & (data_user["Password"] == password )].iloc[0]
            if not data_user.empty
            else None
            ) 
        if user is not None:
            self.name = name
            st.session_state.isverif = True
            st.session_state.isloggin = True
            st.session_state.username = self.name
            st.rerun()
        
    
    def buat_form(self):
        menu = st.selectbox("Opsi",("Masuk","Registrasi"))
        if menu == "Registrasi":
            InputName = st.text_input("Nama Lengkap")
            Inputdate = st.text_input("Tanggal Lahir (DD/MM/YYYY)")
        InputUsername = st.text_input("Username")
        InputPassword = st.text_input("Password", type="password")

        if menu == "Registrasi":
            if st.button("Daftar"):
                self.regist_data(InputUsername,InputPassword,InputName,Inputdate)
        elif menu == "Masuk":
            if st.button("Masuk"):
                self.cek_data(InputUsername, InputPassword)
        
    
    def user_page(self):
        if "isloggin" in st.session_state and st.session_state.isloggin:
            st.title(f"Welcome !")
            with st.container():
                data_user = self.baca_data()

            # Saring kolom-kolom yang ingin ditampilkan
                filtered_data = data_user[data_user["Username"] == st.session_state.username][["Username", "Nama_Lengkap", "Tanggal_Lahir"]]

            # Tampilkan informasi
                if not filtered_data.empty:
                    user_info = filtered_data.iloc[0]  # Ambil baris pertama (karena seharusnya hanya satu baris)
                    st.subheader(f"Username : ")
                    st.write(f"{user_info['Username']}")
                    st.subheader(f"Nama Lengkap : ")
                    st.write(f"{user_info['Nama_Lengkap']}")
                    st.subheader(f"Tanggal Lahir : ")
                    st.write(f"{user_info['Tanggal_Lahir']}")
                    # Tambahkan elemen teks lainnya sesuai kebutuhan
            
            if st.button("Logout"):
                st.session_state.isloggin = False
                st.session_state.isverif = False
                st.rerun()
        else:
            st.sidebar.empty()  
            self.buat_form()

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>Hofelit</h1>", unsafe_allow_html=True)

app = LoginUser()
app.user_page()
