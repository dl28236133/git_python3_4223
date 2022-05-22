from tkinter import *
from member import *

def main():
    window = Tk()
    window.title('도서관리 프로그램')
    window.geometry('800x600')
    window.configure(bg='LightSkyBlue1')

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    memberMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "회원관리", menu = memberMenu)
    memberMenu.add_command(label="회원정보", command=member_search)
    memberMenu.add_separator()
    memberMenu.add_command(label="회원등록", command=member_register)
    memberMenu.add_separator()
    memberMenu.add_command(label="회원정보수정", command=member_search_fix)
    memberMenu.add_separator()
    memberMenu.add_command(label="회원탈퇴", command = member_search_del)
    memberMenu.add_separator()
    memberMenu.add_command(label="탈퇴회원확인", command = deleted_member_search)

    window.mainloop()
main()