from tkinter import *
from member import *
from BOOK import *
from RENT import *


def main_UI():
    window = Tk()
    window.title('도서관리 프로그램')
    window.geometry('800x600')
    window.configure(bg='LightSkyBlue1')

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    memberMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "회원관리", menu = memberMenu)
    memberMenu.add_command(label="회원정보", command=member_search)
    memberMenu.add_command(label="회원등록", command=member_register)
    memberMenu.add_command(label="회원정보수정", command=member_search_fix)
    memberMenu.add_command(label="회원탈퇴", command = member_search_del)
    memberMenu.add_command(label="탈퇴회원확인", command = deleted_member_search)

    BookMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서관리', menu=BookMenu)
    BookMenu.add_command(label='새도서추가', command=Book_add)
    BookMenu.add_command(label='책정보조회', command=Book_search)
    BookMenu.add_command(label='책정보수정', command=bookfix_info)
    BookMenu.add_command(label='책정보삭제', command=bookdel_info)

    RentMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='도서대여', menu=RentMenu)
    RentMenu.add_command(label='도서대여', command=clickRentUser)
    RentMenu.add_command(label='도서반납', command=clickReturnUser)

    SettingMenu = Menu(mainMenu)
    mainMenu.add_cascade(label='환경설정', menu=SettingMenu)
    SettingMenu.add_command(label='종료', command= window.quit)

    window.mainloop()

main_UI()




