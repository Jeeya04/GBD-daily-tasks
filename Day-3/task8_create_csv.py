import csv

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Rahul", 23])
    writer.writerow([2, "Simran", 22])
    writer.writerow([3, "Karan", 25])

print("CSV created")
