import datetime

start = datetime.datetime.now()

# wypełniacz czasu
for i in range(1_000_000):
    a = i ** 2

stop = datetime.datetime.now()

difference = stop - start

print(difference)
