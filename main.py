#-*- coding: utf-8 -*-
import os

#know how many fo in pwd
out_ls = os.popen("ls").read().split("\n")
fo_list = []
Webp_pwd = []
global_workingpath = ""
rapwd = os.popen("pwd").read().split("\n")
print("Drag your Webp_Folder in ")
global_workingpath = raw_input()
print("The Webp Path = " + global_workingpath)

def commadn_dir(output):
    tmplist = []
    for b in output:
        tmplist.append(b)
    return tmplist 

def loop_cd(list_pwd):
    tmp = list_pwd
    if ".png" in tmp[0]:
        Webp_pwd.append(os.popen("pwd").read().split("\n")[0])

    else:
        for x in tmp:
            #print("Trying "+x)
            try:
                os.chdir(x)
                print("cd to "+x)
                tmp_ls = os.popen("ls").read().split("\n")
                loop_cd(commadn_dir(tmp_ls))
                print("is end")
                os.chdir("..")
            except:
                continue
    

    return None

def callingWebp(path):
    workingpath = global_workingpath
    nowpath = path
    javacommand = "java -jar " + workingpath + "/webpgen.jar" + " " + path + " 80 5-8"
    print("Starting Java jobs at "+path+"with command = "+ javacommand)
    
    os.system(javacommand)

fo_list = commadn_dir(out_ls)
#now in pwd

os.chdir("..")
for b in fo_list:
    loop_cd([b])
    print("back to raw" + rapwd[0])
    os.chdir(rapwd[0])


#Now doing Webp
print("Now doing Webp")

for y in Webp_pwd:
    os.chdir(global_workingpath)
    print("Cal in "+y)
    callingWebp(y)




