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


class KeyValue(Model):
    """A configuration value.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar etag: Entity tag (etag) of the object
    :vartype etag: str
    :param key:
    :type key: str
    :param label:
    :type label: str
    :param content_type:
    :type content_type: str
    :param value:
    :type value: str
    :ivar last_modified:
    :vartype last_modified: datetime
    :ivar locked:
    :vartype locked: bool
    :param tags:
    :type tags: dict[str, str]
    """

    _validation = {
        'etag': {'readonly': True},
        'last_modified': {'readonly': True},
        'locked': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'last_modified': {'key': 'last_modified', 'type': 'iso-8601'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, key, label=None, content_type=None, value=None, tags=None):
        super(KeyValue, self).__init__()
        self.etag = None
        self.key = key
        self.label = label
        self.content_type = content_type
        self.value = value
        self.last_modified = None
        self.locked = None
        self.tags = tags
