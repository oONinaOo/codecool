doors = []


for i in range(0, 100):
    doors.append(0)

    for i in range(len(doors)):
        if doors[i] == 0:
            doors[i] = 1

            for i in range(len(doors)):
                if i % 2 == 0:
                    doors[i] = 0
                    
                    for i in range(len(doors)):
                        if i % 3 == 0:
                            if doors[i] == 1:
                                doors[i] = 0
                            else:
                                doors[i] = 1

                        
                        def open():
                            for i in range(len(doors)):
                                if i % x == 0:
                                     if doors[i] == 1:
                                         doors[i] = 0
                                else:
                                    doors[i] = 1

                                 for i in range(100):
                                    open()
                                
                                  

print(doors)