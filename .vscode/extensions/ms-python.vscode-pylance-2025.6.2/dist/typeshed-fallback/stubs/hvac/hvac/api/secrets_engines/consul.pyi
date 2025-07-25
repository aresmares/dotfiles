from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Consul(VaultApiBase):
    def configure_access(self, address, token, scheme=None, mount_point="consul"): ...
    def create_or_update_role(
        self, name, policy=None, policies=None, token_type=None, local=None, ttl=None, max_ttl=None, mount_point="consul"
    ): ...
    def read_role(self, name, mount_point="consul"): ...
    def list_roles(self, mount_point="consul"): ...
    def delete_role(self, name, mount_point="consul"): ...
    def generate_credentials(self, name, mount_point="consul"): ...
