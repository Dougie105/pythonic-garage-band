class Band:

    all = []

    def __init__(self, leader, members=[]):
        self.leader = leader
        self.members = members
        self.__class__.all.append(self)

    def __repr__(self):
        return f'The leader {self.leader} and the others {self.members}'

    def __str__(self):
        return f'The band leader is {self.leader}, its members are {self.members}'

    @staticmethod
    def play_solo():
        return f'{members}'

    @classmethod
    def create_from_data(cls, data):

        lines = data.split('\n')

        leader_line = lines[0]

        line_parts = leader_line.split(',')
        member_name = line_parts[0]
        member_position = line_parts[1]

        if member_position == 'Nick Hipa':
            leader = Guitarist(member_name)

        followers = [Bass('Josh Gilbert'), Drummer('Jordan Mancino')]
        return Band(leader, followers)

class Musician:

    # class attribute
    member_list = []

    def __init__(self, name):
        self.name = name
        self.__class__.member_list.append(self)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'Im a {self.__class__.__name__} for the band "As I Lay Dying". My name is {self.name}'

    @classmethod
    def get_Members(cls):
        return cls.member_list

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'Jordan Mancino')

    def do_something(self):
        return 'smash drumset'

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Nick Hipa')

    def do_something(self):
        return 'crowd surf'

class Bass(Musician):
    def __init__(self, name):
        super().__init__(name, 'Josh Gilbert')

    def do_something(self):
        return 'break guitar'