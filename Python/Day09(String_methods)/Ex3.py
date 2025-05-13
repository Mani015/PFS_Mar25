
x = "orange apple banana"

# print('_'.join(x))
# o_r_a_n_g_e_ _a_p_p_l_e_ _b_a_n_a_n_a


y = "classmate note book"
# syntax: str.split(sperator,max_separator) it returns in list

print(y.split())
# ['classmate', 'note', 'book']

print(y.split('a'))
# ['cl', 'ssm', 'te note book']

print(y.split('o'))
# ['classmate n', 'te b', '', 'k']


print()

print(y.split('o',2))
# ['classmate n', 'te b', 'ok']
