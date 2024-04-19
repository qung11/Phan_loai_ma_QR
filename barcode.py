from pyzbar.pyzbar import decode
import cv2
import serial
import time
# Khai báo đại diện cho các giá trị của mã barcode
#barcode1 = "ABC-abc-1234"
#barcode2 = "123456"
#barcodes = [barcode1, barcode2]

# Khởi tạo camera
cap = cv2.VideoCapture(0)
# Khởi tạo danh sách để lưu trữ nội dung của mã Barcode
Barcode_codes = []
if __name__== '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()


while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()

    # Chuyển đổi ảnh từ không gian màu BGR sang xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Nhận diện mã barcode trong ảnh
    barcodes = decode(gray)

    for barcode in barcodes:
        data1 = barcode.data.decode("utf-8")
        # Tách phần nội dung mong muốn bằng phương thức split()
        if data1 not in Barcode_codes:
            # Lấy phần nội dung thứ hai trong chuỗi
            content = data1[0:8]
            # Lưu trữ và hiển thị phần nội dung đã tách
            Barcode_codes.append((data1))
            with open('Barcode_codes.txt', 'a') as f:
                f.write(content + '\n')
            print("Barcode: ", content)


        # Kiểm tra nếu mã vạch là loại CODE128
       # if barcode.type == "CODE128":
          #  print("Mã barcode loại CODE128")
            # Thực hiện các hành động tương ứng với việc tìm thấy mã barcode
        if data1 == "20161355":
            ser.write(b"1\n")
            
            data1=" "
            content = "   "
            dt=ser.readline().decode().rstrip()
            print(dt)
            
            
        if data1 == "20161106":
            ser.write(b"2\n")
            
            data1=" "
            content = "   "
            dt=ser.readline().decode().rstrip()
            print(dt)
        if data1 == "20161299":
            ser.write(b"3\n")
            
            data1=" "
            content = "   "
            dt=ser.readline().decode().rstrip()
            print(dt)   
        
        # Vẽ khung bao quanh mã barcode
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 150, 0), 2)
        # Hiển thị mã barcode đã giải mã lên khung màn hình camera
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(gray, data1, (x, y - 10), font, 0.5, (0, 150, 0), 2)

        # Giảm kích thước ảnh xuống còn 640x480
        frame = cv2.resize(frame, (550, 360))

    # Hiển thị ảnh lên màn hình
    cv2.imshow('Nhan dien BARCODE', frame)

    # Nếu người dùng bấm phím 'q', thoát chương trình
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên camera và đóng tất cả các cửa sổ hiển thị
cap.release()
ser.close()
cv2.destroyAllWindows()