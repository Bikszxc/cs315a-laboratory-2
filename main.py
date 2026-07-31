# NAOS LEGENDS | CAFE SOLUTION
# JANERVEN & BICKOY

from fastapi import FastAPI

app = FastAPI()

users = []


@app.post("/users/{username}")
async def create_user(username: str, password: str, initial_balance: int = 0):
    for user in users:
        if user["username"] == username:
            return {"message": "Username already exists"}

    users.append(
        {"username": username, "password": password, "balance": initial_balance}
    )

    return {"message": "User created successfully"}


@app.put("/users/{username}/balance")
async def topup_balance(username: str, amount: int):
    for user in users:
        if user["username"] == username:
            user["balance"] += amount
            return {
                f"message: {username} topped up successfully. New balance: {user['balance']}"
            }

    return {"message": "User not found"}


@app.get("/users/{username}/balance")
async def get_balance(username: str):
    for user in users:
        if user["username"] == username:
            return {"balance": user["balance"]}

    return {"message": "User not found"}


@app.get("/users")
async def get_all_users():
    if users == []:
        return {"message": "No available users"}

    return {"users": users}


@app.delete("/users/{username}")
async def delete_user(username: str):
    for user in users:
        if user["username"] == username:
            users.remove(user)
            return {"message": "User deleted successfully"}

    return {"message": "User not found"}
