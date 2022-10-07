import random


def random_famous(famous, count=2):
    """
    Недетерминированная функция
    :param famous: список людей
    :param count: количество
    :return: случайных людей
    """
    return random.sample(famous, count)

# print(random_famous([10,15,16,17,102,105,205,222,777]))