from calculator import divide, add
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide_normal():
    # Kiểm thử dữ liệu hợp lệ
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # Kiểm thử dữ liệu biên (chia cho 0 phải văng ra lỗi ValueError)
    with pytest.raises(ValueError, match="Không thể chia cho 0"):
        divide(10, 0)