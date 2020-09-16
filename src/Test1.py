statement = "This is a test string from Andrew"
sortedStatement = sorted(statement.split(), key=str.lower)
print(sortedStatement)

print([1,2,3] * 3)

x = object()
y = object()

x_list = [x]
x_list = x_list * 10

y_list = [y]
y_list = y_list * 10

big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

mylist = [1,2,3]
print("A list : %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f"

print(format_string % data)
