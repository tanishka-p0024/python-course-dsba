total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")