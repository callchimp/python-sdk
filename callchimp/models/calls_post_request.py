# coding: utf-8

"""
    Callchimp Public API

    ## Introduction👋 Introducing OpenAPI spec for doing almost anything in [callchimp.ai](https://callchimp.ai). CallChimp is a Gen AI Call Center Enhancing telecommunication with GPT-driven bulk calling. It is scalable, user-friendly, and customizable. Optimized for seamless integration and usability. ## API Categories📋 The APIs are divided in 9 categories listed below:   - Campaigns   - Supervisors   - Lists   - Subscribers   - Calls   - Phone Numbers   - Webhooks   - Scripts   - Voices  ## API Operations✅ ### Campaign Operations    - List Campaigns   - Create a Campaign   - Get Campaign by Id   - Delete Campaign by Id   - Update Campaign by Id   - Add Supervisors to Campaign by Id   - Remove Supervisors from Campaign by Id   - Upload audio file to Campaign by Id   - Search Campaign by Name or Id  ### Supervisor Operations    - List Supervisors   - Create a Supervisor   - Get Supervisor by Id   - Delete Supervisor by Id   - Update Supervisor by Id   - Send OTP to Supervisor by Id   - Verify Supervisor OTP by Id  ### List Operations    - List Lists   - Create a List   - Get List by Id   - Delete List by Id   - Update List by Id   - Search List by Name or Id   - Create Campaign with Default List  ### Subscriber Operations    - List Subscribers   - Create one or more Subscriber(s)   - Get Subscriber by Id   - Delete Subscriber by Id   - Update Subscriber by Id   - Get Subscriber by Vendor Lead Code   - Delete Subscriber by Vendor Lead Code   - Update Subscriber by Vendor Lead Code  ### Call Operations    - List Calls   - Create a Call   - Get Call by Id   - List Supervisor Inbound Calls   - Generate Call Reports  ### Phone Number Operations    - List Phone Numbers  ### Webhook Operations    - List Webhooks   - Create a Webhook   - Get Webhook by Id   - Delete Webhook by Id   - Update Webhook by Id  ### Script Operations    - List Scripts   - Create a Script   - Get Script by Id   - Delete Script by Id   - Update Script by Id  ### Voice Operations   - List Available Voices  ## Authentication🔐 Callchimp public API offers authentication with API Keys. All endpoints accepts a header named `x-api-key`. To get started follow the below steps:    1. Login to callchimp dashboard.   2. Click on your profile on the top-right corner.   3. Click on Settings.   4. On the settings page, click on `API Keys` tab.   5. Click on `Create` button, add a name and an expiry date and click on `Add`.   6. An API Key will be generated, please save the key somewhere safe as it won't be shown again!   7. You can use the API Key directly here in this playground to test out the APIs. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from callchimp.models.call_request_by_lead_id import CallRequestByLeadId
from callchimp.models.call_request_by_vendor_lead_code import CallRequestByVendorLeadCode
from callchimp.models.transaction_call_request_by_lead_id import TransactionCallRequestByLeadId
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

CALLSPOSTREQUEST_ANY_OF_SCHEMAS = ["CallRequestByLeadId", "CallRequestByVendorLeadCode", "TransactionCallRequestByLeadId"]

class CallsPostRequest(BaseModel):
    """
    CallsPostRequest
    """

    # data type: CallRequestByLeadId
    anyof_schema_1_validator: Optional[CallRequestByLeadId] = None
    # data type: TransactionCallRequestByLeadId
    anyof_schema_2_validator: Optional[TransactionCallRequestByLeadId] = None
    # data type: CallRequestByVendorLeadCode
    anyof_schema_3_validator: Optional[CallRequestByVendorLeadCode] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[CallRequestByLeadId, CallRequestByVendorLeadCode, TransactionCallRequestByLeadId]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "CallRequestByLeadId", "CallRequestByVendorLeadCode", "TransactionCallRequestByLeadId" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = CallsPostRequest.model_construct()
        error_messages = []
        # validate data type: CallRequestByLeadId
        if not isinstance(v, CallRequestByLeadId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CallRequestByLeadId`")
        else:
            return v

        # validate data type: TransactionCallRequestByLeadId
        if not isinstance(v, TransactionCallRequestByLeadId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionCallRequestByLeadId`")
        else:
            return v

        # validate data type: CallRequestByVendorLeadCode
        if not isinstance(v, CallRequestByVendorLeadCode):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CallRequestByVendorLeadCode`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in CallsPostRequest with anyOf schemas: CallRequestByLeadId, CallRequestByVendorLeadCode, TransactionCallRequestByLeadId. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[CallRequestByLeadId] = None
        try:
            instance.actual_instance = CallRequestByLeadId.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[TransactionCallRequestByLeadId] = None
        try:
            instance.actual_instance = TransactionCallRequestByLeadId.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[CallRequestByVendorLeadCode] = None
        try:
            instance.actual_instance = CallRequestByVendorLeadCode.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CallsPostRequest with anyOf schemas: CallRequestByLeadId, CallRequestByVendorLeadCode, TransactionCallRequestByLeadId. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CallRequestByLeadId, CallRequestByVendorLeadCode, TransactionCallRequestByLeadId]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


