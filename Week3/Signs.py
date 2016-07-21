# attr: projected lifetime, color, surface area, shape, message
# methods: standing, giving messages

class Signs():
    def __init__(self, projected_lifetime, color, surface_area, shape, message):
        self.projected_lifetime = projected_lifetime
        self.color = color
        self.surface_area = surface_area
        self.shape = shape
        self.message = message

    # Methods 
    def standing():
        print("I'm standing")
    def giving_message():
        print(self.message)

stop_sign = Signs(10, "red", 225, "diamond", "STOP")
stop_sign.giving_message()