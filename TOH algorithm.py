def TOH(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TOH(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TOH(n - 1, auxiliary, destination, source)


n = 4
TOH(n, 'A', 'B', 'C')
