import os

# 👉 Put your existing folder path here
folder_path = r"C:\Users\SAMANVAYA VATS\OneDrive\Desktop\anudip\practice-mkdir\anudip\100Problems"

files = [
'29-gcdUsingWhileLoop.py',
'30-sumUntil0Entered.py',
'31-primeNumbersBetween1AndN.py',
'32-factorialUsingForLoop.py',
'33-starPatternUsingForLoop.py',
]

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# " + file_name.replace(".py", "") + "\n")
        print(f"Created: {file_name}")
    else:
        print(f"Already exists: {file_name}")

print("\n✅ Process completed!")