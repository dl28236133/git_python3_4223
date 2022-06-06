from tkinter import *
from tkinter import messagebox
import pandas as pd
from functools import partial
import tkinter.ttk
import webbrowser
import os
import math
from tkinter.filedialog import *
import shutil
from PIL import ImageTk,Image

#--도서 시작

#BOOK_ISBN,BOOK_TITLE,BOOK_AUTHOR,BOOK_PUB,BOOK_PRICE,BOOK_LINK,BOOK_IMAGE,BOOK_EX,BOOK_RENT
def book_csv():
    try:
        df_book = pd.read_csv('Book.csv', encoding='UTF-8-sig')
    except:
        df_book = pd.DataFrame(
            columns=['BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR', 'BOOK_PUB', 'BOOK_PRICE', 'BOOK_LINK',
                     'BOOK_IMAGE', 'BOOK_EX' , 'BOOK_RENT'])
        df_book.to_csv('Book.csv', index=False, encoding='UTF-8-sig')

# 버튼 눌렀을 때 나오는 메세지 박스 코드


def find_book():
    messagebox.showinfo("중복", "검색합니다.")

def find_book2():
    messagebox.showinfo("이미지", "찾기")


def photo_fix_btn():
    messagebox.showinfo("이미지변경", "파일 탐색기 실행")

def fix_btn():
    messagebox.showinfo("수정", "수정완료")

def fix2_btn():
    messagebox.showinfo("삭제", "삭제완료")

# 새 책 추가
def Book_add():
    def image_btn():
        imagename = askopenfilename(parent=newWindow, initialdir="image",
                                    filetypes=(("png 파일", "*.png"), ("gif 파일", "*.gif"), ("모든 파일", "*.*")))
        imagename_onlyfilename = 'image/' + os.path.basename(imagename)
        shutil.copyfile(imagename, imagename_onlyfilename)
        entry7.delete(0, 'end')
        entry7.insert(0, imagename_onlyfilename)


    def add_book():
        # csv 불러오기
        messagebox.showinfo("도서 추가", "추가")

        new_book = { 'BOOK_ISBN' : entry1.get(),
                     'BOOK_TITLE' : entry2.get(),
                     'BOOK_AUTHOR' : entry3.get(),
                     'BOOK_PUB' : entry4.get(),
                     'BOOK_PRICE' : entry5.get(),
                     'BOOK_LINK' : entry6.get(),
                     "BOOK_IMAGE" : entry7.get(),
                     "BOOK_EX" : entry8.get(),
                     "BOOK_RENT" : False
        }
        df_book = pd.read_csv("Book.csv", encoding='UTF-8-sig')
        df_book = df_book.set_index(df_book['BOOK_ISBN'])

        df_book = df_book.append(new_book, ignore_index=True)
        df_book = df_book.set_index(df_book['BOOK_ISBN'])

        df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')

        newWindow.destroy()

    newWindow = Tk()
    newWindow.title('새 도서 추가')
    newWindow.geometry('450x250')
    newWindow.configure(bg='LightSkyBlue1')

    # 책 추가 창의 정보를 입력하는 레이블 / 위치 및 설정
    Label(newWindow, text='ISBN : ', bg='LightSkyBlue1').place(x=20, y=10)
    Button(newWindow, text='중복확인', command=find_book, width=10, height=1, bg='LightSkyBlue1').place(x=260, y=8)

    Label(newWindow, text='도서명 : ', bg='LightSkyBlue1').place(x=20, y=40)
    Label(newWindow, text='저자 : ', bg='LightSkyBlue1').place(x=20, y=70)
    Label(newWindow, text='출판사 : ', bg='LightSkyBlue1').place(x=20, y=100)
    Label(newWindow, text='가격 : ', bg='LightSkyBlue1').place(x=20, y=130)
    Label(newWindow, text='정보페이지 URL : ', bg='LightSkyBlue1').place(x=20, y=160)
    Label(newWindow, text='도서 사진 : ', bg='LightSkyBlue1').place(x=20, y=190)
    Label(newWindow, text='도서 설명 : ', bg='LightSkyBlue1').place(x=20, y=220)
    Button(newWindow, text='찾기', command=image_btn, width=8, height=1, bg='LightSkyBlue1').place(x=300, y=190)
    Button(newWindow, text='추가', command= add_book,
           width=8, height=1, bg='LightSkyBlue1').place(x=300, y=220)

    entry1 = Entry(newWindow, width=25)
    entry2 = Entry(newWindow, width=30)
    entry3 = Entry(newWindow, width=25)
    entry4 = Entry(newWindow, width=25)
    entry5 = Entry(newWindow, width=30)
    entry6 = Entry(newWindow, width=25)
    entry7 = Entry(newWindow, width=25)
    entry8 = Entry(newWindow, width=25)

    entry1.place(x=65, y=10)
    entry2.place(x=75, y=40)
    entry3.place(x=60, y=70)
    entry4.place(x=75, y=100)
    entry5.place(x=60, y=130)
    entry6.place(x=120, y=160)
    entry7.place(x=85, y=190)
    entry8.place(x=85, y=220)


# 책 정보 조회
def Book_search():
    # 불러오기
    df_book = pd.read_csv("Book.csv", encoding='UTF-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    def clickSearch():
        for row in treeview.get_children():
            treeview.delete(row)

        BookName = InputBookName.get()
        AuthorName = InputAuthor.get()

        Namelist = list(df_book['BOOK_TITLE'])
        Autlist = list(df_book['BOOK_AUTHOR'])
        """
        if BookName != '':
            BookName = [ i for i in Namelist if BookName in i]
        if AuthorName != '':
            AuthorName = [s for s in Autlist if AuthorName in s]
        """

        if (BookName in Namelist or AuthorName in Autlist) or (BookName in Namelist and AuthorName == '') or (
                BookName == '' and AuthorName in Autlist):
            datalist = []
            if AuthorName == '':
                df_search = df_book.loc[df_book['BOOK_TITLE'] == BookName]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                     df_search['BOOK_AUTHOR'].iloc[i],
                                     df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                     df_search['BOOK_LINK'].iloc[i]])

            else:
                df_search = df_book.loc[df_book['BOOK_AUTHOR'] == AuthorName]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                     df_search['BOOK_AUTHOR'].iloc[i],
                                     df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                     df_search['BOOK_LINK'].iloc[i]])
            treeview.place(x=25, y=100)
            for j in range(len(datalist)):
                treeview.insert('', 'end', text = i , values=datalist[j])

        else:
            messagebox.showinfo("오류", "잘못된 책이름 또는 저자명입니다.")
        treeview.bind('<Double-Button-1>', bookfix_info_dbclick)


    def bookfix_info_dbclick(event):

        setISBN = treeview.focus()

        B_ISBN = (treeview.set(setISBN, column='1'))
        B_ISBN = int(B_ISBN)

        global imagefilename
        imagefilename = df_book['BOOK_IMAGE'].loc[B_ISBN]

        bookfix = Tk()
        bookfix.title('도서 정보 관리')
        bookfix.geometry('500x400')
        bookfix.configure(bg='LightSkyBlue1')

        ISBN = Label(bookfix, text='ISBN : ', bg='LightSkyBlue1')
        NAME = Label(bookfix, text='도서명 : ', bg='LightSkyBlue1')
        AUTHOR = Label(bookfix, text='저자 : ', bg='LightSkyBlue1')
        PUB = Label(bookfix, text='출판사 : ', bg='LightSkyBlue1')
        PRICE = Label(bookfix, text='가격 : ', bg='LightSkyBlue1')
        URL = Label(bookfix, text='대여 여부 : ', bg='LightSkyBlue1')
        EX = Label(bookfix, text='도서 설명 : ', bg='LightSkyBlue1')
        B_RENT = Label(bookfix, text='대여 여부 : ', bg='LightSkyBlue1')

        img = Image.open(df_book["BOOK_IMAGE"].loc[B_ISBN])
        img = img.resize((140,200) , Image.ANTIALIAS )
        print(df_book["BOOK_IMAGE"].loc[B_ISBN])
        image = ImageTk.PhotoImage(img, master = bookfix)
        PHOTO = Label(bookfix, image = image ,width = 140 )
        PHOTO.pack()


        ISBNinput = Label(bookfix, text=df_book["BOOK_ISBN"].loc[B_ISBN], width=20, bg='white', anchor='w')
        NAMEinput = Label(bookfix, text=df_book["BOOK_TITLE"].loc[B_ISBN], width=20, bg='white', anchor='w')
        AUTHORinput = Label(bookfix, text=df_book["BOOK_AUTHOR"].loc[B_ISBN], width=20, bg='white', anchor='w')
        PUBinput = Label(bookfix, text=df_book["BOOK_PUB"].loc[B_ISBN], width=20, bg='white', anchor='w')
        PRICEinput = Label(bookfix, text=df_book["BOOK_PRICE"].loc[B_ISBN], width=20, bg='white', anchor='w')
        URLinput = Label(bookfix, text=df_book["BOOK_RENT"].loc[B_ISBN], width=20, bg='white', anchor='w')
        EXinput = Label(bookfix, text=df_book["BOOK_EX"].loc[B_ISBN], width=20, bg='white', anchor='w')
        B_RENTinput = Label(bookfix, text=df_book["BOOK_RENT"].loc[B_ISBN], width=20, bg='white', anchor='w')

        # 레이블 위젯 위치 설정
        ISBN.place(x=200, y=20)
        NAME.place(x=200, y=60)
        AUTHOR.place(x=200, y=100)
        PUB.place(x=200, y=140)
        PRICE.place(x=200, y=180)
        URL.place(x=200, y=220)
        EX.place(x=200, y=260)
        PHOTO.place(x=20, y=20)
        B_RENT.place(x=200, y=300)

        # 레이블 위젯 위치 설정
        ISBNinput.place(x=290, y=20)
        NAMEinput.place(x=290, y=60)
        AUTHORinput.place(x=290, y=100)
        PUBinput.place(x=290, y=140)
        PRICEinput.place(x=290, y=180)
        URLinput.place(x=290, y=220)
        EXinput.place(x=290, y=260)
        B_RENTinput.place(x=290, y=300)

        #url 하이퍼링크
        def callback(url):
            webbrowser.open_new(url)
        URLinput.bind("<Button-1>", lambda e: callback(URLinput.cget('text')))

        Backb = Button(bookfix, text='닫기', command=bookfix.destroy)

        Backb.place(x=260, y=350)


    searchBook = Tk()
    searchBook.geometry("850x400")
    searchBook.title("도서 검색")
    searchBook.configure(bg = 'LightSkyBlue1')

    # 검색 기능 레이블 및 버튼 처리
    labelBookName = Label(searchBook, text="도서명 :" , bg = 'LightSkyBlue1')
    labelAuthor = Label(searchBook, text="저자 :", bg = 'LightSkyBlue1')
    InputBookName = Entry(searchBook, width=30)
    InputBookName.pack()
    InputBookName.place(x=100, y=25)


    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    buttonSearch = Button(searchBook, text="검색", command=clickSearch)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)

    labelAuthor.pack()
    labelAuthor.place(x=25, y=50)

    InputAuthor = Entry(searchBook, width=30)
    InputAuthor.pack()
    InputAuthor.place(x=100, y=50)


    treeview = tkinter.ttk.Treeview(searchBook, columns=["1", "2", "3", "4", "5", "6"])
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=80, )
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
    treeview.heading("6", text="대여여부", anchor="center")

    # 표에 삽입될 데이터
    treelist = []
    for i in range(len(df_book)):
        treelist.append( (df_book["BOOK_ISBN"].iloc[i], df_book["BOOK_TITLE"].iloc[i],
                          df_book["BOOK_AUTHOR"].iloc[i], df_book["BOOK_PUB"].iloc[i],
                          df_book["BOOK_PRICE"].iloc[i], df_book["BOOK_RENT"].iloc[i], ) )


    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

    treeview.place(x=25, y=100)
    treeview.bind('<Double-Button-1>', bookfix_info_dbclick)


# 도서 정보 수정
def bookfix_info():
    df_book = pd.read_csv("Book.csv", encoding='UTF-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    #수정- 검색
    def clickSearch():
        for row in treeview.get_children():
            treeview.delete(row)

        BookName = InputBookName.get()
        AuthorName = InputAuthor.get()

        Namelist = list(df_book['BOOK_TITLE'])
        Autlist = list(df_book['BOOK_AUTHOR'])

        if (BookName in Namelist and AuthorName in Autlist) or (BookName in Namelist and AuthorName == '') or (
                BookName == '' and AuthorName in Autlist):

            datalist = []
            if AuthorName == '':
                df_search = df_book.loc[df_book['BOOK_TITLE'] == BookName]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                     df_search['BOOK_AUTHOR'].iloc[i],
                                     df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                     df_search['BOOK_LINK'].iloc[i]])

            else:
                df_search = df_book.loc[df_book['BOOK_AUTHOR'] == AuthorName]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                     df_search['BOOK_AUTHOR'].iloc[i],
                                     df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                     df_search['BOOK_LINK'].iloc[i]])
            treeview.place(x=25, y=100)
            for j in range(len(datalist)):
                treeview.insert('', 'end', text=i, values=datalist[j])

        else:
            messagebox.showinfo("오류", "잘못된 책이름 또는 저자명입니다.")
        treeview.bind('<Double-Button-1>', bookfix_info_dbclick1)

    #수정- 상세정보
    def bookfix_info_dbclick1(event):

        #수정 부분
        def clickFix():

            df_book["BOOK_ISBN"].loc[B_ISBN] = ISBNinput.get()
            df_book["BOOK_TITLE"].loc[B_ISBN] = NAMEinput.get()
            df_book["BOOK_AUTHOR"].loc[B_ISBN] = AUTHORinput.get()
            df_book["BOOK_PUB"].loc[B_ISBN] = PUBinput.get()
            df_book["BOOK_PRICE"].loc[B_ISBN] = PRICEinput.get()
            df_book["BOOK_LINK"].loc[B_ISBN] = URLinput.get()
            df_book["BOOK_EX"].loc[B_ISBN] = EXinput.get()

            df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')

            messagebox.showinfo("수정","수정되었습니다.")
            bookfix.destroy()
            searchBook.destroy()

        setISBN = treeview.focus()

        B_ISBN = (treeview.set(setISBN, column='1'))
        B_ISBN = int(B_ISBN)

        global imagefilename
        imagefilename = df_book['BOOK_IMAGE'].loc[B_ISBN]

        bookfix = Tk()
        bookfix.title('도서 정보 관리')
        bookfix.geometry('500x400')
        bookfix.configure(bg='LightSkyBlue1')

        ISBN = Label(bookfix, text='ISBN : ', bg='LightSkyBlue1')
        NAME = Label(bookfix, text='도서명 : ', bg='LightSkyBlue1')
        AUTHOR = Label(bookfix, text='저자 : ', bg='LightSkyBlue1')
        PUB = Label(bookfix, text='출판사 : ', bg='LightSkyBlue1')
        PRICE = Label(bookfix, text='가격 : ', bg='LightSkyBlue1')
        URL = Label(bookfix, text='정보 URL : ', bg='LightSkyBlue1')
        EX = Label(bookfix, text='도서 설명 : ', bg='LightSkyBlue1')
        B_RENT = Label(bookfix, text='대여 여부 : ', bg='LightSkyBlue1')
        PHOTO = Label(bookfix, width=20, height=12, relief='solid')

        ISBNinput = Entry(bookfix)
        ISBNinput.insert(0 , df_book["BOOK_ISBN"].loc[B_ISBN])
        NAMEinput = Entry(bookfix)
        NAMEinput.insert(0, df_book["BOOK_TITLE"].loc[B_ISBN])
        AUTHORinput = Entry(bookfix)
        AUTHORinput.insert(0, df_book["BOOK_AUTHOR"].loc[B_ISBN])
        PUBinput = Entry(bookfix)
        PUBinput.insert(0, df_book["BOOK_PUB"].loc[B_ISBN])
        PRICEinput = Entry(bookfix)
        PRICEinput.insert(0, df_book["BOOK_PRICE"].loc[B_ISBN])
        URLinput = Entry(bookfix)
        URLinput.insert(0, df_book["BOOK_LINK"].loc[B_ISBN])
        EXinput = Entry(bookfix)
        EXinput.insert(0, df_book["BOOK_EX"].loc[B_ISBN])
        B_RENTinput = Entry(bookfix)
        B_RENTinput.insert(0, df_book["BOOK_RENT"].loc[B_ISBN])

        # 레이블 위젯 위치 설정
        ISBN.place(x=200, y=20)
        NAME.place(x=200, y=60)
        AUTHOR.place(x=200, y=100)
        PUB.place(x=200, y=140)
        PRICE.place(x=200, y=180)
        URL.place(x=200, y=220)
        EX.place(x=200, y=260)
        PHOTO.place(x=20, y=20)
        B_RENT.place(x=200, y=300)

        # 레이블 위젯 위치 설정
        ISBNinput.place(x=290, y=20)
        NAMEinput.place(x=290, y=60)
        AUTHORinput.place(x=290, y=100)
        PUBinput.place(x=290, y=140)
        PRICEinput.place(x=290, y=180)
        URLinput.place(x=290, y=220)
        EXinput.place(x=290, y=260)
        B_RENTinput.place(x=290, y=300)


        fixphotob = Button(bookfix, text='이미지 변경', command=photo_fix_btn)
        fixbutton = Button(bookfix, text='수정', command=clickFix)
        Backb = Button(bookfix, text='닫기', command=bookfix.destroy)

        fixphotob.place(x=55, y=220)
        fixbutton.place(x=200, y=350)
        Backb.place(x=260, y=350)

    searchBook = Tk()
    searchBook.geometry("850x400")
    searchBook.title("도서 검색")
    searchBook.configure(bg='LightSkyBlue1')

    # 검색 기능 레이블 및 버튼 처리
    labelBookName = Label(searchBook, text="도서명 :", bg='LightSkyBlue1')
    labelAuthor = Label(searchBook, text="저자 :", bg='LightSkyBlue1')
    InputBookName = Entry(searchBook, width=30)
    InputBookName.pack()
    InputBookName.place(x=100, y=25)

    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    buttonSearch = Button(searchBook, text="검색", command=clickSearch)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)

    labelAuthor.pack()
    labelAuthor.place(x=25, y=50)

    InputAuthor = Entry(searchBook, width=30)
    InputAuthor.pack()
    InputAuthor.place(x=100, y=50)

    treeview = tkinter.ttk.Treeview(searchBook, columns=["1", "2", "3", "4", "5", "6"])
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

    # 표에 삽입될 데이터
    treelist = []
    for i in range(len(df_book)):
        treelist.append((df_book["BOOK_ISBN"].iloc[i], df_book["BOOK_TITLE"].iloc[i],
                         df_book["BOOK_AUTHOR"].iloc[i], df_book["BOOK_PUB"].iloc[i],
                         df_book["BOOK_PRICE"].iloc[i], df_book["BOOK_RENT"].iloc[i],))

    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

    treeview.place(x=25, y=100)
    treeview.bind('<Double-Button-1>', bookfix_info_dbclick1)


#도서 정보 삭제

def bookdel_info():
    df_book = pd.read_csv("Book.csv", encoding='UTF-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    def clickSearch():
        for row in treeview.get_children():
            treeview.delete(row)

        BookName = InputBookName.get()
        AuthorName = InputAuthor.get()

        Namelist = list(df_book['BOOK_TITLE'])
        Autlist = list(df_book['BOOK_AUTHOR'])

        if (BookName in Namelist and AuthorName in Autlist) or (BookName in Namelist and AuthorName == '') or (
                BookName == '' and AuthorName in Autlist):

            datalist = []
            if AuthorName == '':
                df_search = df_book.loc[df_book['BOOK_TITLE'] == BookName]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                     df_search['BOOK_AUTHOR'].iloc[i],
                                     df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                     df_search['BOOK_LINK'].iloc[i]])

            else:
                df_search = df_book.loc[df_book['BOOK_AUTHOR'] == AuthorName]
                for i in range(len(df_search.index)):
                    datalist.append([df_search['BOOK_ISBN'].iloc[i], df_search['BOOK_TITLE'].iloc[i],
                                     df_search['BOOK_AUTHOR'].iloc[i],
                                     df_search['BOOK_PUB'].iloc[i], df_search['BOOK_PRICE'].iloc[i],
                                     df_search['BOOK_LINK'].iloc[i]])
            treeview.place(x=25, y=100)
            for j in range(len(datalist)):
                treeview.insert('', 'end', text=i, values=datalist[j])

        else:
            messagebox.showinfo("오류", "잘못된 책이름 또는 저자명입니다.")
        treeview.bind('<Double-Button-1>', bookfix_info_dbclick2)

    def bookfix_info_dbclick2(event):
        def bookdel():
            del_index = df_book[df_book['BOOK_ISBN'] == B_ISBN].index
            df_book.drop(del_index, inplace=True)

            df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')


            messagebox.showinfo("삭제", "삭제되었습니다.")
            bookfix.destroy()
            searchBook.destroy()


        setISBN = treeview.focus()

        B_ISBN = (treeview.set(setISBN, column='1'))
        B_ISBN = int(B_ISBN)

        global imagefilename
        imagefilename = df_book['BOOK_IMAGE'].loc[B_ISBN]

        bookfix = Tk()
        bookfix.title('도서 정보 관리')
        bookfix.geometry('500x400')
        bookfix.configure(bg='LightSkyBlue1')

        ISBN = Label(bookfix, text='ISBN : ', bg='LightSkyBlue1')
        NAME = Label(bookfix, text='도서명 : ', bg='LightSkyBlue1')
        AUTHOR = Label(bookfix, text='저자 : ', bg='LightSkyBlue1')
        PUB = Label(bookfix, text='출판사 : ', bg='LightSkyBlue1')
        PRICE = Label(bookfix, text='가격 : ', bg='LightSkyBlue1')
        URL = Label(bookfix, text='대여 여부 : ', bg='LightSkyBlue1')
        EX = Label(bookfix, text='도서 설명 : ', bg='LightSkyBlue1')
        B_RENT = Label(bookfix, text='대여 여부 : ', bg='LightSkyBlue1')
        PHOTO = Label(bookfix, width=20, height=12, relief='solid')

        ISBNinput = Label(bookfix, text=df_book["BOOK_ISBN"].loc[B_ISBN], width=20, bg='white', anchor='w')
        NAMEinput = Label(bookfix, text=df_book["BOOK_TITLE"].loc[B_ISBN], width=20, bg='white', anchor='w')
        AUTHORinput = Label(bookfix, text=df_book["BOOK_AUTHOR"].loc[B_ISBN], width=20, bg='white', anchor='w')
        PUBinput = Label(bookfix, text=df_book["BOOK_PUB"].loc[B_ISBN], width=20, bg='white', anchor='w')
        PRICEinput = Label(bookfix, text=df_book["BOOK_PRICE"].loc[B_ISBN], width=20, bg='white', anchor='w')
        URLinput = Label(bookfix, text=df_book["BOOK_RENT"].loc[B_ISBN], width=20, bg='white', anchor='w')
        EXinput = Label(bookfix, text=df_book["BOOK_EX"].loc[B_ISBN], width=20, bg='white', anchor='w')
        B_RENTinput = Label(bookfix, text=df_book["BOOK_RENT"].loc[B_ISBN], width=20, bg='white', anchor='w')

        # 레이블 위젯 위치 설정
        ISBN.place(x=200, y=20)
        NAME.place(x=200, y=60)
        AUTHOR.place(x=200, y=100)
        PUB.place(x=200, y=140)
        PRICE.place(x=200, y=180)
        URL.place(x=200, y=220)
        EX.place(x=200, y=260)
        PHOTO.place(x=20, y=20)
        B_RENT.place(x=200, y = 300)

        # 레이블 위젯 위치 설정
        ISBNinput.place(x=290, y=20)
        NAMEinput.place(x=290, y=60)
        AUTHORinput.place(x=290, y=100)
        PUBinput.place(x=290, y=140)
        PRICEinput.place(x=290, y=180)
        URLinput.place(x=290, y=220)
        EXinput.place(x=290, y=260)
        B_RENTinput.place(x=290, y=300)

        fixphotob = Button(bookfix, text='이미지 변경', command=photo_fix_btn)
        Backf = Button(bookfix, text='삭제', command=bookdel)
        Backb = Button(bookfix, text='닫기', command=bookfix.destroy)

        fixphotob.place(x=55, y=220)
        Backf.place(x=200, y=350)
        Backb.place(x=260, y=350)



    searchBook = Tk()
    searchBook.geometry("850x400")
    searchBook.title("도서 검색")
    searchBook.configure(bg='LightSkyBlue1')

    # 검색 기능 레이블 및 버튼 처리
    labelBookName = Label(searchBook, text="도서명 :", bg='LightSkyBlue1')
    labelAuthor = Label(searchBook, text="저자 :", bg='LightSkyBlue1')
    InputBookName = Entry(searchBook, width=30)
    InputBookName.pack()
    InputBookName.place(x=100, y=25)

    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    buttonSearch = Button(searchBook, text="검색", command=clickSearch)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)

    labelAuthor.pack()
    labelAuthor.place(x=25, y=50)

    InputAuthor = Entry(searchBook, width=30)
    InputAuthor.pack()
    InputAuthor.place(x=100, y=50)

    treeview = tkinter.ttk.Treeview(searchBook, columns=["1", "2", "3", "4", "5", "6"])
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=80, )
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

    # 표에 삽입될 데이터
    treelist = []
    for i in range(len(df_book)):
        treelist.append((df_book["BOOK_ISBN"].iloc[i], df_book["BOOK_TITLE"].iloc[i],
                         df_book["BOOK_AUTHOR"].iloc[i], df_book["BOOK_PUB"].iloc[i],
                         df_book["BOOK_PRICE"].iloc[i], df_book["BOOK_RENT"].iloc[i],))

    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

    treeview.place(x=25, y=100)
    treeview.bind('<Double-Button-1>', bookfix_info_dbclick2)