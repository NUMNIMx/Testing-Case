
# ไฟล์ my_list.py
- ฟังก์ชัน **find_max** หาค่าสูงสุดในรายการ
- ฟังก์ชัน **find_min** หาค่าต่ำสุดในรายการ
- ฟังก์ชัน **find_average** หาค่าเฉลี่ยในรายการ
- ฟังก์ชัน **is_sorted** ตรวจสอบว่ารายการถูกเรียงลำดับจากน้อยไปมากหรือไม่
- ฟังก์ชัน **reverse_list** พลิกกลับรายการ

# ไฟล์ test_my_list.py
- แต่ละฟังก์ชันทดสอบฟังก์ชันที่เกี่ยวข้องใน my_list.py
- เทสเคส assertEqual เปรียบเทียบผลลัพธ์ที่ได้กับผลลัพธ์ที่คาดหวัง

## เริ่มการ Test case
```bash
$ python -m unittest -v test_my_list
```