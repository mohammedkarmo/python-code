import json
while True:
    
    rr = open('data.json' , "r+")
    with rr as f:
      x = json.load(f)

      q = input('Choose 1 for user 2 for developer\n')
      
      if q == "exit" or q == "Exit" or q == "EXIT" :
                  break

      q = int(q)
      if q == 1:         
          z = input("enter word:\n")
          if z in x:
              print(x[z])
      if q == 2:
          while True:
              
              c = input("enter English word (exit for quit):\n")
              if c == "exit" or c == "Exit" or c == "EXIT" :
                  break
                  
              d = input("enter Arabic word:\n")
              m = {c:d}
              x.update(m)
              f.seek(0)
              print(json.dumps(m))
              json.dump(x, f)

    
