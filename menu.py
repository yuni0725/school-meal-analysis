def download():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import os

    from time import sleep

    for file in os.listdir(f"{os.getcwd()}\\menu"):
        os.remove(f"{os.getcwd()}\\menu\\{file}")

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        { "download.default_directory": 'C:\\Users\\user\\Desktop\\Code\\menu',
        "download.prompt_for_download": False,   
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        }
    )
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)

    
    for i in range(1, 3):
        URL = f"https://school.jbedu.kr/sangsan/M01060401/list?s_idx={i}"
        driver.get(URL)

        for i in range(1, 11):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#usm-content-body-id > table > tbody > tr:nth-child({i}) > td.tch-tit > a').click()
                driver.find_element(By.CSS_SELECTOR, '#m_mainView > tbody > tr:nth-child(3) > td > div > div.file-btn2 > span:nth-child(1) > a').click()
                driver.back()
                print("download complete")
            except:
                print('no file')

        sleep(1)
    driver.close()
    driver.quit()

def rename():
    import win32com.client as win32
    import os
    file_path = 'C:\\Users\\user\\Desktop\\Code\\menu\\'
    file_names = os.listdir(file_path)
    os.chdir(file_path)

    i = 1
    for name in file_names:
        path = f"{file_path}{name}"
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(path)
        if not(".xlsx" in name):
            wb.SaveAs(path+"x", FileFormat = 51)
            wb.SaveAs(f"{file_path}{i}.xlsx", FileFormat = 51)
            wb.Close() 
            excel.Application.Quit()
            os.remove(path)
            os.remove(path + 'x')
        else:
            wb.SaveAs(f"{file_path}{i}.xlsx", FileFormat = 51)
            wb.Close() 
            excel.Application.Quit()
            os.remove(path)
        i += 1

def get_data():
    import os
    file_path = 'C:\\Users\\user\\Desktop\\Code\\menu'
    file_names = os.listdir(file_path)
    os.chdir(file_path)

    menu = []

    from openpyxl import load_workbook

    for name in file_names:
        print(name)
        wb = load_workbook(name)
        ws = wb['기숙사식당']

        for row in ws.rows:
            for cell in row:
                if cell.value:
                    try:
                        if 'ㆍ' in cell.value:
                            for value in cell.value.split('\n'):
                                try :
                                    value = value.split('(')[0]
                                    value = value.split("ㆍ")[1].split('/')
                                    menu.append(value[0])
                                    if value[1]:
                                        menu.append(value[1])
                                except IndexError:
                                    pass
                    except TypeError:
                        pass
    print(f"총 급식수: {len(menu)}")
    print(f"중복 제외 급식수 {len(list(set(menu)))}")

    return menu

download()
rename()
a = get_data()


