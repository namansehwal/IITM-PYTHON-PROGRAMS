def max_elem(M):

   parent = list()
   for x in M:
        parent.extend(x)
   
   mode  = max(parent)

   for r in M:    
         for c in r:
              print(c)
              if c == mode:
                return (M.index(r), r.index(c))


