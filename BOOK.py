from tkinter import *
from tkinter import messagebox
import pandas as pd
from functools import partial


#--도서 시작

# 버튼 눌렀을 때 나오는 메세지 박스 코드
def clickSearch():
    messagebox.showinfo("검색", "검색합니다.")

def find_book():
    messagebox.showinfo("중복", "검색합니다.")

def find_book2():
    messagebox.showinfo("이미지", "찾기")

def add_book(a):
    # csv 불러오기
    messagebox.showinfo("도서 추가", "추가")
"""
    new_book = { 'BOOK_ISBN' : a.entry1.get(),
                 'BOOK.TITLE' : a.entry2.get(),
                 'BOOK_AUTHOR' : a.entry3.get(),
                 'BOOK_PUB' : a.entry4.get(),
                 'BOOK_PRICE' : a.entry5.get(),
                 'BOOK_LINK' : a.entry6.get(),
                 "BOOK_IMAGE" : a.entry7.get(),
                 "BOOK_EX" : a.entry8.get()
    }
    df_book = pd.read_csv("Book.csv", encoding='UTF-8-sig')
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    df_book = df_book.append(new_book, ignore_index=True)
    df_book = df_book.set_index(df_book['BOOK_ISBN'])

    df_book.to_csv('Book.csv', index=False, encoding='utf-8-sig')
"""


def photo_fix_btn():
    messagebox.showinfo("이미지변경", "파일 탐색기 실행")

def fix_btn():
    messagebox.showinfo("수정", "수정완료")

def fix2_btn():
    messagebox.showinfo("삭제", "삭제완료")

# 새 책 추가
def Book_add():
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
    Button(newWindow, text='찾기', command=find_book2, width=8, height=1, bg='LightSkyBlue1').place(x=300, y=190)

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


    Button(newWindow, text='추가', command= partial(add_book, newWindow),
           width=8, height=1, bg='LightSkyBlue1').place(x=300, y=220)


# 책 정보 조회
def Book_search():
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
    InputBookName.insert(0, "도서명을 입력하세요.")

    buttonSearch = Button(searchBook, text="검색", command=clickSearch)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)

    labelAuthor.pack()
    labelAuthor.place(x=25, y=50)

    InputAuthor = Entry(searchBook, width=30)
    InputAuthor.pack()
    InputAuthor.place(x=100, y=50)
    InputAuthor.insert(0, "저자명을 입력하세요.")

    # 도서정보 표시할 리스트박스
    resultbox = Listbox(searchBook, width=112, height=13, selectmode='single')
    resultbox.insert(0, '사진')
    resultbox.bind('<Double-Button-1>', bookfix_info_dbclick)
    resultbox.place(x=25, y=120)

    # 검색한 책 정보 레이블
    labelPhoto = Label(searchBook, text="사진",  width=15)
    labelISBN = Label(searchBook, text="ISBN",   width=15)
    labelBookNameb = Label(searchBook, text="도서명",  width=15)
    labelAuthor = Label(searchBook, text="저자",  width=15)
    labelPUB = Label(searchBook, text="출판사",  width=15)
    labelPrice = Label(searchBook, text="가격",  width=15)
    labelURL = Label(searchBook, text="URL",  width=10)
    labelCan = Label(searchBook, text="대여여부", width=15)

    # 책 정보 레이블 위치 설정
    labelBookName.pack()
    labelPhoto.pack()
    labelISBN.pack()
    labelBookNameb.pack()
    labelAuthor.pack()
    labelPUB.pack()
    labelPrice.pack()
    labelURL.pack()
    labelCan.pack()

    labelBookName.place(x=25, y=25)
    labelPhoto.place(x=25, y=100)
    labelISBN.place(x=125, y=100)
    labelBookNameb.place(x=225, y=100)
    labelAuthor.place(x=325, y=100)
    labelPUB.place(x=425, y=100)
    labelPrice.place(x=525, y=100)
    labelURL.place(x=625, y=100)
    labelCan.place(x=700, y=100)

# 회원 정보 수정 및 삭제
def bookfix_info():
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
    PHOTO = Label(bookfix, width=20, height=12, relief='solid')

    ISBNinput = Label(bookfix, text='ISBN  ', width=20, bg='white', anchor='w')
    NAMEinput = Label(bookfix, text='도서명  ', width=20, bg='white', anchor='w')
    AUTHORinput = Label(bookfix, text='저자  ', width=20, bg='white', anchor='w')
    PUBinput = Label(bookfix, text='출판사  ', width=20, bg='white', anchor='w')
    PRICEinput = Label(bookfix, text='가격  ', width=20, bg='white', anchor='w')
    URLinput = Label(bookfix, text='정보 URL  ', width=20, bg='white', anchor='w')
    EXinput = Label(bookfix, text='도서 설명  ', width=20, bg='white', anchor='w')

    # 레이블 위젯 위치 설정
    ISBN.place(x=200, y=20)
    NAME.place(x=200, y=60)
    AUTHOR.place(x=200, y=100)
    PUB.place(x=200, y=140)
    PRICE.place(x=200, y=180)
    URL.place(x=200, y=220)
    EX.place(x=200, y=260)
    PHOTO.place(x=20, y=20)

    # 레이블 위젯 위치 설정
    ISBNinput.place(x=290, y=20)
    NAMEinput.place(x=290, y=60)
    AUTHORinput.place(x=290, y=100)
    PUBinput.place(x=290, y=140)
    PRICEinput.place(x=290, y=180)
    URLinput.place(x=290, y=220)
    EXinput.place(x=290, y=260)

    fixphotob = Button(bookfix, text='이미지 변경', command=photo_fix_btn)
    fixb = Button(bookfix, text='수정', command=fix_btn)
    delb = Button(bookfix, text='삭제', command=fix2_btn)

    fixphotob.place(x=55, y=220)
    fixb.place(x=180, y=350)
    delb.place(x=260, y=350)

# 더블클릭하면 나오는 창 함수 호출
def bookfix_info_dbclick(event):
    bookfix_info()