print( "Welcome to the tip calculator!" )
bill= float( input( "What was the total bill? " ) )
tip = int( input( "How much tip would you tike to give? 10, 12,15 or 20"))
people = int( input( "How many people to split the billls ? "))

final_amount = (bill+tip) /people
print(f"Each persons want to pay  {final_amount}")