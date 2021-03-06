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


class FacialHairProperties(Model):
    """Properties describing facial hair attributes.

    :param mustache:
    :type mustache: float
    :param beard:
    :type beard: float
    :param sideburns:
    :type sideburns: float
    """

    _validation = {
        'mustache': {'maximum': 1, 'minimum': 0},
        'beard': {'maximum': 1, 'minimum': 0},
        'sideburns': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'mustache': {'key': 'mustache', 'type': 'float'},
        'beard': {'key': 'beard', 'type': 'float'},
        'sideburns': {'key': 'sideburns', 'type': 'float'},
    }

    def __init__(self, mustache=None, beard=None, sideburns=None):
        self.mustache = mustache
        self.beard = beard
        self.sideburns = sideburns
