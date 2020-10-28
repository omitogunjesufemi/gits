   
def main(): 
    start_mile = read_input("Enter the start mile: ")
    end_mile = read_input("Enter the end mile: ")
    mile_step = read_input("Enter the mile step: ")
    start_kilometer = read_input("Enter the start kilometer: ")
    end_kilometer = read_input("Enter the end kilometer: ")
    kilometer_step = read_input("Enter the kilometer step: ")
    
    header()
    while start_mile <= end_mile or start_kilometer <= end_kilometer :
        kilometer_from_mile = conversion_kilometer_from_mile(start_mile)
        mile_from_kilometer = conversion_mile_from_kilometer(start_kilometer)
        mile_text = miles_text(start_mile)
        kilometer_from_mile_text = f"{kilometer_from_mile:.3f}".ljust(10)
        kilometer_text = kilometers_text(start_kilometer)
        mile_from_kilometer_text = f"{mile_from_kilometer:.3f}"
        line = f"{mile_text}{kilometer_from_mile_text}|   {kilometer_text}  {mile_from_kilometer_text}"
        
        
        if (start_mile == end_mile) and (start_kilometer != end_kilometer):
            start_mile = "   "
            kilometer_from_mile = "   "
            mile_from_kilometer = conversion_mile_from_kilometer(start_kilometer)
            mile_text = miles_text_empty(start_mile)
            kilometer_from_mile_text = f"{kilometer_from_mile}".ljust(10)
            kilometer_text = kilometers_text(start_kilometer)
            mile_from_kilometer_text = f"{mile_from_kilometer}"
            line = f"{mile_text}{kilometer_from_mile_text}|   {kilometer_text}  {mile_from_kilometer_text}"
            print(line)
            start_kilometer = start_kilometer + kilometer_step
            
            
        
        elif (start_mile != end_mile) and (start_kilometer == end_kilometer):
            start_kilometer = "   "
            kilometer_from_mile = conversion_kilometer_from_mile(start_mile)
            mile_from_kilometer = "  "
            mile_text = miles_text(start_mile)
            kilometer_from_mile_text = f"{kilometer_from_mile}".ljust(10)
            kilometer_text = kilometers_text_empty(start_kilometer)
            mile_from_kilometer_text = f"{mile_from_kilometer}"
            line = f"{mile_text}{kilometer_from_mile_text}|   {kilometer_text}  {mile_from_kilometer_text}"
            print(line)
            start_mile = start_mile + mile_step
            
        
        else:
            print(line)
            start_mile += mile_step
            start_kilometer += kilometer_step


def miles_text_empty(miles):
    return f"{miles}".ljust(10)

def kilometers_text_empty(kilometers):
    return f"{kilometers}".ljust(10)


def miles_text(miles):
    return f"{miles:d}".ljust(10)

def kilometers_text(kilometers):
    return f"{kilometers:d}".ljust(10)

def conversion_kilometer_from_mile(miles):
    return miles * 1.609

def conversion_mile_from_kilometer(kilometers):
    return kilometers / 1.609

def header():
    print("Miles   Kilometers  |   Kilometers  Miles")

def read_input(prompt):
    return int(input(prompt))

main()