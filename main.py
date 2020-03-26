from time import sleep
from selenium import webdriver
from sys import argv
from win10toast import ToastNotifier


def main(driver, link):
    driver.get(link)
    sleep(10)
    return check_cart_button(driver)


def check_cart_button(driver):
    if driver.find_element_by_id("add_to_cart_button").is_displayed():
        driver.find_element_by_id("add_to_cart_button").click()
        return True
    return False


if __name__ == '__main__':
    if len(argv) != 2:
        raise Exception("Manca un argomento")
    toaster = ToastNotifier()
    link = argv[1]
    driver = webdriver.Edge(executable_path="C:/webdriver/msedgedriver.exe")
    numero_tentativi = 0
    while not main(driver, link):
        sleep(10)
        numero_tentativi += 1
        print(numero_tentativi)
    toaster.show_toast("DecathlonAddCartBot", "Il prodotto da lei selezionato è al momento disponibile")
