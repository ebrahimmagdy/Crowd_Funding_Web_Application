from django.test import TestCase
from home.models.project import Project


class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project()
        self.project.title = 'First project'
        self.project.details = 'This is the first project details'
        self.project.save()

    def test_read(self):
        print(self.project.id)
        self.assertEqual(self.project.title, 'First project')
