#5_func.py

def return_info(name, phone, address, email):
    contact_info = f"연락처\t{phone}\n이메일:\t{email}"
    return f"이름:\t{name}\n{contact_info}\n주소:\t{address}"

def print_info(name, phone, address, email = ""):
    contact_info = f"연락처:\t{phone}\n이메일:\t{email}"
    print(f"이름:\t{name}\n{contact_info}\n주소:\t{address}")
    
print_info("Aaron", "010-5555-5555", "전주")
person = return_info(email="hi@email", phone="010-1111-1111",
                     address="교통대학교", name="Aaron"
                     )
print()
print(person)
    
