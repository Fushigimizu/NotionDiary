import requests
import json
import datetime

""" TOKEN = ""
DATABASE_ID = ""
PROPERTY = "" """

# 検索
def search(conf, title):
    """search target page in database

    Args:
        conf (dict): Config
        title (str): Target page title

    Returns:
        dict: Search result
    """
    header = {"Authorization": f"Bearer {conf['token']}",
              "Notion-Version": "2021-05-13",
              "Content-Type": "application/json"
              }
    url_search = f"https://api.notion.com/v1/databases/{conf['databaseId']}/query"
    payload_search = {
        "filter": {
            "property": conf["property"],
            "text": {
                "equals": title
            }
        }
    }
    req_search = requests.post(
        url_search, data=json.dumps(payload_search), headers=header)
    search_json = req_search.json()
    print(search_json)
    return search_json


def create(conf, title):
    """create target page in database

    Args:
        conf (dict): Config
        title (str): Target page title

    Returns:
        dict: Create result
    """
    header = {"Authorization": f"Bearer {conf['token']}",
              "Notion-Version": "2021-05-13",
              "Content-Type": "application/json"
              }
    url_create = "https://api.notion.com/v1/pages"
    payload_create = {
        "parent": {
            "database_id": conf["databaseId"]
        },
        "properties": {
            conf["property"]: {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
        }
    }
    req_create = requests.post(
        url_create, data=json.dumps(payload_create), headers=header)
    create_json = req_create.json()
    print(create_json)
    return create_json

def write(conf, id, content):
    """write contents to target page

    Args:
        conf (dict): Config
        id (str): Target page id
        content (str): contents to write
    """
    header = {"Authorization": f"Bearer {conf['token']}",
              "Notion-Version": "2021-05-13",
              "Content-Type": "application/json"
              }
    url_patch = f"https://api.notion.com/v1/blocks/{id}/children"

    nowtime = datetime.datetime.now().time()
    timestamp = nowtime.isoformat('seconds')
    payload_patch = {
        "children": []
    }
    if conf["timestamp"]:
        payload_patch["children"].append({
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                    "text": [{"type": "text", "text": {"content": timestamp}}]
                            }
                        })
    payload_patch["children"].append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                                "text": [{"type": "text", "text": {"content": content}}]
                        }
                    })
    req_patch = requests.patch(
        url_patch, data=json.dumps(payload_patch), headers=header)
    print(req_patch.json())


def send(title, content):
    try:
        with open("config", "r") as f:
            conf = json.load(f)
        TOKEN = conf["token"]
        DATABASE_ID = conf["databaseId"]
        PROPERTY = conf["property"]
    except FileNotFoundError:
        return
    else:
        search_json = search(conf, title)
        results = search_json.get("results")
        if results == []:
            # 作成
            results.append(create(conf, title))
        write(conf, results[0].get("id"), content)
