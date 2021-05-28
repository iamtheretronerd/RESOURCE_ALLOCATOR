def server(duration,cpu,budget):
  #reverse order
  usEastPrice = [2.82,1.4,0.774,0.45,0.23,0.12]
  usWestPrice = [2.97,1.3,0.89,0.413,0.14]
  duration = float(duration)
  budget = float(budget)
  #print(duration,cpu,budget)
  if(cpu == 0):
    # print("Case 2")
    # CASE 2
    budgetph = float(budget/duration)
    newlist = [0,0,0,0,0,0]
    newvar = budgetph
    e = 32
    f = 32
    totusecpu = 0
    totuswcpu = 0

    for i in range(6):
        newlist[i] = int(newvar/usEastPrice[i])
        if(newlist[i] > 0):
            newvar -= (usEastPrice[i]*newlist[i])
    #print(newlist)

    for i in range(6):
      totusecpu += newlist[i] * e
      e = e/2

    print("region US East")
    print(f"Total CPU: {int(totusecpu)}")
    print(f"Servers:\nlarge: {newlist[5]}\nxlarge: {newlist[4]}\n2xlarge: {newlist[3]}\n4xlarge: {newlist[2]}\n8xlarge: {newlist[1]}\n10xlarge: {newlist[0]}\n")


    wnewlist = [0,0,0,0,0]
    wnewvar = budgetph
    for i in range(5):
        wnewlist[i] = int(wnewvar/usWestPrice[i])
        if(wnewlist[i] > 0):
            wnewvar -= (usWestPrice[i] * wnewlist[i])
    #print(wnewlist)

    for i in range (5):
      if(f ==2):
          f=1
      totuswcpu += wnewlist[i] * f
      f = f/2

    print("region US West")
    print(f"Total CPU: {int(totuswcpu)}")
    print(f"Servers:\nlarge: {wnewlist[4]}\n2xlarge: {wnewlist[3]}\n4xlarge: {wnewlist[2]}\n8xlarge: {wnewlist[1]}\n10xlarge: {wnewlist[0]}")

  elif(cpu > 0):
    if(budget == 0):
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
        print(f"Total Cost ${round(pricewduration,1)}")
        print(f"Servers:\nlarge: {newlist[5]}\nxlarge: {newlist[4]}\n2xlarge: {newlist[3]}\n4xlarge: {newlist[2]}\n8xlarge: {newlist[1]}\n10xlarge: {newlist[0]}\n")

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
            #price of all servers
            
        for i in range (5):
            wfinalPrice = wfinalPrice + wnewprice[i]
        wpricewduration = wfinalPrice * duration

        print("region US West")
        print(f"Total Cost ${round(wpricewduration,1)}")
        print(f"Servers:\nlarge: {wnewlist[4]}\n2xlarge: {wnewlist[3]}\n4xlarge: {wnewlist[2]}\n8xlarge: {wnewlist[1]}\n10xlarge: {wnewlist[0]}")

      
    elif(budget > 0):
      # print("Case 3")
      # CASE 3
      budgetph = float(budget/duration)
      newelist = [0,0,0,0,0,0]
      newevar = budgetph
      e = 32
      f = 32
      totusecpu = 0
      totuswcpu = 0
      # priceperhour = [0,0,0,0,0,0]
      # totalprice = 0
      for i in range(6):
          newelist[i] = int(newevar/usEastPrice[i])
          if(newelist[i] > 0):
              newevar -= (usEastPrice[i]*newelist[i])

      for i in range(6):
          totusecpu += newelist[i] * e
          e = e/2


      wnewelist = [0,0,0,0,0]
      wnewevar = budgetph
      for i in range(5):
          wnewelist[i] = int(wnewevar/usWestPrice[i])
          if(wnewelist[i] > 0):
              wnewevar -= (usWestPrice[i] * wnewelist[i])
              
      for i in range (5):
          if(f ==2):
              f=1
          totuswcpu += wnewelist[i] * f
          f = f/2

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
          #price of all servers
          
      for i in range (5):
          wfinalPrice = wfinalPrice + wnewprice[i]
      wpricewduration = wfinalPrice * duration


      if(pricewduration >= budget):
          print(f"\nSorry you will have to pay ${round(pricewduration-budget,1)} more to purchase {cpu} CPU for {duration }hours for a US East server")
      else:
          print("region US East")
          print(f"You can buy {int(totusecpu)} CPU for ${budget}")
          print(f"Total CPU: {int(totusecpu)}")
          print(f"Servers:\nlarge: {newelist[5]}\nxlarge: {newelist[4]}\n2xlarge: {newelist[3]}\n4xlarge: {newelist[2]}\n8xlarge: {newelist[1]}\n10xlarge: {newelist[0]}\n")
          
      if(wpricewduration >= budget):
          print(f"\nSorry you will have to pay ${round(wpricewduration-budget)} more to purchase {cpu} CPU for {duration} hours for a US West server")
      else: 
          print("region US West")
          print(f"You can buy {int(totuswcpu)} CPU for ${budget}")
          print(f"Total CPU: {int(totuswcpu)}")
          print(f"Servers:\nlarge: {wnewelist[4]}\n2xlarge: {wnewelist[3]}\n4xlarge: {wnewelist[2]}\n8xlarge: {wnewelist[1]}\n10xlarge: {wnewelist[0]}")





if __name__=="__main__":
      name = input("Enter your Name: ")
      print("Hello "+name)
      duration = int(input("Enter the duration(hours) you want for your servers: "))
      if(duration > 1):
          cpu = int(input("Enter number of CPU, Enter 0 if you dont know: "))
          if (cpu == 0):
              budget = input(f"Enter the amount of money you would like to pay for {duration}hours: $")
              server(duration,cpu,budget)#case2 us-east
              
          elif (cpu > 0):
                budget = int(input("Enter a budget, enter 0 if you dont have any: $"))
                if (budget == 0):
                  server(duration,cpu,budget)#case1 us-east 
                elif (budget > 0):
                  server(duration,cpu,budget)#case3 us-east
          else:
            print("Invalid CPU size")
      else:
        print("Invalid Duration")



