# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from autharmor_python.models.users_credentials_response_page_info import UsersCredentialsResponsePageInfo  # noqa: E501

class TestUsersCredentialsResponsePageInfo(unittest.TestCase):
    """UsersCredentialsResponsePageInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersCredentialsResponsePageInfo:
        """Test UsersCredentialsResponsePageInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersCredentialsResponsePageInfo`
        """
        model = UsersCredentialsResponsePageInfo()  # noqa: E501
        if include_optional:
            return UsersCredentialsResponsePageInfo(
                currnet_page_number = 56,
                currnet_page_size = 56,
                total_page_count = 56,
                total_record_count = 56
            )
        else:
            return UsersCredentialsResponsePageInfo(
        )
        """

    def testUsersCredentialsResponsePageInfo(self):
        """Test UsersCredentialsResponsePageInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()