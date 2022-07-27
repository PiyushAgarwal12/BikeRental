from datetime import datetime

class shop():
    global stock
    stock = {}
    
    def inventory(self):
        num = int(input("Enter the number of enteries in inventory "))
        for i in range(1,num+1):
            item = input('Enter ' + str(i) + 'th item -')
            if(item in stock):
                stock[item] = stock[item]+1
            else:
                stock[item] = 1
    
    def show_inventory(self):
        print('Below are our available bikes')
        for item in stock:
            print(item, stock[item])

class customers(shop):
    def __init__(self, name):
        print('Welcome to Bike Rentals')
        self.name = name
        self.total_price = 0
    
    def choose_model(self):
        print('Please chose the model you like.')
        self.show_inventory()
        while(1):
            self.model_name = input()
            if ((self.model_name not in stock) or (stock[self.model_name] <= 0)):
                print('Stock is unavailable. Re-enter model name.')
            else:
                stock[self.model_name] = stock[self.model_name] -1
                break;
        
    def kindOfBooking(self):
        print('Enter kind of booking - \n 1.Hourly (Rs50) \n 2.Daily(Rs500) \n 3.Weekly(Rs2500) ')
        while(True):
            self.kind = input()
            if(self.kind == '1'):
                self.price = 50
                break;
            elif(self.kind == '2'):
                self.price = 500
                break;
            elif(self.kind == '3'):
                self.price = 2500
                break;
            else:
                print('INVALID. ENTER AGAIN.')
        self.start = datetime.now()

    def generate_bill(self):
        self.endtime = datetime.now()
        temp = 0
        if(self.kind == '1'):
            duration_in_s = (self.endtime - self.start).total_seconds()
            temp = max(1, divmod(duration_in_s, 3600)[0])
        elif (self.kind == '2'):
            duration_in_s = (self.endtime - self.start).total_seconds()
            temp = max(1, divmod(duration_in_s, 86400)[0])
        elif (self.kind == '3'):
            duration_in_s = (self.endtime - self.start).total_seconds()
            temp = max(1, divmod(duration_in_s, 25200)[0])
        else:
            print('INVALID')
            temp = 0
        self.total_price = self.total_price + temp*self.price
        print('Cusomer Name -', self.name)
        print('Total bill - ', self.total_price)
        stock[self.model_name] = stock[self.model_name] + 1 
    
    def transaction(self):
        self.payment = input('Select mode of transaction\n 1.Cash \n 2.Card \n 3.Due\n')
        if (self.payment == '1' or self.payment == '2'):
            self.total_price = 0


print('Create your shop.')
myshop = shop()
myshop.inventory()


while(True):
    inp = input('Enter next value \n 1.New Customer \n 2.Return a bike \n 3.Close shop\n')
    if inp == '1':
        name = input('Enter name of customer: ')
        obj = customers(name)
        obj.choose_model()
        obj.kindOfBooking()
    elif inp == '2':
        obj.generate_bill()
        obj.transaction()
    elif inp == '3':
        print('Shop closed')
        break;
    else:
        print('Please enter a valid number ')        
        





















