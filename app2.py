import streamlit as st

st.title("Laptop Recommendation System based on your budget and purpose! 💻")

st.write("dibuat oleh orang-orang dibawah ini")
st.markdown("""
1. Hasto Timbul (639)
2. Mohammad Zacky (651)
3. Ridwan Hidayatullah (628)
""")

# selection box budget
selected_budget = st.selectbox(
    "Pilih budget:", 
    ("5-10JT", "11-20JT",">=20JT")
)
# selection box purpose
selected_purposed = st.selectbox(
    "Pilih tujuan penggunaan:",
    ("Gaming", "Video Editing","Office", "Programming")
)
# selection box OS
selected_OS = st.selectbox(
    "pilih OS:",
    ("Windows", "macOS")
)
# dynamic selection box brand/RAM

if selected_OS == "macOS":
    brand_label = "Pilih varian RAM:"
    brand_options = ("8GB RAM", "16GB RAM", "32GB RAM", "64GB RAM")
else:
    brand_label = "Pilih brand:"
    brand_options = ("ASUS", "Lenovo", "Acer")

selected_brand = st.selectbox(brand_label, brand_options)

# selection box mobilitas

selected_mobilitas = st.selectbox(
    "Seberapa sering laptop akan dibawa bepergian?",
    ("Ringan (Sering dibawa)", "Standar (Jarang dibawa)")
)


# Database laptop with the key word

laptop_database = {
    # WINDOWS: 5-10JT
    ("5-10JT", "Gaming", "Windows", "ASUS"): "ASUS TUF Gaming F15 (RTX 2050) - Entry level gaming tangguh.",
    ("5-10JT", "Gaming", "Windows", "Lenovo"): "Lenovo IdeaPad Gaming 3 - Keyboard nyaman untuk main game.",
    ("5-10JT", "Gaming", "Windows", "Acer"): "Acer Nitro V 15 - Pendinginan cukup baik di kelas budget.",
    
    ("5-10JT", "Video Editing", "Windows", "ASUS"): "ASUS Vivobook 14 (OLED) - Layar akurat untuk color grading.",
    ("5-10JT", "Video Editing", "Windows", "Lenovo"): "Lenovo IdeaPad Slim 3 - Cocok untuk editing 1080p ringan.",
    ("5-10JT", "Video Editing", "Windows", "Acer"): "Acer Aspire 5 - GPU diskrit entry-level membantu render.",
    
    ("5-10JT", "Office", "Windows", "ASUS"): "ASUS Vivobook Go 14 - Ringan dan baterai awet.",
    ("5-10JT", "Office", "Windows", "Lenovo"): "Lenovo V14 Gen 4 - Laptop bisnis esensial yang kokoh.",
    ("5-10JT", "Office", "Windows", "Acer"): "Acer Swift Go - Desain tipis dan profesional.",
    
    ("5-10JT", "Programming", "Windows", "ASUS"): "ASUS Vivobook 14 - Pilih varian RAM 16GB untuk coding.",
    ("5-10JT", "Programming", "Windows", "Lenovo"): "Lenovo V14 (Ryzen 5) - Performa multi-core oke untuk compile.",
    ("5-10JT", "Programming", "Windows", "Acer"): "Acer Aspire Vero - Ramah lingkungan dan mudah di-upgrade.",

    # WINDOWS: 11-20JT
    ("11-20JT", "Gaming", "Windows", "ASUS"): "ASUS ROG Zephyrus G14 - Powerhouse yang sangat portable.",
    ("11-20JT", "Gaming", "Windows", "Lenovo"): "Lenovo LOQ 15 (RTX 4060) - Raja performa di kelas menengah.",
    ("11-20JT", "Gaming", "Windows", "Acer"): "Acer Nitro 16 - Layar 165Hz yang sangat mulus.",
    
    ("11-20JT", "Video Editing", "Windows", "ASUS"): "ASUS Vivobook Pro 15 OLED - Performa RTX untuk render 4K.",
    ("11-20JT", "Video Editing", "Windows", "Lenovo"): "Lenovo Yoga Slim 7i - Layar premium dan build quality mewah.",
    ("11-20JT", "Video Editing", "Windows", "Acer"): "Acer Swift X - Ringkas tapi punya dedicated GPU.",
    
    ("11-20JT", "Programming", "Windows", "ASUS"): "ASUS ExpertBook B5 - Standar militer untuk dev yang mobile.",
    ("11-20JT", "Programming", "Windows", "Lenovo"): "Lenovo ThinkPad E14 - Keyboard terbaik untuk ngetik kode.",
    ("11-20JT", "Programming", "Windows", "Acer"): "Acer Spin 5 - Layar sentuh, enak untuk testing app mobile.",

    # WINDOWS: >=20JT
    (">=20JT", "Gaming", "Windows", "ASUS"): "ASUS ROG Strix SCAR 16 - Performa monster dengan layar Mini-LED.",
    (">=20JT", "Gaming", "Windows", "Lenovo"): "Lenovo Legion Pro 7i - Build quality premium dan FPS stabil.",
    (">=20JT", "Gaming", "Windows", "Acer"): "Acer Predator Helios 18 - Layar raksasa untuk pengalaman imersif.",
    
    (">=20JT", "Programming", "Windows", "Lenovo"): "Lenovo ThinkPad X1 Carbon - Laptop flagship untuk Senior Developer.",
    (">=20JT", "Video Editing", "Windows", "ASUS"): "ASUS ProArt Studiobook - Ada fitur 'Dial' fisik untuk editing.",

    # macOS: 11-20JT
    ("11-20JT", "Office", "macOS", "8GB RAM"): "MacBook Air M2 - Sangat cukup untuk dokumen dan meeting.",
    ("11-20JT", "Office", "macOS", "16GB RAM"): "MacBook Air M3 - Multitasking banyak tab tanpa lag.",
    ("11-20JT", "Programming", "macOS", "16GB RAM"): "MacBook Air M3 (16GB) - Pilihan cerdas untuk Web Developer.",
    ("11-20JT", "Video Editing", "macOS", "16GB RAM"): "MacBook Air M3 - ProRes engine membantu edit video 4K.",

    # macOS: >=20JT
    (">=20JT", "Programming", "macOS", "16GB RAM"): "MacBook Pro 14 (M4) - Layar ProMotion 120Hz sangat nyaman.",
    (">=20JT", "Programming", "macOS", "32GB RAM"): "MacBook Pro 14 (M4 Pro) - Untuk kompilasi proyek besar/Docker.",
    (">=20JT", "Programming", "macOS", "64GB RAM"): "MacBook Pro 16 (M4 Max) - Ultimate machine untuk AI/ML Engineer.",
    (">=20JT", "Video Editing", "macOS", "32GB RAM"): "MacBook Pro 16 (M4 Pro) - Layar besar dan XDR display.",
}

# if - then logic for recommendation
if st.button("Get Recommendation"):
    
    # Create the search key based on user input
    user_choice = (selected_budget, selected_purposed, selected_OS, selected_brand)

    # MAC CAN'T PLAY GAMES!!!
    if selected_OS == "macOS" and selected_purposed == "Gaming":
        st.error("NO ONE PLAYS GAMES ON MAC!!!!!!🚫")
    
    # check budget for macOS
    elif selected_OS == "macOS" and selected_budget == "5-10JT":
        st.warning("New MacBooks usually start above 10JT. Consider a second-hand M1 Air for this budget. ⚠️")

    # if the recomendation not found in db
    elif user_choice in laptop_database:
        result = laptop_database[user_choice]
        st.success(f"### rekomendasi ditemukan! \n{result}")
    
    # the else (if there's no match in db)
    else:
        st.info("Maaf saat ini tidak ada rekomendasi yang sesuai dengan kobinasi saat ini🔍")