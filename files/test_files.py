f = open("test.txt");
data = f.read();
print(data);

lis = list(range(10));
f_w = open("test2.txt", "w");
f_w.write(data);
for x in lis: f_w.write(str(x) + "\n");
f_w.close();
