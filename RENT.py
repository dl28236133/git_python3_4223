from tkinter import *
from tkinter import messagebox
import pandas as pd
from functools import partial
import tkinter.ttk

#-- 대여시작
def clickMemberSearch():
    windowSearchUser = Tk()
    windowSearchUser.title('도서대여(회원검색)')
    windowSearchUser.geometry('600x300')
    windowSearchUser.configure(bg='LightSkyBlue1')
    
    df_member = pd.DataFrame(columns=['Member_TEL','Member_NAME','Member_BIRTHDATE','Member_GENDER','Member_EMAIL','Member_IMAGE','Member_DEL_MEM'])
    df_member.to_csv('Member.csv', index=False, encoding='UTF-8-sig')
    
    treeview = tkinter.ttk.Treeview(windowSearchUser, columns=["1", "2", "3" , "4" , "5"])
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=80, )
    treeview.heading("#0", text="index")

    treeview.column("#1", width=80, anchor="center")
    treeview.heading("1", text="이름", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("2", text="생년월일", anchor="center")

    treeview.column("#3", width=80, anchor="center")
    treeview.heading("3", text="성별", anchor="center")
        
    treeview.column("#4", width=100, anchor="center")
    treeview.heading("4", text="전화번호", anchor="center")

    treeview.column("#5", width=100, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    treeview.place(x=25, y=25)

    #if(TELinput in 'Member_TEL' and nameinput in 'Member_NAME'):
        #TELinput = df_member.loc['Member_TEL']
        #treelist = [(df_member[TELinput,'Member_NAME'],df_member[TELinput,'Member_BIRTHDATE'],df_member[TELinput,'Member_GENDER'],df_member[TELinput,'Member_TEL'],df_member[TELinput,'Member_EMAIL'])]

    #예시값
    treelist = [("김예지",20011120,"female","01043057883","k8917886@naver.com")]
    for i in range(len(treelist)):
        treeview.insert('','end', text=i, values=treelist[i])
    
    buttonNext = Button(windowSearchUser , text="다음", command=clickSearchBook)
    buttonNext.pack()
    buttonNext.place(x=500, y=200)
    
def clickSearchBook():
    windowSearchBook = Tk()
    windowSearchBook.title('도서대여(도서검색)')
    windowSearchBook.geometry('600x150')
    windowSearchBook.configure(bg='LightSkyBlue1')

    labelBookName = Label(windowSearchBook, text="도서명" , bg = 'LightSkyBlue1')
    labelBookName.pack()
    labelBookName.place(x=25, y=25)

    InputBookName = Entry(windowSearchBook, width=30)
    InputBookName.pack()
    InputBookName.place(x=100, y=25)
    InputBookName.insert(0, "도서명을 입력하세요.")

    buttonSearch = Button(windowSearchBook, text="검색", command=clickRentBook)
    buttonSearch.pack()
    buttonSearch.place(x=350, y=25)


    labelWriterName = Label(windowSearchBook, text="저자" , bg = 'LightSkyBlue1')
    labelWriterName.pack()
    labelWriterName.place(x=25, y=50)

    InputWriterName = Entry(windowSearchBook, width=30)
    InputWriterName.pack()
    InputWriterName.place(x=100, y=50)
    InputWriterName.insert(0, "저자명을 입력하세요.")
    
def clickNext():
    messagebox.showinfo("다음", "다음으로 넘어갑니다.")

def clickRent():
    messagebox.showinfo("대여", "도서를 대여합니다.")

def clickReturn():
    messagebox.showinfo("반납", "도서를 반납합니다.")

def clickRentUser():
    # 회원검색 창 생성
    windowRentUser   = Tk()
    windowRentUser  .title('도서대여(회원검색)')
    windowRentUser  .geometry('600x150')
    windowRentUser  .configure(bg='LightSkyBlue1')

    # 이름, 전화번호 기입 파트 레이블/엔트리
    namelabel = Label(windowRentUser  , text='회원명' , bg='LightSkyBlue1')
    TELlabel = Label(windowRentUser   , text='전화번호',  bg='LightSkyBlue1')
    nameinput = Entry(windowRentUser  , width=30)
    TELinput = Entry(windowRentUser  , width=30)

    # 검색 버튼
    searchbutton = Button(windowRentUser  , text="검색", width=10, command=clickMemberSearch)

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)

def clickRentBook():
    windowRentBook = Tk()
    windowRentBook.geometry("900x350")
    windowRentBook.title("도서 대여")
    windowRentBook.configure(bg='LightSkyBlue1')

    treeview = tkinter.ttk.Treeview(windowRentBook, columns=["1", "2", "3" , "4" , "5", "6", "7", "8"])
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=80, )
    treeview.heading("#0", text="index")

    treeview.column("#1", width=80, anchor="center")
    treeview.heading("1", text="사진", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("2", text="ISBN", anchor="center")

    treeview.column("#3", width=80, anchor="center")
    treeview.heading("3", text="도서명", anchor="center")
        
    treeview.column("#4", width=100, anchor="center")
    treeview.heading("4", text="저자", anchor="center")

    treeview.column("#5", width=100, anchor="center")
    treeview.heading("5", text="출판사", anchor="center")

    treeview.column("#6", width=80, anchor="center")
    treeview.heading("6", text="가격", anchor="center")
        
    treeview.column("#7", width=100, anchor="center")
    treeview.heading("7", text="URL", anchor="center")

    treeview.column("#8", width=100, anchor="center")
    treeview.heading("8", text="대여여부", anchor="center")

    treeview.place(x=25, y=25)

    #표에 데이터 삽입

    buttonRent = Button(windowRentBook, text="대여", command=clickRent)
    buttonRent.pack()
    buttonRent.place(x=750, y=300)

def clickReturnUser():
    # 회원검색 창 생성
    windowReturnUser  = Tk()
    windowReturnUser .title('도서반납(회원검색)')
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

    labelPhoto = Label(windowReturnBook, text="사진",  width=15)
    labelPhoto.pack()
    labelPhoto.place(x=25, y=100)

    labelISBN = Label(windowReturnBook, text="ISBN", width=15)
    labelISBN.pack()
    labelISBN.place(x=125, y=100)

    labelBookNameb = Label(windowReturnBook, text="도서명",  width=15)
    labelBookNameb.pack()
    labelBookNameb.place(x=225, y=100)

    labelWriterNameb = Label(windowReturnBook, text="저자",  width=15)
    labelWriterNameb.pack()
    labelWriterNameb.place(x=325, y=100)

    labelPUB = Label(windowReturnBook, text="출판사",  width=15)
    labelPUB.pack()
    labelPUB.place(x=425, y=100)

    labelPrice = Label(windowReturnBook, text="가격", width=15)
    labelPrice.pack()
    labelPrice.place(x=525, y=100)

    labelURL = Label(windowReturnBook, text="URL", width=10)
    labelURL.pack()
    labelURL.place(x=625, y=100)

    labelCan = Label(windowReturnBook, text="대여여부", width=15)
    labelCan.pack()
    labelCan.place(x=700, y=100)

    buttonReturn = Button(windowReturnBook, text="반납", command=clickReturn)
    buttonReturn.pack()
    buttonReturn.place(x=750, y=300)
#-- 대여끝
