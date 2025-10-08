import streamlit as st

# Judul aplikasi
st.title("Pencarian Cookie Run: Kingdom")

# Database sederhana: cookie dan deskripsinya
cookie_db = {
    "Strawberry Cookie": "Role: Attack, Skill: Healing Berry",
    "Wizard Cookie": "Role: Magic, Skill: Magic Missile",
    "Knight Cookie": "Role: Defense, Skill: Shield Bash",
    "Angel Cookie": "Role: Support, Skill: Healing Light",
    "Dark Choco Cookie": "Role: Attack, Skill: Dark Slash",
}

# Input dari pengguna
query = st.text_input("Masukkan nama cookie atau kata kunci:")

# Fungsi pencarian
def search_cookie(query):
    results = {}
    for name, info in cookie_db.items():
        if query.lower() in name.lower() or query.lower() in info.lower():
            results[name] = info
    return results

# Tampilkan hasil pencarian
if query:
    results = search_cookie(query)
    if results:
        st.subheader("Hasil Pencarian:")
        for name, info in results.items():
            st.write(f"**{name}**: {info}")
    else:
        st.write("Maaf, cookie tidak ditemukan.")
