dem = 1

while dem <= 3:
    print("\n==============================")
    print(f"NHẬP THÔNG TIN NHÂN VIÊN THỨ {dem}")
    print("==============================")

    employee_id = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")

    # Kiểm tra bẫy dữ liệu
    if employee_id.strip() == "" or employee_name.strip() == "":
        print("\n🚨 CẢNH BÁO ĐỎ:")
        print("Mã nhân viên hoặc Họ tên không được để trống!")
        print("Hồ sơ không hợp lệ. Không thể in phiếu hồ sơ.")
    else:
        # In phiếu hồ sơ điện tử
        print("\n========== PHIẾU HỒ SƠ ĐIỆN TỬ ==========")
        print(f"Mã nhân viên : {employee_id}")
        print(f"Họ và tên    : {employee_name}")
        print(f"Phòng ban    : {department}")
        print("=========================================")

    dem += 1

print("\n Đã hoàn thành nhập hồ sơ cho 3 nhân viên.")
print("Chương trình kết thúc.")