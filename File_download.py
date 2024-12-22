import os

a = os.path.dirname(__file__)
current_dir = os.path.abspath(a)
file_path = os.path.join(current_dir, 'Control.py')

print (current_dir)

print(os.path.abspath(__file__))

print (file_path)