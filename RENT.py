from tkinter import *
from tkinter import messagebox
import pandas as pd
from functools import partial
import tkinter.ttk
import datetime


# -- 대여시작
def clickRentUser():
    def member_info_rent_dbclick(event):
        try:
            selectedmem = treeview.focus()
            if(selectedmem ==""):
                raise
            global name
            name = treeview.set(selectedmem,column='2' )
            global Tel
            Tel = treeview.set(selectedmem, column='1')
            clickRentBook()
            windowRentUser.destroy()
        except:
            pass
    def clickMemberSearch():
        for row in treeview.get_children():
            treeview.delete(row)

        # 이름, 전화번호로 회원 검색

        name = nameinput.get()
        tel = TELinput.get()

        if name == '':
            nameresultlist = [None]

        else:
            df_search = df_member[df_member['Member_NAME'].str.contains(name)]
            nameresultlist = list(df_search['Member_NAME'])

        if tel == '':
            telresultlist = [None]

        else:
            df_search = df_member[df_member['Member_TEL'].str.contains(tel)]
            telresultlist = list(df_search['Member_TEL'])

        if ((nameresultlist != [None] and nameresultlist != [] and telresultlist == [None]) or (
                nameresultlist == [None] and telresultlist != [] and telresultlist != [None])
                or (nameresultlist != [None] and nameresultlist != [] and telresultlist != [
                    None] and telresultlist != [])):
            datalist = []
            if tel == '':
                df_search = df_member.loc[df_member['Member_NAME'].str.contains(name)]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i],
                                     df_search['Member_BIRTHDATE'].iloc[i],
                                     df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            elif name == '':
                df_search = df_member.loc[df_member['Member_TEL'].str.contains(tel)]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i],
                                     df_search['Member_BIRTHDATE'].iloc[i],
                                     df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else:
                df_search = df_member.loc[
                    (df_member['Member_TEL'].str.contains(tel)) & (df_member['Member_NAME'].str.contains(name))]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i],
                                     df_search['Member_BIRTHDATE'].iloc[i],
                                     df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            for j in range(len(datalist)):
                treeview.insert('', 'end', values=datalist[j])

        else:
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")

    # 회원검색 창 생성
    windowRentUser = Tk()
    windowRentUser.title('도서대여(회원검색)')
    windowRentUser.geometry('600x400')
    windowRentUser.configure(bg='LightSkyBlue1')

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

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=140, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    treeview.place(x=25, y=150)

    datalist = []
    for i in range(len(df_member.index)):
        datalist.append(
            [df_member['Member_TEL'].iloc[i], df_member['Member_NAME'].iloc[i], df_member['Member_BIRTHDATE'].iloc[i],
             df_member['Member_GENDER'].iloc[i], df_member['Member_EMAIL'].iloc[i]])

    for j in range(len(datalist)):
        treeview.insert('', 'end', values=datalist[j])

    # 검색 버튼
    searchbutton = Button(windowRentUser, text="검색", width=10, \
                          command=clickMemberSearch)

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)
    treeview.bind('<Double-Button-1>', member_info_rent_dbclick)

def clickRentBook():
    def clickSearch():
        for row in treeview.get_children():
            treeview.delete(row)

        BookName = InputBookName.get()
        AuthorName = InputAuthor.get()

        if BookName == '':
            nameresultlist = [None]

        else:
            df_search = df_book[df_book['BOOK_TITLE'].str.contains(BookName, case=False)]
            nameresultlist = list(df_search['BOOK_TITLE'])

        if AuthorName == '':
            telresultlist = [None]

        else:
            df_search = df_book[df_book['BOOK_AUTHOR'].str.contains(AuthorName, case=False)]
            telresultlist = list(df_search['BOOK_AUTHOR'])

        if ((nameresultlist != [None] and nameresultlist != [] and telresultlist == [None]) or (
                nameresultlist == [None] and telresultlist != [] and telresultlist != [None])
                or (nameresultlist != [None] and nameresultlist != [] and telresultlist != [
                    None] and telresultlist != [])):

            datalist = []
            if AuthorName == '':
                df_search = df_book.loc[df_book['BOOK_TITLE'].str.contains(BookName, case=False)]
                for i in range(len(df_search.index)):
                    if (df_search["BOOK_RENT"].iloc[i] == "True"):
                        datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                             df_search['BOOK_AUTHOR'].iloc[i],
                                             df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                             df_search['BOOK_RENT'].iloc[i]])

            elif BookName == '':
                df_search = df_book.loc[df_book['BOOK_AUTHOR'].str.contains(AuthorName, case=False)]
                for i in range(len(df_search.index)):
                    if (df_search["BOOK_RENT"].iloc[i] == "True"):
                        datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                             df_search['BOOK_AUTHOR'].iloc[i],
                                             df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                             df_search['BOOK_RENT'].iloc[i]])

            else:
                df_search = df_book.loc[
                    (df_book['BOOK_AUTHOR'].str.contains(AuthorName, case=False)) & (
                        df_book['BOOK_TITLE'].str.contains(BookName, case=False))]
                for i in range(len(df_search.index)):
                    if (df_search["BOOK_RENT"].iloc[i] == "True"):
                        datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                             df_search['BOOK_AUTHOR'].iloc[i],
                                             df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                             df_search['BOOK_RENT'].iloc[i]])

            for j in range(len(datalist)):
                treeview.insert('', 'end', text=j, values=datalist[j], iid=str(j) + "번")

    def clickRent():
        # 더블클릭으로 도서 선택
        selectedBook = treeview.focus()
        selectedISBN = treeview.set(selectedBook, column='1')
        selectedISBN = float(selectedISBN)
        selectedISBN = int(selectedISBN)

        # 대여 상태로 Book.csv 변경
        df_book["BOOK_RENT"].loc[selectedISBN] = True
        df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')

        messagebox.showinfo("대여", "도서를 대여합니다.")

        # RENT.csv 값 생성
        try:
            df_rent = pd.read_csv('RENT.csv', encoding='UTF-8-sig')
        except:
            df_rent = pd.DataFrame(columns=['BOOK_ISBN', \
                                            'USER_NAME', \
                                            'USER_PHONE', 'RENT_DATE', \
                                            'RENT_RETURN_DATE', \
                                            'RENT_YN'])
            df_rent.to_csv('RENT.csv', index=False, encoding='UTF-8-sig')


        isbn = selectedISBN
        title = df_book["BOOK_TITLE"].loc[selectedISBN]
        rentYN = df_book["BOOK_RENT"].loc[selectedISBN]

        rent_date = datetime.date.today().isoformat()
        rent_return_date = datetime.date.today() + datetime.timedelta(days=14)

        new_rent = { \
                    "BOOK_ISBN": isbn, \
                    "BOOK_TITLE": title, \
                    "USER_NAME": name, \
                    "USER_PHONE": Tel, \
                    "RENT_DATE": rent_date, \
                    "RENT_RETURN_DATE": rent_return_date, \
                    "RENT_YN": rentYN}

        df_rent = df_rent.append(new_rent, ignore_index=True)
        df_rent.to_csv('RENT.csv', index=False, encoding='UTF-8-sig')

        windowRentBook.destroy()

    windowRentBook = Tk()
    windowRentBook.geometry("850x400")
    windowRentBook.title("도서 대여")
    windowRentBook.configure(bg='LightSkyBlue1')

    labelBookName = Label(windowRentBook, text="도서명 :", bg='LightSkyBlue1')
    labelAuthor = Label(windowRentBook, text="저자 :", bg='LightSkyBlue1')
    InputBookName = Entry(windowRentBook, width=30)
    InputBookName.pack()
    InputBookName.place(x=100, y=25)

    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    buttonSearch = Button(windowRentBook, text="검색", command=clickSearch)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)

    labelAuthor.pack()
    labelAuthor.place(x=25, y=50)

    InputAuthor = Entry(windowRentBook, width=30)
    InputAuthor.pack()
    InputAuthor.place(x=100, y=50)

    # 대여 버튼
    rentbutton = Button(windowRentBook, text="대여", width=10, \
                        command=clickRent)

    treeview = tkinter.ttk.Treeview(windowRentBook, columns=["1", "2", "3", "4", "5", "6"] , height = 12)
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=80)
    treeview.heading("#0", text="index")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("1", text="ISBN", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("2", text="도서명", anchor="center")

    treeview.column("#3", width=80, anchor="center")
    treeview.heading("3", text="저자명", anchor="center")

    treeview.column("#4", width=80, anchor="center")
    treeview.heading("4", text="출판사", anchor="center")

    treeview.column("#5", width=100, anchor="center")
    treeview.heading("5", text="가격", anchor="center")

    treeview.column("#6", width=150, anchor="center")
    treeview.heading("6", text="대여 여부", anchor="center")

    treeview.place(x=25, y=100)
    rentbutton.place(x=750, y=337)

    # 책 데이터
    df_book = pd.read_csv("Book.csv", encoding='utf-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    # 대여 가능 상태인 도서 데이터만 표로 출력
    can = []
    df_book_can = df_book.loc[df_book['BOOK_RENT'] == False]
    for i in range(len(df_book_can.index)):
        can.append([df_book_can['BOOK_ISBN'].iloc[i], \
                    df_book_can['BOOK_TITLE'].iloc[i], \
                    df_book_can['BOOK_AUTHOR'].iloc[i], \
                    df_book_can['BOOK_PUB'].iloc[i], \
                    df_book_can['BOOK_PRICE'].iloc[i], \
                     \
                    df_book_can['BOOK_RENT'].iloc[i]])

    for i in range(len(can)):
        treeview.insert('', 'end', text=i, values=can[i], iid=str(i) + "번")


# -- 대여끝


# -- 반납 시작
def clickReturnUser():
    def member_info_return_dbclick(event):
        try:
            selectedmem = treeview.focus()
            if (selectedmem == ""):
                raise
            global name
            name = treeview.set(selectedmem, column='2')
            global Tel
            Tel = treeview.set(selectedmem, column='1')
            windowReturnUser.destroy()
            clickReturnBook()
        except:
            pass
    def clickMemberSearch():
        for row in treeview.get_children():
            treeview.delete(row)

        # 이름, 전화번호로 회원 검색
        name = nameinput.get()
        tel = TELinput.get()

        if name == '':
            nameresultlist = [None]

        else:
            df_search = df_member[df_member['Member_NAME'].str.contains(name)]
            nameresultlist = list(df_search['Member_NAME'])

        if tel == '':
            telresultlist = [None]

        else:
            df_search = df_member[df_member['Member_TEL'].str.contains(tel)]
            telresultlist = list(df_search['Member_TEL'])

        if ((nameresultlist != [None] and nameresultlist != [] and telresultlist == [None]) or (
                nameresultlist == [None] and telresultlist != [] and telresultlist != [None])
                or (nameresultlist != [None] and nameresultlist != [] and telresultlist != [
                    None] and telresultlist != [])):
            datalist = []
            if tel == '':
                df_search = df_member.loc[df_member['Member_NAME'].str.contains(name)]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i],
                                     df_search['Member_BIRTHDATE'].iloc[i],
                                     df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            elif name == '':
                df_search = df_member.loc[df_member['Member_TEL'].str.contains(tel)]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i],
                                     df_search['Member_BIRTHDATE'].iloc[i],
                                     df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else:
                df_search = df_member.loc[
                    (df_member['Member_TEL'].str.contains(tel)) & (df_member['Member_NAME'].str.contains(name))]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i],
                                     df_search['Member_BIRTHDATE'].iloc[i],
                                     df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            for j in range(len(datalist)):
                treeview.insert('', 'end', values=datalist[j])

        else:
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")

    # 회원검색 창 생성
    windowReturnUser = Tk()
    windowReturnUser.title('도서반납(회원검색)')
    windowReturnUser.geometry('600x400')
    windowReturnUser.configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(windowReturnUser, text='회원명', bg='LightSkyBlue1')
    TELlabel = Label(windowReturnUser, text='전화번호', bg='LightSkyBlue1')
    nameinput = Entry(windowReturnUser, width=30)
    TELinput = Entry(windowReturnUser, width=30)

    df_member = pd.read_csv('Member.csv', encoding='utf-8-sig')

    treeview = tkinter.ttk.Treeview(windowReturnUser, \
                                    columns=["1", "2", "3", "4", "5"], \
                                    show='headings')
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=140, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    treeview.place(x=25, y=150)

    # 검색 버튼
    searchbutton = Button(windowReturnUser, text="검색", width=10, \
                          command=clickMemberSearch)

    datalist = []
    for i in range(len(df_member.index)):
        datalist.append(
            [df_member['Member_TEL'].iloc[i], df_member['Member_NAME'].iloc[i], df_member['Member_BIRTHDATE'].iloc[i],
             df_member['Member_GENDER'].iloc[i], df_member['Member_EMAIL'].iloc[i]])

    for j in range(len(datalist)):
        treeview.insert('', 'end', values=datalist[j])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)
    treeview.bind('<Double-Button-1>', member_info_return_dbclick)

# 반납 목록

def clickReturnBook():

    def clickReturn():
        try:
            selectedBook = treeview.focus()
            selectedISBN = treeview.set(selectedBook, column='1')
            selectedRent = treeview.set(selectedBook, column='5')
            if (selectedRent == "False"):
                messagebox.showinfo("반납실패", "이미 반납이 완료된 도서입니다.")
                windowReturnBook.destroy()
                raise
            selectedISBN = float(selectedISBN)
            selectedISBN = int(selectedISBN)

            # 반납 상태로 Book.csv 변경

            df_book["BOOK_RENT"].loc[selectedISBN] = False
            df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')

            messagebox.showinfo("반납", "도서를 반납합니다.")

            # rent.csv 파일 반납 여부 변경
            df_rent["RENT_YN"].loc[selectedISBN] = False
            df_rent.to_csv('RENT.csv', index=False, encoding='utf-8-sig')
            windowReturnBook.destroy()
        except:
            pass

    windowReturnBook = Tk()
    windowReturnBook.geometry("650x400")
    windowReturnBook.title("도서 반납")
    windowReturnBook.configure(bg='LightSkyBlue1')

    labelBookName = Label(windowReturnBook, text="회원명 :", bg='LightSkyBlue1')
    InputBookName = Entry(windowReturnBook, width=30)

    InputBookName.insert(0, name )
    InputBookName.place(x=100, y=25)
    InputBookName.config(state= 'disabled')
    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    # 반납 버튼
    returnbutton = Button(windowReturnBook, text="반납", width=10, \
                          command=clickReturn)

    treeview = tkinter.ttk.Treeview(windowReturnBook, \
                                    columns=["1", "2", "3", "4", "5", \
                                             ], show='headings' , height = 12)
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("1", text="ISBN", anchor="center")

    treeview.column("#2", width=80, anchor="center")
    treeview.heading("2", text="도서명", anchor="center")

    treeview.column("#3", width=100, anchor="center")
    treeview.heading("3", text="대여일", anchor="center")

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("4", text="반납예정일", anchor="center")

    treeview.column("#5", width=100, anchor="center")
    treeview.heading("5", text="대여여부", anchor="center")

    treeview.place(x=25, y=100)
    returnbutton.place(x=550, y=335)

    # 책 데이터 , 반납 데이터
    df_book = pd.read_csv("Book.csv", encoding='utf-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    df_rent = pd.read_csv("RENT.csv", encoding='utf-8-sig')
    df_rent = df_rent.set_index(df_rent['BOOK_ISBN'])

    # 대여 상태인 도서 데이터만 표로 출력

    can = []
    df_rent_can = df_rent.loc[df_rent['USER_PHONE'] == Tel]
    for i in range(len(df_rent_can.index)):
        can.append([ \
                    df_rent_can['BOOK_ISBN'].iloc[i], \
                    df_rent_can['BOOK_TITLE'].iloc[i], \
                    df_rent_can['RENT_DATE'].iloc[i], \
                    df_rent_can['RENT_RETURN_DATE'].iloc[i], \
                    df_rent_can['RENT_YN'].iloc[i]])

    for i in range(len(can)):
        treeview.insert('', 'end', values=can[i])

# -- 반납 끝

