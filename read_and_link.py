import json
import requests
import os

API_RESPONSE_FILE="github-api-response.json"
GITEA_URL = "https://git.athq.de/api/v1/"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

GITEA_PASS = os.environ["GITEA_PASS"]
GITEA_USER = os.environ["GITEA_USER"]

if __name__ == "__main__":

    # query API if file not present #
    if not os.path.isfile(API_RESPONSE_FILE):

        r = requests.get("https://api.github.com/search/repositories?q=user:FAUSheppy",
                            headers={'Authorization': "token {}".format(GITHUB_TOKEN)})

        print('Authorization: '+ "token {}".format(GITHUB_TOKEN))

        with open(API_RESPONSE_FILE, "w") as f:
            f.write(json.dumps(r.json(), indent=2))

    # load file #
    with open(API_RESPONSE_FILE) as f:
        content = json.load(f)

    for item in content["items"]:
        payload = {
            "auth_token" : GITHUB_TOKEN,
            "mirror" : True,
            "repo_name" : item["name"],
            "clone_addr" : item["html_url"],
            "description" : item["description"]
        }
        print(json.dumps(payload, indent=2))
        r = requests.post(GITEA_URL + "/repos/migrate", auth=(GITEA_USER, GITEA_PASS), json=payload)
        try:
            r.raise_for_status()
            print("Create: {}".format(item["name"]))
        except requests.exceptions.HTTPError as e:
            if r.status_code == 409:
                print("Repo already created")
            else:
                raise e
