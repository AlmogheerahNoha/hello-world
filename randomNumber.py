import random
import string

# 1. Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Hàm tạo chuỗi ngẫu nhiên
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# 3. Hàm tính giai thừa đệ quy
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# 4. Hàm kiểm tra chuỗi có đối xứng (Palindrome) không
def is_palindrome(s):
    return s == s[::-1]

# 5. Hàm tìm số Fibonacci thứ n
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 6. Hàm đếm số từ trong một chuỗi
def word_count(s):
    return len(s.split())

# 7. Hàm đổi chỗ hai biến mà không cần biến tạm
def swap(a, b):
    return b, a

# 8. Hàm tìm số lớn nhất trong danh sách
def max_in_list(lst):
    return max(lst) if lst else None

# 9. Hàm chuyển đổi nhiệt độ từ Celsius sang Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 10. Hàm tính tổng các số trong danh sách
def sum_list(lst):
    return sum(lst)

# Kiểm tra nhanh
if __name__ == "__main__":
    print("Số nguyên tố:", is_prime(17))
    print("Chuỗi ngẫu nhiên:", random_string())
    print("Giai thừa của 5:", factorial(5))
    print("Palindrome:", is_palindrome("madam"))
    print("Số Fibonacci thứ 10:", fibonacci(10))
    print("Số từ trong câu:", word_count("ChatGPT là AI mạnh mẽ"))
    print("Hoán đổi:", swap(3, 7))
    print("Số lớn nhất:", max_in_list([1, 9, 3, 7, 5]))
    print("25 độ C -> Fahrenheit:", celsius_to_fahrenheit(25))
    print("Tổng danh sách:", sum_list([1, 2, 3, 4, 5]))
