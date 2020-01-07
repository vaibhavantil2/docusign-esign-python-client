# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EnvelopeDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attachment_tab_id=None, authoritative_copy=None, available_document_types=None, contains_pdf_form_fields=None, display=None, document_fields=None, document_group=None, document_id=None, error_details=None, include_in_download=None, name=None, order=None, pages=None, signer_must_acknowledge=None, size_bytes=None, type=None, uri=None):
        """
        EnvelopeDocument - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attachment_tab_id': 'str',
            'authoritative_copy': 'str',
            'available_document_types': 'list[SignatureType]',
            'contains_pdf_form_fields': 'str',
            'display': 'str',
            'document_fields': 'list[NameValue]',
            'document_group': 'str',
            'document_id': 'str',
            'error_details': 'ErrorDetails',
            'include_in_download': 'str',
            'name': 'str',
            'order': 'str',
            'pages': 'str',
            'signer_must_acknowledge': 'str',
            'size_bytes': 'str',
            'type': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'attachment_tab_id': 'attachmentTabId',
            'authoritative_copy': 'authoritativeCopy',
            'available_document_types': 'availableDocumentTypes',
            'contains_pdf_form_fields': 'containsPdfFormFields',
            'display': 'display',
            'document_fields': 'documentFields',
            'document_group': 'documentGroup',
            'document_id': 'documentId',
            'error_details': 'errorDetails',
            'include_in_download': 'includeInDownload',
            'name': 'name',
            'order': 'order',
            'pages': 'pages',
            'signer_must_acknowledge': 'signerMustAcknowledge',
            'size_bytes': 'sizeBytes',
            'type': 'type',
            'uri': 'uri'
        }

        self._attachment_tab_id = attachment_tab_id
        self._authoritative_copy = authoritative_copy
        self._available_document_types = available_document_types
        self._contains_pdf_form_fields = contains_pdf_form_fields
        self._display = display
        self._document_fields = document_fields
        self._document_group = document_group
        self._document_id = document_id
        self._error_details = error_details
        self._include_in_download = include_in_download
        self._name = name
        self._order = order
        self._pages = pages
        self._signer_must_acknowledge = signer_must_acknowledge
        self._size_bytes = size_bytes
        self._type = type
        self._uri = uri

    @property
    def attachment_tab_id(self):
        """
        Gets the attachment_tab_id of this EnvelopeDocument.
        

        :return: The attachment_tab_id of this EnvelopeDocument.
        :rtype: str
        """
        return self._attachment_tab_id

    @attachment_tab_id.setter
    def attachment_tab_id(self, attachment_tab_id):
        """
        Sets the attachment_tab_id of this EnvelopeDocument.
        

        :param attachment_tab_id: The attachment_tab_id of this EnvelopeDocument.
        :type: str
        """

        self._attachment_tab_id = attachment_tab_id

    @property
    def authoritative_copy(self):
        """
        Gets the authoritative_copy of this EnvelopeDocument.
        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.

        :return: The authoritative_copy of this EnvelopeDocument.
        :rtype: str
        """
        return self._authoritative_copy

    @authoritative_copy.setter
    def authoritative_copy(self, authoritative_copy):
        """
        Sets the authoritative_copy of this EnvelopeDocument.
        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.

        :param authoritative_copy: The authoritative_copy of this EnvelopeDocument.
        :type: str
        """

        self._authoritative_copy = authoritative_copy

    @property
    def available_document_types(self):
        """
        Gets the available_document_types of this EnvelopeDocument.
        

        :return: The available_document_types of this EnvelopeDocument.
        :rtype: list[SignatureType]
        """
        return self._available_document_types

    @available_document_types.setter
    def available_document_types(self, available_document_types):
        """
        Sets the available_document_types of this EnvelopeDocument.
        

        :param available_document_types: The available_document_types of this EnvelopeDocument.
        :type: list[SignatureType]
        """

        self._available_document_types = available_document_types

    @property
    def contains_pdf_form_fields(self):
        """
        Gets the contains_pdf_form_fields of this EnvelopeDocument.
        

        :return: The contains_pdf_form_fields of this EnvelopeDocument.
        :rtype: str
        """
        return self._contains_pdf_form_fields

    @contains_pdf_form_fields.setter
    def contains_pdf_form_fields(self, contains_pdf_form_fields):
        """
        Sets the contains_pdf_form_fields of this EnvelopeDocument.
        

        :param contains_pdf_form_fields: The contains_pdf_form_fields of this EnvelopeDocument.
        :type: str
        """

        self._contains_pdf_form_fields = contains_pdf_form_fields

    @property
    def display(self):
        """
        Gets the display of this EnvelopeDocument.
        

        :return: The display of this EnvelopeDocument.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this EnvelopeDocument.
        

        :param display: The display of this EnvelopeDocument.
        :type: str
        """

        self._display = display

    @property
    def document_fields(self):
        """
        Gets the document_fields of this EnvelopeDocument.
        

        :return: The document_fields of this EnvelopeDocument.
        :rtype: list[NameValue]
        """
        return self._document_fields

    @document_fields.setter
    def document_fields(self, document_fields):
        """
        Sets the document_fields of this EnvelopeDocument.
        

        :param document_fields: The document_fields of this EnvelopeDocument.
        :type: list[NameValue]
        """

        self._document_fields = document_fields

    @property
    def document_group(self):
        """
        Gets the document_group of this EnvelopeDocument.
        

        :return: The document_group of this EnvelopeDocument.
        :rtype: str
        """
        return self._document_group

    @document_group.setter
    def document_group(self, document_group):
        """
        Sets the document_group of this EnvelopeDocument.
        

        :param document_group: The document_group of this EnvelopeDocument.
        :type: str
        """

        self._document_group = document_group

    @property
    def document_id(self):
        """
        Gets the document_id of this EnvelopeDocument.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :return: The document_id of this EnvelopeDocument.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this EnvelopeDocument.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :param document_id: The document_id of this EnvelopeDocument.
        :type: str
        """

        self._document_id = document_id

    @property
    def error_details(self):
        """
        Gets the error_details of this EnvelopeDocument.

        :return: The error_details of this EnvelopeDocument.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this EnvelopeDocument.

        :param error_details: The error_details of this EnvelopeDocument.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def include_in_download(self):
        """
        Gets the include_in_download of this EnvelopeDocument.
        

        :return: The include_in_download of this EnvelopeDocument.
        :rtype: str
        """
        return self._include_in_download

    @include_in_download.setter
    def include_in_download(self, include_in_download):
        """
        Sets the include_in_download of this EnvelopeDocument.
        

        :param include_in_download: The include_in_download of this EnvelopeDocument.
        :type: str
        """

        self._include_in_download = include_in_download

    @property
    def name(self):
        """
        Gets the name of this EnvelopeDocument.
        

        :return: The name of this EnvelopeDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EnvelopeDocument.
        

        :param name: The name of this EnvelopeDocument.
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """
        Gets the order of this EnvelopeDocument.
        

        :return: The order of this EnvelopeDocument.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this EnvelopeDocument.
        

        :param order: The order of this EnvelopeDocument.
        :type: str
        """

        self._order = order

    @property
    def pages(self):
        """
        Gets the pages of this EnvelopeDocument.
        

        :return: The pages of this EnvelopeDocument.
        :rtype: str
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this EnvelopeDocument.
        

        :param pages: The pages of this EnvelopeDocument.
        :type: str
        """

        self._pages = pages

    @property
    def signer_must_acknowledge(self):
        """
        Gets the signer_must_acknowledge of this EnvelopeDocument.
        

        :return: The signer_must_acknowledge of this EnvelopeDocument.
        :rtype: str
        """
        return self._signer_must_acknowledge

    @signer_must_acknowledge.setter
    def signer_must_acknowledge(self, signer_must_acknowledge):
        """
        Sets the signer_must_acknowledge of this EnvelopeDocument.
        

        :param signer_must_acknowledge: The signer_must_acknowledge of this EnvelopeDocument.
        :type: str
        """

        self._signer_must_acknowledge = signer_must_acknowledge

    @property
    def size_bytes(self):
        """
        Gets the size_bytes of this EnvelopeDocument.
        

        :return: The size_bytes of this EnvelopeDocument.
        :rtype: str
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """
        Sets the size_bytes of this EnvelopeDocument.
        

        :param size_bytes: The size_bytes of this EnvelopeDocument.
        :type: str
        """

        self._size_bytes = size_bytes

    @property
    def type(self):
        """
        Gets the type of this EnvelopeDocument.
        

        :return: The type of this EnvelopeDocument.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EnvelopeDocument.
        

        :param type: The type of this EnvelopeDocument.
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """
        Gets the uri of this EnvelopeDocument.
        

        :return: The uri of this EnvelopeDocument.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this EnvelopeDocument.
        

        :param uri: The uri of this EnvelopeDocument.
        :type: str
        """

        self._uri = uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
