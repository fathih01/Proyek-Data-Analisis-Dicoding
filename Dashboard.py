import streamlit as st 

st.write(
     """
    # Dashboard Visualisasi Data Analisis
    By : Fathih Muhammad Alfi
    """
)

st.subheader('Dataset yang digunakan')
st.markdown('<div style="text-align: justify;">Dataset berisi kumpulan data publik e-commerce Brasil mengenai pesanan yang dilakukan di Olist Store. Kumpulan data tersebut memiliki informasi 100 ribu pesanan dari tahun 2016 hingga 2018 yang dilakukan di beberapa pasar di Brasil. Fitur-fiturnya memungkinkan melihat pesanan dari berbagai dimensi: mulai dari status pesanan, harga, pembayaran dan kinerja pengiriman hingga lokasi pelanggan, atribut produk, dan akhirnya ulasan yang ditulis oleh pelanggan. Anda dapat mendownload dataset pada link di bawah</div>', unsafe_allow_html=True)

st.write("Dataset : [E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")


st.write('----------------------------------------------------------------------------------------')

st.subheader('Mendefinisikan Pertanyaan')
st.write('1. Dimanakah daerah yang merupakan segmentasi pasar dari E-Commerce?')
st.write('2. Bagaimana tingkat keberhasilan dari pesanan yang dilakukan customer?')
st.write('3. Bagaimana tingkat kepuasan customer terhadap E-Commerce berdasarkan history order keseluruhan?')

st.write('----------------------------------------------------------------------------------------')


st.subheader('Visualisasi Data Hasil Analisis')

st.write("1. Daerah yang merupakan segmentasi pasar dari E-Commerce")
st.image("Daerah.png")
with st.expander("See explanation"):
    st.markdown('<div style="text-align: justify;">Sao Paulo, Rio de Jeniero, dan Belo Horizonte merupakan 3 daerah dengan transaksi paling besar. Dengan mengetahui daerah daerah yang melakukan transaksi paling besar, kita dapat mengatur strategi untuk mempertahankan pelanggan di lokasi tersebut. Contohnya seperti Kampanye Pemasaran Berbasis Lokasi: Sesuaikan kampanye pemasaran E-Commerce berdasarkan lokasi geografis pelanggan. Penawaran atau promosi yang relevan dengan kebutuhan lokal dapat menarik minat pelanggan.kita juga dapat melakukan Kolaborasi dengan Bisnis Lokal: Kerjasama dengan bisnis lokal di daerah-daerah tersebut bisa menjadi strategi yang efektif. Misalnya, menawarkan diskon bersama dengan restoran atau toko lain yang populer di daerah tersebut.</div>', unsafe_allow_html=True)
 
st.write('----------------------------------------------------------------------------------------')

st.write("2. Tingkat keberhasilan dari pesanan yang dilakukan customer")
st.image("transaksi.png")
with st.expander("See explanation"):
    st.markdown('<div style="text-align: justify;">Berdasarkan hasil visualisasi dapat kita lihat bahwa 97% dari orderan telah berhasil dikirim. sehingga dapat kita katakan bahwa tingkat keberhasilan sangat baik. Jadi kita hanya perlu melanjutkan proses bisnis yang sedang berjalan saat ini.</div>', unsafe_allow_html=True)
 
st.write('----------------------------------------------------------------------------------------')

st.write("3. Tingkat kepuasan customer terhadap E-Commerce berdasarkan history order keseluruhan")
st.image("review.png")
with st.expander("See explanation"):
    st.markdown('<div style="text-align: justify;">Berdasarkan hasil visualisasi, dapat kita lihat bahwasannya cukup banyak konsumen yang memberikan review dengan nilai 1 (11.5%). Tentunya hal itu tidak dapat dibiarkan, sehingga team perlu mencari tau penyebab dari consumen memberikan nilai review yang sangat rendah. Ada beberapa penyebab seperti Kualitas Produk yang Buruk, Pelayanan Pelanggan yang Buruk, Pengiriman yang Lambat atau Rusak, Perbedaan Antara Produk yang Diterima dan Deskripsi Online, dll. Dengan mengetahui penyebabnya kita dapat mengatur strategi seperti melakukan peninjauan kembali dengan pihak2 yang bekerja sama, melakukan pengawasan terhadap toko2 yang ada di E-Commerce, hingga memutus kerja sama dengan pihak yang di rasa membuat citra dari E-Commerce kita menurun dan membuat kerja sama dengan pihak baru yang lebih baik. Dengan begitu kita dapat menyelesaikan masalah review tadi dan mempertahankan konsumen kita untuk tidak beralih ke E-Commerce lain.</div>', unsafe_allow_html=True)

st.write('----------------------------------------------------------------------------------------')

st.caption('Fathih Muhammad Alfi | 2023')
