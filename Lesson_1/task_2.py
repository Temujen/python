source = int(input("Enter time in seconds: "))
hour = source // 3600
minute = (source % 3600) // 60
second = (source % 3600) % 60
print(f"Time in format hh:mm:ss - {hour:02d}:{minute:02d}:{second:02d}")
