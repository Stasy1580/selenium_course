s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')
else:
    print('Substring not found')


index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
else:
    print('Substring not found')

def test_substring(full_string, substring):
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring,full_string)

test_substring("1", "2")