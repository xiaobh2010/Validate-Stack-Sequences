class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed)==0 or len(popped)==0:
            return len(pushed)==0 and len(popped)==0
        if pushed==popped:
            return True
        l=[]
        while len(pushed)>0 or len(popped)>0:
            if len(l)==0:
                l.append(pushed.pop(0))
            else:
                if l[-1]!=popped[0]:
                    if len(pushed)==0:
                        return False
                    l.append(pushed.pop(0))
                else:
                    l.pop()
                    popped.pop(0)
        return len(l)==0
        
        
