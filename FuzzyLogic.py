def fuzzy_logic(temperature, humidity):

    #Inference

    def temp_low(x):
        if x <= 25: return 1
        elif x > 25 and x < 50: return (50 - x)/25
        else : return 0
    
    def temp_med(x):
        if x <= 25 or x >= 75: return 0
        elif x > 25 and x <= 50: return (x - 25)/25
        elif x > 50 and x < 75: return (75 - x)/25
    
    def temp_high(x):
        if x <= 50: return 0
        elif x > 50 and x < 75: return (x - 50)/25
        else : return 1

    def humid_low(x):
        if x <= 25: return 1
        elif x > 25 and x < 50: return (50 - x)/25
        else : return 0
    
    def humid_med(x):
        if x <= 25 or x >= 75: return 0
        elif x > 25 and x <= 50: return (50 - x)/25
        elif x > 50 and x < 75: return (75 - x)/25
    
    def humid_high(x):
        if x <= 50: return 0
        elif x > 50 and x < 75: return (x - 50)/25
        else : return 1
    
    #DeFuzzyfication

    def fan_speed_low():
        return (temp_low(temperature) + humid_low(humidity))/2
        
    
    def fan_speed_med():
        return (temp_med(temperature) + humid_med(humidity))/2
    
    def fan_speed_high():
        return (temp_high(temperature) + humid_high(humidity))/2
    
    return [fan_speed_low(), fan_speed_med(), fan_speed_high()]

if __name__ == '__main__':
    temps = [23, 45, 56, 78]
    humids = [56, 45, 78, 78]
    for t, h in zip(temps, humids):
        result = fuzzy_logic(t, h)
        print(f'For Temperature : {t} and Humidity : {h}')
        print(f'Fan Speed --> Low : {result[0]}, Medium : {result[1]}, High : {result[-1]}')