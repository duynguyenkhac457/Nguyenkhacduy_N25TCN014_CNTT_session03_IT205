print('---Hệ thống gửi email nhân viên tết ---')

for employee_number in range(1, 4):
    print('---Đang xử lý nhân viên số', employee_number, '---')

    working_days = int(input('Nhập số ngày công trong tháng:'))

    if working_days == 0:
        print('Cảnh báo: nhân viên nghỉ cả tháng, không xét duyệt thưởng.')
    
    elif working_days >= 20:
        bonus_amount = working_days * 200000
        print('-> Đã gửi emial: Chúc mừng nhận được', bonus_amount, 'VND tiền thưởng!')
        print('-------------------------------------------------')

print('Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!')