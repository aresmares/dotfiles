from typing import Final

ASSERTION_TYPE: Final[str]

class JWTBearerClientAssertion:
    CLIENT_ASSERTION_TYPE: Final[str]
    CLIENT_AUTH_METHOD: Final[str]
    token_url: str
    leeway: int
    def __init__(self, token_url: str, validate_jti: bool = True, leeway: int = 60) -> None: ...
    def __call__(self, query_client, request): ...
    def create_claims_options(self): ...
    def process_assertion_claims(self, assertion, resolve_key): ...
    def authenticate_client(self, client): ...
    def create_resolve_key_func(self, query_client, request): ...
    def validate_jti(self, claims, jti) -> None: ...
    def resolve_client_public_key(self, client, headers) -> None: ...
