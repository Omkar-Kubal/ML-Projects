import os

# Absolute path check
file_path = os.path.join(os.getcwd(), 'notebook', 'data', 'stud.csv')
print(f"Checking file path: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")