

from selenium.webdriver.common.by import By
import xlrd
import time

def locator_value(driver, locator_type, value):

    if locator_type == "id":
        webelement = driver.find_element_by_id(value)
       # enter_text(driver, webelement, text)
    elif locator_type == "name":
        webelement = driver.find_element_by_name(value)
    elif locator_type == "xpath":
        webelement = driver.find_element_by_name(value)
    return webelement


def enter_text(driver, webelement, text):

    try:
        webelement.send_keys(text)
    except Exception:
        print "No Element found to enter text"


def click_button(driver, webelement):
    try:
        webelement.click()
    except Exception:
        print "No such Element"


def get_data_from_spread_sheet():
    workbook = xlrd.open_workbook("C:/Users/sagarkul/Desktop/Keyword.xlsx")
    worksheet = workbook.sheet_by_name("Sheet1")
    rowEndIndex = worksheet.nrows - 1
    colEndIndex = worksheet.ncols - 1
    rowStartIndex = 0
    colStartIndex = 0
    data_row = []
    curr_row = rowStartIndex
    while curr_row <= rowEndIndex:
            cur_col = colStartIndex
            while cur_col <= colEndIndex:
                value = worksheet.cell_value(curr_row, cur_col)
                data_row.append(value)
                cur_col+=1
            curr_row += 1
    return data_row


def step_execution(driver):
    data_row_index = get_data_from_spread_sheet()

    for item in data_row_index:
        if item == "enter_username":
            web_elemnt = locator_value(driver, data_row_index[13], data_row_index[14])
            enter_text(driver, web_elemnt, data_row_index[15])

        elif item == "click_next":
            web_elemnt = locator_value(driver, data_row_index[17], data_row_index[18])
            click_button(driver, web_elemnt)

        elif item == "enter_passward":
            time.sleep(2)
            web_elemnt = locator_value(driver, data_row_index[21], data_row_index[22])
            enter_text(driver, web_elemnt, data_row_index[23])

        elif item == "click_sign_in":
            web_elemnt = locator_value(driver, data_row_index[25], data_row_index[26])
            click_button(driver, web_elemnt)









