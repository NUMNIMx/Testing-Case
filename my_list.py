def find_max(list1):
    """
    ฟังก์ชันสำหรับหาค่าสูงสุดในรายการ

    Args:
        list1 (list): รายการตัวเลข

    Returns:
        int: ค่าสูงสุดในรายการ
    """
    if len(list1) == 0:
        return None
    max_value = list1[0]
    for i in range(1, len(list1)):
        if list1[i] > max_value:
            max_value = list1[i]
    return max_value

def find_min(list1):
    """
    ฟังก์ชันสำหรับหาค่าต่ำสุดในรายการ

    Args:
        list1 (list): รายการตัวเลข

    Returns:
        int: ค่าต่ำสุดในรายการ
    """
    if len(list1) == 0:
        return None
    min_value = list1[0]
    for i in range(1, len(list1)):
        if list1[i] < min_value:
            min_value = list1[i]
    return min_value

def find_average(list1):
    """
    ฟังก์ชันสำหรับหาค่าเฉลี่ยในรายการ

    Args:
        list1 (list): รายการตัวเลข

    Returns:
        float: ค่าเฉลี่ยในรายการ
    """
    if len(list1) == 0:
        return None
    sum_value = 0
    for i in range(len(list1)):
        sum_value += list1[i]
    return sum_value / len(list1)

def is_sorted(list1):
    """
    ฟังก์ชันสำหรับตรวจสอบว่ารายการถูกเรียงลำดับจากน้อยไปมากหรือไม่

    Args:
        list1 (list): รายการตัวเลข

    Returns:
        bool: True ถ้ารายการเรียงลำดับจากน้อยไปมาก False ถ้าไม่
    """
    for i in range(1, len(list1)):
        if list1[i] < list1[i - 1]:
            return False
    return True

def reverse_list(list1):
    """
    ฟังก์ชันสำหรับพลิกกลับรายการ

    Args:
        list1 (list): รายการตัวเลข

    Returns:
        list: รายการที่ถูกพลิกกลับ
    """
    new_list = []
    for i in range(len(list1) - 1, -1, -1):
        new_list.append(list1[i])
    return new_list
