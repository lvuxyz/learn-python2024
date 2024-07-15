import random

ran_dom = random.randint(1, 100)
ten_file = f"{ran_dom}.txt"
with open(ten_file, 'w') as file:
    file.write(str(ran_dom))
with open(ten_file, 'r') as file:
    content = file.read()
    print(f'Noi dung tep tin {ten_file}: {content}')