def server(duration,cpu,budget):
  #reverse order
  usEastPrice = [2.82,1.4,0.774,0.45,0.23,0.12]
  usWestPrice = [2.97,1.3,0.89,0.413,0.14]
  duration = float(duration)
  print(duration,cpu,budget)
  if(cpu == 0):
    print("Case 2")
  elif(cpu > 0):
    if(budget == 0):
      if(cpu > 32):
        #CASE 1
        # US EAST
        newlist = [0,0,0,0,0,0]
        newprice = [0,0,0,0,0,0]
        balance = cpu
        finalPrice = 0
        pricewduration = 0
        div = int(32)
        for i in range (6):
            newvar = int(balance/div) 
            newlist[i] = newvar
            if(newlist[i] != 0):
                balance -= (newlist[i] * div)
            div = div / 2
            
        for i in range (6):
            newprice[i] = newlist[i] * usEastPrice[i]
            
        for i in range (6):
            finalPrice = finalPrice + newprice[i]
        pricewduration = finalPrice * duration

        print("region US East")
        print(f"Total Cost {pricewduration}")
        print(f"Servers:\nlarge: {newprice[5]}\nxlarge: {newprice[4]}\n 2xlarge: {newprice[3]}\n4xlarge: {newprice[2]}\n8xlarge: {newprice[1]}\n10xlarge: {newprice[0]}")

        #US WEST
        
        wnewlist = [0,0,0,0,0]
        wnewprice = [0,0,0,0,0]
        wbalance = cpu
        wfinalPrice = 0
        wdiv = int(32)

        for i in range (5):
            if (wdiv == 2):
                wdiv = 1
            wnewvar = int(wbalance/wdiv) 
            wnewlist[i] = wnewvar
            if(wnewlist[i] != 0):
                wbalance -= (wnewlist[i] * wdiv)
            if(wdiv!= 1):
                wdiv = wdiv / 2
            #print (wnewlist)
            
        for i in range (5):
            wnewprice[i] = wnewlist[i] * usWestPrice[i]
            
        for i in range (5):
            wfinalPrice = wfinalPrice + wnewprice[i]
        wpricewduration = wfinalPrice * duration

        print("region US West")
        print(f"Total Cost {wpricewduration}")
        print(f"Servers:\nlarge: {wnewprice[4]}\n 2xlarge: {wnewprice[3]}\n4xlarge: {wnewprice[2]}\n8xlarge: {wnewprice[1]}\n10xlarge: {wnewprice[0]}")


      
    elif(budget > 0):
      print("Case 3")


if __name__=="__main__":
      name = input("Enter your Name: ")
      print("Hello "+name)
      duration = input("Enter the duration you want for your servers: ")
     # region = int(input("Enter 1 for US-EAST and 2 for US-WEST: "))
      cpu = int(input("Enter number of CPU, Enter 0 if you dont know: "))
      if (cpu == 0):
          budget = input("Enter the amount of money you would like to pay: ")
          server(duration,cpu,budget)#case2 us-east
          
      elif (cpu > 0):
            budget = int(input("Enter a budget, enter 0 if you dont have any: "))
            if (budget == 0):
              server(duration,cpu,budget)#case1 us-east 
            elif (budget > 0):
              server(duration,cpu,budget)#case3 us-east
      else:
        print("Invalid CPU size")
  




    # cpu = input("Enter number of CPU you require: ")
    # duration = input("Enter the duration in hours: ")  
    # server = int(input("Enter 1 for US-EAST and 2 for US-WEST: "))
    # if( server == 1):
    #   server()
    # elif( server == 2):
    #   usWest()
    # else:
    #   print("Enter valid server")