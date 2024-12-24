
def test_input_text(expected_result, actual_result):
    #assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)

test_input_text(8,11)


assert abs(-42) == 42, "Should be absolute value of a number"

k = abs(-55)

print("Let's count together: {}, then goes {}, and then {}".format(1, 2, "3"))

s = "shinima: {}".format(k)

print (s)

str1 = "Show"
str2 = "must"
str3 = "go"
str4 = "on"
print(f"Song: {str1} {str2} {str3} {str4}")
print(f"Song: {str3} {str4} {str2} {str1}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

print(f"{2+3}")
