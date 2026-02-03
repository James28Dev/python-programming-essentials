print("โปรแกรมหาค่าผลรวมของเลขที่หาร 3 ลงตัว ตั้งแต่ 1 ถึงเลขที่ต้องการ")
end_number = int(input("เลขสูงสุด : "))
def sums_can_divided_by_3(end_num):
  total = 0
  for num in range(1, end_num + 1):
    if num % 3 == 0:
      total += num
  return total
print(f"ผลรวมของเลขที่หาร 3 ลงตัว ตั้งแต่ 1 - {end_number} คือ {sums_can_divided_by_3(end_number)}")
