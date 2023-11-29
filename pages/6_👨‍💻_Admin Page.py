import streamlit as st
import pandas as pd


class Admin:
    def __init__(self):
        self.data = None
        self.admin = ["kemasverii","jukai",'tessa28','Alyaa']
        self.password = "admin1"

    def baca_data(self):
        data_user = pd.read_csv("User.csv")
        return data_user

    def baca_jawaban(self):
        data_jawaban = pd.read_csv("jawaban_user.csv")
        return data_jawaban

    def admin_form(self):
        InputName = st.text_input("Admin: ")
        InputPassword = st.text_input("Password", type="password")
        klik = st.button("Login Admin")
        if klik:
            if InputName in self.admin and InputPassword == "admin1":
                st.session_state.isadmin = True
                self.admin_page()
                st.rerun()
            else:
                st.warning("ANDA BUKAN ADMIN")

    def hapus_data_user(self, username):
        data_user = self.baca_data()
        data_user = data_user[data_user["Username"] != username]
        data_user.to_csv("User.csv", index=False)
        st.rerun()

    def hapus_jawaban_user(self, index):
        data_jawaban = self.baca_jawaban()
        try:
            index = int(index)
        except ValueError:
            st.warning("Indeks harus berupa angka.")
        except KeyError:
            st.warning(f"Tidak terdapat indeks ke{index} pada data.")
        data_jawaban = data_jawaban.drop(index)     
        data_jawaban.to_csv("jawaban_user.csv", index=False)
        st.rerun()

    def hapus_semua_jawaban_user(self):
        data_jawaban = self.baca_jawaban()
        if not data_jawaban.empty:
            data_jawaban = pd.DataFrame(columns=data_jawaban.columns)
            data_jawaban.to_csv("jawaban_user.csv", index=False)
            st.success("Semua jawaban telah dihapus.")
        else:
            st.warning("Tidak ada jawaban yang dapat dihapus.")
        st.rerun()

    def admin_page(self):
        st.write(self.baca_data())
        st.write(self.baca_jawaban())
        # Form untuk menghapus data
        st.subheader("Hapus Data User")
        data_user = self.baca_data()
        hapus_username = st.selectbox("Username yang akan dihapus", data_user["Username"])
        if st.button("Hapus Data User"):
            self.hapus_data_user(hapus_username)
        opsi = st.selectbox("Opsi",("Hapus Jawaban User (index)","Hapus Semua Jawaban User"))
        if opsi == "Hapus Jawaban User (index)":
            # Form untuk menghapus jawaban
            st.subheader("Hapus Jawaban User (Index)")
            jawaban_dihapus = st.text_input("Index untuk menghapus jawaban")
            if st.button("Hapus Jawaban User"):
                self.hapus_jawaban_user(jawaban_dihapus)
        elif opsi == "Hapus Semua Jawaban User":
            st.subheader("HAPUS SEMUA JAWABAN USER")
            if st.button("HAPUS SEMUA JAWABAN USER"):
                self.hapus_semua_jawaban_user()

        if st.button("Logout"):
            st.session_state.isadmin = False
            st.rerun()


admin = Admin()

# Check if the user is an admin or show the login form
if "isadmin" in st.session_state and st.session_state.isadmin:
    admin.admin_page()
else:
    admin.admin_form()
