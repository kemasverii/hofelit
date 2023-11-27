import streamlit as st



class Komunitas:
    def __init__(self, nama):
        self.nama = nama
        self.posts = []

    def tambah_post(self, pengirim, isi_post):
        post_baru = {'pengirim': pengirim, 'isi': isi_post, 'balasan': []}
        self.posts.append(post_baru)

    def balas_post(self, id_post, pengirim, isi_balasan):
        if id_post >=0 and id_post < len(self.posts):
            balasan_baru = {'pengirim': pengirim, 'isi': isi_balasan}
            self.posts[id_post]['balasan'].append(balasan_baru)

if "isverif" not in st.session_state or st.session_state.isverif == False:
    st.title("SILAHKAN MASUK TERLEBIH DAHULU!")
    multi = """ 
        Community Page is Unavaible !
    """
    st.markdown(multi)
else:
    
    if 'komunitas_hofelit' not in st.session_state:
        st.session_state.komunitas_hofelit = Komunitas("Komunitas Hofelit")

    st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>Hofelit Community</h1>", unsafe_allow_html=True)



    menu = st.selectbox("Menu",("Tambah Post","Post"))

    # Tambah Post
    if menu == "Tambah Post":
        st.header(f"Tambah Post di {st.session_state.komunitas_hofelit.nama}")
        pengirim_post = st.text_input("Nama Pengirim (Anonim)", )
        isi_post = st.text_area("Isi Post")
        if st.button("Kirim Post"):
            st.session_state.komunitas_hofelit.tambah_post(pengirim_post, isi_post)
            st.success("Post berhasil ditambahkan!")

    # Tampilkan Post
    elif menu == "Post":
        st.header(f"Posts di {st.session_state.komunitas_hofelit.nama}")
        for i, post in enumerate(st.session_state.komunitas_hofelit.posts):
            st.text(f">. Dari: {post['pengirim']}\nIsi: {post['isi']}")
            # Tampilkan Balasan untuk setiap post
            if post['balasan']:
                st.subheader("Balasan:")
                for balasan in post['balasan']:
                    st.text(f"Dari: {balasan['pengirim']}\nIsi: {balasan['isi']}")

            # Tombol Balas untuk setiap post
            balasan_input = st.text_area(f"Balas Post {i}")
            if st.button(f"Balas Post - {i}") and balasan_input:
                st.session_state.komunitas_hofelit.balas_post(i, "Pengguna", balasan_input)
                st.sidebar.text(f"Balasan pada post {i} berhasil ditambahkan!")
                st.rerun()  


