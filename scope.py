
x  = "global x" # global scope
def function():
    x = "local x" # local scope
    print(x)
function()
print(x)