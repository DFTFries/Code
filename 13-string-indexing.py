# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_num = "1234-5678-9012-3456"
credit_num = credit_num[::-1]
# print(credit_num[:4])
# print(credit_num[5:9])
# print(credit_num[5:])
# print(credit_num[-4:])
# print(credit_num[::3])

last_digits = credit_num[-4:]

# print(f"Your last digits are: XXXX-XXXX-XXXX-{last_digits}")

print(credit_num)