
input1 = [[0,0,0,0,0,0,0],[0,3,1,3,8,2,0],[0,4,1,5,7,9,0],[0,2,1,4,5,0,0],[0,4,1,5,8,3,0],[0,3,1,4,7,2,0],[0,0,0,0,0,0,0]]
input2 = [[0,0,0,0,0,0,0],[0,5,4,1,3,8,0],[0,4,9,1,4,7,0],[0,7,3,1,4,6,0],[0,8,4,1,5,2,0],[0,2,3,1,8,2,0],[0,0,0,0,0,0,0]]
input3 = [[0,0,0,0,0,0,0],[0,2,2,3,7,3,0],[0,6,9,4,4,5,0],[0,1,1,1,1,1,0],[0,8,3,4,5,5,0],[0,7,2,3,1,4,0],[0,0,0,0,0,0,0]]

verticalMask = [[-1,0,1],[-2,0,2],[-1,0,1]]
horizontalMask = [[1,2,1],[0,0,0],[-1,-2,-1]]

def compute(input,filter,output):
    process = len(input)-len(filter)+1
    
    for offsetVertical in range(process):
        for offsetHorizontal in range(process):
            number = 0
            for i in range(len(filter)):
                for j in range(len(filter)):
                    number += filter[i][j]*input[i+offsetVertical][j+offsetHorizontal]
            output[offsetVertical][offsetHorizontal] += number

def main():
    print "The first vertical mask: "
    output1 = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
    compute(input1,verticalMask,output1)
    compute(input2,verticalMask,output1)
    compute(input3,verticalMask,output1)
    print output1
    print "The second horizontal mask: "
    output2 = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
    compute(input1,horizontalMask,output2)
    compute(input2,horizontalMask,output2)
    compute(input3,horizontalMask,output2)
    print output2
                
main()
