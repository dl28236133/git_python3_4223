from tkinter import *
from tkinter import messagebox
import pandas as pd
from functools import partial
import tkinter.ttk
import datetime


#-- 대여시작
def member_info_rent_dbclick(event):
    clickRentBook()

def clickRentUser():
    def clickMemberSearch():
        for row in treeview.get_children() :
            treeview.delete(row)
        
        #이름, 전화번호로 회원 검색

        name = nameinput.get()
        global tel
        tel = TELinput.get()
        df_namelist = list(df_member['Member_NAME'])
        df_tellist = list(df_member['Member_TEL'])

        if (name in df_namelist and tel in df_tellist) or \
                (name in df_namelist and tel == '') or \
                (name == '' and tel in df_tellist):
            datalist = []

            if tel == '' :
                df_search = df_member.loc[df_member['Member_NAME']==name]
                for i in range(len(df_search.index)) :

                    datalist.append([df_search['Member_TEL'].iloc[i], \
                                     df_search['Member_NAME'].iloc[i], \
                                     df_search['Member_BIRTHDATE'].iloc[i], \
                                     df_search['Member_GENDER'].iloc[i], \
                                     df_search['Member_EMAIL'].iloc[i]])
                    
            elif name == '' :
                df_search = df_member.loc[df_member['Member_TEL']==tel]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], \
                                 df_search['Member_NAME'].iloc[i], \
                                 df_search['Member_BIRTHDATE'].iloc[i], \
                                 df_search['Member_GENDER'].iloc[i], \
                                 df_search['Member_EMAIL'].iloc[i]])


            else :
                df_search = df_member.loc[df_member['Member_TEL']==tel]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], \
                                 df_search['Member_NAME'].iloc[i], \
                                 df_search['Member_BIRTHDATE'].iloc[i], \
                                 df_search['Member_GENDER'].iloc[i], \
                                 df_search['Member_EMAIL'].iloc[i]])
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        else:
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")

        # 회원 선택(더블클릭 이벤트)
        selectedmem = treeview.focus()
        Tel = treeview.set(selectedmem, column='1')

    # 회원검색 창 생성

    windowRentUser   = Tk()
    windowRentUser  .title('도서대여(회원검색)')
    windowRentUser  .geometry('600x400')
    windowRentUser  .configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(windowRentUser, text='회원명', bg='LightSkyBlue1')
    TELlabel = Label(windowRentUser, text='전화번호', bg='LightSkyBlue1')
    nameinput = Entry(windowRentUser, width=30)
    TELinput = Entry(windowRentUser, width=30)

    df_member = pd.read_csv('Member.csv', encoding='utf-8-sig')

    treeview = tkinter.ttk.Treeview(windowRentUser, \
                                    columns=["1", "2", "3", "4", "5"], \
                                    show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', member_info_rent_dbclick)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    treeview.place(x=25, y=150)

    df_member = pd.read_csv('Member.csv', encoding = 'cp949')
    
    treeview = tkinter.ttk.Treeview(windowRentUser, \
                                    columns=["1", "2", "3" , "4" , "5"], \
                                    show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', member_info_rent_dbclick)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    treeview.place(x=25, y=150)

    # 검색 버튼

    searchbutton = Button(windowRentUser  , text="검색", width=10, \
                          command=clickMemberSearch)

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)


def clickRentBook():
    def clickRent(event):
        #더블클릭으로 도서 선택
        selectedBook = treeview.focus()
        selectedISBN = treeview.set(selectedBook, column='1')
        selectedISBN = float(selectedISBN)
        selectedISBN = int(selectedISBN)
        
        #대여 상태로 Book.csv 변경
        df_book["BOOK_RENT"].loc[selectedISBN] = True
        df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')        
        
        messagebox.showinfo("대여", "도서를 대여합니다.")

        #RENT.csv 값 생성
        try:
            df_rent = pd.read_csv('RENT.csv', encoding='UTF-8-sig')
        except:
            df_rent = pd.DataFrame( columns=['BOOK_ISBN', \
                                             'USER_PHONE', 'RENT_DATE', \
                                             'RENT_RETURN_DATE', \
                                             'RENT_RETURN_YN'])
            df_rent.to_csv('RENT.csv', index=False, encoding='UTF-8-sig')
            
        isbn = selectedISBN
        phone = tel
        rent_date = datetime.date.today().isoformat()
        rent_return_date = datetime.date.today() + datetime.timedelta(days=14)

        new_rent = {"BOOK_ISBN": isbn, \
                    "USER_PHONE": phone, \
                    "RENT_DATE": rent_date, \
                    "RENT_RETURN_DATE": rent_return_date, \
                    "RENT_RETURN_YN": None}

        df_rent = df_rent.append(new_rent, ignore_index=True)
        df_rent.to_csv('RENT.csv', index=False, encoding='UTF-8-sig')

        windowRentBook.destroy()

    windowRentBook = Tk()
    windowRentBook.geometry("900x350")
    windowRentBook.title("도서 대여")
    windowRentBook.configure(bg='LightSkyBlue1')

    treeview = tkinter.ttk.Treeview(windowRentBook, \
                                    columns=["1", "2", "3" , "4" , "5", "6",\
                                             "7", "8"], show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', clickRent)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("1", text="ISBN", anchor="center")

    treeview.column("#2", width=80, anchor="center")
    treeview.heading("2", text="도서명", anchor="center")
        
    treeview.column("#3", width=100, anchor="center")
    treeview.heading("3", text="저자", anchor="center")

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("4", text="출판사", anchor="center")

    treeview.column("#5", width=80, anchor="center")
    treeview.heading("5", text="가격", anchor="center")
        
    treeview.column("#6", width=100, anchor="center")
    treeview.heading("6", text="URL", anchor="center")

    treeview.column("#7", width=100, anchor="center")
    treeview.heading("7", text="대여여부", anchor="center")

    treeview.place(x=25, y=25)

    # 책 데이터
    df_book = pd.read_csv("Book.csv", encoding='utf-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])
    print(1)
    # 대여 가능 상태인 도서 데이터만 표로 출력
    can = []

    df_book_can = df_book.loc[df_book['BOOK_RENT']==False]
    for i in range(len(df_book_can.index)) :

        can.append([df_book_can['BOOK_ISBN'].iloc[i], \
                    df_book_can['BOOK_TITLE'].iloc[i], \
                    df_book_can['BOOK_AUTHOR'].iloc[i], \
                    df_book_can['BOOK_PUB'].iloc[i], \
                    df_book_can['BOOK_PRICE'].iloc[i], \
                    df_book_can['BOOK_LINK'].iloc[i], \
                    df_book_can['BOOK_RENT'].iloc[i]])

    for i in range(len(can)):
        treeview.insert('', 'end', values=can[i])
    print(df_book_can)
    # 더블클릭으로 도서 선택

#-- 대여끝

def member_info_return_dbclick(event):
    clickReturnBook()
 
def member_info_return_dbclick(event):
    def clickReturn(event):
        selectedBook = treeview.focus()
        selectedISBN = treeview.set(selectedBook, column='1')
        selectedISBN = float(selectedISBN)
        selectedISBN = int(selectedISBN)

        #반납 상태로 Book.csv 변경
        df_book["BOOK_RENT"].loc[selectedISBN] = False
        df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')

        #RENT.csv에 반납 날짜 추가
        return_date = datetime.date.today().isoformat()
        df_rent = pd.read_csv('RENT.csv', encoding='UTF-8-sig')
        df_rent = df_rent.set_index(df_rent['BOOK_ISBN'])
        df_rent["RENT_RETURN_YN"].loc[selectedISBN] = return_date
        df_rent.to_csv('RENT.csv', index=False, encoding='utf-8-sig')
        
        messagebox.showinfo("반납", "도서를 반납합니다.")

        windowReturnBook.destroy() 
   
    
    windowReturnBook = Tk()
    windowReturnBook.geometry("900x350")
    windowReturnBook.title("도서 대여")
    windowReturnBook.configure(bg='LightSkyBlue1')

    treeview = tkinter.ttk.Treeview(windowReturnBook, \
                                    columns=["1", "2", "3" , "4" , "5", "6",\
                                             "7", "8"], show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', clickReturn)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("1", text="ISBN", anchor="center")

    treeview.column("#2", width=80, anchor="center")
    treeview.heading("2", text="도서명", anchor="center")
        
    treeview.column("#3", width=100, anchor="center")
    treeview.heading("3", text="저자", anchor="center")

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("4", text="출판사", anchor="center")

    treeview.column("#5", width=80, anchor="center")
    treeview.heading("5", text="가격", anchor="center")
        
    treeview.column("#6", width=100, anchor="center")
    treeview.heading("6", text="URL", anchor="center")

    treeview.column("#7", width=100, anchor="center")
    treeview.heading("7", text="대여여부", anchor="center")

    treeview.place(x=25, y=25)

    #책 데이터
    df_book = pd.read_csv("Book.csv", encoding='utf-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    
    #대여 상태인 도서 데이터만 표로 출력
    can = []
    df_book_can = df_book.loc[df_book['BOOK_RENT']==True]
    for i in range(len(df_book_can.index)) :
        can.append([df_book_can['BOOK_ISBN'].iloc[i], \
                    df_book_can['BOOK_TITLE'].iloc[i], \
                    df_book_can['BOOK_AUTHOR'].iloc[i], \
                    df_book_can['BOOK_PUB'].iloc[i], \
                    df_book_can['BOOK_PRICE'].iloc[i], \
                    df_book_can['BOOK_LINK'].iloc[i], \
                    df_book_can['BOOK_RENT'].iloc[i]])

    for i in range(len(can)) :
        treeview.insert('', 'end', values=can[i])

#회원 검색 창 (반납) 

def clickReturnUser():
    def clickMemberSearch():
        for row in treeview.get_children() :
            treeview.delete(row)
        
        #이름, 전화번호로 회원 검색
        name = nameinput.get()
        tel = TELinput.get()
        df_namelist = list(df_member['Member_NAME'])
        df_tellist = list(df_member['Member_TEL'])

        if (name in df_namelist and tel in df_tellist) or\
           (name in df_namelist and tel=='') or\
           (name=='' and tel in df_tellist) :
            datalist = []
            if tel == '' :
                df_search = df_member.loc[df_member['Member_NAME']==name]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], \
                                     df_search['Member_NAME'].iloc[i], \
                                     df_search['Member_BIRTHDATE'].iloc[i], \
                                     df_search['Member_GENDER'].iloc[i], \
                                     df_search['Member_EMAIL'].iloc[i]])
                    
            elif name == '' :
                df_search = df_member.loc[df_member['Member_TEL']==tel]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], \
                                 df_search['Member_NAME'].iloc[i], \
                                 df_search['Member_BIRTHDATE'].iloc[i], \
                                 df_search['Member_GENDER'].iloc[i], \
                                 df_search['Member_EMAIL'].iloc[i]])

            else :
                df_search = df_member.loc[df_member['Member_TEL']==tel]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], \
                                 df_search['Member_NAME'].iloc[i], \
                                 df_search['Member_BIRTHDATE'].iloc[i], \
                                 df_search['Member_GENDER'].iloc[i], \
                                 df_search['Member_EMAIL'].iloc[i]])
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        else :
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")

        #회원 선택(더블클릭 이벤트)
        selectedmem = treeview.focus()
        
    # 회원검색 창 생성
    windowReturnUser  = Tk()
    windowReturnUser .title('도서반납(회원검색)')
    windowReturnUser .geometry('600x400')
    windowReturnUser .configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(windowReturnUser  , text='회원명' , bg='LightSkyBlue1')
    TELlabel = Label(windowReturnUser   , text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(windowReturnUser  , width=30)
    TELinput = Entry(windowReturnUser  , width=30)

    df_member = pd.read_csv('Member.csv', encoding = 'cp949')
    
    treeview = tkinter.ttk.Treeview(windowReturnUser, \
                                    columns=["1", "2", "3" , "4" , "5"], \
                                    show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', member_info_return_dbclick)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    treeview.place(x=25, y=150)

    # 검색 버튼
    searchbutton = Button(windowReturnUser  , text="검색", width=10, \
                          command=clickMemberSearch)

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)


#-- 반납 끝

