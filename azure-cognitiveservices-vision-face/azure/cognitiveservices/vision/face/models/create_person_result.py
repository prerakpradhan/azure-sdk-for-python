# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreatePersonResult(Model):
    """Result of creating person.

    :param person_id: personID of the new created person.
    :type person_id: str
    """

    _validation = {
        'person_id': {'required': True},
    }

    _attribute_map = {
        'person_id': {'key': 'personId', 'type': 'str'},
    }

    def __init__(self, person_id):
        self.person_id = person_id
