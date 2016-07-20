# -*- coding: utf-8 -*-


class Trouble(object):
    def __str__(self):
        return "[Trouble(number:{})]".format(self.number)

    def __init__(self, number):
        self.number = number


class Supporter(object):
    name = None
    next_supporter = None

    def __str__(self):
        return "(%s)%s" % (self.name, self.__name__)

    def __init__(self, name):
        self.name = name

    def set_next_supporter(self, next_supporter):
        self.next_supporter = next_supporter
        return self.next_supporter

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next_supporter is not None:
            self.next_supporter.support(trouble)
        else:
            self.fail(trouble)

    def resolve(self, trouble):
        NotImplementedError("Should Be Implemented")

    def done(self, trouble):
        print(str(trouble) + " is resolved by " + self.__class__.__name__)

    def fail(self, trouble):
        print(str(trouble) + " cannot be resolved")


class NoSupporter(Supporter):
    def __init__(self, name):
        super(NoSupporter, self).__init__(name)

    def resolve(self, trouble):
        # Nothing to support
        return False


class LimitSupporter(Supporter):
    def __init__(self, name, limit):
        super(LimitSupporter, self).__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        if trouble.number < self.limit:
            return True
        else:
            return False

    def done(self, trouble):
        print("DO IT trouble({})!! {}".format(
            trouble.number, self.__class__.__name__))


class OddSupporter(Supporter):
    def __init__(self, name):
        super(OddSupporter, self).__init__(name)

    def resolve(self, trouble):
        if trouble.number % 2 == 1:
            return True
        else:
            return False


class SpecialSupporter(Supporter):
    def __init__(self, name, num):
        super(SpecialSupporter, self).__init__(name)
        self.num = num

    def resolve(self, trouble):
        if trouble.number == self.num:
            return True
        else:
            return False
