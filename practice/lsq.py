


def average():
    total_n, cnt = 0, 0

    while True:
        line = input()

        if not line:
            break
                
        total_n += float(line)
        cnt     += 1

    print("Average is:", total_n / cnt)



if __name__ == "__main__":
    average()


