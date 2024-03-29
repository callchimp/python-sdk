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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from callchimp.models.inbound_call_response_callchimp_number import InboundCallResponseCallchimpNumber
from callchimp.models.inbound_call_response_hangup_cause import InboundCallResponseHangupCause
from callchimp.models.inbound_call_response_supervisor import InboundCallResponseSupervisor
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InboundCallResponse(BaseModel):
    """
    InboundCallResponse
    """ # noqa: E501
    callchimp_number: Optional[InboundCallResponseCallchimpNumber] = None
    created_at: Optional[datetime] = None
    dial_status: Optional[StrictStr] = None
    duration: Optional[StrictInt] = Field(default=None, description="Call duration in seconds")
    hangup_cause: Optional[InboundCallResponseHangupCause] = None
    id: Optional[StrictInt] = None
    inbound_caller: Optional[StrictStr] = None
    is_answered: Optional[StrictBool] = None
    organization: Optional[StrictInt] = None
    supervisor: Optional[InboundCallResponseSupervisor] = None
    supervisor_number: Optional[InboundCallResponseHangupCause] = None
    __properties: ClassVar[List[str]] = ["callchimp_number", "created_at", "dial_status", "duration", "hangup_cause", "id", "inbound_caller", "is_answered", "organization", "supervisor", "supervisor_number"]

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
        """Create an instance of InboundCallResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of callchimp_number
        if self.callchimp_number:
            _dict['callchimp_number'] = self.callchimp_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hangup_cause
        if self.hangup_cause:
            _dict['hangup_cause'] = self.hangup_cause.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supervisor
        if self.supervisor:
            _dict['supervisor'] = self.supervisor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supervisor_number
        if self.supervisor_number:
            _dict['supervisor_number'] = self.supervisor_number.to_dict()
        # set to None if dial_status (nullable) is None
        # and model_fields_set contains the field
        if self.dial_status is None and "dial_status" in self.model_fields_set:
            _dict['dial_status'] = None

        # set to None if supervisor (nullable) is None
        # and model_fields_set contains the field
        if self.supervisor is None and "supervisor" in self.model_fields_set:
            _dict['supervisor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InboundCallResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "callchimp_number": InboundCallResponseCallchimpNumber.from_dict(obj.get("callchimp_number")) if obj.get("callchimp_number") is not None else None,
            "created_at": obj.get("created_at"),
            "dial_status": obj.get("dial_status"),
            "duration": obj.get("duration"),
            "hangup_cause": InboundCallResponseHangupCause.from_dict(obj.get("hangup_cause")) if obj.get("hangup_cause") is not None else None,
            "id": obj.get("id"),
            "inbound_caller": obj.get("inbound_caller"),
            "is_answered": obj.get("is_answered"),
            "organization": obj.get("organization"),
            "supervisor": InboundCallResponseSupervisor.from_dict(obj.get("supervisor")) if obj.get("supervisor") is not None else None,
            "supervisor_number": InboundCallResponseHangupCause.from_dict(obj.get("supervisor_number")) if obj.get("supervisor_number") is not None else None
        })
        return _obj


