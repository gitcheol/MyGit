import sys 

n = int(input())

employees = set()
for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        employees.add(name)
    elif status == 'leave':
        employees.remove(name)


list_employees = list(employees)
list_employees.sort(reverse=True)

print('\n'.join(list_employees))
