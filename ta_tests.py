from ToDoListApp import *
import sys


def adding_uncompleted_task():
    site = ToDoListApp()
    site.add_task("/* car fixing */")
    site.close_connection()
    logging.info("Test " + sys._getframe().f_code.co_name + " passed")


def adding_completed_task():
    site = ToDoListApp()
    t1 = """¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿƒΑΒΓΔΕΖΗ"""
    t2 = """ΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψωϑϒϖ•…′″‾⁄℘ℑℜ™ℵ←↑→↓↔↵⇐⇑⇒⇓⇔∀∂∃∅∇∈∉∋∏∑−∗√∝∞∠∧∨∩∪∫∴∼≅≈≠≡≤≥⊂⊃⊄⊆⊇⊕⊗⊥⋅"""
    t3 = """⌈⌉⌊⌋⟨⟩◊♠♣♥♦"&<>ŒœŠšŸˆ˜–—‘’‚“”„†‡‰‹›€"""
    site.add_task(t1+t2+t3, is_added_task_completed=True)
    site.close_connection()
    logging.info("Test " + sys._getframe().f_code.co_name + " passed")


def cancel_adding_task_by_cancel_button():
    site = ToDoListApp()
    site.add_task_with_cancel()
    site.close_connection()
    logging.info("Test " + sys._getframe().f_code.co_name + " passed")


def cancel_adding_task_by_closing_form():
    site = ToDoListApp()
    site.add_task_with_close_form("check email")
    site.close_connection()
    logging.info("Test " + sys._getframe().f_code.co_name + " passed")


def adding_task_with_empty_title():
    site = ToDoListApp()
    site.add_task("")
    site.close_connection()
    logging.info("Test " + sys._getframe().f_code.co_name + " passed")


if __name__ == "__main__":
    adding_uncompleted_task()
    adding_completed_task()
    cancel_adding_task_by_cancel_button()
    cancel_adding_task_by_closing_form()
    adding_task_with_empty_title()
