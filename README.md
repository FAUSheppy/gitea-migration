# Description
Collection of scripts to migrate GitHub repositories to GitTea as mirrors.

# Environment Variables

    API_RESPONSE_FILE="github-api-response.json"
    GITEA_URL = "https://<your_domain>/api/v1/"
    GITEA_USER = <gitea user>
    GITEA_PASS = <gitea passwort, if you use external OIDC, you need to set on after logging in>
    GITHUB_TOKEN = <github token created in developer settings with read_code & metadata>
