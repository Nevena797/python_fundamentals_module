filename_plus_extension = input().split("\\")  # ['C:', 'Internal', 'training-internal', 'Template.pptx']
file_name, extension = filename_plus_extension[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")