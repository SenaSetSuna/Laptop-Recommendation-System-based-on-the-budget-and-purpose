# Laptop Recommendation System based on your budget and purpose! 💻
# build by these kind of peaople :v
# 1. <NAME> <NIM> <GITHUB>
# 2. <NAME> <NIM> <GITHUB>
# 3. <NAME> <NIM> <GITHUB>


import streamlit as st

st.title("Laptop Recommendation System based on your budget and purpose! 💻")

# selection box budget
selected_budget = st.selectbox(
    "Pilih budget:", 
    ("<=5JT", "6-10JT", "11-15JT", "16-20JT", "21-25JT", "26-30JT", ">30JT")
)
# selection box purpose
selected_purposed = st.selectbox(
    "Pilih tujuan penggunaan:",
    ("Gaming", "3D Rendering", "Video Editing", "Game Making", "Office", "Programming")
)

if st.button("Get Recommendation"):

    # else if logic for recommendations based on selected genre and thing
    
# Gaming recommendation
    if selected_budget == "<=5JT" and selected_purposed == "Gaming":
        st.write("Advan Workmate (Ryzen 5) is the best 'budget gaming' compromise for esports titles under 5JT! 🎮")
        st.info("Note: This laptop is best for lightweight games like Valorant, CS:GO, and League of Legends. Don't expect AAA titles to run well on high settings! 🎮")
    elif selected_budget == "6-10JT" and selected_purposed == "Gaming":
        st.write("ASUS TUF A15 (RTX 2050) is a fantastic entry-level gaming laptop with military-grade durability! 🎮")
    elif selected_budget == "11-15JT" and selected_purposed == "Gaming":
        st.write("Axioo Pongo 750 (RTX 4050) is the price-to-performance king in this range for 2026! 🎮")
    elif selected_budget == "16-20JT" and selected_purposed == "Gaming":
        st.write("Lenovo LOQ 15 (RTX 5050) features the latest generation GPU for high-refresh 1080p gaming! 🎮")
    elif selected_budget == "21-25JT" and selected_purposed == "Gaming":
        st.write("Acer Predator Helios Neo 16 is a powerful beast with superior cooling and HX-series processors! 🎮")
    elif selected_budget == "26-30JT" and selected_purposed == "Gaming":
        st.write("Lenovo Legion Pro 5i (RTX 5060) offers top-tier build quality and consistent FPS for pro gamers! 🎮")
    elif selected_budget == ">30JT" and selected_purposed == "Gaming":
        st.write("MSI Titan 18 HX AI is a literal desktop replacement with the monstrous RTX 5090! 🎮")

# 3D Rendering recommendation
    elif selected_budget == "<=5JT" and selected_purposed == "3D Rendering":
        st.write("Advan WorkMate (Ryzen 5) is the best budget compromise for lightweight 3D modeling under 5JT! 🖥️")
        st.info("Note: This laptop is suitable for basic 3D modeling and rendering in software like Blender, but don't expect it to handle complex scenes or high-poly models well! 🖥️")
    elif selected_budget == "6-10JT" and selected_purposed == "3D Rendering":
        st.write("Acer Aspire Lite (Ryzen 7 8000 Series) offers solid multi-core power for CPU-based rendering! 🖥️")
    elif selected_budget == "11-15JT" and selected_purposed == "3D Rendering":
        st.write("Axioo Pongo 725 (RTX 2050) is the most affordable way to get dedicated ray-tracing hardware! 🖥️")
    elif selected_budget == "16-20JT" and selected_purposed == "3D Rendering":
        st.write("Lenovo LOQ 15 (RTX 5050) with 8GB VRAM is perfect for rendering complex textures and scenes! 🖥️")
    elif selected_budget == "21-25JT" and selected_purposed == "3D Rendering":
        st.write("Acer Predator Helios Neo 16 provides the thermal cooling needed for long render sessions! 🖥️")
    elif selected_budget == "26-30JT" and selected_purposed == "3D Rendering":
        st.write("ASUS ProArt Studiobook 16 OLED is tailor-made for professionals with its color-accurate 4K screen! 🖥️")
    elif selected_budget == ">30JT" and selected_purposed == "3D Rendering":
        st.write("MSI Titan 18 HX AI is the ultimate workstation for heavy VFX and 8K 3D rendering! 🖥️")

# Video Editing recommendation
    elif selected_budget == "<=5JT" and selected_purposed == "Video Editing":
        st.write("SPC Life 5 (Intel Core i5-12450H) is the performance leader for budget 1080p editing under 5JT! 🎬")
        st.info("Note: This laptop is best for basic video editing in software like Adobe Premiere Pro and DaVinci Resolve at 1080p. Don't expect it to handle 4K editing or complex effects smoothly! 🎬")
    elif selected_budget == "6-10JT" and selected_purposed == "Video Editing":
        st.write("Lenovo IdeaPad Slim 3 (i5-12450H + 16GB RAM) handles multi-layer editing smoothly for mid-range budgets! 🎬")
    elif selected_budget == "11-15JT" and selected_purposed == "Video Editing":
        st.write("Acer Nitro Lite 16 (100% sRGB) is essential for color-accurate work without breaking the bank! 🎬")
    elif selected_budget == "16-20JT" and selected_purposed == "Video Editing":
        st.write("ASUS Vivobook 16X OLED provides a stunning professional display and RTX graphics for 4K editing! 🎬")
    elif selected_budget == "21-25JT" and selected_purposed == "Video Editing":
        st.write("HP Omen 15 (RTX 5050) offers the power and VRAM needed for complex effects and faster exports! 🎬")
    elif selected_budget == "26-30JT" and selected_purposed == "Video Editing":
        st.write("ASUS ProArt Studiobook 16 is a dedicated creator machine with an built-in dial for editing precision! 🎬")
    elif selected_budget == ">30JT" and selected_purposed == "Video Editing":
        st.write("MacBook Pro 16 (M4 Max) is the ultimate choice for professional 8K timelines and long battery life! 🎬")

# Game Making recommendation
    elif selected_budget == "<=5JT" and selected_purposed == "Game Making":
        st.write("Advan Workplus (Ryzen 5 6600H) is the only budget laptop with enough threads for basic 2D game dev! 🎮")
        st.info("Note: This laptop is suitable for entry-level game development using engines like Unity or Godot, but it may struggle with more complex 3D game projects or large scenes! 🎮")
    elif selected_budget == "6-10JT" and selected_purposed == "Game Making":
        st.write("Axioo Pongo 725 (Core i7-12650H) provides the CPU cores and RTX GPU needed for entry-level 3D dev! 🎮")
    elif selected_budget == "11-15JT" and selected_purposed == "Game Making":
        st.write("Acer Nitro V 15 (RTX 4060) is the best value for mid-range game development in 2026! 🎮")
    elif selected_budget == "16-20JT" and selected_purposed == "Game Making":
        st.write("Lenovo LOQ 15 (RTX 5050) offers 8GB VRAM, which is essential for high-res textures in game engines! 🎮")
    elif selected_budget == "21-25JT" and selected_purposed == "Game Making":
        st.write("Acer Predator Helios Neo 16 is a thermal beast, keeping performance stable during long engine compiles! 🎮")
    elif selected_budget == "26-30JT" and selected_purposed == "Game Making":
        st.write("ASUS ROG Zephyrus G14 (2026) is the perfect portable workstation for developers on the go! 🎮")
    elif selected_budget == ">30JT" and selected_purposed == "Game Making":
        st.write("ASUS ROG Strix SCAR 18 is the ultimate performance beast for AAA game production and VR dev! 🎮")

# Office recommendation
    elif selected_budget == "<=5JT" and selected_purposed == "Office":
        st.write("Axioo Hype 3 (Core i3-1215U) is a fast and reliable choice for office multitasking on a budget! 💼")
        st.info("Note: This laptop is suitable for basic office tasks like document editing, email, and web browsing. It may struggle with more demanding applications or multitasking! 💼")
    elif selected_budget == "6-10JT" and selected_purposed == "Office":
        st.write("ASUS Vivobook 14 (A1404) offers a professional design and a great keyboard for daily office work! 💼")
    elif selected_budget == "11-15JT" and selected_purposed == "Office":
        st.write("HP Pavilion Aero 13 is incredibly lightweight (under 1kg), making it perfect for office commutes! 💼")
    elif selected_budget == "16-20JT" and selected_purposed == "Office":
        st.write("MacBook Air M3 provides the best battery life and silence for a distraction-free office experience! 💼")
    elif selected_budget == "21-25JT" and selected_purposed == "Office":
        st.write("Lenovo Yoga Slim 7i Carbon is a premium, ultra-tough laptop with a stunning display for professionals! 💼")
    elif selected_budget == "26-30JT" and selected_purposed == "Office":
        st.write("Dell XPS 13 (2025) offers a futuristic bezel-less design and top-tier build quality for executives! 💼")
    elif selected_budget == ">30JT" and selected_purposed == "Office":
        st.write("MacBook Pro 16 (M4 Pro) is the ultimate workspace with a massive screen and power for any office task! 💼")

# Programming recommendation
    elif selected_budget == "<=5JT" and selected_purposed == "Programming":
        st.write("Advan WorkMate (Ryzen 5) is the ultimate budget dev machine with an upgradable 16:10 screen! 💻")
        st.info("Note: This laptop is suitable for entry-level programming tasks, web development, and learning to code. It may struggle with more demanding software development tasks or large codebases! 💻")
    elif selected_budget == "6-10JT" and selected_purposed == "Programming":
        st.write("ASUS Vivobook 14 (Ryzen 7) with 16GB RAM is a powerhouse for heavy multitasking and Docker! 💻")
    elif selected_budget == "11-15JT" and selected_purposed == "Programming":
        st.write("MacBook Air M2 (8GB) provides a stable Unix-based environment perfect for web and mobile dev! 💻")
    elif selected_budget == "16-20JT" and selected_purposed == "Programming":
        st.write("Lenovo ThinkPad P14s Gen 5 is a certified workstation with the world's best keyboard for coding! 💻")
    elif selected_budget == "21-25JT" and selected_purposed == "Programming":
        st.write("MacBook Pro 14 (M4) offers incredible build quality and speed for professional software engineers! 💻")
    elif selected_budget == "26-30JT" and selected_purposed == "Programming":
        st.write("Lenovo ThinkPad X1 Carbon Gen 13 is the ultra-light flagship for developers who travel often! 💻")
    elif selected_budget == ">30JT" and selected_purposed == "Programming":
        st.write("MacBook Pro 16 (M5 Max) with 64GB+ RAM is the ultimate beast for AI, ML, and large-scale backend dev! 💻")

    #else (y begitulah) :v
    else:
        st.write("Invalid selection. Please select a valid genre and thing you like.")