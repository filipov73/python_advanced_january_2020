def age_assignment(*args, **kwargs):
    dict_ = kwargs
    for key in dict_.keys():
        for name in args:
            if name[0] == key:
                dict_[name] = dict_.pop(key)
    return dict_


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# def age_assignment(*args, **kwargs):
#     result = {}
#     for name in args:
#         result[name] = kwargs[name[0]]
#     return result
#
#
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))