# Problem: Up and Down
# Language: GolfScript
# Author: KirarinSnow
# Usage: golfscript.rb thisfile.gs <input.in >output.out
# Comments: Large may take slightly too long.


# 57 bytes

n%(~,{"Case #"\)@": "\(;([~][.${[]+/.{,,}%~&\~+}/])*,n@}/
