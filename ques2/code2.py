def check(string):
    str_len = len(string)
    for itr in range(0, str_len):
        if string[itr] == 'a' and itr+3 <= str_len-1 and string[itr+1] == 'b' and string[itr+2] == 'b' and string[itr+3] == 'b':
            return "PASS"
    return "FAIL"
string=input("Enter String: ")
print(check((string)))