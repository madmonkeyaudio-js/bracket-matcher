def bracket_matcher(my_input):
  start = ["[","{","("] 
  close = ["]","}",")"] 
  stack = [] 
  for i in my_input: 
      if i in start: 
          stack.append(i) 
      elif i in close: 
          position = close.index(i) 
          if ((len(stack) > 0) and (start[position] == stack[len(stack)-1])): 
              stack.pop() 
          else: 
              return False
  if len(stack) == 0: 
      return True


print(bracket_matcher('abc(123)'))
# returns true

print(bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns true

print(bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print(bracket_matcher('()'))
# returns true

print(bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched

