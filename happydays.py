#this is a program to create a holiday planner, with ticket bookings and reservations.
print(" Welcome to HAPPYDAYS, the best holiday planner in business! ")
print(" Kindly signup by providing the listed details.")
customerdetails=[]
for a in range (100):
    n1=input("enter your name:")
    m1=input("enter your gamil id:")
    no1=int(input("enter your contact number:"))
    customerdetails.append(n1)
    customerdetails.append(m1)
    customerdetails.append(no1)
    
    choice1=input("do you want to signup another account?")
    if choice1 == "yes" or choice1 == "s" :
        continue
    else:
        break
print(" Please choose your requirement.","\n" , "1. hotel bookings","\n ","2.train tickets","\n" ,"3.bus ticket","\n" ,"4.flight ticket","\n" ,"\n" ,"5.restaurant reservation")
customerchoice=int(input("enter the number of your requirement:"))
if customerchoice == 1:
    while True :
        place=input("enter your destination:")
        checkindate=input("enter check in date(d/m/y):")
        checkoutdate=input("enter check out date(d/m/y):")
        people=int(input("no of adults (13+):"))
        people2=int(input("no of children or infants:"))
        print("choose your room:", "\n", "1.service apartment","\n", "2.business suite","\n", "3.cottage ","\n", "4.villa","\n", "5.family suite")
        roomtype=int(input("enter your preference:"))
        rating=int(input("enter hotel's star rating:"))
        tarif=int(input("enter your maximum tarif per night:"))
        others=input("enter your specific preferences(eg.pool,pet friendly,gym,spa,etc):")
        print(" The shortlisted options as per your choice is sent to your mail id ","\n", "kindly check and pick one among them and send a reply mail")
        print(" Thank you for choosing HAPPY DAYS , have a wonderful trip :)")
        break
elif customerchoice==2:
    while True:
        boardingplace=input("enter your departure station:")
        arrivingplace=input("enter your destination station:")
        bdate=input("enter your boarding date:")
        btiming=input("enter your prefered boarding time:")
        dtiming=input("enter your prefered arrival time:")
        seating=input("enter your class preference (1st class ac or non ac, 2nd class ac or non ac, etc):")
        birth=input("lower, middle or upper birth:")
        p1=input("how many passengers:")
        for a in p1:
            pname=input("name:")
            page=input("age:")
            pgender=input("M/F/OTHER:")
            pno=int(input("contact no:"))
        print(" The shortlisted options as per your choice is sent to your mail id ","\n", "kindly check and pick one among them and send a reply mail")
        print(" Thank you for choosing HAPPY DAYS , have a wonderful trip :)")
        break
elif customerchoice==3:
    while True:
        bboardingplace=input("enter your boarding place:")
        barrivingplace=input("enter your destination :")
        bdate=input("enter your boarding date:")
        bbtiming=input("enter your prefered boarding time:")
        bdtiming=input("enter your prefered arrival time:")
        bustype=input(" seater,sleeper,semi-sleeper:")
        ac=input("ac or non-ac:")
        if bustype == "sleeper":
            seat=input("upper or lower birth:")
        bp1=input("how many passengers:")
        for a in bp1:
            pname=input("name:")
            page=input("age:")
            pgender=input("M/F/OTHER:")
            pno=int(input("contact no:"))
        print(" The shortlisted options as per your choice is sent to your mail id ","\n", "kindly check and pick one among them and send a reply mail")
        print(" Thank you for choosing HAPPY DAYS , have a wonderful trip :)")
        break    
elif customerchoice == 4:
    while True:
        fboardingplace=input("enter your departure city:")
        farrivingplace=input("enter your destination city:")
        bdate=input("enter your boarding date:")
        fbtiming=input("enter your prefered boarding time:")
        fdtiming=input("enter your prefered arrival time:")
        fclass=input("economy,premium economy,business or first class:")
        fare=input(" are you a regular or student or doctor and nurses or armed forces?:")
        trip=input("one-way or roundtrip?:")
        if trip == "roundtrip":
            print(" do you want to book your return flight with the same choices?", "\n", "1.yes", "\n", "2. no")
            ans=int(input(" your choice:"))
        if ans == 1:
            break
        else:
            fboardingplace=input("enter your departure city:")
            farrivingplace=input("enter your destination city:")
            bdate=input("enter your boarding date:")
            fbtiming=input("enter your prefered boarding time:")
            fdtiming=input("enter your prefered arrival time:")
            fclass=input("economy,premium economy,business or first class:")
        fp1=input("how many passengers:")
        for a in fp1:
                pname=input("name:")
                page=input("age:")
                pgender=input("M/F/OTHER:")
                pno=int(input("contact no:"))
        print(" The shortlisted options as per your choice is sent to your mail id ","\n", "kindly check and pick one among them and send a reply mail")
        print(" Thank you for choosing HAPPY DAYS , have a wonderful trip :)")
        break 
elif customerchoice == 5:
    while True:
        heads=int(input("how many heads?"))
        tables=int(input("no of tables:"))
        rname=input("restaurant name:")
        city=input("restuarant location:")
        time=input("reservation time:")
        rno=int(input("contact no:"))
        resername=input("reservation name:")
        print(" your table will be booked soon. HAPPY DAYS team will update you through your mail id","\n"," Use code HAPPYDAYS15 for 10% off")
        print(" Thank you for choosing HAPPY DAYS , have a wonderful trip :)")
        break
else:
    print("you have chosen an ivalid option, try again.")
        
                
                
            
        
            
        
        
        
        
   
    
        
                   
        
        
        

        
    
    
            
    

