# -*- coding: utf-8 -*-

class ErrorCode(object):
    SYSTEM_ERROR = 1001

    MISSING_PARAMETER = 2001
    INVALID_PARAMETER = 2002
    ACCOUNT_NOT_FOUND = 3001
    ACCOUNT_NOT_VALID = 3002
    TYPE_ERROR = 3003
    API_EXCEPTION = 2003
    NOT_AUTHENTICATED = 2005
    PERMISSION_DENIED = 2006
    AUTHENTICATION_FAILED = 2008
    NOT_FOUND = 2012
    CONFIG_ERROR = 2020

    VALIDATOR_ERROR = 3000

    CONTENT_TYPE_DENIED = 4001

    UNSUPPORTED_MEDIATYPE = 3308

    API_SECRET_NOT_VALID = 7001
    API_KEY_NOT_FOUND = 7002
    API_KEY_NOT_VALID = 7003


class BlogException(Exception):

    def __init__(self, code=ErrorCode.SYSTEM_ERROR, event=None, message=''):
        self.code = code
        self.event = event
        self.message = message
        super(BlogException, self).__init__(str(self))

    def __str__(self):
        return '[ClothoException] code: {}, message: {}'.format(self.code, self.message)

    def __unicode__(self):
        return u'[ClothoException] code: {}, message: {}'.format(self.code, self.message)


class PermissionDeniedException(BlogException):
    def __init__(self, code=ErrorCode.PERMISSION_DENIED, event=None, message='PermissionDenied'):
        super(PermissionDeniedException, self).__init__(code=code, event=event, message=message)


class BlogAPIException(BlogException):
    pass


class NotFoundException(BlogException):

    def __init__(self, code=ErrorCode.NOT_FOUND, event=None, message='not found'):
        super(NotFoundException, self).__init__(code=code, event=event, message=message)


class ParamException(BlogAPIException):

    def __init__(self, code=ErrorCode.INVALID_PARAMETER, event=None, message='invalid_parameter'):
        super(ParamException, self).__init__(code=code, event=event, message=message)


class ConfigException(BlogAPIException):

    def __init__(self, code=ErrorCode.CONFIG_ERROR, event=None, message='config_error'):
        super(ConfigException, self).__init__(code=code, event=event, message=message)
