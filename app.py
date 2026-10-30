import streamlit as st
import pandas as pd
import numpy as np

# =========================================================
# 1. KONFIGURASI APLIKASI
# =========================================================

st.set_page_config(
    page_title="SPK Laptop | Metode MOORA Pro",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CUSTOM CSS (CLEAN & MODERN GREEN-WHITE THEME)
# =========================================================

st.markdown("""
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Global Typography & Reset */
    html, body, .stApp, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Pastikan icon Material Symbols bawaan Streamlit tidak ter-override oleh font sans-serif */
    [data-testid="stIconMaterial"],
    [data-testid="stIconMaterial"] *,
    [data-testid*="Icon"],
    [data-testid*="icon"],
    [data-testid*="Chevron"],
    [data-testid*="Chevron"] *,
    [data-testid*="chevron"],
    [data-testid="stExpanderToggleIcon"],
    [data-testid="stExpanderStepChevron"],
    span[translate="no"],
    .material-symbols-rounded,
    .material-symbols-outlined,
    .material-icons,
    [class*="material-symbols"] {
        font-family: 'Material Symbols Rounded', 'Material Symbols Outlined', 'Material Icons' !important;
        font-feature-settings: 'liga' 1 !important;
        -webkit-font-feature-settings: 'liga' 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        white-space: nowrap !important;
        word-wrap: normal !important;
        direction: ltr !important;
        font-style: normal !important;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace;
    }

    /* Background Utama (Bersih, Minimalis, Soft White/Gray) */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    /* Area Konten Container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Sidebar Clean & Modern White/Light Emerald Accent */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }

    section[data-testid="stSidebar"] * {
        color: #1e293b !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        background: #f8fafc;
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 8px;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: #ecfdf5;
        border-color: #10b981;
        color: #047857 !important;
        transform: translateX(4px);
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background: #10b981 !important;
        border-color: #10b981 !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] * {
        color: #ffffff !important;
        font-weight: 600;
    }

    /* Header Typography */
    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
        letter-spacing: -0.025em;
    }

    /* Hero Banner Modern Minimalist Green Gradient */
    .hero {
        background: linear-gradient(135deg, #059669 0%, #10b981 50%, #34d399 100%);
        border: 1px solid #a7f3d0;
        padding: 36px 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.2);
        position: relative;
        overflow: hidden;
    }

    .hero h1 {
        color: #ffffff !important;
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: -0.02em;
    }

    .hero p {
        color: #ecfdf5;
        font-size: 15px;
        margin-bottom: 0;
        line-height: 1.6;
        max-width: 800px;
    }

    /* Stat Cards / Kartu Statistik */
    .stat-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px 24px;
        min-height: 120px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
        transition: all 0.25s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-3px);
        border-color: #10b981;
        box-shadow: 0 12px 20px -5px rgba(16, 185, 129, 0.12);
    }

    .stat-label {
        color: #64748b;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .stat-value {
        color: #047857;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.03em;
    }

    .stat-caption {
        color: #94a3b8;
        font-size: 12px;
        margin-top: 6px;
    }

    /* Winner Card / Kartu Rekomendasi Juara */
    .winner-card {
        background: #ffffff;
        border: 2px solid #10b981;
        padding: 28px 32px;
        border-radius: 20px;
        margin: 20px 0 30px 0;
        box-shadow: 0 10px 30px -10px rgba(16, 185, 129, 0.18);
        position: relative;
    }

    .winner-label {
        color: #059669;
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .winner-name {
        color: #0f172a;
        font-size: 26px;
        font-weight: 800;
        margin-top: 8px;
        letter-spacing: -0.02em;
    }

    .winner-score {
        color: #047857;
        font-size: 14px;
        font-weight: 700;
        margin-top: 12px;
        display: inline-block;
        padding: 6px 16px;
        background: #ecfdf5;
        border-radius: 30px;
        border: 1px solid #a7f3d0;
    }

    /* Criterion Cards / Kartu Kriteria */
    .criterion-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
        transition: all 0.25s ease;
    }

    .criterion-card:hover {
        border-color: #10b981;
        transform: translateY(-2px);
        box-shadow: 0 8px 16px -4px rgba(16, 185, 129, 0.1);
    }

    .criterion-name {
        font-size: 15px;
        font-weight: 700;
        color: #1e293b;
    }

    .criterion-weight {
        font-size: 26px;
        font-weight: 800;
        color: #059669;
        margin-top: 8px;
    }

    .criterion-type {
        color: #475569;
        font-size: 12px;
        font-weight: 600;
        margin-top: 8px;
        display: inline-block;
        padding: 4px 10px;
        background: #f1f5f9;
        border-radius: 6px;
    }

    /* Section Label Badge */
    .section-label {
        color: #059669;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        padding: 32px 0;
        border-top: 1px solid #e2e8f0;
        margin-top: 48px;
        background: transparent;
    }

    .footer b {
        color: #0f172a;
    }

    /* Custom Tombol Streamlit */
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
        background: #10b981;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.25);
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        background: #059669;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
        transform: translateY(-1px);
    }

    /* Tabel / Dataframe styling */
    div[data-testid="stDataFrame"] {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
        background: #ffffff;
    }

    /* Metric Box Optimization */
    div[data-testid="stMetric"] {
        background: #ffffff;
        padding: 16px 20px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
    }

    div[data-testid="stMetricValue"] {
        color: #059669 !important;
        font-weight: 800;
    }

    /* Expander / Collapsible Card Styling */
    div[data-testid="stExpander"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        overflow: hidden;
        transition: all 0.25s ease;
    }

    div[data-testid="stExpander"]:hover {
        border-color: #10b981;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.08);
    }

    div[data-testid="stExpander"] summary {
        font-weight: 700;
        color: #0f172a;
        padding: 14px 18px;
    }

    div[data-testid="stExpander"] summary:hover {
        color: #059669;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. DATA KRITERIA
# =========================================================

kriteria = [
    "C1 Harga",
    "C2 Kapasitas Baterai",
    "C3 RAM",
    "C4 CPU",
    "C5 Hardisk",
    "C6 Ukuran"
]

bobot = {
    "C1 Harga": 0.20,
    "C2 Kapasitas Baterai": 0.10,
    "C3 RAM": 0.20,
    "C4 CPU": 0.20,
    "C5 Hardisk": 0.20,
    "C6 Ukuran": 0.10
}

atribut = {
    "C1 Harga": "Cost",
    "C2 Kapasitas Baterai": "Benefit",
    "C3 RAM": "Benefit",
    "C4 CPU": "Benefit",
    "C5 Hardisk": "Benefit",
    "C6 Ukuran": "Cost"
}


# =========================================================
# 4. DATA ALTERNATIF
# =========================================================

data = [
    {
        "Kode": "A1",
        "Nama Laptop": "Acer Aspire 5 A514-56P-57Q8",
        "C1 Harga": 3,
        "C2 Kapasitas Baterai": 2,
        "C3 RAM": 3,
        "C4 CPU": 2,
        "C5 Hardisk": 1,
        "C6 Ukuran": 3
    },
    {
        "Kode": "A2",
        "Nama Laptop": "Acer Aspire 5 Slim i3 MX350",
        "C1 Harga": 5,
        "C2 Kapasitas Baterai": 1,
        "C3 RAM": 2,
        "C4 CPU": 2,
        "C5 Hardisk": 1,
        "C6 Ukuran": 3
    },
    {
        "Kode": "A3",
        "Nama Laptop": "Axioo MyBook Z10 METAL",
        "C1 Harga": 2,
        "C2 Kapasitas Baterai": 2,
        "C3 RAM": 3,
        "C4 CPU": 4,
        "C5 Hardisk": 3,
        "C6 Ukuran": 4
    },
    {
        "Kode": "A4",
        "Nama Laptop": "Lenovo IdeaPad Slim1 14ILG05",
        "C1 Harga": 3,
        "C2 Kapasitas Baterai": 2,
        "C3 RAM": 3,
        "C4 CPU": 3,
        "C5 Hardisk": 3,
        "C6 Ukuran": 3
    },
    {
        "Kode": "A5",
        "Nama Laptop": "Asus Vivobook A4 16MAO",
        "C1 Harga": 5,
        "C2 Kapasitas Baterai": 1,
        "C3 RAM": 2,
        "C4 CPU": 2,
        "C5 Hardisk": 1,
        "C6 Ukuran": 3
    },
    {
        "Kode": "A6",
        "Nama Laptop": "Axioo MyBook 14F CELERON",
        "C1 Harga": 2,
        "C2 Kapasitas Baterai": 3,
        "C3 RAM": 3,
        "C4 CPU": 4,
        "C5 Hardisk": 1,
        "C6 Ukuran": 3
    }
]

df = pd.DataFrame(data)


# =========================================================
# 5. FUNGSI PERHITUNGAN MOORA
# =========================================================

def hitung_moora(dataframe):

    matriks = dataframe[kriteria].astype(float)

    # Normalisasi matriks
    pembagi = np.sqrt((matriks ** 2).sum(axis=0))

    normalisasi = matriks.div(
        pembagi.replace(0, np.nan),
        axis=1
    ).fillna(0)

    # Normalisasi terbobot
    terbobot = normalisasi.copy()

    for kolom in kriteria:
        terbobot[kolom] = (
            normalisasi[kolom] * bobot[kolom]
        )

    # Pemisahan benefit dan cost
    kolom_benefit = [
        kolom for kolom in kriteria
        if atribut[kolom] == "Benefit"
    ]

    kolom_cost = [
        kolom for kolom in kriteria
        if atribut[kolom] == "Cost"
    ]

    # Menghitung nilai benefit
    nilai_benefit = terbobot[kolom_benefit].sum(axis=1)

    # Menghitung nilai cost
    nilai_cost = terbobot[kolom_cost].sum(axis=1)

    # Menghitung nilai optimasi
    nilai_yi = nilai_benefit - nilai_cost

    # Membuat tabel hasil
    hasil = dataframe[
        ["Kode", "Nama Laptop"]
    ].copy()

    hasil["Nilai Benefit"] = nilai_benefit
    hasil["Nilai Cost"] = nilai_cost
    hasil["Nilai Yi"] = nilai_yi

    hasil = hasil.sort_values(
        by="Nilai Yi",
        ascending=False
    ).reset_index(drop=True)

    hasil["Peringkat"] = range(1, len(hasil) + 1)

    return normalisasi, terbobot, hasil


normalisasi, terbobot, hasil = hitung_moora(df)


# =========================================================
# 6. SIDEBAR NAVIGASI
# =========================================================

with st.sidebar:

    st.markdown("""
        <div style="text-align:center; padding:16px 5px 20px 5px;">
            <div style="font-size:42px; margin-bottom:6px;">💻</div>
            <div style="font-size:20px; font-weight:800; color:#0f172a; letter-spacing:-0.02em;">
                SPK LAPTOP
            </div>
            <div style="font-size:11px; color:#059669; font-weight:700; letter-spacing:1.5px; margin-top:4px; text-transform: uppercase;">
                METODE MOORA PRO
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        "<div style='font-size:11px; font-weight:800; "
        "color:#059669; margin-bottom:12px; letter-spacing:1.5px; text-transform: uppercase;'>MENU UTAMA</div>",
        unsafe_allow_html=True
    )

    menu = st.radio(
        "Navigasi",
        [
            "Beranda",
            "Data Alternatif",
            "Kriteria dan Bobot",
            "Perhitungan MOORA",
            "Hasil Perangkingan"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("""
        <div style="font-size:12px; color:#475569; line-height:1.7; background: #f8fafc; padding: 14px; border-radius: 10px; border: 1px solid #e2e8f0;">
            <b>Metode:</b> MOORA<br>
            <b>Alternatif:</b> 6 Laptop<br>
            <b>Kriteria:</b> 6 Parameter<br><br>
            <span style="color:#059669; font-size:11px; font-weight:700;">
                ⚡ Decision Support System Core
            </span>
        </div>
    """, unsafe_allow_html=True)


# =========================================================
# 7. HALAMAN BERANDA
# =========================================================

if menu == "Beranda":

    st.markdown("""
        <div class="hero">
            <div class="section-label" style="color: #a7f3d0;">
                ✨ SISTEM PENDUKUNG KEPUTUSAN
            </div>
            <h1>Selamat Datang di SPK Pemilihan Laptop</h1>
            <p>
                Platform cerdas rekomendasi pemilihan laptop modern
                menggunakan metode MOORA berdasarkan kriteria terbobot
                secara presisi dan transparan.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Ringkasan Sistem")

    col1, col2, col3, col4 = st.columns(4)

    statistik = [
        ("💻", "Alternatif Laptop", str(len(df))),
        ("📊", "Kriteria Penilaian", str(len(kriteria))),
        ("⚖️", "Total Bobot", "100%"),
        ("🧮", "Metode", "MOORA")
    ]

    for col, item in zip(
        [col1, col2, col3, col4],
        statistik
    ):
        with col:
            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-label">{item[0]} {item[1]}</div>
                    <div class="stat-value">{item[2]}</div>
                    <div class="stat-caption">Sistem pemilihan laptop</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("### Rekomendasi Terbaik")

    terbaik = hasil.iloc[0]

    st.markdown(f"""
        <div class="winner-card">
            <div class="winner-label">
                🏆 ALTERNATIF DENGAN PERINGKAT PERTAMA
            </div>
            <div class="winner-name">
                {terbaik["Nama Laptop"]}
            </div>
            <div class="winner-score">
                Kode {terbaik["Kode"]} &nbsp; • &nbsp;
                Nilai Yi: {terbaik["Nilai Yi"]:.4f}
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Gambaran Sistem")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Tujuan Aplikasi")
        st.write(
            "Membantu proses pemilihan laptop dengan "
            "melakukan penilaian terhadap beberapa alternatif "
            "berdasarkan enam kriteria."
        )

    with col2:
        st.markdown("#### Metode Perhitungan")
        st.write(
            "Metode MOORA melakukan normalisasi matriks, "
            "pembobotan kriteria, perhitungan nilai optimasi, "
            "dan perangkingan alternatif."
        )

    st.info(
        "Gunakan menu navigasi di sebelah kiri untuk "
        "melihat data, kriteria, proses perhitungan, "
        "dan hasil rekomendasi."
    )


# =========================================================
# 8. HALAMAN DATA ALTERNATIF
# =========================================================

elif menu == "Data Alternatif":

    st.markdown(
        '<div class="section-label">📁 DATA MASTER</div>',
        unsafe_allow_html=True
    )

    st.title("Data Alternatif Laptop")

    st.write(
        "Daftar alternatif laptop yang digunakan "
        "sebagai objek penilaian dalam sistem."
    )

    col1, col2 = st.columns([3, 1])

    with col1:
        st.metric("Total Alternatif", len(df))

    with col2:
        st.metric("Total Kriteria", len(kriteria))

    st.markdown("### Tabel Data Alternatif")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=300
    )

    st.caption(
        "Sumber: Matriks keputusan alternatif pada "
        "artikel Rusadin, Tatuhey, dan Lahallo (2024)."
    )


# =========================================================
# 9. HALAMAN KRITERIA DAN BOBOT
# =========================================================

elif menu == "Kriteria dan Bobot":

    st.markdown(
        '<div class="section-label">⚙️ PREFERENSI PENILAIAN</div>',
        unsafe_allow_html=True
    )

    st.title("Kriteria dan Bobot")

    st.write(
        "Kriteria merupakan faktor yang digunakan "
        "dalam proses penilaian alternatif laptop."
    )

    st.markdown("### Bobot Setiap Kriteria")

    kolom = st.columns(3)

    for i, nama in enumerate(kriteria):

        with kolom[i % 3]:

            jenis = atribut[nama]

            st.markdown(f"""
                <div class="criterion-card">
                    <div class="criterion-name">{nama}</div>
                    <div class="criterion-weight">
                        {bobot[nama] * 100:.0f}%
                    </div>
                    <div class="criterion-type">
                        Jenis: {jenis}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("### Tabel Kriteria")

    data_kriteria = pd.DataFrame({
        "Kode": ["C1", "C2", "C3", "C4", "C5", "C6"],
        "Nama Kriteria": kriteria,
        "Bobot": [bobot[k] for k in kriteria],
        "Jenis Atribut": [atribut[k] for k in kriteria]
    })

    st.dataframe(
        data_kriteria,
        use_container_width=True,
        hide_index=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.success(
            "BENEFIT: semakin besar nilai, semakin "
            "diutamakan."
        )

    with col2:
        st.warning(
            "COST: semakin kecil nilai, semakin "
            "diutamakan."
        )

    st.metric(
        "Total Bobot",
        f"{sum(bobot.values()) * 100:.0f}%"
    )


# =========================================================
# 10. HALAMAN PERHITUNGAN MOORA
# =========================================================

elif menu == "Perhitungan MOORA":

    st.markdown(
        '<div class="section-label">📊 PROSES ANALISIS</div>',
        unsafe_allow_html=True
    )

    st.title("Perhitungan Metode MOORA")

    st.write(
        "Berikut merupakan tahapan perhitungan "
        "menggunakan metode MOORA."
    )

    # Tahap 1
    with st.expander(
        "01. Matriks Keputusan",
        expanded=True
    ):

        st.write(
            "Matriks keputusan berisi nilai setiap "
            "alternatif berdasarkan seluruh kriteria."
        )

        st.dataframe(
            df.set_index(
                ["Kode", "Nama Laptop"]
            )[kriteria],
            use_container_width=True
        )

    # Tahap 2
    with st.expander(
        "02. Matriks Normalisasi",
        expanded=True
    ):

        st.write(
            "Normalisasi dilakukan dengan membagi nilai "
            "setiap alternatif dengan akar jumlah kuadrat "
            "nilai pada masing-masing kriteria."
        )

        st.latex(
            r"x_{ij}^{*} = "
            r"\frac{x_{ij}}"
            r"{\sqrt{\sum_{i=1}^{m}x_{ij}^{2}}}"
        )

        st.dataframe(
            normalisasi.round(4),
            use_container_width=True
        )

    # Tahap 3
    with st.expander(
        "03. Matriks Normalisasi Terbobot",
        expanded=True
    ):

        st.write(
            "Hasil normalisasi dikalikan dengan "
            "bobot masing-masing kriteria."
        )

        st.dataframe(
            terbobot.round(4),
            use_container_width=True
        )

    # Tahap 4
    with st.expander(
        "04. Perhitungan Nilai Optimasi",
        expanded=True
    ):

        st.write(
            "Nilai optimasi dihitung dengan mengurangi "
            "total nilai kriteria Benefit dengan "
            "total nilai kriteria Cost."
        )

        st.latex(
            r"Y_i = \sum Benefit - \sum Cost"
        )

        tabel_optimasi = hasil[
            [
                "Kode",
                "Nama Laptop",
                "Nilai Benefit",
                "Nilai Cost",
                "Nilai Yi"
            ]
        ].copy()

        st.dataframe(
            tabel_optimasi.round(4),
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# 11. HALAMAN HASIL PERANGKINGAN
# =========================================================

elif menu == "Hasil Perangkingan":

    st.markdown(
        '<div class="section-label">🏆 HASIL ANALISIS</div>',
        unsafe_allow_html=True
    )

    st.title("Hasil Perangkingan Laptop")

    st.write(
        "Perangkingan dilakukan berdasarkan nilai "
        "optimasi MOORA. Nilai Yi tertinggi menjadi "
        "alternatif dengan peringkat terbaik."
    )

    terbaik = hasil.iloc[0]

    st.markdown(f"""
        <div class="winner-card">
            <div class="winner-label">
                🏆 REKOMENDASI LAPTOP TERBAIK
            </div>
            <div class="winner-name">
                {terbaik["Nama Laptop"]}
            </div>
            <div class="winner-score">
                Peringkat 1 &nbsp; • &nbsp;
                Nilai Yi: {terbaik["Nilai Yi"]:.4f}
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Daftar Perangkingan")

    tabel_ranking = hasil[
        [
            "Peringkat",
            "Kode",
            "Nama Laptop",
            "Nilai Yi"
        ]
    ].copy()

    tabel_ranking["Nilai Yi"] = (
        tabel_ranking["Nilai Yi"].round(4)
    )

    st.dataframe(
        tabel_ranking,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Grafik Perbandingan Nilai Yi")

    grafik = hasil[
        ["Nama Laptop", "Nilai Yi"]
    ].set_index("Nama Laptop")

    st.bar_chart(
        grafik,
        horizontal=True
    )

    st.caption(
        "Alternatif dengan nilai Yi tertinggi "
        "merupakan alternatif terbaik berdasarkan "
        "data dan bobot yang digunakan."
    )


# =========================================================
# 12. FOOTER
# =========================================================

st.markdown("""
    <div class="footer">
        <b>SPK PEMILIHAN LAPTOP | METODE MOORA</b><br>
        Sistem Pendukung Keputusan Pemilihan Laptop<br>
        Adaptasi penelitian Rusadin, Tatuhey, dan Lahallo (2024)
    </div>
""", unsafe_allow_html=True)