while True:
    reply = input('enter text: ')
    if reply == 'stop':
        print('exit')
        break
    else:
        print(reply.upper())
        if reply.isdigit():
            print(int(reply) ** 2)
        else: print('non digit')
print('bye')
