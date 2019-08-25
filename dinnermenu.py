#Menu Generator
main_courses=["mac & cheese","lasagna","chicken burger",
"dumplings","pasta","tacos","chicken and rice"]
side_dishes=["french fries","creamed corn","fruit salad",
"mashed potatoes","garlic bread","apple sauce"]
desserts=["ice cream","brownies","apple pie","cheesecake",
"banana pudding","tiramisu cake","frozen yogurt"]
from random import *
number_main=randint(0,len(main_courses)-1)
number_side=randint(0,len(side_dishes)-1)
number_dessert=randint(0,len(desserts)-1)
print("Good evening! For dinner you will be having " + main_courses[number_main]+
" as your main dish with a side of " + side_dishes[number_side]+
", and your dessert will be " + desserts[number_dessert] + "!")
