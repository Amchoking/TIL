class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start=0
        end=0
        answer=[]
        for i in range(len(intervals)):
            if(i==0):
                start=intervals[i][0]
                end=intervals[i][1]
            else:
                if(intervals[i][0]>end):
                    answer.append([start,end])
                    start=intervals[i][0]
                    end=intervals[i][1]
                else:
                    end=max(end,intervals[i][1])
        answer.append([start,end])
        return answer
