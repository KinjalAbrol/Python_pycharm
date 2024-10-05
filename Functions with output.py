# functions with outputs
# def my_function():
#     result = 3*2
#     return result
# print(my_function())
# nxt example
# def format_name(f_name, l_name):
#     print(f"i am {f_name}")
#     print(f"i am {l_name}")
#
# format_name("kinjal", "ayush")
# title case example
# def format_name(f_name, l_name):
#     print(f"i am {f_name}".title())
#     print(f"i am {l_name}".title())
#
# format_name("kinjal", "ayush")

# title case two in the same line:
# def format_name(f_name, l_name):
#     formated_f_name = (f"i am {f_name}")
#     formated_l_name = (f"i am {l_name}")
#     print(f"{formated_f_name}, {formated_l_name}".title())
#
# format_name("kinjal", "ayush")


# use of return at the place of return
def format_name(f_name, l_name):
    formated_f_name = (f"i am {f_name}")
    formated_l_name = (f"i am {l_name}")
    return f"{formated_f_name} {formated_l_name}".title()
print(format_name("kinjal", "ayush"))
# also like this last line
formated_string = format_name("kinjal", "ayush")
print(formated_string)