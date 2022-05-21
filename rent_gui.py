from tkinter import*
from tkinter import messagebox

def clickSearch():
        messagebox.showinfo("검색", "검색합니다.")

def clickNext() :
    messagebox.showinfo("다음", "다음으로 넘어갑니다.")

def clickRent() :
    messagebox.showinfo("대여", "도서를 대여합니다.")

def clickReturn():
    messagebox.showinfo("반납", "도서를 반납합니다.")

def clickRentUser() :
    windowRentUser = Tk()
    windowRentUser.geometry("700x400")
    windowRentUser.title("도서 대여(회원 검색)")

    labelUserName = Label(windowRentUser, text = "회원명")
    labelUserName.pack()
    labelUserName.place( x = 25, y = 25)

    InputUserName = Entry(windowRentUser, width = 30)
    InputUserName.pack()
    InputUserName.place( x = 100, y = 25)
    InputUserName.insert(0, "이름을 입력하세요.")


    buttonSearch = Button(windowRentUser, text = "검색", command = clickSearch)
    buttonSearch.pack()
    buttonSearch.place( x = 350, y = 25)
        

    labelUserNumber = Label(windowRentUser, text = "전화번호")
    labelUserNumber.pack()
    labelUserNumber.place( x = 25, y = 50)

    InputUserNumber = Entry(windowRentUser, width = 30)
    InputUserNumber.pack()
    InputUserNumber.place( x = 100, y = 50)
    InputUserNumber.insert(0, "전화번호를 입력하세요.")


    labelPhoto = Label(windowRentUser, text = "사진", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelPhoto.pack()
    labelPhoto.place( x = 25, y = 100)

    labelName = Label(windowRentUser, text = "이름", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelName.pack()
    labelName.place( x = 125, y = 100)

    labelBirth = Label(windowRentUser, text = "생년월일", bg = 'blue', fg = 'white' ,\
                       width = 25)
    labelBirth.pack()
    labelBirth.place( x = 230, y = 100)

    labelNumber = Label(windowRentUser, text = "전화번호", bg = 'blue', fg = 'white' ,\
                       width = 25)
    labelNumber.pack()
    labelNumber.place( x = 375, y = 100)

    labelMail = Label(windowRentUser, text = "이메일", bg = 'blue', fg = 'white' ,\
                       width = 20)
    labelMail.pack()
    labelMail.place( x = 530, y = 100)


    buttonNext = Button(windowRentUser, text = "다음", command = clickNext)
    buttonNext.pack()
    buttonNext.place( x = 600, y = 300)

def clickRentBook() :
    windowRentBook = Tk()
    windowRentBook.geometry("700x400")
    windowRentBook.title("도서 대여(도서 검색)")

    labelBookName = Label(windowRentBook, text = "도서명")
    labelBookName.pack()
    labelBookName.place( x = 25, y = 25)

    InputBookName = Entry(windowRentBook, width = 30)
    InputBookName.pack()
    InputBookName.place( x = 100, y = 25)
    InputBookName.insert(0, "도서명을 입력하세요.")


    buttonSearch = Button(windowRentBook, text = "검색", command = clickSearch)
    buttonSearch.pack()
    buttonSearch.place( x = 350, y = 25)
        

    labelWriterName = Label(windowRentBook, text = "저자")
    labelWriterName.pack()
    labelWriterName.place( x = 25, y = 50)

    InputWriterName = Entry(windowRentBook, width = 30)
    InputWriterName.pack()
    InputWriterName.place( x = 100, y = 50)
    InputWriterName.insert(0, "저자명을 입력하세요.")


    labelPhoto = Label(windowRentBook, text = "사진", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelPhoto.pack()
    labelPhoto.place( x = 25, y = 100)

    labelISBN = Label(windowRentBook, text = "ISBN", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelISBN.pack()
    labelISBN.place( x = 125, y = 100)

    labelBookNameb = Label(windowRentBook, text = "도서명", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelBookNameb.pack()
    labelBookNameb.place( x = 225, y = 100)

    labelWriterNameb = Label(windowRentBook, text = "저자", bg = 'blue', fg = 'white' ,\
                       width = 10)
    labelWriterNameb.pack()
    labelWriterNameb.place( x = 325, y = 100)

    labelPrice = Label(windowRentBook, text = "가격", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelPrice.pack()
    labelPrice.place( x = 400, y = 100)

    labelURL = Label(windowRentBook, text = "URL", bg = 'blue', fg = 'white' ,\
                       width = 10)
    labelURL.pack()
    labelURL.place( x = 510, y = 100)

    labelCan = Label(windowRentBook, text = "대여여부", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelCan.pack()
    labelCan.place( x = 570, y = 100)


    buttonRent = Button(windowRentBook, text = "대여", command = clickRent)
    buttonRent.pack()
    buttonRent.place( x = 600, y = 300)

def clickReturnUser() :
    windowReturnUser = Tk()
    windowReturnUser.geometry("700x400")
    windowReturnUser.title("도서 반납")

    labelUserName = Label(windowReturnUser, text = "회원명")
    labelUserName.pack()
    labelUserName.place( x = 25, y = 25)

    InputUserName = Entry(windowReturnUser, width = 30)
    InputUserName.pack()
    InputUserName.place( x = 100, y = 25)
    InputUserName.insert(0, "이름을 입력하세요.")


    buttonSearch = Button(windowReturnUser, text = "검색", command = clickSearch)
    buttonSearch.pack()
    buttonSearch.place( x = 350, y = 25)
        

    labelUserNumber = Label(windowReturnUser, text = "전화번호")
    labelUserNumber.pack()
    labelUserNumber.place( x = 25, y = 50)

    InputUserNumber = Entry(windowReturnUser, width = 30)
    InputUserNumber.pack()
    InputUserNumber.place( x = 100, y = 50)
    InputUserNumber.insert(0, "전화번호를 입력하세요.")


    labelPhoto = Label(windowReturnUser, text = "사진", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelPhoto.pack()
    labelPhoto.place( x = 25, y = 100)

    labelName = Label(windowReturnUser, text = "이름", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelName.pack()
    labelName.place( x = 125, y = 100)

    labelBirth = Label(windowReturnUser, text = "생년월일", bg = 'blue', fg = 'white' ,\
                       width = 25)
    labelBirth.pack()
    labelBirth.place( x = 230, y = 100)

    labelNumber = Label(windowReturnUser, text = "전화번호", bg = 'blue', fg = 'white' ,\
                       width = 25)
    labelNumber.pack()
    labelNumber.place( x = 375, y = 100)

    labelMail = Label(windowReturnUser, text = "이메일", bg = 'blue', fg = 'white' ,\
                       width = 20)
    labelMail.pack()
    labelMail.place( x = 530, y = 100)


    buttonNext = Button(windowReturnUser, text = "다음", command = clickNext)
    buttonNext.pack()
    buttonNext.place( x = 600, y = 300)

def clickReturnBook() :
    windowReturnBook = Tk()
    windowReturnBook.geometry("700x400")
    windowReturnBook.title("도서 반납")

    labelUserName = Label(windowReturnBook, text = "회원명")
    labelUserName.pack()
    labelUserName.place( x = 25, y = 25)

    InputUserName = Entry(windowReturnBook, width = 30)
    InputUserName.pack()
    InputUserName.place( x = 100, y = 25)
    InputUserName.insert(0, "이름")


    labelPhoto = Label(windowReturnBook, text = "사진", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelPhoto.pack()
    labelPhoto.place( x = 25, y = 100)

    labelISBN = Label(windowReturnBook, text = "ISBN", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelISBN.pack()
    labelISBN.place( x = 125, y = 100)

    labelBookNameb = Label(windowReturnBook, text = "도서명", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelBookNameb.pack()
    labelBookNameb.place( x = 225, y = 100)

    labelWriterNameb = Label(windowReturnBook, text = "저자", bg = 'blue', fg = 'white' ,\
                       width = 10)
    labelWriterNameb.pack()
    labelWriterNameb.place( x = 325, y = 100)

    labelPrice = Label(windowReturnBook, text = "가격", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelPrice.pack()
    labelPrice.place( x = 400, y = 100)

    labelURL = Label(windowReturnBook, text = "URL", bg = 'blue', fg = 'white' ,\
                       width = 10)
    labelURL.pack()
    labelURL.place( x = 510, y = 100)

    labelCan = Label(windowReturnBook, text = "대여여부", bg = 'blue', fg = 'white' ,\
                       width = 15)
    labelCan.pack()
    labelCan.place( x = 570, y = 100)


    buttonReturn = Button(windowReturnBook, text = "반납", command = clickReturn)
    buttonReturn.pack()
    buttonReturn.place( x = 600, y = 300)
    
clickRentUser()
clickRentBook()
clickReturnUser()
clickReturnBook()
