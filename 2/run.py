with open('./2/input.txt') as input:

    part_one = 0
    part_two = 0
    for i in input:
        row = i.split()
        # set up rule - [1, 3]
        rule = row[0].split('-')
        min = int(rule[0])
        max = int(rule[1])
        # set up value, remove ":"
        value = row[1].replace(':', '')
        # set up password
        password = row[2]

        # count instance of value in password, check for rule and add to count
        if (password.count(value) >= min and password.count(value) <= max):
            part_one += 1
        
        # part 2, get instances of letter in password
        instances = [pos for pos, char in enumerate(password) if char == value]
        bunk_index_first = min - 1
        bunk_index_last = max - 1

        bunk_first_in = bunk_index_first in instances
        bunk_last_in = bunk_index_last in instances
        
        if ((bunk_first_in or bunk_last_in) and not ( bunk_first_in and bunk_last_in )):
            part_two += 1

    print(part_one)
    print(part_two)
       
