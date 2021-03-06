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


class ReviewsOperations(object):
    """ReviewsOperations operations.

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

    def get_review(
            self, team_name, review_id, custom_headers=None, raw=False, **operation_config):
        """Returns review details for the review Id passed.

        :param team_name: Your Team Name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Review or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Review
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}'
        path_format_arguments = {
            'azureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
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
            deserialized = self._deserialize('Review', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_reviews(
            self, team_name, body, sub_team=None, custom_headers=None, raw=False, **operation_config):
        """The reviews created would show up for Reviewers on your team. As
        Reviewers complete reviewing, results of the Review would be POSTED
        (i.e. HTTP POST) on the specified CallBackEndpoint.
        <h3>CallBack Schemas </h3>
        <h4>Review Completion CallBack Sample</h4>
        <p>
        {<br/>
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
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
        :param body: Body for create reviews API
        :type body:
         list[~azure.cognitiveservices.vision.contentmoderator.models.BodyItem]
        :param sub_team: SubTeam of your team, you want to assign the created
         review to.
        :type sub_team: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ReviewListResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.ReviewListResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews'
        path_format_arguments = {
            'azureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sub_team is not None:
            query_parameters['subTeam'] = self._serialize.query("sub_team", sub_team, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("self.config.content_type", self.config.content_type, 'str')
        header_parameters['Ocp-Apim-Subscription-Key'] = self._serialize.header("self.config.ocp_apim_subscription_key", self.config.ocp_apim_subscription_key, 'str')

        # Construct body
        body_content = self._serialize.body(body, '[BodyItem]')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ReviewListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
