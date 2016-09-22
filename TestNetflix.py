from Netflix import *
from unittest import main, TestCase
import urllib.request
import pickle

def cutFile(filename, start, end):
    r = open(filename, "rt")
    w = open("cut.txt","w")
    for i in range(start):
        r.readline()
    linein = r.readline().strip("\n")
    numLeft = end-start
    while(linein!="" and linein!=-1 and linein is not None and not linein.endswith(":")):
        linein = r.readline().strip("\n")
    w.write(linein + "\n")
    numWritten = 0
    try:
        for i in range(numLeft):
            w.write(r.readline())
            numWritten += 1
    except:
        print(numWritten)
    w.close()
    r.close()


class TestNetflix(TestCase): #I am copying this off of testcollatz so...


    def test_linreg(self):
        x = [1,2,3,4,5]
        y = [0,-2,-3,-4,-5]
        desired = 1
        avg = -3
        val = linRegError(x,y,desired,avg)
        self.assertEqual(2.59999996-(2.59999996%0.1), val - (val%0.1))

    def test_linreg_2(self):
        x = [1,2,3,4,5,6,7,8,9,10]
        y = [10,9,8,7,6,5,4,3,2,1]
        desired = 5
        avg = 0
        val = linRegError(x,y,desired,avg)
        self.assertEqual(val, 6)
        
    def test_linreg_3(self):
        x = [1,2,3,4,5,6,7,8,9,10]
        y = [1,1,1,1,1,1,1,1,1,1]
        desired = 5
        avg = 1
        val = linRegError(x,y,desired,avg)
        self.assertEqual(val, 0)

 

    def test_netflix_eval_1(self):
        r2 = open("probe.txt", "rt")
        w = open("probeOut.txt", "w")
        netflix_eval(r2,w)
        r2.close()
        w.close()

    
        r = open("probe.txt", "rt")
        fout = open("probeOut.txt", "rt")
        self.assertEqual(len(r.readlines()),len(fout.readlines()))
        r.seek(0)
        fout.seek(0)
        
        err = 0
        num = 0
        linein = r.readline().strip("\n")
        fout.readline() # skip movie on output
        actualRaw = urllib.request.urlopen("http://www.cs.utexas.edu/users/downing/netflix-cs373/cat3238-actual.p")
        actuals = pickle.load(actualRaw)
        while(linein!=-1 and linein and linein!=""):
            
            movie = int(linein.strip(":"))
            linein = r.readline().strip("\n")
            #print(linein)
            #input()
            try:
                outVal = float(fout.readline().strip("\n"))
            except:
                print("Missed expected output value")
            while(linein!="" and linein is not None and linein!=-1 and not linein.endswith(":")):
                realVal = None
                customer = int(linein.split(",")[0])
                temp = actuals.get(movie)
                realVal = temp.get(customer)
                if(realVal is not None and outVal is not None):
                    #print("HSOUL DINC NUM")
                    err += (realVal-outVal)**2
                    num += 1
                else:
                    print("Unable to match output to actual")
                linein = r.readline().strip("\n")
                outVal = None
                try:
                    outVal = float(fout.readline().strip("\n").strip(":"))
                except:
                    pass #we expect this to whiff once, and not cause issues.
        meanErr = err / num
        RMSE = meanErr ** 0.5
        r.close()
        fout.close()

        self.assertLess(RMSE,1)

    def test_netflix_eval_2(self):
        cutFile("probe.txt" , 1000, 3000)
        r2 = open("cut.txt", "rt")
        w = open("probeOut.txt", "w")
        netflix_eval(r2,w)
        r2.close()
        w.close()

    
        r = open("cut.txt", "rt")
        fout = open("probeOut.txt", "rt")
        self.assertEqual(len(r.readlines()),len(fout.readlines()))
        r.seek(0)
        fout.seek(0)
        
        err = 0
        num = 0
        linein = r.readline().strip("\n")
        fout.readline() # skip movie on output
        actualRaw = urllib.request.urlopen("http://www.cs.utexas.edu/users/downing/netflix-cs373/cat3238-actual.p")
        actuals = pickle.load(actualRaw)
        while(linein!=-1 and linein and linein!=""):
            
            movie = int(linein.strip(":"))
            linein = r.readline().strip("\n")
            #print(linein)
            #input()
            try:
                outVal = float(fout.readline().strip("\n"))
            except:
                print("Missed expected output value")
            while(linein!="" and linein is not None and linein!=-1 and not linein.endswith(":")):
                realVal = None
                customer = int(linein.split(",")[0])
                temp = actuals.get(movie)
                realVal = temp.get(customer)
                if(realVal is not None and outVal is not None):
                    #print("HSOUL DINC NUM")
                    err += (realVal-outVal)**2
                    num += 1
                else:
                    print("Unable to match output to actual")
                linein = r.readline().strip("\n")
                outVal = None
                try:
                    outVal = float(fout.readline().strip("\n").strip(":"))
                except:
                    pass #we expect this to whiff once, and not cause issues.
        meanErr = err / num
        RMSE = meanErr ** 0.5
        r.close()
        fout.close()

        self.assertLess(RMSE,1)

    def test_netflix_eval_3(self):
        cutFile("probe.txt" , 3000, 5000)
        r2 = open("cut.txt", "rt")
        w = open("probeOut.txt", "w")
        netflix_eval(r2,w)
        r2.close()
        w.close()

    
        r = open("cut.txt", "rt")
        fout = open("probeOut.txt", "rt")
        self.assertEqual(len(r.readlines()),len(fout.readlines()))
        r.seek(0)
        fout.seek(0)
        
        err = 0
        num = 0
        linein = r.readline().strip("\n")
        fout.readline() # skip movie on output
        actualRaw = urllib.request.urlopen("http://www.cs.utexas.edu/users/downing/netflix-cs373/cat3238-actual.p")
        actuals = pickle.load(actualRaw)
        while(linein!=-1 and linein and linein!=""):
            
            movie = int(linein.strip(":"))
            linein = r.readline().strip("\n")
            #print(linein)
            #input()
            try:
                outVal = float(fout.readline().strip("\n"))
            except:
                print("Missed expected output value")
            while(linein!="" and linein is not None and linein!=-1 and not linein.endswith(":")):
                realVal = None
                customer = int(linein.split(",")[0])
                temp = actuals.get(movie)
                realVal = temp.get(customer)
                if(realVal is not None and outVal is not None):
                    #print("HSOUL DINC NUM")
                    err += (realVal-outVal)**2
                    num += 1
                else:
                    print("Unable to match output to actual")
                linein = r.readline().strip("\n")
                outVal = None
                try:
                    outVal = float(fout.readline().strip("\n").strip(":"))
                except:
                    pass #we expect this to whiff once, and not cause issues.
        meanErr = err / num
        RMSE = meanErr ** 0.5
        r.close()
        fout.close()

        self.assertLess(RMSE,1)

        


if __name__ == "__main__" :
    main()
