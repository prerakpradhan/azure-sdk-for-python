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

from .property_batch_operation import PropertyBatchOperation


class GetPropertyBatchOperation(PropertyBatchOperation):
    """Represents a PropertyBatchOperation that gets the specified property if it
    exists.  Note that if one PropertyBatchOperation in a PropertyBatch fails,
    the entire batch fails and cannot be committed in a transactional manner.
    .

    :param property_name:
    :type property_name: str
    :param kind: Polymorphic Discriminator
    :type kind: str
    :param include_value: Whether or not to return the property value with the
     metadata.  True if values should be returned with the metadata; False to
     return only property metadata.
     . Default value: False .
    :type include_value: bool
    """

    _validation = {
        'property_name': {'required': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'property_name': {'key': 'PropertyName', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'include_value': {'key': 'IncludeValue', 'type': 'bool'},
    }

    def __init__(self, property_name, include_value=False):
        super(GetPropertyBatchOperation, self).__init__(property_name=property_name)
        self.include_value = include_value
        self.kind = 'Get'
