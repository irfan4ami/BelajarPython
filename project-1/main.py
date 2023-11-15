import os
import function
from function import color



if not os.path.exists('token'):
        os.makedirs('token', 0o777, exist_ok=True)


function.menu()

