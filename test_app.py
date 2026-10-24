import unittest
from app import validate_name, validate_age, register_user

class TestUserRegistration(unittest.TestCase):

     def test_valid_data(self):
         """Düzgün məlumatlar daxil edildikdə uğurlu qeydiyyat testi."""
         result = register_user("Айшан", "25")
         self.assertTrue(result["success"])
         self.assertIn("успешно зарегистрирован", result["message"])

     def test_empty_name(self):
         """Ad boş buraxıldıqda xətanın tutulması testi."""
         is_valid, msg = validate_name("")
         self.assertFalse(is_valid)
         self.assertEqual(msg, "Имя не может быть пустым!")

     def test_age_is_not_number(self):
          """Yaş yerinə hərf yazıldıqda proqramın çökməməsi testi."""
          is_valid, msg = validate_age("abc")
          self.assertFalse(is_valid)
          self.assertEqual(msg, "Возраст должен быть числом!")

     def test_negative_age(self):
        """Mənfi yaş daxil edildikdə xətanın idarə olunması testi."""
        is_valid, msg = validate_age("-5")
        self.assertFalse(is_valid)
        self.assertEqual(msg, "Возраст должен быть больше нуля!")

if __name__ == "__main__":
    unittest.main()