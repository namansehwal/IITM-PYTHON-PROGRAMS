def max_elem(M):

   parent = list()
   for x in M:
        
        parent.extend(x)
   
  # [2, 8, 2, 3, 8, 7, 2, 8, 8, 3, 2, 3]
   mode  = max(parent)

   for r in M:
         
         for c in r:
              print(c)
            #   if c == mode:
            #     return (M.index(r), r.index(c))


max_elem([[2, 8, 2, 3], [8, 7, 2, 8], [8, 3, 2, 3]])