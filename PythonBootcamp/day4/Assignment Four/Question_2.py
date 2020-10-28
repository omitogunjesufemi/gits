MILES = 1
KILOMETERS = 20
print(f""" 
Miles       Kilometers  |   Kilometers      Miles
""")
while (MILES < 11) and (KILOMETERS < 66):
    kilometers = MILES * 1.609
    miles = KILOMETERS / 1.609
    print(f"""
{MILES:<4.0f}         {kilometers:<9.3f}  |   {KILOMETERS:>9.3f}  {miles:>11.3f}
    """)
    MILES += 1
    KILOMETERS += 5