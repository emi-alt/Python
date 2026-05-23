class Myclass:
    __priv_var = 27

    def __privfunc(self):
        print("This is a private method. It can not be accessed een with an object.")

    def hello(self):
        print("This is a regular public function. print private variable: ", Myclass.__priv_var)

obj = Myclass()
obj.hello()
obj.__priv_var
obj.__privfunc()