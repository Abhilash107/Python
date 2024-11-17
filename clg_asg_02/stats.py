import statistics
list = [1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6]
mean = statistics.mean(list)
print(f'{mean:.2f}')
print(statistics.mode(list))
print(statistics.median(list))
