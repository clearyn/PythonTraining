#print('Hello {a} {b}! You just delved into python.'.format(a=first,b=last))
# IF ELSE
n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0:
    if(n in range(2, 6)):
        print("Not Weird")
    elif(n in range(6, 21)):
        print("Weird")
    elif(n > 20):
        print("Not Weird")

# LEAP
def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year % 100 == 0):
        if(year % 400 == 0):
            leap = True
        else:
            leap = False
    elif(year % 4 == 0):
        leap = True
            
    return leap

# COMPERHENSION
x = int(input())
y = int(input())
z = int(input())
n = int(input())
list_under_n = []
for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i+j+k != n:
                    list_under_n.append([i,j,k])

# RUNNER UP
n = int(input())
arr = map(int, input().split())
arr_list = list(set(arr))
arr_sorted = []
while arr_list:
    current_value = arr_list[0]
    current_index = 0
    for idx, data in enumerate(arr_list):
        if data > current_value:
            current_value = data
            current_index = idx
    arr_sorted.append(current_value)
    del arr_list[current_index]
    
print(arr_sorted[1])

# PERCENT
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total_line = 0
line_count = 0
for i in student_marks[query_name]:
    total_line += 1
    line_count += i
print('{:.2f}'.format(line_count/total_line))

#LIST FUNCTION
def function_switcher(command):
    switcher = {
        'insert': lambda: input_list.insert(int_value[0],int_value[1]),
        'print': lambda: print(input_list),
        'remove': lambda: input_list.remove(int_value[0]),
        'append': lambda: input_list.append(int_value[0]),
        'sort': lambda: input_list.sort(),
        'pop': lambda: input_list.pop(),
        'reverse': lambda: input_list.reverse() 
    }
    return switcher.get(command, lambda: print('invalid command'))()
N = int(input())
input_list = []
for _ in range(0, N):
    command, *value = input().split()
    int_value = list(map(int, value))
    function_switcher(command)

#SWAP
def swap_case(s):
    swapped_char = ''
    for char in s:
        if(char.isupper() == True):
            swapped_char += (char.lower())
        elif(char.islower() == True):
            swapped_char += (char.upper())
        else:
            swapped_char += char
    return swapped_char

#COUNTSTRING
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if(string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count

#BINARY
binary = list(input())
container1 = []
container2 = []

for i in binary:
    if(i == '1'):
        container1.append(i)
    elif(i == '0'):
        container2.append(i)

s_binary = ''.join(container1 + container2)
print(s_binary)

#VOWELS
input = input()
totalVowels = 0
for char in input:
    if char in "aiueoAIUEO":
        totalVowels += 1
print(totalVowels)

#REVERSE
input = 'abcde'
reverse_str = ""
for i in input:
    reverse_str=i+reverse_str
print(reverse_str)

#RIGHTCOUNT
input = [5, 7, 1, 2, 8, 4, 3]
sum = 10
found = False
for i in input:
  for j in input:
    if (i + j) == sum:
      print("%i + %i" % (i, j))
      found = True
      break
  if found == True:
    break

#R_DOUBLE
def remove_d(input):
  list_input = list(input)
  recorded = ''
  result = ''
  for s in list_input:
    if s not in recorded:
      result = result+s
      recorded += s
    else:
      result += ''
  return result

print(remove_d('aabbccdd'))
