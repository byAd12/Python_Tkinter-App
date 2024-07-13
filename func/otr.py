import random, sys, string, calendar
#############################################################################################
def contra(long):
    contra = "".join(random.choices(string.ascii_letters + string.digits + "-" + "_" + "!", k=int(long)))
    print(contra)

def cal(año, mes):
    print(calendar.month(int(año), int(mes)))
#############################################################################################
if str(sys.argv[1]) == "func1":
    contra(str(sys.argv[2]))
if str(sys.argv[1]) == "func2":
    cal(str(sys.argv[2]), str(sys.argv[3]))