from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Gcp(VaultApiBase):
    def configure(self, credentials=None, ttl=None, max_ttl=None, mount_point="gcp"): ...
    def rotate_root_credentials(self, mount_point="gcp"): ...
    def read_config(self, mount_point="gcp"): ...
    def create_or_update_roleset(self, name, project, bindings, secret_type=None, token_scopes=None, mount_point="gcp"): ...
    def rotate_roleset_account(self, name, mount_point="gcp"): ...
    def rotate_roleset_account_key(self, name, mount_point="gcp"): ...
    def read_roleset(self, name, mount_point="gcp"): ...
    def list_rolesets(self, mount_point="gcp"): ...
    def delete_roleset(self, name, mount_point="gcp"): ...
    def generate_oauth2_access_token(self, roleset, mount_point="gcp"): ...
    def generate_service_account_key(
        self,
        roleset,
        key_algorithm: str = "KEY_ALG_RSA_2048",
        key_type: str = "TYPE_GOOGLE_CREDENTIALS_FILE",
        method: str = "POST",
        mount_point="gcp",
    ): ...
    def create_or_update_static_account(
        self, name, service_account_email, bindings=None, secret_type=None, token_scopes=None, mount_point="gcp"
    ): ...
    def rotate_static_account_key(self, name, mount_point="gcp"): ...
    def read_static_account(self, name, mount_point="gcp"): ...
    def list_static_accounts(self, mount_point="gcp"): ...
    def delete_static_account(self, name, mount_point="gcp"): ...
    def generate_static_account_oauth2_access_token(self, name, mount_point="gcp"): ...
    def generate_static_account_service_account_key(
        self,
        name,
        key_algorithm: str = "KEY_ALG_RSA_2048",
        key_type: str = "TYPE_GOOGLE_CREDENTIALS_FILE",
        method: str = "POST",
        mount_point="gcp",
    ): ...
    def create_or_update_impersonated_account(
        self, name, service_account_email, token_scopes=None, ttl=None, mount_point="gcp"
    ): ...
    def read_impersonated_account(self, name, mount_point="gcp"): ...
    def list_impersonated_accounts(self, mount_point="gcp"): ...
    def delete_impersonated_account(self, name, mount_point="gcp"): ...
    def generate_impersonated_account_oauth2_access_token(self, name, mount_point="gcp"): ...
