from .base import AuthenticationBase

class Enterprise(AuthenticationBase):
    def saml_metadata(self): ...
    def wsfed_metadata(self): ...
