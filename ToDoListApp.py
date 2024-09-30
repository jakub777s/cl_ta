from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
import logging


class ToDoListApp():

    def __init__(self):
        self.gecko_path = "/snap/bin/geckodriver"
        self.web_address = "https://wc-react-todo-app.netlify.app/"
        self.loading_timeout = 10
        self.driver = self.__create_connection()
        self.driver.get(self.web_address)
        self.task_wrapper_xpath = """//div[@class="app_content__wrapper__Mm7EF"]"""
        self.single_task_root_xpath = """//div[@class="todoItem_item__fnR7B"]"""
        self.single_task_rest_of_xpath = "/div[1]/div[2]/p[1]"
        self.single_task_time_rest_of_xpath = "/div[1]/div[2]/p[2]"
        self.task_status_icon_rest_of_xpath = "/div[1]/div[1]"
        self.task_status_icon_css_selector = "div.todoItem_item__fnR7B"
        self.task_status_icon_rest_of_css_selector = ("div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > "
                                                      "path:nth-child(1)")
        self.add_task_button_xpath = """//button[@class='button_button__zbfSX button_button--primary__09xDJ']"""
        self.task_title_input_xpath = """//*[@id="title"]"""
        self.add_task_eventual_button_xpath = """//div[@class='modal_buttonContainer__r9NWb']/button[1]"""
        self.cancel_add_task_button_xpath = """//div[@class='modal_buttonContainer__r9NWb']/button[2]"""
        self.close_button_add_task_form_xpath = """//div[@class='modal_closeButton__Fg7AM']"""
        self.add_task_status_xpath = """//div[@role='status' and @class='go3958317564']"""
        self.task_type_xpath = """//*[@id="type"]"""
        self.current_number_of_tasks = self.__get_number_of_tasks()
        self.completed_option_in_type_task_menu = 1
        self.time_of_adding_task = str()
        self.is_added_task_completed = False
        logging.basicConfig(level=logging.INFO)

    def __create_connection(self):
        driver = Firefox(service=Service(executable_path=self.gecko_path))
        if driver.service.is_connectable() is not True:
            raise ConnectionError("Connection with browser was not established")
        return driver

    def close_connection(self):
        self.driver.close()

    def __check_if_element_is_loaded(self, element_name, type='XPATH'):
        if type == "XPATH":
            element = expected_conditions.presence_of_element_located((By.XPATH, element_name))
        elif type == "CSS_SELECTOR":
            element = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element_name))
        else:
            raise Exception("Selected type", type, "is not yet implemented in test code.")
        try:
            WebDriverWait(self.driver, self.loading_timeout).until(element)
        except TimeoutException:
            raise TimeoutError("Timed out waiting for page to load. There is no element with xpath", element_name,
                               " at the page ", self.driver.current_url)

    def __get_number_of_tasks(self):
        return len(self.driver.find_elements(By.XPATH, self.single_task_root_xpath))

    def __get_task_title_from_page(self):
        task_xpath = (self.task_wrapper_xpath + "/div[" + str(self.current_number_of_tasks) + "]"
                      + self.single_task_rest_of_xpath)
        self.__check_if_element_is_loaded(task_xpath)
        return self.driver.find_element(By.XPATH, task_xpath).text

    def __get_task_time_from_page(self):
        task_xpath = (self.task_wrapper_xpath + "/div[" + str(self.current_number_of_tasks) + "]"
                      + self.single_task_time_rest_of_xpath)
        self.__check_if_element_is_loaded(task_xpath)
        return self.driver.find_element(By.XPATH, task_xpath).text

    def __check_task_actions(self):
        task_action_delete_xpath = (self.task_wrapper_xpath + "/div[" + str(self.current_number_of_tasks) + "]"
                                    + "/div[2]/div[1]")
        task_action_update_xpath = (self.task_wrapper_xpath + "/div[" + str(self.current_number_of_tasks) + "]"
                                    + "/div[2]/div[2]")
        self.__check_if_element_is_loaded(task_action_delete_xpath)
        self.__check_if_element_is_loaded(task_action_update_xpath)

    def __complete_add_task_form(self, title, is_added_task_completed):
        self.__check_if_element_is_loaded(self.add_task_button_xpath)
        self.driver.find_element(By.XPATH, self.add_task_button_xpath).click()
        self.__check_if_element_is_loaded(self.task_title_input_xpath)
        title_input = self.driver.find_element(By.XPATH, self.task_title_input_xpath)
        title_input.send_keys(title)
        self.__check_if_element_is_loaded(self.task_type_xpath)
        if is_added_task_completed:
            (Select(self.driver.find_element(By.XPATH, self.task_type_xpath)).
             select_by_index(self.completed_option_in_type_task_menu))
            self.is_added_task_completed = True
        self.time_of_adding_task = datetime.now().strftime("%-I:%M %p, %m/%d/%Y")

    def add_task(self, title='', is_added_task_completed=False):
        self.__complete_add_task_form(title, is_added_task_completed)
        self.__check_if_element_is_loaded(self.add_task_eventual_button_xpath)
        self.driver.find_element(By.XPATH, self.add_task_eventual_button_xpath).click()
        self.__check_if_element_is_loaded(self.add_task_status_xpath)
        task_status = self.driver.find_element(By.XPATH, self.add_task_status_xpath).text
        if title:
            expected_status_of_task = "Task added successfully"
            self.current_number_of_tasks += 1
            self.__check_add_task_title(title)
            self.__check_add_task_time()
            self.__check_task_actions()
            self.__check_task_status()
        else:
            expected_status_of_task = "Please enter a title"
            self.__check_if_no_new_task_has_been_added()
        if task_status != expected_status_of_task:
            raise Exception("Task status notification", task_status, "is not equal to", expected_status_of_task)

    def add_task_with_cancel(self, title='', is_added_task_completed=False):
        self.__complete_add_task_form(title, is_added_task_completed)
        self.__check_if_element_is_loaded(self.cancel_add_task_button_xpath)
        self.driver.find_element(By.XPATH, self.cancel_add_task_button_xpath).click()
        self.__check_if_no_new_task_has_been_added()

    def add_task_with_close_form(self, title='', is_added_task_completed=False):
        self.__complete_add_task_form(title, is_added_task_completed)
        self.__check_if_element_is_loaded(self.close_button_add_task_form_xpath)
        self.driver.find_element(By.XPATH, self.close_button_add_task_form_xpath).click()
        self.__check_if_no_new_task_has_been_added()

    def __check_if_no_new_task_has_been_added(self):
        number_of_tasks = self.__get_number_of_tasks()
        expected_number_of_tasks = self.current_number_of_tasks
        if number_of_tasks != expected_number_of_tasks:
            raise Exception("New task was added to the list incorrectly")

    def __check_add_task_title(self, expected_title):
        task_title = self.__get_task_title_from_page()
        if task_title != expected_title:
            raise Exception("Incorrect title of added task: ", task_title, "Expected title is", expected_title)

    def __check_add_task_time(self):
        task_time = self.__get_task_time_from_page()
        expected_task_time = self.time_of_adding_task
        if task_time != expected_task_time:
            raise Exception("Incorrect time of added task. ", task_time, "is not equal to", expected_task_time)

    def __check_task_status(self):
        task_xpath = (self.task_wrapper_xpath + "/div[" + str(self.current_number_of_tasks) + "]"
                      + self.single_task_rest_of_xpath)
        self.__check_if_element_is_loaded(task_xpath)
        is_element_visible_as_strike = (self.driver.find_element(By.XPATH, task_xpath).
                                        value_of_css_property('text-decoration-line'))
        task_status_icon_xpath = (self.task_wrapper_xpath + "/div[" + str(self.current_number_of_tasks) + "]"
                                  + self.task_status_icon_rest_of_xpath)
        self.__check_if_element_is_loaded(task_status_icon_xpath)
        task_status_icon_color = (self.driver.find_element(By.XPATH, task_status_icon_xpath).
                                  value_of_css_property('background-color'))
        task_status_icon_css_selector = (self.task_status_icon_css_selector + ":nth-child("
                                         + str(self.current_number_of_tasks) + ") > "
                                         + self.task_status_icon_rest_of_css_selector)
        self.__check_if_element_is_loaded(task_status_icon_css_selector, "CSS_SELECTOR")
        svg_path_element = (self.driver.find_element(By.CSS_SELECTOR, task_status_icon_css_selector).
                            get_attribute('outerHTML'))
        if self.is_added_task_completed:
            task_name_expected_format_property = "line-through"
            task_status_expected_icon_color = "rgb(100, 111, 240)"
            task_svg_path_expected_opacity = "opacity=\"1\""
            task_svg_path_expected_stroke_dasharray = "stroke-dasharray=\"1px 1px\""
        else:
            task_name_expected_format_property = "none"
            task_status_expected_icon_color = "rgb(222, 223, 225)"
            task_svg_path_expected_opacity = "opacity=\"0\""
            task_svg_path_expected_stroke_dasharray = "stroke-dasharray=\"0px 1px\""
        if is_element_visible_as_strike != task_name_expected_format_property:
            raise Exception("Incorrect format option for task status. Expected parameter",
                            task_name_expected_format_property, "is not equal to", is_element_visible_as_strike)
        if task_status_icon_color != task_status_expected_icon_color:
            raise Exception("Incorrect task status icon color. Expected parameter", task_status_expected_icon_color,
                            "is not equal to", task_status_icon_color)
        if svg_path_element.find(task_svg_path_expected_opacity) == -1:
            raise Exception("Incorrect svg path object opacity option". task_svg_path_expected_opacity,
                            "was not found in <path> element")
        if svg_path_element.find(task_svg_path_expected_stroke_dasharray) == -1:
            raise Exception("Incorrect svg path object stroke dasharray option".
                            task_svg_path_expected_stroke_dasharray, "was not found in <path> element")
