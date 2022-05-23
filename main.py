from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


#-- 대여시작
def clickSearch():
    messagebox.showinfo("검색", "검색합니다.")


def clickNext():
    messagebox.showinfo("다음", "다음으로 넘어갑니다.")


def clickRent():
    messagebox.showinfo("대여", "도서를 대여합니다.")


def clickReturn():
    messagebox.showinfo("반납", "도서를 반납합니다.")


def clickRentUser():
    # 회원검색 창 생성
    windowRentUser   = Tk()
    windowRentUser  .title('회원검색')
    windowRentUser  .geometry('600x400')
    windowRentUser  .configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(windowRentUser  , text='회원명' , bg='LightSkyBlue1')
    TELlabel = Label(windowRentUser   , text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(windowRentUser  , width=30)
    TELinput = Entry(windowRentUser  , width=30)

    # 회원정보 표시할 리스트박스
    resultbox = Listbox(windowRentUser  , width=72, height=10, selectmode='single')
    resultbox.insert(0, '회원이름')


    # 검색 버튼
    searchbutton = Button(windowRentUser  , text="검색", width=10, command=search_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성
    resultframe = Frame(windowRentUser  , relief='solid')
    resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    for i in range(5):
        resultlist[i] = Label(resultframe, text=resultlist[i])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

    resultframe.place(x=25, y=150)
    for result in resultlist:
        result.pack(side='left', padx=30)

    resultbox.place(x=25, y=172)
    buttonNext = Button(windowRentUser , text="다음", command=clickReturnBook)
    buttonNext.pack()
    buttonNext.place(x=490, y=300)



def clickRentBook():
    windowRentBook = Tk()
    windowRentBook.geometry("850x400")
    windowRentBook.title("도서 대여(도서 검색)")
    windowRentBook.configure(bg='LightSkyBlue1')

    labelBookName = Label(windowRentBook, text="도서명" , bg = 'LightSkyBlue1')
    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    InputBookName = Entry(windowRentBook, width=30)
    InputBookName.pack()
    InputBookName.place(x=100, y=25)
    InputBookName.insert(0, "도서명을 입력하세요.")

    buttonSearch = Button(windowRentBook, text="검색", command=clickSearch)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)

    labelWriterName = Label(windowRentBook, text="저자" , bg = 'LightSkyBlue1')
    labelWriterName.pack()
    labelWriterName.place(x=25, y=50)

    InputWriterName = Entry(windowRentBook, width=30)
    InputWriterName.pack()
    InputWriterName.place(x=100, y=50)
    InputWriterName.insert(0, "저자명을 입력하세요.")

    resultbox = Listbox(windowRentBook, width=112, height=13, selectmode='single')
    resultbox.insert(0, '사진')
    resultbox.place(x=25, y=120)


    labelPhoto = Label(windowRentBook, text="사진",  width=15)
    labelPhoto.pack()
    labelPhoto.place(x=25, y=100)

    labelISBN = Label(windowRentBook, text="ISBN",  width=15)
    labelISBN.pack()
    labelISBN.place(x=125, y=100)

    labelBookNameb = Label(windowRentBook, text="도서명",  width=15)
    labelBookNameb.pack()
    labelBookNameb.place(x=225, y=100)

    labelWriterNameb = Label(windowRentBook, text="저자",  width=15)
    labelWriterNameb.pack()
    labelWriterNameb.place(x=325, y=100)

    labelPUB = Label(windowRentBook, text= '출판사' ,  width=15)
    labelPUB.pack()
    labelPUB.place(x=425, y=100)

    labelPrice = Label(windowRentBook, text="가격",  width=15)
    labelPrice.pack()
    labelPrice.place(x=520, y=100)

    labelURL = Label(windowRentBook, text="URL",   width=10)
    labelURL.pack()
    labelURL.place(x=625, y=100)

    labelCan = Label(windowRentBook, text="대여여부",  width=15)
    labelCan.pack()
    labelCan.place(x=700, y=100)

    buttonRent = Button(windowRentBook, text="대여", command=clickRent)
    buttonRent.pack()
    buttonRent.place(x=750, y=300)



def clickReturnUser():
    # 회원검색 창 생성
    windowReturnUser  = Tk()
    windowReturnUser .title('회원검색')
    windowReturnUser .geometry('600x400')
    windowReturnUser .configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(windowReturnUser , text='회원명' , bg='LightSkyBlue1')
    TELlabel = Label(windowReturnUser , text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(windowReturnUser , width=30)
    TELinput = Entry(windowReturnUser , width=30)

    # 회원정보 표시할 리스트박스
    resultbox = Listbox(windowReturnUser , width=72, height=10, selectmode='single')
    resultbox.insert(0, '회원이름')


    # 검색 버튼
    searchbutton = Button(windowReturnUser , text="검색", width=10, command=search_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성
    resultframe = Frame(windowReturnUser , relief='solid')
    resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    for i in range(5):
        resultlist[i] = Label(resultframe, text=resultlist[i]  )

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

    resultframe.place(x=25, y=150)
    for result in resultlist:
        result.pack(side='left', padx=30 ,)

    resultbox.place(x=25, y=172)
    buttonNext = Button(windowReturnUser, text="다음", command=clickReturnBook)
    buttonNext.pack()
    buttonNext.place(x=490, y=300)

def clickReturnBook():
    windowReturnBook = Tk()
    windowReturnBook.geometry("850x400")
    windowReturnBook.title("도서 반납")
    windowReturnBook.configure(bg='LightSkyBlue1')

    labelUserName = Label(windowReturnBook, text="회원명" , bg = 'LightSkyBlue1')
    labelUserName.pack()
    labelUserName.place(x=25, y=25)

    InputUserName = Entry(windowReturnBook, width=30)
    InputUserName.pack()
    InputUserName.place(x=100, y=25)
    InputUserName.insert(0, "이름")

    resultbox = Listbox(windowReturnBook, width=112, height=13, selectmode='single')
    resultbox.insert(0, '사진')

    resultbox.place(x=25, y=120)

    labelPhoto = Label(windowReturnBook, text="사진",  \
                       width=15)
    labelPhoto.pack()
    labelPhoto.place(x=25, y=100)

    labelISBN = Label(windowReturnBook, text="ISBN",  \
                      width=15)
    labelISBN.pack()
    labelISBN.place(x=125, y=100)

    labelBookNameb = Label(windowReturnBook, text="도서명",  \
                           width=15)
    labelBookNameb.pack()
    labelBookNameb.place(x=225, y=100)

    labelWriterNameb = Label(windowReturnBook, text="저자",  \
                             width=15)
    labelWriterNameb.pack()
    labelWriterNameb.place(x=325, y=100)

    labelPUB = Label(windowReturnBook, text="출판사",  \
                             width=15)
    labelPUB.pack()
    labelPUB.place(x=425, y=100)

    labelPrice = Label(windowReturnBook, text="가격",  \
                       width=15)
    labelPrice.pack()
    labelPrice.place(x=525, y=100)

    labelURL = Label(windowReturnBook, text="URL",  \
                     width=10)
    labelURL.pack()
    labelURL.place(x=625, y=100)

    labelCan = Label(windowReturnBook, text="대여여부",  \
                     width=15)
    labelCan.pack()
    labelCan.place(x=700, y=100)

    buttonReturn = Button(windowReturnBook, text="반납", command=clickReturn)
    buttonReturn.pack()
    buttonReturn.place(x=750, y=300)


#-- 대여끝


#-- 회원시작

# 회원정보 - 회원검색창
def member_search():
    # 회원검색 창 생성
    memsearchwindow = Tk()
    memsearchwindow.title('회원검색')
    memsearchwindow.geometry('600x400')
    memsearchwindow.configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(memsearchwindow, text='회원명', bg='LightSkyBlue1')
    TELlabel = Label(memsearchwindow, text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(memsearchwindow, width=30)
    TELinput = Entry(memsearchwindow, width=30)

    # 회원정보 표시할 리스트박스
    resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    resultbox.insert(0, '회원이름')
    resultbox.bind('<Double-Button-1>', member_info_dbclick)

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=search_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성
    resultframe = Frame(memsearchwindow, relief='solid')
    resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    for i in range(5):
        resultlist[i] = Label(resultframe, text=resultlist[i])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

    resultframe.place(x=25, y=150)
    for result in resultlist:
        result.pack(side='left', padx=30)

    resultbox.place(x=25, y=172)


# 회원검색 - 검색 버튼 클릭 시
def search_btn():
    messagebox.showinfo("검색실행", "회원 검색을 실행함")


# 회원정보 리스트박스 회원 더블클릭시 이벤트
def member_info_dbclick(event):
    member_info()


# 회원검색 - 회원 선택 시 회원정보 창 출력
def member_info():
    # 회원정보 창 생성
    meminfowindow = Tk()
    meminfowindow.title('회원정보')
    meminfowindow.geometry('500x300')
    meminfowindow.configure(bg='LightSkyBlue1')

    # 회원정보 인덱스 표시할 레이블
    infonamelabel = Label(meminfowindow, text='회원명',  bg='LightSkyBlue1')
    infodatelabel = Label(meminfowindow, text='생년월일',  bg='LightSkyBlue1')
    infogenderlabel = Label(meminfowindow, text='성별',  bg='LightSkyBlue1')
    infoTELlabel = Label(meminfowindow, text='전화번호',  bg='LightSkyBlue1')
    infoemaillabel = Label(meminfowindow, text='이메일', bg='LightSkyBlue1')
    infophotolabel = Label(meminfowindow, width=20, height=12, relief='solid')

    # 회원정보(실제 회원 정보) 표시할 레이블
    infonameinput = Label(meminfowindow, text='회원명', width=25, bg='white', anchor='w')
    infodateinput = Label(meminfowindow, text='생년월일', width=25, bg='white', anchor='w')
    infogenderinput = Label(meminfowindow, text='성별', width=25, bg='white', anchor='w')
    infoTELinput = Label(meminfowindow, text='전화번호', width=25, bg='white', anchor='w')
    infoemailinput = Label(meminfowindow, text='이메일', width=25, bg='white', anchor='w')

    # 회원정보 창 닫기 버튼
    infoclosebutton = Button(meminfowindow, text='닫기', command=meminfowindow.destroy)

    # 레이블 위젯 위치 지정(회원정보 인덱스)
    infonamelabel.place(x=200, y=20)
    infodatelabel.place(x=200, y=60)
    infogenderlabel.place(x=200, y=100)
    infoTELlabel.place(x=200, y=140)
    infoemaillabel.place(x=200, y=180)
    infophotolabel.place(x=20, y=20)

    # 레이블 위젯 위치 지정(실제 회원 정보)
    infonameinput.place(x=290, y=20)
    infodateinput.place(x=290, y=60)
    infogenderinput.place(x=290, y=100)
    infoTELinput.place(x=290, y=140)
    infoemailinput.place(x=290, y=180)

    # 창 닫기 버튼 위치 지정
    infoclosebutton.place(x=440, y=250)


# 회원등록
def member_register():
    # 회원등록 창 생성
    memregiwindow = Tk()
    memregiwindow.title('회원등록')
    memregiwindow.geometry('400x300')
    memregiwindow.configure(bg='LightSkyBlue1')

    # 회원정보 인덱스 표시할 레이블
    reginamelabel = Label(memregiwindow, text='회원명', bg='LightSkyBlue1')
    regidatelabel = Label(memregiwindow, text='생년월일',  bg='LightSkyBlue1')
    regigenderlabel = Label(memregiwindow, text='성별',  bg='LightSkyBlue1')
    regiTELlabel = Label(memregiwindow, text='전화번호',  bg='LightSkyBlue1')
    regiemaillabel = Label(memregiwindow, text='이메일',  bg='LightSkyBlue1')
    regiphotolabel = Label(memregiwindow, text='사진',  bg='LightSkyBlue1')

    # 회원정보 입력받을 엔트리
    reginameinput = Entry(memregiwindow, width=25)
    regidateinput = Entry(memregiwindow, width=25)

    # 회원정보 중 성별을 입력받을 라디오버튼, 초기값은 '남'
    var = StringVar()
    regigenderinput1 = Radiobutton(memregiwindow, text='남', bg='white', value='남', variable=var)
    regigenderinput1.select()
    regigenderinput2 = Radiobutton(memregiwindow, text='여', bg='white', value='여', variable=var)

    # 회원정보 입력받을 엔트리
    regiTELinput = Entry(memregiwindow, width=25)
    regiemailinput = Entry(memregiwindow, width=25)
    regiphotoinput = Entry(memregiwindow, width=25)

    # 이미지 파일 등록할 '파일찾기', 회원등록 '등록', 창 닫기 '취소' 버튼
    imagebutton = Button(memregiwindow, text='파일찾기', command=image_btn)
    regibutton = Button(memregiwindow, text='등록', command=regi_btn)
    regicanclebutton = Button(memregiwindow, text='취소', command=memregiwindow.destroy)

    # 생성한 레이블 위젯 위치 지정
    reginamelabel.place(x=30, y=20)
    regidatelabel.place(x=30, y=60)
    regigenderlabel.place(x=30, y=100)
    regiTELlabel.place(x=30, y=140)
    regiemaillabel.place(x=30, y=180)
    regiphotolabel.place(x=30, y=220)

    # 생성한 엔트리 및 라디오버튼 위젯 위치 지정
    reginameinput.place(x=120, y=20)
    regidateinput.place(x=120, y=60)
    regigenderinput1.place(x=120, y=100)
    regigenderinput2.place(x=160, y=100)
    regiTELinput.place(x=120, y=140)
    regiemailinput.place(x=120, y=180)
    regiphotoinput.place(x=120, y=220)

    # 파일찾기, 등록, 취소 버튼 위치 지정
    imagebutton.place(x=310, y=220)
    regibutton.place(x=160, y=260)
    regicanclebutton.place(x=220, y=260)


# 회원등록 - 파일찾기 버튼 클릭 시
def image_btn():
    messagebox.showinfo("이미지 찾기", "탐색기로 이미지 파일 찾기")


# 회원등록 - 등록 버튼 클릭 시
def regi_btn():
    messagebox.showinfo("회원등록", "회원등록 기능")


# 회원정보수정 - 회원검색 창
def member_search_fix():
    # 회원검색(회원정보수정) 창 생성
    memsearchwindow = Tk()
    memsearchwindow.title('회원검색(회원정보수정)')
    memsearchwindow.geometry('600x400')
    memsearchwindow.configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(memsearchwindow, text='회원명',  bg='LightSkyBlue1')
    TELlabel = Label(memsearchwindow, text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(memsearchwindow, width=30)
    TELinput = Entry(memsearchwindow, width=30)

    # 회원정보 표시할 리스트박스
    resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    resultbox.insert(0, '회원이름')
    resultbox.bind('<Double-Button-1>', member_info_fix_dbclick)

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=search_fix_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성
    resultframe = Frame(memsearchwindow, relief='solid')
    resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    for i in range(5):
        resultlist[i] = Label(resultframe, text=resultlist[i])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

    resultframe.place(x=25, y=150)
    for result in resultlist:
        result.pack(side=LEFT, padx=30)

    resultbox.place(x=25, y=172)


# 회원정보수정 - 회원검색 - 검색 버튼 클릭
def search_fix_btn():
    messagebox.showinfo("검색실행", "회원 검색을 실행함")


# 회원정보수정 - 회원정보 리스트박스 회원 더블클릭시 이벤트
def member_info_fix_dbclick(event):
    member_info_fix()


# 회원정보수정 - 회원검색 - 회원정보(수정 버튼 존재)
def member_info_fix():
    # 회원정보(회원정보수정) 창 생성
    meminfowindow = Tk()
    meminfowindow.title('회원정보(회원정보수정)')
    meminfowindow.geometry('500x300')
    meminfowindow.configure(bg='LightSkyBlue1')

    # 회원정보 인덱스 표시할 레이블
    infonamelabel = Label(meminfowindow, text='회원명',  bg='LightSkyBlue1')
    infodatelabel = Label(meminfowindow, text='생년월일',  bg='LightSkyBlue1')
    infogenderlabel = Label(meminfowindow, text='성별',  bg='LightSkyBlue1')
    infoTELlabel = Label(meminfowindow, text='전화번호',  bg='LightSkyBlue1')
    infoemaillabel = Label(meminfowindow, text='이메일', bg='LightSkyBlue1')
    infophotolabel = Label(meminfowindow, width=20, height=12, relief='solid')

    # 회원정보를 입력받을 엔트리
    infonameinput = Entry(meminfowindow, width=25)
    infonameinput.insert(0, '회원명')
    infodateinput = Entry(meminfowindow, width=25)
    infodateinput.insert(0, '생년월일')

    # 회원정보 중 성별을 입력받을 라디오버튼
    var = StringVar()
    var.set('남')  # 추후 데이터프레임에서 가져온 값으로 설정되어 있도록 수정
    infogenderinput1 = Radiobutton(meminfowindow, text='남', bg='white', value='남', variable=var)
    infogenderinput2 = Radiobutton(meminfowindow, text='여', bg='white', value='여', variable=var)

    # 회원정보를 입력받을 엔트리
    infoTELinput = Entry(meminfowindow, width=25)
    infoTELinput.insert(0, '전화번호')
    infoemailinput = Entry(meminfowindow, width=25)
    infoemailinput.insert(0, '이메일')

    # 닫기, 수정, 이미지 변경 버튼
    infoclosebutton = Button(meminfowindow, text='닫기', command=meminfowindow.destroy)
    infofixbutton = Button(meminfowindow, text='수정', command=info_fix_btn)
    photofixbutton = Button(meminfowindow, text='이미지 변경', command=photo_fix_btn)

    # 레이블 위젯 위치 지정(회원정보 인덱스)
    infonamelabel.place(x=200, y=20)
    infodatelabel.place(x=200, y=60)
    infogenderlabel.place(x=200, y=100)
    infoTELlabel.place(x=200, y=140)
    infoemaillabel.place(x=200, y=180)
    infophotolabel.place(x=20, y=20)

    # 엔트리 위젯 및 라디오버튼 위젯 위치 지정
    infonameinput.place(x=290, y=20)
    infodateinput.place(x=290, y=60)
    infogenderinput1.place(x=290, y=100)
    infogenderinput2.place(x=330, y=100)
    infoTELinput.place(x=290, y=140)
    infoemailinput.place(x=290, y=180)

    # 닫기, 수정, 이미지 변경 버튼 위치 지정
    infoclosebutton.place(x=440, y=250)
    infofixbutton.place(x=390, y=250)
    photofixbutton.place(x=55, y=220)


# 회원정보수정 - 회원검색 - 회원정보 - 수정 버튼 클릭
def info_fix_btn():
    messagebox.showinfo("회원정보수정", "회원정보수정 기능")


# 회원정보수정 - 회원검색 - 회원정보 - 이미지 변경 버튼 클릭
def photo_fix_btn():
    messagebox.showinfo("이미지 변경", "회원정보수정 - 이미지 변경")


# 회원탈퇴 - 회원검색 창
def member_search_del():
    # 회원검색(회원탈퇴) 창 생성
    memsearchwindow = Tk()
    memsearchwindow.title('회원검색(회원탈퇴)')
    memsearchwindow.geometry('600x400')
    memsearchwindow.configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(memsearchwindow, text='회원명',  bg='LightSkyBlue1')
    TELlabel = Label(memsearchwindow, text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(memsearchwindow, width=30)
    TELinput = Entry(memsearchwindow, width=30)

    # 회원정보 표시할 리스트박스
    resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    resultbox.insert(0, '회원이름')
    resultbox.bind('<Double-Button-1>', member_info_del_dbclick)

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=search_del_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성
    resultframe = Frame(memsearchwindow, relief='solid')
    resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    for i in range(5):
        resultlist[i] = Label(resultframe, text=resultlist[i])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

    resultframe.place(x=25, y=150)
    for result in resultlist:
        result.pack(side=LEFT, padx=30)

    resultbox.place(x=25, y=172)


# 회원탈퇴 - 회원검색 - 검색 버튼 클릭
def search_del_btn():
    messagebox.showinfo("검색실행", "회원 검색을 실행함")


# 회원탈퇴 - 회원정보 리스트박스 회원 더블클릭시 이벤트
def member_info_del_dbclick(event):
    member_info_del()


# 회원탈퇴 - 회원검색 - 회원정보(회원탈퇴 버튼 존재)
def member_info_del():
    # 회원정보(회원탈퇴) 창 생성
    meminfowindow = Tk()
    meminfowindow.title('회원정보(회원탈퇴)')
    meminfowindow.geometry('500x300')
    meminfowindow.configure(bg='LightSkyBlue1')

    # 회원정보 인덱스 표시할 레이블
    infonamelabel = Label(meminfowindow, text='회원명', bg='LightSkyBlue1')
    infodatelabel = Label(meminfowindow, text='생년월일',  bg='LightSkyBlue1')
    infogenderlabel = Label(meminfowindow, text='성별',bg='LightSkyBlue1')
    infoTELlabel = Label(meminfowindow, text='전화번호',  bg='LightSkyBlue1')
    infoemaillabel = Label(meminfowindow, text='이메일',  bg='LightSkyBlue1')
    infophotolabel = Label(meminfowindow, width=20, height=12, relief='solid')

    # 회원정보(실제 회원 정보) 표시할 레이블
    infonameinput = Label(meminfowindow, text='회원명', width=25, bg='white', anchor='w')
    infodateinput = Label(meminfowindow, text='생년월일', width=25, bg='white', anchor='w')
    infogenderinput = Label(meminfowindow, text='성별', width=25, bg='white', anchor='w')
    infoTELinput = Label(meminfowindow, text='전화번호', width=25, bg='white', anchor='w')
    infoemailinput = Label(meminfowindow, text='이메일', width=25, bg='white', anchor='w')

    # 회원정보 창 닫기 버튼
    infoclosebutton = Button(meminfowindow, text='닫기', command=meminfowindow.destroy)
    infodelbutton = Button(meminfowindow, text='회원탈퇴', command=info_del_btn)

    # 레이블 위젯 위치 지정(회원정보 인덱스)
    infonamelabel.place(x=200, y=20)
    infodatelabel.place(x=200, y=60)
    infogenderlabel.place(x=200, y=100)
    infoTELlabel.place(x=200, y=140)
    infoemaillabel.place(x=200, y=180)
    infophotolabel.place(x=20, y=20)

    # 레이블 위젯 위치 지정(실제 회원 정보)
    infonameinput.place(x=290, y=20)
    infodateinput.place(x=290, y=60)
    infogenderinput.place(x=290, y=100)
    infoTELinput.place(x=290, y=140)
    infoemailinput.place(x=290, y=180)

    # 창 닫기 버튼 위치 지정
    infoclosebutton.place(x=440, y=250)
    infodelbutton.place(x=370, y=250)


# 회원탈퇴 - 회원검색 - 회원정보 - 회원탈퇴 버튼 클릭
def info_del_btn():
    messagebox.showinfo("회원탈퇴", "회원탈퇴 기능")


# 탈퇴회원검색
def deleted_member_search():
    # 탈퇴회원검색 창 생성
    memsearchwindow = Tk()
    memsearchwindow.title('탈퇴회원검색')
    memsearchwindow.geometry('600x400')
    memsearchwindow.configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(memsearchwindow, text='회원명', bg='LightSkyBlue1')
    TELlabel = Label(memsearchwindow, text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(memsearchwindow, width=30)
    TELinput = Entry(memsearchwindow, width=30)

    # 회원정보 표시할 리스트박스
    resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    resultbox.insert(0, '회원이름')
    resultbox.bind('<Double-Button-1>', deleted_member_info_dbclick)

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=deleted_search_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성
    resultframe = Frame(memsearchwindow, relief='solid')
    resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    for i in range(5):
        resultlist[i] = Label(resultframe, text=resultlist[i])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

    resultframe.place(x=25, y=150)
    for result in resultlist:
        result.pack(side=LEFT, padx=30)

    resultbox.place(x=25, y=172)


# 탈퇴회원검색 - 검색 버튼 클릭 시
def deleted_search_btn():
    messagebox.showinfo("검색실행", "회원 검색을 실행함")


# 탈퇴회원검색 - 회원정보 리스트박스 회원 더블클릭시 이벤트
def deleted_member_info_dbclick(event):
    deleted_member_info()


# 탈퇴회원검색 - 회원 선택 시 회원정보 창 출력
def deleted_member_info():
    # 탈퇴회원정보 창 생성
    meminfowindow = Tk()
    meminfowindow.title('탈퇴회원정보')
    meminfowindow.geometry('500x300')
    meminfowindow.configure(bg='LightSkyBlue1')

    # 탈퇴회원정보 인덱스 표시할 레이블
    infonamelabel = Label(meminfowindow, text='회원명',  bg='LightSkyBlue1')
    infodatelabel = Label(meminfowindow, text='생년월일',  bg='LightSkyBlue1')
    infogenderlabel = Label(meminfowindow, text='성별',  bg='LightSkyBlue1')
    infoTELlabel = Label(meminfowindow, text='전화번호',  bg='LightSkyBlue1')
    infoemaillabel = Label(meminfowindow, text='이메일',  bg='LightSkyBlue1')
    infophotolabel = Label(meminfowindow, width=20, height=12, relief='solid')

    # 탈퇴회원정보(실제 회원 정보) 표시할 레이블
    infonameinput = Label(meminfowindow, text='회원명', width=25, bg='white', anchor='w')
    infodateinput = Label(meminfowindow, text='생년월일', width=25, bg='white', anchor='w')
    infogenderinput = Label(meminfowindow, text='성별', width=25, bg='white', anchor='w')
    infoTELinput = Label(meminfowindow, text='전화번호', width=25, bg='white', anchor='w')
    infoemailinput = Label(meminfowindow, text='이메일', width=25, bg='white', anchor='w')

    # 탈퇴회원정보 창 닫기 버튼
    infoclosebutton = Button(meminfowindow, text='닫기', command=meminfowindow.destroy)

    # 레이블 위젯 위치 지정(회원정보 인덱스)
    infonamelabel.place(x=200, y=20)
    infodatelabel.place(x=200, y=60)
    infogenderlabel.place(x=200, y=100)
    infoTELlabel.place(x=200, y=140)
    infoemaillabel.place(x=200, y=180)
    infophotolabel.place(x=20, y=20)

    # 레이블 위젯 위치 지정(실제 회원 정보)
    infonameinput.place(x=290, y=20)
    infodateinput.place(x=290, y=60)
    infogenderinput.place(x=290, y=100)
    infoTELinput.place(x=290, y=140)
    infoemailinput.place(x=290, y=180)

    # 창 닫기 버튼 위치 지정
    infoclosebutton.place(x=440, y=250)

#--회원끝

#--도서 시작

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


def main_UI():
    window = Tk()
    window.title('도서관리 프로그램')
    window.geometry('800x600')
    window.configure(bg='LightSkyBlue1')

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    MemberMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = '회원관리' , menu = MemberMenu)
    MemberMenu.add_command(label = '회원정보', command = member_search)
    MemberMenu.add_command(label='회원등록', command=member_register)
    MemberMenu.add_command(label='회원정보수정', command=member_search_fix)
    MemberMenu.add_command(label='회원탈퇴', command=member_search_del)
    MemberMenu.add_command(label='탈퇴회원확인', command=deleted_member_search)

    BookMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서관리', menu=BookMenu)
    BookMenu.add_command(label='새도서추가', command=Book_add)
    BookMenu.add_command(label='책정보조회', command=Book_search)
    BookMenu.add_command(label='책정보수정', command=bookfix_info)
    BookMenu.add_command(label='책정보삭제', command=bookfix_info)

    RentMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서대여', menu=RentMenu)
    RentMenu.add_command(label='도서대여', command=clickRentUser)
    RentMenu.add_command(label='도서반납', command=clickReturnUser)

    SettingMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='환경설정', menu=SettingMenu)
    SettingMenu.add_command(label='실험', command=window.quit) # 나중에 지워야함
    SettingMenu.add_command(label='종료', command= window.quit)

    window.mainloop()


main_UI()





