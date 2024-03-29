# coding: utf-8

"""
    Callchimp Public API

    ## Introduction👋 Introducing OpenAPI spec for doing almost anything in [callchimp.ai](https://callchimp.ai). CallChimp is a Gen AI Call Center Enhancing telecommunication with GPT-driven bulk calling. It is scalable, user-friendly, and customizable. Optimized for seamless integration and usability. ## API Categories📋 The APIs are divided in 7 categories listed below:   - Campaigns   - Supervisors   - Lists   - Subscribers   - Calls   - Phone Numbers   - Webhooks  ## API Operations✅ ### Campaign Operations    - List all Campaigns   - Create a Campaign   - Get Campaign by Id   - Delete Campaign by Id   - Update Campaign by Id   - Add Supervisors to Campaign by Id   - Remove Supervisors from Campaign by Id   - Upload audio file to Campaign by Id  ### Supervisor Operations    - List all Supervisors   - Create a Supervisor   - Get Supervisor by Id   - Delete Supervisor by Id   - Update Supervisor by Id   - Send OTP to Campaign by Id   - Verify Supervisor OTP by Id  ### List Operations    - List all Lists   - Create a List   - Get List by Id   - Delete List by Id   - Update List by Id  ### Subscriber Operations    - List all Subscribers   - Create one or more Subscriber(s)   - Get Subscriber by Id   - Delete Subscriber by Id   - Update Subscriber by Id  ### Call Operations    - List outbound Calls   - Create a Call   - Get Call by Id   - List Inbound Calls   - Generate Call Reports  ### Phone Number Operations    - List Phone Numbers  ### Webhook Operations    - List all Webhooks   - Create a Webhook   - Get Webhook by Id   - Delete Webhook by Id   - Update Webhook by Id  ## Authentication🔐 CallChimp public API offers authentication with API Keys. All endpoints accepts a header named `x-api-key`. To get started follow the below steps:    1. Login to callchimp dashboard.   2. Click on your profile on the top-right corner.   3. Click on Settings.   4. On the settings page, click on `API Keys` from the left sidebar.   5. Click on `Add new` button, add an expiry date and click on `Add`.   6. An API Key will be generated, please save the key somewhere safe as it won't be shown again!   7. You can use the API Key directly here in this playground to test out the APIs. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from callchimp.api.webhooks_api import WebhooksApi


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_webhooks_delete(self) -> None:
        """Test case for webhooks_delete

        Delete Webhook by Id
        """
        pass

    def test_webhooks_get(self) -> None:
        """Test case for webhooks_get

        Get Webhook by Id
        """
        pass

    def test_webhooks_list(self) -> None:
        """Test case for webhooks_list

        List Webhooks
        """
        pass

    def test_webhooks_post(self) -> None:
        """Test case for webhooks_post

        Create a Webhook
        """
        pass

    def test_webhooks_update(self) -> None:
        """Test case for webhooks_update

        Update Webhook by Id
        """
        pass


if __name__ == '__main__':
    unittest.main()
