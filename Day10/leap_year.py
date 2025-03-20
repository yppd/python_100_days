# def format_name(f_name, l_name):

#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"f_name: {formatted_f_name} {formatted_l_name}"
# print("Hello {}")

# format_name(f_name="yiAnNis", l_name="παΠαΔημΤΡΙοΥ")


def is_leap_year(year):
    # Write your code here.
    if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0:
        return 1
    else:
        return 0
    # Don't change the function name.


is_leap_year(2020)
