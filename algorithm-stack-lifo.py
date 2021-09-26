# Пример использования стека типа LIFO

a = input("Введите строку: ")
stack = []
flVerify = True

for lt in a:
    if lt in "([{":
        stack.append(lt)
    elif lt in ")]}":
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:    # стек по итогам проверок должен быть пустым
    print("Yes")
else:
    print("No")
