import sys

semina = []
semina_num = int(sys.stdin.readline().rstrip())
room_num = [["Algorithm","204"],["DataAnalysis","207"],["ArtificialIntelligence","302"],["CyberSecurity","B101"]
            ,["Network","303"],["Startup","501"],["TestStrategy","105"]]

for i in range(semina_num):
    semina.append(sys.stdin.readline().rstrip())

for i in range(semina_num):
    for j in range(len(room_num)):
        if semina[i] == room_num[j][0]:
            print(room_num[j][1])
            break
    
