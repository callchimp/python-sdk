# coding: utf-8

"""
    Callchimp Public API

    ## Introduction👋 Introducing OpenAPI spec for doing almost anything in [callchimp.ai](https://callchimp.ai). CallChimp is a Gen AI Call Center Enhancing telecommunication with GPT-driven bulk calling. It is scalable, user-friendly, and customizable. Optimized for seamless integration and usability. ## API Categories📋 The APIs are divided in 9 categories listed below:   - Campaigns   - Supervisors   - Lists   - Subscribers   - Calls   - Phone Numbers   - Webhooks   - Scripts   - Voices  ## API Operations✅ ### Campaign Operations    - List Campaigns   - Create a Campaign   - Get Campaign by Id   - Delete Campaign by Id   - Update Campaign by Id   - Add Supervisors to Campaign by Id   - Remove Supervisors from Campaign by Id   - Upload audio file to Campaign by Id   - Search Campaign by Name or Id  ### Supervisor Operations    - List Supervisors   - Create a Supervisor   - Get Supervisor by Id   - Delete Supervisor by Id   - Update Supervisor by Id   - Send OTP to Supervisor by Id   - Verify Supervisor OTP by Id  ### List Operations    - List Lists   - Create a List   - Get List by Id   - Delete List by Id   - Update List by Id   - Search List by Name or Id   - Create Campaign with Default List  ### Subscriber Operations    - List Subscribers   - Create one or more Subscriber(s)   - Get Subscriber by Id   - Delete Subscriber by Id   - Update Subscriber by Id   - Get Subscriber by Vendor Lead Code   - Delete Subscriber by Vendor Lead Code   - Update Subscriber by Vendor Lead Code  ### Call Operations    - List Calls   - Create a Call   - Get Call by Id   - List Supervisor Inbound Calls   - Generate Call Reports  ### Phone Number Operations    - List Phone Numbers  ### Webhook Operations    - List Webhooks   - Create a Webhook   - Get Webhook by Id   - Delete Webhook by Id   - Update Webhook by Id  ### Script Operations    - List Scripts   - Create a Script   - Get Script by Id   - Delete Script by Id   - Update Script by Id  ### Voice Operations   - List Available Voices  ## Authentication🔐 Callchimp public API offers authentication with API Keys. All endpoints accepts a header named `x-api-key`. To get started follow the below steps:    1. Login to callchimp dashboard.   2. Click on your profile on the top-right corner.   3. Click on Settings.   4. On the settings page, click on `API Keys` tab.   5. Click on `Create` button, add a name and an expiry date and click on `Add`.   6. An API Key will be generated, please save the key somewhere safe as it won't be shown again!   7. You can use the API Key directly here in this playground to test out the APIs. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class InboundCallResponseCallchimpNumber(BaseModel):
    """
    InboundCallResponseCallchimpNumber
    """ # noqa: E501
    id: Optional[StrictInt] = None
    number: Optional[StrictStr] = Field(default=None, description="Outbound caller id in E.164 format, e.g. `[+][country_code][number]`.")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "number", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['JIO', 'TWILIO']):
            raise ValueError("must be one of enum values ('JIO', 'TWILIO')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InboundCallResponseCallchimpNumber from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InboundCallResponseCallchimpNumber from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "number": obj.get("number"),
            "type": obj.get("type")
        })
        return _obj


