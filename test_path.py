import os

print("Current working directory:", os.getcwd())

file_path = "./data/Alabama_county.csv"
print("Trying to read file at:", file_path)

try:
    with open(file_path, 'r') as f:
        print("File opened successfully!")
        # Optional: print first 3 lines just to confirm content
        for _ in range(3):
            print(f.readline().strip())
except FileNotFoundError:
    print("FileNotFoundError: File does NOT exist at this path.")
except Exception as e:
    print("Other error:", e)
