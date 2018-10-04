regex_pattern = r""	# Do not delete '
import re
print(*re.split(r'[.,]+', input().strip('., ')), sep='\n')