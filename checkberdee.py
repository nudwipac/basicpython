def checkberdee(phone_number=0):
    # สร้าง program ผลรวมเบอร์
    total = 0
    # ตัวแปรทำนายผล
    predict = ""
    # Loop ผลรวมเบอร์
    for phone in phone_number:
        total += int(phone)

    print(total)

    # ทำนายผลรวม
    if total in (4, 5, 6, 9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54):
        predict = "ดีมากกกก"
    elif total in (63, 64, 65, 69, 79):
        predict = "โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข"
    elif total in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57):
        predict = "ให้คุณระดับดีปานกลาง"
    elif total in (58, 60, 6162, 66, 68, 74, 75):
        predict = "เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม"
    elif total in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73):
        predict = "ให้โทษ ใครได้ผลรวมเหล่านี้ควรเปลี่ยน"
    elif total in (76, 77, 78, 80):
        predict = "เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น"
    else:
        predict = "ไม่มีข้อมูล"
    return predict


# Call FUNC
phone = input("Input phone number")
print(checkberdee(phone))
