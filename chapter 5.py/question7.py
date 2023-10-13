def seats_A(seats_A):
    return seats_A * 20
def seats_B(seats_B):
    return seats_B * 15
def seats_C(seats_C):
    return seats_C * 10
seatsa_count = int(input("how mant ticket for class A of seat were sold "))
seatsb_count = int(input("how mant ticket for class B of seat were sold "))
seatsc_count = int(input("how mant ticket for class C of seat were sold "))

print(f"{seats_A(seatsa_count)}")
print(f"{seats_A(seatsb_count)}")
print(f"{seats_A(seatsc_count)}")       
total_income= seatsa_count + seatsb_count + seatsc_count
print(f"Total income from all seats: ${total_income}")

    