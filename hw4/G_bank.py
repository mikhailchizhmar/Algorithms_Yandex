accounts = {}


def check_name(name):
    if name not in accounts:
        accounts[name] = 0


def deposit(name, amount):
    check_name(name)
    accounts[name] += amount


def income(percent):
    for client in accounts:
        if accounts[client] > 0:
            accounts[client] += accounts[client] * percent // 100


def balance(name):
    if name in accounts:
        print(accounts[name])
    else:
        print("ERROR")


def withdraw(name, amount):
    check_name(name)
    accounts[name] -= amount


def transfer(name1, name2, amount):
    check_name(name1)
    check_name(name2)
    accounts[name1] -= amount
    accounts[name2] += amount


with open("input.txt", "r") as inp:
    text = inp.read().rstrip().split("\n")

for line in text:
    operation = line.split()
    if operation[0] == "DEPOSIT":
        deposit(operation[1], int(operation[2]))
    elif operation[0] == "INCOME":
        income(int(operation[1]))
    elif operation[0] == "BALANCE":
        balance(operation[1])
    elif operation[0] == "TRANSFER":
        transfer(operation[1], operation[2], int(operation[3]))
    elif operation[0] == "WITHDRAW":
        withdraw(operation[1], int(operation[2]))
