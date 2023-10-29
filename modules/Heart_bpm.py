from machine import Pin, ADC
import time


def detect_bpm(INPUT_pin):
    sensor_pin = ADC(Pin(INPUT_pin))
    sensor_pin.atten(ADC.ATTN_11DB)
    sensor_pin.width(ADC.WIDTH_12BIT)

    def read_heart_rate():
        raw_value = sensor_pin.read()
        #print(raw_value)
        heart_rate = map_value(raw_value, 0, 4095, 0, 200)
        return heart_rate

    def map_value(value, from_low, from_high, to_low, to_high):
        return (value - from_low) * (to_high - to_low) // (from_high - from_low) + to_low

    # สร้างรายการเพื่อเก็บค่า Heart Rate
    heart_rate_list = []

    while True:
        heart_rate = read_heart_rate()
        heart_rate_list.append(heart_rate)  # เพิ่มค่า Heart Rate ลงในรายการ
        #print("Heart Rate:", heart_rate)

        # หากมี 10 ค่าในรายการแล้ว
        if len(heart_rate_list) == 2000:
            average_heart_rate = sum(heart_rate_list) / len(heart_rate_list)  # หาค่าเฉลี่ย
            average_heart_rate = round(average_heart_rate, 2)
            #print("Average Heart Rate (last 10 readings):", average_heart_rate)
            heart_rate_list = []  # ลบข้อมูลในรายการเพื่อเตรียมรับค่าใหม่
            return (average_heart_rate)
        #time.sleep(0.01)