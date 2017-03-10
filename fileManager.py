import pickle

FILE = 'data.file'

def save(data, filename):
	with open(filename, 'wb') as output_data:
		pickle.dump(data, output_data, pickle.HIGHEST_PROTOCOL)

def load(filename):
	with open(filename, 'rb') as input_data:
		return pickle.load(input_data)

#def test():
	#global NewCls
	#obj_test = type('NewCls',(object,),{"name": "test", "value":15})
	#NewCls = obj_test
	#save(obj_test, 'test.tst')
	#del obj_test
	#ld_obj = load('test.tst')
	#print ld_obj.name
	#print ld_obj.value

# test()
