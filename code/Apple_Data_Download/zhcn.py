import os.path
import shutil
from datetime import datetime
import requests,json
import re
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

SAS_token='?sv=2023-01-03&st=2024-12-15T09%3A29%3A28Z&se=2024-12-21T09%3A29%3A00Z&skoid=ee0abe40-c783-4ec3-9f28-341c64cfe859&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2024-12-15T09%3A29%3A28Z&ske=2024-12-21T09%3A29%3A00Z&sks=b&skv=2023-01-03&sr=c&sp=racwdxltf&sig=x6NSiB1YTZLmrq10U%2FmPFN4vFeHDuqEHwTTL906AwQ8%3D'
azcopy_path=r"D:\v-huayuecao\Apple_Data_Download\azcopy.exe"
OUT_DIR=r"C:\Users\v-zhazhai\Desktop\Apple_data\batch06"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_blobdir=r'https://stdstoragettsdp01eus.blob.core.windows.net/data/v-litfen/apple/tier1/jajp/podcast/raw/data_batch01/'
# url=f"https://podcasts.apple.com/gb/charts"
#
# driver.get(url)
# time.sleep(1)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# button=driver.find_element(by=By.XPATH,value='/html/body/div/div/div[2]/main/div/div[2]/div[1]/div[1]/h2/button')
# button.click()
# while True:
#     button = driver.find_elements(by=By.XPATH, value='//ul[@class="grid svelte-1kdxsjw grid--flow-row"]/li/div/a')
#     num1 = len(button)
#     # print(num1)
#     for _ in range(50):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         action = ActionChains(driver)
#         action.send_keys(Keys.ARROW_DOWN).perform()
#         driver.execute_script('window.scrollBy(0,4000)')
#         action = ActionChains(driver)
#         action.send_keys(Keys.ARROW_DOWN).perform()
#         time.sleep(2)
#     button = driver.find_elements(by=By.XPATH, value='//ul[@class="grid svelte-1kdxsjw grid--flow-row"]/li/div/a')
#     num2 = len(button)
#     # print(num2)
#     if num2 == num1:
#         break
# # print(len(button))
# search_list_url=[]
# if len(button)!=0:
#     for i in button:
#         search_list_url.append(i.get_attribute("href"))

search_list_url=['https://podcasts.apple.com/cn/podcast/%E5%8F%88%E4%B8%80%E6%9C%AC/id1597381578', 'https://podcasts.apple.com/cn/podcast/%E5%A4%A7%E4%B8%8A%E6%B5%B7%E6%AD%8C%E8%88%9E%E5%8E%85/id1504870875', 'https://podcasts.apple.com/cn/podcast/%E5%85%AB%E5%8D%A6%E5%A4%9A%E4%B8%80%E7%82%B9/id1451455818', 'https://podcasts.apple.com/cn/podcast/%E7%83%AD%E6%95%8F%E4%BF%AE%E8%BE%9E%E5%AD%A6-instant-acumen/id1551459284', 'https://podcasts.apple.com/cn/podcast/%E7%A6%BB%E6%95%A3%E7%94%B5%E6%B3%A2/id1555909745', 'https://podcasts.apple.com/cn/podcast/%E5%87%8C%E6%92%AD%E5%BE%AE%E6%AD%A5/id1563145522', 'https://podcasts.apple.com/cn/podcast/%E7%A9%BA%E9%97%B4/id1602842350', 'https://podcasts.apple.com/cn/podcast/%E5%9F%8E%E8%AE%B0%E6%92%AD%E5%AE%A2/id1473795699', 'https://podcasts.apple.com/cn/podcast/101%E4%B8%AA%E6%97%B7%E7%9C%9F%E4%BA%BA%E6%95%85%E4%BA%8B/id1776517400']
a=1
for i in search_list_url:
    print(i)
    b = 1
    driver.get(i)
    time.sleep(5)
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
    button = driver.find_elements(by=By.XPATH, value='//li[@class="svelte-8rlk6b"]/div/a')
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
            button = driver.find_elements(by=By.XPATH, value='//li[@class="svelte-8rlk6b"]/div/a')
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
            button = driver.find_elements(by=By.XPATH, value='//li[@class="svelte-8rlk6b"]/div/a')
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
                time.sleep(2)
                # audio_button = driver.find_element(by=By.XPATH,value="/html/body/div/div/div[2]/main/div/div[1]/div/div/div[2]/div/div/div/button")
                audio_button = driver.find_element(by=By.XPATH,
                                                   value='//*[@class="button svelte-okjphp primary"]/button')
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
        # os.system(azcommand)
        # # shutil.rmtree(outdir)
        # if os.path.exists(outdir):
        #     # 尝试删除目录
        #     try:
        #         shutil.rmtree(outdir)
        #         print("目录已删除")
        #     except OSError as e:
        #         print(f"无法删除目录: {e}")