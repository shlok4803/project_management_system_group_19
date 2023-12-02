# from django.test import TestCase, Client
# from django.urls import reverse
# from accounts.models import CustomUser,owner,manager,employee
# from django.contrib.auth import get_user_model
# from dashboard.models import project, Task

# class TestViews(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user_owner = CustomUser.objects.create_user(
#             email='owner@gmail.com', password='Owner@123',is_active='True',user_type='owner',first_name='owner',contact='1234567890'  # Adjust this based on your user creation logic
#         )
#         self.user_manager = CustomUser.objects.create_user(
#             email='manager@gmail.com', password='Manager@123',is_active='True',user_type='manager',first_name='manager',contact='1234567890'  # Adjust this based on your user creation logic
#         )
#         self.user_owner = CustomUser.objects.create_user(
#             email='employee@gmail.com', password='Empl@123',is_active='True',user_type='employee',first_name='employee',contact='1234567890'  # Adjust this based on your user creation logic
#         )
        
#         self.project = project.objects.create(
#             projectID='PRJ123456',
#             projectTitle='Test Project',
#             description='Test Description',
#             deadline='2023-12-31T23:59:59Z',
#             created='2023-01-01T00:00:00Z',
#             managerName='Test Manager',
#             managerEmail='manager@example.com',
#             ownerName='Test Owner',
#             ownerEmail='owner@example.com',
#             status='O',
#             chat='NULL'
#         )
#         self.task = Task.objects.create(
#             taskID='TSK123456',
#             taskTitle='Test Task',
#             description='Test Task Description',
#             deadline='2023-12-31T23:59:59Z',
#             submitted=None,
#             completed=None,
#             assignedDate='2023-01-01T00:00:00Z',
#             employeeName='Test Employee',
#             employeeEmail='employee@example.com',
#             projectID=self.project,
#             managerName='Test Manager',
#             managerEmail='manager@example.com',
#             late=False,
#             decline=False,
#             status='I'
#         )

#     def test_dashboard_view_owner(self):
#         self.client.login(email='owner@gmail.com', password='Owner@123')
#         response = self.client.get('/dashboard_owner/')
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response, 'owner/dashboard_owner.html')
       
    
#     def test_dashboard_view_manager(self):
#         self.client.login(email='manager@gmail.com', password='Manager@123')
#         response = self.client.get('/dashboard/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'manager/dashboard_manager.html')

#     def test_dashboard_view_employee(self):
#         self.client.login(email='employee@gmail.com', password='Empl@123')
#         response = self.client.get('/dashboard/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'employee/dashboard_employee.html')
       
#     class TestViews(TestCase):
#         def setUp(self):
#             self.client = Client()
       

  