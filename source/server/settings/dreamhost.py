from .base import *

ALLOWED_HOSTS = ['*']

OAUTH2_PROVIDER = {
    'RESOURCE_SERVER_INTROSPECTION_URL': 'https://auth.fe.fernandoe.com/api/v1/introspect/',
    'RESOURCE_SERVER_AUTH_TOKEN': 'fe-endereco-server',
    'OAUTH2_VALIDATOR_CLASS': 'fe_core.services.auth.oauth2_validators.FEOAuth2Validator'
}

STATIC_ROOT = '/home/fems/endereco.fe.fernandoe.com/public/static'
