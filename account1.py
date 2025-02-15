def sum_of_list(numbers):
    """Hàm tính tổng các số trong một danh sách."""
    return sum(numbers)

def average_of_list(numbers):
    """Hàm tính giá trị trung bình của các số trong danh sách."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def max_of_list(numbers):
    """Hàm tìm số lớn nhất trong danh sách."""
    if len(numbers) == 0:
        return None
    return max(numbers)

def min_of_list(numbers):
    """Hàm tìm số nhỏ nhất trong danh sách."""
    if len(numbers) == 0:
        return None
    return min(numbers)

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    print(f"Tổng của danh sách {sample_list} là: {sum_of_list(sample_list)}")
    print(f"Giá trị trung bình của danh sách {sample_list} là: {average_of_list(sample_list)}")
    print(f"Số lớn nhất trong danh sách {sample_list} là: {max_of_list(sample_list)}")
    print(f"Số nhỏ nhất trong danh sách {sample_list} là: {min_of_list(sample_list)}")
