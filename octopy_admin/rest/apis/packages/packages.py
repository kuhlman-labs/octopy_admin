"""
Manage packages for authenticated users and organizations.
"""


class Packages:
    """
    Manage packages for authenticated users and organizations.
    """

    def __init__(self, client):
        self._base_url = client._base_url
        self._execute = client._execute

    def list_packages_for_an_organization(self, org, **payload):
        """
        List packages for an organization
        https://docs.github.com/rest/reference/packages#list-packages-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        package_type
         package-visibility
        """
        url = self._base_url + f"/orgs/{org}/packages"
        response = self._execute("get", url, payload)
        return response

    def get_a_package_for_an_organization(self, package_type, package_name, org, **payload):
        """
        Get a package for an organization
        https://docs.github.com/rest/reference/packages#get-a-package-for-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}"
        response = self._execute("get", url, payload)
        return response

    def delete_a_package_for_an_organization(self, package_type, package_name, org, **payload):
        """
        Delete a package for an organization
        https://docs.github.com/rest/reference/packages#delete-a-package-for-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}"
        response = self._execute("delete", url, payload)
        return response

    def restore_a_package_for_an_organization(self, package_type, package_name, org, **payload):
        """
        Restore a package for an organization
        https://docs.github.com/rest/reference/packages#restore-a-package-for-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        Payload Parameters:
        token
        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}/restore"
        response = self._execute("post", url, payload)
        return response

    def get_all_package_versions_for_a_package_owned_by_an_organization(
        self, package_type, package_name, org, **payload
    ):
        """
        Get all package versions for a package owned by an organization
        https://docs.github.com/rest/reference/packages#get-all-package-versions-for-a-package-owned-by-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        Payload Parameters:
        page
         per-page
         state
        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}/versions"
        response = self._execute("get", url, payload)
        return response

    def get_a_package_version_for_an_organization(
        self, package_type, package_name, org, package_version_id, **payload
    ):
        """
        Get a package version for an organization
        https://docs.github.com/rest/reference/packages#get-a-package-version-for-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("get", url, payload)
        return response

    def delete_package_version_for_an_organization(
        self, package_type, package_name, org, package_version_id, **payload
    ):
        """
        Delete package version for an organization
        https://docs.github.com/rest/reference/packages#delete-a-package-version-for-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("delete", url, payload)
        return response

    def restore_package_version_for_an_organization(
        self, package_type, package_name, org, package_version_id, **payload
    ):
        """
        Restore package version for an organization
        https://docs.github.com/rest/reference/packages#restore-a-package-version-for-an-organization
        Attributes:
        Path Parameters:
        package_type
        package_name
        org
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        )
        response = self._execute("post", url, payload)
        return response

    def list_packages_for_the_authenticated_users_namespace(self, **payload):
        """
        List packages for the authenticated user's namespace
        https://docs.github.com/rest/reference/packages#list-packages-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        package_type
         package-visibility
        """
        url = self._base_url + f"/user/packages"
        response = self._execute("get", url, payload)
        return response

    def get_a_package_for_the_authenticated_user(self, package_type, package_name, **payload):
        """
        Get a package for the authenticated user
        https://docs.github.com/rest/reference/packages#get-a-package-for-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}"
        response = self._execute("get", url, payload)
        return response

    def delete_a_package_for_the_authenticated_user(self, package_type, package_name, **payload):
        """
        Delete a package for the authenticated user
        https://docs.github.com/rest/reference/packages#delete-a-package-for-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}"
        response = self._execute("delete", url, payload)
        return response

    def restore_a_package_for_the_authenticated_user(self, package_type, package_name, **payload):
        """
        Restore a package for the authenticated user
        https://docs.github.com/rest/reference/packages#restore-a-package-for-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        Payload Parameters:
        token
        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}/restore"
        response = self._execute("post", url, payload)
        return response

    def get_all_package_versions_for_a_package_owned_by_the_authenticated_user(
        self, package_type, package_name, **payload
    ):
        """
        Get all package versions for a package owned by the authenticated user
        https://docs.github.com/rest/reference/packages#get-all-package-versions-for-a-package-owned-by-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        Payload Parameters:
        page
         per-page
         state
        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}/versions"
        response = self._execute("get", url, payload)
        return response

    def get_a_package_version_for_the_authenticated_user(
        self, package_type, package_name, package_version_id, **payload
    ):
        """
        Get a package version for the authenticated user
        https://docs.github.com/rest/reference/packages#get-a-package-version-for-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("get", url, payload)
        return response

    def delete_a_package_version_for_the_authenticated_user(
        self, package_type, package_name, package_version_id, **payload
    ):
        """
        Delete a package version for the authenticated user
        https://docs.github.com/rest/reference/packages#delete-a-package-version-for-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("delete", url, payload)
        return response

    def restore_a_package_version_for_the_authenticated_user(
        self, package_type, package_name, package_version_id, **payload
    ):
        """
        Restore a package version for the authenticated user
        https://docs.github.com/rest/reference/packages#restore-a-package-version-for-the-authenticated-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        )
        response = self._execute("post", url, payload)
        return response

    def list_packages_for_a_user(self, username, **payload):
        """
        List packages for a user
        https://docs.github.com/rest/reference/packages#list-packages-for-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        package_type
         package-visibility
        """
        url = self._base_url + f"/users/{username}/packages"
        response = self._execute("get", url, payload)
        return response

    def get_a_package_for_a_user(self, package_type, package_name, username, **payload):
        """
        Get a package for a user
        https://docs.github.com/rest/reference/packages#get-a-package-for-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}"
        response = self._execute("get", url, payload)
        return response

    def delete_a_package_for_a_user(self, package_type, package_name, username, **payload):
        """
        Delete a package for a user
        https://docs.github.com/rest/reference/packages#delete-a-package-for-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}"
        response = self._execute("delete", url, payload)
        return response

    def restore_a_package_for_a_user(self, package_type, package_name, username, **payload):
        """
        Restore a package for a user
        https://docs.github.com/rest/reference/packages#restore-a-package-for-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        username
        Payload Parameters:
        token
        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}/restore"
        response = self._execute("post", url, payload)
        return response

    def get_all_package_versions_for_a_package_owned_by_a_user(
        self, package_type, package_name, username, **payload
    ):
        """
        Get all package versions for a package owned by a user
        https://docs.github.com/rest/reference/packages#get-all-package-versions-for-a-package-owned-by-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}/versions"
        response = self._execute("get", url, payload)
        return response

    def get_a_package_version_for_a_user(
        self, package_type, package_name, package_version_id, username, **payload
    ):
        """
        Get a package version for a user
        https://docs.github.com/rest/reference/packages#get-a-package-version-for-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        package_version_id
        username
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("get", url, payload)
        return response

    def delete_package_version_for_a_user(
        self, package_type, package_name, username, package_version_id, **payload
    ):
        """
        Delete package version for a user
        https://docs.github.com/rest/reference/packages#delete-a-package-version-for-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        username
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("delete", url, payload)
        return response

    def restore_package_version_for_a_user(
        self, package_type, package_name, username, package_version_id, **payload
    ):
        """
        Restore package version for a user
        https://docs.github.com/rest/reference/packages#restore-a-package-version-for-a-user
        Attributes:
        Path Parameters:
        package_type
        package_name
        username
        package_version_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        )
        response = self._execute("post", url, payload)
        return response
