"""Initialize the Notion client to access Notion programmatically."""

import os
from pprint import pprint
from notion_client import Client

NOTION_CLIENT: Client = Client(auth=os.environ["NOTION_TOKEN"])

if __name__ == "__main__":
    list_users_response = NOTION_CLIENT.users.list()
    pprint(list_users_response)
