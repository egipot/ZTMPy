is_magician = True
is_expert = False

#check if magician and expert : if true print "you are a master magician"
#check if magician but not an expert : if true print "at least you're getting there"
# if you're not a magician: "you need magic powers"

#egi solution /*
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician==True and is_expert==False:
    print("at least you're getting there")
elif is_magician==False:
    print("you need magic powers")
# */

#andrei's solution /*
if is_expert and is_magician:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("you need magic powers") 
# */ WAAAAAY COOLER!