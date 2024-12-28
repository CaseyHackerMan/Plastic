from basics import *

def note(freq, dur):
    return fade_in_lin(fade_out_lin(s_saww(freq,dur),.25),0.1)

a = note(900, .5)
b = note(953.5, .5)
rest = np.zeros(d2s(.5))
x = np.concatenate((rest,a,a,a,a,a,a,rest,b,b,b,a,a,a,a,rest))
write_wav(x)

write_wav(fade_in_lin(fade_out_lin(s_white(10),4),4),'ocean')