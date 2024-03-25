"""
2022/01/20   李衡
"""


import os
import phreeqpy.iphreeqc.phreeqc_dll as phreeqc_mod
import numpy as np
import matplotlib.pyplot as plt


# ——————————————————————————————————————————————

def loadDatadet(infile):
    f = open(infile, 'r')
    sourceInLine = f.readlines()[9:]
    dataset = []
    for line in sourceInLine:
        temp3 = line.split()

        dataset.append(temp3)
        # print (dataset)
    k = len(dataset[0])
    for i in range(0, len(dataset)):       # 该位置可能会报错，与cpu性能有关
        for j in range(0, k):
            dataset[i].append(float(dataset[i][j]))
        del (dataset[i][0:k])
    return dataset


print(__name__)

if __name__ == "__main__":

    # 数据库路径
    datpath = "C:/Program Files (x86)/USGS/Phreeqc Interactive 3.7.3-15968/database"


    def selected_array(db_path, input_string):
        """
        调用phreeqc的COM对象
        """
        dbase = phreeqc_mod.IPhreeqc('C:/Program Files/USGS/IPhreeqcCOM 3.7.3-15968/bin/IPhreeqcCOM.dll')
        dbase.load_database(db_path)
        dbase.run_string(input_string)
        return dbase.get_selected_output_array()



    # ——————————————————————————————存储路径，后台运行环境配置
    import numpy as np
    import time
    import sys
    import os
    import shutil


    def mkdir(path):

        path = path.strip()

        path = path.rstrip("\\")

        isExists = os.path.exists(path)

        if not isExists:

            os.makedirs(path)
            print(path + ' ok')
            return True
        else:
            print(path + ' exist')
            return False



    def wait(path):
        isExists = os.path.exists(path)
        if not isExists:
            return False
        else:
            print(path + ' ok')
            return True


    import psutil
    pids = psutil.pids()
    # print(pids)
    for pid in pids:
        # print(pid)
        p = psutil.Process(pid)
        if p.name() == 'comsolmphserver.exe':
            print("pid-%d,pname-%s" % (pid, p.name()))
            PID = pid
    # 后台是否打开

    print(PID)

    def get_cpu_info():
        cpucount = psutil.cpu_count(logical=True)

        process = psutil.Process(int(PID))
        cpupercent = process.cpu_percent(interval=2)

        cpu = int(cpupercent / cpucount)

        start = time.time()
        while cpu > 10:

            time.sleep(0.01)
            cpupercent = process.cpu_percent(interval=2)
            cpu = int(cpupercent / cpucount)
        end1 = time.time()


    class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass


    path = os.path.abspath(os.path.dirname(__file__))
    type = sys.getfilesystemencoding()
    sys.stdout = Logger('runlog.txt')
    # 记录时间节点
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('------------------')

    start = time.time()

    import os

    path1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result"
    mkdir(path1)
    # 时间步长
    timestep = 10
    # 总的时间
    totaltime = 1000
    # 共计xx步
    steps = int(totaltime / timestep)

    ###————————————————1.初始化comsol，————————————————————#######################################


    import initial_comsolrun

    incr1 = 'range(0,'
    incr2 = ','
    incr3 = ')'
    incr = incr1 + str(timestep) + incr2 + str(timestep) + incr3
    inputcomsolstr01 = initial_comsolrun.inputcomsolstr0.replace('range(###)', incr)

    print(inputcomsolstr01)

    incr1 = "'t', '"
    incr = incr1 + str(timestep)
    inputcomsolstr02 = inputcomsolstr01.replace("'t', '#", incr)

    incr1 = "outcon"
    incr = incr1 + str(timestep)
    inputcomsolstr03 = inputcomsolstr02.replace("outcono", incr)

    incr1 = "Pressure"
    incr = incr1 + str(timestep)
    inputcomsolstr04 = inputcomsolstr03.replace("Pressureo", incr)

    incr1 = "flowvelocity"
    incr = incr1 + str(timestep)
    inputcomsolstr05 = inputcomsolstr04.replace("flowvelocityo", incr)

    incr1 = "materialvelocity"
    incr = incr1 + str(timestep)
    inputcomsolstr06 = inputcomsolstr05.replace("materialvelocityo", incr)
    
    fh = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc/initial_comsolrun.m', 'w', encoding='utf-8')
    fh.write(inputcomsolstr06)
    fh.close()


    import win32api

    win32api.ShellExecute(0, 'run', 'F:\\(Comsol+Phreeqc)python\COMSOL_phreeqc/initial_comsolrun.m', '', '', 1)


    incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\outcon"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！")

    incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/Pressure"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！")

    incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/flowvelocity"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！")

    incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！！")

    ###————————————————   2.获取初始化输出数据———————————————————################################################

    infile = 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\outcon0.txt'
    infile = np.array(loadDatadet(infile))

    print(infile.shape)


    m = infile.shape[0]

    n = infile.shape[1] - 2  # 所有反应物数量

    outn = 18
    phresult = np.zeros((m, outn))

    end1 = time.time()


    ###————————————————   3.初始phreeqc输入数据 ————############################


    incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/outcon"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    print(infile)
    infile = np.array(loadDatadet(infile))


    input_string10 = """   """
    #溶液数据输入框架
    for i in range(0, m):
        input_string1 = """
                SOLUTION #
                    temp      56
                    pH        ### 
                    pe        #
                    redox     pe
                    units     mol/kgw
                    density   1
                    water    1
                    A         ###
                    B         ###
                    C         ###
                    D         ###
                    E         ###
                    F         ###
                    G         ###
                    H         ###
                    I         ###
                    J         ###
                    """

        ph = 7
        pe = 4

        for j in range(2, 13):
            if infile[i, j] < 0:
                infile[i, j] = 0

        # print(ph, pe)

        incr = str(round(infile[i, 2], 10))
        str1 = 'pH        '
        incr = str1 + incr
        input_string11 = input_string1.replace('pH        ###', incr)

        incr = str(round(pe, 4))
        str1 = 'pe        '
        incr = str1 + incr
        input_string12 = input_string11.replace('pe        #', incr)

        # 修改 A
        incr = str(round(infile[i, 3], 10))
        # print(incr)
        str1 = 'Ca        '
        incr = str1 + incr
        input_string13 = input_string12.replace('A         ###', incr)

        # 修改 B
        incr = str(round(infile[i, 4], 10))
        str1 = 'C(4)        '
        incr = str1 + incr
        input_string14 = input_string13.replace('B         ###', incr)
        
        incr = str(round(infile[i, 5], 10))
        str1 = 'Al        '
        incr = str1 + incr
        input_string15 = input_string14.replace('C         ###', incr)
        
        incr = str(round(infile[i, 6], 10))
        str1 = 'Na        '
        incr = str1 + incr
        input_string16 = input_string15.replace('D         ###', incr)
        
        incr = str(round(infile[i, 7], 10))
        str1 = 'K        '
        incr = str1 + incr
        input_string17 = input_string16.replace('E         ###', incr)
        
        incr = str(round(infile[i, 8], 10))
        str1 = 'Fe(2)        '
        incr = str1 + incr
        input_string18 = input_string17.replace('F         ###', incr)
        
        incr = str(round(infile[i, 9], 10))
        str1 = 'Mg        '
        incr = str1 + incr
        input_string19 = input_string18.replace('G         ###', incr)
        
        incr = str(round(infile[i, 10], 10))
        str1 = 'S(6)        '
        incr = str1 + incr
        input_string20 = input_string19.replace('H         ###', incr)
        
        incr = str(round(infile[i, 11], 10))
        str1 = 'Si        '
        incr = str1 + incr
        input_string21 = input_string20.replace('I         ###', incr)
        
        incr = str(round(infile[i, 12], 10))
        str1 = 'Cl        '
        incr = str1 + incr
        input_string22 = input_string21.replace('J         ###', incr)
              
        incr = str(i + 1)
        str1 = 'SOLUTION '
        incr = str1 + incr
        input_string24 = input_string22.replace('SOLUTION #', incr)

        # 反应配置
        input_string10 = input_string10 + input_string24
    #动力学参数输入及输出框架
    input_string2 = """
            PHASES
            Pyrophyllite
                Al2Si4O12H2 + 6H+ + 4H2O = 2Al+3 + 4H4SiO4
                -analytical_expression -8979.387 -2.082858 444075.9 3366.644 -23685900 0.0005204115
                -Vm       128.04 cm3/mol
            Smectite_Ca
                Ca.165Mg0.33Al1.67Si4O12H2 + 6H+ + 4H2O = 1.67Al+3 + 0.165Ca+2 + 0.33Mg+2 + 4H4SiO4
                log_k     3.481
                -Vm       365.394 cm3/mol
            SELECTED_OUTPUT #
                -simulation           false
                -state                false
                -distance             false
                -time                 false
                -step                 false
                -pe                   false
                -totals               Al  C(4)  Ca  Cl  Fe(2)  K  Mg Na  S(6)  Si
                -saturation_indices    Calcite Quartz  Smectite_Ca  Pyrophyllite   Anorthite
            USER_PUNCH # 
                -headings Activity_H+
               -start
            10 PUNCH ACT("H+")
               -end                 
          End
                """

    # 修改输出
    incr = str(m)
    str1 = 'SELECTED_OUTPUT 1-'
    incr = str1 + incr
    input_string31 = input_string2.replace('SELECTED_OUTPUT #', incr)
    
    incr = str(m)
    str1 = 'USER_PUNCH 1-'
    incr = str1 + incr
    input_string32 = input_string31.replace('USER_PUNCH #', incr)

    input_string = input_string10 + input_string32



    phreeqc_result = selected_array(os.path.join(datpath, 'phreeqc.dat'), input_string)

    ###———————————---------—————   5.修改phreeqc输出数据的排布------------————————————————————#############################################

    for jj in range(0, outn):
        for zz in range(1, m + 1):
            a = [entry[jj] for entry in phreeqc_result][zz:]
            phresult[zz - 1, jj] = float(a[0])
    '''
    np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/rphreeqc0.txt', phreeqc_result, encoding='utf-8')
    infile0 = 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/phreeqc0.txt'

    phresult = np.array(loadDatadet(infile0))
    '''
    ### ————————————————————6. 反应过后的初始化输出数据（浓度）————————————————————————###########################################

    for i in range(0, m):
        for k in range(0, n):
            infile[i, 2 + k] = phresult[i, 2 + k] * 1000 #将phreeqc的值赋给comsol，以及浓度单位修改
    for i in range(0, m):
        for k in range(0, n-11):
            infile[i, 12 + k] = phresult[i, 12 + k] #将phreeqc的值赋给comsol，饱和指数



    print(infile)
    print(infile.shape)

    incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/outcon"
    incr =  str(timestep)
    incr2 = ".txt"
    infile11 = incr1 + incr + incr2


    np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile.txt', infile)
    # np.savetxt('F:\Pycharm\COMSOL_phreeqc\Result/infile.txt', infile, fmt="%10.5f")

    with open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile.txt', 'r', encoding='utf-8') as f:
        dataset = f.read()  # 类型: str


    fh = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/initcon.txt', 'w')
    for line in open(infile11, 'r'):
        a = line.split(' ')
        if a[0] == '%':
            fh.write(line)
    fh.write(dataset)
    fh.close()


    strint1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/initcon"
    strint2 = str(timestep)
    strint3 = ".txt"
    shutil.copy('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/initcon.txt', strint1 + strint2 + strint3)


    ###————————————————————————7. 输入反应过后的初始化数据（进入主循环）###################################
    # 按节点计算化学反应

    import comsolrun

    for nstep in range(1, steps):

        print(infile.shape)


        incr1 = 'range('
        incr2 = ','
        incr3 = ')'
        incr = incr1 + str(timestep * nstep) + incr2 + str(timestep) + incr2 + str(timestep * (nstep + 1)) + incr3
        inputcomsolstr01 = comsolrun.inputcomsolstr0.replace('range(###)', incr)

        incr1 = "initcon"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr02 = inputcomsolstr01.replace("initconi", incr)


        incr1 = "Pressure"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr03 = inputcomsolstr02.replace("Pressurei", incr)

        incr1 = "flowvelocity"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr04 = inputcomsolstr03.replace("flowvelocityi", incr)
        
        ###———————————————————————
        
        incr1 = "materialvelocity"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr05 = inputcomsolstr04.replace("materialvelocityi", incr)
        
        ###———————————————————————
        
        incr1 = "'t', '"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr06 = inputcomsolstr05.replace("'t', '#", incr)

        incr1 = "outcon"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr07 = inputcomsolstr06.replace("outcono", incr)

        incr1 = "Pressure"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr08 = inputcomsolstr07.replace("Pressureo", incr)

        incr1 = "flowvelocity"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr09 = inputcomsolstr08.replace("flowvelocityo", incr)

        incr1 = "materialvelocity"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr10 = inputcomsolstr09.replace("materialvelocityo", incr)
        
        incr1 = "model_"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr11 = inputcomsolstr10.replace("model_o", incr)
        
        fh = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc/comsolrun.m', 'w', encoding='utf-8')
        fh.write(inputcomsolstr11)
        fh.close()


        ###————————————————————————8. 下一步的comsol运行#########################



        win32api.ShellExecute(0, 'run', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc/comsolrun.m', '', '', 1)


        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\outcon"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        print(infile)
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")

        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/Pressure"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")

        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/flowvelocity"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")
        
        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")
        ###———————————————————————9. 网格位移累加###################################
        import pandas as pd
        
        # list1, list2, list13, list14, list23, list24 = [], [], [], [], [], []
   
        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity"
        incr = str(timestep * nstep)
        incr2 = ".txt"
        infile1 = incr1 + incr + incr2
        while wait(infile1) == False:
            time.sleep(0.01)
        print(infile1, "ok！")
        infile1 = np.array(loadDatadet(infile1))
        np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile1.txt', infile1)
        df1= pd.read_csv('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile1.txt',sep=" ",names=["% x1","y1","material1.u","material1.v"])
        '''
        f = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile1.txt', 'r', encoding='utf-8')
        line = f.readline() # 类型: str;以行的形式进行读取文件
        list13 = []
        while line:
            a = line.split()
            b = a[2:4]  # 选取需要读取的位数
            list13.append(b) # 将其添加在列表之中
            line = f.readline()
        f.close()
        '''
        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile22 = incr1 + incr + incr2
        while wait(infile22) == False:
            time.sleep(0.01)
        print(infile22, "ok！")
        infile2 = np.array(loadDatadet(infile22))
        np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile2.txt', infile2)
        df2= pd.read_csv('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile2.txt',sep=" ",names=["% x2","y2","material2.u","material2.v"])
        '''
        f = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile2.txt', 'r', encoding='utf-8')
        line = f.readline() # 类型: str;以行的形式进行读取文件
        list23 = []
        while line:
            a = line.split()
            b = a[2:4]  # 这是选取需要读取的位数
            list23.append(b) # 将其添加在列表之中
            line = f.readline()
        f.close()
        '''
        df2['material2.u']=df1['material1.u']+df2['material2.u']
        df2['material2.v']=df1['material1.v']+df2['material2.v']

        '''
        outfile = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile3.txt', 'w',encoding='utf-8')       
        #for r in range(0, m):
            #df[list]=df[list13]+df[list23]

        #for r in list13:
            #outfile.write(str(round(infile1[r, 0]))).reshape(-1,1)
            #outfile.write(str(round(infile2[r, 1]))).reshape(-1,1)
            #outfile.write(list13[r+9])
            #print(result)
            #outfile.write(str(zip(round(infile1[r, 3]), round(infile2[r, 3])))).reshape(-1,1)
        outfile.close()    
        '''        
        np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile3.txt',df2)
        with open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile3.txt', 'r', encoding='utf-8') as f:
            dataset = f.read()  # 类型: str


        fh = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity.txt', 'w')
        for line in open(infile22, 'r'):
            a = line.split(' ')
            if a[0] == '%':
                fh.write(line)
        fh.write(dataset)
        fh.close()


        strint1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity"
        strint2 = str(timestep * (nstep + 1))
        strint3 = ".txt"
        shutil.copy('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity.txt', strint1 + strint2 + strint3)
        '''
        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocity"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile3 = incr1 + incr + incr2 
        infile3 = np.array(loadDatadet(infile3)) 
        '''

           
        ###———————————————————————10. 下一步的浓度输出文件（outcon）###################################

        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/outcon"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile=incr1+incr+incr2
        infile = np.array(loadDatadet(infile))


        ###———————————————————————11. 下一步的phreeqc输入文件—————————————————————##############################################

        np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/result.txt', phresult)


        input_string10 = """   """
    #溶液数据输入框架
        for i in range(0, m):
            input_string1 = """
                SOLUTION #
                    temp      56
                    pH        ### 
                    pe        #
                    redox     pe
                    units     mol/kgw
                    density   1
                    water    1
                    A         ###
                    B         ###
                    C         ###
                    D         ###
                    E         ###
                    F         ###
                    G         ###
                    H         ###
                    I         ###
                    J         ###
                    """

            ph = 7
            pe = 4

            for j in range(2, 13):
                if infile[i, j] < 0:
                   infile[i, j] = 0

        # print(ph, pe)

            incr = str(round(infile[i, 2], 10))
            str1 = 'pH        '
            incr = str1 + incr
            input_string11 = input_string1.replace('pH        ###', incr)

            incr = str(round(pe, 4))
            str1 = 'pe        '
            incr = str1 + incr
            input_string12 = input_string11.replace('pe        #', incr)
    
            # 修改 A
            incr = str(round(infile[i, 3], 10))
            # print(incr)
            str1 = 'Ca        '
            incr = str1 + incr
            input_string13 = input_string12.replace('A         ###', incr)
    
            # 修改 B
            incr = str(round(infile[i, 4], 10))
            str1 = 'C(4)        '
            incr = str1 + incr
            input_string14 = input_string13.replace('B         ###', incr)
        
            incr = str(round(infile[i, 5], 10))
            str1 = 'Al        '
            incr = str1 + incr
            input_string15 = input_string14.replace('C         ###', incr)
        
            incr = str(round(infile[i, 6], 10))
            str1 = 'Na        '
            incr = str1 + incr
            input_string16 = input_string15.replace('D         ###', incr)
        
            incr = str(round(infile[i, 7], 10))
            str1 = 'K        '
            incr = str1 + incr
            input_string17 = input_string16.replace('E         ###', incr)
            
            incr = str(round(infile[i, 8], 10))
            str1 = 'Fe(2)        '
            incr = str1 + incr
            input_string18 = input_string17.replace('F         ###', incr)
            
            incr = str(round(infile[i, 9], 10))
            str1 = 'Mg        '
            incr = str1 + incr
            input_string19 = input_string18.replace('G         ###', incr)
            
            incr = str(round(infile[i, 10], 10))
            str1 = 'S(6)        '
            incr = str1 + incr
            input_string20 = input_string19.replace('H         ###', incr)
            
            incr = str(round(infile[i, 11], 10))
            str1 = 'Si        '
            incr = str1 + incr
            input_string21 = input_string20.replace('I         ###', incr)
        
            incr = str(round(infile[i, 12], 10))
            str1 = 'Cl        '
            incr = str1 + incr
            input_string22 = input_string21.replace('J         ###', incr)
              
            incr = str(i + 1)
            str1 = 'SOLUTION '
            incr = str1 + incr
            input_string24 = input_string22.replace('SOLUTION #', incr)

            # 反应配置
            input_string10 = input_string10 + input_string24
        #动力学参数输入及输出框架
        input_string2 = """
            PHASES
            Pyrophyllite
                Al2Si4O12H2 + 6H+ + 4H2O = 2Al+3 + 4H4SiO4
                -analytical_expression -8979.387 -2.082858 444075.9 3366.644 -23685900 0.0005204115
                -Vm       128.04 cm3/mol
            Smectite_Ca
                Ca.165Mg0.33Al1.67Si4O12H2 + 6H+ + 4H2O = 1.67Al+3 + 0.165Ca+2 + 0.33Mg+2 + 4H4SiO4
                log_k     3.481
                -Vm       365.394 cm3/mol
            SELECTED_OUTPUT #
                -simulation           false
                -state                false
                -distance             false
                -time                 false
                -step                 false
                -pe                   false
                -totals               Al  C(4)  Ca  Cl  Fe(2)  K  Mg Na  S(6)  Si
                -saturation_indices    Calcite Quartz  Smectite_Ca  Pyrophyllite   Anorthite
            USER_PUNCH # 
                -headings Activity_H+
               -start
            10 PUNCH ACT("H+")
               -end                 
          End
                """

        # 修改输出
        incr = str(m)
        str1 = 'SELECTED_OUTPUT 1-'
        incr = str1 + incr
        input_string31 = input_string2.replace('SELECTED_OUTPUT #', incr)
    
        incr = str(m)
        str1 = 'USER_PUNCH 1-'
        incr = str1 + incr
        input_string32 = input_string31.replace('USER_PUNCH #', incr)

        input_string = input_string10 + input_string32



        phreeqc_result = selected_array(os.path.join(datpath, 'phreeqc.dat'), input_string)
    
        for jj in range(0, outn):
            for zz in range(1, m + 1):
                a = [entry[jj] for entry in phreeqc_result][zz:]
                phresult[zz - 1, jj] = float(a[0])



            ### ————————————————————11. 下一步的phreeqc的输出文件——————————————————------------------#####################


        for i in range(0, m):
            for k in range(0, n):
                infile[i, 2 + k] = phresult[i, 2 + k] * 1000 #将phreeqc的值赋给comsol，以及浓度单位修改
        for i in range(0, m):
            for k in range(0, n-11):
                infile[i, 12 + k] = phresult[i, 12 + k] #将phreeqc的值赋给comsol，饱和指数


        incr1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/outcon"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile11=incr1+incr+incr2


        np.savetxt('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile.txt', infile)


        with open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/infile.txt', 'r', encoding='utf-8') as f:
            dataset = f.read()  # type: str


        fh = open('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/initcon.txt', 'w')
        for line in open(infile11, 'r'):
            a = line.split(' ')
            if a[0] == '%':
                fh.write(line)
        fh.write(dataset)
        fh.close()

        strint1 = "F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/initcon"
        strint2 = str(int(timestep * (nstep + 1)))
        strint3 = ".txt"
        shutil.copy('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/initcon.txt', strint1 + strint2 + strint3)


        # 完成一个时间步
        print('finish %dstep Phreeqc' % (nstep + 1))
        print("-------------------------------------------------")

    # —————————————————————————over————————————————————————————————————————

    # os.system("draw.py")

    end00 = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('运行完毕！')
    print("用时:%.2fs" % (end00 - start))

