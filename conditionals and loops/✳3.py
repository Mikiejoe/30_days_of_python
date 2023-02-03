for row in range(7):
    for col in range(7):
        if(col == 6 or row==0 or col>=row):
            print("*" , end=" ")
        else:
            print(' ', end=' ')
            
    print()
