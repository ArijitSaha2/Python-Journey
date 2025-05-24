# Print pattern:
'''
    *
   * *       Use recursion only—no loops.
  * * *
 * * * *   '''

def star(n, total = 4):
    if n > total:
        return
    print(" "*(total - n) + "* " * n)
    star(n + 1, total)
    
star(1)