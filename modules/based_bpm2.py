from machine import Pin, ADC
import time


bpm = 0
def detect_bpm(INPUT_pin):
    adc = ADC(Pin(INPUT_pin))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    v = adc.read()




   