from .azure_configuration_client_imp import AzureConfigurationClientImp

class AzureConfigurationClient(object):
    """Do stuff with azconfig

    :ivar config: Configuration for client.
    :vartype config: AzureConfigurationClientConfiguration

    :param connection_string: Credentials needed for the client to connect to Azure.
    :type connection_string: str
    """

    def __init__(
            self, connection_string):

        self._client = AzureConfigurationClientImp(connection_string)
    
    def list_key_values(
            self, label=None, key=None, accept_date_time=None, fields=None, custom_headers=None, raw=False, **operation_config):
        """List key values.

        List the key values in the configuration store, optionally filtered by
        label.

        :param label: Filter returned values based on their label. '*' can be
         used as wildcard in the beginning or end of the filter
        :type label: list[str]
        :param key: Filter returned values based on their keys. '*' can be
         used as wildcard in the beginning or end of the filter
        :type key: list[str]
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param fields: Specify which fields to return
        :type fields: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of KeyValue
        :rtype:
         ~azure.configurationservice.models.KeyValuePaged[~azure.configurationservice.models.KeyValue]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_key_values(label, key, accept_date_time, fields, custom_headers, raw, **operation_config)
    
    def get_key_value(
            self, key, label="%00", accept_date_time=None, custom_headers=None, raw=False, **operation_config):
        
        """Get a KeyValue.

        Get the KeyValue for the given key and label.

        :param key: string
        :type key: str
        :param label: Label of key to retreive
        :type label: str
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyValue or ClientRawResponse if raw=true
        :rtype: ~azure.configurationservice.models.KeyValue or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.get_key_values(key, label, accept_date_time, custom_headers, raw, **operation_config)

    def create_key_value(
            self, key_value, key, label="%00", custom_headers=None, raw=False, **operation_config):
        """Create a KeyValue.

        Create a KeyValue.

        :param key_value:
        :type key_value: ~azure.configurationservice.models.KeyValue
        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyValue or ClientRawResponse if raw=true
        :rtype: ~azure.configurationservice.models.KeyValue or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.create_or_update_key_values(key_value, key, label, custom_headers, raw, **operation_config)
    
    def update_key_value(
            self, key_value, key, label="%00", custom_headers=None, raw=False, **operation_config):
        """Update a KeyValue.

        Update a KeyValue.

        :param key_value:
        :type key_value: ~azure.configurationservice.models.KeyValue
        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyValue or ClientRawResponse if raw=true
        :rtype: ~azure.configurationservice.models.KeyValue or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.create_or_update_key_values(key_value, key, label, custom_headers, raw, **operation_config)
    
    def delete_key_value(
            self, key, label=None, custom_headers=None, raw=False, **operation_config):
        """Delete a KeyValue.

        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyValue or ClientRawResponse if raw=true
        :rtype: ~azure.configurationservice.models.KeyValue or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.delete_key_values(key, label, custom_headers, raw, **operation_config)

    def list_keys(
            self, name=None, accept_date_time=None, custom_headers=None, raw=False, **operation_config):
        """

        :param name:
        :type name: str
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Key
        :rtype:
         ~azure.configurationservice.models.KeyPaged[~azure.configurationservice.models.Key]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_keys(name, accept_date_time, custom_headers, raw, **operation_config)
    
    def list_labels(
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
        return self._client.list_labels(accept_date_time, fields, name, custom_headers, raw, **operation_config)

    def lock(
            self, key, label=None, custom_headers=None, raw=False, **operation_config):
        """

        :param key:
        :type key: str
        :param label:
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyValue or ClientRawResponse if raw=true
        :rtype: ~azure.configurationservice.models.KeyValue or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.create_locks(key, label, custom_headers, raw, **operation_config)
    
    def unlock(
            self, key, label=None, custom_headers=None, raw=False, **operation_config):
        """

        :param key:
        :type key: str
        :param label:
        :type label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyValue or ClientRawResponse if raw=true
        :rtype: ~azure.configurationservice.models.KeyValue or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.delete_locks(key, label, custom_headers, raw, **operation_config)
    
    def list_revisions(
            self, label=None, key=None, fields=None, accept_date_time=None, custom_headers=None, raw=False, **operation_config):
        """

        :param label: Filter returned values based on their label. '*' can be
         used as wildcard in the beginning or end of the filter
        :type label: list[str]
        :param key: Filter returned values based on their keys. '*' can be
         used as wildcard in the beginning or end of the filter
        :type key: list[str]
        :param fields: Specify which fields to return
        :type fields: list[str]
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of KeyValue
        :rtype:
         ~azure.configurationservice.models.KeyValuePaged[~azure.configurationservice.models.KeyValue]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_revisions(label, key, fields, accept_date_time, custom_headers, raw, **operation_config)