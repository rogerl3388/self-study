def add_time(start: str, duration: str, day = '') -> str:
    # Input format:
    #    start: 'hh:mm AM' or 'hh:mm PM'
    #    duration: 'hh:mm'
    #    day (optional): name of day of week (not case sensitive)
    # output: 'hh:mm AM/PM, [day of week] (next day/n days later)
    day_string = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    start_min_count = int(start[-5:-3]) + int(start[:-6]) % 12 * 60
    if start[-2:] == 'PM':
        start_min_count += 12*60
    end_min_count = start_min_count + int(duration[-2:]) + int(duration[:-3])*60
    
    new_min = str(end_min_count % 60)
    if len(new_min) == 1:
        final_min = '0' + new_min
    else:
        final_min = new_min
    
    new_hour = end_min_count // 60
    day_count = new_hour // 24
    final_hour = new_hour % 12
    if final_hour == 0:
        final_hour = 12
    
    if new_hour % 24 < 12:
        final_noon = 'AM'
    else:
        final_noon = 'PM'

    new_time = f'{final_hour}:{final_min} {final_noon}'

    if day.lower() in day_string:
        day_num = day_string.index(day.lower())
        new_day_index = (day_num + day_count) % 7
        final_day = day_string[new_day_index]
        new_time += f', {final_day.capitalize()}'


    if day_count == 1:
        new_time += ' (next day)'
    elif day_count > 1:
        new_time += f' ({day_count} days later)'

    return new_time

print(add_time('2:59 AM', '24:00', 'saturDay'))