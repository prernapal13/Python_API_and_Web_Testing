import json
import logging
import unittest

import requests

from utilities.json_utils import JsonUtils

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ApiTests(unittest.TestCase):
    """
    This class is to write test cases related to public APIs on https://reqres.in/ 
    """

    def setUp(self):
        self.url = "https://reqres.in/"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.json_util = JsonUtils()

    def test_get_single_user(self, id=2, first_name="Janet", last_name="Weaver"):
        """
        This method is to test GET request for a single user on https://reqres.in/ 
        :param id: id for which user details are fetched
        :param first_name: expected first name for given id
        :param last_name: expected last name for given id
        """
        url = self.url + "api/users/" + str(id)
        logging.info("# GET url: " + url)

        response = requests.get(url)
        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)

        json_response = json.loads(response.text)
        actual_id = self.json_util.get_jsonpath_value(json_response, "data.id")
        actual_first_name = self.json_util.get_jsonpath_value(json_response, "data.first_name")
        actual_last_name = self.json_util.get_jsonpath_value(json_response, "data.last_name")

        assert actual_id == id, "actual id '{0}' should be same as expected id '{1}'.".format(actual_id, id)
        assert actual_first_name == first_name, \
            "actual first name '{0}' should be same as expected first name '{1}'.".format(actual_first_name, first_name)
        assert actual_last_name == last_name, \
            "actual last name '{0}' should be same as expected last name '{1}'.".format(actual_last_name, last_name)

    def test_post_create_new_user(self, name='Prerna Pal', job='QA Engineer'):
        """
        This method is to test POST request for creating a new user on https://reqres.in/
        :param name: name of the new user to be created
        :param job: job of the new user to be created
        """
        url = self.url + "api/users"
        logging.info("# POST url: " + url)

        body = self.json_util.get_request_body()
        response = requests.post(url, data=json.dumps(body), headers=self.headers)
        actual_status_code = response.status_code
        json_response = json.loads(response.text)
        actual_name = self.json_util.get_jsonpath_value(json_response, "name")
        actual_job = self.json_util.get_jsonpath_value(json_response, "job")

        assert actual_status_code == 201, "status code {0} should be 201.".format(actual_status_code)
        assert actual_name == name, "actual name '{0}' should be same as expected name '{1}'.".format(actual_name, name)
        assert actual_job == job, "actual job '{0}' should be same as expected job '{1}'.".format(actual_job, job)

    def test_put_update_user_details(self, id=2, name='Prerna Pal', job='QA Engineer'):
        """
        This method is to test PUT request for updating an existing user on https://reqres.in/
        :param id: id of the user to be updated
        :param name: new name of the user
        :param job: new job of the user
        """
        url = self.url + "api/users/" + str(id)
        logging.info("# PUT url: " + url)
        body = self.json_util.get_request_body()

        response = requests.put(url, data=json.dumps(body), headers=self.headers)
        actual_status_code = response.status_code
        json_response = json.loads(response.text)
        actual_name = self.json_util.get_jsonpath_value(json_response, "name")
        actual_job = self.json_util.get_jsonpath_value(json_response, "job")

        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)
        assert actual_name == name, "actual name '{0}' should be same as expected name '{1}'.".format(actual_name, name)
        assert actual_job == job, "actual job '{0}' should be same as expected job '{1}'.".format(actual_job, job)

    def test_delete_existing_user(self, id=2):
        """
        This method is to test DELETE request for deleting an existing user on https://reqres.in/
        :param id: id of the user to be deleted
        """
        url = self.url + "api/users/" + str(id)
        logging.info("# DELETE url: " + url)
        response = requests.delete(url)
        assert response.status_code == 204, "status code {0} should be 204.".format(response.status_code)


if __name__ == '__main__':
    unittest.main()