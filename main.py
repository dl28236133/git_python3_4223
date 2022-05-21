from tkinter import *
from tkinter import messagebox

def Member_Menu():
    messagebox.showinfo("회원", "회원")

def Book_Menu():
    messagebox.showinfo("도서", "도서")

def Rent_Menu():
    messagebox.showinfo("대여", "대여")

def main_UI():
    window = Tk()
    window.title('도서관리 프로그램')
    window.geometry('800x600')
    window.configure(bg='LightSkyBlue1')

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    MemberMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = '회원관리' , menu = MemberMenu)
    MemberMenu.add_command(label = '회원정보', command = Member_Menu)
    MemberMenu.add_command(label='회원등록', command=Member_Menu)
    MemberMenu.add_command(label='회원정보수정', command=Member_Menu)
    MemberMenu.add_command(label='회원탈퇴', command=Member_Menu)
    MemberMenu.add_command(label='탈퇴회원확인', command=Member_Menu)

    BookMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서관리', menu=BookMenu)
    BookMenu.add_command(label='새도서추가', command=Book_Menu)
    BookMenu.add_command(label='책정보조회', command=Book_Menu)
    BookMenu.add_command(label='책정보수정', command=Book_Menu)
    BookMenu.add_command(label='책정보삭제', command=Book_Menu)

    RentMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서대여', menu=RentMenu)
    RentMenu.add_command(label='도서대여', command=Rent_Menu)
    RentMenu.add_command(label='도서반납', command=Rent_Menu)

    SettingMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='환경설정', menu=SettingMenu)
    SettingMenu.add_command(label='종료', command= window.quit)

    window.mainloop()



main_UI()





