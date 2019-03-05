'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        candidates.sort()
        def findCandidates(target,index,temp,output):
            if target == 0 and temp not in output:
                output.append(temp)
                return
            if target < 0:
                return
            for i in range(index,len(candidates)):
                findCandidates(target-candidates[i],i+1,temp+[candidates[i]],output)
        findCandidates(target,0,[],output)
        return output
