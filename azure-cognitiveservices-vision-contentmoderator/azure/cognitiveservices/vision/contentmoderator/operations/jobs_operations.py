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

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class JobsOperations(object):
    """JobsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_job_details(
            self, team_name, job_id, custom_headers=None, raw=False, **operation_config):
        """Get the Job Details for a Job Id.

        :param team_name: Your Team Name.
        :type team_name: str
        :param job_id: Id of the job.
        :type job_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Job or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Job or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/jobs/{JobId}'
        path_format_arguments = {
            'azureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'JobId': self._serialize.url("job_id", job_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Ocp-Apim-Subscription-Key'] = self._serialize.header("self.config.ocp_apim_subscription_key", self.config.ocp_apim_subscription_key, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Job', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_job_method(
            self, team_name, content_id, workflow_name, content_value, content_type="Image", call_back_endpoint=None, custom_headers=None, raw=False, **operation_config):
        """A job Id will be returned for the content posted on this endpoint.
        Once the content is evaluated against the Workflow provided the review
        will be created or ignored based on the workflow expression.
        <h3>CallBack Schemas </h3>
        <p>
        <h4>Job Completion CallBack Sample</h4><br/>
        {<br/>
        "JobId": "<Job Id>,<br/>
        "ReviewId": "<Review Id, if the Job resulted in a Review to be
        created>",<br/>
        "WorkFlowId": "default",<br/>
        "Status": "<This will be one of Complete, InProgress, Error>",<br/>
        "ContentType": "Image",<br/>
        "ContentId": "<This is the ContentId that was specified on
        input>",<br/>
        "CallBackType": "Job",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>
        <p>
        <h4>Review Completion CallBack Sample</h4><br/>
        {
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        },<br/>
        "ReviewerResultTags": {<br/>
        "a": "False",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>.

        :param team_name: Your team name.
        :type team_name: str
        :param content_type: Image, Text or Video. Possible values include:
         'Image', 'Text', 'Video'
        :type content_type: str
        :param content_id: Id/Name to identify the content submitted.
        :type content_id: str
        :param workflow_name: Workflow Name that you want to invoke.
        :type workflow_name: str
        :param content_value: Content to evaluate for a job.
        :type content_value: str
        :param call_back_endpoint: Callback endpoint for posting the create
         job result.
        :type call_back_endpoint: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CreateJob or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.CreateJob or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        content = models.Content(content_value=content_value)

        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/jobs'
        path_format_arguments = {
            'azureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['ContentType'] = self._serialize.query("content_type", content_type, 'str')
        query_parameters['ContentId'] = self._serialize.query("content_id", content_id, 'str')
        query_parameters['WorkflowName'] = self._serialize.query("workflow_name", workflow_name, 'str')
        if call_back_endpoint is not None:
            query_parameters['CallBackEndpoint'] = self._serialize.query("call_back_endpoint", call_back_endpoint, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Ocp-Apim-Subscription-Key'] = self._serialize.header("self.config.ocp_apim_subscription_key", self.config.ocp_apim_subscription_key, 'str')
        header_parameters['Content-Type'] = self._serialize.header("self.config.content_type1", self.config.content_type1, 'str')

        # Construct body
        body_content = self._serialize.body(content, 'Content')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CreateJob', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
