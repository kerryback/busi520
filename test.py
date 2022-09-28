import sys
name = sys.argv[1]
print("Hello", name)
with open("hello.txt", "w") as f:
    f.write("Hello " + name)