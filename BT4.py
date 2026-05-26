def processEmployeeDeclaration():
    print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
    
    while True:
        try:
            employeeCount = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
            
            if employeeCount <= 0:
                print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.")
            else:
                print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {employeeCount} nhân sự mới!")
                break
        except ValueError:
            print("[LỖI] Dữ liệu nhập vào không phải là số nguyên! Vui lòng thử lại.")
            
    print("--- CHƯƠNG TRÌNH KẾT THÚC ---")

if __name__ == "__main__":
    processEmployeeDeclaration()