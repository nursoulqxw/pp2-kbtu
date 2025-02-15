import json

with open("sample-data.json") as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""  # Описание может быть пустым
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")