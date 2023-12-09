import pysinewave, time, random

d2pitches = [4, 5, 7]
lpitches = [[7, 9], [9, 10], [10, 12]]
shift = random.randint(-12,12)

def main():
    droan1 = pysinewave.SineWave(shift,1)

    droan1.play()

    droan2 = pysinewave.SineWave(0,4)

    d2i = 0

    lead = pysinewave.SineWave(0, 10)

    while True:
        d2i = random.randint(0,2)
        droan2.set_pitch(d2pitches[d2i]+shift)
        droan2.play()
 
        for i in range(0,random.randint(0,5)):
            lead_p = random.choice(lpitches[d2i])+shift
            lead.set_pitch(lead_p)
            lead.play()
            print(shift, d2pitches[d2i]+shift, lead_p)
            time.sleep(random.uniform(0.1,2))


main()