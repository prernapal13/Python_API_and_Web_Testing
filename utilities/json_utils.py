import json
import jsonpath
import logging


class JsonUtils:
    """
    This class is for maintaining the utilities related to json objects
    """

    def get_request_body(self):
        """
        This method is to get json body from resources folder
        :return: json body
        """
        file_content = open(".\\resources\\request_body.json", 'r')
        request_body = json.loads(file_content.read())
        return request_body

    def get_jsonpath_value(self, json_response, key):
        """
        This method is to navigate in the json and to get the value of desired key
        :param json_response: response received from API
        :param key: key for which the value needs to be retrieved
        :return: value of given key as string
        """
        value = jsonpath.jsonpath(json_response, key)[0]
        logging.info("# {0}: {1}".format(key, value))
        return value