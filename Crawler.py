# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import re
import schedule
import time

class NewsClass:
    title_text=[]
    link_text=[]
    source_text=[]
    date_text=[]
    contents_text=[]

    def del_Overlab(self): #중복제거 함수
        #임시로 데이터를 옮길 리스트 변수들
        title_temp=[]
        link_temp=[]
        source_temp=[]
        date_temp=[]
        contents_temp=[]

        while(self.link_text): #인자갯수만큼 반복
            url = self.link_text.pop(0) #맨처음을 꺼냄
            if not url in  self.link_text: #맨처음 URL과 겹치는 URL이 없다면 삽입
                link_temp.append(url)
                title_temp.append(self.title_text.pop(0))
                source_temp.append(self.source_text.pop(0))
                date_temp.append(self.date_text.pop(0))
                contents_temp.append(self.contents_text.pop(0))
            else: #겹치는 URL이 있다면 POP하여 삭제
                self.title_text.pop(0)
                self.source_text.pop(0)
                self.date_text.pop(0)
                self.contents_text.pop(0)

        #원래 리스트로 다시 복사
        self.title_text = title_temp[:]
        self.link_text = link_temp[:]
        self.source_text = source_temp[:]
        self.date_text = date_temp[:]
        self.contents_text = contents_temp[:]

#날짜 정제화 함수
def date_cleansing(_string):
    try:
        #지난 뉴스
        #머니투데이  10면1단  2018.11.05.  네이버뉴스   보내기
        pattern = '\d+.(\d+).(\d+).'  #정규표현식
        r = re.compile(pattern)
        match = re.search(pattern, _string)  # 0번째 인덱스는 문자열 전체 반환 2018.11.05.
        news.date_text.append(match)

    except AttributeError:
        #최근 뉴스(아래 두개 중 하나의 패턴)
        #이데일리  1시간 전  네이버뉴스   보내기
        #동아일보  A18면1단  8시간 전  네이버뉴스  보내기
        pattern = '(\d*[시|분])'     #정규표현식
        #r = re.compile(pattern, re.X) # 정규식 안에 공백은 무시한다
        match = re.search(pattern, _string)
        if match.find('시') is not -1 : # '시'라는 글자가 있다면
            match = match + '간 전'
        elif match.find('분') is not -1 : # '분'라는 글자가 있다면
            match = match + ' 전'

        news.date_text.append(match)


#내용 정제화 함수
def contents_cleansing(contents):
    first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
                                      str(contents)).strip()  #앞에 필요없는 부분 제거
    second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
                                       first_cleansing_contents).strip()#뒤에 필요없는 부분 제거 (새끼 기사)
    third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
    news.contents_text.append(third_cleansing_contents)
    #print(news.contents_text)


def crawler(maxpage,query,sort,s_date,e_date,now):

    s_from = s_date.replace(".","")
    e_to = e_date.replace(".","")
    page = 1
    maxpage_t =(int(maxpage)-1)*10+1   # 11= 2페이지 21=3페이지 31=4페이지  ...81=9페이지 , 91=10페이지, 101=11페이지

    while page <= maxpage_t:
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        response = requests.get(url, headers = headers)
        html = response.text

        #뷰티풀소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        #<a>태그에서 제목과 링크주소 추출
        atags = soup.select('._sp_each_title')
        for atag in atags:
            news.title_text.append(atag.text)     #제목
            news.link_text.append(atag['href'])   #링크주소

        #신문사 추출
        source_lists = soup.select('._sp_each_source')
        for source_list in source_lists:
            news.source_text.append(source_list.text)    #신문사

        #날짜 추출
        date_lists = soup.select('.txt_inline')
        for date_list in date_lists:
            test=date_list.text
            date_cleansing(test)  #날짜 정제 함수사용

        #본문요약본
        contents_lists = soup.select('ul.type01 dl')
        for contents_list in contents_lists:
            #print('==='*40)
            #print(contents_list)
            contents_cleansing(contents_list) #본문요약 정제화

        #엑셀로 저장하기 위한 변수

        news.del_Overlab() # 중복기사 제거
        #모든 리스트 딕셔너리형태로 저장
        result = {"date" : news.date_text , "title":news.title_text ,  "source" : news.source_text ,"contents": news.contents_text ,"link":news.link_text }
        #print(page)

        df = pd.DataFrame(result)  #df로 변환
        page += 10


    # 새로 만들 파일이름 지정
    outputFileName = '뉴스 모니터링 %s.0%s.%s %s시 %s분.xlsx' % (now.year, now.month, now.day, now.hour, now.minute)
    df.to_excel(outputFileName,sheet_name='sheet1')

def main():
    now = datetime.now() #파일이름 현 시간으로 저장하기
    #info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
    print('%s.0%s.%s %s시 %s분 %s초 뉴스 검색을 시작합니다' % (now.year, now.month, now.day, now.hour, now.minute, now.second) )
    maxpage = '3' #input("최대 크롤링할 페이지 수 입력하세요: ")
    query = '해군'#input("검색어 입력: ")
    sort = '0' #input("뉴스 검색 방식 입력(관련도순=0  최신순=1  오래된순=2): ")    #관련도순=0  최신순=1  오래된순=2
    s_date =  '%s.0%s.%s' % (now.year, now.month, now.day)#input("시작날짜 입력(2019.01.04):")  #2019.01.04
    e_date =  '%s.0%s.%s' % (now.year, now.month, now.day)#input("끝날짜 입력(2019.01.05):")   #2019.01.05
    crawler(maxpage,query,sort,s_date,e_date,now)

#각 크롤링 결과 저장하기 위한 리스트 선언
news = NewsClass()
result={}
period = int(input('주기(초 단위, 최소 1분 이상)를 설정해주세요 : '))
schedule.every(period).seconds.do(main)
#print(str(period)+'초마다 뉴스 검색을 시작합니다.')
main()
while True:
    schedule.run_pending()
    time.sleep(1)
