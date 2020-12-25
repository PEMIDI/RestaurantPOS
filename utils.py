from menu import Item
from order import Order
from finance import Bill, Payment


# DONE-4: Add create_time() function which get proper data from user,
#       create Item instance and return
# DONE-4: Add get_order() function which will:
#       get item data from user, create Order intance and return
#       Call show_menu() method of Item class on the top of each order,
#       User can select any item, anytime
#       It's up to you (developer) how to store items(by id, uuid, instance)

def create_item():
    Item.prompt()


def get_order():
    ordering = True
    item_dic = {}
    in_out = ''
    while ordering:
        Item.show_menu()
        print('type exit to exit\n')
        meal_choice = input('select a food to add to your order')
        for item in Item.item_list:
            if item.id == meal_choice:
                item_dic.update(item)
        in_out = input('where you prefer eat the meal? press I for inside,'
                       ' O for outside')
        ordering = False
    Order(in_out=in_out, item_dict=item_dic)
    print(Order.order_list)


def show_unpaid_bill():
    for item in Bill.show_unpaid():
        print(f"{item.id} : {item}")


def pay_bill():
    bill_choice = input('select a bill to pay | enter id number')
    for item in Bill.bill_list:
        if item.id == bill_choice:
            item.payment.is_paid = True
            print(f"bill with id : {item.id} paid")
        else:
            print('you entered wrong')


def get_finance_report():
    print(f"aggregation all paid bills: {Payment.paid_list()}")
    print('last 10 paid bills:\n')
    for item in Bill.show_paid():
        print(f"id : {item.id} : {item}")

# DONE-4: Add show_unpaid_bill() function which will render a list to console
# DONE-4: Add pay_bill() function which just get a bill identifier
#       (id, uuid or ...) and set all related payment flags to True
# DONE-4: Add get_finance_report() method which will show last 10 paid
#       Payments and aggregation of all paid payments as integer (Hint: use
#       paid_list() method of Payment class)
