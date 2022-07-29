"""
Endpoints that give information about the API.
"""


class Meta:
    """
    Endpoints that give information about the API.
    """

    def __init__(self, client):
        self._base_url = client._base_url
        self._execute = client._execute

    def github_api_root(self, **payload):
        """
        GitHub API Root
        https://docs.github.com/rest/overview/resources-in-the-rest-api#root-endpoint
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + f"/"
        response = self._execute("get", url, payload)
        return response

    def get_github_meta_information(self, **payload):
        """
        Get GitHub meta information
        https://docs.github.com/rest/reference/meta#get-github-meta-information
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + f"/meta"
        response = self._execute("get", url, payload)
        return response

    def get_octocat(self, **payload):
        """
        Get Octocat
        https://docs.github.com/rest/reference/meta#get-octocat
        Attributes:
        Path Parameters:

        Payload Parameters:
        s
        """
        url = self._base_url + f"/octocat"
        response = self._execute("get", url, payload)
        return response

    def get_all_api_versions(self, **payload):
        """
        Get all API versions
        https://docs.github.com/rest/reference/meta#get-all-api-versions
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + f"/versions"
        response = self._execute("get", url, payload)
        return response

    def get_the_zen_of_github(self, **payload):
        """
        Get the Zen of GitHub
        N/A
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + f"/zen"
        response = self._execute("get", url, payload)
        return response
