a = int(input("Nhập giá trị số nguyên dương:"))

def tongCacChuSo(a):
    total = 0
    while (a > 0):
        # Số dư là số cuối cùng trong dãy số
        total = total + a % 10
        # Kiểm tra và lấy phần số còn lại của số a
        a = int(a/10)
    return total

print("Tổng các chữ số của số nguyên dương a là", + tongCacChuSo(a))


"""
input = 2022
total = 0 + 2
a = 2022 / 10 = 202

total = 2 + 2 
a = 202 / 10 = 20

total = 4 + 0
a = 20  / 10 = 2

total = 2 + 2 + 0 + 2 
a = 2 / 10 = 0

total = 6

"""
