try:
    print('10'+10)
except IOError:
    print('You have an input/output error')
except TypeError:
    print(f"You are using the wrong data type")
except:
    print('Error on data processing')
finally:
    print("Finally will run independently of the occurs of errors")
# else:
#     print("Else block here, runs if everything runs without error")