THIỆP CƯỚI ONLINE NHẬT & MY — PHIÊN BẢN NHÀ TRAI ĐƠN GIẢN

BẢN NÀY DÙNG CHO VM NHÀ TRAI. Phiên bản thiệp đầy đủ nhà gái được giữ trong bride-full/.

NỘI DUNG ĐÃ LƯỢC BỎ
- Không dùng ảnh cưới dọc riêng cho hero mobile; ảnh ngang vẫn được giữ cho desktop.
- Hero có ba dòng lời mời: “TRÂN TRỌNG KÍNH MỜI”, “QUÝ KHÁCH”, “TỚI DỰ LỄ THÀNH HÔN”. Cả ba dùng class hero-date-main; riêng “QUÝ KHÁCH” lớn hơn nhẹ, còn font và màu được kế thừa từ hero-date-main.
- Lịch trình chỉ giữ box “Tiệc đám vui nhà trai”; hai box nhà gái và lễ thành hôn đã được gỡ khỏi HTML.
- Đã gỡ section album ảnh và liên kết album khỏi menu/câu chuyện.
- Khung ảnh trang trí trong phần “Câu chuyện” vẫn được giữ; không còn tương tác mở album.

CẤU TRÚC
- index.html: thiệp nhà trai đơn giản.
- admin.html, admin.js, admin.css: trang quản trị, chỉ nằm trong phiên bản nhà trai.
- qr-code.html: tiện ích tạo mã QR, chỉ nằm trong phiên bản nhà trai.
- script.js: RSVP, sổ lưu bút, bản đồ, ngôn ngữ, nhạc nền và tương tác còn dùng.
- Thời gian và ngày âm lịch trong hero được làm đậm hơn; box lịch trình nhà trai có thêm dòng ngày âm đậm, tự đổi theo ngôn ngữ.
- Phần RSVP bỏ tiêu đề câu hỏi và câu hướng dẫn xác nhận; chỉ giữ câu “Sự hiện diện của Quý khách sẽ làm ngày vui của gia đình chúng tôi thêm trọn vẹn!” với cỡ chữ lớn, đậm.
- site-config.js: thông tin cô dâu chú rể và sự kiện.
- styles.css, design-system.css, responsive.css, layout-system.css: CSS nguồn.
- groom-simple.css: điều chỉnh riêng cho phiên bản đơn giản.
- site.min.css: CSS build dùng bởi website.
- SQL quản trị được lưu ở ../database/supabase-admin-setup.sql trong gói hai phiên bản, không nằm trong thư mục public web.

CẬP NHẬT CSS
Chạy `python build-css.py` trong thư mục này sau khi sửa CSS nguồn.

DEPLOY
- Triển khai nội dung thư mục groom-simple/ lên VM nhà trai bằng job Jenkins riêng.
- Chỉ mở admin trên VM nhà trai; vẫn phải dùng xác thực và RLS để bảo vệ dữ liệu.
- Không đưa thư mục database/ hoặc file SQL vào document root.
- Không đưa service_role key vào frontend; chỉ dùng publishable/anon key.
- Trước khi gửi khách, kiểm thử RSVP, bản đồ nhà trai, ngôn ngữ, menu, mobile và admin.

Typography maintenance (2026-10-23): letter spacing has been normalized across page sections, Google Fonts now requests the used 400–700 weights, and build-css.py preserves spaces before CSS pseudo-selectors such as :is(). Run `python build-css.py` after editing source CSS.
