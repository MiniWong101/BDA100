def welcomeMessage():
  
    print("|====================================================|")
    print("|Welcome to Private Covid-19 Vaccination system(PCVS)|")
    print("|====================================================|\n")
    print("|========================|")
    print("|Step 1: Purchase vaccine|")
    print("|========================|")


game_ended = False
accPrice = 0 
vaccine_Name_noOf_vial= []
schedules = ["1/10/2021","2/10/2021","3/10/2021"]
health_center = ["University of Malaya Medical Centre","Kuala Lumpur Convention Centre","Stadium National Bukit Jalil"]


def getBatchData():
  global accPrice
  global game_ended
  global global_one_vaccine
  while not game_ended:
    batchID=input('\nEnter batch ID / Press <Enter> to exit: ')
    if batchID!="":
      date = input('Enter date of purchase [Eg. date/month/year]: ')
      manufacturer=input('Enter manufacturer name: ')
      vaccineName=input('Enter vaccine name: ')
      originCountry=input('Enter the origin country: ')
      vialPrice=float(input('Enter price per vial: '))
      noOfvial=int(input('Enter number of vial: '))
      if vialPrice<=0 or noOfvial<=0:
        print('Zero or negative value is not allowed')
      else:
        batchTotalPrice=vialPrice*noOfvial
        accPrice += batchTotalPrice
        dict_name_vial = {vaccineName:noOfvial}
        vaccine_Name_noOf_vial.append(dict_name_vial)

        displayInvoice(batchID,date,manufacturer,vaccineName,originCountry,vialPrice,noOfvial,batchTotalPrice)

    else:
      print(f"Total price for all batch {accPrice}")
      game_ended = True

def displayInvoice(batch,dat,manu,vaccine,origin,vial,no,totalPrice):
  print('=================================================')
  print('Invoice for <',batch,'>')
  print('Date:',dat)
  print('-------------------------------------------------')
  print('VACCINE DETAILS')
  print('Producer:',manu)
  print('Country:',origin)
  print('Vaccine name:',vaccine)
  print('-------------------------------------------------')
  print('PURCHASE DETAILS')
  print('Price per vial:',vial)
  print('Number of vials purchased:',no)
  print('Total Price: $',totalPrice)
  print('=================================================')

def displayVaccines(all_vaccine_Name_all_noOf_vial,all_schedules):
  print("vaccine’s availabilities and schedules")
  print(f"Total types of vaccine and total number of vaccine {vaccine_Name_noOf_vial}")
  print(f"Health center offer vaccination {health_center}")
  print(f"Time schedules: {all_schedules}")


def welcomeMessage2():
  print('\n')
  print('|==============================|')
  print('|Step 1: Vaccination Appoinment|')
  print('|==============================|')

Multiple_vaccine_left = 0
vaccine_left = 0
def getAppointment():
  global vaccine_left
  global Multiple_vaccine_left
  appoinment_ended = False
  while not appoinment_ended:
    patientID = input("Enter patient ID / Press <Enter> to exit: ")
    if patientID != "":
      name = input("What is your name? ")
      vaccine_name = input("Choose one vaccine from above that you would like to take ")
      health_center = input("Choose one health center from above that you would like to go ")
      appoinment_date_time = input("Choose one appoinment date from above that you prefer ")
      fee = int(input("enter amount "))
      # compare option that patient choosen with dictionary that store multiple batch and type of vaccine. And save the correct type of vaccine as a list into dict_choice.
      dict_choice = next(item for item in vaccine_Name_noOf_vial if item[vaccine_name])
      # print(dict_choice)
      number_of_vaccine_left = dict_choice.values()
      # extract value from dict_choice (dictionary) and change it to a list and store it in number_of_vaccine_left. 
      for vac in number_of_vaccine_left:
        #loop through the list and save it inside Multiple_vaccine_left. However there is a logic error here. cause we are using while loop so it will continue add up again and again. In result we cant check for selected vaccine is zero.
          Multiple_vaccine_left += vac
          if Multiple_vaccine_left == vac:
            # In order calculate selected vaccine is zero, we need to set up a new if statement and a new variable. This variable only adding once.
            vaccine_left +=Multiple_vaccine_left
      print(vaccine_left)
      if fee<=0 :
        print('Zero or negative value is not allowed')
      elif vaccine_left<=0:
        print("Sorry, run out of vaccine. Please Choose another")
      else:
        vaccine_left -= 1
        print(vaccine_left)
        displayAppointment(patientID,name,vaccine_name,health_center,appoinment_date_time,fee)
    else:
      appoinment_ended = True

def displayAppointment(all_patientID,all_name,all_vaccine_name,all_health_center,all_appoinment_date_time,all_fee):
    print('=================================================')
    print('Invoice for <',all_patientID,'>')
    print('Date:',all_appoinment_date_time)
    print('-------------------------------------------------')
    print('Patient DETAILS')
    print('Name:',all_name)
    print('Health center:',all_health_center)
    print('Vaccine name:',all_vaccine_name)
    print('-------------------------------------------------')
    print('PURCHASE DETAILS')
    print('Total amount paid: $',all_fee)
    print('=================================================')



welcomeMessage()
getBatchData()
welcomeMessage2()
displayVaccines(vaccine_Name_noOf_vial,schedules)
getAppointment()


