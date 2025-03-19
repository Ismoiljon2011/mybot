a = open("data.txt", "r").readlines()

ismoiljon = int(a[0])
izzatbek = int(a[1])


def update(a):
    ismoiljon = int(a[0])
    izzatbek = int(a[1])


def save_voice(ismoiljon, izzatbek):
    with open("data.txt", "w") as f:
        f.write(f"{ismoiljon}\n{izzatbek}")
        f.close()
    update(open("data.txt", "r").readlines())
