import os.path
import shutil
from datetime import datetime
import requests,json
import re,os
from selenium import webdriver
import time,random
from lxml import etree
import urllib.parse
# from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
op = webdriver.EdgeOptions()
op.add_experimental_option("detach" , True)
op.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Edge(options=op)
driver.maximize_window()

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
         'referer':"https://pixabay.com/sound-effects/search/laugh/"}

SAS_token=''
azcopy_path=r"azcopy.exe"
OUT_DIR=r"C:\Users\v-zhazhai\Downloads\ApplePodcast"
os.makedirs(OUT_DIR, exist_ok=True)
#https://stdstoragettsdp01eus.blob.core.windows.net/data/v-litfen/apple/tier3/sa/podcast/raw/data_batch01/
OUT_blobdir=r'https://stdstoragettsdp01eus.blob.core.windows.net/data/v-litfen/apple/tier1/jajp/podcast/raw/data_batch01/'
search_list_url= ["https://podcasts.apple.com/de/podcast/tomorrow-business-stars-lifestyle/id1524307880","https://podcasts.apple.com/br/podcast/a-hora/id1753993865"]
for i in search_list_url:
    print(i)
    b = 1
    driver.get(i)
    time.sleep(5)
    # 检查是否已经登录
    # def is_logged_in():
    #     try:
    #         # 查找登录按钮，若找不到，说明已登录
    #         sign_in_button = driver.find_element(By.XPATH, "//button[@data-testid='sign-in-button']")
    #         return False  # 还没有登录，登录按钮仍然存在
    #     except Exception as e:
    #         return True  # 找不到登录按钮，说明已经登录

    # # 如果未登录，则执行登录流程
    # if not is_logged_in():
    #     # 点击登录按钮  /html/body/div/div/div[2]/div/div/amp-chrome-player/div[2]/div[2]/button
    #     button = driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div/div/amp-chrome-player/div[2]/div[2]/button')
    #     # button = driver.find_element(by=By.XPATH, value="//button[@data-testid='sign-in-button']")
    #     button.click()
    #     apple_id = 'moonenhy@gmail.com'  # 请替换为你的 Apple ID
    #     password = 'Yueliang1'  # 请替换为你的密码

    #     iframe = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "authenticate")]')))
    #     # 切换到 iframe
    #     driver.switch_to.frame(iframe)

    #     # 等待并定位 Apple ID 输入框，输入 Apple ID
    #     apple_id_input = WebDriverWait(driver, 20).until( EC.visibility_of_element_located((By.XPATH, '//input[@id="accountName"]')))
    #     apple_id_input.send_keys(apple_id)  # 输入 Apple ID

    #     button = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[1]/cwc-app/div/div/div[3]/button/span')
    #     button.click()
    #     # 等待密码框加载
    #     time.sleep(30)

    #     WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@id="aid-auth-widget-iFrame"]')))
    #     # 定位密码输入框并输入密码
    #     password_input =  WebDriverWait(driver, 30).until( EC.visibility_of_element_located((By.XPATH, '//input[@id="password_text_field"]')))  # 假设密码输入框的 id 为 password
    #     # password_input = driver.find_element(By.XPATH, '//input[@id="password_text_field"]')  # 假设密码输入框的 id 为 password
    #     password_input.send_keys(password)  # 输入密码
    #     # 提交登录信息
    #     login_button = driver.find_element(By.XPATH, '//button[@id="sign-in"]')
    #     login_button.click()

    #     # # 切换回主页面（如果需要）
    #     driver.switch_to.default_content()
    
    # time.sleep(5)
    # driver.get(i)
    # try:
    #     button = driver.find_element(by=By.XPATH, value='//*[@class="headings__metadata-bottom svelte-1scg3f0"]/ul/li[@class="metadata__explicit-badge svelte-11a0tog"]')
    # except:
    blog_index = search_list_url.index(i) + 35  # str(blog_index).zfill(5) + '_' +
    # print(i)
    locale = i.split('/')[-4]
    # print(locale)
    blogname = i.split('/')[-1]
    outdir = os.path.join(OUT_DIR, locale,blogname)
    blobdir = os.path.join(OUT_blobdir, blogname)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    try:
        button = driver.find_element(by=By.XPATH, value='//*[@id="scrollable-page"]/main/div/div/div[3]/div/div/a')
        button.click()
    except:
        print("已经到顶了")
    time.sleep(2)
    button = driver.find_elements(by=By.XPATH, value='//li[@class="svelte-834w84"]/div/a')
    num1 = len(button)
    print(num1)
    button = driver.find_elements(by=By.XPATH,
                                  value='//span[@class="episode-details__explicit-badge svelte-5dvoy6"]/span/span')
    num2 = len(button)
    print(num2)
    if num1 >= num2:
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        while True:
            button = driver.find_elements(by=By.XPATH, value='//li[@class="svelte-834w84"]/div/a')
            num1 = len(button)
            # print(num1)
            for _ in range(50):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                action = ActionChains(driver)
                action.send_keys(Keys.ARROW_DOWN).perform()
                driver.execute_script('window.scrollBy(0,4000)')
                action = ActionChains(driver)
                action.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(2)
            button = driver.find_elements(by=By.XPATH, value='//li[@class="svelte-834w84"]/div/a')
            num2 = len(button)
            # print(num2)
            if num2 == num1:
                break

        print(len(button))
        if len(button) != 0:
            list1 = []
            for i in button:
                list1.append(i.get_attribute("href"))
            print(len(list1))
            for i in list1:
                dict1 = {}
                driver.get(i)
                time.sleep(3)
                # audio_button = driver.find_element(by=By.XPATH,value="/html/body/div/div/div[2]/main/div/div[1]/div/div/div[2]/div/div/div/button")
                audio_button = driver.find_element(by=By.XPATH,
                                                   value='//*[@class="button svelte-yk984v primary"]/button')
                audio_button.click()
                time.sleep(5)
                try:
                    audio = driver.find_element(by=By.XPATH, value="/html/body/audio")
                    audio_url = audio.get_attribute("src")
                    # print(audio_url)
                    name = driver.find_element(by=By.XPATH,
                                               value='//*[@id="scrollable-page"]/main/div/div/div[1]/div/div/div[1]/h1/span').text
                    # name="""u'%s'""" % name
                    # jiemu=driver.find_element(by=By.XPATH,value='//*[@id="scrollable-page"]/main/div/div[3]/div[2]/ul/li[1]/div[2]').text
                    # jiemu="""u'%s'""" % jiemu
                    dict1['AudioTitle'] = name
                    # dict1['CaptionType']=eval(jiemu)
                    num = len(driver.find_elements(by=By.XPATH,
                                                   value='//*[@class="section section--information svelte-1jzcdlo"]/div[2]/ul/li'))
                    # print(num)
                    for i in range(1, num + 1):
                        key = driver.find_element(by=By.XPATH,
                                                  value='//*[@class="section section--information svelte-1jzcdlo"]/div[2]/ul/li[' + str(
                                                      i) + ']/div[1]').text
                        value = driver.find_element(by=By.XPATH,
                                                    value='//*[@class="section section--information svelte-1jzcdlo"]/div[2]/ul/li[' + str(
                                                        i) + ']/div[2]').text
                        if key in ['Émission', 'Sendung', 'Podcast', 'Programa', 'Show', '番組', '프로그램']:
                            key = 'CaptionType'
                        elif key in ['Chaîne', 'チャンネル']:
                            key = 'Channel'
                        elif key in ['频率', 'Fréquence', 'Häufigkeit', 'Frequency', '頻度', '주기']:
                            key = 'Frequency'
                        elif key in ['发布时间', 'Publiée', 'Veröffentlicht', 'Uscita', 'Publicación', 'Published', '配信日',
                                     '발행일']:
                            key = 'release_time'
                        elif key in ['长度', 'Durée', 'Länge', 'Durata', 'Duración', 'Length', '長さ', '길이']:
                            key = 'Duration'
                            value = value.replace(' 分钟', 'min').replace('分钟', 'min').replace(' 分', 'min').replace('分',
                                                                                                                  'min')
                        elif key in ['Saison', 'Temporada']:
                            key = 'Season'
                        elif key in ['单集', 'Épisode', 'Episodio', 'エピソード', '에피소드']:
                            key = 'episode'
                        elif key in ['分级', 'Classification', 'Bewertung', 'Classificazione', 'Clasificación', 'Rating',
                                     '制限指定', '등급']:
                            key = 'Type'
                        dict1[key] = value
                    dict1['AudioUrl'] = audio_url
                    name = audio_url.split('/')[-1].split('.')[0].replace('https://','').replace('https%3A%2F%2F','')
                    jsonpath = os.path.join(outdir, name + str(b).zfill(5) + '.json')
                    m4apath = os.path.join(outdir, name + str(b).zfill(5) + '.mp3')


                    def default(o):
                        if isinstance(o, datetime):
                            return o.isoformat()
                        raise TypeError("Unserializable object {}".format(o))


                    with open(jsonpath, 'w', encoding='utf-8') as f:
                        json.dump(dict1, f, ensure_ascii=False, indent=4, default=default)
                    response = requests.get(url=f"{audio_url}", headers=headers)
                    with open(m4apath, 'wb') as f:
                        f.write(response.content)
                    # a=a+1
                    b = b + 1
                    time.sleep(3)
                except:
                    print('error' + '\t' + str(i))
                    continue
            # a = a + 1
        # azcommand = f'{azcopy_path} copy "{outdir}/*" "{blobdir}{SAS_token}"'
        # # 执行上传命令
        # upload_status = os.system(azcommand)

        # # 检查上传是否成功
        # if upload_status == 0:
        #     print("上传成功，准备删除目录...")
        #     if os.path.exists(outdir):
        #         try:
        #             shutil.rmtree(outdir)
        #             print("目录已删除")
        #         except OSError as e:
        #             print(f"无法删除目录: {e}")
        # else:
        #     print("上传失败，目录不会删除。")