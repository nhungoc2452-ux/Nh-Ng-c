import streamlit as st
from PIL import Image

# =====================
# CẤU HÌNH GIAO DIỆN
# =====================

st.set_page_config(
    page_title="Tính thuế TNCN",
    page_icon="💰",
    layout="centered"
)

# =====================
# HIỂN THỊ ẢNH
# =====================

try:
    image = Image.open("anh.jpg")
    st.image(image, width=180)
except:
    st.warning("Chưa tìm thấy ảnh. Hãy đặt ảnh tên 'anh_cua_ban.jpg' trong cùng thư mục.")

# Tiêu đề
st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN_Phạm Thị Như Ngọc")
st.write("Tính thuế TNCN từ tiền lương, tiền công theo biểu thuế lũy tiến từng phần.")

st.divider()


# =====================
# NHẬP DỮ LIỆU
# =====================

st.subheader("📌 Nhập thông tin cá nhân")

luong = st.number_input(
    "Thu nhập chịu thuế/tháng (VNĐ)",
    min_value=0,
    value=30000000,
    step=1000000
)

bao_hiem = st.number_input(
    "Các khoản bảo hiểm bắt buộc (VNĐ)",
    min_value=0,
    value=3150000,
    step=100000
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)


# =====================
# TÍNH THUẾ
# =====================

def tinh_thue(thu_nhap_tinh_thue):

    if thu_nhap_tinh_thue <= 0:
        return 0

    elif thu_nhap_tinh_thue <= 5_000_000:
        return thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 10_000_000:
        return thu_nhap_tinh_thue * 0.1 - 250_000

    elif thu_nhap_tinh_thue <= 18_000_000:
        return thu_nhap_tinh_thue * 0.15 - 750_000

    elif thu_nhap_tinh_thue <= 32_000_000:
        return thu_nhap_tinh_thue * 0.2 - 1_650_000

    elif thu_nhap_tinh_thue <= 52_000_000:
        return thu_nhap_tinh_thue * 0.25 - 3_250_000

    elif thu_nhap_tinh_thue <= 80_000_000:
        return thu_nhap_tinh_thue * 0.3 - 5_850_000

    else:
        return thu_nhap_tinh_thue * 0.35 - 9_850_000



# =====================
# NÚT TÍNH
# =====================

if st.button("🧮 Tính thuế TNCN"):

    giam_tru_ban_than = 11_000_000
    giam_tru_nguoi_phu_thuoc = 4_400_000

    thu_nhap_tinh_thue = (
        luong
        - bao_hiem
        - giam_tru_ban_than
        - nguoi_phu_thuoc * giam_tru_nguoi_phu_thuoc
    )

    thue = tinh_thue(thu_nhap_tinh_thue)


    # =====================
    # HIỂN THỊ KẾT QUẢ
    # =====================

    st.divider()

    st.subheader("📊 Kết quả tính toán")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Thu nhập tính thuế",
            f"{thu_nhap_tinh_thue:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Thuế TNCN phải nộp",
            f"{thue:,.0f} VNĐ"
        )


    st.success(
        f"Số thuế thu nhập cá nhân phải nộp là: {thue:,.0f} VNĐ/tháng"
    )


# =====================
# THÔNG TIN
# =====================

st.divider()

st.caption(
    "Ứng dụng tính thuế TNCN phục vụ mục đích học tập."
)
