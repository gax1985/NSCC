# Author: Mohammad Al Jokhadar
# Date: Sept. 27th, 2023
# Description: Here we have a Python script that converts weights given in imperial to metric weights, which include
# tons, stones, pounds and ounces
 

def main():

#   Let us get started! First, let us take a look at the equations kindly provided by our instructor (Thank you!):

#   total ounces = (35840 * tons) + (224 * stone) + (16 * pounds) + ounces

#   total kilos = total ounces / 35.274

#-------------------------------------------------------------------------------------------------------------------


        #===========================================================================

        #   Now, we have the fun part : Interacting with the user ! We ask the user 
        #   for the number of tons, stones, pounds and ounces : 

        #---------------------------------------------------------------------------



        print("""===================================================================
 _____ _         _____                          _       ____  ___     _        _        _____ _____      
|_   _| |       |_   _|                        (_)     | |  \/  |    | |      (_)      |_   _|_   _|  _  
  | | | |__   ___ | | _ __ ___  _ __   ___ _ __ _  __ _| | .  . | ___| |_ _ __ _  ___    | |   | |   (_) 
  | | | '_ \ / _ \| || '_ ` _ \| '_ \ / _ \ '__| |/ _` | | |\/| |/ _ \ __| '__| |/ __|   | |   | |       
  | | | | | |  __/| || | | | | | |_) |  __/ |  | | (_| | | |  | |  __/ |_| |  | | (__   _| |_ _| |_   _  
  \_/ |_| |_|\___\___/_| |_| |_| .__/ \___|_|  |_|\__,_|_\_|  |_/\___|\__|_|  |_|\___|  \___/ \___/  (_) 
                               | |                                                                       
                               |_|                                                                       
 _____ _           ______     _                             __   _   _            _   _       _ _        
|_   _| |          | ___ \   | |                           / _| | | | |          | | | |     (_) |       
  | | | |__   ___  | |_/ /___| |_ _   _ _ __ _ __     ___ | |_  | |_| |__   ___  | | | |_ __  _| |_      
  | | | '_ \ / _ \ |    // _ \ __| | | | '__| '_ \   / _ \|  _| | __| '_ \ / _ \ | | | | '_ \| | __|     
  | | | | | |  __/ | |\ \  __/ |_| |_| | |  | | | | | (_) | |   | |_| | | |  __/ | |_| | | | | | |_      
  \_/ |_| |_|\___| \_| \_\___|\__|\__,_|_|  |_| |_|  \___/|_|    \__|_| |_|\___|  \___/|_| |_|_|\__|     
                                                                                                         
===================================================================""")
        

        print("""Behold, on a land
        far far away ...

        a few metric units, 
        were visiting today

        One of them, with a name tons \n """)
        tons =input("""How many, would you say, 
        were there of tons  ? \n \n""")
        
        tons = float(tons)


        print(""" and there were many, 
        many a-stone,
        How many would you say,""")
        
        stones = input("were there of stones? \n")

        stones = float(stones)

        print("""\n \nFollowed them, they did 
            those named pounds...
              
            How many, would you say,""") 
        pounds = input("were there in pounds ?\n" )

        pounds = float(pounds)

        print("""\n \n... and finally, here they come
        ... those named ounces
              
        How many, would you say,""")
        ounces = input("were there in ounces ?\n")

        ounces = float(ounces)

       #    Here comes the math part :D  

        import math 

#   Let us translate these quations to the Python language. Let us do the math : 
# ==============================================================================================

        TonsConverter = float(35840 *tons)        

        #   ... and a variable for stones : 

        StoneConverter= float(224 * stones)
        
        #   ... and a variable for pounds :

        PoundsConverter=float(16 * pounds)

        #   ... It is a great idea to add them all together!

        TotalOunces = (TonsConverter + StoneConverter + PoundsConverter + ounces)


        #   ... We should accertain the total number of kilograms that we have :

        TotalKilos = float(TotalOunces / 35.2748)  # Added float to the whole variable


      #  TotalGrams = (TotalKilos * 1000)      

        
        
        
        
        
        
        CalculatedTons = float(TotalKilos/1000)

        CalculatedKilograms = float(TotalKilos)-(int(CalculatedTons) * 1000)

        CalculatedGrams = ((float(CalculatedKilograms)*1000))-(int(CalculatedKilograms)*1000)





        #CalculatedGrams = (TotalKilos*1000)-(int(CalculatedKilograms)*1000)

        # New method ------ multiplying TotalOunces X 28.3495

        #grams = (TotalOunces*28.3495)


        ########################CalculatedKilograms = (grams / 1000)

       # CalculatedKilograms = math.floor(grams / 1000)


        # New Method ---- Now we have the grams, let us figure out the tons : 

       # CalculatedTons = (grams / 1000000)

        #CalculatedKilograms = (math.floor(CalculatedTons))*1000

        #CalculatedGrams = 

        #CalculatedTons = float(CalculatedTons)

       # CalculatedGrams = ((CalculatedKilograms)*1000)
        
        #CalculatedGrams = (float(CalculatedKilograms) - int(CalculatedKilograms)) * 1000 
   
       # CalculatedGrams = int(CalculatedGrams)
       

        #CalculatedKilograms = (grams / 1000)

        
       
        #CalculatedKilograms = int(CalculatedKilograms)
       
       #    Now comes the time for presenting our dearest user with the much needed metric results : 
       #    ========================================================================================

       #    Tons :
       
       
       
        print("""There they were, those friends of ours,
        The {} metric of tons\n""".format(int(CalculatedTons)))


        #   Kilograms : 


        print("""   The mightiest {} kilos\n""".format(int(CalculatedKilograms)))


        #   ... and grams :

        #grams = (float(TotalKilos)*1000)
        

        #CalculatedGrams = math.floor(grams/1000000)

        print("""   ... and the amazing {:.1f} Grams!""".format(float(CalculatedGrams)))

        #print("""   ... and the amazing {:.1f} Grams!""".format(grams))




#       Note : I 



if __name__ == "__main__":
    main()
