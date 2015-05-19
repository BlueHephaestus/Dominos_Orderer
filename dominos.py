
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import sys, time
driver = webdriver.Firefox()
driver.get("https://order.dominos.com/en/pages/order/#/locations/search/")

fname = raw_input("First Name: ")
lname = raw_input("Last Name: ")
email = raw_input("Email: ")
phone = raw_input("Phone #: ")

web_pipeline = raw_input("Is this for Website Pipeline(Y/N)?: ")
if web_pipeline.lower() == 'y':
	addr_type = 'business'
	loc_name = 'Website Pipeline'
	addr_street = '555 N. Pleasantburg Drive'
	suite_apt = '214'
	city = 'Greenville'
	state = 'SC'
	zip = '29607'
else:	
	addr_type = raw_input("Address Type(House, Apartment, Business): ")

	if addr_type.lower() == "house":
		pass
	elif addr_type.lower() =="apartment":
		loc_name = raw_input("Apartment Name: ").title()
		#append "*" to suite_apt value 
	elif addr_type.lower() == "business":
		loc_name = raw_input("Business Name: ").title()
	#else: cover more options here?
	addr_street = raw_input("Street Address: ")
	#leave blank if unknown or irrelevant
	suite_apt = raw_input('Suite/Apt #: ')
	city = raw_input("City(i.e. Greenville: ")
	state = raw_input("State(i.e. SC): ")
	state = state.upper()
	if state == '':
		state = 'SC'
	zip = raw_input("Zip: ")
order_type = raw_input("Delivery/Carryout: ")
#use_coupons = True
#TODO: Coupon adding system
#set preset, read preset
#with open("log.txt", "w") as log:
	


if order_type.lower() == 'delivery':
	#varies according to house/apartment/business
	driver.find_element_by_xpath("//label[@class='form__input--icon Delivery']").click()
	Select(driver.find_element_by_id("Address_Type_Select")).select_by_visible_text(addr_type.title())
	#if apartment or business
	if loc_name != '':
		driver.find_element_by_id("Location_Name").send_keys(loc_name)
	#Rest of important info
	driver.find_element_by_id("Street").send_keys(addr_street)
	driver.find_element_by_id("City").send_keys(city.title())
	Select(driver.find_element_by_id("Region")).select_by_visible_text(state)
	driver.find_element_by_id("Postal_Code").send_keys(zip)
	#driver.find_element_by_xpath("//button[@class='btn btn--large js-search-cta']").click()
	driver.find_element_by_css_selector("button.btn").click()
elif order_type.lower() == 'carryout':
	#always these 3 options
	driver.find_element_by_xpath("//label[@class='form__input--icon Carryout']").click()
	driver.find_element_by_id("City").send_keys(city)
	Select(driver.find_element_by_id("Region")).select_by_visible_text(state)
	driver.find_element_by_id("Postal_Code").send_keys(zip)
	driver.find_element_by_css_selector("button.btn").click()
time.sleep(2)#TODO: implicit wait here


def crust_handler():
	print """Choose Crust(Name, Abbreviation, or Number): 
	1. Hand Tossed(Hand)
	2. Handmade Pan(Pan)
	3. Thin Crust(Thin)
	4. Brooklyn Style(Brooklyn)
	5. Gluten Free(Gluten)"""
	###################################
	crust_type = raw_input("Crust Type: ")
	if crust_type.title() == 'Hand' or crust_type.title() == 'Hand Tossed' or crust_type == '1':
		crust_size = raw_input("Crust Size(S, M, L): ")
		crust_type = '1'
		if crust_size.upper() == 'S':
			crust_size = 3
		elif crust_size.upper() == 'M':
			crust_size = 4
		elif crust_size.upper() == 'L':
			crust_size = 5
	elif crust_type.title() == 'Pan' or crust_type.title() == 'Handmade Pan' or crust_type == '2':
		crust_size = raw_input("Crust Size(M): ")
		crust_type = '2'
		if crust_size.upper() == 'M':
			crust_size = 3
	elif crust_type.title() == 'Thin' or crust_type.title() == 'Thin Crust' or crust_type == '3':
		##################################
		crust_size = raw_input("Crust Size(M, L): ")
		crust_size = 'm'
		crust_type = '3'
		if crust_size.upper() == 'M':
			crust_size = 3
		elif crust_size.upper() == 'L':
			crust_size = 4
	elif crust_type.title() == 'Brooklyn' or crust_type.title() == 'Brooklyn Style' or crust_type == '4':
		crust_size = raw_input("Crust Size(L, XL): ")
		crust_type = '4'
		if crust_size.upper() == 'L':
			crust_size = 3
		elif crust_size.upper() == 'XL':
			crust_size = 4
	elif crust_type.title() == 'Gluten' or crust_type.title() == 'Gluten Free' or crust_type == '5':
		crust_size = raw_input("Crust Size(S): ")
		crust_type = '5'
		if crust_size.upper() == 'S':
			crust_size = 3
	else:
		print "Invalid Value for Crust Size, please try again: "
	crust_type = int(crust_type) + 1
	#2-6 depending on column			#3-5 depending on options available
	crust_select_string = "div.product:nth-child(%s) > div:nth-child(%s) > label:nth-child(1) > input:nth-child(1)" % (str(crust_type), str(crust_size))
	driver.find_element_by_css_selector(crust_select_string).click()
	if crust_type == 6:
		driver.find_element_by_css_selector("#glutenFreePizza > button:nth-child(3)").click()	
	go_next()
	#return complete if all values were correct, otherwise loop(outside of this function however)

def cheese_sauce_handler():
####################################
	cheese_sauce_changes = raw_input("Default settings for Cheese/Sauce(Y/N)?: ")
	if cheese_sauce_changes.upper() == 'Y':
		go_next()
		#if len(driver.find_elements_by_css_selector("button.js-closePizzaMessage:nth-child(2)")) > 0:
		driver.find_element_by_css_selector("button.js-closePizzaMessage:nth-child(2)").click()
		
	elif cheese_sauce_changes.upper() == 'N':
		cheese_sauce_changes = True
		cheese = raw_input("Cheese(Y/N)?: ")
		if cheese.upper() == 'Y':
			print """Choose Quantity(Name or Number):
1. Light
2. Normal
3. Extra
4. Double
5. Triple"""
			cheese_quantity = raw_input("Cheese Quantity: ")
			if cheese_quantity.lower() == 'light' or cheese_quantity == '1':
				cheese_quantity = 'Light'
			elif cheese_quantity.lower() == 'normal' or cheese_quantity == '2':
				cheese_quantity = 'Normal'
			elif cheese_quantity.lower() == 'extra' or cheese_quantity == '3':
				cheese_quantity = 'Extra'
			elif cheese_quantity.lower() == 'double' or cheese_quantity == '4':
				cheese_quantity = 'Double'
			elif cheese_quantity.lower() == 'triple' or cheese_quantity == '5':
				cheese_quantity = 'Triple'
			Select(driver.find_element_by_css_selector("div.split:nth-child(1) > select:nth-child(4)")).select_by_visible_text(cheese_quantity)
		elif cheese.upper() == 'N':
			driver.find_element_by_css_selector("#cheeseSauceWrapper > div:nth-child(2) > div:nth-child(2) > label:nth-child(1) > input:nth-child(1)").click()
		sauce = raw_input("Sauce(Y/N)?: ")
		if sauce.upper() == 'Y':
			print """Choose Sauce(Name, Abbreviation, or Number):
1. Tomato Sauce(Tomato)
2. Marinara Sauce(Marinara)
3. BBQ Sauce(BBQ)
4. Garlic Parmesan White Sauce(White)"""
			sauce_type = raw_input("Sauce Type: ")
			if sauce_type.lower() == 'tomato sauce' or sauce_type.lower() == 'tomato' or sauce_type == '1':
				sauce_type = 1
			elif sauce_type.lower() == 'marinara sauce' or sauce_type.lower() == 'marinara' or sauce_type == '2':
				sauce_type = 2
			elif sauce_type.lower() == 'bbq sauce' or sauce_type.lower() == 'bbq' or sauce_type == '3':
				sauce_type = 3
			elif sauce_type.lower() == 'garlic parmesan white sauce' or sauce_type.lower() == 'white' or sauce_type == '4':
				sauce_type = 4
			
			if sauce_type == 3:
				print """Choose Quantity(Name or Number):
1. Light
2. Normal
3. Extra
4. Double
5. Triple"""
			else:
				print """Choose Quantity(Name or Number):
1. Light
2. Normal
3. Extra"""
			sauce_quantity = raw_input("Sauce Quantity: ")
			if sauce_quantity.lower() == 'light' or sauce_quantity == '1':
				sauce_quantity = 'Light'
				sauce_num = 1
			elif sauce_quantity.lower() == 'normal' or sauce_quantity == '2':
				sauce_quantity = 'Normal'
				sauce_num = 2
			elif sauce_quantity.lower() == 'extra' or sauce_quantity == '3':
				sauce_quantity = 'Extra'
				sauce_num = 3
			elif sauce_quantity.lower() == 'double' or sauce_quantity == '4':
				sauce_quantity = 'Double'
				sauce_num = 4
			elif sauce_quantity.lower() == 'triple' or sauce_quantity == '5':
				sauce_quantity = 'Triple'
				sauce_num = 5
			sauce_select_string = "div.toppingSettings:nth-child(3) > div:nth-child(%s) > label:nth-child(1) > input:nth-child(1)" % (sauce_type)
			sauce_quantity_select_string = "div.toppingSettings:nth-child(3) > div:nth-child(%s) > div:nth-child(2) > select:nth-child(2)" % (sauce_type)
			sauce_dropdown_select_string = "div.toppingSettings:nth-child(3) > div:nth-child(%s) > div:nth-child(2) > select:nth-child(2) > option:nth-child(%s)" % (sauce_type, sauce_num)
			#Select(driver.find_element_by_css_selector(sauce_select_string)).select_by_visible_text(sauce_quantity)
			driver.find_element_by_css_selector(sauce_select_string).click()
			driver.find_element_by_css_selector(sauce_quantity_select_string).click()
			driver.find_element_by_css_selector(sauce_dropdown_select_string).click()

		elif sauce.upper() == 'N':
			driver.find_element_by_css_selector(".selectSauce")
			
def go_next():
	driver.find_element_by_css_selector("a.js-next:nth-child(2)").click()	

def meats_handler():
	meats_selected = False
	while meats_selected == False:
		print """Choose Meats(Name or Number):
1. Pepperoni
2. Sausage
3. Sliced Sausage
4. Beef
5. Philly Steak
6. Ham
7. Bacon
8. Salami
9. Chicken"""
		print "Input Meats, leave field blank when done: "
		meats_array = []
		new_meats_array = []
		while True:
			meats_input = raw_input('')
			if meats_input == '':
				break
			meats_array.append(meats_input)
		for meats in meats_array:
			#print meats
			#i couldve used an array here....*regret*
			if meats.title() == 'Pepperoni' or meats == '1':
				meat = 'Pepperoni'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Sausage' or meats == '2':
				meat = 'Sausage'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Sliced' or meats.title() =='Sliced Sausage' or meats == '3':
				meat = 'Sliced Sausage'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Beef' or meats == '4':
				meat = 'Beef'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Philly' or meats == 'Steak' or meats == 'Philly Steak' or meats == '5':
				meat = 'Philly Steak'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Ham' or meats == '6':
				meat = 'Ham'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Bacon' or meats == '7':
				meat = 'Bacon'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Salami' or meats == '8':
				meat = 'Salami'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)").click()
			elif meats.title() == 'Chicken' or meats == '9':
				meat = 'Chicken'
				driver.find_element_by_css_selector("#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > label:nth-child(1) > input:nth-child(1)").click()
			new_meats_array.append(meat)
		meats_selected = True
	###############################
	meat_dist = raw_input("Would you like the Normal Distribution of Meats and Non-Meats(Y/N)?: ")
	
	if meat_dist.upper() == 'Y' or meat_dist.lower() == 'yes':
		#add pizza to order
		pass
	elif meat_dist.upper() == 'N' or meat_dist.lower() == 'no':
		meat_count = 1
		print "Choose Meats to Customize(q = Quantity Change, s = Side Change,\n\t\t\t qs/sq = Both, '' = No Change):"
		#seperate ones for quantity and side? or same?
		for meats in new_meats_array:
			quantity_side_str = raw_input("%s. %s: " %(meat_count, meats))
			if quantity_side_str == '':
				pass
			elif quantity_side_str.lower() == 'q':
				topping_quantity_handler(meats)
			elif quantity_side_str.lower() == 's':
				topping_side_handler(meats)
			elif quantity_side_str.lower() == 'qs' or quantity_side_str.lower() == 'sq':
				topping_quantity_handler(meats)
				topping_side_handler(meats)
			meat_count += 1
		#Customizing meats and non meats
		non_meats_handler()
def non_meats_handler():
	print """Choose Non-Meats(Name, Abbreviation, or Number):
	1. Cheddar 
	2. Feta
	3. Parmesan
	4. Provolone
	5. Banana Peppers(Banana)
	6. Black Olives(Olives)
	7. Green Peppers(Green)
	8. Jalapeno Peppers(Jalapeno)
	9. Mushrooms
	10. Pineapple
	11. Onions
	12. Red Peppers(Red)
	13. Spinach
	14. Diced Tomatoes(Tomatoes)
	15. Hot Sauce"""
	print "Input Non-Meats, leave field blank when done: "
	non_meats_array = []
	new_non_meats_array = []
	while True:
		meats_input = raw_input('')
		if meats_input == '':
			break
		non_meats_array.append(meats_input)
	for nm in non_meats_array:
		topping_select(nm)
		nm = nm.lower()
		if nm == 'cheddar' or nm == '1':
			non_meat_index = 0
		elif nm == 'feta' or nm == '2':
			non_meat_index = 1
		elif nm == 'parmesan' or nm == '3':
			non_meat_index = 2
		elif nm == 'provolone' or nm == '4':
			non_meat_index = 3
		elif nm == 'banana peppers' or nm == 'banana' or nm == '5':
			non_meat_index = 4
		elif nm == 'black olives' or nm == 'olives' or nm == '6':
			non_meat_index = 5
		elif nm == 'green peppers' or nm == 'green' or nm == '7':
			non_meat_index = 6
		elif nm == 'jalapeno peppers' or nm == 'jalapeno' or nm == '8':
			non_meat_index = 7
		elif nm == 'mushrooms' or nm == '9':
			non_meat_index = 8
		elif nm == 'pineapple' or nm == '10':
			non_meat_index = 9
		elif nm == 'onions' or nm == '11':
			non_meat_index = 10
		elif nm == 'red peppers' or nm == 'red' or nm == '12':
			non_meat_index = 11
		elif nm == 'spinach' or nm == '13':
			non_meat_index = 12
		elif nm == 'diced tomatoes' or nm == 'tomatoes' or nm == '14':
			non_meat_index = 13
		elif nm == 'hot sauce' or nm == '15':
			non_meat_index = 14
		non_meats_ref = ['Cheddar', 'Feta', 'Parmesan', 'Provolone', 'Banana Peppers', 'Black Olives', 'Green Peppers', 'Jalapeno Peppers', 'Mushrooms', 'Pineapple', 'Onions', 'Red Peppers', 'Spinach', 'Diced Tomatoes', 'Hot Sauce']
		new_non_meats_array.append(non_meats_ref[non_meat_index])
	if len(new_non_meats_array) == 0:
		return
	non_meat_count = 1
	print "Choose Non-Meats to Customize(q = Quantity Change, s = Side Change,\n\t\t\t     qs/sq = Both, '' = No Change):"
	#seperate ones for quantity and side? or same?
	for non_meats in new_non_meats_array:
		quantity_side_str = raw_input("%s. %s: " %(non_meat_count, non_meats))
		if quantity_side_str == '':
			pass
		elif quantity_side_str.lower() == 'q':
			topping_quantity_handler(non_meats)
		elif quantity_side_str.lower() == 's':
			topping_side_handler(non_meats)
		elif quantity_side_str.lower() == 'qs' or quantity_side_str.lower() == 'sq':
			topping_quantity_handler(non_meats)
			topping_side_handler(non_meats)
		non_meat_count += 1

def select_dropdown_option(dropdown, dropdown_option):
	Select(driver.find_element_by_css_selector(dropdown)).select_by_visible_text(dropdown_option)
	
def select_side(side):
	driver.find_element_by_css_selector(side).click()
	
def topping_select(non_meat):
	non_meats_array_L1 = ['1cheddar', '2feta', '3parmesan', '4provolone', '5banana peppers', '6black olives', '7green peppers']
	non_meats_array_L2 = ['8jalapeno peppers', '9mushrooms', '10pineapple', '11onions', '12red peppers', '13spinach', '14diced tomatoes', '15hot sauce']
	for nm in range(len(non_meats_array_L1)):
		if non_meats_array_L1[nm].find(non_meat) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > label:nth-child(1) > input:nth-child(1)" % (nm + 1)
			return driver.find_element_by_css_selector(select_str).click()
			
	for nm in range(len(non_meats_array_L2)):
		if non_meats_array_L2[nm].find(non_meat) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(%s) > label:nth-child(1) > input:nth-child(1)" % (nm + 1)
			return driver.find_element_by_css_selector(select_str).click()
			
def topping_quantity_handler(topping):		
	print "Select Quantity of %s: " % topping
	print """\t1. Light
\t2. Normal
\t3. Extra
\t4. Double
\t5. Triple"""
	quantity = raw_input("%s Quantity(Name or Number): " % (topping))
	quantity_array = ['1light', '2normal', '3extra', '4double', '5triple']
	for q in range(len(quantity_array)):
		if quantity_array[q].find(quantity.lower()) >= 0:
			if q == 0:
				dropdown_option = 'Light'
			elif q == 1:
				dropdown_option = 'Normal'
			elif q == 2:
				dropdown_option = 'Extra'
			elif q == 3:
				dropdown_option = 'Double'
			elif q == 4:
				dropdown_option = 'Triple'
			
	quantity_array_L1 = ['pepperoni', 'sausage', 'sliced sausage', 'beef', 'philly steak', 'ham', 'bacon']
	quantity_array_L2 = ['salami', 'chicken']
	quantity_array_R1 = ['cheddar', 'feta', 'parmesan asiago', 'provolone cheese', 'banana peppers', 'black olives', 'green peppers']
	quantity_array_R2 = ['jalapeno peppers', 'mushrooms', 'pineapple', 'onions', 'red peppers', 'spinach', 'tomatoes', 'hot sauce']
	#add element_found = True/false to avoid over-iteration?
	for t in range(len(quantity_array_L1)):
		if quantity_array_L1[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > select:nth-child(4)" % (t + 1)
			select_dropdown_option(select_str, dropdown_option)
			break
	for t in range(len(quantity_array_L2)):
		if quantity_array_L2[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > select:nth-child(4)" % (t + 1)
			select_dropdown_option(select_str, dropdown_option)
			break
	for t in range(len(quantity_array_R1)):
		if quantity_array_R1[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > select:nth-child(4)" % (t + 1)
			select_dropdown_option(select_str, dropdown_option)
			break
	for t in range(len(quantity_array_R2)):
		if quantity_array_R2[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > select:nth-child(4)" % (t + 1)
			select_dropdown_option(select_str, dropdown_option)	
			break
			
def topping_side_handler(topping):
	side = raw_input("Which side would you like your %s on(L,R)?: " % (topping))
	if side.lower() == 'l':
		side = '1'
	elif side.lower() == 'r':
		side = '3'
	side_array_L1 = ['pepperoni', 'sausage', 'sliced sausage', 'beef', 'philly steak', 'ham', 'bacon']
	side_array_L2 = ['salami', 'chicken']
	side_array_R1 = ['cheddar', 'feta', 'parmesan asiago', 'provolone cheese', 'banana peppers', 'black olives', 'green peppers']
	side_array_R2 = ['jalapeno peppers', 'mushrooms', 'pineapple', 'onions', 'red peppers', 'spinach', 'tomatoes', 'hot sauce']
	for t in range(len(side_array_L1)):
		if side_array_L1[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > label:nth-child(%s)" % (t + 1, side)
			select_side(select_str)
			break
	for t in range(len(side_array_L2)):
		if side_array_L2[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > label:nth-child(%s)" % (t + 1, side)
			select_side(select_str)
			break
	for t in range(len(side_array_R1)):
		if side_array_R1[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > label:nth-child(%s)" % (t + 1, side)
			select_side(select_str)
			break
	for t in range(len(side_array_R2)):
		if side_array_R2[t].find(topping.lower()) >= 0:
			select_str = "#toppingsWrapper > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(%s) > div:nth-child(2) > div:nth-child(1) > label:nth-child(%s)" % (t + 1, side)
			select_side(select_str)	
			break
def is_order_complete():
	order_complete = raw_input("Add more pizza?(Y/N): ")
	if order_complete.lower() == 'n':
		checkout()
	elif order_complete.lower() == 'y':
		build_pizza()
def add_to_order():
	driver.find_element_by_css_selector("button.btn--block").click()
def checkout():
	driver.find_element_by_css_selector("a.btn--large").click()
	driver.find_element_by_css_selector(".js-nothanks").click()

	driver.get("https://order.dominos.com/en/pages/order/#/checkout/")
	time.sleep(2)
	driver.find_element_by_css_selector("a.btn--large:nth-child(2)").click()
	spec_instr = raw_input("Special Driver Instructions: ")
	driver.find_element_by_css_selector("#Delivery_Instructions").send_keys(spec_instr)
	
	css("#First_Name").send_keys(fname)
	css("#Last_Name").send_keys(lname)
	css("#Email").send_keys(email)
	css("#Callback_Phone").send_keys(phone)
	driver.find_element_by_css_selector("#Email_Opt_In").click()
	cash_credit = raw_input("Cash/Credit: ")
	if cash_credit.lower() == 'cash':
		driver.find_element_by_css_selector(".js-paymentCash > label:nth-child(1) > input:nth-child(1)").click()
	else:
		#driver.find_element_by_css_selector(".js-remainingBalanceAmount").text()
		#if driver.find_element_by_css_selector(".js-remainingBalanceAmount").text() > 50:
		print """Apologies, but you must use credit for purchases greater than $50.
For security purposes, please input your values into the respective fields, 
please press enter when complete. """
		driver.find_element_by_css_selector(".js-paymentCreditCard > label:nth-child(1) > input:nth-child(1)").click()
	
		raw_input('')

	if raw_input("Press enter to confirm.") == '':
		css("button.btn").click()
def css(element):
	return driver.find_element_by_css_selector(element)
'''def credit_handler()
	print "None of these values will be stored, and you can manually input them into the page if you would prefer."
	card = raw_input("Credit Card Number: ")
	exp_date_month = raw_input("Expiration Month: ")
	exp_date_'''
def build_pizza():
	driver.find_element_by_css_selector(".navigation-BuildYourOwn").click()
	pizza_quantity = raw_input("Pizza Quantity: ")
	Select(driver.find_element_by_css_selector(".quantity")).select_by_visible_text(pizza_quantity)
	crust_handler()
	cheese_sauce_handler()
	meats_handler()
	add_to_order()
	is_order_complete()

build_pizza()
#checkout()
#driver.find_element_by_css_selector("").click()


assert "No results found." not in driver.page_source
#driver.close()