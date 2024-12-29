from basics import *
s = Samples

def scree(freq, dur):
    return fade_in_lin(fade_out_lin(s.saww(freq,dur),.25),0.1)

major = [0,2,4,5,7,9,11,12]
minor = [0,2,3,5,7,8,10,12]

a = (13, 1/2)
b = (14, 1/2)
rest = (None,1/2)
x = line((rest,a,a,a,a,a,a,rest,b,b,b,a,a,a,a,rest),scree)
y = line(((-36,1/2),(None,1/2))*8,s.drum)
write_wav((x+y)/2,'classic')

write_wav(fade_in_lin(fade_out_lin(s.white(None,10),4),4),'ocean')

def zap(freq, dur):
    voice = [1]*20
    return sum(voice[i]*s.sine(freq*(i+1), dur) for i in range(len(voice)))/sum(voice)

write_wav(np.concatenate([fade_out_lin(zap(note(n), 1/4),1/16) for n in major]),'major')
write_wav(np.concatenate([fade_out_lin(zap(note(n), 1/4),1/16) for n in minor]),'minor')
