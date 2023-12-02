# from django.test import TestCase, Client
# from django.urls import reverse
# from accounts.models import CustomUser,owner

# class ViewTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = CustomUser.objects.create_user(email='test123@gmail.com', password='Sojn@574',is_active='True',user_type='manager',first_name='test',contact='1234567890')

#     def test_landing_view_authenticated(self):
#         response = self.client.get(reverse('landing'))
#         self.assertTemplateUsed(response,'landing.html')

#         self.client.login(email='test123@gmail.com', password='Sojn@574')
#         response = self.client.get(reverse('landing'))
#         self.assertRedirects(response, '/dashboard',302,301)  # Assuming /dashboard/ is the expected redirection

#     def test_login_view_authenticated(self):
#         self.client.login(email='test123@gmail.com', password='Sojn@574')
#         response = self.client.get(reverse('login'))
#         self.assertRedirects(response, '/dashboard',302,301) 
        
#     def test_login_view_valid_post(self):
        
#         response = self.client.post(reverse('login'), {'email': 'test123@gmail.com', 'password': 'Sojn@574'})
#         self.assertRedirects(response, '/dashboard',302,301)  # Assuming /dashboard/ is the expected redirection

   

#     def test_logout_view(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect after logout

#     def test_home_view_authenticated(self):
#         self.client.login(email='test123@gmail.com', password='Sojn@574')
#         response = self.client.get(reverse('dashboard'))
#         self.assertEqual(response.status_code, 200)  # Assuming home page should return 200 for authenticated user

#     def test_register_view_authenticated(self):
#         self.client.login(email='test123@gmail.com', password='Sojn@574')
#         response = self.client.get(reverse('register'))
#         self.assertRedirects(response, '/dashboard',302,301) 
        
#     def test_register_view_unthenticated(self):
#         self.client.login(email='test13@gmail.com', password='Sojn@574')
#         response = self.client.get(reverse('register'))  #cheaking else condition
#         self.assertTemplateUsed(response,'register.html')

#     def test_register_view_authenticated(self):
#         self.client.login(email='test123@gmail.com', password='Sojn@574')
#         response = self.client.get(reverse('register'))
#         self.assertRedirects(response, '/dashboard',302,301) 
    
#     def test_register_view_owner_authenticated(self):
#         response = self.client.post(reverse('reg_owner'), {'first_name':'ojas','email': 'test12@gmail.com', 'password1': 'Sojn@574', 'password1': 'Sojn@574','company_ name':'daiict','contact':'1234567890'})  #cheaking else condition
#         self.assertTemplateUsed(response, 'owner/register_as_admin.html')
    
#     def test_register_view_manager_authenticated(self):
#         response = self.client.post(reverse('reg_manager'), {'first_name':'ojas','email': 'manager1@gmail.com', 'password1': 'Sojn@574', 'password1': 'Sojn@574','company_ name':'daiict','contact':'1234567890'})  #cheaking else condition
#         self.assertTemplateUsed(response, 'manager/register_as_manager.html')
    
#     def test_register_view_employee_authenticated(self):
#         response = self.client.post(reverse('reg_employee'), {'first_name':'ojas','email': 'emplyee1@gmail.com', 'password1': 'Sojn@574', 'password1': 'Sojn@574','company_ name':'daiict','contact':'1234567890'})  #cheaking else condition
#         self.assertTemplateUsed(response, 'employee/register_as_employee.html')
