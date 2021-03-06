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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class LabelsOperations(object):
    """LabelsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def list(
            self, accept_date_time=None, fields=None, name=None, custom_headers=None, raw=False, **operation_config):
        """List labels.

        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param fields: Specify which fields to return
        :type fields: list[str]
        :param name:
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Label
        :rtype:
         ~azure.configurationservice.models.LabelPaged[~azure.configurationservice.models.Label]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if fields is not None:
                    query_parameters['fields'] = self._serialize.query("fields", fields, '[str]', div=',')
                if name is not None:
                    query_parameters['name'] = self._serialize.query("name", name, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if accept_date_time is not None:
                header_parameters['Accept-DateTime'] = self._serialize.header("accept_date_time", accept_date_time, 'iso-8601')
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.LabelPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LabelPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/labels'}
