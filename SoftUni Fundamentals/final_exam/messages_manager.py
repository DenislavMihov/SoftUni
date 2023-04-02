capacity = int(input())
users = {}

while True:
    command = input().split("=")
    if command[0] == "Statistics":
        break
    elif command[0] == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in users:
            users[username] = {"sent": sent, "received": received}
    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender]["sent"] += 1
            users[receiver]["received"] += 1
            if users[sender]["sent"] + users[sender]["received"] == capacity:
                users.pop(sender)
                print(f"{sender} reached the capacity!")
            if users[receiver]["sent"] + users[receiver]["received"] == capacity:
                users.pop(receiver)
                print(f"{receiver} reached the capacity!")
    elif command[0] == "Empty":
        username = command[1]
        if username in users:
            users.pop(username)
        if username == "All":
            users.clear()

users_count = len(users)
print(f"Users count: {users_count}")

for user in users.keys():
    messages_count = users[user]["sent"] + users[user]["received"]
    print(f"{user} - {messages_count}")
    


