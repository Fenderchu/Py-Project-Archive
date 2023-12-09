
aligne = lambda a, b: a-len(b)


### initialising the order class
class order:
    def __init__(self, num):
        self.items = []
        ### Item format [size/name, cost, item number, quantity]
        self.total = 0
        self.order_num = num
        self.item_num = 1
    
    def print_order(self):
        print("")
        for item in self.items:
            print(str(item[2]) + ": " + item[0] + " x" + str(item[3]) + " "*aligne(15, (item[0]+" x"+str(item[3]))) + "$"+ str(item[1]))
        print("\n total: $" + str(self.total))

    def add_item(self, item):
        
        new_entry = True

        for i in self.items:
            if i[0] == item[0]:
                item[3]+=1
                ###shenanigans
                i[1] = str(float(i[1]) + float(item[1]))
                new_entry = False
        
        if new_entry:
            item.append(1)
            ###set quantity to 1
            item[2] += self.item_num
            ### give item unique item number
            self.item_num += 1

            self.items.append(item)
        
        self.add_total()
    
    def remove_item(self, item_id = None):


        valid = False

        for item in self.items:
            if item[2] == int(item_id):
                if item[3] == 1:
                    self.total -= float(item[1])
                    valid = True
                    self.items.remove(item)
                else:
                    item[1] = (float(item[1])/item[3])*(item[3]-1)
                    ### cost = (cost/quantity) * (quantity - 1)

                    item[3] -= 1
        
        if not valid:
            raise Exception("No item id given/invalid id")
    
    def add_total(self):
        self.total = 0
        for item in self.items:
            self.total += float(item[1])




menus = {
    "Sandwitches":[["burger", "6.25", 0], ["chicken", "5.25", 0], ["veggie", "5.75", 0]],
    "Drinks":[["small drink", "1.00", 0], ["medium drink", "2.25", 0], ["large drink", "2.75", 0]],
    "Fries":[["small fry", "1.00", 0], ["medium fry", "1.75", 0], ["large fry", "2.25", 0]]
}

order_list = []


def main():
    
    run = True

    order_num = 0

    while run:
        sub_run = True
        order_list.append(order(order_num))
        
        while sub_run:
            print_menu("Sandwitches")
            choice_get("Sandwitches", order_num)

            if input("Would you like more sandwitches? (y/n)>>>") != "y":
                sub_run = False
        

        if input("Would you like a drink? (y/n)>>>") == "y":
            sub_run = True
            while sub_run:
                print_menu("Drinks")
                choice_get("Drinks", order_num)

                if input("Would you like more drinks? (y/n)>>>") != "y":
                    sub_run = False

        
        if input("Would you ike fries? (y/n)>>>") == "y":
            sub_run = True
            while sub_run:
                print_menu("Fries")
                if choice_get("Fries", order_num) == "small fry":
                    if input("would you like to supersize that? (y/n)>>>") == "y":
                            order_list[order_num].remove_item(order_list[order_num].items[-1][2])
                            order_list[order_num].add_item(menus["Fries"][2])

                if input("Would you like more fries? (y/n)>>>") != "y":
                    sub_run = False
        
        if input("Do you want Ketchup? (y/n)>>>") == "y":
            ketchup_text = input("How many Ketchups would you like?>>>")
        
            if  ketchup_text.isnumeric():
                order_list[order_num].add_item(["Ketchup", 0.25*int(ketchup_text), 0, ketchup_text])

        order_list[order_num].print_order()

        while input("Dose your order look corect? (y/n)>>>") != "y":
            valid = False
            while not valid:
                item_num = input("what item would you like to change (item number)>>>")
                if item_num.isnumeric() and int(item_num) <= len(order_list[order_num].items):
                    order_list[order_num].remove_item(item_num)
                    valid = True
                    print("Item removed")
                else:
                    print("incorrect number given \n")
                order_list[order_num].print_order()
        
        if input("start new order? (y/n)>>> ") == "y":
            pass
        else:
            run = False


def print_menu(foodtype):


    print("\n"+" "*aligne(10,"foodtype")+foodtype)

    for food in menus[foodtype]:
        print(food[0]+" "*aligne(15,food[0]) +"$"+food[1])

    print("")




def choice_get(foodtype, order_num):

    valid = False

    while not valid:
        
        choice = input("What would you like? (first 3 letters)>>>")
        for item in menus[foodtype]:
            if choice in item[0]:
                order_list[order_num].add_item(item)
                choice = item[0]
                valid = True

    print("You chose "+choice+"\n")
    
    print("total: $" + str(order_list[order_num].total) + "\n")


    return choice




main()