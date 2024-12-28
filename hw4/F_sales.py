with open("input.txt", "r") as inp:
    text = inp.read().rstrip().split("\n")

db = {}
for row in text:
    name, goods, amount = row.split()
    if name not in db.keys():
        db[name] = {}
    if goods not in db[name].keys():
        db[name][goods] = 0
    db[name][goods] += int(amount)

for name in sorted(db):
    print(name + ":")
    for goods in sorted(db[name]):
        print(goods, db[name][goods])
