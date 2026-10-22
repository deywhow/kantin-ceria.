
import streamlit as st

st.set_page_config(
    page_title="Kantin Ceria",
    page_icon="🍱",
    layout="wide"
)

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
