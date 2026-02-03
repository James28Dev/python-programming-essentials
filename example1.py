#โปรแกรมแสดงชื่อตามจำนวนที่ต้องการ
def my_function(fname, num):
    for x in range(0, num):
        print(fname)
my_function("Emil", 2)
my_function("Jaksit", 1)

#โปรแกรมคำนวณพื้นที่วงกลม
def circle(radius):
    area = 22.0 / 7.0 * radius * radius
    print(f"Area = {area:.2f}")
circle(15)
circle(10.5)

#โปรแกรมคำนวณพื้นที่สามเหลี่ยม
def triangle(base, height):
  return 0.5 * base * height
base = float(input("Enter base : ")) #input() รับข้อมูลจากคีย์บอร์ด
height = float(input("Enter height : "))
print(f"Triangle area = {triangle(base, height):.2f}") #:.2f แสดงทศนิยม 2 ตำแหน่ง

#โปรแกรมบวกเลข
def sum(a, b):
    return (a + b)
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(f"{a} + {b} = {sum(a, b)}")
