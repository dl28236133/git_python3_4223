from tkinter import *
from tkinter import messagebox
import tkinter.ttk
from tkinter.filedialog import *
import math
import pandas as pd

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
            datalist = []
            if tel == '' :
                df_search = df_member.loc[df_member['Member_NAME']==name]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else :
                datalist = [[df_member['Member_TEL'].loc[tel], df_member['Member_NAME'].loc[tel], df_member['Member_BIRTHDATE'].loc[tel],
                            df_member['Member_GENDER'].loc[tel], df_member['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        else :
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")

    # 회원검색 - 회원 선택 시 회원정보 창 출력
    def member_info():

        #사용자가 더블클릭한 회원의 전화번호(ID) 값을 가져옴
        selectedmem = treeview.focus()
        Tel = treeview.set(selectedmem, column='1')
        
        global imagefilename
        imagefilename = df_member['Member_IMAGE'].loc[Tel]

        # 회원정보 창 생성
        meminfowindow = Tk()
        meminfowindow.title('회원정보')
        meminfowindow.geometry('500x300')
        meminfowindow.configure(bg='LightSkyBlue1')

        # 회원정보 인덱스 표시할 레이블
        infonamelabel = Label(meminfowindow, text='회원명',  bg='LightSkyBlue1')
        infodatelabel = Label(meminfowindow, text='생년월일',  bg='LightSkyBlue1')
        infogenderlabel = Label(meminfowindow, text='성별',  bg='LightSkyBlue1')
        infoTELlabel = Label(meminfowindow, text='전화번호', bg='LightSkyBlue1')
        infoemaillabel = Label(meminfowindow, text='이메일', bg='LightSkyBlue1')
        
        #이미지 파일이 들어갈 레이블 처리, 이미지 파일이 등록되지 않은 경우 nan값을 반환하므로 isnan함수로 처리
        try :
            if math.isnan(imagefilename)==False :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

            else :
                infophotolabel = Label(meminfowindow, width=20, height=13, relief='solid')

        except :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

        # 회원정보(실제 회원 정보) 표시할 레이블
        infonameinput = Label(meminfowindow, text=df_member['Member_NAME'].loc[Tel], width=25, bg='white', anchor='w')
        infodateinput = Label(meminfowindow, text=df_member['Member_BIRTHDATE'].loc[Tel], width=25, bg='white', anchor='w')
        infogenderinput = Label(meminfowindow, text=df_member['Member_GENDER'].loc[Tel], width=25, bg='white', anchor='w')
        infoTELinput = Label(meminfowindow, text=df_member['Member_TEL'].loc[Tel], width=25, bg='white', anchor='w')
        infoemailinput = Label(meminfowindow, text=df_member['Member_EMAIL'].loc[Tel], width=25, bg='white', anchor='w')

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
    #회원정보 - 끝

    # 회원정보 표(treeview) 회원 더블클릭시 이벤트
    def member_info_dbclick(event):
        member_info()
            
    #csv 파일 불러오기, 회원탈퇴 여부=False인 정보만 불러 옴
    df_member_ori = pd.read_csv("Member.csv", encoding='UTF-8-sig')
    df_member = df_member_ori.loc[df_member_ori['Member_DEL_MEM']==False]
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

    #회원정보 표시할 표 생성, 더블클릭 이벤트 지정
    treeview = tkinter.ttk.Treeview(memsearchwindow, columns=["1", "2", "3", "4", "5"], show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', member_info_dbclick)

    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
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


# 회원등록
imagefilename = None
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

    # 회원정보수정 - 회원검색 - 검색 버튼 클릭
    def search_fix_btn():

        for row in treeview.get_children() :
            treeview.delete(row)
        
        name = nameinput.get()
        tel = TELinput.get()
        df_namelist = list(df_member['Member_NAME'])
        df_tellist = list(df_member['Member_TEL'])

        if (name in df_namelist and tel in df_tellist) or (name in df_namelist and tel=='') or (name=='' and tel in df_tellist) :
            messagebox.showinfo("회원검색", "검색이 완료되었습니다.")
            datalist = []
            if tel == '' :
                df_search = df_member.loc[df_member['Member_NAME']==name]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else :
                datalist = [[df_member['Member_TEL'].loc[tel], df_member['Member_NAME'].loc[tel], df_member['Member_BIRTHDATE'].loc[tel],
                            df_member['Member_GENDER'].loc[tel], df_member['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        else :
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")

    # 회원정보수정 - 회원검색 - 회원정보(수정 버튼 존재)
    def member_info_fix():

        # 회원정보수정 - 회원검색 - 회원정보 - 수정 버튼 클릭
        def info_fix_btn():

            global imagefilename
            nonlocal df_member

            df_member["Member_TEL"].loc[Tel] = infoTELinput.get()
            df_member["Member_NAME"].loc[Tel] = infonameinput.get()
            df_member["Member_BIRTHDATE"].loc[Tel] = infodateinput.get()
            df_member["Member_EMAIL"].loc[Tel] = infoemailinput.get()
            df_member["Member_GENDER"].loc[Tel] = gender.get()
            df_member["Member_IMAGE"].loc[Tel] = imagefilename

            df_member.to_csv('Member.csv', index=False, encoding='utf-8-sig')

            messagebox.showinfo("회원정보수정", "회원정보수정이 완료되었습니다.")
            meminfowindow.destroy()

            for row in treeview.get_children() :
                treeview.delete(row)
        
            df_member_ori = pd.read_csv("Member.csv", encoding='UTF-8-sig')
            df_member = df_member_ori.loc[df_member_ori['Member_DEL_MEM']==False]
            df_member = df_member.set_index(df_member['Member_TEL'])

            name = nameinput.get()
            tel = TELinput.get()
            df_namelist = list(df_member['Member_NAME'])
            df_tellist = list(df_member['Member_TEL'])

            if (name in df_namelist and tel in df_tellist) or (name in df_namelist and tel=='') or (name=='' and tel in df_tellist) :
                datalist = []
                if tel == '' :
                    df_search = df_member.loc[df_member['Member_NAME']==name]
                    for i in range(len(df_search.index)) :
                        datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                         df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

                else :
                        datalist = [[df_member['Member_TEL'].loc[tel], df_member['Member_NAME'].loc[tel], df_member['Member_BIRTHDATE'].loc[tel],
                                     df_member['Member_GENDER'].loc[tel], df_member['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        # 회원정보수정 - 회원검색 - 회원정보 - 이미지 변경 버튼 클릭
        def photo_fix_btn():
            imagename = askopenfilename(parent = meminfowindow, filetypes=(("png 파일", "*.png"),("모든 파일","*.*")))
            global imagefilename
            imagefilename = imagename
            try :
                if math.isnan(imagefilename)==False :
                    meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                    infophotolabel.configure(image=meminfophoto)
                    infophotolabel.image = meminfophoto

            except :
                if imagefilename!='' :
                    meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                    infophotolabel.configure(image=meminfophoto)
                    infophotolabel.image = meminfophoto
                
        
        # 라디오버튼(성별) 커맨드 함수
        def genderM_set():
            gender.set("남")
    
        def genderW_set():
            gender.set("여")

        #사용자가 더블클릭한 회원의 전화번호(ID) 값을 가져옴
        selectedmem = treeview.focus()
        Tel = treeview.set(selectedmem, column='1')
        
        #지정된 이미지 파일 경로를 전역변수 imagefilename에 저장함.
        global imagefilename
        imagefilename = df_member['Member_IMAGE'].loc[Tel]

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

        #이미지 파일이 들어갈 레이블 처리, 이미지 파일이 등록되지 않은 경우 nan값을 반환하므로 isnan함수로 처리
        try :
            if math.isnan(imagefilename)==False :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

            else :
                infophotolabel = Label(meminfowindow, width=20, height=13, relief='solid')

        except :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

        # 회원정보를 입력받을 엔트리
        infonameinput = Entry(meminfowindow, width=25)
        infonameinput.insert(0, df_member['Member_NAME'].loc[Tel])
        infodateinput = Entry(meminfowindow, width=25)
        infodateinput.insert(0, df_member['Member_BIRTHDATE'].loc[Tel])

        # 회원정보 중 성별을 입력받을 라디오버튼
        gender = StringVar()
        gender.set(df_member['Member_GENDER'].loc[Tel])  
        infogenderinput1 = Radiobutton(meminfowindow, text='남', bg='white', variable=gender, value="남", command=genderM_set)
        infogenderinput2 = Radiobutton(meminfowindow, text='여', bg='white', variable=gender, value="여", command=genderW_set)
        if gender.get() == '남' :
            infogenderinput1.select()

        else :
            infogenderinput2.select()

        # 회원정보를 입력받을 엔트리
        infoTELinput = Entry(meminfowindow, width=25)
        infoTELinput.insert(0, df_member['Member_TEL'].loc[Tel])
        infoemailinput = Entry(meminfowindow, width=25)
        infoemailinput.insert(0, df_member['Member_EMAIL'].loc[Tel])

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
    # 회원정보수정-회원정보 끝

    # 회원정보 표(treeview) 회원 더블클릭시 이벤트
    def member_info_fix_dbclick(event):
        member_info_fix()
            
    #csv 파일 불러오기, 회원탈퇴 여부=False인 정보만 불러 옴
    df_member_ori = pd.read_csv("Member.csv", encoding='UTF-8-sig')
    df_member = df_member_ori.loc[df_member_ori['Member_DEL_MEM']==False]
    df_member = df_member.set_index(df_member['Member_TEL'])

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

    # 회원정보 표시할 리스트박스 -> treeview(표)로 대체
    # resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    # resultbox.insert(0, '회원이름')
    # resultbox.bind('<Double-Button-1>', member_info_fix_dbclick)

    #회원정보 표시할 표 생성
    treeview = tkinter.ttk.Treeview(memsearchwindow, columns=["1", "2", "3", "4", "5"], show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', member_info_fix_dbclick)

    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=search_fix_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성 -> treeview(표)로 대체
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
    #     result.pack(side=LEFT, padx=30)

    # resultbox.place(x=25, y=172)


# 회원탈퇴 - 회원검색 창
def member_search_del():

    # 회원탈퇴 - 회원검색 - 검색 버튼 클릭
    def search_del_btn():
        for row in treeview.get_children() :
            treeview.delete(row)
        
        name = nameinput.get()
        tel = TELinput.get()
        df_namelist = list(df_member['Member_NAME'])
        df_tellist = list(df_member['Member_TEL'])

        if (name in df_namelist and tel in df_tellist) or (name in df_namelist and tel=='') or (name=='' and tel in df_tellist) :
            messagebox.showinfo("회원검색", "검색이 완료되었습니다.")
            datalist = []
            if tel == '' :
                df_search = df_member.loc[df_member['Member_NAME']==name]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else :
                datalist = [[df_member['Member_TEL'].loc[tel], df_member['Member_NAME'].loc[tel], df_member['Member_BIRTHDATE'].loc[tel],
                            df_member['Member_GENDER'].loc[tel], df_member['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        else :
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 탈퇴처리 된 회원입니다.")


    # 회원탈퇴 - 회원검색 - 회원정보(회원탈퇴 버튼 존재)
    def member_info_del():

        # 회원탈퇴 - 회원검색 - 회원정보 - 회원탈퇴 버튼 클릭
        def info_del_btn():
            nonlocal df_member

            df_member["Member_DEL_MEM"].loc[Tel] = True

            df_member.to_csv('Member.csv', index=False, encoding='utf-8-sig')

            messagebox.showinfo("회원탈퇴", "회원탈퇴가 완료되었습니다.")
            meminfowindow.destroy()

            for row in treeview.get_children() :
                treeview.delete(row)
        
            df_member_ori = pd.read_csv("Member.csv", encoding='UTF-8-sig')
            df_member = df_member_ori.loc[df_member_ori['Member_DEL_MEM']==False]
            df_member = df_member.set_index(df_member['Member_TEL'])

            name = nameinput.get()
            tel = TELinput.get()
            df_namelist = list(df_member['Member_NAME'])
            df_tellist = list(df_member['Member_TEL'])

            if (name in df_namelist and tel in df_tellist) or (name in df_namelist and tel=='') or (name=='' and tel in df_tellist) :
                datalist = []
                if tel == '' :
                    df_search = df_member.loc[df_member['Member_NAME']==name]
                    for i in range(len(df_search.index)) :
                        datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                         df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

                else :
                        datalist = [[df_member['Member_TEL'].loc[tel], df_member['Member_NAME'].loc[tel], df_member['Member_BIRTHDATE'].loc[tel],
                                     df_member['Member_GENDER'].loc[tel], df_member['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])


        #사용자가 더블클릭한 회원의 전화번호(ID) 값을 가져옴
        selectedmem = treeview.focus()
        Tel = treeview.set(selectedmem, column='1')
        
        global imagefilename
        imagefilename = df_member['Member_IMAGE'].loc[Tel]

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
        
        #이미지 파일이 들어갈 레이블 처리, 이미지 파일이 등록되지 않은 경우 nan값을 반환하므로 isnan함수로 처리
        try :
            if math.isnan(imagefilename)==False :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

            else :
                infophotolabel = Label(meminfowindow, width=20, height=13, relief='solid')

        except :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

        # 회원정보(실제 회원 정보) 표시할 레이블
        infonameinput = Label(meminfowindow, text=df_member['Member_NAME'].loc[Tel], width=25, bg='white', anchor='w')
        infodateinput = Label(meminfowindow, text=df_member['Member_BIRTHDATE'].loc[Tel], width=25, bg='white', anchor='w')
        infogenderinput = Label(meminfowindow, text=df_member['Member_GENDER'].loc[Tel], width=25, bg='white', anchor='w')
        infoTELinput = Label(meminfowindow, text=df_member['Member_TEL'].loc[Tel], width=25, bg='white', anchor='w')
        infoemailinput = Label(meminfowindow, text=df_member['Member_EMAIL'].loc[Tel], width=25, bg='white', anchor='w')

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

    def member_info_del_dbclick(event):
        member_info_del()
            
    #csv 파일 불러오기
    df_member_ori = pd.read_csv("Member.csv", encoding='UTF-8-sig')
    df_member = df_member_ori.loc[df_member_ori['Member_DEL_MEM']==False]
    df_member = df_member.set_index(df_member['Member_TEL'])

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

    # 회원정보 표시할 리스트박스  -> treeview(표)로 대체
    # resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    # resultbox.insert(0, '회원이름')
    # resultbox.bind('<Double-Button-1>', member_info_del_dbclick)

    #회원정보 표시할 표 생성, 더블클릭 이벤트 지정
    treeview = tkinter.ttk.Treeview(memsearchwindow, columns=["1", "2", "3", "4", "5"], show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', member_info_del_dbclick)

    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=search_del_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성  -> treeview(표)로 대체
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
    #     result.pack(side=LEFT, padx=30)

    # resultbox.place(x=25, y=172)


# 탈퇴회원검색
def deleted_member_search():

    # 탈퇴회원검색 - 검색 버튼 클릭 시
    def deleted_search_btn():
        for row in treeview.get_children() :
            treeview.delete(row)
        
        name = nameinput.get()
        tel = TELinput.get()
        df_namelist = list(df_delmem['Member_NAME'])
        df_tellist = list(df_delmem['Member_TEL'])

        if (name in df_namelist and tel in df_tellist) or (name in df_namelist and tel=='') or (name=='' and tel in df_tellist) :
            messagebox.showinfo("회원검색", "검색이 완료되었습니다.")
            datalist = []
            if tel == '' :
                df_search = df_delmem.loc[df_delmem['Member_NAME']==name]
                for i in range(len(df_search.index)) :
                    datalist.append([df_search['Member_TEL'].iloc[i], df_search['Member_NAME'].iloc[i], df_search['Member_BIRTHDATE'].iloc[i], 
                                df_search['Member_GENDER'].iloc[i], df_search['Member_EMAIL'].iloc[i]])

            else :
                datalist = [[df_delmem['Member_TEL'].loc[tel], df_delmem['Member_NAME'].loc[tel], df_delmem['Member_BIRTHDATE'].loc[tel],
                            df_delmem['Member_GENDER'].loc[tel], df_delmem['Member_EMAIL'].loc[tel]]]
        
            for j in range(len(datalist)) :
                treeview.insert('', 'end', values=datalist[j])

        else :
            messagebox.showinfo("오류", "존재하지 않는 회원이거나, 회원탈퇴 처리되지 않은 회원입니다.")

    # 탈퇴회원검색 - 회원 선택 시 회원정보 창 출력
    def deleted_member_info():

        #사용자가 더블클릭한 회원의 전화번호(ID) 값을 가져옴
        selectedmem = treeview.focus()
        Tel = treeview.set(selectedmem, column='1')

        global imagefilename
        imagefilename = df_delmem['Member_IMAGE'].loc[Tel]

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

        #이미지 파일이 들어갈 레이블 처리, 이미지 파일이 등록되지 않은 경우 nan값을 반환하므로 isnan함수로 처리
        try :
            if math.isnan(imagefilename)==False :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

            else :
                infophotolabel = Label(meminfowindow, width=20, height=13, relief='solid')

        except :
                meminfophoto = PhotoImage(file=imagefilename, master=meminfowindow)
                infophotolabel = Label(meminfowindow, width=150, height=200, relief='solid', image=meminfophoto)
                infophotolabel.image = meminfophoto

        # 탈퇴회원정보(실제 회원 정보) 표시할 레이블
        infonameinput = Label(meminfowindow, text=df_delmem['Member_NAME'].loc[Tel], width=25, bg='white', anchor='w')
        infodateinput = Label(meminfowindow, text=df_delmem['Member_BIRTHDATE'].loc[Tel], width=25, bg='white', anchor='w')
        infogenderinput = Label(meminfowindow, text=df_delmem['Member_GENDER'].loc[Tel], width=25, bg='white', anchor='w')
        infoTELinput = Label(meminfowindow, text=df_delmem['Member_TEL'].loc[Tel], width=25, bg='white', anchor='w')
        infoemailinput = Label(meminfowindow, text=df_delmem['Member_EMAIL'].loc[Tel], width=25, bg='white', anchor='w')

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
    #탈퇴회원정보 - 끝
    
    # 탈퇴회원검색 - 회원정보 표(treeview) 회원 더블클릭시 이벤트
    def deleted_member_info_dbclick(event):
        deleted_member_info()
            
    #csv 파일 불러오기
    df_member = pd.read_csv("Member.csv", encoding='UTF-8-sig')
    df_delmem = df_member.loc[df_member['Member_DEL_MEM']==True]
    df_delmem = df_delmem.set_index(df_delmem['Member_TEL'])

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

    # 회원정보 표시할 리스트박스 -> treeview(표)로 대체
    # resultbox = Listbox(memsearchwindow, width=72, height=10, selectmode='single')
    # resultbox.insert(0, '회원이름')
    # resultbox.bind('<Double-Button-1>', deleted_member_info_dbclick)

    # 검색 버튼
    searchbutton = Button(memsearchwindow, text="검색", width=10, command=deleted_search_btn)

    # 검색창 윗부분(컬럼스) 레이블로 생성 -> treeview(표)로 대체
    # resultframe = Frame(memsearchwindow, relief='solid')
    # resultlist = ['이름', '생년월일', '성별', '전화번호', '이메일']
    # for i in range(5):
    #     resultlist[i] = Label(resultframe, text=resultlist[i])

    #회원정보 표시할 표 생성
    treeview = tkinter.ttk.Treeview(memsearchwindow, columns=["1", "2", "3", "4", "5"], show='headings')
    treeview.pack()
    treeview.bind('<Double-Button-1>', deleted_member_info_dbclick)

    treeview.column("#1", width=100, )
    treeview.heading("1", text="전화번호")

    treeview.column("2", width=100, anchor="center")
    treeview.heading("2", text="이름", anchor="center")

    treeview.column("3", width=100, anchor="center")
    treeview.heading("3", text="생년월일", anchor="center")

    treeview.column("4", width=80, anchor="center")
    treeview.heading("4", text="성별", anchor="center")

    treeview.column("5", width=120, anchor="center")
    treeview.heading("5", text="이메일", anchor="center")

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
    #     result.pack(side=LEFT, padx=30)

    # resultbox.place(x=25, y=172)

    

#--회원끝