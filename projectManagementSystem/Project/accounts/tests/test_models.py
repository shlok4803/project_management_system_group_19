# from django.test import TestCase
# from accounts.models import CustomUser, owner, manager, employee

# class CustomUserModelTestCase(TestCase):
#     def setUp(self):
#         # Create a sample user for testing
#         self.user = CustomUser.objects.create_user(
#             email='test@example.com',
#             password='testpassword',
#             first_name='John',
#             contact='1234567890'
#         )

#     def test_custom_user_creation(self):
#         # Test if the user was created successfully
#         self.assertEqual(self.user.email, 'test@example.com')
#         self.assertTrue(self.user.check_password('testpassword'))
#         self.assertEqual(self.user.first_name, 'John')
#         self.assertEqual(self.user.contact, '1234567890')

#     def test_owner_creation(self):
#         # Test creating an owner
#         owner_user = owner.objects.create(
#             email='owner@example.com',
#             first_name='Alice',
#             contact='9876543210',
#             company_name='ABC Corp'
#         )
#         owner_user.set_password('ownerpassword')  # Set the password explicitly
#         owner_user.save()  # Save the user after setting the password
#         self.assertTrue(owner_user.check_password('ownerpassword'))  # Check the password

#     def test_manager_creation(self):
#         # Test creating a manager
#         test_owner = owner.objects.create(
#             email='owner@example.com',
#             first_name='Alice',
#             contact='9876543210',
#             company_name='ABC Corp'
#         )
#         manager_user = manager.objects.create(
#             email='manager@example.com',
#             first_name='Bob',
#             contact='5555555555',
#             company_name=test_owner
#         )
#         manager_user.set_password('managerpassword')  # Set the password explicitly
#         manager_user.save()  # Save the user after setting the password
#         self.assertTrue(manager_user.check_password('managerpassword'))  # Check the password
#     def test_employee_creation(self):
#         # Test creating an employee
#         test_owner = owner.objects.create(
#             email='owner@example.com',
#             first_name='Alice',
#             contact='9876543210',
#             company_name='ABC Corp'
#         )
#         employee_user = employee.objects.create(
#             email='employee@example.com',
#             first_name='Charlie',
#             contact='1111111111',
#             company_name=test_owner
#         )
#         employee_user.set_password('employeepassword')  
#         employee_user.save()  # Save the user after setting the password
#         self.assertTrue(employee_user.check_password('employeepassword'))  # Check the password
#         self.assertEqual(employee_user.email, 'employee@example.com')
#         self.assertEqual(employee_user.first_name, 'Charlie')
#         self.assertEqual(employee_user.contact, '1111111111')
#         self.assertEqual(employee_user.company_name, test_owner)