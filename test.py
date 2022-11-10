import json
with open("serverInfo.json", "r", encoding="utf-8") as f:
    serverInfo = json.load(f)
    print(serverInfo)

current_server_index = next((index for (index, d) in enumerate(serverInfo) if d["id"] == 5), None)

print(current_server_index)