import md5

counter = 1

pass_in = input("Enter the MD5 hash: ")
pwfile = input('Please enter the password file: ')

try:
    pwfile = open(pwfile, 'r')
except:
    print('file not found')
    quit()
for password in pwfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    print('trying password number %d: %s ' %(counter, password.strip()))

    counter += 1

    if pass_in == filemd5:
        print('found')
        print('password is :' + password)
        break
else: print('password not found')
