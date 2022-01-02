import pyinputplus as p
cost = 0
pricing = {'wheat':10, 'white':20, 'sourdough':10, 'chicken':10, 'turkey':20, 'ham':30, 'tofu':5, 'cheddar':8, 'swiss':11, 'mozzarella':10, 'mayo':2, 'mustard':2, 'lettuce':1, 'tomato':1}
bread = p.inputMenu(['wheat','white','sourdough'],prompt="WHAT BREAD WOULD YOU LIKE?\n")
protein = p.inputMenu(['chicken','turkey','ham','tofu'],prompt="WHAT KIND OF MEAT WOULD YOU LIKE?\n")
cost = cost + pricing.get(bread) + pricing.get(protein)
wantcheese = p.inputYesNo(prompt="DO YOU WANT CHEESE? yes/no: ")
if wantcheese == 'yes':
    cheese = p.inputMenu(['cheddar','swiss','mozzarella'],prompt="WHICH CHEESE WOULD YOU LIKE?\n")
    cost += pricing.get(cheese)
mayo = p.inputYesNo(prompt="DO YOU WANT MAYO? ")
mustard = p.inputYesNo(prompt="DO YOU WANT MUSTARD? ")
lettuce = p.inputYesNo(prompt="DO YOU WANT LETTUCE? ")
tomato = p.inputYesNo(prompt="DO YOU WANT TOMATO? ")
if mayo == 'yes':
    cost += pricing.get('mayo')
if mustard == 'yes':
    cost += pricing.get('mustard')
if lettuce == 'yes':
    cost += pricing.get('lettuce')
if tomato == 'yes':
    cost += pricing.get('tomato')

num = p.inputInt(min= 0, prompt= "HOW MANY SANDWICHES WOULD YOU LIKE? ")
finalcost = cost * num
print(finalcost)
