# ฟังก์ชันคำนวณเกรด
def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# ฟังก์ชันหลัก
def main():
    print("โปรแกรมคำนวณเกรดนักเรียน 🎓")
    try:
        # รับคะแนนจากผู้ใช้
        score = float(input("ป้อนคะแนน (0-100): "))
        
        # ตรวจสอบว่าคะแนนอยู่ในช่วงที่ถูกต้องหรือไม่
        if 0 <= score <= 100:
            grade = calculate_grade(score)  # คำนวณเกรด
            print(f"เกรดของคุณคือ: {grade}")
        else:
            print("กรุณาป้อนคะแนนระหว่าง 0 ถึง 100 เท่านั้น!")
    except ValueError:
        print("โปรดป้อนตัวเลขเท่านั้น!")

# เริ่มโปรแกรม
main()