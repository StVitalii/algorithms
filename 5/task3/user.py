#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних двбічнооднозв'язний список з поточним елементом.
"""

def init():
    """ Викликається один раз на початку виконання програми. """
    global catalogue, curr
    catalogue = []
    curr = -1


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return not catalogue


def set_first():
    """ Зробити поточний елемент першим.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global curr
    catalogue.insert(0, catalogue.pop(curr))
    curr = 0


def set_last():
    """ Зробити поточними останній елемент списку

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global curr
    catalogue.append(catalogue.pop(curr))
    curr = len(catalogue) - 1


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    global curr
    c = curr + 1
    if c >= len(catalogue): raise StopIteration
    else: curr = c



def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    global curr
    if curr > 0:
        curr -= 1
    else: raise StopIteration


def current():
    """ Повертає навантаження поточного елементу.

    :return: Навантаження поточного елементу
    """
    return catalogue[curr]


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    global curr
    curr += 1
    catalogue.insert(curr, item)



def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    global curr
    catalogue.insert(curr, item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    """
    del catalogue[curr]
    try:
        catalogue[curr]
    except IndexError:
        try:
            prev()
        except StopIteration: pass

