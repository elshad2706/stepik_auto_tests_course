def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
    except AssertionError:
        print(f"ожидаем {expected_result}, получили {actual_result}")

# Примеры тестирования
test_input_text(8, 11)
test_input_text(11, 11)
test_input_text(11, 15)

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

def test_substring(full_string, substring):
    try:
        assert substring in full_string
    except AssertionError:
        print(f"expected '{substring}' to be substrings of '{full_string}'")

test_substring("fulltext", "some_value")
test_substring("1","1")
test_substring("some_text", "some")







