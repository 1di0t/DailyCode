import sys

beers = int(sys.stdin.readline().rstrip())

for i in range(beers,-1,-1):
    if i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        if beers == 1:
            print(f"Go to the store and buy some more, {beers} bottle of beer on the wall.")
        else:
            print(f"Go to the store and buy some more, {beers} bottles of beer on the wall.")
    elif i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
