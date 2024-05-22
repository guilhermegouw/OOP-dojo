class MercedezBenz:
    doors = 2
    wheels = 4
    model = 'G'

    def __init__(self, color):
        self.color = color

    def drive(self):
        return 'I am driving'

    @staticmethod
    def auto_drive():
        return 'Auto-driving for now...'

    @classmethod
    def electric(cls):
        print(f'A lease for {cls} will be created.')
