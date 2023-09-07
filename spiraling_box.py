def create_box(m, n):  ## m and n positive integers
    outer_box = [];
    
    for i in range(m + 1):
        box = []
        for j in range(n + 1):
            if(i == 0 or i == m or j == 0 or j == n):
                box.append(1)
            else:
                box.append(i + 1)
        outer_box.append(box)
    return outer_box

print(create_box(5, 8))