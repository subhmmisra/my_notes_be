from rest_framework.test import APITestCase
from apps.notes.models import Note
from apps.notes.tests.factories import create_note
from apps.notes.tests.utils import BadRequestErrorMixin
from django.urls import reverse


class NoteTestCase(BadRequestErrorMixin, APITestCase):
    '''this test case deals with creation of notes'''
    def setUp(self):
        self.note_response_keys = {
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
        }
        self.note_data = {
            "title": "My Frist Note",
            "description": "Sample Description"
        }

        self.url = reverse("notes-v1-add")
        self.request_method = "post"
    
    def test_note_response(self):
        response = self.get_api_response(self.url, request_method=self.request_method, data=self.note_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], self.note_data['title'])
        self.assertSetEqual(self.note_response_keys, set(response.data))
    
    def test_note_without_title(self):
        note_data = {
            "description": "Sample Description"
        }
        response = self.get_api_response(self.url, request_method=self.request_method, data=note_data)
        self.assertEqual(response.status_code, 400)

    def test_note_without_description(self):
        note_data = {
            "title": "Sample Description"
        }
        response = self.get_api_response(self.url, request_method=self.request_method, data=note_data)
        self.assertEqual(response.status_code, 400)



class NoteListTestCase(BadRequestErrorMixin, APITestCase):
    '''this testcase deals with listing of notes'''
    def setUp(self):
        self.note_list_response_keys = {
            "count",
            "next",
            "previous",
            "results",
        }

        self.result_response_keys = {
            "id",
            "title",
            "description",
            "created_at",
            "updated_at"
        }

        self.note_obj = create_note(
            title="My First Note",
            description= "Sample description"
        )
        self.note_obj_2 = create_note(
            title="My Second Note",
            description= "Sample description"
        )

        self.note_obj_3 = create_note(
            title="My Third Note",
            description= "Sample description"
        )

        self.url = reverse("notes-v1-list")
        self.request_method = "get"
    
    def test_note_list_response(self):
        response = self.get_api_response(self.url, request_method=self.request_method)
        self.assertEqual(response.status_code, 200)
        self.assertSetEqual(self.note_list_response_keys, set(response.data))
    

    def test_note_created_list(self):
        response = self.get_api_response(self.url, request_method=self.request_method)
        self.assertEqual(response.status_code, 200)
        self.assertSetEqual(self.note_list_response_keys, set(response.data))
        self.assertEqual(response.data['results'][0]['title'], self.note_obj.title)
    

    def test_count_pagination(self):
        response = self.get_api_response(self.url, request_method=self.request_method)
        self.assertEqual(response.status_code, 200)
        self.assertSetEqual(self.note_list_response_keys, set(response.data))
        self.assertEqual(response.data['count'], 3)
    
    def test_search_title(self):
        self.url = self.url + '?title=third'
        response = self.get_api_response(self.url, request_method=self.request_method)
        self.assertEqual(response.status_code, 200)
        self.assertSetEqual(self.note_list_response_keys, set(response.data))
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], self.note_obj_3.title)



class NoteUpdateTestCase(BadRequestErrorMixin, APITestCase):
    '''this test case deals with notes update'''
    def setUp(self):
        self.result_response_keys = {
            "id",
            "title",
            "description",
            "created_at",
            "updated_at"
        }

        self.note_obj = create_note(
            title="My First Note",
            description= "Sample description"
        )

        self.note_data = {
            "title": "My Updated Note",
            "description": "Sample Description"
        }

        self.url = reverse("notes-v1-detail", args=[str(self.note_obj.id)])
        self.request_method = "put"
    
    def test_note_update_response(self):
        self.assertEqual(self.note_obj.title, 'My First Note')
        response = self.get_api_response(self.url, request_method=self.request_method, data=self.note_data)
        self.assertEqual(response.status_code, 200)
        note_obj = Note.objects.filter(id=self.note_obj.id).first()
        self.assertEqual(note_obj.title, self.note_data['title'])
        self.assertSetEqual(self.result_response_keys, set(response.data))


class NoteDeleteTestCase(BadRequestErrorMixin, APITestCase):
    '''this testcase deals with the deletion of notes and listing'''
    def setUp(self):
        self.result_response_keys = {
            "id",
            "title",
            "description",
            "created_at",
            "updated_at"
        }

        self.note_obj = create_note(
            title="My First Note",
            description= "Sample description"
        )

        self.note_obj_2 = create_note(
            title="My Second Note",
            description= "Sample description"
        )

        self.url = reverse("notes-v1-detail", args=[str(self.note_obj.id)])
        self.request_method = "delete"
    
    def test_note_update_response(self):
        '''check if two notes are available'''
        url = reverse("notes-v1-list")
        request_method = "get"
        response = self.get_api_response(url, request_method=request_method)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 2)
        #------------------------------------------
        '''delete the note_obj and then re-verify'''
        response = self.get_api_response(self.url, request_method=self.request_method)
        self.assertEqual(response.status_code, 204)
        #------------------------------------------
        response = self.get_api_response(url, request_method=request_method)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)