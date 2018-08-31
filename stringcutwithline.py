#（上海分行的需求）
#输入：result.txt文件
#输出：切割好的多个文件，以每行的固定编号命名（具体可以修改），后缀名字.txt
def find_string(s,t):
    try:
        nPos=s.index(t)
        return nPos
    except(ValueError):
        return -1
#“result文件所在的位置”
infilename="C:\\Users\\41951\\Desktop\\result.txt"
inputfile = open(infilename, 'r', encoding="utf-8")
lines=inputfile.readlines()
findstartindex='"w"'
findendindex='"wb"'
for line in lines:
    nstartPos=find_string(line,findstartindex)
    nendPos = find_string(line, findendindex)
    if nstartPos!=-1 and nendPos!=-1:
        # print(nstartPos)
        # print(nendPos)
        code=line[87:113]
        print(code)
        #输出文件写出的位置
        name='C:\\Users\\41951\\Desktop\\'+line[19:82]+'+'+code+'.txt'
        file_out=open(name,'w', encoding="utf-8")
        str=line[nstartPos+5:nendPos-2]
        file_out.write(str)
        file_out.close()
    else:
        continue

