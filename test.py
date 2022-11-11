import json
with open("serverInfo.json", "r", encoding="utf-8") as f:
    serverInfo = json.load(f)
    print(serverInfo)


if (next((index for (index, d) in enumerate(serverInfo) if d["id"] == 1039016204397985832), None) != None):
    current_server_index = next((index for (index, d) in enumerate(serverInfo) if d["id"] == 1039016204397985832), None)
else :
    current_server_index = len(serverInfo)

print(current_server_index)