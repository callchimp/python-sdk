# coding: utf-8

"""
    Callchimp Public API

    ## Introduction👋 Introducing OpenAPI spec for doing almost anything in [callchimp.ai](https://callchimp.ai). CallChimp is a Gen AI Call Center Enhancing telecommunication with GPT-driven bulk calling. It is scalable, user-friendly, and customizable. Optimized for seamless integration and usability. ## API Categories📋 The APIs are divided in 7 categories listed below:   - Campaigns   - Supervisors   - Lists   - Subscribers   - Calls   - Phone Numbers   - Webhooks  ## API Operations✅ ### Campaign Operations    - List all Campaigns   - Create a Campaign   - Get Campaign by Id   - Delete Campaign by Id   - Update Campaign by Id   - Add Supervisors to Campaign by Id   - Remove Supervisors from Campaign by Id   - Upload audio file to Campaign by Id  ### Supervisor Operations    - List all Supervisors   - Create a Supervisor   - Get Supervisor by Id   - Delete Supervisor by Id   - Update Supervisor by Id   - Send OTP to Campaign by Id   - Verify Supervisor OTP by Id  ### List Operations    - List all Lists   - Create a List   - Get List by Id   - Delete List by Id   - Update List by Id  ### Subscriber Operations    - List all Subscribers   - Create one or more Subscriber(s)   - Get Subscriber by Id   - Delete Subscriber by Id   - Update Subscriber by Id  ### Call Operations    - List outbound Calls   - Create a Call   - Get Call by Id   - List Inbound Calls   - Generate Call Reports  ### Phone Number Operations    - List Phone Numbers  ### Webhook Operations    - List all Webhooks   - Create a Webhook   - Get Webhook by Id   - Delete Webhook by Id   - Update Webhook by Id  ## Authentication🔐 CallChimp public API offers authentication with API Keys. All endpoints accepts a header named `x-api-key`. To get started follow the below steps:    1. Login to callchimp dashboard.   2. Click on your profile on the top-right corner.   3. Click on Settings.   4. On the settings page, click on `API Keys` from the left sidebar.   5. Click on `Add new` button, add an expiry date and click on `Add`.   6. An API Key will be generated, please save the key somewhere safe as it won't be shown again!   7. You can use the API Key directly here in this playground to test out the APIs. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SubscriberResponse(BaseModel):
    """
    SubscriberResponse
    """ # noqa: E501
    id: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    user: Optional[StrictInt] = None
    vendor_lead_code: Optional[StrictStr] = None
    source_id: Optional[StrictStr] = None
    gmt_offset_now: Optional[StrictInt] = Field(default=None, description="Integer milisecond offset for call place")
    called_since_last_reset: Optional[StrictStr] = None
    phone_code: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    middle_initial: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    address3: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    province: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = None
    gender: Optional[StrictStr] = None
    date_of_birth: Optional[StrictStr] = None
    alt_phone: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    comments: Optional[StrictStr] = None
    called_count: Optional[StrictInt] = None
    last_local_call_time: Optional[StrictInt] = None
    rank: Optional[StrictStr] = None
    custom_data: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    origin_type: Optional[StrictStr] = None
    leadlist: Optional[StrictInt] = Field(default=None, description="Leadlist foreign key")
    upload: Optional[StrictInt] = Field(default=None, description="Upload foreign key")
    organization: Optional[StrictInt] = Field(default=None, description="Organization foreign key")
    __properties: ClassVar[List[str]] = ["id", "status", "user", "vendor_lead_code", "source_id", "gmt_offset_now", "called_since_last_reset", "phone_code", "phone_number", "title", "first_name", "middle_initial", "last_name", "address1", "address2", "address3", "city", "state", "province", "postal_code", "country_code", "gender", "date_of_birth", "alt_phone", "email", "comments", "called_count", "last_local_call_time", "rank", "custom_data", "owner", "origin_type", "leadlist", "upload", "organization"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SubscriberResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SubscriberResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "user": obj.get("user"),
            "vendor_lead_code": obj.get("vendor_lead_code"),
            "source_id": obj.get("source_id"),
            "gmt_offset_now": obj.get("gmt_offset_now"),
            "called_since_last_reset": obj.get("called_since_last_reset"),
            "phone_code": obj.get("phone_code"),
            "phone_number": obj.get("phone_number"),
            "title": obj.get("title"),
            "first_name": obj.get("first_name"),
            "middle_initial": obj.get("middle_initial"),
            "last_name": obj.get("last_name"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "address3": obj.get("address3"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "province": obj.get("province"),
            "postal_code": obj.get("postal_code"),
            "country_code": obj.get("country_code"),
            "gender": obj.get("gender"),
            "date_of_birth": obj.get("date_of_birth"),
            "alt_phone": obj.get("alt_phone"),
            "email": obj.get("email"),
            "comments": obj.get("comments"),
            "called_count": obj.get("called_count"),
            "last_local_call_time": obj.get("last_local_call_time"),
            "rank": obj.get("rank"),
            "custom_data": obj.get("custom_data"),
            "owner": obj.get("owner"),
            "origin_type": obj.get("origin_type"),
            "leadlist": obj.get("leadlist"),
            "upload": obj.get("upload"),
            "organization": obj.get("organization")
        })
        return _obj


