import streamlit as st
from streamlit_option_menu import option_menu

class MemoApp:
    def __init__(self):
        self.memo = ""

    def tulis_memo(self, isi_memo):
        self.memo = isi_memo

    def tampilkan_memo(self):
        st.header("My Memo")
        st.write(self.memo)

if "isverif" not in st.session_state or st.session_state.isverif == False:
    st.title("SILAHKAN MASUK TERLEBIH DAHULU!")
    multi = """ 
            Memo Page is Unavaible !
    """
    st.markdown(multi)
else:
    MemoApp()
    if "memo_app" not in st.session_state:
        st.session_state.memo_app = MemoApp ()
    st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>Hofelit</h1>", unsafe_allow_html=True)

    def streamlit_menu():
        selected = option_menu(
            menu_title=None,
            options =["Tulis Memo","Tampilkan Memo"],
            icons=['pen','envelope'],
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

    if menu == "Tulis Memo":
        st.header("Keresehan Kuuu !")
        isi_memo = st.text_area("Apa yang Anda rasakan saat ini?")
        if st.button("Simpan Memo"):
            if isi_memo.strip():  
                st.session_state.memo_app.tulis_memo(isi_memo)
                st.success("Memo berhasil disimpan!")
            else:
                st.error("Isi memo tidak boleh kosong. Silakan tulis sesuatu sebelum menyimpan.")

    elif menu == "Tampilkan Memo":
        st.session_state.memo_app.tampilkan_memo()
