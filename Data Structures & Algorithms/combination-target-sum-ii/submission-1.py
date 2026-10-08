class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []


        def backtrack(start,path,total):

            if total == target and sorted(path) not in res:
                res.append(sorted(path.copy()))
                return

            if total > target:
                return

            
            for i in range(start,len(candidates)):
                
                path.append(candidates[i])

                backtrack(i+1,path,total + candidates[i])

                path.pop()

        backtrack(0,[],0)
        return res


        