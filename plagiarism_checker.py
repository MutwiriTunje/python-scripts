from difflib import SequenceMatcher

# def plagiarism_checker(f1, f2):
#     try:
#         with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
#             f1_data = file1.read()
#             f2_data = file2.read()
#             res = SequenceMatcher(None, f1_data, f2_data).ratio()
#             print(f"These files are {res * 100:.2f}% similar")
#     except FileNotFoundError:
#         print("One or both files not found. Please check the paths.")

# f1 = input("Enter file_1 path: ")
# f2 = input("Enter file_2 path: ")
# plagiarism_checker(f1, f2)

def plagiarism_checker(f1, f2):
    try:
        with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
            f1_data = file1.read()
            f2_data = file2.read()
            res = SequenceMatcher(None, f1_data, f2_data).ratio()
            print(f"These files are {res * 100:.2f}% similar")
    except FileNotFoundError:
        print("One or both files not found. Please check the paths.")

f1 = input("Enter file_1 path: ")
f2 = input("Enter file_2 path: ")
plagiarism_checker(f1, f2)
