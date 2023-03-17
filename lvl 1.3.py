n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("* "*i if i%2!=0 else "# "*i)
