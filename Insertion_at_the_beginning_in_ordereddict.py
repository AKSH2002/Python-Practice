from collections import OrderedDict

iniordered_dict = OrderedDict([('aksh', '1'), ('nikhil', '2')])

iniordered_dict.update({'raju': '3'})
iniordered_dict.move_to_end('raju', last=False)

print("Resultant Dictionary : "+str(iniordered_dict))
