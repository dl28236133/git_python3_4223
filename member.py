from tkinter import *
from tkinter import messagebox
import tkinter.ttk
from tkinter.filedialog import *
import pandas as pd
from functools import partial

#--회원시작

#member.csv 파일이 없다면 생성하는 함수
def member_csv():
    try : 
        df_member = pd.read_csv('Member.csv', encoding='UTF-8-sig')
    except:
        df_member = pd.DataFrame(columns=['Member_TEL','Member_NAME','Member_BIRTHDATE','Member_GENDER','Member_EMAIL','Member_IMAGE','Member_DEL_MEM'])
        df_member.to_csv('Member.csv', index=False, encoding='UTF-8-sig')

# 회원정보 - 회원검색창
def member_search():

    # 회원검색 - 검색 버튼 클릭 시
    def search_btn():
        for row in treeview.get_children() :
            treeview.delete(row)
        
        name = nameinput.get()
        tel = TELinput.get()
        df_namelist = list(df_member['Member_NAME'])
        df_tellist = list(df_member['Member_TEL'])

        if (name in df_namelist and tel in df_tellist) or (name in df_namelist and tel=='') or (name=='' and tel in df_tellist) :
            messagebox.showinfo("회원검색", "검색이 완료되었습니다.")
            if tel == '' :
                df_search = df_member.loc[df_member['Member_NAME']==name]
                for i in range(len(df_member.index)) :
                    datalist = []
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else :
                datalist = [[df_member['Member_TEL'].loc[tel], df_member['Member_NAME'].loc[tel], df_member['Member_BIRTHDATE'].loc[tel],
                            df_member['Member_GENDER'].loc[tel], df_member['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', index=j, values=datalist[j])
            

        else :
            messagebox.showinfo("오류", "존재하지 않는 회원입니다.")
            
    #csv 파일 불러오기
    df_member = pd.read_csv("Member.csv", encoding='UTF-8-sig')
    df_member = df_member.set_index(df_member['Member_TEL'])

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

    # 회원정보 표시할 리스트박스 -> treeview(표)로 대체
    # resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    # resultbox.insert(0, '회원이름')
    # resultbox.bind('<Double-Button-1>', member_info_dbclick) 

    #회원정보 표시할 표 생성
    treeview = tkinter.ttk.Treeview(memsearchwindow, columns=["1", "2", "3", "4", "5"], show='headings')
    treeview.pack()

    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=100, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")


    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=search_btn)

    # # 검색창 윗부분(컬럼스) 레이블로 생성 -> treeview(표)로 대체
    # resultframe = Frame(memsearchwindow, relief='solid')
    # resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    # for i in range(5):
    #     resultlist[i] = Label(resultframe, text=resultlist[i])

    # 생성한 위젯 위치 지정
    namelabel.place(x=30, y=20)
    nameinput.place(x=120, y=20)
    TELlabel.place(x=30, y=60)
    TELinput.place(x=120, y=60)
    searchbutton.place(x=350, y=20)
    treeview.place(x=25, y=150)

    # treeview(표)로 대체
    # resultframe.place(x=25, y=150)
    # for result in resultlist:
    #     result.pack(side='left', padx=30)

    # resultbox.place(x=25, y=172)

    # 회원정보 리스트박스 회원 더블클릭시 이벤트 -> treeview(표)로 대체됨
    # def member_info_dbclick(event):

    #     member_info()

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

    # 회원등록 - 파일찾기 버튼 클릭 시
    def image_btn():
        imagename = askopenfilename(parent = memregiwindow, filetypes=(("png 파일", "*.png"),("모든 파일","*.*")))
        regiphotoinput.delete(0, 'end')
        regiphotoinput.insert(0, imagename)

    # 라디오버튼(성별) 커맨드 함수
    def genderM_set():
        gender.set("남")
    
    def genderW_set():
        gender.set("여")
    
    # 회원등록 - 등록 버튼 클릭 시
    def regi_btn():
        df_member = pd.read_csv('Member.csv', encoding='UTF-8-sig')
        df_member = df_member.set_index(df_member['Member_TEL'])

        new_member = {"Member_TEL": regiTELinput.get(),
              "Member_NAME": reginameinput.get(),
              "Member_BIRTHDATE": regidateinput.get(),
              "Member_GENDER": gender.get(),
              "Member_EMAIL": regiemailinput.get(),
              "Member_IMAGE": regiphotoinput.get(),
              "Member_DEL_MEM": False}

        df_member = df_member.append(new_member,ignore_index=True)
        df_member = df_member.set_index(df_member['Member_TEL'])
        df_member.to_csv('Member.csv', index=False, encoding='utf-8-sig')
        messagebox.showinfo("회원등록완료", "회원등록이 완료되었습니다.")
        memregiwindow.destroy()
        
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
    gender = StringVar()
    gender.set("남")
    regigenderinput1 = Radiobutton(memregiwindow, text='남', bg='white', variable=gender, value="남", command=genderM_set)
    regigenderinput1.select()
    regigenderinput2 = Radiobutton(memregiwindow, text='여', bg='white', variable=gender, value="여", command=genderW_set)

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