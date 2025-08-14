# ДЗ 5.3. hashtag

import string

# my_string = input("Enter your string: ")
my_string = "s a<<<<< a JJJJJJJJJ  f                                                        ao    s s                                            ()()()()()($%#@$%^&*() m)"
# my_string = "i like python community!"
# my_string = "Should, I. subscribe? Yes!"

print(len(my_string))

len_string = my_string.split()
len_string = "".join(len_string)

print(len(len_string))

if len(len_string) <= 140:
    lst_my_string = list(my_string)

    for _ in range(len(lst_my_string)):
        for i in lst_my_string:
            if i in string.punctuation:
                lst_my_string.remove(i)

    join_lst = "".join(lst_my_string)
    make_title = join_lst.title()
    split_string = make_title.split()
    split_string.insert(0, "#")
    final_result = "".join(split_string)

    print(final_result)
else:
    print("Too many symbols. Max 140")