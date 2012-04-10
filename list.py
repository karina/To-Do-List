import sys
class Event(object):

	def __init__(self,name):
		self.completed = False
		self.name = name
		self.details = ""
		all_list.append(self)


def change_status(name):
	for names in all_list:
		print names.name
		if name == names.name:
			print names.name
			names.completed = True
			print "Good Job, you have finished a task!"

def delete_item(name):
	for names in all_list:
		if name == names.name:
			all_list.remove(names)
			print "Removed"
			
def add_details(name, details):
	for names in all_list:
		if name == names.name:
			names.details = details
			return "Details added"
	else:
		return "Event not found"

def print_all():
	for names in all_list:
		print names.name
		print "\t Status: %s" % names.completed
		print "\t Details: %s " % names.details

#def write_all(file_name):

all_list = []

while True:
	print "Would you like to add, delete, mark complete, or edit details of an event. (Enter to exit)",
	event = raw_input("---->")
	if event == '':
		break

	print "What is the name of the event",
	name = raw_input("---->")

	if 'add' ==  event:
		new_event = Event(name)
	elif 'delete' == event:
		delete_item(name)
	elif 'edit' == event:
		print "What are the details you wish to add",
		details = raw_input("---->")
		print add_details(name, details)
	elif 'complete' == event:
		change_status(name)
	else:
		break

print_all()
f = open(sys.argv[1],'w')
f.write('hello')
