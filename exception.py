try:
    print('I will try this code and will throw exceptino if there is any problem')
except Exception as e:
    print("I will run only if try block fails")
else:
    print('I will run only if there is no exception . sue this to run code whihc should only execute if there is no excpetion')
finally:
    print("this will be printed in every case")