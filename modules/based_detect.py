from machine import Pin, Signal, I2C, ADC, Timer
import time

def push_based(analog_pin):
    adc = ADC(Pin(analog_pin))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    Data_based = adc.read()
    return Data_based

def Detect_beat(analog_pin,out_pin):
    adc = ADC(Pin(analog_pin))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)

    v = adc.read()
    print (v)
    Threshold = 2500

    if v > Threshold:
        Pin(out_pin, Pin.OUT).value(1)
    if v < Threshold:
        Pin(out_pin, Pin.OUT).value(0)
    
