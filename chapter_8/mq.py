import random, time
import pyinputplus as p

numques = 10
correct = 0 
for quesnum in range(1,numques+1):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s * %s : '  %(quesnum, num1, num2)
    try:
# Right answers are handled by allowRegexes.
# Wrong answers are handled by blockRegexes, with a custom message. 
        p.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except p.TimeoutException:
        print("TIME LIMIT EXCEEDED!")
    except p.RetryLimitException:
        print("MAX LIMIT OF ATTEMPT REACHED!")
    else:
        print("CORRECT ANSWER!")
        correct += 1
    time.sleep(1)
    print('Score : %s/%s' %(correct,numques))

