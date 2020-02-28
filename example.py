#Lets start by importing some useful libraries.
import numpy as np
import sys, math, getopt


def read(filename):
    #Set up some arrays to store the data we read in.
    results = []
    header = []

    #First we open the file. We can refer to the file at any point using its variable name we assigned here (f).
    with open(filename, encoding='utf8') as f:

        #First line is the header so lets pull that out of the data set and save for later.
        header = np.array(f.readline().strip().split(","))

        #Now we iterate through the file one line at a time.
        for line in f:
            #line.strip().split() first removes whitespace and then splits the line into an array based off the delimiter.
            row = line.strip().split(",")
            
            #Now for a given row we need to mark missing data and convert the strings to numbers.
            for i in range(len(row)):
                if(row[i] == "?"):
                    row[i] = -1
                else:
                    row[i] = float(row[i])

            #We save the current line to our results vector before continuing.
            results.append(np.array(row))

    #We have now read in the entire data set and we want to return what we got
    return header, np.array(results)


def dataManipulation(header, data):
    print(header)
    print(data)
    print(np.shape(data))

    #Lets delete the two columns that had a lot of missing data points. 
    #print(data[:,26], data[:,27]) #This will show you that column 26 and 27 are mostly empty.
    print()
    print("The following is pre and post column deletion")
    print(data[0])
    data = np.delete(data, [26, 27], 1)
    print(data[0])

    print()
    print("Before:")
    for label in range(len(header)):
        if label > 23 and label < 30:
            print(header[label])

    header = np.delete(header, [26, 27], 0)

    print()
    print("After:")
    for label in range(len(header)):
        if label > 23 and label < 28:
            print(header[label])



def output(filename, data):
    np.savetxt(filename, data, delimiter=",", fmt="%1.2f")




def main(argv):
    opts, args = getopt.getopt(argv, "hi:o:", ['input=', "output="])
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: IntroToPy -i <input_filename> -o <output_filename>")
            sys.exit(1)
        elif opt in ('-i', '--input'):
            inputFilePath = arg
        elif opt in ('-o', '--output'):
            outputFilePath = arg

    #Now that we have parsed arguments, lets run the program!
    header, data = read(inputFilePath)
    
    #We will use a function to manipulate the data.
    dataManipulation(header, data)

    #We can write the data back to a file.
    output(outputFilePath, data)













##You dont need to worry about this section.
#Basically this just allows the script to be run in a similar manner to a C++ program which is what im a bit more used to.
if __name__ == '__main__':
    main(sys.argv[1:])  