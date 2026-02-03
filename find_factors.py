def factorCal(calNum, calFactor):
    j = 0
    for i in range(0, calNum):
        j += 1
        if j % calFactor == 0:
            print(j, end = " ")

print("โปรแกรมหาตัวประกอบทั้งหมดของจำนวนที่ผู้ใช้ป้อน")
num = int(input("ระบุจำนวนตัวเลข "))
factor = int(input("ระบุเลขตัวประกอบ "))
print(f"จากเลข {num} หาตัวประกอบด้วย {factor} จะได้", end = " ")
factorCal(num, factor)
