from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_sequence_state import EndUserSequenceState

from apps.core.serializers import EndUserSerializer

# tests for api views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_end_user(id="", vendor_branch=""):
        if id != "" and vendor_branch != "":
            EndUser.objects.create(id=id, vendor_branch=vendor_branch)

    def setUp(self):
        # add test data
        self.create_end_user("1", "sean paul")
        self.create_end_user("2", "konshens")
        self.create_end_user("3", "brick and lace")
        self.create_end_user("4", "damien marley")


class GetAllEndUsersTest(BaseViewTest):

    def test_get_all_end_users(self):
        """
        This test ensures that all end_users added in the setUp method
        exist when we make a GET request to the end_users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("end_users-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = EndUser.objects.all()
        serialized = EndUserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)