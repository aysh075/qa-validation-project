def validate_name(name):
    """İstifadəçi adının boş olub-olmadığını yoxlayan funksiya."""
    if not name or name.strip() == "":
        return False, "Имя не может быть пустым!"
    return True, name.strip()

def validate_age(age_input):
    """Yaşın düzgün formatda (rəqəm və müsbət) olduğunu yoxlayan funksiya."""
    try:
        age = int(age_input)
        if age <= 0:
            return False, "Возраст должен быть больше нуля!"
        if age > 120:
            return False, "Возраст выглядит нереалистичным!"
        return True, age
    except ValueError:
        return False, "Возраст должен быть числом!"

def register_user(name_input, age_input):
    """Qeydiyyatı tamamlayan əsas funksiya (Bir funksiya - bir tapşırıq)."""
    is_name_valid, name_res = validate_name(name_input)
    if not is_name_valid:
        return {"success": False, "error": name_res}

    is_age_valid, age_res = validate_age(age_input)
    if not is_age_valid:
        return {"success": False, "error": age_res}

    return {
        "success": True,
        "message": f"Пользователь {name_res} ({age_res} лет) успешно зарегистрирован!"
    }

if __name__ == "__main__":
    print("--- Программа регистрации пользователей ---")
    u_name = input("Введите имя: ")
    u_age = input("Введите возраст: ")

    result = register_user(u_name, u_age)
    if result["success"]:
        print("✅", result["message"])
    else:
        print("❌ Ошибка:", result["error"])