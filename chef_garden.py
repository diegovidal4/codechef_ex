def cmp(a,b):
    return ((a > b) - (a < b))

#Check if tree heights are in zigzag
# def zigzag(arr):
#     for i in arr:
#


def main():
    #Number of input cases
    t = int(input())
    for i in range(0,t):
        # Number of trees
        n = int(input())
        for j in range(0,n):
            # Initial height and grow speed
            d = input()
            h = int(d.split(" ")[0])
            m = int(d.split(" ")[1])

if __name__ == '__main__':
    main()
