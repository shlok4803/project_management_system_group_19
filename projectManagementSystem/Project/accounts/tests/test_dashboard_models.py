# from django.test import TestCase
# from dashboard.models import project, Task, message

# class ProjectModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
       
#         project.objects.create(
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

#     def test_project_title(self):
#         project_instance = project.objects.get(projectID='PRJ123456')
#         expected_object_name = f'{project_instance.projectTitle}'
#         self.assertEqual(expected_object_name, 'Test Project')

    

# class TaskModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
       
#         project_instance = project.objects.create(
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
#         Task.objects.create(
#             taskID='TSK123456',
#             taskTitle='Test Task',
#             description='Test Task Description',
#             deadline='2023-12-31T23:59:59Z',
#             submitted=None,
#             completed=None,
#             assignedDate='2023-01-01T00:00:00Z',
#             employeeName='Test Employee',
#             employeeEmail='employee@example.com',
#             projectID=project_instance,
#             managerName='Test Manager',
#             managerEmail='manager@example.com',
#             late=False,
#             decline=False,
#             status='I'
#         )

#     def test_task_title(self):
#         task_instance = Task.objects.get(taskID='TSK123456')
#         expected_object_name = f'{task_instance.taskTitle}'
#         self.assertEqual(expected_object_name, 'Test Task')

# class MessageModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         message.objects.create(
#             chatID='test-chat-id',
#             prevMessage='Previous Message',
#             text='Test Message Content',
#             senderName='Sender',
#             senderEmail='sender@example.com',
#             role='E'
#         )

#     def test_chatID_max_length(self):
#         msg = message.objects.get(chatID='test-chat-id')
#         max_length = msg._meta.get_field('chatID').max_length
#         self.assertEqual(max_length, 15)

#     def test_senderEmail_unique(self):
#         msg = message.objects.get(chatID='test-chat-id')
#         is_unique = msg._meta.get_field('senderEmail').unique
#         self.assertFalse(is_unique)  

