from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tk

# 버튼 눌렀을 때 나오는 메세지 박스 코드 
def clickSearch():
    messagebox.showinfo("검색", "검색합니다.")

def find_book():
    messagebox.showinfo("중복", "검색합니다.")

def find_book2():
    messagebox.showinfo("이미지", "찾기")

def photo_fix_btn():
    messagebox.showinfo("이미지변경", "변경완료")

def fix_btn():
    messagebox.showinfo("수정", "수정완료")

def fix2_btn():
    messagebox.showinfo("삭제", "삭제완료")
    


# 새 책 추가  
def Book_add():
    newWindow = Tk()
    newWindow.title('새 책 추가')
    newWindow.geometry('450x250')
    newWindow.configure(bg='LightSkyBlue1')

# 책 추가 창의 정보를 입력하는 레이블 / 위치 및 설정    
    Label(newWindow, text='ISBN : ', bg='LightSkyBlue1').place(x=20, y=10)
    Button(newWindow,text='중복확인',command=find_book,width=10,height=1, bg='LightSkyBlue1').place(x=260, y=8)

    Label(newWindow, text='도서명 : ', bg='LightSkyBlue1').place(x=20, y=40)
    Label(newWindow, text='저자 : ', bg='LightSkyBlue1').place(x=20, y=70)
    Label(newWindow, text='출판사 : '  , bg='LightSkyBlue1').place(x=20, y=100)
    Label(newWindow, text='가격 : ', bg='LightSkyBlue1').place(x=20, y=130)
    Label(newWindow, text='정보페이지 URL : ', bg='LightSkyBlue1').place(x=20, y=160)
    Label(newWindow, text='도서 사진 : ', bg='LightSkyBlue1').place(x=20, y=190)
    Label(newWindow, text='도서 설명 : ', bg='LightSkyBlue1').place(x=20, y=220)
    Button(newWindow,text='찾기',command=find_book2,width=8,height=1, bg='LightSkyBlue1').place(x=300, y=190)

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
    
    searchBook = Tk()
    searchBook.geometry("600x400")
    searchBook.title("도서 검색")

    #검색 기능 레이블 및 버튼 처리 
    labelBookName = Label(searchBook, text="도서명 :")
    labelAuthor = Label(searchBook, text="저자 :")
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

    #도서정보 표시할 리스트박스
    resultbox = Listbox(searchBook, width=72, height=10, selectmode='single')
    resultbox.insert(0, '사진')
    resultbox.bind('<Double-Button-1>', bookfix_info_dbclick)
    resultbox.place(x=25, y=172)
    
    # 검색한 책 정보 레이블 
    labelPhoto = Label(searchBook, text="사진", bg='blue', fg='white', \
                       width=15)
    labelISBN = Label(searchBook, text="ISBN", bg='blue', fg='white', \
                      width=15)
    labelBookNameb = Label(searchBook, text="도서명", bg='blue', fg='white', \
                           width=15)
    labelAuthor = Label(searchBook, text="저자", bg='blue', fg='white', \
                             width=10)
    labelPrice = Label(searchBook, text="가격", bg='blue', fg='white', \
                       width=15)
    labelURL = Label(searchBook, text="URL", bg='blue', fg='white', \
                     width=10)
    labelCan = Label(searchBook, text="대여여부", bg='blue', fg='white', \
                     width=15)

    # 책 정보 레이블 위치 설정 
    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    labelPhoto.pack()
    labelPhoto.place(x=25, y=100)

    labelISBN.pack()
    labelISBN.place(x=125, y=100)
   
           
    labelBookNameb.pack()
    labelBookNameb.place(x=225, y=100)

    
    labelAuthor.pack()
    labelAuthor.place(x=325, y=100)

    
    labelPrice.pack()
    labelPrice.place(x=400, y=100)

    
    labelURL.pack()
    labelURL.place(x=510, y=100)

    
    labelCan.pack()
    labelCan.place(x=570, y=100)

#회원 정보 수정 및 삭제 

def bookfix_info():
    
    bookfix = Tk()
    bookfix.title('도서 정보 관리')
    bookfix.geometry('500x400')
    bookfix.configure(bg='LightSkyBlue1')

    ISBN=Label(bookfix, text='ISBN : ', bg='LightSkyBlue1')
    NAME=Label(bookfix, text='도서명 : ', bg='LightSkyBlue1')
    AUTHOR=Label(bookfix, text='저자 : ', bg='LightSkyBlue1')
    PUB=Label(bookfix, text='출판사 : '  , bg='LightSkyBlue1')
    PRICE=Label(bookfix, text='가격 : ', bg='LightSkyBlue1')
    URL=Label(bookfix, text='정보 URL : ', bg='LightSkyBlue1')    
    EX=Label(bookfix, text='도서 설명 : ', bg='LightSkyBlue1')
    PHOTO=Label(bookfix, width=20, height=12, relief='solid')

    
    ISBNinput=Label(bookfix, text='ISBN  ', width=20, bg='white', anchor='w')
    NAMEinput=Label(bookfix, text='도서명  ', width=20, bg='white', anchor='w')
    AUTHORinput=Label(bookfix, text='저자  ',width=20, bg='white', anchor='w')
    PUBinput=Label(bookfix, text='출판사  '  , width=20, bg='white', anchor='w')
    PRICEinput=Label(bookfix, text='가격  ', width=20, bg='white', anchor='w')
    URLinput=Label(bookfix, text='정보 URL  ', width=20, bg='white', anchor='w')   
    EXinput=Label(bookfix, text='도서 설명  ', width=20, bg='white', anchor='w')

    #레이블 위젯 위치 설정 
    ISBN.place(x=200,y=20)
    NAME.place(x=200,y=60)
    AUTHOR.place(x=200,y=100)
    PUB.place(x=200,y=140)
    PRICE.place(x=200,y=180)
    URL.place(x=200,y=220)   
    EX.place(x=200,y=260)
    PHOTO.place(x=20,y=20)

    # 레이블 위젯 위치 설정
    ISBNinput.place(x=290,y=20)
    NAMEinput.place(x=290,y=60)
    AUTHORinput.place(x=290,y=100)
    PUBinput.place(x=290,y=140)
    PRICEinput.place(x=290,y=180)
    URLinput.place(x=290,y=220)   
    EXinput.place(x=290,y=260)
  

    
    fixphotob= Button(bookfix,text='이미지 변경',command=photo_fix_btn)
    fixb= Button(bookfix,text='수정',command=fix_btn)
    delb= Button(bookfix,text='삭제',command=fix2_btn)

    fixphotob.place(x=55, y=220)
    fixb.place(x=180, y=350)
    delb.place(x=260, y=350)

    


# 더블클릭하면 나오는 창 함수 호출 
def bookfix_info_dbclick(event) :
    bookfix_info()   



# 메인 UI
def main_UI():
    window = Tk()
    window.title('도서관리 프로그램')
    window.geometry('800x600')
    window.configure(bg='LightSkyBlue1')

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    MemberMenu = Menu(mainMenu)
    MemberMenu = Menu(mainMenu)
    MemberMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = '회원관리' , menu = MemberMenu)
    MemberMenu.add_command(label = '회원정보')
    MemberMenu.add_command(label='회원등록')
    MemberMenu.add_command(label='회원정보수정')
    MemberMenu.add_command(label='회원탈퇴')
    MemberMenu.add_command(label='탈퇴회원확인')

# 책 수정 및 삭제는 검색후에 해야하므로 커맨드 통일함
    BookMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서관리', menu=BookMenu)
    BookMenu.add_command(label='새도서추가', command=Book_add)
    BookMenu.add_command(label='책정보조회', command=Book_search)
    BookMenu.add_command(label='책정보수정', command=Book_search)
    BookMenu.add_command(label='책정보삭제', command=Book_search)

    RentMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서대여', menu=RentMenu)
    RentMenu.add_command(label='도서대여')
    RentMenu.add_command(label='도서반납')

    SettingMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='환경설정',menu=SettingMenu)
    SettingMenu.add_command(label='실험') 
    SettingMenu.add_command(label='종료')

    window.mainloop()


main_UI()
