class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []
        for s in strs: 
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)



    def decode(self, s: str) -> List[str]:
    
      res = []
      
      startPtr = 0 
      
      while startPtr < len(s): 
      
        endPtr = startPtr
        
        # move forward pointer until # is found
        while s[endPtr] != '#': 
          endPtr += 1
        
        wordLen = int(s[startPtr: endPtr])
        
        startPtr = endPtr + 1
        endPtr = startPtr + wordLen
        
        res.append(s[startPtr:endPtr])
        
        startPtr = endPtr
      
      return res