
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(
    page_title="Kantin Ceria",
    page_icon="🍱",
    layout="wide"
)
credentials = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

gc = gspread.authorize(credentials)
SPREADSHEET_ID = "14JjCKxm9-bTVPaQgRzh7C3Y0rdtrX6_m1HiLljQJmpk"

try:
    spreadsheet = gc.open_by_key(SPREADSHEET_ID)
    st.success("Spreadsheet berhasil ditemukan!")
    st.write("Nama file:", spreadsheet.title)

    Sheet = spreadsheet.worksheet(
        "Riwayat Transaksi Kantin Kejujuran X ALG kel 1"
    )

except Exception as e:
    st.error(f"Koneksi Google Sheets gagal: {type(e).__name__}")
                                                 
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff4e6, #e5f7ee);
}
h1, h2, h3 {
    color: #226448;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.85);
    border-radius: 16px;
}
.stButton > button {
    background: #21865b;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
/* Opening screen */
#kantin-opening {
    position: fixed;
    inset: 0;
    z-index: 999999;
    background: linear-gradient(145deg, #173d31, #21865b);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    animation: opening-exit 4.2s ease-in-out forwards;
}
/* Opening full-screen */
#kantin-opening {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999999;
    background: linear-gradient(135deg, #173d31, #21865b);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    animation: opening-exit 7s ease forwards;
}

#kantin-opening .opening-line {
    position: absolute;
    width: 90%;
    left: 5%;
    top: 50%;
    margin: 0;
    color: #ffffff !important;
    font-family: Arial, sans-serif;
    font-size: clamp(28px, 5vw, 48px);
    font-weight: 800;
    line-height: 1.3;
    text-align: center;
    transform: translateY(-50%);
    opacity: 0;
    visibility: hidden;
}

#kantin-opening .opening-one {
    animation: show-one 7s linear forwards;
}

#kantin-opening .opening-two {
    animation: show-two 7s linear forwards;
}

#kantin-opening .opening-three {
    animation: show-three 7s linear forwards;
}

@keyframes show-one {
    0% { opacity: 0; visibility: visible; transform: translateY(25px) scale(.85); }
    8%, 25% { opacity: 1; visibility: visible; transform: translateY(-50%) scale(1); }
    32%, 100% { opacity: 0; visibility: hidden; transform: translateY(-80px); }
}

@keyframes show-two {
    0%, 29% { opacity: 0; visibility: hidden; transform: translateY(25px); }
    30% { visibility: visible; }
    36%, 52% { opacity: 1; visibility: visible; transform: translateY(-50%); }
    60%, 100% { opacity: 0; visibility: hidden; transform: translateY(-80px); }
}

@keyframes show-three {
    0%, 57% { opacity: 0; visibility: hidden; transform: translateY(25px); }
    58% { visibility: visible; }
    65%, 82% { opacity: 1; visibility: visible; transform: translateY(-50%); }
    90%, 100% { opacity: 0; visibility: hidden; transform: translateY(-80px); }
}

@keyframes opening-exit {
    0%, 85% { opacity: 1; visibility: visible; }
    100% { opacity: 0; visibility: hidden; pointer-events: none; }
}

/* Konten utama muncul dari bawah */
.stMainBlockContainer {
    animation: main-enter 1s ease-out 5.8s both;
}

@keyframes main-enter {
    from { opacity: 0; transform: translateY(45px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Main content enters */
.stMainBlockContainer {
    animation: main-enter 1s ease-out 2.8s both;
}

@keyframes main-enter {
    from { opacity: 0; transform: translateY(45px); }
    to { opacity: 1; transform: translateY(0); }
}
/* Teks halaman muncul bergantian */
.stMainBlockContainer h1 {
    animation: textFadeUp 0.8s ease-out both;
}

.stMainBlockContainer h2 {
    animation: textSlideIn 0.8s ease-out both;
}

.stMainBlockContainer h3 {
    animation: textFadeUp 0.7s ease-out both;
}

/* Kartu produk muncul dari bawah */
[data-testid="stVerticalBlockBorderWrapper"] {
    animation: productEnter 0.75s ease-out both;
    transition: transform 0.3s ease,
                box-shadow 0.3s ease;
}

/* Efek ketika kursor menyentuh kartu */
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 24px rgba(33, 134, 91, 0.18);
}

/* Efek tombol */
.stButton > button {
    transition: transform 0.2s ease,
                background-color 0.2s ease;
}

.stButton > button:hover {
    transform: scale(1.04);
}

/* Gerakan animasi */
@keyframes textFadeUp {
    from {
        opacity: 0;
        transform: translateY(24px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes textSlideIn {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes productEnter {
    from {
        opacity: 0;
        transform: translateY(28px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

produk = {
    "Jus Fauzan": {
        "harga": 5000,
        "varian": ["Melon", "Mangga", "Semangka", "Jambu"],
        "emoji": "🧃"
    },
    "Puding Jihan": {
        "harga": 8000,
        "varian": ["Melon", "Original", "Strawberry", "Cokelat"],
        "emoji": "🍮"
    },
    "Buah Potong Segar": {
        "harga": 6000,
        "varian": ["Melon", "Semangka", "Mangga"],
        "emoji": "🍉"
    },
    "Es Kul Kul + Cokelat": {
        "harga": 3000,
        "varian": ["Pisang", "Melon", "Semangka", "Marshmallow"],
        "emoji": "🍫"
    },
    "Macaroni Schotel": {
        "harga": 8000,
        "varian": ["Original"],
        "emoji": "🧀"
    }
}

if "keranjang" not in st.session_state:
    st.session_state.keranjang = {}

if "struk" not in st.session_state:
    st.session_state.struk = None

st.markdown("""
<div id="kantin-opening">
    <div class="opening-line opening-one">
        Hai! 👋
    </div>
    <div class="opening-line opening-two">
        Lagi pengin jajan apa?
    </div>
    <div class="opening-line opening-three">
        Yuk, cari favoritmu!
    </div>
</div>
""", unsafe_allow_html=True)
st.title("🍱 KANTIN CERIA")
st.write("✨ Jajan enak, belanja mudah, transaksi jujur!")
st.caption("Pilih produk favoritmu dan masukkan ke keranjang.")

st.subheader("🛍️ Daftar Produk")

kolom = st.columns(2)

for i, (nama, info) in enumerate(produk.items()):
    with kolom[i % 2]:
        with st.container(border=True):
            st.markdown(f"## {info['emoji']} {nama}")
            st.markdown(
                f"### Rp{info['harga']:,}".replace(",", ".")
            )

            if nama == "Buah Potong Segar":
                st.caption("Melon, semangka, dan mangga.")
            elif nama == "Es Kul Kul + Cokelat":
                st.caption("Buah atau marshmallow dengan cokelat.")

            varian = st.selectbox(
                "Pilih varian",
                info["varian"],
                key="varian_" + nama
            )

            jumlah = st.number_input(
                "Jumlah pesanan",
                min_value=1,
                max_value=99,
                value=1,
                step=1,
                key="jumlah_" + nama
            )

            if st.button(
                "➕ Tambahkan ke keranjang",
                key="tambah_" + nama,
                use_container_width=True
            ):
                kunci = f"{nama} — {varian}"
                keranjang = st.session_state.keranjang
                keranjang[kunci] = (
                    keranjang.get(kunci, 0) + jumlah
                )
                st.session_state.struk = None
                st.rerun()

st.divider()
st.subheader("🛒 Keranjang Belanja")

keranjang = st.session_state.keranjang
total = 0

if not keranjang:
    st.info("Keranjang masih kosong. Yuk, pilih produk!")
else:
    for kunci, jumlah in list(keranjang.items()):
        nama, varian = kunci.split(" — ", 1)
        harga = produk[nama]["harga"]
        subtotal = harga * jumlah
        total += subtotal

        a, b, c = st.columns([3, 2, 1])
        a.write(f"**{nama}**")
        a.caption(f"Varian: {varian}")
        b.write(f"{jumlah} × Rp{harga:,}".replace(",", "."))
        c.write(f"Rp{subtotal:,}".replace(",", "."))

        if st.button("Hapus", key="hapus_" + kunci):
            del keranjang[kunci]
            st.session_state.struk = None
            st.rerun()

    st.markdown(
        f"## 💰 Total: Rp{total:,}".replace(",", ".")
    )

    st.divider()
    st.subheader("💳 Pembayaran")

    pembeli = st.text_input("Nama pembeli")
    bayar = st.number_input(
        "Uang pembayaran (Rp)",
        min_value=0,
        step=1000,
        value=0
    )

    if st.button("✅ Proses Pembayaran", use_container_width=True):
        if not pembeli.strip():
            st.warning("Masukkan nama pembeli terlebih dahulu.")
        elif bayar < total:
            st.error("Uang pembayaran masih kurang.")
        else:
            st.session_state.struk = {
                "pembeli": pembeli,
                "total": total,
                "bayar": bayar,
                "kembalian": bayar - total,
                "pesanan": dict(keranjang)
            }
            st.session_state.keranjang = {}
            st.rerun()

if st.session_state.struk:
    st.balloons()
    struk = st.session_state.struk

    st.divider()
    st.subheader("🧾 Struk Pembayaran")
    st.success("Pembayaran berhasil! Terima kasih sudah berbelanja.")

    st.write(f"**Nama pembeli:** {struk['pembeli']}")

    for kunci, jumlah in struk["pesanan"].items():
        nama, varian = kunci.split(" — ", 1)
        harga = produk[nama]["harga"]
        st.write(
            f"- {nama} ({varian}) × {jumlah} = "
            f"Rp{harga * jumlah:,}".replace(",", ".")
        )

    st.write(f"**Total:** Rp{struk['total']:,}".replace(",", "."))
    st.write(f"**Uang bayar:** Rp{struk['bayar']:,}".replace(",", "."))
    st.write(
        f"**Kembalian:** Rp{struk['kembalian']:,}".replace(",", ".")
    )

    if st.button("🛍️ Transaksi Baru"):
        st.session_state.struk = None
        st.rerun()

st.divider()
st.caption("💚 Kantin Ceria | Belanja jujur, hati gembira!")
