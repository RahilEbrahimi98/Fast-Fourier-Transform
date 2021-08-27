import cmath
import math
import matplotlib.pyplot as plt
import numpy as np

def powerTwo(pointsArray):
    while len(pointsArray) & (len(pointsArray) - 1) != 0:
        pointsArray.append(0)
    return pointsArray

def reverseBits(currentNumber, totalBits):
    result = 0
    for i in range(totalBits):
        if (currentNumber >> i) & 1:
            result |= 1 << (totalBits - 1 - i)
    return result

def reorderPoints(pointsArray, number):
    result = [None] * number
    for i in range(number):
        result[i] = pointsArray[reverseBits(i, int(math.log2(number)))]
    return result

def FFT(pointsArray, number):
    pointsArray = powerTwo(pointsArray)
    number = len(pointsArray)
    pointsArray = reorderPoints(pointsArray, number)
    stage = 1 
    while (stage != number): 
        w = math.e ** (-1j * math.pi / stage)
        flag = False 
        counter = 0 
        temp = [x for x in pointsArray] 
        for i in range(number): 
            if counter == stage: 
                flag = not(flag) 
                counter = 0 
            if flag == False: 
                pointsArray[i] = (w ** (i % stage)) * temp[i + stage]  + temp[i]
                counter += 1 
            else: 
                pointsArray[i] = temp[i - stage] - (w ** (i % stage)) * temp[i] 
                counter += 1 
        stage *= 2 
    return pointsArray

def plot(pointsArray):
    ##my result
    result = FFT(pointsArray, len(pointsArray))
    absResult = [abs(x) for x in result]
    print("my ans is: ")
    print(result)
    phaseResult = [cmath.phase(x) for x in result]
    plt.subplot(5, 1, 1) 
    plt.title('X[n]') 
    plt.plot([x for x in range(len(pointsArray))], pointsArray, 'og') 
    plt.subplot(5, 1, 2) 
    plt.title('FFT abs') 
    plt.xlabel('w abs') 
    plt.ylabel('|H(e^jw)|') 
    plt.plot([x for x in range(len(pointsArray))], absResult, 'r') 
    plt.subplot(5, 1, 3) 
    plt.title('FFT phase') 
    plt.xlabel('w phase') 
    plt.ylabel('phase H(e^jw)') 
    plt.plot([x for x in range(len(pointsArray))], phaseResult, 'r')
    plt.subplot(5, 1, 4)
    plt.title('FFT real') 
    plt.xlabel('w ') 
    plt.ylabel('real')
    resultreal=[np.real(x) for x in result]
    plt.plot([x for x in range(len(pointsArray))], resultreal, 'g')
    plt.subplot(5, 1, 5)
    plt.title('FFT image') 
    plt.xlabel('w ') 
    plt.ylabel('image')
    resultimage=[np.imag(x) for x in result]
    plt.plot([x for x in range(len(pointsArray))], resultimage, 'g')
    plt.show()
    
    ##python result:
    
#     result = np.fft.fft(pointsArray)
#     absResult = [abs(x) for x in result]
#     print("python ans is: ")
#     print(result)
#     phaseResult = [cmath.phase(x) for x in result]
#     plt.subplot(5, 1, 1) 
#     plt.title('X[n]') 
#     plt.plot([x for x in range(len(pointsArray))], pointsArray, 'og') 
#     plt.subplot(5, 1, 2) 
#     plt.title('FFT abs') 
#     plt.xlabel('w abs') 
#     plt.ylabel('|H(e^jw)|') 
#     plt.plot([x for x in range(len(pointsArray))], absResult, 'r') 
#     plt.subplot(5, 1, 3) 
#     plt.title('FFT phase') 
#     plt.xlabel('w phase') 
#     plt.ylabel('phase H(e^jw)') 
#     plt.plot([x for x in range(len(pointsArray))], phaseResult, 'r')
#     plt.subplot(5, 1, 4)
#     plt.title('FFT real') 
#     plt.xlabel('w ') 
#     plt.ylabel('real')
#     resultreal=[np.real(x) for x in result]
#     plt.plot([x for x in range(len(pointsArray))], resultreal, 'g')
#     plt.subplot(5, 1, 5)
#     plt.title('FFT image') 
#     plt.xlabel('w ') 
#     plt.ylabel('image')
#     resultimage=[np.imag(x) for x in result]
#     plt.plot([x for x in range(len(pointsArray))], resultimage, 'g')
#     plt.show()


#print(np.fft.fft([1,2,3,4,4,3,2,1]))
# plot([1,2,3,4,4,3,2])
#print(np.fft.fft([math.sin(x) for x in range(8)]))

# 
inputt = [math.sin(x) for x in range(1024)]
input2=[1,2,3,4,5]
plot(inputt)