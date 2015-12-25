values = []
while len(values) < 3:
  try:
    value = int( input( 'Enter a number:\n' ) )
    values.append( value )
  except ValueError:
    print( '\t\t\t\tInvalid Number!!!!' )

values.sort()
print( values )
print( sum(values) )
