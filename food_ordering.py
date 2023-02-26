# Initialize an empty dictionary to store food items
food_items = {}

# Add a new food item to the dictionary
def add_food_item(name, quantity, price, discount, stock):
    food_id = len(food_items) + 1  # Generate a new FoodID
    food_items[food_id] = {'Name': name, 'Quantity': quantity, 'Price': price, 'Discount': discount, 'Stock': stock}
    print('Food item added successfully!')
    print(food_items[food_id])  # Print the details of the added food item

# Edit a food item using its FoodID
def edit_food_item(food_id, name=None, quantity=None, price=None, discount=None, stock=None):
    if food_id in food_items:
        if name:
            food_items[food_id]['Name'] = name
        if quantity:
            food_items[food_id]['Quantity'] = quantity
        if price:
            food_items[food_id]['Price'] = price
        if discount:
            food_items[food_id]['Discount'] = discount
        if stock:
            food_items[food_id]['Stock'] = stock
        print('Food item edited successfully!')
        print(food_items[food_id])  # Print the details of the edited food item
    else:
        print(f'Food item with ID {food_id} not found.')

# View the list of all food items
def view_food_items():
    if not food_items:
        print('No food items found.')
    else:
        for food_id, food_item in food_items.items():
            print(f'FoodID: {food_id}, Name: {food_item["Name"]}, Quantity: {food_item["Quantity"]}, Price: {food_item["Price"]}, Discount: {food_item["Discount"]}, Stock: {food_item["Stock"]}')

# Remove a food item from the menu using FoodID
def remove_food_item(food_id):
    if food_id in food_items:
        del food_items[food_id]
        print(f'Food item with ID {food_id} removed successfully!')
    else:
        print(f'Food item with ID {food_id} not found.')


# Add a new food item
add_food_item('Pizza', '12 inches', 12.99, 0.2, 10)

# Edit an existing food item
edit_food_item(1, quantity='8 pieces', price=8.99)

# View all food items
view_food_items()

# Remove a food item
remove_food_item(1)




# Initialize an empty dictionary to store users
users = {}

# Initialize an empty list to store orders
orders = []

# Register a new user
def register_user(full_name, phone_number, email, address, password):
    user_id = len(users) + 1  # Generate a new UserID
    users[user_id] = {'Full Name': full_name, 'Phone Number': phone_number, 'Email': email, 'Address': address, 'Password': password}
    print('User registered successfully!')
    print(users[user_id])  # Print the details of the registered user

# Log in to the application
def login(email, password):
    for user_id, user in users.items():
        if user['Email'] == email and user['Password'] == password:
            print(f'Welcome {user["Full Name"]}!')
            return user_id
    print('Invalid email or password.')
    return None

# Place a new order
def place_order(user_id, food_items):
    if not food_items:
        print('Please select at least one food item.')
        return
    total_price = 0
    order_items = []
    for food_item in food_items:
        if food_item == 1:
            name = 'Tandoori Chicken'
            quantity = '4 pieces'
            price = 240
        elif food_item == 2:
            name = 'Vegan Burger'
            quantity = '1 piece'
            price = 320
        elif food_item == 3:
            name = 'Truffle Cake'
            quantity = '500gm'
            price = 900
        else:
            print(f'Invalid food item {food_item}.')
            return
        total_price += price
        order_items.append({'Name': name, 'Quantity': quantity, 'Price': price})
    orders.append({'User ID': user_id, 'Order Items': order_items, 'Total Price': total_price})
    print('Order placed successfully!')
    print(order_items)
    print(f'Total price: {total_price}')

# View order history of a user
def view_order_history(user_id):
    user_orders = []
    for order in orders:
        if order['User ID'] == user_id:
            user_orders.append(order)
    if not user_orders:
        print('No orders found.')
    else:
        for user_order in user_orders:
            print(user_order)

# Update user profile
def update_user_profile(user_id, full_name=None, phone_number=None, email=None, address=None, password=None):
    if user_id in users:
        if full_name:
            users[user_id]['Full Name'] = full_name
        if phone_number:
            users[user_id]['Phone Number'] = phone_number
        if email:
            users[user_id]['Email'] = email
        if address:
            users[user_id]['Address'] = address
        if password:
            users[user_id]['Password'] = password
        print('User profile updated successfully!')
        print(users[user_id])  # Print the details of the updated user
    else:
        print(f'User with ID {user_id} not found.')


# Register a new user
register_user('John Doe', '9876543210', 'johndoe@example.com', '123 Main St, Anytown, USA', 'password123')

# Log in to the application
user_id = login('johndoe@example.com', 'password123')

# Place a new order
place_order(user_id, [2, 3])

# View order history
