# Creating enumerations
from enum import Enum

class Schools(Enum):
    EMAp = 1
    EBAPE = 2
    EPGE = 3
    CPDOC = 4
    DIREITO_RIO = 5
    
print(Schools.EMAp)
print(Schools.EMAp.name)
print(Schools.EMAp.value)
print(type(Schools))
print(type(Schools.EMAp))
print(list(Schools))

print('\n\n')
print(Schools.CPDOC == Schools.DIREITO_RIO)

school = Schools.EMAp

if school is Schools.EMAp:
    print('I\'m from EMAp', '\n\n\n\n\n')
    
# Creating Exceptions
class GoneWrongError(ZeroDivisionError):
    pass

def test():
    raise GoneWrongError()
    
try:
    test()
except GoneWrongError:
    print('At least we tried...')