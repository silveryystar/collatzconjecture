import matplotlib.pyplot as plt


def collatz(p, n, x, y):
    for i in range(1, 100):
        p.append(i/100)

    for i in range(1, n+1):
        if i/n in p:
            print(f"{int(i/n*100)}%")

        x.append(i)

        c = 0
        while i > 1:
            if i % 2:
                i = 3*i+1

            else:
                i = i/2

            c += 1

        y.append(c)


n = input("Maximum number: ")
while True:
    try:
        n = int(n)

    except ValueError:
        n = input("Invalid input. Enter an integer.\n"
                  "Maximum number: ")

    else:
        break


p = []
x = []
y = []

collatz(p, n, x, y)

plt.scatter(x, y, s=1)

plt.xlim(-n*0.2, n*1.2)
plt.ylim(0)

plt.xlabel("Number")
plt.ylabel("Iterations")

plt.title(f"Collatz Conjecture for 1 ≤ n ≤ {n}")

plt.show()
